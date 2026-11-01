"""Build a reproducible A–F evidence audit; missing evidence always fails calibration.

Internal invariants, a source URL and in-sample calibration are three different
things. This report never upgrades an unchecked estimate to an empirical PASS.
"""
from collections import Counter,defaultdict
import csv,json,math
from pathlib import Path
from statistics import mean
import subprocess,sys
import yaml
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from policyshock.config import ROOT
from policyshock.engine.simulate import simulate
from policyshock.policies.loader import registry
from policyshock.policies.coverage import company_coverage


def ranks(values: list[float]) -> list[float]:
    """Return average ranks, including ties, without an external stats dependency."""
    order=sorted(range(len(values)),key=lambda i:values[i]);out=[0.]*len(values)
    start=0
    while start<len(order):
        end=start+1
        while end<len(order) and values[order[end]]==values[order[start]]:end+=1
        for j in range(start,end):out[order[j]]=(start+1+end)/2
        start=end
    return out


def spearman(x: list[float], y: list[float]) -> float | None:
    """Compute tie-corrected Pearson correlation of ranks for at least five observations."""
    if len(x)<5 or len(x)!=len(y):return None
    a,b=ranks(x),ranks(y);am,bm=mean(a),mean(b)
    denom=math.sqrt(sum((v-am)**2 for v in a)*sum((v-bm)**2 for v in b))
    return sum((u-am)*(v-bm) for u,v in zip(a,b))/denom if denom else None


def safe(value) -> str:
    """Escape prose for a compact Markdown evidence table."""
    return str(value if value is not None else 'unavailable').replace('|','/').replace('\n',' ')


def number(value) -> str:
    """Keep enough numerical precision to review small exposure coefficients."""
    return 'unavailable' if value is None else f'{value:,.8g}'


def main() -> None:
    """Write one report per stable policy ID, with full company/exposure source rows."""
    reg=registry();out=ROOT/'reports/policies';out.mkdir(exist_ok=True,parents=True)
    sources=list(csv.DictReader((ROOT/'data/sources_registry.csv').open()))
    checked={(r['parameter'],r['company']):r for r in sources}
    bench_path=ROOT/'reports/evidence/published_benchmarks.json'
    benchmarks=json.loads(bench_path.read_text()) if bench_path.exists() else []
    changes=json.loads((ROOT/'reports/evidence/bank_parameter_changes.json').read_text())
    audit=json.loads((ROOT/'design/reviews/policy-audit.json').read_text());internal={r['policy']:r for r in audit['policies']}
    all_checks=[];scorecard=[];ids=[p.id for p in reg.policies.values()]
    if len(ids)!=len(set(ids)):raise ValueError('Policy IDs collide; reports cannot be overwritten')
    for key,p in sorted(reg.policies.items()):
        an=simulate(p.industry,p.id);r=an.base;own=[b for b in benchmarks if b['policy']==key]
        checks=[];analyses={tuple(sorted(p.default_inputs().items())):an}
        for b in own:
            scenario=tuple(sorted(b['inputs'].items()))
            if scenario not in analyses:analyses[scenario]=simulate(p.industry,p.id,inputs=b['inputs'])
            a=analyses[scenario];c=a.base.company(b['ticker']);lo,hi=sorted([getattr(a.envelopes[c.ticker].low,b['metric']),getattr(a.envelopes[c.ticker].high,b['metric'])])
            value=getattr(c,b['metric']);expected=b['benchmark'];sign=value*expected>0 if expected else abs(value)<1e-9
            relative=abs(value-expected)/abs(expected) if expected else (0 if abs(value)<1e-9 else None)
            size=(relative is not None and relative<=.25) or lo<=expected<=hi
            checks.append({**b,'model':value,'low':lo,'high':hi,'relative_error':relative,'direction_pass':sign,'size_pass':size,'pass':sign and size})
        all_checks.extend(checks)
        exposure_rows=[];unchecked=0;included=[];scope=[]
        for c in r.companies:
            decision=company_coverage(p,c.ticker);scope.append((c.ticker,decision))
            if decision['status']!='included':continue
            included.append(c.ticker)
            for k in p.exposure_keys:
                e=reg.exposure(c.ticker,k);proof=checked.get(('exposure.'+k,c.ticker),{});verified=proof.get('verified')=='Y'
                unchecked+=not verified
                exposure_rows.append((c.ticker,k,e,proof,verified))
        unverified_assumptions=[a.key for a in p.assumptions if checked.get((key+'.assumption.'+a.key,'ALL'),{}).get('verified')!='Y']
        # An incomplete company cohort or unmatched financial metric cannot pass
        # merely because the few available calibration points fit themselves.
        covered_bench={b['ticker'] for b in checks}
        complete=bool(checks) and set(included)<=covered_bench and not unchecked and not unverified_assumptions and all(b['pass'] for b in checks)
        verdict='PASS' if complete else 'FAIL-UNRESOLVED'
        changed=[c for c in changes if c['policy']==key]
        if key=='industrials/steel_tariffs':
            old=yaml.safe_load(subprocess.check_output(['git','show','5d8b2df:config/policies/industrials/steel_tariffs.yaml']))
            for a in p.assumptions:
                before=next((v['base'] for v in old.get('assumptions',[]) if v['key']==a.key),None)
                if before!=a.base:changed.append(dict(ticker='ALL',parameter=a.key,before=before,after=a.base,source_url=a.source_url,location=a.source))
        if complete and changed:verdict='RECALIBRATED'
        lines=[f'# {p.name}', '',f'Policy `{key}` · reviewed 2026-10-31 · **{verdict}**', '', '## A. Mechanics and scope', '',
            ('Verified submitted text: S.Amdt.2428 (119th Congress), section 71117 proposed 21% → 28% for taxable years after 2025. This amendment was submitted, not enacted. The model covers only its rate provision using positive US book income as a taxable-income proxy. Credits, tax losses, AMT/GILTI and deferred-tax remeasurement are omitted. The direct after-tax channel does not remeasure the separately displayed effective tax-rate field.' if p.id.startswith('us_corporate_tax_') else 'Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.'), '',p.description,'',f'Duration: `{p.persistence}`. Default inputs: `{json.dumps(p.default_inputs(),sort_keys=True)}`.', '', '| Channel | Template/role limits | Parameters |','|---|---|---|']
        for c in p.channels:lines.append(f'| {c.type} | {safe(c.company_kinds)} / {safe(c.roles)} | {safe(json.dumps(c.params))} |')
        lines += ['', 'Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.', '', 'Policy references (a citation is not numeric verification):','']
        lines.extend('- '+url for url in p.references)
        if key=='financial_services/credit_card_interchange_cap':lines+=['','Scope finding: this is a hypothetical US four-party credit-issuer fee cap. AmEx three-party merchant discount is deliberately excluded as written; Visa/Mastercard network service fees are not issuer interchange. Regulation II is a debit-card rule and does not establish an enacted credit-card cap.']
        if key=='financial_services/fdic_assessment_increase':lines+=['','Scope finding: FDIC bank assessments do not directly insure AIG/PGR/PRU policyholder liabilities. Any holding-company insured-bank subsidiary would require a separately sourced subsidiary assessment base. Insurer classification alone is not FDIC exposure.']
        lines+=['','| Company | Configured status | Basis |','|---|---|---|']
        for t,d in scope:lines.append(f'| {t} | {d["status"]} | {safe(d["reason"])} |')
        lines+=['','## B. Every in-scope exposure','','Exact numeric checks are distinguished from filing links and estimates. UNVERIFIED values are retained, not silently replaced. Historical observed low/high values are not forecast confidence intervals.','','| Company | Exposure | Base | Low | High | Exact-source status | Primary source / location / rationale |','|---|---|---:|---:|---:|---|---|']
        for t,k,e,proof,verified in exposure_rows:
            lines.append(f'| {t} | {k} | {number(e.value)} | {number(e.low)} | {number(e.high)} | {"VERIFIED observation; conversion limits retained" if verified else "UNVERIFIED"} | {safe(e.source_url or "No source URL")} · {safe(proof.get("document_location") or e.source)} · {safe(e.rationale)} |')
        if not exposure_rows:lines.append('| — | No quantified in-scope company exposure | — | — | — | FAIL-UNRESOLVED | Absence of a measured base is not proof of no economic exposure. |')
        lines+=['','## C. Published sensitivity benchmark','','| Company / input | Metric | Published | Modeled | Low / high | Relative error | Direction / size | Source |','|---|---|---:|---:|---|---:|---|---|']
        for b in checks:lines.append(f'| {b["ticker"]} / {safe(b["inputs"])} | {b["unit"]} | {number(b["benchmark"])} | {number(b["model"])} | {number(b["low"])} / {number(b["high"])} | {number(None if b["relative_error"] is None else 100*b["relative_error"])}% | {"PASS" if b["direction_pass"] else "FAIL"} / {"PASS" if b["size_pass"] else "FAIL"} | {b["source_url"]} · {safe(b["document_location"])} |')
        if not checks:lines+=['| — | No matched published company sensitivity obtained | — | — | — | — | FAIL-UNRESOLVED | The exact input, timing, business perimeter and financial metric must match before comparison. |']
        if key=='industrials/steel_tariffs':lines+=['','Verified sector-price calibration: USITC Publication 5405, corrected May 2023, table 5.2 (p.125), 25% tariff: buyer steel prices +2.39%, domestic producer prices +0.74%. The engine gives '+number(100*r.derived['steel_price_rise'])+'% and '+number(100*r.derived['domestic_steel_price_rise'])+'%. These are price metrics, not company EPS. The observed 2018 gross-margin replay remains a confounded magnitude miss; it is not used to fit the tariff coefficient. Source: https://www.usitc.gov/publications/332/pub5405.pdf']
        if key=='financial_services/fed_rate_change':lines+=['','Benchmark matching: COF Table 32, AXP Table 22 current assumptions, STT USD-only column and Ally instantaneous column are used. PNC explicitly permits half-scaling its 200bp scenario; TFC is checked at its published 50bp shock. MS quantifies only Wealth Management; other segments remain unquantified. SCHW/FITB/KEY gradual shocks are not reinterpreted as instantaneous. BNY/USB instantaneous numerical benchmarks were not obtained. Citi negative-shock asymmetry remains unverified. Twelve sourced coefficient changes do not validate missing banks or permanent persistence.']
        lines+=['','## D. Tolerances, totals and ranking','','Direction must match; size must be within ±25% of the published value or contain it in the scenario range. No benchmark means no pass. Comparisons below are in-sample calibration checks, not independent prediction validation.','','Totals: no like-for-like official score for this public-company sample and exact policy horizon was obtained. A national ten-year fiscal score cannot be compared directly with a one-year partial-company cost total. **UNVERIFIED.**','']
        cohorts=defaultdict(list)
        for b in checks:cohorts[(json.dumps(b['inputs'],sort_keys=True),b['metric'])].append(b)
        for (inputs,metric),cohort in cohorts.items():
            rho=spearman([b['model'] for b in cohort],[b['benchmark'] for b in cohort])
            lines.append(f'- `{inputs}` / {metric}: n={len(cohort)}, Spearman rho={number(rho)}'+(' (n<5 or constant ranks)' if rho is None else ' (after calibration; absolute NII ordering, not EPS ranking).'))
        if not cohorts:lines.append('Spearman: unavailable; fewer than five matched published company observations. No ordering is inferred from unverified priors.')
        lines+=['','## E. One-at-a-time sensitivity','','| Driver | Industry metric at low | At high | Absolute swing |','|---|---:|---:|---:|']
        for b in an.tornado:lines.append(f'| {b.driver.kind}.{b.driver.key} | {number(b.low_value)} | {number(b.high_value)} | {number(b.swing)} |')
        top=an.tornado[0] if an.tornado else None
        lines+=['',f'Dominant configured driver: `{top.driver.key if top else "none"}` using `{an.metric}`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.','']
        for f in internal.get(key,{}).get('review_flags',[]):lines.append(f'- REVIEW {f["ticker"]}: EPS {f["eps_change"]:+.1%}; {f["reason"]} {f["range_basis"]}.')
        lines+=['','## F. Verdict and parameter changes','',f'**{verdict}**. {unchecked} unchecked in-scope exposure values; {len(unverified_assumptions)} unchecked assumptions; {len(checks)} matched numerical benchmark comparisons. Internal accounting/scope errors: {len(internal.get(key,{}).get("errors",[]))}.', '', 'A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.','', '| Company | Parameter | Before | After | Evidence |','|---|---|---:|---:|---|']
        for c in changed:lines.append(f'| {c["ticker"]} | {c["parameter"]} | {number(c["before"])} | {number(c["after"])} | {safe(c["source_url"])} · {safe(c["location"])} |')
        if not changed:lines.append('| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |')
        (out/(p.id+'.md')).write_text('\n'.join(lines)+'\n')
        scorecard.append(dict(policy=key,report='reports/policies/'+p.id+'.md',verdict=verdict,unverified_exposures=unchecked,unverified_assumptions=len(unverified_assumptions),matched_benchmarks=len(checks),benchmark_passes=sum(b['pass'] for b in checks),recalibrated_parameters=len(changed),coverage_gaps=sum(d['status']=='unquantified' for _,d in scope)))
    (ROOT/'reports/policy_scorecard.json').write_text(json.dumps(scorecard,indent=2)+'\n')
    (ROOT/'reports/benchmark_checks.json').write_text(json.dumps(all_checks,indent=2)+'\n')
    with (ROOT/'reports/policy_scorecard.csv').open('w',newline='') as h:
        w=csv.DictWriter(h,fieldnames=list(scorecard[0]));w.writeheader();w.writerows(scorecard)
    print(f'{len(scorecard)} A–F reports; verdicts: {dict(Counter(s["verdict"] for s in scorecard))}; {len(all_checks)} published comparisons')


if __name__=='__main__':main()

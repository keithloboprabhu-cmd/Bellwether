"""Admit supported US candidates and add a sourced corporate-rate scenario.

No peer exposure is copied. Unreviewed existing-policy/macro activities stay
explicitly unquantified. Book pretax income is labeled a taxable-income proxy;
the law is verified, but forecast calibration remains unresolved.
"""
from pathlib import Path
import json
import sys
import yaml
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from policyshock.config import ROOT, CONFIG_DIR, load_universe
from policyshock.data import edgar
from policyshock.data.baseline import build_baseline, shares_outstanding
from policyshock.policies.loader import registry

LAW='https://www.congress.gov/amendment/119th-congress/senate-amendment/2428/text'
TAXKEY='audit_us_pretax_income_musd'
SECTORS=['consumer_retail','healthcare','financial_services','tmt','education','transportation_logistics']


def missing_exposure(reason: str) -> dict:
    """Represent a missing measurement as an inactive sentinel, never a reported zero."""
    return dict(value=0., low=0., high=0., applicable=False, source='estimate', rationale='UNQUANTIFIED sentinel, not a measured zero. '+reason)


def write_yaml(path: Path, data: dict) -> None:
    """Write readable validated configuration without Python-specific objects."""
    path.write_text(yaml.safe_dump(data,sort_keys=False,width=105))


def main() -> None:
    """Apply the admission gate and preserve a machine-readable decision ledger."""
    if (ROOT/'data/universe_sources/admission_decisions.json').exists():
        raise RuntimeError('Admission already recorded; review the ledger before a new roster change.')
    reg=registry(); old=load_universe(); config=yaml.safe_load((CONFIG_DIR/'industries.yaml').read_text())
    snapshot_path=ROOT/'data/snapshots/baselines.json'; snap=json.loads(snapshot_path.read_text())
    candidates=json.loads((ROOT/'data/universe_sources/expansion_candidates.json').read_text())['candidates']
    decisions=[]; added=[]; exposure_files={}; original={i.slug:set(i.tickers) for i in old.industries}
    for c in candidates:
        t=c['ticker']; slug=c.get('industry')
        if t in old.all_tickers:continue
        decision=dict(ticker=t, industry=slug, status='not_admitted', reason=c['reason'])
        if c.get('cik'):
            sub=edgar.submissions(c['cik'],1e12)
            state=sub.get('stateOfIncorporation','')
            decision['incorporation']=sub.get('stateOfIncorporationDescription',state)
            domestic_us=len(state)==2 and state in 'AL AK AZ AR CA CO CT DE FL GA HI ID IL IN IA KS KY LA ME MD MA MI MN MS MO MT NE NV NH NJ NM NY NC ND OH OK OR PA RI SC SD TN TX UT VT VA WA WV WI WY DC'.split()
            facts=edgar.company_facts(c['cik'],1e12)
            ys=build_baseline(facts,c.get('kind','standard'))
            if ys:
                it=ys[0].items
                eligible=(domestic_us and slug in SECTORS+['industrials'] and t!='BRK-A'
                    and all(it.get(k) is not None for k in ['revenue','cost_of_revenue','pretax_income','diluted_shares','eps_diluted'])
                    and (it.get('pretax_domestic') or 0)>0 and (it.get('pretax_income') or 0)>0)
                if eligible:
                    added.append(t)
                    co=dict(ticker=t,name=c['name'],kind=c['kind'],subsector=c['sic_description'])
                    next(i for i in config['industries'] if i['slug']==slug)['companies'].append(co)
                    years=[{**y.to_dict(),'filing_url':edgar.filing_url(y.source_cik or c['cik'],y.source_accn) if y.source_accn else None} for y in ys]
                    so=shares_outstanding(facts)
                    if t=='V':
                        # DEI A/B/C raw class counts are not additive economic shares.
                        so=None
                    snap['companies'][t]=dict(ticker=t,name=c['name'],entity_name=c['name'],cik=c['cik'],industry=slug,kind=c['kind'],shares_outstanding=so,years=years)
                    keys=set().union(*(set(reg.exposures.get(x,{})) for x in original[slug]))
                    vals={k:missing_exposure('New issuer: exact policy-specific quantity has not been independently verified; no unrelated peer prior transferred.') for k in keys}
                    if slug=='industrials':
                        ratios=[y.items['pretax_domestic']/y.items['pretax_income'] for y in ys[:3] if (y.items.get('pretax_income') or 0)>0 and y.items.get('pretax_domestic') is not None and 0<=y.items['pretax_domestic']<=y.items['pretax_income']]
                        share=it['pretax_domestic']/it['pretax_income']
                        vals['ind_us_pretax_income_share']=dict(value=share,low=min([share,*ratios]),high=max([share,*ratios]),source='verified SEC companyfacts',source_url=f"https://data.sec.gov/api/xbrl/companyfacts/CIK{c['cik']:010d}.json",rationale='US-incorporated issuer: reported domestic pretax / reported total pretax. Bounds are available three-year historical ratios, not confidence intervals.')
                    exposure_files.setdefault(slug,dict(industry=slug,companies={}))['companies'][t]=vals
                    decision.update(status='admitted',reason='Complete current statement and positive sourced US pretax income; other exposures remain explicitly unquantified. All parser flags explained in the admission ledger.',flags=ys[0].flags,flag_explanations={f:('Arithmetic derivation from disclosed statement lines; retained visibly.' if 'derived' in f else 'Missing or normalized field remains flagged; unrelated channels are unquantified, so it is not treated as a measured zero.') for f in ys[0].flags})
                else:
                    decision['reason']='Admission deferred: '+('; '.join(filter(None,[
                        'non-US incorporation: domestic tax geography requires explicit US jurisdiction reconciliation' if not domestic_us else '',
                        'required statement/share/cost field missing' if any(it.get(k) is None for k in ['revenue','cost_of_revenue','pretax_income','diluted_shares','eps_diluted']) else '',
                        'positive current US pretax exposure not verified' if not (it.get('pretax_domestic') or 0)>0 else '',
                        'partnership/share-class basis requires review' if t in ['BRK-A','ET','EPD'] else '',
                        'no sourced policy for this industry' if slug not in SECTORS+['industrials'] else ''
                    ])) or 'manual review needed')
        decisions.append(decision)
    write_yaml(CONFIG_DIR/'industries.yaml',config)
    snapshot_path.write_text(json.dumps(snap,indent=1)+'\n')
    for slug,d in exposure_files.items():write_yaml(CONFIG_DIR/'exposures'/f'{slug}_audit_admissions.yaml',d)
    # Extend each existing-policy decision explicitly; no legal exclusion is inferred
    # merely because the exact numeric sensitivity has not been sourced.
    coverage=yaml.safe_load((CONFIG_DIR/'policy_company_coverage.yaml').read_text())
    for key,p in reg.policies.items():
        names=[t for t in added if snap['companies'][t]['industry']==p.industry]
        if not names:continue
        good=[t for t in names if p.id=='corporate_tax_rate_change']
        if good:coverage['policies'][key]['groups'].append(dict(status='included',tickers=good,reason='Reported US pretax-income share drives the statutory-rate channel.',default_direction=dict(metric='dNI',sign=-1)))
        unknown=[t for t in names if t not in good]
        if unknown:coverage['policies'][key]['groups'].append(dict(status='unquantified',tickers=unknown,reason='Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact.'))
    defs={'exposures':[dict(key=TAXKEY,label='US pretax book income (taxable-income proxy)',unit='usd_m',help='Positive reported US book pretax income; not reported taxable income. Historical bounds reflect available annual observations, not statistical uncertainty.') ]}
    write_yaml(CONFIG_DIR/'exposure_definitions.d/audit_tax.yaml',defs)
    review=yaml.safe_load((CONFIG_DIR/'policy_review.yaml').read_text()); verified=[]
    for slug in SECTORS:
        companies=[c for c in snap['companies'].values() if c['industry']==slug]
        exp={};included=[];unknown=[]
        for c in companies:
            sub=edgar.submissions(c['cik'],1e12); state=sub.get('stateOfIncorporation','')
            us=state in 'AL AK AZ AR CA CO CT DE FL GA HI ID IL IN IA KS KY LA ME MD MA MI MN MS MO MT NE NV NH NJ NM NY NC ND OH OK OR PA RI SC SD TN TX UT VT VA WA WV WI WY DC'.split()
            ys=c['years']; v=ys[0]['items'].get('pretax_domestic'); valid=us and c['kind']!='reit' and v is not None and v>0
            if valid:
                vals=[y['items']['pretax_domestic'] for y in ys[:3] if y['items'].get('pretax_domestic') is not None and y['items']['pretax_domestic']>0]
                source=f"https://data.sec.gov/api/xbrl/companyfacts/CIK{c['cik']:010d}.json"
                exp[c['ticker']]={TAXKEY:dict(value=v,low=min(vals),high=max(vals),source='verified SEC companyfacts',source_url=source,rationale=f"US-incorporated issuer; {ys[0]['period_end']} us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy.")}
                included.append(c['ticker']);verified.append(dict(parameter='exposure.'+TAXKEY,company=c['ticker'],value=v,low=min(vals),high=max(vals),source_url=source,document_location='us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period '+ys[0]['period_end'],date_accessed='2026-10-31',verified='Y',verification_basis='Exact book-income observation. Book-to-tax conversion is NOT verified; historical range is not a forecast confidence interval.'))
            else:
                unknown.append(c['ticker']);exp[c['ticker']]={TAXKEY:missing_exposure('US jurisdiction, positive taxable-income proxy or pass-through tax status not established. Deferred tax assets/valuation allowances and foreign income are not modeled.')}
        write_yaml(CONFIG_DIR/'exposures'/f'{slug}_audit_tax.yaml',dict(industry=slug,companies=exp))
        policy_id='us_corporate_tax_'+slug
        key=slug+'/'+policy_id
        pol=dict(id=policy_id,industry=slug,name='US corporate tax rate increase — book-income proxy',description='Rate-only scenario based on S.Amdt.2428 (119th Congress), a submitted 21% to 28% proposal, not enacted law. Uses positive reported US book pretax income as a labeled taxable-income proxy; excludes unverified jurisdictions, loss carryforwards and deferred-tax remeasurement.',persistence='permanent',user_inputs=[dict(key='d_rate_pts',label='Increase in federal rate',unit='percentage points',min=0,max=7,step=1,default=7,help='0 leaves current law unchanged; +7 reproduces the submitted 21% to 28% proposal. The proposal was not enacted.')],assumptions=[],channels=[dict(type='tax_credit',label='Rate increase on positive US pretax book income (proxy)',params=dict(credit_rate='-input.d_rate_pts / 100',base_musd='exposure.'+TAXKEY))],exposure_keys=[TAXKEY],default_role='neutral',references=[LAW,'https://uscode.house.gov/us/usc/119-121/t26/s11/'],narrative=dict(extra='Submitted proposal, not enacted law. Reported US book income is a taxable-income proxy. Historical income variation forms the scenario range; credits, AMT, deferred taxes, GILTI and behavioral responses are excluded.'))
        write_yaml(CONFIG_DIR/'policies'/slug/(policy_id+'.yaml'),pol)
        groups=[dict(status='included',tickers=included,reason='US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast.',default_direction=dict(metric='dNI',sign=-1))]
        if unknown:groups.append(dict(status='unquantified',tickers=unknown,reason='Positive US taxable-income proxy not verified; jurisdiction, pass-through status or loss-tax treatment requires review.'))
        coverage['policies'][key]=dict(references=[LAW],groups=groups)
        review['reviews'][key]=dict(rationale='Submitted rate increase, modeled only on positive sourced US pretax book income; other provisions omitted explicitly.',expect=[dict(ticker=included[0],metric='dNI',sign=-1)],unaffected=unknown)
        verified.append(dict(parameter=key+'.input.d_rate_pts',company='USER',value=7,low=0,high=7,source_url=LAW,document_location='Submitted text, section 71117(a): 21% to 28%; 0 is no-change control',date_accessed='2026-10-31',verified='Y',verification_basis='Exact proposed rate-only input. Not enacted; no claim that book income equals taxable income.'))
    write_yaml(CONFIG_DIR/'policy_company_coverage.yaml',coverage);write_yaml(CONFIG_DIR/'policy_review.yaml',review)
    (ROOT/'data/universe_sources/admission_decisions.json').write_text(json.dumps(dict(before=len(old.all_tickers),added=added,after=len(snap['companies']),decisions=decisions),indent=2)+'\n')
    (ROOT/'data/universe_sources/verified_tax_parameters.json').write_text(json.dumps(verified,indent=2)+'\n')
    print(f'Admitted {len(added)}: {", ".join(added)}; 6 new sourced rate-only policies')


if __name__=='__main__':main()

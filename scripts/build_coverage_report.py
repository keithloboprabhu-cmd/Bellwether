"""Report actual default earnings/value coverage without treating missing exposures as zero facts."""
import csv
import json
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from policyshock.config import ROOT,load_universe
from policyshock.engine.simulate import build_runner
from policyshock.policies.loader import registry
from policyshock.policies.coverage import company_coverage


def main() -> None:
    """Write each own-industry policy decision plus strict EPS/value coverage gaps."""
    rows=[];covered=set()
    for key,p in registry().policies.items():
        result=build_runner(p.industry,p.id).run()
        for c in result.companies:
            d=company_coverage(p,c.ticker)
            effect=abs(c.dEPS)>1e-9 or abs(c.dP or 0)>1e-9 or any(abs(o.delta.dValue_pv)>1e-9 or abs(o.delta.dValue_pct)>1e-12 for o in c.outcomes)
            if effect:covered.add(c.ticker)
            declared=d['status']; status={'outside_scope':'out_of_scope','unquantified':'unquantified'}.get(declared,'in_scope' if effect else 'not_binding')
            rows.append(dict(company=c.ticker,industry=p.industry,policy=key,status=status,declared_status=declared,default_earnings_or_value_effect=effect,dNI=c.dNI,dEPS=c.dEPS,dP=c.dP,reason=d['reason']))
    path=ROOT/'reports/coverage_matrix.csv'
    with path.open('w',newline='') as h:
        w=csv.DictWriter(h,fieldnames=list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(sorted(rows,key=lambda r:(r['company'],r['policy'])))
    gaps=sorted(set(load_universe().all_tickers)-covered)
    reasons={
        'BLK':'Asset management is not principal trading. Domestic pretax source excludes noncontrolling interests, while the engine apportions minority income separately; reconciliation pending. No guessed investment-rate sensitivity.',
        'PGR':'No insured bank-assessment exposure; the insurer is not an FDIC bank. Exact US tax jurisdiction base not separately quantified in the current tax note.',
        'SLM':'Education lender, not a tuition operator. Its insured bank subsidiary warrants a separately sourced assessment/NII policy in the education bucket; no Title IV tuition share invented.',
        'LYFT':'Reported US pretax loss; positive-income tax channel does not bind. Net repurchase excise tax is disclosed as immaterial, not a usable numeric base.',
        'MDT':'Irish domicile: GAAP domestic income is not US income; 12.5% statutory-rate reconciliation confirms the jurisdiction distinction. US device-import sensitivity still needs a disclosed numeric base.'}
    lines=['# Coverage gaps','','Default-case coverage requires nonzero EPS or equity value, including explicit unpriced direct-value channels. Revenue-only effects and unquantified exposures do not qualify.','','| Item | Count |','|---|---:|',f'| Companies | {len(load_universe().all_tickers)} |',f'| Default covered | {len(covered)} |',f'| Gaps | {len(gaps)} |',f'| Explicit company-policy decisions | {len(rows)} |','','## Unresolved rule failures','']
    for t in gaps:lines.append(f'- **{t}**: {reasons.get(t,"No independently sourced policy sensitivity established; review the company-policy ledger.")}')
    lines+=['','These are unresolved coverage failures, not assertions that the firms have no economic policy exposure. They are deliberately not filled with copied peer priors.','',
            'Round 3 (see `reports/AUDIT_ROUND3.md`) closed the BLK, PGR, SLM and MDT gaps: the corporate-tax proxy now covers untagged US issuers via their reviewed US share, the rate policy reaches insurer portfolios, borrowing caps credit private lenders, and a medical-device tariff policy covers device importers. Companies covered only by a corporate-tax scenario are listed in `reports/audit_matrix/summary.json`.','','## New policies','','Six industry-specific `us_corporate_tax_<industry>` scenarios cover positive sourced US book pretax income under the submitted S.Amdt.2428 rate change (21% to 28%). Book income is a labeled taxable-income proxy, not a verified cash-tax forecast. Low/high values are historical income observations, not confidence intervals. All original policy IDs remain stable.','']
    for key,p in registry().policies.items():
        if p.id.startswith('us_corporate_tax_'):
            names=[r['company'] for r in rows if r['policy']==key and r['default_earnings_or_value_effect']]
            lines.append(f'- `{key}`: '+', '.join(names))
    (ROOT/'reports/coverage_gaps.md').write_text('\n'.join(lines)+'\n')
    (ROOT/'reports/coverage_summary.json').write_text(json.dumps(dict(companies=len(load_universe().all_tickers),covered=len(covered),gaps=gaps,decisions=len(rows)),indent=2)+'\n')
    print(f'{len(rows)} decisions, {len(covered)} covered, {len(gaps)} unresolved coverage gaps')


if __name__=='__main__':main()

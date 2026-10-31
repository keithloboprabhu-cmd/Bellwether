"""Stage primary-source universe candidates without inventing missing policy exposures.

Fortune membership is publisher-verified. OEF is only a fund-holdings proxy for
S&P membership and cannot certify the requested full S&P publisher roster.
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
import csv
import io
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from policyshock.config import ROOT, load_universe
from policyshock.data import edgar
from policyshock.data.baseline import build_baseline, shares_outstanding

OUT = ROOT / 'data/universe_sources'
REQUESTED = 'V BRK-A MCK COR CAH ACN TXN PM MO MDLZ LIN TMUS CHTR BKNG PYPL MET DHR BMY ISRG INTU NOW SPGI DELL SYY ADM TSN ALL ET EPD ACI'.split()


def canonical(ticker: str) -> str:
    """Use one stable issuer identity, explicitly preserving Berkshire A-share economics."""
    t = ticker.upper().replace('.', '-').replace(' ', '-')
    return {'GOOG': 'GOOGL', 'BRK-B': 'BRK-A'}.get(t, t)


def industry_for(sic: int, description: str, ticker: str) -> tuple[str | None, str]:
    """Map SEC business classifications to this app's broad industry buckets."""
    reviewed = {
        'V': ('financial_services', '10-K Business: payment-network services; SIC 7389 is broader than its actual payment activity.'),
        'PYPL': ('financial_services', '10-K Business: digital payments and transaction services; not an insured commercial bank.'),
        'SPGI': ('financial_services', '10-K Business segments: ratings, market intelligence, indices and commodity insights.'),
        'ACN': ('tmt', '10-K Business: consulting and managed technology services; not classified as a pure government contractor.'),
        'DHR': ('healthcare', '10-K Business segments: biotechnology, life sciences and diagnostics.'),
        'BKNG': ('real_estate_hospitality', '10-K Business: online travel reservations and related services; not a fuel-burning transport operator.'),
        'LRCX': ('tmt', '10-K Business: semiconductor fabrication equipment; not primary steel production.'),
    }
    if ticker in reviewed:
        return reviewed[ticker]
    if ticker in ('ET', 'EPD'):
        return 'energy_resources', 'Midstream pipeline operator; SIC and annual business description.'
    if 6000 <= sic <= 6799:
        return 'financial_services', 'SEC financial-services SIC; subtype retained for statement review.'
    if 8000 <= sic <= 8099 or 2830 <= sic <= 2836 or 3840 <= sic <= 3851 or sic == 5122:
        return 'healthcare', 'SEC healthcare/pharmaceutical/distributor SIC.'
    if 1000 <= sic <= 1499 or 2900 <= sic <= 2999 or 4900 <= sic <= 4999:
        return 'energy_resources', 'SEC resources/energy/utility SIC.'
    if 7000 <= sic <= 7099 or sic in (6512, 6513, 6798, 4724, 7990):
        return 'real_estate_hospitality', 'SEC lodging/travel/real-estate SIC.'
    if 8200 <= sic <= 8299:
        return 'education', 'SEC education SIC.'
    if 4800 <= sic <= 4899 or 3570 <= sic <= 3579 or 3660 <= sic <= 3679 or 7370 <= sic <= 7379 or sic in (3576, 5045):
        return 'tmt', 'SEC technology/telecommunications/software/electronics SIC.'
    if 4000 <= sic <= 4799 or 3710 <= sic <= 3716:
        return 'transportation_logistics', 'SEC transport/vehicle SIC.'
    if 2000 <= sic <= 2399 or 5000 <= sic <= 5999 or sic in (2840, 2844):
        return 'consumer_retail', 'SEC consumer product/retail/wholesale SIC.'
    if 1500 <= sic <= 3999:
        return 'industrials', 'SEC manufacturing/materials SIC.'
    return None, 'SIC alone is insufficient; segment-level assignment requires manual review.'


def fetch_candidate(ticker: str, mapping: dict) -> dict:
    """Fetch SEC facts and classify flags before permitting any runtime activation."""
    cik = mapping.get(ticker)
    if not cik:
        return dict(ticker=ticker, status='unresolved_identifier', reason='No exact SEC ticker-to-CIK match; no identity guessed.')
    sub = edgar.submissions(cik)
    sic = int(sub.get('sic') or 0)
    slug, rationale = industry_for(sic, sub.get('sicDescription', ''), ticker)
    insurer = 6300 <= sic <= 6399
    kind = 'insurer' if insurer else 'standard'
    facts = edgar.company_facts(cik)
    years = build_baseline(facts, kind)
    recent = sub.get('filings', {}).get('recent', {})
    docs = [dict(form=f, accession=a, primary_document=p, filed=d) for f,a,p,d in zip(
        recent.get('form', []), recent.get('accessionNumber', []), recent.get('primaryDocument', []), recent.get('filingDate', [])) if f in ('10-K', '20-F', '40-F')]
    result = dict(ticker=ticker, name=sub.get('name'), cik=cik, sic=sic, sic_description=sub.get('sicDescription'),
        industry=slug, industry_rationale=rationale, kind=kind, role='neutral',
        identity_source=f'https://data.sec.gov/submissions/CIK{cik:010d}.json', accessed='2026-10-31', filings=docs[:2],
        shares_outstanding=shares_outstanding(facts), years=[{**y.to_dict(), 'filing_url':edgar.filing_url(y.source_cik or cik,y.source_accn) if y.source_accn else None} for y in years])
    if not years:
        result.update(status='unsupported_statement', reason='No complete US-GAAP annual 10-K series; 20-F/40-F or custom statement mapping needs review.')
    elif ticker == 'BRK-A':
        result.update(status='share_basis_review', reason='Multi-class A-equivalent EPS/share counts must be reconciled with all traded classes before valuation activation.')
    elif slug is None:
        result.update(status='industry_review', reason=rationale)
    else:
        y=years[0].items
        missing=[k for k in ('revenue','pretax_income','net_income','diluted_shares','eps_diluted') if y.get(k) is None]
        result.update(status='staged' if not missing else 'statement_review', reason='Candidate statement and flags retained; policy-specific numeric exposures must be sourced before activation.' if not missing else 'Missing required statement items: '+', '.join(missing))
    return result


def main() -> None:
    """Archive every membership/exclusion decision and stage SEC evidence for public gaps."""
    fortune=json.loads((OUT/'fortune_100_2026.json').read_text())
    existing=set(load_universe().all_tickers)
    candidates={canonical(t):{'requested_gap':True} for t in REQUESTED}
    decisions=[]
    for p in fortune['profiles']:
        info=p['companyInfo']; t=canonical(info.get('Ticker',''))
        reason = 'Existing reference issuer' if t in existing else ('Federal conservatorship; separate category, not ordinary financial equity' if t in ('FNMA','FMCC') else ('No publicly traded equity; excluded from stock valuation' if info.get('Company type') != 'Public' or not t else 'Public gap: statement and exposure verification required'))
        status='existing' if t in existing else ('conservatorship' if t in ('FNMA','FMCC') else ('excluded_no_traded_equity' if info.get('Company type') != 'Public' or not t else 'candidate'))
        decisions.append(dict(list='Fortune 100 2026', rank=p['rank'],name=p['name'],ticker=t,status=status,reason=reason,source_url=p['source_url']))
        if status=='candidate':candidates.setdefault(t,{})['fortune_rank']=p['rank']
    raw=(OUT/'oef_holdings.csv').read_text(); reader=csv.DictReader(io.StringIO(raw[raw.index('Ticker,'):]))
    for row in reader:
        if row.get('Asset Class') != 'Equity': continue
        t=canonical(row['Ticker'])
        if t not in existing:candidates.setdefault(t,{})['oef_proxy']=True
        decisions.append(dict(list='OEF holdings proxy 2026-10-29; NOT verified S&P publisher membership',rank='', name=row['Name'],ticker=t,status='existing' if t in existing else 'candidate',reason='Fund issuer holdings cross-check only',source_url='https://www.ishares.com/us/products/239723/ishares-s-p-100-etf/latest-holdings.csv'))
    mapping=edgar.ticker_to_cik(); results=[]
    with ThreadPoolExecutor(max_workers=3) as pool:
        jobs={pool.submit(fetch_candidate,t,mapping):t for t in candidates if t not in existing}
        for f in as_completed(jobs):
            t=jobs[f]
            try: r=f.result()
            except Exception as e:r=dict(ticker=t,status='fetch_failed',reason=str(e))
            r.update(candidates[t]);results.append(r)
            print(t,r['status'],flush=True)
    (OUT/'expansion_candidates.json').write_text(json.dumps(dict(accessed='2026-10-31',candidates=sorted(results,key=lambda r:r['ticker'])),indent=1)+'\n')
    with (OUT/'membership_decisions.csv').open('w',newline='') as h:
        w=csv.DictWriter(h,fieldnames=['list','rank','name','ticker','status','reason','source_url']);w.writeheader();w.writerows(decisions)
    print(f'{len(results)} public candidates staged; {len(decisions)} membership decisions')


if __name__=='__main__':main()

"""Admit two otherwise eligible candidates after verifying their actual 10-K covers.

SEC submissions leave incorporation blank for these issuers. The cached original
annual covers supply Delaware; no geography is inferred from revenue or a ticker.
All unrelated policy and macro quantities remain explicitly unquantified.
"""
from pathlib import Path
import gzip
import hashlib
import json
import re
import sys

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from policyshock.config import ROOT, CONFIG_DIR, load_universe
from policyshock.data import edgar
from policyshock.data.baseline import shares_outstanding
from policyshock.policies.loader import registry
from admit_audited_candidates import missing_exposure, write_yaml, TAXKEY


def main() -> None:
    """Apply only the reviewed PLTR/PYPL increment; refuse partial or repeated admission."""
    targets = ('PLTR', 'PYPL')
    universe = load_universe()
    if any(t in universe.all_tickers for t in targets):
        raise RuntimeError('Admission already applied or partial; review the ledger first.')
    candidates = {c['ticker']: c for c in json.loads((ROOT / 'data/universe_sources/expansion_candidates.json').read_text())['candidates']}
    evidence = json.loads((ROOT / 'reports/evidence/filings.json').read_text())
    ledger_path = ROOT / 'data/universe_sources/admission_decisions.json'
    ledger = json.loads(ledger_path.read_text())
    config = yaml.safe_load((CONFIG_DIR / 'industries.yaml').read_text())
    snap_path = ROOT / 'data/snapshots/baselines.json'
    snap = json.loads(snap_path.read_text())
    cov_path = CONFIG_DIR / 'policy_company_coverage.yaml'
    cov = yaml.safe_load(cov_path.read_text())
    verified_path = ROOT / 'data/universe_sources/verified_tax_parameters.json'
    verified = json.loads(verified_path.read_text())
    covers = []
    reg = registry()
    for ticker in targets:
        c = candidates[ticker]
        year = c['years'][0]
        path = ROOT / 'data/cache/filings' / f"{ticker}-{year['source_accn']}.html.gz"
        html = gzip.decompress(path.read_bytes())
        states = re.findall(rb'<ix:nonNumeric[^>]*name=["\']dei:EntityIncorporationStateCountryCode["\'][^>]*>(.*?)</ix:nonNumeric>', html, re.I | re.S)
        assert states and set(states) == {b'Delaware'}
        assert year['items']['pretax_domestic'] > 0 and year['items']['pretax_income'] > 0
        assert all(year['items'][k] is not None for k in ('revenue', 'cost_of_revenue', 'diluted_shares', 'eps_diluted'))
        source = evidence[ticker]['source_url']
        accessed = evidence[ticker]['accessed']
        covers.append(dict(ticker=ticker, value='Delaware', source_url=source,
            document_location='10-K cover / dei:EntityIncorporationStateCountryCode', date_accessed=accessed,
            raw_sha256=hashlib.sha256(html).hexdigest(), verified='Y'))
        slug = c['industry']
        next(i for i in config['industries'] if i['slug'] == slug)['companies'].append(dict(
            ticker=ticker, name=c['name'], kind=c['kind'], subsector=c['sic_description']))
        snap['companies'][ticker] = dict(ticker=ticker, name=c['name'], entity_name=c['name'],
            cik=c['cik'], industry=slug, kind=c['kind'], years=c['years'],
            shares_outstanding=shares_outstanding(edgar.company_facts(c['cik'], 1e12)))
        path = CONFIG_DIR / 'exposures' / f'{slug}_audit_admissions.yaml'
        exp = yaml.safe_load(path.read_text())
        keys = set().union(*(set(reg.exposures.get(t, {})) for t in universe.industry(slug).tickers)) - {TAXKEY}
        exp['companies'][ticker] = {k: missing_exposure('New issuer: policy-specific quantity has not been verified; no peer prior transferred.') for k in sorted(keys)}
        write_yaml(path, exp)
        path = CONFIG_DIR / 'exposures' / f'{slug}_audit_tax.yaml'
        exp = yaml.safe_load(path.read_text())
        values = [y['items']['pretax_domestic'] for y in c['years'][:3] if (y['items'].get('pretax_domestic') or 0) > 0]
        value = year['items']['pretax_domestic']
        tax_source = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{c['cik']:010d}.json"
        exp['companies'][ticker] = {TAXKEY: dict(value=value, low=min(values), high=max(values),
            source='verified SEC companyfacts and annual incorporation cover', source_url=tax_source,
            rationale=f"Delaware verified on annual cover ({source}); {year['period_end']} domestic pretax book income. Historical annual bounds are not forecast confidence intervals; book income is not taxable income.")}
        write_yaml(path, exp)
        verified.append(dict(parameter='exposure.' + TAXKEY, company=ticker, value=value, low=min(values), high=max(values),
            source_url=tax_source, document_location='IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / ' + year['period_end'],
            date_accessed=c['accessed'], verified='Y', verification_basis='Exact book-income observation, US jurisdiction confirmed by actual annual cover. Book-to-tax conversion remains unverified.'))
        tax_id = 'us_corporate_tax_' + slug
        for key, policy in reg.policies.items():
            if policy.industry != slug:
                continue
            group = next((g for g in cov['policies'][key]['groups'] if g['status'] == ('included' if policy.id == tax_id else 'unquantified')), None)
            if group is None:
                group = dict(status='unquantified', tickers=[], reason='New issuer: exact activity and numeric sensitivity not independently verified. No measured zero inferred.')
                cov['policies'][key]['groups'].append(group)
            group['tickers'].append(ticker)
        decision = next(d for d in ledger['decisions'] if d['ticker'] == ticker)
        decision.update(status='admitted', incorporation='Delaware', incorporation_source=source,
            reason='Actual annual cover resolves blank submissions metadata; positive reported US book pretax income supplies a labeled rate-only proxy. Other policies remain unquantified.',
            flags=year['flags'], flag_explanations={f: ('Reported line arithmetic retained visibly; only the exact pretax book-income tax proxy is active.' if 'derived' in f else 'Missing borrowing balance stays unknown; financing channels inactive, never a measured zero.') for f in year['flags']})
        ledger['added'].append(ticker)
    ledger['after'] = len(snap['companies'])
    ledger_path.write_text(json.dumps(ledger, indent=2) + '\n')
    verified_path.write_text(json.dumps(verified, indent=2) + '\n')
    (ROOT / 'data/universe_sources/incorporation_cover_verifications.json').write_text(json.dumps(covers, indent=2) + '\n')
    write_yaml(CONFIG_DIR / 'industries.yaml', config)
    write_yaml(cov_path, cov)
    snap_path.write_text(json.dumps(snap, indent=1) + '\n')
    print('Admitted PLTR and PYPL using actual annual covers; unrelated exposures remain unquantified.')


if __name__ == '__main__':
    main()

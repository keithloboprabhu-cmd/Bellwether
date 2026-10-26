"""Refresh selected insured-bank assessment proxies from the free, keyless FDIC API.

Uses reported subsidiary assets/Tier 1 capital, never revenue-scaled peer balances.
Quarter-end values approximate the statutory average-assets/average-Tier-1 base.
Custody deductions remain explicit scenario estimates. Does not fetch paid data,
change other exposures, or claim these approximations are an actual FDIC invoice.
Run scripts/apply_exposure_audit.py afterward to update canonical exposure files.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import sys

import requests
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'src'))


def assessment_proxy(records: list[dict], mapping: dict) -> dict:
    """Validate identity/units and estimate a base from one company's bank subsidiaries."""
    by_cert = {int(b['CERT']): b for b in records}
    if set(by_cert) != set(mapping['certs']) or len(by_cert) != len(records):
        raise ValueError('Missing/duplicate FDIC subsidiary certificates')
    for b in records:
        if mapping['parent_contains'] not in b.get('NAMEHCR', ''):
            raise ValueError(f'Unexpected parent for certificate {b["CERT"]}: {b.get("NAMEHCR")}')
        if not 0 < b['RBCT1J'] < b['ASSET']:
            raise ValueError(f'Missing/invalid bank assets or Tier 1 capital: {b["CERT"]}')
    dates = {b['REPDTE'] for b in records}
    if len(dates) != 1:
        raise ValueError('Mixed bank reporting dates')
    # FDIC monetary fields are thousands; the modeling engine uses millions.
    gross = sum((b['ASSET'] - b['RBCT1J']) / 1000 for b in records)
    factor = mapping.get('custody_base_factor', 1.0)
    return dict(value=gross * factor, low=gross * mapping.get('factor_low', .9),
                high=gross * mapping.get('factor_high', 1.1),
                gross_base_musd=gross, reported_assets_musd=sum(b['ASSET']/1000 for b in records),
                report_date=next(iter(dates)))


def main() -> None:
    """Fetch/validate all mapped banks before writing a dated snapshot and estimate overrides."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--report-date', default='20260630', help='FDIC YYYYMMDD reporting date')
    args = parser.parse_args()
    mapping = yaml.safe_load((ROOT/'config/fdic_bank_subsidiaries.yaml').read_text())['banks']
    certs = [c for m in mapping.values() for c in m['certs']]
    response = requests.get('https://api.fdic.gov/banks/financials', params={
        'filters': f'REPDTE:{args.report_date} AND CERT:('+' OR '.join(map(str, certs))+')',
        'fields': 'NAME,CERT,REPDTE,ASSET,RBCT1J,NAMEHCR', 'limit': len(certs)+1,
    }, timeout=45)
    response.raise_for_status()
    payload = response.json()
    records = [row['data'] for row in payload['data']]
    if len(records) != len(certs):
        raise ValueError('Incomplete FDIC response; existing exposures were preserved')
    overrides_path = ROOT/'config/company_exposure_overrides.yaml'
    overrides = yaml.safe_load(overrides_path.read_text())
    company_rows = {}
    for ticker, m in mapping.items():
        banks = [b for b in records if int(b['CERT']) in m['certs']]
        values = assessment_proxy(banks, m)
        company_rows[ticker] = dict(**values, certificates=m['certs'])
        source_url = 'https://api.fdic.gov/banks/financials?filters=CERT:'+str(m['certs'][0])+'%20AND%20REPDTE:'+args.report_date
        names = '; '.join(f'{b["NAME"]} (CERT {b["CERT"]})' for b in banks)
        rationale = (f'FDIC {args.report_date} bank reports: {names}. Reported subsidiary ASSET minus RBCT1J (Tier 1 capital), '
                     f'converted from thousands to millions = ${values["gross_base_musd"]:,.3f}M. '
                     'This is a quarter-end proxy for statutory average assets minus average Tier 1 capital, '
                     'not a reported assessment base. No holding-company or revenue-scaled peer assets are used. ')
        if 'custody_base_factor' in m:
            rationale += ('Apply an estimated 55% residual assessment base (30–80% range) for custodial-bank exclusions; '
                          'the deduction is not disclosed in this source and remains uncertain.')
        else:
            rationale += 'Use ±10% sensitivity for averaging/timing and remaining assessment adjustments.'
        overrides['companies'].setdefault(ticker, {})['fdic_assessment_base_musd'] = dict(
            **{k: values[k] for k in ('value', 'low', 'high')}, source='estimate', source_url=source_url,
            rationale=rationale, applicable=True)
    snapshot = dict(retrieved_at=datetime.now(timezone.utc).isoformat(), report_date=args.report_date,
                    source_url=response.url, source='FDIC BankFind financials', monetary_unit='USD thousands',
                    records=records, companies=company_rows,
                    limitations='Quarter-end proxy, not a bank invoice or exact statutory quarterly average. Custodial deductions are estimated; entity mappings require review after mergers.')
    (ROOT/'data/snapshots/fdic_assessment_bases.json').write_text(json.dumps(snapshot, indent=2)+'\n')
    overrides_path.write_text(yaml.safe_dump(overrides, sort_keys=False, width=105))
    print(f'Validated {len(records)} insured bank reports for {len(company_rows)} companies; dated {args.report_date}')
    print(f'COF assessment proxy: ${company_rows["COF"]["value"]:,.0f}M')


if __name__ == '__main__':
    main()

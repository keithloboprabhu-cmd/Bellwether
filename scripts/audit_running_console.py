"""Verify every configured policy/input boundary through the running live-data API.

Start the local server first. This check never requests an upstream data refresh;
each response identifies the source capture actually used by the serving engine.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import math
from pathlib import Path
import sys
from urllib.request import Request, urlopen

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'src'))
from policyshock.policies.audit import input_cases
from policyshock.policies.loader import registry
from policyshock.policies.coverage import coverage_reviews
from policyshock.config import load_universe


def main() -> None:
    """Audit live API policy outputs without changing company or scenario settings."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base-url', default='http://127.0.0.1:8787')
    args = parser.parse_args()
    rows, errors = [], []
    reviews = yaml.safe_load((ROOT/'config/policy_review.yaml').read_text())['reviews']
    for key, p in sorted(registry().policies.items()):
        count = 0
        data = {}
        impact_seen = set()
        decisions = {t:g for g in coverage_reviews()[key]['groups'] for t in g['tickers']}
        for inputs in input_cases(p):
            req = Request(args.base_url+'/api/scenario', data=json.dumps(dict(industry=p.industry,policy=p.id,inputs=inputs)).encode(), headers={'Content-Type':'application/json'})
            try:
                with urlopen(req, timeout=60) as response:
                    data = json.load(response)
                assert data.get('captured_at'), 'No live data capture identified'
                assert {c['id'] for c in data['companies']} == set(load_universe().industry(p.industry).tickers), 'Incomplete/wrong company sample'
                by_ticker = {c['id']:c for c in data['companies']}
                assert set(by_ticker) == set(decisions), 'Incomplete independent company coverage review'
                for ticker, group in decisions.items():
                    c = by_ticker[ticker]
                    changed = any(abs(c[f] or 0) > 1e-8 for f in ('revenue','dNI','value')) or c['coverage']['status'] == 'value_only'
                    if changed:
                        impact_seen.add(ticker)
                    if group['status'] in ('outside_scope','unquantified','conditional'):
                        assert not changed, f'{ticker} affected outside reviewed central coverage'
                    if group['status'] == 'outside_scope':
                        assert c['coverage']['status'] == 'outside_scope' and c['coverage']['reason'], f'{ticker} missing policy-scope explanation'
                for ticker in reviews[key].get('unaffected', []):
                    c = by_ticker[ticker]
                    assert all(abs(c[f] or 0) < 1e-8 for f in ('revenue','dNI','value')), f'{ticker} affected outside declared scope'
                if inputs == p.default_inputs():
                    for expected in reviews[key]['expect']:
                        c = by_ticker[expected['ticker']]
                        field = expected['metric']
                        value = c['metrics']['price']['delta'] if field == 'dP' else c['revenue' if field == 'dR' else field]
                        assert value is not None and value * expected['sign'] > 1e-8, f'{c["id"]} wrong economic direction'
                for c in data['companies']:
                    for name in ('revenue','dNI','dEPS','eps','value','market_value'):
                        assert c[name] is None or math.isfinite(c[name]), f'{c["id"]} nonfinite {name}'
                    assert math.isclose(sum(ch['dNI'] for ch in c['channels']),c['dNI'],rel_tol=1e-9,abs_tol=1e-7), f'{c["id"]} attribution mismatch'
                    if c['market_value'] is not None:
                        assert math.isclose(sum(ch['dValue'] for ch in c['channels']),c['market_value'],rel_tol=1e-9,abs_tol=1e-7), f'{c["id"]} valuation mismatch'
                count += 1
            except Exception as exc:
                errors.append(f'{key}/{inputs}: {exc}')
        for ticker, group in decisions.items():
            if group['status'] == 'included' and ticker not in impact_seen:
                errors.append(f'{key}/{ticker}: expected direct effect missing at every live API input case')
        rows.append(dict(policy=key, companies=len(decisions), passed=count, expected=len(input_cases(p)),versions=data.get('versions'),captured_at=data.get('captured_at')))
    result = dict(checked_at=datetime.now(timezone.utc).isoformat(), policies=rows, errors=errors)
    (ROOT/'design/reviews/live-policy-smoke.json').write_text(json.dumps(result,indent=2)+'\n')
    print(f'{len(rows)} policies / {sum(r["passed"] for r in rows)} live API input cases passed; {len(errors)} failures')
    for error in errors: print(error)
    raise SystemExit(bool(errors))


if __name__ == '__main__':
    main()

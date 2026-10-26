"""Run the complete policy audit and write a reviewable report; exit nonzero on failure."""

from __future__ import annotations

from datetime import datetime, timezone
import csv
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from policyshock.policies.audit import audit_all


def main() -> None:
    """Write policy-by-policy scope, boundary and accounting evidence."""
    result = audit_all()
    files = sorted((ROOT/'config').rglob('*.yaml')) + sorted((ROOT/'src/policyshock').rglob('*.py')) + sorted((ROOT/'data/snapshots').glob('*.*'))
    digest = hashlib.sha256()
    for path in files:
        digest.update(str(path.relative_to(ROOT)).encode())
        digest.update(path.read_bytes())
    result['fingerprint'] = digest.hexdigest()[:16]
    result['checked_at'] = datetime.now(timezone.utc).isoformat()
    out = ROOT/'design/reviews'
    out.mkdir(parents=True, exist_ok=True)
    ps, ms = result['policies'], result['macro_shocks']
    decisions = [dict(policy=p['policy'], **c) for p in ps for c in p['company_checks']]
    result['company_policy_decisions'] = len(decisions)
    result['unique_companies'] = len({c['ticker'] for c in decisions})
    (out/'policy-audit.json').write_text(json.dumps(result, indent=2)+'\n')
    lines = ['# Bellwether policy audit', '', f'Checked {result["checked_at"]}; source/data fingerprint `{result["fingerprint"]}`.', '',
             f'{len(ps)} industry policies and {len(ms)} macro shocks. {sum(p["input_cases"] for p in ps)} industry input cases; {sum(p["driver_cases"] for p in ps)} coefficient/exposure endpoint cases; {sum(m["input_cases"] for m in ms)} macro input cases. {len(result["errors"])} failures.', '',
             f'{len(decisions)} explicit industry-policy/company coverage decisions across {result["unique_companies"]} unique companies. Every decision is independently recorded in config/policy_company_coverage.yaml, including business rationale and default direction for covered firms. Missing/extra firms, missing expected impacts, wrong default directions and out-of-scope effects are failures. Scope checks also run at uncertainty endpoints, not only defaults. Macro shocks cover all 203 companies and their uncertain-driver endpoints.', '',
             'Checks: defaults, every valid input endpoint and endpoint combination, legal all-zero settings, every uncertain driver endpoint, finite results, nonnegative revenue/cost levels, exact earnings and valuation attribution, EPS/share identity, tax bounds, per-company oriented scenario ranges, independent sign/scope expectations, exposure provenance and explicit no-coverage exceptions.', '',
             'This is an internal model audit, not independent assurance, causal policy attribution or out-of-sample forecast validation. Exposures and transmission coefficients marked estimate remain uncertain. A filing link provides business context and does not turn an estimated ratio into reported data. Current business scope can differ from the fiscal-year financial baseline after a divestiture.', '',
             '| Policy | Affected / sample | Input cases | Driver endpoints | Result |', '|---|---:|---:|---:|---|']
    for p in ps:
        lines.append(f'| {p["policy"]} | {len(p["affected"])}/{p["companies"]} | {p["input_cases"]} | {p["driver_cases"]} | {"FAIL" if p["errors"] else "PASS"} |')
    lines += ['', '## Macro shocks', '']
    lines += [f'- {m["shock"]}: {m["input_cases"]} input cases + {m["driver_cases"]} driver endpoints × {m["companies"]} firms; {len(m["errors"])} failures.' for m in ms]
    lines += ['', '## Company scope and remaining limitations', '']
    for p in ps:
        lines += [f'### {p["policy"]}', '', p['rationale'] or '', '', 'Affected: '+(', '.join(p['affected']) or 'None quantified')+'.', 'Neutral in direct channels: '+(', '.join(p['neutral']) or 'None')+'.', f'{p["estimate_exposures"]} estimated company exposure inputs; {p["scope_checks"]} narrow-business scope checks.']
        if p['value_only']: lines.append('Value-only impact: the console defaults to implied share-price change; zero EPS is intentional.')
        lines += ['- '+w for w in p['warnings']]
        lines += ['- Reference: '+url for url in p['references']]
        lines += ['']
    if result['errors']: lines += ['## Failures', '']+['- '+e for e in result['errors']]
    (out/'POLICY_AUDIT.md').write_text('\n'.join(lines)+'\n')
    with (out/'policy-company-coverage.csv').open('w', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=['policy', 'ticker', 'status', 'default_affected', 'any_input_affected', 'reason'])
        writer.writeheader()
        writer.writerows(decisions)
    print(f'{len(ps)} policies, {len(ms)} macro shocks, {len(result["errors"])} failures')
    for e in result['errors']: print(e)
    raise SystemExit(bool(result['errors']))


if __name__ == '__main__':
    main()

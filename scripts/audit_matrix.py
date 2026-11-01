"""Policy × company credibility matrix over the full configured universe.

For every industry policy and every company in that industry this runs the
default scenario, each numeric input at its min and max, and (where legal) an
all-zero shock, then records base ΔEPS %, implied price %, the declared coverage
status from config/policy_company_coverage.yaml, and anomaly flags:

  zero_shock_nonzero   a zero shock moved results (engine invariant)
  sign_flip            the min and max of the policy's main input move the company in
                       the same direction while defaults sit between them in a way
                       that is not monotone (checked per input, numeric only)
  extreme_eps          |ΔEPS %| > 100 % at defaults (flag for review, not an error)
  extreme_price        |Δprice %| > 50 % at defaults
  included_but_zero    declared `included` yet no effect at defaults or any endpoint
  unquantified         declared coverage gap

It also reports companies that receive no economic effect from any policy other
than the generic US corporate-tax policy. Outputs go to reports/audit_matrix/.
Run: PYTHONPATH=src .venv/bin/python scripts/audit_matrix.py
"""

from __future__ import annotations

import csv
import json
import math
from dataclasses import replace
from pathlib import Path

from policyshock.config import load_universe
from policyshock.engine.simulate import build_runner
from policyshock.policies.coverage import company_coverage, economic_effect
from policyshock.policies.loader import registry

OUT = Path(__file__).resolve().parents[1] / "reports" / "audit_matrix"
GENERIC = ("us_corporate_tax", "corporate_tax_rate_change")


def _metric(c) -> float:
    """Company headline metric: ΔEPS % when defined, else implied price %, else 0."""
    if c.dEPS_pct is not None:
        return c.dEPS_pct
    return c.dP_pct or 0.0


def _endpoint_cases(p) -> list[tuple[str, dict]]:
    """Defaults, each numeric input at min and max, and the all-zero shock where legal."""
    d = p.default_inputs()
    cases = [("default", d)]
    for u in p.user_inputs:
        if u.type != "number":
            continue
        for tag, v in (("min", u.min), ("max", u.max)):
            if v is not None:
                cases.append((f"{u.key}={tag}", d | {u.key: v}))
    nums = [u for u in p.user_inputs if u.type == "number"]
    if nums and all((u.min is None or u.min <= 0) and (u.max is None or u.max >= 0) for u in nums):
        cases.append(("zero", d | {u.key: 0 for u in nums}))
    return cases


def _monotone_issue(runner, p, ticker: str) -> list[str]:
    """For each numeric input, sweep min→max in 5 steps; flag direction reversals."""
    out = []
    for u in p.user_inputs:
        if u.type != "number" or u.min is None or u.max is None or u.min == u.max:
            continue
        xs = [u.min + (u.max - u.min) * k / 4 for k in range(5)]
        ys = []
        for x in xs:
            r = replace(runner, inputs=runner.inputs | {u.key: x}).run()
            ys.append(r.company(ticker).dNI + 1e-9 * (r.company(ticker).dP or 0))
        diffs = [b - a for a, b in zip(ys, ys[1:]) if abs(b - a) > 1e-6]
        if diffs and any(dd > 0 for dd in diffs) and any(dd < 0 for dd in diffs):
            out.append(f"non-monotone in {u.key}")
    return out


def main() -> None:
    """Build the matrix CSV, a JSON summary and a short Markdown report."""
    reg = registry()
    uni = load_universe()
    OUT.mkdir(parents=True, exist_ok=True)
    rows, any_effect = [], {t: set() for t in uni.all_tickers}
    for key, p in sorted(reg.policies.items()):
        runner = build_runner(p.industry, p.id)
        results = {tag: replace(runner, inputs=inp).run() for tag, inp in _endpoint_cases(p)}
        base = results["default"]
        for c in base.companies:
            g = company_coverage(p, c.ticker) or {}
            status = g.get("status", "MISSING")
            touched = [tag for tag, r in results.items() if tag != "zero" and economic_effect(r.company(c.ticker))]
            if touched and not p.id.startswith(GENERIC):
                any_effect[c.ticker].add(p.id)
            flags = []
            if "zero" in results and economic_effect(results["zero"].company(c.ticker)):
                flags.append("zero_shock_nonzero")
            m = _metric(c)
            if abs(m) > 1.0 and c.dEPS_pct is not None:
                flags.append("extreme_eps")
            if c.dP_pct is not None and abs(c.dP_pct) > 0.5:
                flags.append("extreme_price")
            if status == "included" and not touched:
                flags.append("included_but_zero")
            if status in ("outside_scope",) and touched:
                flags.append("outside_scope_but_effect")
            if status == "unquantified":
                flags.append("unquantified")
            if touched:
                flags += _monotone_issue(runner, p, c.ticker)
            rows.append(dict(
                policy=key, ticker=c.ticker, status=status,
                dEPS_pct=None if c.dEPS_pct is None else round(c.dEPS_pct, 5),
                dP_pct=None if c.dP_pct is None else round(c.dP_pct, 5),
                dNI_musd=round(c.dNI, 3), dR_musd=round(c.dR, 3),
                effect_cases=len(touched), flags=";".join(flags),
            ))
    with (OUT / "matrix.csv").open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    from collections import Counter
    flag_counts = Counter(fl.split(" in ")[0] for r in rows for fl in r["flags"].split(";") if fl)
    status_counts = Counter(r["status"] for r in rows)
    orphans = sorted(t for t, s in any_effect.items() if not s)
    summary = dict(pairs=len(rows), policies=len(reg.policies), companies=len(uni.all_tickers),
                   status_counts=status_counts, flag_counts=flag_counts,
                   companies_without_specific_policy_effect=orphans,
                   flagged=[r for r in rows if r["flags"] and r["flags"] != "unquantified"])
    (OUT / "summary.json").write_text(json.dumps(summary, indent=1, default=str))
    print(json.dumps({k: v for k, v in summary.items() if k != "flagged"}, indent=1, default=str))
    print("flagged rows:", len(summary["flagged"]))


if __name__ == "__main__":
    main()

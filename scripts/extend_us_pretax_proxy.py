"""Extend `audit_us_pretax_income_musd` to issuers the first audit left unquantified.

The rate-only `us_corporate_tax_<industry>` policies tax positive US pretax book
income. The first admission pass only accepted issuers whose latest 10-K tags
domestic pretax income directly. This pass fills the remaining gaps with a
documented hierarchy, using only committed SEC companyfacts data:

1. tagged    latest-year domestic pretax income tagged and positive
2. derived   latest-year total pretax and foreign pretax tagged; domestic = total − foreign > 0
3. estimate  no split tagged: total pretax × the reviewed `mx_us_pretax_share` estimate
             (the same share the Full Market corporate-tax shock already uses)

Issuers stay UNQUANTIFIED (inactive sentinel) when the latest year shows a US or
total pretax loss (the positive-income proxy does not apply; NOL and deferred-tax
effects are not modeled) or when they are not US-incorporated. Low/high are the
min/max of the same proxy over up to three recent positive years (estimates also
scale by the share's low/high), i.e. historical variation, not confidence bands.

Updates config/exposures/<industry>_audit_tax.yaml and the coverage groups in
config/policy_company_coverage.yaml. Idempotent.
Run: PYTHONPATH=src .venv/bin/python scripts/extend_us_pretax_proxy.py
"""

from __future__ import annotations

import yaml

from policyshock.config import CONFIG_DIR, load_universe
from policyshock.data import store
from policyshock.policies.loader import registry

KEY = "audit_us_pretax_income_musd"


def store_cik(t: str) -> int:
    """Issuer CIK from the committed EDGAR baseline snapshot."""
    import json
    from policyshock.config import ROOT
    return int(json.loads((ROOT / "data/snapshots/baselines.json").read_text())["companies"][t]["cik"])
NON_US_INCORPORATED = {"MDT": "Irish-incorporated (Medtronic plc); 'domestic' in its tax note is not US federal income."}
INDUSTRIES = ["consumer_retail", "healthcare", "financial_services", "tmt", "education", "transportation_logistics"]


def _years(t: str) -> list[dict]:
    return sorted(store.company_years(t), key=lambda y: y["period_end"], reverse=True)[:3]


def proxy(t: str, share) -> tuple[str, float, float, float, str] | tuple[str, str]:
    """Return (tier, value, low, high, rationale) or ('gap', reason)."""
    if t in NON_US_INCORPORATED:
        return "gap", NON_US_INCORPORATED[t]
    ys = _years(t)
    it = ys[0]["items"]
    pti, dom, frn = it.get("pretax_income"), it.get("pretax_domestic"), it.get("pretax_foreign")
    fy = ys[0]["fiscal_year"]
    if pti is None or pti <= 0:
        return "gap", f"FY{fy} total pretax book loss; the positive-income proxy gives no current-tax effect and NOL/deferred-tax value is not modeled."
    if dom is not None:
        if dom <= 0:
            return "gap", f"FY{fy} tagged US pretax book loss ({dom:,.0f} $M) despite positive total income; the positive-income proxy does not apply and US taxable income is not disclosed."
        vals = [y["items"]["pretax_domestic"] for y in ys if (y["items"].get("pretax_domestic") or 0) > 0]
        return "tagged", dom, min(vals), max(vals), (
            f"US-incorporated issuer; FY{fy} us-gaap IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic. "
            "Low/high are observed positive values in up to three recent years; book income is a taxable-income proxy.")
    if frn is not None and pti - frn > 0:
        vals = [y["items"]["pretax_income"] - y["items"]["pretax_foreign"] for y in ys
                if y["items"].get("pretax_income") is not None and y["items"].get("pretax_foreign") is not None
                and y["items"]["pretax_income"] - y["items"]["pretax_foreign"] > 0]
        return "derived", pti - frn, min(vals), max(vals), (
            f"US-incorporated issuer; FY{fy} total pretax income less tagged foreign pretax income "
            "(IncomeLossFromContinuingOperationsBeforeIncomeTaxesForeign). Low/high are the same derivation over up to three recent years.")
    vals = [y["items"]["pretax_income"] for y in ys if (y["items"].get("pretax_income") or 0) > 0]
    k_lo, k_hi = share.low / share.value, share.high / share.value
    return "estimate", pti * share.value, min(vals) * share.value * k_lo, max(vals) * share.value * k_hi, (
        f"No domestic/foreign split tagged. FY{fy} total pretax income × US share {share.value:.2f} "
        f"({share.low:.2f}-{share.high:.2f}) from mx_us_pretax_share: {share.rationale}")


def main() -> None:
    """Rewrite the gap sentinels that a sourced proxy can now replace; report the rest."""
    reg = registry()
    cov_path = CONFIG_DIR / "policy_company_coverage.yaml"
    cov = yaml.safe_load(cov_path.read_text())
    uni = load_universe()
    report = {}
    for slug in INDUSTRIES:
        path = CONFIG_DIR / "exposures" / f"{slug}_audit_tax.yaml"
        doc = yaml.safe_load(path.read_text())
        key = f"{slug}/us_corporate_tax_{slug}"
        groups = cov["policies"][key]["groups"]
        included = next(g for g in groups if g["status"] == "included")
        for t in uni.industry(slug).tickers:
            cur = reg.exposure(t, KEY)
            if cur.applicable:
                continue
            res = proxy(t, reg.exposure(t, "mx_us_pretax_share"))
            report[t] = res[0]
            if res[0] == "gap":
                doc["companies"][t][KEY]["rationale"] = "UNQUANTIFIED sentinel, not a measured zero. " + res[1]
                continue
            tier, v, lo, hi, why = res
            lo, hi = min(lo, v), max(hi, v)
            doc["companies"][t][KEY] = dict(
                value=round(v, 3), low=round(lo, 3), high=round(hi, 3),
                source="estimate" if tier == "estimate" else f"{tier} SEC companyfacts",
                source_url=f"https://data.sec.gov/api/xbrl/companyfacts/CIK{store_cik(t):010d}.json",
                rationale=why)
            for g in groups:
                if t in g["tickers"] and g is not included:
                    g["tickers"].remove(t)
            if t not in included["tickers"]:
                included["tickers"].append(t)
        cov["policies"][key]["groups"] = [g for g in groups if g["tickers"]]
        path.write_text(yaml.safe_dump(doc, sort_keys=False, width=105))
    cov_path.write_text(yaml.safe_dump(cov, sort_keys=False, width=105))
    from collections import Counter
    print(Counter(report.values()))
    print({t: v for t, v in report.items()})


if __name__ == "__main__":
    main()

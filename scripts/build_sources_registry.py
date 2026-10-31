"""Inventory model parameters without confusing a citation with verified calibration."""

from pathlib import Path
import csv
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from policyshock.config import ROOT
from policyshock.data.supplements import statement_supplements
from policyshock.policies.loader import registry

FIELDS = ["parameter", "company", "value", "low", "high", "source_url", "document_location", "date_accessed", "verified", "verification_basis"]


def main() -> None:
    """Save verified filing facts separately from existing unverified modeling priors."""
    reg = registry()
    rows = []
    for ticker, exposures in reg.exposures.items():
        for key, value in exposures.items():
            rows.append(dict(parameter="exposure." + key, company=ticker, value=value.value, low=value.low,
                high=value.high, source_url=value.source_url or "", document_location=value.source + "; " + (value.rationale or ""),
                date_accessed="", verified="N", verification_basis="Existing value retained; this audit has not independently verified the exact numeric exposure against its source."))
    for key, policy in reg.policies.items():
        for a in policy.assumptions:
            verified = key == "industrials/steel_tariffs" and a.key in ("price_response", "producer_price_response")
            rows.append(dict(parameter=key + ".assumption." + a.key, company="ALL", value=a.base, low=a.low,
                high=a.high, source_url=a.source_url or "", document_location=a.source + "; " + (a.rationale or ""),
                date_accessed="2026-10-31" if verified else "", verified="Y" if verified else "N",
                verification_basis="USITC table 5.2, each annual effect divided by 25%; exact historical price metric, not company EPS." if verified else "UNVERIFIED: citation/estimate is not an independently checked benchmark."))
        for u in policy.user_inputs:
            rows.append(dict(parameter=key + ".input." + u.key, company="USER", value=u.default, low=u.min,
                high=u.max, source_url="; ".join(policy.references), document_location=u.help or u.label,
                date_accessed="", verified="N", verification_basis="Scenario control; legal scope and realistic bounds require per-policy review."))
    for entry in statement_supplements().values():
        for key, value in entry["items"].items():
            rows.append(dict(parameter="baseline." + key, company=entry["ticker"], value=value["value"], low=value["value"], high=value["value"],
                source_url=value["source_url"], document_location=value["document_location"], date_accessed=value["accessed"], verified="Y", verification_basis=value["rationale"]))
        s = entry.get("shares_outstanding")
        if s:
            rows.append(dict(parameter="baseline.shares_outstanding", company=entry["ticker"], value=s["value"], low=s["value"], high=s["value"],
                source_url=s["source_url"], document_location=s["document_location"], date_accessed=s["accessed"], verified="Y", verification_basis="Latest annual cover date; unique share-class contexts summed; millions of shares."))
    for name, value, reason in [("valuation.price_floor", 0, "Audit specification, Phase 1: equity limited-liability floor"),
                                ("valuation.median_years", 3, "Audit specification, Phase 1: three-year median valuation fallback"),
                                ("valuation.depressed_threshold", .6, "Audit specification: current EPS more than 40% below three-year median"),
                                ("audit.eps_review_threshold", .5, "Audit specification: absolute EPS change above 50% triggers review")]:
        rows.append(dict(parameter=name, company="ALL", value=value, low=value, high=value, source_url="",
            document_location=reason + "; user brief dated 2026-10-31", date_accessed="2026-10-31", verified="Y",
            verification_basis="User-specified model control, not an empirical financial calibration."))
    for name, value, source, location, verified in [
        ("tax.post_2017_statutory", .21, "https://www.irs.gov/irb/2018-18_IRB", "Corporate rate 21%; TCJA fiscal-year transition", "Y"),
        ("tax.pre_2018_statutory", .35, "https://www.irs.gov/irb/2018-18_IRB", "Corporate rate 35% before TCJA", "Y"),
        ("tax.prior_normalization_years", 3, "", "Documented audit model convention; preceding fiscal years only", "N"),
        ("tax.ordinary_rate_screen_low", 0, "", "Existing model judgment retained; not a legal rate floor", "N"),
        ("tax.ordinary_rate_screen_high", .40, "", "Existing model judgment retained; not a legal rate ceiling", "N"),
    ]:
        rows.append(dict(parameter=name, company="ALL", value=value, low=value, high=value,
            source_url=source, document_location=location, date_accessed="2026-10-31" if verified == "Y" else "",
            verified=verified, verification_basis="Statutory rule" if verified == "Y" else "UNVERIFIED empirical convention; explicitly documented, not a reported company rate."))
    path = ROOT / "data/sources_registry.csv"
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    print(f"{len(rows)} source rows; {sum(r['verified'] == 'Y' for r in rows)} verified exact facts/rules")


if __name__ == "__main__":
    main()

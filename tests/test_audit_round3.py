"""Regression tests for the round-3 credibility audit (see reports/AUDIT_ROUND3.md)."""

from dataclasses import replace

import pytest

from policyshock.config import load_universe
from policyshock.data import store
from policyshock.engine.channels import run_channel
from policyshock.engine.simulate import build_runner
from policyshock.macro.aggregate import build_market_runner
from policyshock.policies.coverage import economic_effect
from policyshock.policies.loader import registry

# Companies with no effect from any industry-specific policy, each for a documented reason
# (see reports/AUDIT_ROUND3.md "Remaining coverage gaps"). Shrinking this set is fine;
# growing it means a regression in coverage.
DOCUMENTED_ORPHANS = {
    "BLK", "MA", "PYPL", "SNEX", "SPGI",  # payments/asset management: no fitting policy or unsourced sensitivity
    "CHRW", "UBER", "LYFT",  # freight brokerage / ride-hailing: no fitting transport policy
    "LAUR",  # operates outside the US; US education policies do not reach it
    "NOW", "PANW", "PLTR", "SNDK", "SNX", "DELL", "HPQ",  # TMT exposures not sourced (see report)
}
# Responses that reverse direction across an input's range and are verified from filings.
VERIFIED_NON_MONOTONE = {("financial_services/fed_rate_change", "TFC")}  # 10-K: NII falls at both +50bp and -50bp


def test_rate_change_never_books_a_gain_on_a_pretax_loss():
    """A tax increase cannot raise a loss-maker's earnings (no current tax is paid)."""
    b = dict(pretax_income=-500.0)
    assert run_channel("tax_rate", b, {"d_statutory_rate": 0.07}).dTaxRate == 0
    assert run_channel("tax_rate", dict(pretax_income=500.0), {"d_statutory_rate": 0.07}).dTaxRate == pytest.approx(0.07)
    clf = build_runner("industrials", "corporate_tax_rate_change").run().company("CLF")
    assert clf.baseline["pretax_income"] < 0 and clf.dNI == 0
    market = build_market_runner("corporate_tax_change").run()
    for ind in market.industries.values():
        for c in ind.companies:
            if c.baseline["pretax_income"] <= 0:
                assert c.dNI <= 1e-9, c.ticker


@pytest.mark.parametrize("industry,policy", [("consumer_retail", "import_tariffs"), ("transportation_logistics", "auto_import_tariffs")])
def test_tariff_inputs_are_increments_over_the_baseline(industry, policy):
    """Zero additional tariff leaves the (already tariff-inclusive) baseline unchanged; rollbacks help."""
    r = build_runner(industry, policy)
    zero = replace(r, inputs={"tariff_pct": 0}).run()
    assert not any(economic_effect(c) for c in zero.companies)
    up, down = replace(r, inputs={"tariff_pct": 10}).run(), replace(r, inputs={"tariff_pct": -10}).run()
    for c in up.companies:
        if c.dNI:
            assert c.dNI < 0 < down.company(c.ticker).dNI


def test_gm_tariff_cost_is_not_counted_twice_at_the_current_rate():
    """GM's 2025 baseline already includes the 25% Section 232 cost."""
    gm = build_runner("transportation_logistics", "auto_import_tariffs", inputs={"tariff_pct": 0}).run().company("GM")
    assert gm.dNI == 0


def test_us_pretax_proxy_tiers():
    """Derived and estimated US book-income proxies follow the documented hierarchy."""
    reg = registry()
    aapl = store.company_years("AAPL")
    latest = max(aapl, key=lambda y: y["period_end"])["items"]
    assert reg.exposure("AAPL", "audit_us_pretax_income_musd").value == pytest.approx(latest["pretax_income"] - latest["pretax_foreign"], abs=0.01)
    for t in ("MRK", "IBM", "INTC", "CNC", "F", "MDT"):  # US loss, total loss, or non-US incorporation
        assert not reg.exposure(t, "audit_us_pretax_income_musd").applicable
    for t, e in ((t, reg.exposures[t].get("audit_us_pretax_income_musd")) for t in reg.exposures):
        if e is not None and e.applicable:
            assert 0 < e.low <= e.value <= e.high, t


def test_audit_additions_have_filing_based_macro_tax_shares():
    """Newly admitted issuers no longer sit at a zero sentinel in the Full Market tax shock."""
    import json
    from policyshock.config import ROOT
    added = json.loads((ROOT / "data/universe_sources/admission_decisions.json").read_text())["added"]
    for t in added:
        e = registry().exposure(t, "mx_us_pretax_share")
        assert e.applicable and e.high > 0 and "XBRL" in e.source, t


def test_unlike_peer_priors_were_replaced():
    """Chip and grocery exposures are no longer copied from NVIDIA or general merchandisers."""
    reg = registry()
    nvda = reg.exposure("NVDA", "greater_china_revenue_share").value
    for t in ("QCOM", "AMD", "INTC"):
        e = reg.exposure(t, "greater_china_revenue_share")
        assert e.value != nvda and not e.rationale.startswith("Explicit modeling prior")
    assert reg.exposure("KR", "us_import_share_of_cogs").value < reg.exposure("WMT", "us_import_share_of_cogs").value
    assert reg.exposure("LUV", "tl_domestic_passenger_revenue_share").value > 0.85


def test_rate_cut_reaches_insurers_without_double_counting_banks():
    """Insurers reprice portfolios; banks keep only their 10-K NII channel."""
    r = build_runner("financial_services", "fed_rate_change", inputs={"d_rate_bps": -100}).run()
    for t in ("MET", "TRV", "ALL", "PGR"):
        assert r.company(t).dR < 0
    for c in r.companies:
        if c.baseline.get("kind") == "bank" or registry().exposure(c.ticker, "fs_investment_income_revenue_share").rationale.startswith("Company-specific scope estimate: Banks"):
            assert all(o.family != "price" or o.dNI == 0 for o in c.outcomes)


def test_grad_loan_caps_move_borrowing_to_private_lenders():
    """Schools lose above-cap graduate revenue while Sallie Mae gains it."""
    r = build_runner("education", "student_loan_borrowing_caps").run()
    assert r.company("SLM").dR > 0 > r.company("CVSA").dR


def test_tobacco_excise_is_monotone_and_scoped():
    """Only tobacco makers move; a larger tax cuts more volume; zero tax is zero."""
    r = build_runner("consumer_retail", "tobacco_excise_increase")
    vals = [replace(r, inputs={"d_cigarette_tax_per_pack": x, "oral_nicotine_tax_pct": 0}).run().company("MO").dR for x in (0, 0.5, 1.0, 2.0)]
    assert vals[0] == 0 and vals[1] > vals[2] > vals[3]
    base = r.run()
    assert all(base.company(t).dNI == 0 for t in ("TGT", "NKE", "KO", "WMT"))


def test_device_tariff_reaches_only_importers():
    """Drugmakers stay with the pharma tariff policy; device importers pay this one."""
    r = build_runner("healthcare", "medical_device_tariffs").run()
    assert r.company("MDT").dNI < 0 and r.company("ISRG").dNI < 0
    assert r.company("PFE").dNI == 0 and r.company("UNH").dNI == 0


def test_every_company_responds_to_a_specific_policy_or_is_documented():
    """No company silently drops out of policy coverage."""
    reg = registry()
    hit = set()
    for p in reg.policies.values():
        if p.id.startswith(("us_corporate_tax", "corporate_tax_rate_change")):
            continue
        hit.update(c.ticker for c in build_runner(p.industry, p.id).run().companies if economic_effect(c))
    orphans = set(load_universe().all_tickers) - hit
    assert orphans <= DOCUMENTED_ORPHANS, sorted(orphans - DOCUMENTED_ORPHANS)


def test_numeric_inputs_move_results_monotonically():
    """Sweep every numeric input min→max; each company's earnings move in one direction."""
    found = set()
    for key, p in registry().policies.items():
        runner = build_runner(p.industry, p.id)
        for u in p.user_inputs:
            if u.type != "number" or u.min is None or u.max is None:
                continue
            xs = [u.min + (u.max - u.min) * k / 6 for k in range(7)]
            runs = [replace(runner, inputs=runner.inputs | {u.key: x}).run() for x in xs]
            for t in runner.tickers:
                ys = [r.company(t).dNI for r in runs]
                steps = [b - a for a, b in zip(ys, ys[1:]) if abs(b - a) > 1e-6]
                if any(s > 0 for s in steps) and any(s < 0 for s in steps):
                    found.add((key, t))
    assert found <= VERIFIED_NON_MONOTONE, sorted(found - VERIFIED_NON_MONOTONE)

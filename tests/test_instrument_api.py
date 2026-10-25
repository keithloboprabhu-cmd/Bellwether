"""Exercise the browser/Python contract against committed, actual scenarios."""

import math

import pytest

from policyshock.engine.simulate import simulate
from policyshock.ui.api import calculate, catalog


def test_catalog_uses_actual_configuration():
    """The catalog derives coverage and bounds rather than hardcoding UI data."""
    cat = catalog()
    assert sum(i["count"] for i in cat["industries"]) == cat["company_count"]
    assert all(20 <= i["count"] <= 30 for i in cat["industries"])
    pol = next(p for i in cat["industries"] if i["id"] == "healthcare" for p in i["policies"] if p["id"] == "medicare_advantage_rate_change")
    assert pol["user_inputs"][0]["min"] == -10


def test_real_engine_result_and_scenario_range():
    """Serializing a real result preserves the reference calculation and range."""
    payload = {"industry": "healthcare", "policy": "medicare_advantage_rate_change", "inputs": {"rate_change_pct": -2}}
    actual = calculate(payload)
    reference = simulate("healthcare", "medicare_advantage_rate_change", inputs=payload["inputs"])
    assert actual["totals"]["d_eps_pct"] == reference.base.totals()["d_eps_pct"]
    assert actual["range"] == [reference.industry_low.totals()["d_eps_pct"], reference.industry_high.totals()["d_eps_pct"]]
    assert all(c["exposures"][0]["source"] for c in actual["companies"])
    assert sum(c["dNI"] for c in actual["channels"]) == pytest.approx(actual["totals"]["d_ni"])


@pytest.mark.parametrize("bad", [11, -11, math.nan, math.inf, "-2", True])
def test_invalid_inputs_are_not_substituted(bad):
    """Reject invalid browser/profile values instead of clamping or defaulting."""
    with pytest.raises(ValueError):
        calculate({"industry": "healthcare", "policy": "medicare_advantage_rate_change", "inputs": {"rate_change_pct": bad}})


def test_zero_shock_is_exactly_zero_and_missing_is_null():
    """Zero remains distinct from invalid denominators or absent values."""
    actual = calculate({"industry": "healthcare", "policy": "medicare_advantage_rate_change", "inputs": {"rate_change_pct": 0}})
    assert actual["totals"]["d_eps_pct"] == 0
    assert all(c["dEPS"] == 0 for c in actual["companies"])
    assert all(c["eps"] == 0 if c["baseline"]["eps_diluted"] > 0 else c["eps"] is None for c in actual["companies"])


def test_unavailable_version_rejected():
    """Links cannot silently calculate with different data from the named version."""
    with pytest.raises(ValueError, match="different model or data version"):
        calculate({"industry": "healthcare", "policy": "medicare_advantage_rate_change", "versions": {"model": "old", "data": "old"}})


def test_unknown_input_rejected():
    """Unknown values cannot make a plausible-looking scenario."""
    with pytest.raises(ValueError, match="unsupported input"):
        calculate({"industry": "healthcare", "policy": "medicare_advantage_rate_change", "inputs": {"bogus": 3}})


def test_projection_columns_follow_engine_deltas():
    """The console's absolute values use declared bases and the existing deltas."""
    actual = calculate({"industry": "healthcare", "policy": "medicare_advantage_rate_change"})
    for c in actual["companies"]:
        for name, delta in [("eps", c["dEPS"]), ("revenue", c["revenue"]), ("net_income", c["dNI"])]:
            metric = c["metrics"][name]
            assert metric["projected"] == pytest.approx(metric["baseline"] + delta)
        assert c["metrics"]["eps"]["percent"] == c["eps"]
        if c["metrics"]["price"]["projected"] is not None:
            assert c["metrics"]["price"]["projected"] == pytest.approx(c["baseline"]["price"] * (1 + c["value"]))
        model_ni = c["baseline"]["pretax_income"] * (1 - c["tax_rate"]) * c["baseline"].get("parent_share", 1)
        assert c["metrics"]["net_income"]["baseline"] == pytest.approx(model_ni)


def test_sparklines_are_actual_filed_history():
    """Charts cannot use invented price paths or simulated history as a filler."""
    from policyshock.data import store
    actual = calculate({"industry": "tmt", "policy": "app_store_commission_cap"})
    for c in actual["companies"]:
        assert c["history"] == [{"year": y["fiscal_year"], "eps": y["items"].get("eps_diluted")} for y in reversed(store.company_years(c["id"])[:8])]


def test_undefined_valuation_is_not_a_projected_zero():
    """A loss issuer's missing P/E valuation remains unavailable in absolute columns."""
    actual = calculate({"industry": "education", "policy": "online_compliance_costs"})
    losses = [c for c in actual["companies"] if c["baseline"]["eps_diluted"] <= 0 and c["dNI"] != 0]
    assert losses
    assert all(c["metrics"]["price"]["projected"] is None and c["metrics"]["eps"]["percent"] is None for c in losses)

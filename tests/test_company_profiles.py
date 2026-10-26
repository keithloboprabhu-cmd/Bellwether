"""Validate user profiles and their integration with the existing policy engine."""

import copy
import math

import pytest
from pydantic import ValidationError

from policyshock.company.profiles import CompanyProfile, lookup_company, peer_exposures, run_company, search_companies
from policyshock.data import store
from policyshock.policies.loader import registry
from policyshock.ui.api import calculate


@pytest.fixture
def profile():
    """Explicit illustrative user inputs, not a purported API company measurement."""
    return {
        "schema_version": 1, "name": "User-entered example", "ticker": "", "industry": "consumer_retail",
        "kind": "standard", "role": "importer",
        "financials": {"revenue": 1000, "cost_of_revenue": 600, "operating_income": 100,
                       "interest_expense": 10, "other_nonoperating_income": 0, "pretax_income": 90,
                       "effective_tax_rate": .21, "net_income": 71.1, "diluted_shares": 10, "price": 100},
        "exposures": {}, "financial_sources": {"all": "User input (estimate), illustrative test scenario."},
    }


def tariff():
    """Choose the configured retail tariff with its real required exposure schema."""
    return next(p for p in registry().industry_policies("consumer_retail") if any(c.type == "cost" for c in p.channels))


def populated(profile):
    """Use peer estimates only via the explicit opt-in operation."""
    p = copy.deepcopy(profile)
    pol = tariff()
    p["exposures"] = peer_exposures(p["industry"], pol.id, p["financials"]["revenue"])
    return p, pol


@pytest.mark.parametrize("field,value", [("diluted_shares", 0), ("revenue", math.nan), ("price", math.inf), ("effective_tax_rate", 1.1), ("pretax_income", 91), ("interest_expense", True)])
def test_invalid_financials_fail(profile, field, value):
    """Reject invalid denominators, non-finite/coerced values and broken identities."""
    profile["financials"][field] = value
    with pytest.raises(ValidationError):
        CompanyProfile.model_validate(profile)


def test_unknown_exposures_and_unsafe_source_urls_fail(profile):
    """A profile cannot smuggle unknown model inputs or executable source links."""
    profile["filing_url"] = "javascript:alert(1)"
    with pytest.raises(ValidationError, match="http or https"):
        CompanyProfile.model_validate(profile)
    profile.pop("filing_url")
    profile["exposures"] = {"unknown": {"value": 1, "source": "estimate", "rationale": "User input"}}
    with pytest.raises(ValidationError, match="unsupported"):
        CompanyProfile.model_validate(profile)


def test_no_silent_exposure_defaults(profile):
    """Financial statements alone cannot silently supply policy exposures."""
    with pytest.raises(ValueError, match="required policy exposures"):
        run_company(CompanyProfile.model_validate(profile), tariff().id, {})


def test_company_result_and_json_roundtrip(profile):
    """A portable profile runs on the same engine and keeps reference companies separate."""
    p, pol = populated(profile)
    validated = CompanyProfile.model_validate_json(CompanyProfile.model_validate(p).model_dump_json())
    expected = run_company(validated, pol.id, pol.default_inputs())
    actual = calculate({"industry": p["industry"], "policy": pol.id, "company": validated.model_dump(mode="json")})
    c = next(c for c in actual["companies"] if c["is_custom"])
    assert len(actual["companies"]) == 21
    assert actual["mode"] == "company"
    assert actual["totals"]["d_ni"] == pytest.approx(expected.base.companies[0].dNI)
    assert actual["totals"]["d_eps_pct"] == pytest.approx(c["dEPS"] / 7.11)
    assert sum(o["dNI"] for o in actual["channels"]) == pytest.approx(c["dNI"])
    assert actual["long"] != c["id"] and actual["short"] != c["id"]
    assert all(v["source"] == "estimate" and v["rationale"] for v in actual["profile"]["exposures"].values())


def test_zero_shock_and_no_price_are_explicit(profile):
    """Zero shock is exactly zero; absent price suppresses implied value."""
    p, pol = populated(profile)
    p["financials"].pop("price")
    an = run_company(CompanyProfile.model_validate(p), pol.id, {u.key: 0 for u in pol.user_inputs})
    c = an.base.companies[0]
    assert c.dNI == c.dEPS == 0
    assert c.dP_pct is None


def test_sensitivity_uses_reported_eps_denominator(profile):
    """Single-company tornado and headline use the same EPS definition."""
    p, pol = populated(profile)
    first = run_company(CompanyProfile.model_validate(p), pol.id, {})
    p["financials"]["eps_diluted"] = 14.22
    second = run_company(CompanyProfile.model_validate(p), pol.id, {})
    assert second.metric == "d_eps_pct"
    for a, b in zip(first.tornado, second.tornado):
        assert a.driver.key == b.driver.key
        assert b.low_value == pytest.approx(a.low_value / 2)
        assert b.high_value == pytest.approx(a.high_value / 2)


def test_loss_company_retains_absolute_eps_sensitivity(profile):
    """An undefined EPS percentage never discards the absolute earnings result."""
    p, pol = populated(profile)
    p["financials"]["net_income"] = -10
    an = run_company(CompanyProfile.model_validate(p), pol.id, {})
    assert an.base.companies[0].dEPS_pct is None
    assert an.metric == "d_eps"
    assert all(math.isfinite(b.low_value) for b in an.tornado)


def test_lookup_search_uses_real_directory(monkeypatch):
    """Directory search never creates an issuer and ranks an exact ticker first."""
    from policyshock.company import profiles
    monkeypatch.setattr(profiles.edgar, "company_directory", lambda: [{"ticker": "ADSK", "title": "AUTODESK INC", "cik_str": 769397}, {"ticker": "ADSKX", "title": "Other", "cik_str": 1}])
    assert search_companies("adsk")[0]["ticker"] == "ADSK"
    assert search_companies("no such issuer") == []


def test_known_lookup_preserves_missing_values():
    """An API gap stays missing and cannot become an unlabelled zero."""
    p = lookup_company("AAPL", "tmt")
    assert p["financials"]["interest_expense"] is None
    assert "Unavailable" in p["financial_sources"]["interest_expense"]
    assert p["filing_url"].startswith("https://www.sec.gov/")


def test_nonbank_scope_is_not_a_bank_exposure():
    """Payments/insurers/assets managers cannot receive bank-only mechanical effects."""
    actual = calculate({"industry": "financial_services", "policy": "fed_rate_change"})
    for c in actual["companies"]:
        if c["id"] in {"MA", "BLK", "AIG", "PRU", "PGR"}:
            assert c["dNI"] == 0
            assert all(not e["applicable"] for e in c["exposures"])
            assert c['coverage']['status'] == 'outside_scope'
            assert 'separate channels' in c['reason']


@pytest.mark.parametrize("ticker,expected", [("MCD", 716.4), ("LINC", 31.26)])
def test_documented_share_units(ticker, expected):
    """Issuer-reported millions/thousands cannot produce millionfold EPS changes."""
    f = store.fiscal_year(ticker)["items"]
    assert f["diluted_shares"] == pytest.approx(expected)
    assert f["net_income"] / (f["eps_diluted"] * f["diluted_shares"]) == pytest.approx(1, rel=.01)

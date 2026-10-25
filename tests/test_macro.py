"""Full Market shocks: smoke test on all 60 companies, plus the spec's sign tests."""

from __future__ import annotations

import math

import pytest

from policyshock.config import load_universe
from policyshock.macro.aggregate import simulate_market
from policyshock.policies.loader import registry

SHOCKS = sorted(registry().macro)


def _finite(x):
    return x is None or math.isfinite(x)


@pytest.mark.parametrize("shock_id", SHOCKS)
def test_shock_runs_on_all_60(shock_id):
    an = simulate_market(shock_id)
    assert set(an.base.industries) == {i.slug for i in load_universe().industries}
    assert len(an.base.companies) == len(load_universe().all_tickers)
    for c in an.base.companies:
        for f in ("dR", "dEBIT", "dNI", "dEPS", "dEPS_pct", "dP", "d_mcap"):
            assert _finite(getattr(c, f)), f"{shock_id} {c.ticker} {f}"
    assert all(_finite(v) for v in an.base.totals().values() if isinstance(v, float))
    lo, hi = an.market_low.totals()[an.metric], an.market_high.totals()[an.metric]
    base = an.base.totals()[an.metric]
    assert lo - 1e-12 <= base <= hi + 1e-12


@pytest.mark.parametrize("shock_id", SHOCKS)
def test_every_industry_explicit(shock_id):
    shock = registry().macro[shock_id]
    for slug, eff in shock.industry_effects.items():
        assert eff.channels or (eff.effect == "none" and eff.rationale), f"{shock_id}/{slug}"


def test_rates_up_banks_nii_up_reits_down():
    an = simulate_market("fed_rate_change", inputs={"d_ff_bps": 100})
    banks = an.base.industries["financial_services"]
    assert sum(c.dR for c in banks.companies) > 0  # NII up in the base case
    for t in ("PLD", "AMT", "SPG"):
        assert an.base.industries["real_estate_hospitality"].company(t).dP < 0


def test_second_round_toggle():
    on = simulate_market("fed_rate_change", inputs={"d_ff_bps": 100})
    off = simulate_market("fed_rate_change", inputs={"d_ff_bps": 100}, components=set())
    hd_on = on.base.industries["consumer_retail"].company("HD").dNI
    hd_off = off.base.industries["consumer_retail"].company("HD").dNI
    assert hd_on < hd_off  # second-round demand hit is extra


@pytest.mark.skipif("oil_supply_shock" not in SHOCKS, reason="oil shock not configured yet")
def test_oil_up_helps_producers_hurts_airlines():
    an = simulate_market("oil_supply_shock")
    energy = an.base.industries["energy_resources"]
    for t in ("XOM", "CVX", "COP"):
        assert energy.company(t).dEPS > 0
    assert an.base.industries["transportation_logistics"].company("DAL").dEPS < 0


def test_recession_betas_match_snapshot():
    """The recession shock's industry betas are copied from the committed GDP-beta fits."""
    from policyshock.macro import gdp_beta

    shock = registry().macro["recession_gdp_shock"]
    for slug, fit in gdp_beta.load().items():
        a = next(x for x in shock.industry_effects[slug].assumptions if x.key == f"gdp_beta_{slug}")
        assert a.base == pytest.approx(fit["beta"], abs=0.005), slug


def test_corporate_tax_spares_reits_and_hits_domestic_firms_most():
    an = simulate_market("corporate_tax_change", inputs={"d_rate_pts": 7})
    re = an.base.industries["real_estate_hospitality"]
    assert re.company("PLD").dNI == 0  # REIT: no corporate tax on distributed income
    cr = an.base.industries["consumer_retail"]
    assert cr.company("KO").dEPS_pct > cr.company("HD").dEPS_pct  # KO books most profit abroad


def test_strong_dollar_hurts_multinationals_not_domestic_utilities():
    an = simulate_market("strong_dollar")
    assert an.base.industries["consumer_retail"].company("KO").dNI < 0
    assert an.base.industries["energy_resources"].company("DUK").dNI == 0

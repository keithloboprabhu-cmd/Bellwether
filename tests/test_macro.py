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

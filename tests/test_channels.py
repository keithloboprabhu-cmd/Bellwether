"""Hand-calculated checks for every channel and for aggregation / valuation.

The toy company used throughout ($ millions):
    R = 1,000   C = 600 (cm 40%)   EBIT = 200   Int = 20   PTI = 180   t = 20%
    model NI = 144   S = 100 shares   EPS = 1.44   price = 28.80 (P/E 20)   D = 500
"""

from __future__ import annotations

import pytest

from policyshock.engine.channels import CHANNELS, run_channel
from policyshock.engine.model import ChannelOutcome, aggregate
from policyshock.engine.valuation import annuity_factor, earnings_multiple

B = {
    "ticker": "TOY",
    "name": "Toy Co",
    "revenue": 1000.0,
    "cost_of_revenue": 600.0,
    "contribution_margin": 0.4,
    "operating_income": 200.0,
    "interest_expense": 20.0,
    "pretax_income": 180.0,
    "effective_tax_rate": 0.20,
    "net_income": 144.0,
    "diluted_shares": 100.0,
    "shares_outstanding": 100.0,
    "eps_diluted": 1.44,
    "price": 28.8,
    "pe": 20.0,
    "total_debt": 500.0,
    "net_interest_income": 300.0,
}
approx = pytest.approx


def agg(*deltas, persistence="permanent", b=B):
    outs = [ChannelOutcome(label=f"c{i}", family="cost", persistence=persistence, delta=d) for i, d in enumerate(deltas)]
    return aggregate(dict(b), outs)


# ---------------------------------------------------------------- tax


def test_tax_rate_only_domestic_share_counts():
    d = run_channel("tax_rate", B, {"d_statutory_rate": -0.14, "domestic_income_share": 0.5})
    assert d.dTaxRate == approx(-0.07)
    r = agg(d)
    # t' = 13%: NI' = 180 × 0.87 = 156.6 → dNI = 12.6 (not double-counted)
    assert r.tax_rate_new == approx(0.13)
    assert r.dNI == approx(12.6)
    assert r.dEPS == approx(0.126)
    assert r.dP == approx(0.126 * 20)


def test_tax_credit_is_after_tax():
    d = run_channel("tax_credit", B, {"credit_rate": 0.10, "base_musd": 50})
    assert agg(d).dNI == approx(5.0)


def test_revenue_tax_is_deductible():
    d = run_channel("tax_revenue", B, {"rate": 0.03, "in_scope_share": 0.5})
    assert d.dOpex == approx(15.0)
    assert agg(d).dNI == approx(-15 * 0.8)


def test_full_expensing_is_timing_not_eps():
    d = run_channel("tax_timing", B, {"capex_musd": 100, "expensed_share": 1.0, "statutory_rate": 0.21, "discount_rate": 0.09, "recovery_years": 5})
    af5 = annuity_factor(5, 0.09)  # 3.8897
    assert d.dValue_pv == approx(0.21 * 100 * (1 - af5 / 5))  # ≈ 4.665
    r = agg(d)
    assert r.dNI == 0 and r.dEPS == 0
    assert r.dP == approx(d.dValue_pv / 100)


# ---------------------------------------------------------------- cost


def test_cost_no_pass_through():
    d = run_channel("cost", B, {"exposed_cost_share": 0.5, "shock_pct": 0.10})
    # dCost = 600 × 0.5 × 0.10 = 30, nothing passed on
    assert d.dR == approx(0) and d.dC == approx(30)
    assert agg(d).dNI == approx(-30 * 0.8)


def test_cost_with_pass_through_and_elasticity():
    d = run_channel("cost", B, {"exposed_cost_share": 0.5, "shock_pct": 0.10, "pass_through": 0.6, "elasticity": 1.0})
    dp = 0.6 * 30 / 1000  # 1.8% price rise
    dQ = -dp  # −1.8% volume
    assert d.dR == approx(1000 * ((1 + dp) * (1 + dQ) - 1))  # −0.324
    assert d.dC == approx(30 * (1 + dQ) + 600 * dQ)  # 29.46 − 10.8 = 18.66
    assert d.ebit == approx(d.dR - d.dC)


def test_domestic_producer_uplift():
    d = run_channel("domestic_uplift", B, {"domestic_sales_share": 0.8, "price_uplift": 0.05, "flow_through": 0.5})
    assert d.dR == approx(40) and d.ebit == approx(20)


# ---------------------------------------------------------------- demand / price


def test_demand_transfer():
    # $100B transfer, MPC 0.5, firm captures 1% of spending → dR = 500, dEBIT = 200
    d = run_channel("demand_transfer", B, {"total_transfer_musd": 100_000, "mpc": 0.5, "capture_share": 0.01})
    assert d.dR == approx(500) and d.ebit == approx(200)


def test_demand_price():
    d = run_channel("demand_price", B, {"dp_consumer": 0.02, "elasticity": 1.5, "exposed_revenue_share": 0.5})
    assert d.dR == approx(-15) and d.ebit == approx(-6)


def test_demand_volume():
    d = run_channel("demand_volume", B, {"d_volume": -0.10, "exposed_revenue_share": 0.3})
    assert d.dR == approx(-30) and d.ebit == approx(-12)


def test_price_with_offset():
    d = run_channel("price", B, {"d_price": -0.03, "exposed_revenue_share": 0.5, "offset_share": 0.4})
    assert d.dR == approx(-15) and d.ebit == approx(-9)


# ---------------------------------------------------------------- financing


def test_financing_debt():
    d = run_channel("financing_debt", B, {"d_rate_bps": 100, "floating_share": 0.3, "maturing_share": 0.1})
    assert d.dInt == approx(500 * 0.4 * 0.01)  # 2.0
    assert agg(d).dNI == approx(-2.0 * 0.8)


def test_financing_debt_zero_without_debt():
    d = run_channel("financing_debt", {**B, "total_debt": None}, {"d_rate_bps": 100})
    assert d.dInt == 0 and d.notes


def test_bank_nii():
    d = run_channel("bank_nii", B, {"d_rate_bps": -50, "nii_sensitivity_per_100bp": 0.02})
    assert d.dR == approx(-3.0) and d.ebit == approx(-3.0)


def test_bank_capital_value_only():
    d = run_channel("bank_capital", B, {"cet1_ratio": 0.12, "d_ratio": 0.01})
    assert d.dValue_pct == approx(0.12 / 0.13 - 1)
    r = agg(d)
    assert r.dNI == 0 and r.dP == approx(28.8 * (0.12 / 0.13 - 1))


def test_reit_nav():
    d = run_channel("reit_nav", B, {"d_10y_bps": 100, "cap_rate": 0.05, "cap_rate_beta": 0.5})
    assert d.dValue_pct == approx(-0.10)


# ---------------------------------------------------------------- government


def test_gov_budget():
    d = run_channel("gov_budget", B, {"gov_revenue_share": 0.8, "d_budget_pct": -0.05, "program_relevance": 0.5})
    assert d.dR == approx(-20) and d.ebit == approx(-8)


def test_gov_shutdown():
    d = run_channel("gov_shutdown", B, {"gov_revenue_share": 0.9, "days": 36.5, "affected_share": 0.5, "recovery_share": 0.6})
    assert d.dR == approx(-1000 * 0.9 * 0.5 * 0.1 * 0.4)


def test_gov_cr():
    d = run_channel("gov_cr", B, {"gov_revenue_share": 1.0, "months_delayed": 3, "new_award_share": 0.2})
    assert d.dR == approx(-50)


# ---------------------------------------------------------------- aggregation & valuation


def test_zero_shock_is_exactly_zero():
    """Regardless of reported NI, no shock means no change (model-baseline dNI)."""
    weird = {**B, "net_income": 999.0}  # reported NI ≠ PTI(1−t)
    r = agg(run_channel("cost", weird, {"exposed_cost_share": 0.5, "shock_pct": 0.0}), b=weird)
    assert r.dNI == 0 and r.dEPS == 0 and r.dP == 0


def test_attribution_sums_to_total():
    d1 = run_channel("tax_rate", B, {"d_statutory_rate": 0.05})
    d2 = run_channel("cost", B, {"exposed_cost_share": 0.5, "shock_pct": 0.10})
    d3 = run_channel("tax_credit", B, {"credit_rate": 0.1, "base_musd": 20})
    r = agg(d1, d2, d3)
    assert sum(o.dNI for o in r.outcomes) == approx(r.dNI)
    # by hand: PTI' = 150, t' = 25% → NI' = 112.5 + 2 = 114.5 → dNI = −29.5
    assert r.dNI == approx(-29.5)


def test_persistence_multiples():
    assert earnings_multiple("permanent", 20) == 20
    assert earnings_multiple("permanent", None) is None
    assert earnings_multiple("one_time", 20) == 1
    assert earnings_multiple("years:2", 20) == approx(1 / 1.09 + 1 / 1.09**2)


def test_one_time_value_and_nm_price():
    d = run_channel("demand_transfer", B, {"total_transfer_musd": 100_000, "mpc": 0.5, "capture_share": 0.01})
    r = agg(d, persistence="one_time")
    assert r.dP == approx(r.dEPS)  # one-time bump worth itself
    loss_maker = {**B, "eps_diluted": -0.5, "pe": None}
    r = agg(d, b=loss_maker)
    assert r.dEPS_pct is None and r.dP is None  # n/m for permanent with no P/E


def test_margin_bps():
    r = agg(run_channel("cost", B, {"exposed_cost_share": 0.5, "shock_pct": 0.10}))
    assert r.d_margin_bps == approx((170 / 1000 - 0.2) * 10_000)  # −300 bps


def test_every_registered_channel_has_a_test():
    tested = {
        "tax_rate", "tax_credit", "tax_revenue", "tax_timing", "cost", "domestic_uplift",
        "demand_transfer", "demand_price", "demand_volume", "price", "financing_debt",
        "bank_nii", "bank_capital", "reit_nav", "gov_budget", "gov_shutdown", "gov_cr",
    }
    assert set(CHANNELS) == tested

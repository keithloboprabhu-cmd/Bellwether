"""Tests for the SEC XBRL baseline parser (src/policyshock/data/baseline.py).

Two kinds of test:
1. Synthetic facts that pin down each parsing rule (duration filter, restatements,
   per-year tag fallback, managed-care costs, bank template, tax clamp).
2. Real trimmed company-facts fixtures, one company per industry, checked against
   figures reported in each company's 10-K (FY2017, chosen because it is also the
   TCJA backtest base year and the numbers are well documented).
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from policyshock.config import load_universe
from policyshock.data.baseline import annual_series, build_baseline, fiscal_year_label, shares_outstanding

FIXTURES = Path(__file__).parent / "fixtures"


def _fact(val, end, filed, start=None, form="10-K", accn="0000000000-00-000001"):
    row = {"val": val, "end": end, "filed": filed, "form": form, "accn": accn}
    if start:
        row["start"] = start
    return row


def _facts(**tags):
    """Build a minimal companyfacts payload: tag=[rows] (USD), eps/shares via suffix."""
    out = {"facts": {"us-gaap": {}, "dei": {}}}
    for tag, rows in tags.items():
        unit = "USD/shares" if tag.startswith("EarningsPerShare") else "shares" if "Shares" in tag else "USD"
        ns = "dei" if tag.startswith("Entity") else "us-gaap"
        out["facts"][ns][tag] = {"units": {unit: rows}}
    return out


# --------------------------------------------------------------------------- rules


def test_quarterly_facts_are_dropped():
    facts = _facts(
        Revenues=[
            _fact(100e6, "2024-12-31", "2025-02-01", start="2024-10-01"),  # Q4 only
            _fact(400e6, "2024-12-31", "2025-02-01", start="2024-01-01"),  # full year
        ]
    )
    s = annual_series(facts, "Revenues")
    assert s["2024-12-31"].value == 400e6


def test_restatement_latest_filed_wins():
    facts = _facts(
        Revenues=[
            _fact(400e6, "2023-12-31", "2024-02-01", start="2023-01-01", accn="A"),
            _fact(390e6, "2023-12-31", "2025-02-01", start="2023-01-01", accn="B"),  # restated comparative
        ]
    )
    assert annual_series(facts, "Revenues")["2023-12-31"].value == 390e6


def test_non_annual_forms_ignored():
    facts = _facts(Revenues=[_fact(400e6, "2024-12-31", "2025-02-01", start="2024-01-01", form="10-Q")])
    assert annual_series(facts, "Revenues") == {}


def test_tag_fallback_is_applied_per_year():
    """A company that switched revenue tags still gets revenue in both years."""
    facts = _facts(
        SalesRevenueNet=[_fact(90e6, "2017-12-31", "2018-02-01", start="2017-01-01")],
        RevenueFromContractWithCustomerExcludingAssessedTax=[_fact(100e6, "2018-12-31", "2019-02-01", start="2018-01-01")],
        NetIncomeLoss=[
            _fact(9e6, "2017-12-31", "2018-02-01", start="2017-01-01"),
            _fact(10e6, "2018-12-31", "2019-02-01", start="2018-01-01"),
        ],
    )
    years = {y.fiscal_year: y for y in build_baseline(facts)}
    assert years[2018].items["revenue"] == 100
    assert years[2018].tags["revenue"] == "RevenueFromContractWithCustomerExcludingAssessedTax"
    assert years[2017].items["revenue"] == 90
    assert years[2017].tags["revenue"] == "SalesRevenueNet"


def test_source_filing_is_first_10k_for_period():
    facts = _facts(
        Revenues=[
            _fact(400e6, "2023-12-31", "2024-02-01", start="2023-01-01", accn="ORIGINAL"),
            _fact(390e6, "2023-12-31", "2025-02-01", start="2023-01-01", accn="LATER"),
        ],
        NetIncomeLoss=[_fact(40e6, "2023-12-31", "2024-02-01", start="2023-01-01", accn="ORIGINAL")],
    )
    fy = build_baseline(facts)[0]
    assert fy.source_accn == "ORIGINAL"
    assert fy.items["revenue"] == 390  # but the value is the restated one


def test_tax_rate_clamped_and_defaulted():
    base = dict(
        Revenues=[_fact(1000e6, "2024-12-31", "2025-02-01", start="2024-01-01")],
        NetIncomeLoss=[_fact(100e6, "2024-12-31", "2025-02-01", start="2024-01-01")],
    )
    pti = "IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest"
    neg_tax = _facts(**base, **{pti: [_fact(100e6, "2024-12-31", "2025-02-01", start="2024-01-01")]},
                     IncomeTaxExpenseBenefit=[_fact(-20e6, "2024-12-31", "2025-02-01", start="2024-01-01")])
    fy = build_baseline(neg_tax)[0]
    assert fy.items["effective_tax_rate"] == 0.0
    assert fy.items["effective_tax_rate_raw"] == pytest.approx(-0.2)
    assert any("clamped" in f for f in fy.flags)

    loss = _facts(**base, **{pti: [_fact(-50e6, "2024-12-31", "2025-02-01", start="2024-01-01")]},
                  IncomeTaxExpenseBenefit=[_fact(-10e6, "2024-12-31", "2025-02-01", start="2024-01-01")])
    fy = build_baseline(loss)[0]
    assert fy.items["effective_tax_rate"] == 0.21
    assert any("21%" in f for f in fy.flags)


def test_cost_of_revenue_from_gross_profit():
    facts = _facts(
        Revenues=[_fact(1000e6, "2024-12-31", "2025-02-01", start="2024-01-01")],
        GrossProfit=[_fact(300e6, "2024-12-31", "2025-02-01", start="2024-01-01")],
        NetIncomeLoss=[_fact(100e6, "2024-12-31", "2025-02-01", start="2024-01-01")],
    )
    fy = build_baseline(facts)[0]
    assert fy.items["cost_of_revenue"] == 700
    assert fy.tags["cost_of_revenue"] == "= Revenue − GrossProfit"


def test_cost_of_revenue_left_missing_rather_than_guessed():
    """With no cost tags and no SG&A/R&D, deriving cost = R − EBIT would just echo
    the operating margin, so the parser flags it instead."""
    facts = _facts(
        Revenues=[_fact(1000e6, "2024-12-31", "2025-02-01", start="2024-01-01")],
        OperatingIncomeLoss=[_fact(50e6, "2024-12-31", "2025-02-01", start="2024-01-01")],
        NetIncomeLoss=[_fact(40e6, "2024-12-31", "2025-02-01", start="2024-01-01")],
    )
    fy = build_baseline(facts)[0]
    assert fy.items["cost_of_revenue"] is None
    assert any("industry default margin" in f for f in fy.flags)


def test_multi_class_shares_are_summed():
    facts = _facts(
        EntityCommonStockSharesOutstanding=[
            {"val": 600e6, "end": "2025-01-31", "filed": "2025-02-05", "form": "10-K", "accn": "X"},
            {"val": 400e6, "end": "2025-01-31", "filed": "2025-02-05", "form": "10-K", "accn": "X"},
            {"val": 900e6, "end": "2024-01-31", "filed": "2024-02-05", "form": "10-K", "accn": "W"},
        ]
    )
    so = shares_outstanding(facts)
    assert so["value"] == 1000 and so["classes"] == 2


def test_fiscal_year_label():
    assert fiscal_year_label("2026-01-31") == 2026  # Walmart fiscal 2026
    assert fiscal_year_label("2026-01-02") == 2025  # 52/53-week year ending first days of Jan
    assert fiscal_year_label("2025-09-27") == 2025


# --------------------------------------------------------------------------- fixtures

# (ticker, fiscal year, {item: value in $M or $/share}) — values as reported in each
# company's 10-K. Tolerance 0.5% allows for later restatements of comparatives.
REPORTED = [
    ("AAPL", 2017, {"revenue": 229234, "net_income": 48351}),
    ("JPM", 2017, {"net_income": 24441}),
    ("WMT", 2017, {"revenue": 485873}),
    ("UNH", 2017, {"revenue": 201159, "net_income": 10558}),
    ("NUE", 2017, {"net_income": 1318.7}),
    ("XOM", 2017, {"net_income": 19710}),
    ("DAL", 2017, {"revenue": 41244}),
    ("BAH", 2018, {"revenue": 6167.6}),
    ("PLD", 2017, {"revenue": 2618.1}),
]


def _load(ticker: str) -> list:
    facts = json.loads((FIXTURES / f"companyfacts_{ticker}.json").read_text())
    return build_baseline(facts, load_universe().company(ticker).kind)


@pytest.mark.parametrize("ticker,year,expected", REPORTED)
def test_fixture_matches_reported_10k(ticker, year, expected):
    fy = next(y for y in _load(ticker) if y.fiscal_year == year)
    for key, value in expected.items():
        assert fy.items[key] == pytest.approx(value, rel=0.005), f"{ticker} FY{year} {key}"


@pytest.mark.parametrize("ticker", ["AAPL", "JPM", "WMT", "UNH", "NUE", "XOM", "DAL", "BAH", "PLD", "CVSA"])
def test_fixture_latest_year_is_complete(ticker):
    """Every industry's fixture yields a usable latest year with tags recorded."""
    fy = _load(ticker)[0]
    it = fy.items
    assert it["revenue"] and it["revenue"] > 0
    assert it["net_income"] is not None
    assert it["diluted_shares"] and it["diluted_shares"] > 0
    assert 0.0 <= it["effective_tax_rate"] <= 0.40
    assert fy.source_accn, "latest year should link to its 10-K"
    assert "revenue" in fy.tags


def test_bank_template():
    fy = _load("JPM")[0]
    assert fy.items["net_interest_income"] and fy.items["net_interest_income"] > 0
    assert fy.items["cost_of_revenue"] is None
    assert fy.items["operating_income"] == fy.items["pretax_income"]


def test_managed_care_cost_includes_medical_claims():
    fy = _load("UNH")[0]
    cm = 1 - fy.items["cost_of_revenue"] / fy.items["revenue"]
    assert 0.05 < cm < 0.30, "medical costs must be in cost of revenue"
    assert "Policyholder" in fy.tags["cost_of_revenue"]


def test_predecessor_cik_merge_keeps_history():
    """XOM re-registered under a new holding-company CIK in 2026; history must survive."""
    years = [y.fiscal_year for y in _load("XOM")]
    assert 2017 in years and max(years) >= 2025


def test_near_duplicate_period_ends_collapse():
    """Two period ends 1 day apart are one fiscal year; the later filing wins."""
    facts = _facts(
        NetIncomeLoss=[
            _fact(10e6, "2015-10-31", "2015-12-10", start="2014-11-01", accn="OLD"),
            _fact(11e6, "2015-11-01", "2016-12-10", start="2014-11-02", accn="NEW"),
        ]
    )
    years = build_baseline(facts)
    assert len(years) == 1 and years[0].period_end == "2015-11-01"


def test_bank_revenue_components_and_pretax_precede_template_fallback():
    """Banks without a total-revenue/pretax tag retain their reported components."""
    def row(v):
        return [_fact(v, '2025-12-31', '2026-02-01', start='2025-01-01')]
    fy = build_baseline(_facts(InterestIncomeExpenseNet=row(100e6), NoninterestIncome=row(30e6),
                                NetIncomeLoss=row(20e6), IncomeTaxExpenseBenefit=row(5e6)), 'bank')[0]
    assert fy.items['revenue'] == 130
    assert fy.items['pretax_income'] == fy.items['operating_income'] == 25
    assert 'NoninterestIncome' in fy.tags['revenue']


def test_loss_basic_shares_fallback_has_explicit_estimate_provenance():
    """Loss-year basic shares are usable only as a documented diluted-share proxy."""
    def row(v):
        return [_fact(v, '2025-12-31', '2026-02-01', start='2025-01-01')]
    fy = build_baseline(_facts(Revenues=row(100e6), NetIncomeLoss=row(-10e6),
                               WeightedAverageNumberOfSharesOutstandingBasic=row(20e6)))[0]
    assert fy.items['diluted_shares'] == 20
    assert fy.estimates['diluted_shares']['source'] == 'estimate'
    assert fy.estimates['diluted_shares']['rationale']


def test_share_scale_is_explicit_and_preserves_per_share_eps():
    """Configured filing units scale counts; they cannot scale reported EPS."""
    def row(v):
        return [_fact(v, '2025-12-31', '2026-02-01', start='2025-01-01')]
    fy = build_baseline(_facts(NetIncomeLoss=row(100e6), EarningsPerShareDiluted=row(5),
                               WeightedAverageNumberOfDilutedSharesOutstanding=row(20)), share_scale=1e6)[0]
    assert fy.items['diluted_shares'] == 20
    assert fy.items['eps_diluted'] == 5
    assert any('normalized' in f for f in fy.flags)


def test_share_normalization_does_not_rescale_older_correct_facts():
    """A tagging change applies by filing date, not to an issuer's entire history."""
    facts = _facts(
        NetIncomeLoss=[_fact(100e6, '2020-12-31', '2021-02-01', start='2020-01-01'),
                       _fact(100e6, '2025-12-31', '2026-02-01', start='2025-01-01')],
        WeightedAverageNumberOfDilutedSharesOutstanding=[
            _fact(20e6, '2020-12-31', '2021-02-01', start='2020-01-01'),
            _fact(20, '2025-12-31', '2026-02-01', start='2025-01-01')],
    )
    years = build_baseline(facts, share_scale=1e6, share_scale_since_filed='2024-02-22')
    assert [y.items['diluted_shares'] for y in years] == [20, 20]

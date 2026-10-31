"""Regression cases from the 2026-10-31 quantitative audit brief."""

import pytest

from policyshock.data import store
from policyshock.engine.channels import Delta
from policyshock.engine.model import ChannelOutcome, aggregate
from policyshock.engine.simulate import simulate


def test_equity_floor_preserves_loss_arithmetic_and_attribution():
    """Equity can be wiped out while the underlying operating loss remains uncapped."""
    b = store.baseline_row("HUM", 10.)
    outcome = ChannelOutcome("Loss", "cost", "permanent", Delta(dOpex=1e9))
    c = aggregate({**b, "pe": 10., "valuation_pe": 10.}, [outcome])
    assert c.equity_wiped_out
    assert c.dP == -10. and b["price"] + c.dP == 0.
    assert c.unconstrained_dP < c.dP
    assert c.dNI < -1e6
    assert sum(o.dNI for o in c.outcomes) == pytest.approx(c.dNI)
    assert sum(o.dP for o in c.outcomes) == pytest.approx(c.dP)


def test_humana_ma_down_four_has_no_negative_share_price():
    """The exact reported Medicare Advantage scenario cannot project a negative stock price."""
    analysis = simulate("healthcare", "medicare_advantage_rate_change", inputs={"rate_change_pct": -4})
    for c in [analysis.base.company("HUM"), analysis.envelopes["HUM"].low, analysis.envelopes["HUM"].high]:
        assert c.dP is None or c.baseline["price"] + c.dP >= -1e-10


def test_depressed_eps_uses_supported_history_without_changing_reported_eps():
    """Normalization changes the valuation denominator, not the EPS change or profile format."""
    company = store.load_baselines()["companies"]["COF"]
    b = store.baseline_row("COF", 100.)
    assert b["eps_diluted"] == company["years"][0]["items"]["eps_diluted"]
    assert b["valuation_method"] == "three_year_median_eps"
    assert b["valuation_eps"] > b["eps_diluted"]
    assert b["valuation_pe"] < b["pe"]


@pytest.mark.parametrize("ticker", ["CMCSA", "MA", "NKE", "SCHL"])
def test_current_class_shares_replace_stale_companyfacts_cover_pages(ticker):
    """Current class counts must have their annual-filing date and include both classes."""
    company = store.load_baselines()["companies"][ticker]
    shares = company["shares_outstanding"]
    assert shares["date"] >= company["years"][0]["period_end"]
    assert shares["classes"] >= 2
    assert shares["source_url"].startswith("https://www.sec.gov/")


@pytest.mark.parametrize("ticker", ["F", "GM", "DE", "TXT"])
def test_captive_finance_debt_never_reprices_as_industrial_borrowings(ticker):
    """Both debt balances are sourced and visible; the financing channel uses industrial debt."""
    b = store.baseline_row(ticker, 100.)
    assert b["debt_basis"] == "industrial_only"
    assert b["total_debt"] > 0 and b["finance_arm_debt"] > 0
    assert any("industrial" in f.lower() or "financing channel" in f.lower() for f in b["flags"])


def test_unknown_debt_is_not_described_as_reported_zero():
    """No debt tag is a coverage failure, not an assertion that the firm has no debt."""
    from policyshock.data.baseline import build_baseline
    facts = {"facts": {"us-gaap": {"NetIncomeLoss": {"units": {"USD": [
        {"val": 1e6, "start": "2025-01-01", "end": "2025-12-31", "form": "10-K", "filed": "2026-02-01", "accn": "test"}]}}}}}
    y = build_baseline(facts)[0]
    assert y.items["total_debt"] is None
    assert not any("assumed 0" in f for f in y.flags)


def test_steel_buyer_and_producer_prices_match_official_distinct_metrics():
    """USITC table 5.2 reports separate blended-buyer and domestic-mill prices."""
    from policyshock.policies.loader import registry
    p = registry().policy("industrials", "steel_tariffs")
    assumptions = {a.key: a for a in p.assumptions}
    assert .25 * assumptions["price_response"].base == pytest.approx(.0239)
    assert .25 * assumptions["producer_price_response"].base == pytest.approx(.0074)


def test_inline_facts_keep_classes_scale_sign_and_periods():
    """Dimensional cover counts and signed monetary values keep their source context."""
    from policyshock.data.filing import parse_inline
    parsed = parse_inline('''<xbrli:context id="a"><xbrli:entity><xbrli:segment>
      <xbrldi:explicitMember dimension="us-gaap:StatementClassOfStockAxis">co:ClassA</xbrldi:explicitMember>
      </xbrli:segment></xbrli:entity><xbrli:period><xbrli:instant>2026-02-01</xbrli:instant></xbrli:period></xbrli:context>
      <ix:nonFraction name="dei:EntityCommonStockSharesOutstanding" contextRef="a" unitRef="shares" scale="6">1,234</ix:nonFraction>
      <ix:nonFraction name="co:Loss" contextRef="a" unitRef="USD" scale="6" sign="-">42</ix:nonFraction>''')
    assert parsed.contexts["a"]["instant"] == "2026-02-01"
    assert parsed.contexts["a"]["dimensions"]["us-gaap:StatementClassOfStockAxis"] == "co:ClassA"
    assert [f["value"] for f in parsed.facts] == [1234e6, -42e6]

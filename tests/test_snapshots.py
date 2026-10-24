"""Sanity checks on the committed snapshots the app reads on a cold start."""

from datetime import date

import pandas as pd

from policyshock.config import load_universe
from policyshock.data import fred, prices, store


def test_every_ticker_has_a_recent_baseline():
    companies = store.load_baselines()["companies"]
    universe = load_universe()
    assert set(companies) == set(universe.all_tickers)
    for t in universe.all_tickers:
        latest = companies[t]["years"][0]
        age_days = (date.today() - date.fromisoformat(latest["period_end"])).days
        assert age_days < 550, f"{t} latest fiscal year {latest['period_end']} looks stale"
        assert latest["items"]["net_income"] is not None


def test_baseline_rows_are_model_ready():
    px = prices.load_snapshot()
    df = store.baseline_frame(load_universe().all_tickers, px)
    assert df["price"].notna().all()
    assert df["diluted_shares"].gt(0).all()
    # P/E is only computed for positive EPS
    assert (df.loc[df["pe"].notna(), "eps_diluted"] > 0).all()


def test_prices_snapshot_covers_universe():
    px = prices.load_snapshot()
    assert set(px["ticker"]) == set(load_universe().all_tickers)
    assert (px["close"] > 0).all()


def test_fred_snapshot_has_all_series():
    latest = fred.latest_values()
    assert set(fred.SERIES) <= set(latest)
    assert isinstance(fred.load_snapshot()["date"].iloc[0], pd.Timestamp)

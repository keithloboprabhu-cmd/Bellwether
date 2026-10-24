"""Backtests run on the committed snapshot and give sensible results."""

from policyshock.backtests import tcja


def test_tcja_predicts_lower_rates():
    rows = tcja.run()
    s = tcja.summary(rows)
    assert s["n"] == len(tcja.TICKERS)
    assert all(r.predicted_change < 0 for r in rows)
    assert s["direction_hits"] >= s["n"] - 1
    assert s["mae"] < 0.06  # within 6 points on average


def test_tcja_base_year_precedes_enactment():
    for r in tcja.run():
        assert r.base_period <= "2017-11-30"
        assert all(p > "2018-01-01" for p in r.post_periods)

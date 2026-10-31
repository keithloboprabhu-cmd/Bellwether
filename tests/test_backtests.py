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


def test_steel_232_signs_and_nucor():
    from policyshock.backtests import steel_232

    rows = {r.ticker: r for r in steel_232.run()}
    assert rows["NUE"].pred_bps > 0 and rows["NUE"].actual_bps > 0  # domestic producer helped
    assert rows["CAT"].pred_bps < 0 and rows["DE"].pred_bps < 0  # steel users squeezed
    nue = rows["NUE"]
    # The annual observed change includes demand, mix and volume. Do not fit a
    # causal price response to the entire annual margin change to make this pass.
    assert nue.pred_high_bps < nue.actual_bps
    assert rows["DE"].note  # like-for-like cost recomputation applied

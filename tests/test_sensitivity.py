"""Ranges, tornado and long/short on a known policy (Consumer & Retail tariffs)."""

import pytest

from policyshock.engine.simulate import simulate


@pytest.fixture(scope="module")
def tariffs():
    return simulate("consumer_retail", "import_tariffs", inputs={"tariff_pct": 20})


def test_tariffs_hurt_every_importer(tariffs):
    assert all(c.dNI < 0 for c in tariffs.base.companies)


def test_tornado_sorted_by_swing(tariffs):
    swings = [b.swing for b in tariffs.tornado]
    assert swings == sorted(swings, reverse=True)
    assert tariffs.tornado[0].driver.key == "pass_through"


def test_higher_pass_through_helps_importers(tariffs):
    """Orientation must find that the *high* end of pass-through is the optimistic one."""
    bar = next(b for b in tariffs.tornado if b.driver.key == "pass_through")
    assert bar.high_value > bar.low_value


def test_industry_range_brackets_base(tariffs):
    lo = tariffs.industry_low.totals()["d_eps_pct"]
    base = tariffs.base.totals()["d_eps_pct"]
    hi = tariffs.industry_high.totals()["d_eps_pct"]
    assert lo <= base <= hi


def test_long_is_least_hurt(tariffs):
    ranked = sorted((c for c in tariffs.base.companies if abs(c.rank_value) > 1e-6), key=lambda c: c.rank_value)
    assert tariffs.short.ticker == ranked[0].ticker
    assert tariffs.long.ticker == ranked[-1].ticker
    assert any("least-hurt" in n for n in tariffs.notes)


def test_rebate_is_one_time_and_positive():
    an = simulate("consumer_retail", "consumer_tax_rebate")
    for c in an.base.companies:
        assert c.dNI > 0
        assert c.dP == pytest.approx(c.dEPS)  # one-time: valued at its own size


def test_edited_assumption_changes_result():
    base = simulate("consumer_retail", "consumer_tax_rebate").base.totals()["d_ni"]
    more = simulate(
        "consumer_retail", "consumer_tax_rebate", assumption_ranges={"mpc": (0.5, 0.9, 0.9)}
    ).base.totals()["d_ni"]
    assert more == pytest.approx(base * 0.9 / 0.7)


def test_unaffected_names_are_not_picked():
    """School-choice money only reaches LRN: a single call, no pair built from zeros."""
    an = simulate("education", "school_choice_esa")
    assert an.long is not None and an.long.ticker == "LRN"
    assert an.short is None

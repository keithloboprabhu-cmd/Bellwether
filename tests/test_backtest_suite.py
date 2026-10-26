"""Check benchmark coverage, scoring denominators and historical evidence."""

from datetime import date

import pytest

from policyshock.backtests.suite import _start, report, score
from policyshock.config import load_universe
from policyshock.data import store


@pytest.fixture(scope="module")
def benchmark():
    """Compute the deterministic industry suite once for this test module."""
    return report()


def test_sign_score_does_not_count_missing_or_unaffected_as_correct():
    """An observed zero misses a nonzero forecast; absent predictions stay excluded."""
    result = score([{"predicted": 2, "actual": 10}, {"predicted": -2, "actual": -1},
                    {"predicted": 2, "actual": 0}, {"predicted": 0, "actual": 8},
                    {"predicted": None, "actual": -1}, {"predicted": 1, "actual": float("nan")}])
    assert result["n"] == 3 and result["hits"] == 2
    assert result["accuracy_pct"] == pytest.approx(200 / 3)
    assert score([])["accuracy_pct"] is None


def test_every_industry_has_a_case_and_every_company_is_accounted_for(benchmark):
    """Sector coverage cannot conceal omitted or outcome-selected companies."""
    assert {c["industry"] for c in benchmark["cases"]} == {i.slug for i in load_universe().industries}
    for c in benchmark["cases"]:
        included = [r["ticker"] for r in c["rows"]]
        excluded = [r["ticker"] for r in c["excluded"]]
        assert len(included + excluded) == len(set(included + excluded))
        assert set(included + excluded) == set(load_universe().industry(c["industry"]).tickers)
        assert c["summary"]["n"] > 0


def test_overall_score_reconciles_to_displayed_rows(benchmark):
    """The headline is a pooled hit count, not an average of convenient cases."""
    rows = [r for c in benchmark["cases"] for r in c["rows"]]
    hits = sum(r["direction_ok"] for r in rows)
    assert benchmark["summary"]["n"] == len(rows)
    assert benchmark["summary"]["hits"] == hits
    assert benchmark["summary"]["accuracy_pct"] == pytest.approx(100 * hits / len(rows))
    assert "mae" not in benchmark["summary"]  # incompatible units must not be pooled


def test_evidence_and_pre_policy_periods_are_real(benchmark):
    """Every reported observation points to the same committed historical record."""
    for case in benchmark["cases"]:
        for row in case["rows"]:
            assert row["base_period"] < min(row["post_periods"])
            periods = {y["period_end"]: y for y in store.company_years(row["ticker"])}
            assert row["error"] == pytest.approx(row["predicted"] - row["actual"])
            for f in row["filings"]:
                assert f["url"] == periods[f["period"]]["filing_url"]
                assert f["url"].startswith("https://www.sec.gov/")
            if case["id"].startswith("tcja-"):
                assert row["base_period"] < "2017-12-01"
                assert len(row["post_periods"]) == 2
                years = store.company_years(row["ticker"])
                assert all(_start(periods[p], years) >= date(2018, 1, 1) for p in row["post_periods"])


def test_fiscal_year_start_respects_adjacent_fifty_two_week_period():
    """A January fiscal year must not accidentally include a partial policy year."""
    prior = {"period_end": "2017-12-30"}
    following = {"period_end": "2018-12-29"}
    assert _start(following, [prior, following]) == date(2017, 12, 31)

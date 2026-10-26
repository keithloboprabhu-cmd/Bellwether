"""Live-data isolation, fallback, provider timestamps and engine integration."""

from copy import deepcopy

import pytest

from policyshock.data import live, store
from policyshock.ui import api


def test_capture_is_immutable_and_committed_history_is_unchanged(tmp_path):
    """A later provider update cannot alter an in-flight calculation or history."""
    service = live.LiveData(tmp_path / "state.json")
    service.active = True
    original = deepcopy(store.fiscal_year("AAPL"))
    service.state["quotes"]["AAPL"] = {"ticker": "AAPL", "close": 150., "date": "2090-01-01T15:00:00+00:00", "source": "yfinance", "retrieved_at": "2090-01-01T15:00:05+00:00"}
    old = service.capture()
    service.state["quotes"]["AAPL"]["close"] = 175.
    new = service.capture()
    assert service.baseline_rows(["AAPL"], old)[0]["price"] == 150.
    assert service.baseline_rows(["AAPL"], new)[0]["price"] == 175.
    assert old["data_version"] != new["data_version"]
    assert store.fiscal_year("AAPL") == original


def test_provider_failure_keeps_last_success_and_original_observation(tmp_path, monkeypatch):
    """A failed refresh must not label old values as newly observed."""
    service = live.LiveData(tmp_path / "state.json")
    quote = {"ticker": "AAPL", "close": 150., "date": "2090-01-01T15:00:00+00:00", "source": "yfinance"}
    service.state["quotes"]["AAPL"] = quote.copy()
    monkeypatch.setattr(live, "fetch_quotes", lambda _: [])
    service._refresh_provider("quotes")
    assert service.state["quotes"]["AAPL"] == quote
    assert service.status()["providers"]["quotes"]["error"]
    assert not service.status()["providers"]["quotes"]["refreshing"]


def test_live_annual_override_changes_engine_inputs_without_rewriting_snapshots(tmp_path, monkeypatch):
    """Current annual figures feed the real engine; backtests retain original facts."""
    service = live.LiveData(tmp_path / "state.json")
    service.active = True
    co = deepcopy(store.load_baselines()["companies"]["UNH"])
    original_revenue = co["years"][0]["items"]["revenue"]
    co["years"][0]["items"]["revenue"] *= 1.1
    co["checked_at"] = "2090-01-01T15:00:00+00:00"
    service.state["financials"]["UNH"] = co
    monkeypatch.setattr(live, "service", service)
    result = api.calculate({"industry": "healthcare", "policy": "medicare_advantage_rate_change", "inputs": {"rate_change_pct": -2}})
    row = next(c for c in result["companies"] if c["id"] == "UNH")
    assert row["baseline"]["revenue"] == pytest.approx(original_revenue * 1.1)
    assert row["baseline"]["financial_source"] == "SEC EDGAR API"
    assert result["versions"]["data"] == service.capture()["data_version"]
    assert store.fiscal_year("UNH")["items"]["revenue"] == original_revenue


def test_inactive_service_uses_committed_inputs(tmp_path):
    """Importing the library never starts network refresh work."""
    service = live.LiveData(tmp_path / "state.json")
    assert not service.active
    row = service.baseline_rows(["JPM"], service.capture())[0]
    assert row["financial_source"] == "committed SEC snapshot"
    assert row["price_source"] == "snapshot"


def test_metrics_rejects_unsafe_ticker_before_contacting_provider(tmp_path):
    """Only literal ticker symbols reach Yahoo, never arbitrary paths or URLs."""
    service = live.LiveData(tmp_path / "state.json")
    for ticker in ["https://example.com", "../../AAPL", "AAPL?x=1"]:
        with pytest.raises(ValueError, match="valid ticker"):
            service.company_metrics(ticker)

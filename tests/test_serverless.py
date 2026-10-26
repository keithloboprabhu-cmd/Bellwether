"""Vercel request lifecycle, bounded refresh batches and the real HTTP contract."""

from concurrent.futures import ThreadPoolExecutor
from io import BytesIO
import json
import subprocess
import sys
import threading

from policyshock.config import ROOT, load_universe
from policyshock.data import live
from policyshock.ui import api


def test_request_refresh_finishes_and_prioritizes_selected_industry(tmp_path, monkeypatch):
    """No provider work survives a response; only selected firms consume quote work."""
    service = live.LiveData(tmp_path / "state.json")
    service.active = service.request_driven = True
    selected = load_universe().industry("financial_services").tickers
    calls = []

    def fetch(provider, keys):
        calls.append((provider, keys))
        with service.lock:
            for key in keys:
                service.state[provider][key] = {"retrieved_at": live._now(), "checked_at": live._now()}
            service.running.discard(provider)

    monkeypatch.setattr(service, "_refresh_provider", fetch)
    service.refresh_for_request(selected)
    assert dict(calls)["quotes"] == selected
    assert len(dict(calls)["financials"]) == 1
    assert len(dict(calls)["fred"]) == 2
    assert not service.running
    first_financial = dict(calls)["financials"][0]
    calls.clear()
    service.refresh_for_request(selected)
    assert "quotes" not in dict(calls)
    assert dict(calls)["financials"][0] != first_financial
    assert len(dict(calls)["fred"]) == 2


def test_concurrent_refresh_coalesces_and_failed_records_rotate(tmp_path, monkeypatch):
    """An unavailable company must not starve other records or trigger duplicate jobs."""
    service = live.LiveData(tmp_path / "state.json")
    service.active = service.request_driven = True
    entered, release = threading.Event(), threading.Event()
    calls = []

    def fetch(provider, keys):
        calls.append((provider, keys))
        entered.set()
        assert release.wait(5)
        with service.lock:
            service.running.discard(provider)

    monkeypatch.setattr(service, "_refresh_provider", fetch)
    with ThreadPoolExecutor(max_workers=1) as pool:
        pending = pool.submit(service.refresh_for_request)
        assert entered.wait(5)
        assert service.refresh_for_request()["providers"]["quotes"]["refreshing"]
        release.set()
        pending.result()
    assert len(calls) == 3
    first_quote_batch = set(dict(calls)["quotes"])
    calls.clear()
    service.refresh_for_request()
    assert not first_quote_batch.intersection(dict(calls)["quotes"])


def test_partial_provider_batch_does_not_claim_unrequested_firms_failed(tmp_path, monkeypatch):
    """One successful quote batch retains provenance and doesn't fail the other 202 firms."""
    service = live.LiveData(tmp_path / "state.json")
    service.active = True
    monkeypatch.setattr(live, "fetch_quotes", lambda tickers: [
        {"ticker": "AAPL", "close": 150., "date": "2090-01-01T15:00:00+00:00",
         "source": "yfinance", "retrieved_at": live._now()}])
    service._refresh_provider("quotes", ["AAPL"])
    assert service.state["status"]["quotes"]["missing"] == []
    assert service.state["status"]["quotes"]["error"] is None
    assert service.capture()["prices"].set_index("ticker").loc["AAPL", "close"] == 150
    assert json.loads(service.cache.read_text())["quotes"]["AAPL"]["date"].startswith("2090")


def test_serverless_http_uses_same_engine_and_validates_before_refresh(tmp_path, monkeypatch):
    """Exercise real requests, error responses and custom-company entrypoint bootstrap."""
    import importlib.util

    service = live.LiveData(tmp_path / "state.json")
    monkeypatch.setattr(live, "service", service)
    spec = importlib.util.spec_from_file_location("bellwether_vercel_test", ROOT / "api/index.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    calls = []
    monkeypatch.setattr(service, "refresh_for_request", lambda tickers=None: calls.append(tickers) or service.status())

    def request(path, payload=None):
        class Connection:
            def makefile(self, mode, buffering=-1):
                return BytesIO(wire)

            def sendall(self, data):
                output.write(data)

        body = json.dumps(payload).encode() if payload is not None else b""
        method = "POST" if payload is not None else "GET"
        wire = f"{method} {path} HTTP/1.0\r\nContent-Length: {len(body)}\r\nContent-Type: application/json\r\n\r\n".encode() + body
        output = BytesIO()
        module.handler(Connection(), ("127.0.0.1", 1), object())
        headers, response = output.getvalue().split(b"\r\n\r\n", 1)
        return headers.decode(), json.loads(response)

    assert request("/api/catalog")[1]["company_count"] == 203
    assert not calls
    assert "Reported financials" in request("/api/methodology")[1]["text"]
    payload = {"industry": "financial_services", "policy": "fdic_assessment_increase", "inputs": {"d_rate_bp": 2}}
    headers, result = request("/api/scenario", payload)
    assert "Cache-Control: no-store" in headers
    assert calls == [load_universe().industry("financial_services").tickers]
    assert result["totals"]["d_ni"] < 0
    aig = next(c for c in result["companies"] if c["id"] == "AIG")
    assert aig["dNI"] == 0
    calls.clear()
    headers, result = request("/api/scenario", {**payload, "inputs": {"d_rate_bp": "bad"}})
    assert "422" in headers and result["error"]
    assert not calls


def test_vercel_bootstrap_writes_only_temporary_caches(tmp_path):
    """A fresh cloud process puts SEC, Yahoo and live caches outside the read-only repo."""
    import os

    result = subprocess.run([sys.executable, "-c", """
import importlib.util
from pathlib import Path
import tempfile
spec = importlib.util.spec_from_file_location('cloud', 'api/index.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
from policyshock.data import edgar, live
assert edgar.CACHE_DIR.is_relative_to(Path(tempfile.gettempdir()).resolve())
assert not edgar.CACHE_DIR.is_relative_to(Path.cwd())
assert not live.CACHE.is_relative_to(Path.cwd())
assert live.service.active and live.service.request_driven
assert not live.service.running
"""], cwd=ROOT, env={**os.environ, "VERCEL": "1", "TMPDIR": str(tmp_path)}, capture_output=True, text=True)
    assert result.returncode == 0, result.stderr

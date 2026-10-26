"""Nonblocking public-data refresh with immutable per-request captures.

Quotes refresh every five minutes, FRED hourly, SEC annual statements every six
hours. Provider failures retain the last successful data and its original time.
Committed histories remain untouched for historical backtests.
"""

from __future__ import annotations

import hashlib
import json
import math
import re
import threading
import time
import warnings
from concurrent.futures import ThreadPoolExecutor
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

from policyshock.config import CACHE_DIR, load_universe
from policyshock.data import edgar, fred, prices, store
from policyshock.data.baseline import build_baseline, shares_outstanding

CACHE = CACHE_DIR / "live/state.json"
INTERVALS = {"quotes": 300, "fred": 3600, "financials": 21600}


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _number(value, positive=False):
    return float(value) if isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value) and (not positive or value > 0) else None


def fetch_quotes(tickers: list[str]) -> list[dict]:
    """Fetch latest available five-minute Yahoo observations, retaining market time."""
    import yfinance as yf

    rows = []
    # Bounded concurrency avoids launching hundreds of simultaneous Yahoo calls.
    for start in range(0, len(tickers), 40):
        batch = tickers[start:start + 40]
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", message="The inplace keyword.*")
            data = yf.download(batch, period="5d", interval="5m", auto_adjust=False,
                               progress=False, threads=4, timeout=10, group_by="column")
        if data.empty or "Close" not in data:
            continue
        closes = data["Close"]
        if isinstance(closes, pd.Series):
            closes = closes.to_frame(batch[0])
        for ticker in batch:
            if ticker not in closes:
                continue
            s = closes[ticker].dropna()
            if s.empty:
                continue
            value = _number(float(s.iloc[-1]), True)
            if value is None:
                continue
            stamp = pd.Timestamp(s.index[-1])
            if stamp.tzinfo is None:
                # yfinance intraday indexes normally carry an exchange timezone.
                continue
            rows.append({"ticker": ticker, "close": value,
                         "date": stamp.tz_convert("UTC").isoformat(),
                         "source": "yfinance", "retrieved_at": _now(),
                         "interval": "5m", "delayed_possible": True})
    return rows


class LiveData:
    """Provider-isolated refresh jobs; only validated successes replace cached values."""

    def __init__(self, cache: Path = CACHE):
        self.cache = cache
        self.lock = threading.RLock()
        self.active = False
        self.request_driven = False
        self.running: set[str] = set()
        self.attempted: dict[str, float] = {}
        self.state = {"quotes": {}, "fred": {}, "financials": {}, "status": {}}
        self.metrics_cache: dict[str, tuple[float, dict]] = {}
        self.record_attempted: dict[tuple[str, str], float] = {}
        try:
            data = json.loads(cache.read_text())
            if isinstance(data, dict) and all(isinstance(data.get(k), dict) for k in self.state):
                self.state = data
        except (OSError, ValueError):
            pass

    def start(self) -> None:
        """Enable refresh only in the serving process, never during library import/tests."""
        if self.active:
            return
        self.active = True
        self.refresh()

        def schedule():
            while self.active:
                time.sleep(30)
                self.refresh()

        threading.Thread(target=schedule, name="public-data-schedule", daemon=True).start()

    def refresh(self) -> dict:
        """Queue due providers without blocking HTTP, coalescing concurrent requests."""
        if self.request_driven:
            return self.refresh_for_request()
        with self.lock:
            if not self.active:
                return self.status()
            for provider, ttl in INTERVALS.items():
                status = self.state["status"].get(provider, {})
                last = status.get("success_epoch", 0)
                # Failed sources retry at most once a minute; manual refresh obeys TTL.
                if provider in self.running or time.time() - last < ttl or time.time() - self.attempted.get(provider, 0) < 60:
                    continue
                self.running.add(provider)
                self.attempted[provider] = time.time()
                threading.Thread(target=self._refresh_provider, args=(provider,), name=f"refresh-{provider}", daemon=True).start()
            return self.status()

    def refresh_for_request(self, tickers: list[str] | None = None) -> dict:
        """Finish a bounded batch before returning on hosts without a scheduler.

        Scenarios prioritize their industry; the Data page rotates through the
        universe. Per-record TTLs prevent a partial refresh marking all firms fresh.
        No provider worker survives the request, and failures keep prior values.
        """
        if not self.active:
            return self.status()
        universe = load_universe().all_tickers
        selected = [t for t in (tickers or universe) if t in universe]
        jobs = []
        with self.lock:
            for provider, keys, limit in (("quotes", selected, 30 if tickers else 12),
                                          ("financials", selected, 1),
                                          ("fred", list(fred.SERIES), 2)):
                if provider in self.running:
                    continue
                def checked(key):
                    value = self.state[provider].get(key, {})
                    stamp = value.get("checked_at" if provider == "financials" else "retrieved_at")
                    try:
                        return datetime.fromisoformat(stamp).timestamp() if stamp else 0
                    except (ValueError, TypeError):
                        return 0
                due = [k for k in keys if time.time() - checked(k) >= INTERVALS[provider]
                       and time.time() - self.record_attempted.get((provider, k), 0) >= 60]
                due.sort(key=lambda k: (checked(k), self.record_attempted.get((provider, k), 0)))
                batch = due[:limit]
                if batch:
                    for key in batch:
                        self.record_attempted[provider, key] = time.time()
                    self.running.add(provider)
                    jobs.append((provider, batch))
        # The context manager joins every task before returning to Vercel.
        with ThreadPoolExecutor(max_workers=3) as pool:
            futures = [pool.submit(self._refresh_provider, provider, keys) for provider, keys in jobs]
            for future in futures:
                future.result()
        return self.status()

    def _save(self):
        self.cache.parent.mkdir(parents=True, exist_ok=True)
        tmp = self.cache.with_suffix(".tmp")
        tmp.write_text(json.dumps(self.state, allow_nan=False, separators=(",", ":")))
        tmp.replace(self.cache)

    def _refresh_provider(self, provider, keys=None):
        try:
            if provider == "quotes":
                fetched = fetch_quotes(keys if keys is not None else load_universe().all_tickers)
                if not fetched:
                    raise ValueError("Yahoo returned no valid quotes")
                values = {r["ticker"]: r for r in fetched}
            elif provider == "fred":
                values, errors = {}, []
                for sid in (keys if keys is not None else fred.SERIES):
                    try:
                        series = fred.fetch_series(sid)
                        if len(series):
                            values[sid] = {"value": float(series.iloc[-1]), "date": series.index[-1].date().isoformat(), "label": fred.SERIES[sid], "retrieved_at": _now(), "source": "FRED fredgraph CSV"}
                    except Exception:
                        errors.append(sid)
                if not values:
                    raise ValueError("FRED returned no series")
            else:
                values, errors = {}, []
                companies = store.load_baselines()["companies"]

                def fetch_one(ticker):
                    old, co = companies[ticker], load_universe().company(ticker)
                    facts = edgar.merged_company_facts([old["cik"], *co.predecessor_ciks], max_age_s=INTERVALS["financials"])
                    parsed = build_baseline(facts, co.kind, cost_basis=co.cost_basis,
                        share_scale={"shares": 1, "thousands": 1000, "millions": 1000000}[co.reported_share_unit], share_scale_since_filed=co.share_unit_since_filed)
                    if not parsed:
                        raise ValueError("No supported annual SEC facts")
                    latest = parsed[0].to_dict()
                    if not all(_number(latest["items"].get(k)) is not None for k in ("revenue", "operating_income", "diluted_shares")) or latest["items"]["revenue"] <= 0 or latest["items"]["diluted_shares"] <= 0:
                        raise ValueError("Incomplete latest annual SEC statement")
                    years = [{**y.to_dict(), "filing_url": edgar.filing_url(y.source_cik or old["cik"], y.source_accn) if y.source_accn else None} for y in parsed]
                    return ticker, {**old, "years": years, "shares_outstanding": shares_outstanding(facts), "checked_at": _now(), "source": "SEC EDGAR API"}

                with ThreadPoolExecutor(max_workers=3) as pool:
                    futures = {t: pool.submit(fetch_one, t) for t in (keys if keys is not None else load_universe().all_tickers)}
                    for ticker, future in futures.items():
                        try:
                            t, co = future.result()
                            values[t] = co
                        except Exception:
                            errors.append(ticker)
                if not values:
                    raise ValueError("SEC returned no supported annual statements")
            with self.lock:
                # Preserve newer observations if a provider temporarily returns older data.
                for key, value in values.items():
                    previous = self.state[provider].get(key)
                    date_key = "date" if provider != "financials" else None
                    newer = not previous or (value[date_key] >= previous[date_key] if date_key else value["years"][0]["period_end"] >= previous["years"][0]["period_end"])
                    if newer:
                        self.state[provider][key] = value
                requested = keys if keys is not None else (load_universe().all_tickers if provider != "fred" else fred.SERIES)
                missing = sorted(set(requested) - set(values))
                self.state["status"][provider] = {"checked_at": _now(), "success_epoch": time.time(), "updated": len(values), "missing": missing, "error": None if not missing else f"Partial refresh: {len(missing)} unavailable; prior data retained"}
                self._save()
        except Exception as exc:
            with self.lock:
                previous = self.state["status"].get(provider, {})
                self.state["status"][provider] = {**previous, "checked_at": _now(), "error": str(exc)}
        finally:
            with self.lock:
                self.running.discard(provider)

    def status(self) -> dict:
        """Return honest retrieval status, retaining observation times separately."""
        with self.lock:
            return {"enabled": self.active, "refresh_mode": "request" if self.request_driven else "background", "providers": {k: {**deepcopy(self.state["status"].get(k, {})), "refreshing": k in self.running, "refresh_seconds": ttl, "cached_records": len(self.state[k])} for k, ttl in INTERVALS.items()},
                    "quote_note": "Latest available Yahoo five-minute observations; delays are possible. Outside market hours, the last market observation remains visible.",
                    "financial_note": "Financial statements are latest filed annual SEC data; market metrics may be trailing twelve months. Economic releases update on their publication schedules."}

    def capture(self) -> dict:
        """Freeze one request's quotes, macro and annual statements; never read mid-refresh."""
        with self.lock:
            state = deepcopy(self.state)
            status = self.status()
        px = prices.load_snapshot()
        px["retrieved_at"] = None
        px["interval"] = "daily close"
        if self.active and state["quotes"]:
            px = pd.concat([px, pd.DataFrame(state["quotes"].values())], ignore_index=True)
            px = px.sort_values("date").drop_duplicates("ticker", keep="last")
        macro = fred.latest_values()
        if self.active:
            for sid, value in state["fred"].items():
                if sid not in macro or value["date"] >= macro[sid]["date"]:
                    macro[sid] = value
        committed = store.load_baselines()["companies"]
        companies = {t: co for t, co in state["financials"].items()
                     if t in committed and co.get("years") and co["years"][0]["period_end"] >= committed[t]["years"][0]["period_end"]} if self.active else {}
        content = {"quotes": px.where(pd.notna(px), None).to_dict("records"), "macro": macro, "financials": companies}
        fingerprint = hashlib.sha256(json.dumps(content, sort_keys=True, default=str).encode()).hexdigest()[:16]
        return {"prices": px, "macro": macro, "companies": companies, "status": status,
                "data_version": fingerprint, "captured_at": _now()}

    def baseline_rows(self, tickers: list[str], captured: dict) -> list[dict]:
        """Build current engine inputs with quote and SEC provenance attached."""
        px = captured["prices"].set_index("ticker")
        out = []
        for ticker in tickers:
            quote = px.loc[ticker].to_dict() if ticker in px.index else {}
            co = captured["companies"].get(ticker)
            b = store.baseline_row(ticker, quote.get("close"), quote.get("date"), company=co)
            b.update({"price_source": quote.get("source", "snapshot"), "quote_retrieved_at": quote.get("retrieved_at"), "financials_checked_at": co.get("checked_at") if co else None,
                      "financial_source": "SEC EDGAR API" if co else "committed SEC snapshot"})
            out.append(b)
        return out

    def company_metrics(self, ticker: str) -> dict:
        """Fetch Yahoo's current/TTM metrics on demand with a five-minute cache."""
        ticker = ticker.strip().upper()
        if not re.fullmatch(r"[A-Z0-9][A-Z0-9.\-]{0,19}", ticker):
            raise ValueError("Provide a valid ticker")
        with self.lock:
            previous = self.metrics_cache.get(ticker)
            if previous and time.time() - previous[0] < 300:
                return deepcopy(previous[1])
        try:
            import yfinance as yf
            info = yf.Ticker(ticker).get_info()
            keys = ["regularMarketPrice", "currentPrice", "marketCap", "enterpriseValue", "trailingPE", "forwardPE", "trailingEps", "forwardEps", "totalRevenue", "netIncomeToCommon", "profitMargins", "sharesOutstanding", "regularMarketTime", "mostRecentQuarter"]
            values = {k: _number(info.get(k)) for k in keys}
            if not any(v is not None for v in values.values()):
                raise ValueError("Yahoo returned no company metrics")
            result = {"ticker": ticker, "currency": info.get("currency"), "financial_currency": info.get("financialCurrency"), "retrieved_at": _now(), "source": "yfinance / Yahoo Finance", "values": values, "error": None}
            with self.lock:
                self.metrics_cache[ticker] = (time.time(), result)
            return deepcopy(result)
        except Exception:
            if previous:
                return {**deepcopy(previous[1]), "error": "Refresh unavailable; last successful metrics retained"}
            return {"ticker": ticker, "source": "yfinance / Yahoo Finance", "retrieved_at": None, "values": {}, "error": "Current metrics unavailable from Yahoo. Annual SEC figures remain available."}


service = LiveData()

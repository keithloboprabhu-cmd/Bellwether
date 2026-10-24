"""Latest closing prices: live from yfinance, falling back to the committed snapshot.

yfinance is unofficial and Yahoo often rate-limits cloud IPs, so the snapshot
(data/snapshots/prices.csv, refreshed daily by GitHub Actions) is the dependable
source; a live fetch only replaces it when it succeeds and is newer.
"""

from __future__ import annotations

import warnings

import pandas as pd

from policyshock.config import SNAPSHOT_DIR

SNAPSHOT_FILE = SNAPSHOT_DIR / "prices.csv"


def fetch_live(tickers: list[str]) -> pd.DataFrame:
    """Latest close per ticker from yfinance → DataFrame(ticker, close, date, source).

    Returns an empty frame on any failure; tickers with no data are omitted.
    """
    try:
        import yfinance as yf

        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            data = yf.download(tickers, period="7d", progress=False, auto_adjust=False, threads=True)
        closes = data["Close"]
        rows = []
        for t in tickers:
            if t not in closes:
                continue
            s = closes[t].dropna()
            if len(s):
                rows.append({"ticker": t, "close": round(float(s.iloc[-1]), 4), "date": s.index[-1].date().isoformat(), "source": "yfinance"})
        return pd.DataFrame(rows, columns=["ticker", "close", "date", "source"])
    except Exception:
        return pd.DataFrame(columns=["ticker", "close", "date", "source"])


def load_snapshot() -> pd.DataFrame:
    df = pd.read_csv(SNAPSHOT_FILE, dtype={"ticker": str})
    df["source"] = "snapshot"
    return df


def latest_prices(tickers: list[str], try_live: bool = True) -> pd.DataFrame:
    """Snapshot prices, overridden per ticker by any newer live yfinance close."""
    snap = load_snapshot()
    if not try_live:
        return snap[snap["ticker"].isin(tickers)].reset_index(drop=True)
    live = fetch_live(tickers)
    merged = pd.concat([snap, live]).sort_values("date").drop_duplicates("ticker", keep="last")
    return merged[merged["ticker"].isin(tickers)].reset_index(drop=True)

"""FRED macro series via the keyless fredgraph CSV endpoint (no API key needed).

Used for default current rates in financing policies, the macro context strip, and
real GDP (GDPC1) for the industry revenue-beta regressions. Falls back to the
committed snapshot data/snapshots/fred.csv when FRED is unreachable.
"""

from __future__ import annotations

import io

import pandas as pd

from policyshock.config import SNAPSHOT_DIR
from policyshock.data.http import get_with_retry

FREDGRAPH_URL = "https://fred.stlouisfed.org/graph/fredgraph.csv"
SERIES = {
    "DFF": "Effective federal funds rate (%)",
    "DGS10": "10-year Treasury yield (%)",
    "MORTGAGE30US": "30-year mortgage rate (%)",
    "CPIAUCSL": "CPI, all urban consumers (index)",
    "UNRATE": "Unemployment rate (%)",
    "GDPC1": "Real GDP (billions of chained 2017 $, SAAR)",
    "PCE": "Personal consumption expenditures (billions $, SAAR)",
}
SNAPSHOT_FILE = SNAPSHOT_DIR / "fred.csv"
# Names available to policy expressions as macro.<key> (see macro_context).
MACRO_KEYS = {"fed_funds", "treasury_10y", "mortgage_30y", "unemployment", "pce_musd"}


def fetch_series(series_id: str, start: str = "2005-01-01") -> pd.Series:
    """Download one FRED series as a float Series indexed by date (missing values dropped)."""
    resp = get_with_retry(FREDGRAPH_URL, params={"id": series_id, "cosd": start})
    df = pd.read_csv(io.StringIO(resp.text))
    df.columns = ["date", series_id]
    df["date"] = pd.to_datetime(df["date"])
    values = pd.to_numeric(df[series_id], errors="coerce")  # FRED marks gaps with "."
    return pd.Series(values.values, index=df["date"], name=series_id).dropna()


def fetch_all(start: str = "2005-01-01") -> pd.DataFrame:
    """Long-format frame (series_id, date, value) for every series in SERIES."""
    frames = []
    for sid in SERIES:
        s = fetch_series(sid, start)
        frames.append(pd.DataFrame({"series_id": sid, "date": s.index, "value": s.values}))
    return pd.concat(frames, ignore_index=True)


def load_snapshot() -> pd.DataFrame:
    df = pd.read_csv(SNAPSHOT_FILE, parse_dates=["date"])
    return df


def latest_values(df: pd.DataFrame | None = None) -> dict[str, dict]:
    """{series_id: {"value": float, "date": "YYYY-MM-DD", "label": str}} from the snapshot."""
    df = load_snapshot() if df is None else df
    out = {}
    for sid, g in df.groupby("series_id"):
        row = g.sort_values("date").iloc[-1]
        out[sid] = {"value": float(row["value"]), "date": row["date"].date().isoformat(), "label": SERIES.get(sid, sid)}
    return out


def macro_context(latest: dict[str, dict] | None = None) -> dict[str, float]:
    """Macro values exposed to policy expressions as `macro.<name>` (rates in %, $ in millions)."""
    v = latest_values() if latest is None else latest
    return {
        "fed_funds": v["DFF"]["value"],
        "treasury_10y": v["DGS10"]["value"],
        "mortgage_30y": v["MORTGAGE30US"]["value"],
        "unemployment": v["UNRATE"]["value"],
        "pce_musd": v["PCE"]["value"] * 1000,  # FRED reports $ billions SAAR
    }

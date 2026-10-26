"""Shared Streamlit helpers: page setup, cached data access, footer and macro strip."""

from __future__ import annotations

import time

import pandas as pd
import streamlit as st

from policyshock.config import load_universe
from policyshock.data import fred, prices, store

REFRESH_COOLDOWN_S = 600  # public app: at most one live refresh per 10 minutes, app-wide


def page_setup(title: str) -> None:
    """Configure the page title and supplied Bellwether brand icon."""
    from pathlib import Path

    logo = Path(__file__).resolve().parents[3] / "web/public/bellwether-logo.png"
    st.set_page_config(page_title=f"{title} · Bellwether", page_icon=str(logo), layout="wide", initial_sidebar_state="expanded")


@st.cache_data(ttl=86400, show_spinner="Fetching latest prices…")
def cached_prices() -> pd.DataFrame:
    """Snapshot prices, overlaid with live yfinance closes when that call succeeds."""
    return prices.latest_prices(load_universe().all_tickers, try_live=True)


@st.cache_data(ttl=86400)
def cached_fred_latest() -> dict:
    return fred.latest_values()


@st.cache_resource
def _refresh_state() -> dict:
    return {"last": 0.0}


def refresh_button() -> None:
    """Clear cached data so prices/macro values are refetched; rate-limited app-wide."""
    state = _refresh_state()
    wait = REFRESH_COOLDOWN_S - (time.time() - state["last"])
    if st.button("🔄 Refresh data", help="Clears the cache and refetches live prices. Filings refresh daily via GitHub Actions."):
        if wait > 0:
            st.info(f"Data was refreshed recently; try again in {int(wait // 60) + 1} min.")
        else:
            state["last"] = time.time()
            st.cache_data.clear()
            store.load_baselines.cache_clear()
            st.rerun()


def data_as_of() -> str:
    """One-line 'data as of' string used in footers."""
    meta = store.load_meta()
    px = cached_prices()
    px_date = px["date"].max() if len(px) else "n/a"
    live = (px["source"] == "yfinance").any() if "source" in px else False
    filings = meta.get("baselines", {}).get("as_of", "n/a")[:10]
    return f"Filings checked {filings} · prices as of {px_date} ({'live' if live else 'snapshot'})"


def footer() -> None:
    st.divider()
    st.caption(f"Educational project for Duke FMKT 256. Not investment advice. · {data_as_of()}")


def macro_strip() -> None:
    vals = cached_fred_latest()
    cols = st.columns(4)
    for col, sid in zip(cols, ["DFF", "DGS10", "MORTGAGE30US", "UNRATE"]):
        v = vals.get(sid)
        if v:
            col.metric(v["label"], f"{v['value']:.2f}%", help=f"FRED {sid}, as of {v['date']}")

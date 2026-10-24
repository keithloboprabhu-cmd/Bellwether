"""Data page: every company's baseline, its fiscal period, 10-K link, XBRL tags and flags."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

import pandas as pd  # noqa: E402
import streamlit as st  # noqa: E402

from policyshock.config import load_universe  # noqa: E402
from policyshock.data import store  # noqa: E402
from policyshock.ui.common import cached_prices, footer, page_setup, refresh_button  # noqa: E402

page_setup("Data")
st.title("Data")
st.markdown(
    "Baselines are parsed from each company's annual 10-K XBRL data via the free "
    "[SEC EDGAR API](https://www.sec.gov/edgar/sec-api-documentation). A GitHub Action re-pulls filings, "
    "prices (yfinance) and macro series (FRED) every day, so new 10-Ks flow in automatically. "
    "Dollar figures are **$ millions** for the latest fiscal year each company has filed."
)
refresh_button()

universe = load_universe()
px = cached_prices()
df = store.baseline_frame(universe.all_tickers, px)
names = {i.slug: i.name for i in universe.industries}
df["industry_name"] = df["industry"].map(names)
df["n_flags"] = df["flags"].map(len)

industry = st.selectbox("Industry", ["All"] + [i.name for i in universe.industries])
view = df if industry == "All" else df[df["industry_name"] == industry]

table = pd.DataFrame(
    {
        "Ticker": view["ticker"],
        "Company": view["name"],
        "Industry": view["industry_name"],
        "Fiscal year": view["fiscal_year"],
        "Period end": view["period_end"],
        "10-K filed": view["filed"],
        "Revenue": view["revenue"],
        "Op. income": view["operating_income"],
        "Net income": view["net_income"],
        "Diluted EPS": view["eps_diluted"],
        "Tax rate": view["effective_tax_rate"] * 100,
        "Price": view["price"],
        "Mkt cap ($B)": view["market_cap"] / 1000,
        "P/E": view["pe"],
        "Flags": view["n_flags"],
        "10-K": view["filing_url"],
    }
)
st.dataframe(
    table,
    hide_index=True,
    width="stretch",
    column_config={
        "Revenue": st.column_config.NumberColumn(format="%,.0f"),
        "Op. income": st.column_config.NumberColumn(format="%,.0f"),
        "Net income": st.column_config.NumberColumn(format="%,.0f"),
        "Diluted EPS": st.column_config.NumberColumn(format="%.2f"),
        "Tax rate": st.column_config.NumberColumn(format="%.1f%%"),
        "Price": st.column_config.NumberColumn(format="$%.2f"),
        "Mkt cap ($B)": st.column_config.NumberColumn(format="%,.0f"),
        "P/E": st.column_config.NumberColumn(format="%.1f"),
        "10-K": st.column_config.LinkColumn(display_text="EDGAR"),
    },
)

st.subheader("Company detail")
ticker = st.selectbox("Company", view["ticker"].tolist(), format_func=lambda t: f"{t} · {universe.company(t).name}")
row = df.set_index("ticker").loc[ticker]
c1, c2 = st.columns([1, 1])
with c1:
    st.markdown(f"**{row['name']}** · FY{row['fiscal_year']} (period ended {row['period_end']})")
    if row["filing_url"]:
        st.markdown(f"[10-K filing index on EDGAR]({row['filing_url']}) · filed {row['filed']}")
    st.markdown(f"Shares for market cap: {row['shares_source']}")
    if row["flags"]:
        st.warning("**Data flags**\n\n" + "\n".join(f"- {f}" for f in row["flags"]))
    else:
        st.success("No data-quality flags.")
with c2:
    st.markdown("**XBRL tags used**")
    st.dataframe(
        pd.DataFrame(sorted(row["tags"].items()), columns=["Line item", "Tag / derivation"]),
        hide_index=True,
        width="stretch",
    )

st.markdown("**History** ($ millions)")
hist = pd.DataFrame(
    [
        {
            "Fiscal year": y["fiscal_year"],
            "Period end": y["period_end"],
            "Revenue": y["items"].get("revenue"),
            "Cost of revenue": y["items"].get("cost_of_revenue"),
            "Op. income": y["items"].get("operating_income"),
            "Net income": y["items"].get("net_income"),
            "Tax rate %": (y["items"].get("effective_tax_rate_raw") or float("nan")) * 100,
            "Flags": "; ".join(y["flags"]),
        }
        for y in store.company_years(ticker)
    ]
)
st.dataframe(hist, hide_index=True, width="stretch")
st.caption("Per-share figures in history are as reported in the latest filing covering each year and are not adjusted for later stock splits.")
footer()

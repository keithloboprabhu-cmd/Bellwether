"""Read-side access to the committed snapshots: baselines + prices → model-ready rows.

The app never calls SEC/FRED/Yahoo on a cold start; it reads data/snapshots/ and
(optionally) overlays a fresher live price. Valuation fields derived here:
    market cap = price × shares outstanding (cover page; diluted weighted shares if absent)
    P/E        = price / diluted EPS, only when EPS > 0
"""

from __future__ import annotations

import json
from functools import lru_cache

import pandas as pd

from policyshock.config import SNAPSHOT_DIR

BASELINES_FILE = SNAPSHOT_DIR / "baselines.json"
META_FILE = SNAPSHOT_DIR / "meta.json"


@lru_cache(maxsize=1)
def load_baselines() -> dict:
    """The full baselines.json payload ({as_of, source, companies: {ticker: …}})."""
    return json.loads(BASELINES_FILE.read_text())


def load_meta() -> dict:
    return json.loads(META_FILE.read_text()) if META_FILE.exists() else {}


def company_years(ticker: str) -> list[dict]:
    """All parsed fiscal years for a ticker, newest first."""
    return load_baselines()["companies"][ticker]["years"]


def fiscal_year(ticker: str, year: int | None = None) -> dict:
    """One fiscal year record (latest when `year` is None). Raises KeyError if absent."""
    years = company_years(ticker)
    if year is None:
        return years[0]
    for y in years:
        if y["fiscal_year"] == year:
            return y
    raise KeyError(f"{ticker} FY{year} not in snapshot")


def baseline_row(ticker: str, price: float | None, price_date: str | None = None, year: int | None = None, *, company: dict | None = None) -> dict:
    """Model-ready annual row, optionally from an immutable live SEC company record.

    Historical callers keep reading committed snapshots; live overrides never
    mutate those records or alter backtest financial histories.
    """
    co = company if company is not None else load_baselines()["companies"][ticker]
    fy = (co["years"][0] if year is None else next(y for y in co["years"] if y["fiscal_year"] == year)) if company is not None else fiscal_year(ticker, year)
    it = fy["items"]
    flags = list(fy["flags"])

    so = co.get("shares_outstanding")
    diluted = it.get("diluted_shares")
    shares_out, shares_src = diluted, "diluted weighted-average shares"
    if year is None:
        if not so or not so["value"]:
            flags.append("shares outstanding not on cover page (multi-class); using diluted shares")
        elif diluted and not 0.8 <= so["value"] / diluted <= 1.25:
            # A >25% gap usually means a class is missing from the cover page (NKE), a tagging
            # error, or a post-year share issue; diluted shares keep market cap on the same
            # share basis as the EPS the model uses.
            flags.append(
                f"cover-page shares ({so['value']:,.0f}M, {so['date']}) differ from diluted shares "
                f"({diluted:,.0f}M) by >25%; using diluted shares"
            )
        else:
            shares_out, shares_src = so["value"], f"cover page {so['date']}"

    eps = it.get("eps_diluted")
    mcap = price * shares_out if (price is not None and shares_out) else None
    pe = price / eps if (price is not None and eps and eps > 0) else None
    R, C = it.get("revenue"), it.get("cost_of_revenue")
    return {
        "ticker": ticker,
        "name": co["name"],
        "industry": co["industry"],
        "kind": co["kind"],
        "fiscal_year": fy["fiscal_year"],
        "period_end": fy["period_end"],
        "filing_url": fy.get("filing_url"),
        "filed": fy.get("source_filed"),
        "revenue": R,
        "cost_of_revenue": C,
        "contribution_margin": (R - C) / R if (R and C is not None) else None,
        "operating_income": it.get("operating_income"),
        "interest_expense": it.get("interest_expense"),
        "pretax_income": it.get("pretax_income"),
        "income_tax": it.get("income_tax"),
        "effective_tax_rate": it.get("effective_tax_rate"),
        "net_income": it.get("net_income"),
        "nci_income": it.get("nci_income"),
        "diluted_shares": it.get("diluted_shares"),
        "eps_diluted": eps,
        "total_debt": it.get("total_debt"),
        "da": it.get("da"),
        "net_interest_income": it.get("net_interest_income"),
        "total_assets": it.get("total_assets"),
        "shares_outstanding": shares_out,
        "shares_source": shares_src,
        "price": price,
        "price_date": price_date,
        "market_cap": mcap,
        "pe": pe,
        "tags": fy["tags"],
        "flags": flags,
    }


def baseline_frame(tickers: list[str], prices_df: pd.DataFrame) -> pd.DataFrame:
    """Baselines for many tickers joined to a prices frame (ticker, close, date[, source])."""
    px = prices_df.set_index("ticker")
    rows = []
    for t in tickers:
        p = px["close"].get(t) if t in px.index else None
        d = px["date"].get(t) if t in px.index else None
        rows.append(baseline_row(t, None if p is None else float(p), d))
    return pd.DataFrame(rows)

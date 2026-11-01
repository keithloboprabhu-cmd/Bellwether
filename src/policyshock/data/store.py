"""Read-side access to the committed snapshots: baselines + prices → model-ready rows.

The app never calls SEC/FRED/Yahoo on a cold start; it reads data/snapshots/ and
(optionally) overlays a fresher live price. Valuation fields derived here:
    market cap = price × shares outstanding (cover page; diluted weighted shares if absent)
    P/E        = price / diluted EPS, only when EPS > 0
"""

from __future__ import annotations

import json
import statistics
from functools import lru_cache

import pandas as pd

from policyshock.config import SNAPSHOT_DIR

BASELINES_FILE = SNAPSHOT_DIR / "baselines.json"
META_FILE = SNAPSHOT_DIR / "meta.json"


@lru_cache(maxsize=1)
def load_baselines() -> dict:
    """The full baselines.json payload ({as_of, source, companies: {ticker: …}})."""
    return json.loads(BASELINES_FILE.read_text())


@lru_cache(maxsize=1)
def load_valuation_adjustments() -> dict:
    """Only independently sourced, period-matched adjusted EPS can normalize valuation."""
    path = SNAPSHOT_DIR / 'valuation_adjustments.json'
    return json.loads(path.read_text()).get('companies', {}) if path.exists() else {}


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
        if co.get('share_basis') == 'class_a_equivalent':
            shares_src = 'annual class-A-equivalent diluted shares'
            flags.append('Raw class cover counts are not economic A-equivalent shares; current equivalent outstanding shares unquantified, annual equivalent diluted count used')
        elif so and so.get("date", "") < fy["period_end"]:
            flags.append(f"stale cover-page shares ({so.get('date')}); using current diluted weighted shares")
        elif not so or not so["value"]:
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
    history = [y for y in co["years"] if y["period_end"] <= fy["period_end"]][:3]
    historical_eps = [y["items"].get("eps_diluted") for y in history]
    median_eps = statistics.median(historical_eps) if len(historical_eps) == 3 and all(isinstance(v, (int, float)) for v in historical_eps) else None
    valuation_eps, valuation_method = eps, "reported_eps"
    adjustments = load_valuation_adjustments().get(ticker, {})
    current_adjustment = adjustments.get(fy['period_end'])
    special_items = current_adjustment and current_adjustment.get('adjusted_eps') != current_adjustment.get('reported_eps')
    if eps is None or eps <= 0 or special_items or (median_eps is not None and median_eps > 0 and eps < .6 * median_eps):
        normalized = [adjustments.get(y['period_end']) for y in history]
        supported = len(normalized) == 3 and all(row and row.get('source_url') and row.get('adjusted_eps') is not None
            and isinstance(y['items'].get('eps_diluted'), (int,float))
            and round(y['items']['eps_diluted'],2) == row.get('reported_eps') for y,row in zip(history,normalized))
        adjusted_median = statistics.median(row['adjusted_eps'] for row in normalized) if supported else None
        valuation_eps = adjusted_median if adjusted_median is not None and adjusted_median > 0 else None
        valuation_method = "three_year_median_adjusted_eps" if valuation_eps else "unavailable_normalization_pending"
        flags.append("Valuation uses the median of three issuer-adjusted annual EPS figures; non-GAAP definitions and acquisition comparability remain disclosed limitations" if valuation_eps else "Negative/depressed EPS: no verified adjusted three-year earnings series or EV/EBITDA inputs; permanent valuation unavailable")
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
        "finance_arm_debt": it.get("finance_arm_debt"),
        "debt_basis": "industrial_only" if it.get("finance_arm_debt") is not None else "reported_borrowings",
        "operating_lease_liabilities": it.get("operating_lease_liabilities"),
        "finance_lease_liabilities": it.get("finance_lease_liabilities"),
        "da": it.get("da"),
        "net_interest_income": it.get("net_interest_income"),
        "total_assets": it.get("total_assets"),
        "shares_outstanding": shares_out,
        "shares_source": shares_src,
        "price": price,
        "price_date": price_date,
        "market_cap": mcap,
        "pe": pe,
        "valuation_eps": valuation_eps,
        "valuation_pe": price / valuation_eps if price is not None and valuation_eps and valuation_eps > 0 else None,
        "valuation_method": valuation_method,
        "valuation_history": [{"period_end": y["period_end"], "eps": y["items"].get("eps_diluted"), "filing_url": y.get("filing_url")} for y in history],
        "valuation_adjustments": [load_valuation_adjustments().get(ticker, {}).get(y['period_end']) for y in history] if valuation_method == 'three_year_median_adjusted_eps' else [],
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

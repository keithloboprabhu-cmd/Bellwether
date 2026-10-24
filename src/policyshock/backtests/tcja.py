"""Backtest 1: the 2017 Tax Cuts and Jobs Act (35% → 21% federal rate from 1 Jan 2018).

We run the engine's `tax_rate` channel on each company's last *pre-TCJA* fiscal year and
compare the predicted effective tax rate with what the company actually reported once
the new rate applied. We compare tax rates, not EPS, because EPS moved for many other
reasons (and per-share history isn't split-adjusted across years).

Period choices (all from the same EDGAR snapshot as the app):
- Pre-TCJA base year: the last fiscal year ending on or before 30 Nov 2017. The year that
  contains the enactment date (22 Dec 2017) is distorted by one-time deferred-tax
  remeasurement and the deemed-repatriation charge, so it is shown but not used.
- Post-TCJA actual: the average effective rate of the first two fiscal years that *start*
  on or after 1 Jan 2018 (averaging smooths one-offs such as Walmart's FY2019 foreign
  impairments).
- Domestic share of pretax income comes from the 10-K tax note (XBRL domestic/foreign
  pretax tags); where a company doesn't tag the split we assume 100% domestic (the sample is
  chosen to be domestic-heavy) and say so.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from policyshock.data.store import company_years
from policyshock.engine.channels import run_channel
from policyshock.engine.model import ChannelOutcome, aggregate

TICKERS = ["WMT", "TGT", "HD", "COST", "UNP", "UPS", "DAL", "LOPE", "NUE"]
D_STATUTORY = 0.21 - 0.35
ENACTED = date(2017, 12, 22)
BASE_YEAR_CUTOFF = date(2017, 11, 30)
POST_START = date(2018, 1, 1)


@dataclass
class TcjaRow:
    ticker: str
    base_period: str
    enactment_period: str | None
    post_periods: list[str]
    domestic_share: float
    domestic_share_source: str
    t_base: float
    t_enactment_year: float | None
    t_predicted: float
    t_actual: float
    notes: list[str]

    @property
    def predicted_change(self) -> float:
        return self.t_predicted - self.t_base

    @property
    def actual_change(self) -> float:
        return self.t_actual - self.t_base

    @property
    def error(self) -> float:
        """Predicted minus actual post-TCJA rate (positive = we predicted too high a rate)."""
        return self.t_predicted - self.t_actual


def _start(y: dict) -> date:
    """Approximate fiscal-year start: one year before the period end."""
    end = date.fromisoformat(y["period_end"])
    return date(end.year - 1, end.month, min(end.day, 28))


def run_ticker(ticker: str) -> TcjaRow:
    years = sorted(company_years(ticker), key=lambda y: y["period_end"])
    base = [y for y in years if date.fromisoformat(y["period_end"]) <= BASE_YEAR_CUTOFF][-1]
    enact = next((y for y in years if _start(y) < ENACTED <= date.fromisoformat(y["period_end"])), None)
    post = [y for y in years if _start(y) >= date(2017, 12, 25)][:2]
    notes: list[str] = []

    it = base["items"]
    d, f = it.get("pretax_domestic"), it.get("pretax_foreign")
    if d is not None and d > 0 and d + (f or 0) > 0:
        share = min(1.0, d / (d + (f or 0)))
        share_src = "10-K tax note (domestic ÷ total pretax income)"
    else:
        share, share_src = 1.0, "assumed 100% (no domestic/foreign split tagged; US-focused company)"
        notes.append("domestic share assumed 100%")

    # Run the same engine channel the app uses, on the pre-TCJA baseline.
    b = {
        "ticker": ticker,
        "name": ticker,
        "revenue": it["revenue"],
        "operating_income": it["operating_income"],
        "pretax_income": it["pretax_income"],
        "effective_tax_rate": it["effective_tax_rate_raw"],
        "diluted_shares": it["diluted_shares"],
        "eps_diluted": it["eps_diluted"],
        "price": None,
        "pe": None,
    }
    delta = run_channel("tax_rate", b, {"d_statutory_rate": D_STATUTORY, "domestic_income_share": share})
    res = aggregate(b, [ChannelOutcome("TCJA", "tax", "permanent", delta)])

    post_rates = [y["items"]["effective_tax_rate_raw"] for y in post if y["items"].get("effective_tax_rate_raw") is not None]
    if len(post_rates) < 2:
        notes.append("fewer than two post-TCJA years available")
    return TcjaRow(
        ticker=ticker,
        base_period=base["period_end"],
        enactment_period=enact["period_end"] if enact else None,
        post_periods=[y["period_end"] for y in post],
        domestic_share=share,
        domestic_share_source=share_src,
        t_base=it["effective_tax_rate_raw"],
        t_enactment_year=enact["items"].get("effective_tax_rate_raw") if enact else None,
        t_predicted=res.tax_rate_new,
        t_actual=sum(post_rates) / len(post_rates),
        notes=notes,
    )


def run(tickers: list[str] = TICKERS) -> list[TcjaRow]:
    return [run_ticker(t) for t in tickers]


def summary(rows: list[TcjaRow]) -> dict:
    """Mean absolute error and how much of the actual decline the model explains."""
    n = len(rows)
    mae = sum(abs(r.error) for r in rows) / n
    pred = sum(r.predicted_change for r in rows) / n
    act = sum(r.actual_change for r in rows) / n
    same_sign = sum(1 for r in rows if r.predicted_change * r.actual_change > 0)
    return {"n": n, "mae": mae, "mean_predicted_change": pred, "mean_actual_change": act, "direction_hits": same_sign}

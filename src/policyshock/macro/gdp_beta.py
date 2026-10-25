"""Industry revenue betas to real GDP growth (used by the Full Market recession shock).

For each industry we pool its configured companies and regress annual revenue growth on real
GDP growth over the same fiscal year:

    g_rev(i, t) = α + β · g_GDP(t) + ε

- Revenue: EDGAR annual revenue (FY2009 → latest), consecutive fiscal years only.
- Real GDP: FRED GDPC1 (quarterly). For a fiscal year ending in quarter q, g_GDP is the
  average of the four quarters ending in q over the average of the four before them, so
  fiscal years that don't end in December line up correctly.
- Revenue growth is winsorized at [−50%, +100%] to limit acquisitions and divestitures, and the
  number of clipped points is reported. Results are shown with and without fiscal years
  ending in 2020–2021, whose pandemic swings dominate a short sample.
These are small samples (uneven company histories), so the standard error and R² are shown so
users can judge how much to trust each β.
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass

import numpy as np
import pandas as pd

from policyshock.config import SNAPSHOT_DIR, load_universe
from policyshock.data import fred, store

OUT_FILE = SNAPSHOT_DIR / "gdp_betas.json"
CLIP = (-0.5, 1.0)


@dataclass
class Beta:
    industry: str
    beta: float
    se: float
    alpha: float
    r2: float
    n: int
    n_clipped: int
    beta_ex_covid: float
    se_ex_covid: float
    r2_ex_covid: float
    n_ex_covid: int
    small_sample: bool


def gdp_growth_by_quarter(gdp: pd.Series) -> pd.Series:
    """Trailing-four-quarter average growth, indexed by quarter period."""
    q = gdp.copy()
    q.index = pd.PeriodIndex(q.index, freq="Q")
    avg4 = q.rolling(4).mean()
    return (avg4 / avg4.shift(4) - 1).dropna()


def panel() -> pd.DataFrame:
    """One row per company-year: industry, period end, revenue growth, matched GDP growth."""
    fr = fred.load_snapshot()
    gdp = fr[fr["series_id"] == "GDPC1"].set_index("date")["value"]
    g_gdp = gdp_growth_by_quarter(gdp)
    rows = []
    for ind in load_universe().industries:
        for t in ind.tickers:
            ys = sorted(store.company_years(t), key=lambda y: y["period_end"])
            for prev, cur in zip(ys, ys[1:]):
                r0, r1 = prev["items"].get("revenue"), cur["items"].get("revenue")
                days = (pd.Timestamp(cur["period_end"]) - pd.Timestamp(prev["period_end"])).days
                if not (r0 and r1 and r0 > 0 and 350 <= days <= 380 and cur["fiscal_year"] >= 2009):
                    continue
                q = pd.Period(cur["period_end"], freq="Q")
                if q not in g_gdp.index:
                    continue
                rows.append(
                    {
                        "industry": ind.slug,
                        "ticker": t,
                        "period_end": cur["period_end"],
                        "g_rev_raw": r1 / r0 - 1,
                        "g_gdp": float(g_gdp[q]),
                    }
                )
    df = pd.DataFrame(rows)
    df["g_rev"] = df["g_rev_raw"].clip(*CLIP)
    df["clipped"] = df["g_rev"] != df["g_rev_raw"]
    df["covid"] = df["period_end"].str[:4].isin(["2020", "2021"])
    return df


def ols(x: np.ndarray, y: np.ndarray) -> tuple[float, float, float, float]:
    """OLS with intercept → (alpha, beta, se(beta), R²)."""
    X = np.column_stack([np.ones_like(x), x])
    coef, *_ = np.linalg.lstsq(X, y, rcond=None)
    resid = y - X @ coef
    sigma2 = resid @ resid / (len(y) - 2)
    se = float(np.sqrt(sigma2 * np.linalg.inv(X.T @ X)[1, 1]))
    r2 = 1 - (resid @ resid) / ((y - y.mean()) @ (y - y.mean()))
    return float(coef[0]), float(coef[1]), se, float(r2)


def estimate(df: pd.DataFrame | None = None) -> dict[str, Beta]:
    df = panel() if df is None else df
    out = {}
    for ind, g in df.groupby("industry"):
        a, b, se, r2 = ols(g["g_gdp"].to_numpy(), g["g_rev"].to_numpy())
        gx = g[~g["covid"]]
        _, bx, sex, r2x = ols(gx["g_gdp"].to_numpy(), gx["g_rev"].to_numpy())
        out[ind] = Beta(ind, b, se, a, r2, len(g), int(g["clipped"].sum()), bx, sex, r2x, len(gx), len(g) < 60)
    return out


def write_snapshot() -> dict:
    betas = estimate()
    OUT_FILE.write_text(json.dumps({k: asdict(v) for k, v in betas.items()}, indent=1))
    return {"industries": len(betas)}


def load() -> dict[str, dict]:
    return json.loads(OUT_FILE.read_text())

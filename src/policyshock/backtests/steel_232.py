"""Backtest 2: the March 2018 Section 232 tariffs (25% on imported steel).

Runs the Industrials `steel_tariffs` policy (the same config the simulator uses, with a
25-point tariff) on FY2017 baselines for Nucor (domestic producer) and the two heaviest
steel users, Caterpillar and Deere. Predicted Δ gross margin is compared with the reported
FY2017 → FY2018 change, with the low/high range from the policy's own assumptions.

What this can and can't show: 2018 was also a strong demand year for steel and machinery,
so actual margins moved for reasons the tariff channel doesn't model. The test is whether
the engine gets the **direction** right (Nucor up, steel users squeezed) and the right
**order of magnitude**, not a point forecast. Exposures are the current (FY2025) estimates,
applied to the FY2017 income statements.
"""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

from policyshock.data import store
from policyshock.engine.scenarios import prepare_baselines
from policyshock.engine.sensitivity import Runner, analyze
from policyshock.policies.loader import registry

TICKERS = ["NUE", "CAT", "DE"]
BASE_YEAR, POST_YEAR = 2017, 2018
TARIFF_PTS = 25


@dataclass
class SteelRow:
    ticker: str
    role: str
    base_period: str
    post_period: str
    gm_base: float
    gm_post_actual: float
    pred_bps: float
    pred_low_bps: float
    pred_high_bps: float
    note: str | None = None

    @property
    def actual_bps(self) -> float:
        return (self.gm_post_actual - self.gm_base) * 10_000

    @property
    def direction_ok(self) -> bool:
        return self.pred_bps * self.actual_bps > 0


def _gm(r: float, c: float) -> float:
    return (r - c) / r


def consistent_cost(base: dict, post: dict) -> tuple[float, float, str | None]:
    """Cost of revenue for two years on one definition.

    If the parser used different tags/derivations in the two years (Deere switched from
    CostOfGoodsSold to a CostsAndExpenses-based figure in FY2018), recompute both years as
    CostsAndExpenses − SG&A − R&D so the margin change is like-for-like.
    """
    tb, tp = base["tags"].get("cost_of_revenue"), post["tags"].get("cost_of_revenue")
    if tb == tp:
        return base["items"]["cost_of_revenue"], post["items"]["cost_of_revenue"], None

    def derived(y):
        it = y["items"]
        if it.get("costs_and_expenses") is None:
            return None
        return it["costs_and_expenses"] - (it.get("sga") or 0) - (it.get("rnd") or 0)

    cb, cp = derived(base), derived(post)
    if cb is None or cp is None:
        return base["items"]["cost_of_revenue"], post["items"]["cost_of_revenue"], "cost definition differs between years"
    return cb, cp, "both years recomputed as CostsAndExpenses − SG&A − R&D (tag changed between years)"


def _gm_change_bps(c) -> float:
    """Predicted change in gross margin from a CompanyResult."""
    b = c.baseline
    R, C = b["revenue"], b["cost_of_revenue"]
    return (_gm(R + c.dR, C + c.dC) - _gm(R, C)) * 10_000


def run() -> list[SteelRow]:
    reg = registry()
    pol = reg.policy("industrials", "steel_tariffs")
    rows_b, costs = [], {}
    for t in TICKERS:
        b = store.baseline_row(t, None, year=BASE_YEAR)
        cb, cp, note = consistent_cost(store.fiscal_year(t, BASE_YEAR), store.fiscal_year(t, POST_YEAR))
        b["cost_of_revenue"] = cb
        b["contribution_margin"] = (b["revenue"] - cb) / b["revenue"]
        costs[t] = (cp, note)
        rows_b.append(b)
    frame = pd.DataFrame(rows_b)
    runner = Runner(
        policy=pol,
        baselines=prepare_baselines(frame),
        inputs={"tariff_pct": TARIFF_PTS},
        assumption_ranges={a.key: (a.low, a.base, a.high) for a in pol.assumptions},
        exposure_cfg=reg.exposures,
    )
    an = analyze(runner)
    rows = []
    for c in an.base.companies:
        post = store.fiscal_year(c.ticker, POST_YEAR)
        e = an.envelopes[c.ticker]
        lo, hi = sorted([_gm_change_bps(e.low), _gm_change_bps(e.high)])
        rows.append(
            SteelRow(
                ticker=c.ticker,
                role=c.role,
                base_period=c.baseline["period_end"],
                post_period=post["period_end"],
                gm_base=_gm(c.baseline["revenue"], c.baseline["cost_of_revenue"]),
                gm_post_actual=_gm(post["items"]["revenue"], costs[c.ticker][0]),
                pred_bps=_gm_change_bps(c),
                pred_low_bps=lo,
                pred_high_bps=hi,
                note=costs[c.ticker][1],
            )
        )
    return rows


def render(st) -> None:
    """Streamlit section for the Backtests page."""
    import plotly.graph_objects as go

    rows = st.cache_data(run)()
    st.markdown(
        f"Tariffs of 25% on imported steel took effect in March 2018. We run the simulator's **Industrials steel-tariff policy** "
        f"(+{TARIFF_PTS} pts) on FY{BASE_YEAR} income statements and compare the predicted change in **gross margin** with what "
        f"each company reported for FY{POST_YEAR}. Whiskers show the policy's own low–high range."
    )
    hits = sum(r.direction_ok for r in rows)
    st.metric("Direction correct", f"{hits} of {len(rows)}")
    fig = go.Figure()
    t = [r.ticker for r in rows]
    fig.add_bar(
        x=t, y=[r.pred_bps for r in rows], name="Predicted", marker=dict(color="#2a78d6", cornerradius=4),
        error_y=dict(type="data", symmetric=False, array=[max(0, r.pred_high_bps - r.pred_bps) for r in rows],
                     arrayminus=[max(0, r.pred_bps - r.pred_low_bps) for r in rows], color="#52514e", thickness=1.5, width=5),
        hovertemplate="%{x}: predicted %{y:+.0f} bps<extra></extra>",
    )
    fig.add_bar(x=t, y=[r.actual_bps for r in rows], name="Actual", marker=dict(color="#eb6834", cornerradius=4),
                hovertemplate="%{x}: actual %{y:+.0f} bps<extra></extra>")
    fig.update_layout(
        barmode="group", height=340, margin=dict(l=8, r=8, t=8, b=8), plot_bgcolor="#fcfcfb", paper_bgcolor="rgba(0,0,0,0)",
        yaxis=dict(title="Change in gross margin (bps)", gridcolor="#e8e7e3"), legend=dict(orientation="h", y=1.1), bargap=0.3,
    )
    st.plotly_chart(fig, width="stretch")
    st.dataframe(
        pd.DataFrame(
            [
                {
                    "Ticker": r.ticker, "Role": r.role.replace("_", " "), f"FY{BASE_YEAR} period": r.base_period,
                    f"FY{BASE_YEAR} gross margin": r.gm_base, f"FY{POST_YEAR} gross margin": r.gm_post_actual,
                    "Actual change (bps)": r.actual_bps, "Predicted (bps)": r.pred_bps,
                    "Predicted low": r.pred_low_bps, "Predicted high": r.pred_high_bps, "Direction OK": "✓" if r.direction_ok else "✗",
                    "Note": r.note or "",
                }
                for r in rows
            ]
        ),
        hide_index=True, width="stretch",
        column_config={
            f"FY{BASE_YEAR} gross margin": st.column_config.NumberColumn(format="percent"),
            f"FY{POST_YEAR} gross margin": st.column_config.NumberColumn(format="percent"),
            **{c: st.column_config.NumberColumn(format="%+.0f") for c in ["Actual change (bps)", "Predicted (bps)", "Predicted low", "Predicted high"]},
        },
    )
    with st.expander("Confounders and how to read this", expanded=True):
        st.markdown(
            """
- **2018 was a boom year.** Steel demand and machinery orders were strong, so Nucor's margin gain and the equipment
  makers' price increases reflect demand as well as the tariff. The tariff channel captures only the policy effect.
- **Caterpillar is the miss.** Its revenue rose about 20% in 2018 (FY2017 $45.5B → FY2018 $54.7B in the EDGAR data),
  and the operating leverage from that volume outweighed higher steel costs. The model holds demand fixed apart from the
  tariff's own price effect, so it can't see this.
- **Deere's cost tag changed** between FY2017 and FY2018, so both years are recomputed on one definition
  (CostsAndExpenses − SG&A − R&D) to keep the comparison like-for-like.
- **Timing.** The tariff began in March 2018: Deere's FY2018 (ending Oct 2018) and Caterpillar's calendar 2018 include
  roughly 7–10 months of it, and contract pricing lags.
- **Exposures are today's estimates** (steel share of costs, Nucor's domestic share), applied to FY2017 statements.
- **What a pass looks like:** the right sign for the domestic producer and the users, and a predicted change of the
  same order of magnitude as the actual one, ideally with the actual inside the predicted range.
"""
        )

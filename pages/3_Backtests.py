"""Backtests: run the engine on pre-policy baselines and compare with what companies reported."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

import pandas as pd  # noqa: E402
import plotly.graph_objects as go  # noqa: E402
import streamlit as st  # noqa: E402

from policyshock.backtests import tcja  # noqa: E402
from policyshock.narrative import formatting as f  # noqa: E402
from policyshock.ui.common import footer, page_setup  # noqa: E402

page_setup("Backtests")
st.title("Backtests")
st.markdown(
    "Does the engine get real policy changes right? Each backtest runs the **same channels the simulator uses** "
    "on the fiscal year *before* the policy took effect, then compares the prediction with what the companies "
    "later reported in their 10-Ks."
)

PRED, ACT = "#2a78d6", "#eb6834"  # categorical slots 1 and 2

# ------------------------------------------------------------------ TCJA
st.header("1 · 2017 Tax Cuts and Jobs Act")
st.markdown(
    "The federal corporate rate fell from **35% to 21%** on 1 Jan 2018. The tax channel predicts each company's new "
    "effective rate as `t' = t − 14 pts × domestic share of pretax income`. We compare **effective tax rates**, not EPS, "
    "because EPS moved for many other reasons over the same years."
)


@st.cache_data
def tcja_rows():
    return tcja.run()


rows = tcja_rows()
s = tcja.summary(rows)
c1, c2, c3 = st.columns(3)
c1.metric("Mean predicted change", f.pct(s["mean_predicted_change"], signed=True))
c2.metric("Mean actual change", f.pct(s["mean_actual_change"], signed=True))
c3.metric("Mean absolute error", f"{s['mae'] * 100:.1f} pts", help="|predicted − actual| post-TCJA effective rate, averaged")
st.caption(f"Direction correct for {s['direction_hits']} of {s['n']} companies.")

fig = go.Figure()
tick = [r.ticker for r in rows]
fig.add_bar(x=tick, y=[r.predicted_change for r in rows], name="Predicted change", marker=dict(color=PRED, cornerradius=4),
            hovertemplate="%{x}: predicted %{y:+.1%}<extra></extra>")
fig.add_bar(x=tick, y=[r.actual_change for r in rows], name="Actual change", marker=dict(color=ACT, cornerradius=4),
            hovertemplate="%{x}: actual %{y:+.1%}<extra></extra>")
fig.update_layout(
    barmode="group", height=340, margin=dict(l=8, r=8, t=8, b=8), plot_bgcolor="#fcfcfb", paper_bgcolor="rgba(0,0,0,0)",
    yaxis=dict(title="Change in effective tax rate", tickformat="+.0%", gridcolor="#e8e7e3"), legend=dict(orientation="h", y=1.1),
    bargap=0.3, bargroupgap=0.08,
)
st.plotly_chart(fig, width="stretch")

table = pd.DataFrame(
    [
        {
            "Ticker": r.ticker,
            "Pre-TCJA year": r.base_period,
            "Rate before": r.t_base,
            "Enactment year (distorted)": r.t_enactment_year,
            "Domestic share": r.domestic_share,
            "Predicted rate": r.t_predicted,
            "Actual rate (avg of first 2 full years)": r.t_actual,
            "Error (pts)": r.error * 100,
            "Post-TCJA years": ", ".join(r.post_periods),
            "Domestic share source": r.domestic_share_source,
        }
        for r in rows
    ]
)
pct_cols = ["Rate before", "Enactment year (distorted)", "Domestic share", "Predicted rate", "Actual rate (avg of first 2 full years)"]
st.dataframe(
    table,
    hide_index=True,
    width="stretch",
    column_config={**{c: st.column_config.NumberColumn(format="percent") for c in pct_cols}, "Error (pts)": st.column_config.NumberColumn(format="%+.1f")},
)
with st.expander("Confounders and how to read this", expanded=True):
    st.markdown(
        """
- **The enactment year is distorted.** Fiscal years containing 22 Dec 2017 include one-time remeasurement of deferred
  taxes and the deemed-repatriation charge (UNP's rate that year was negative), so the base year is the last fiscal year
  ending before December 2017.
- **TCJA changed more than the rate.** It repealed the Section 199 domestic-production deduction, which had lowered
  manufacturers' rates, so NUE's actual rate fell less than predicted. It also added GILTI/FDII for multinationals.
- **State taxes.** The model applies the full 14-point federal cut to a state-inclusive effective rate. Because state
  taxes are federally deductible, the true change is slightly smaller (about 14 × (1 − state rate)), so the model
  predicts slightly too big a fall on average.
- **One-offs after 2018.** WMT's FY2019 rate (37.4%) was lifted by non-recurring foreign items, so its two-year average
  is high; its FY2020 rate was 24.4%. We show this rather than drop it.
- **Domestic shares** come from the 10-K tax note where the domestic/foreign pretax split is tagged; otherwise we assume
  100% for these US-focused companies (marked in the table).
"""
    )

# ------------------------------------------------------------------ Section 232
st.header("2 · 2018 Section 232 steel tariffs")
try:
    from policyshock.backtests import steel_232

    steel_232.render(st)
except ImportError:
    st.info("The steel-tariff backtest runs the Industrials steel policy on FY2017 baselines; it's being finalised.")

footer()

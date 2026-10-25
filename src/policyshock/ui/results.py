"""Render an Analysis: KPI cards, company table/chart, tornado, assumptions, downloads.

Colour roles (validated reference palette): polarity uses the blue↔red diverging pair
(helped = blue, hurt = red); the tornado's two ends use categorical slots 1 and 2.
Every chart has a table view and per-mark hover text, so meaning never rests on colour.
"""

from __future__ import annotations

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from policyshock.engine.sensitivity import Analysis
from policyshock.engine.valuation import persistence_label
from policyshock.narrative import formatting as f
from policyshock.policies.loader import Registry

POS, NEG = "#2a78d6", "#e34948"  # diverging poles: helped / hurt
LOW_C, HIGH_C = "#eb6834", "#2a78d6"  # tornado: driver at low / at high
INK_2 = "#52514e"
GRID = "#e8e7e3"


def _layout(fig: go.Figure, height: int, x_title: str) -> go.Figure:
    fig.update_layout(
        height=height,
        margin=dict(l=8, r=16, t=8, b=40),
        plot_bgcolor="#fcfcfb",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color=INK_2, size=13),
        xaxis=dict(title=x_title, tickformat="+.1%", gridcolor=GRID, zerolinecolor="#9a9994", zerolinewidth=1),
        yaxis=dict(gridcolor="rgba(0,0,0,0)", automargin=True),
        hoverlabel=dict(bgcolor="white", font_size=13),
        bargap=0.35,
    )
    return fig


# ------------------------------------------------------------------ helpers


def value_metric(an: Analysis) -> tuple[str, str]:
    """Which per-company % metric to chart: implied Δprice when available, else ΔEPS."""
    if any(c.dP_pct is not None for c in an.base.companies):
        return "dP_pct", "Implied Δ share price"
    return "dEPS_pct", "Δ EPS"


def company_frame(an: Analysis) -> pd.DataFrame:
    rows = []
    for c in an.base.companies:
        e = an.envelopes[c.ticker]
        dom = c.dominant
        rows.append(
            {
                "Ticker": c.ticker,
                "Company": c.name,
                "Role": c.role.replace("_", " "),
                "Fiscal year": c.baseline["fiscal_year"],
                "Revenue ($M)": c.baseline["revenue"],
                "Δ Revenue ($M)": c.dR,
                "Δ EBIT ($M)": c.dEBIT,
                "Δ Net income ($M)": c.dNI,
                "Δ EPS ($)": c.dEPS,
                "Δ EPS %": c.dEPS_pct,
                "Δ EPS % low": e.low.dEPS_pct,
                "Δ EPS % high": e.high.dEPS_pct,
                "Implied Δ price %": c.dP_pct,
                "Δ price % low": e.low.dP_pct,
                "Δ price % high": e.high.dP_pct,
                "Implied Δ market cap ($M)": c.d_mcap,
                "Δ op. margin (bps)": c.d_margin_bps,
                "Main driver": dom.label if dom else "",
                "Notes": "; ".join(c.notes),
            }
        )
    return pd.DataFrame(rows)


def reason(an: Analysis, c, reg: Registry) -> str:
    """One-line, deterministic reason for a long/short pick."""
    dom = c.dominant
    if dom is None:
        return "No direct exposure."
    def lower_first(txt: str) -> str:  # "Tariff on…" → "tariff on…", but "US consumer…" stays
        return txt if txt[1:2].isupper() else txt[:1].lower() + txt[1:]

    bits = [lower_first(dom.label)]
    for key in dom.exposure_refs:
        d = reg.exposure_defs[key]
        v = reg.exposures[c.ticker][key].value
        shown = f.pct(v, digits=0) if d.unit == "fraction" else f.money(v) if d.unit == "usd_m" else f.number(v)
        bits.append(f"{lower_first(d.label)} {shown}")
    # lead with the metric the ranking used: implied Δprice when available, else ΔEPS
    if c.dP_pct is not None:
        head = f"implied Δ price {f.pct(c.dP_pct, signed=True)} (Δ EPS {f.pct(c.dEPS_pct, signed=True)})"
    else:
        head = f"Δ EPS {f.pct(c.dEPS_pct, signed=True)}"
    return f"{head[:1].upper()}{head[1:]}, driven by {bits[0]}" + (f" ({'; '.join(bits[1:])})" if len(bits) > 1 else "") + "."


# ------------------------------------------------------------------ tabs


def overview(an: Analysis, reg: Registry) -> None:
    t, lo, hi = an.base.totals(), an.industry_low.totals(), an.industry_high.totals()
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Δ Industry revenue", f.money(t["d_revenue"], signed=True), f.pct(t["d_revenue_pct"], signed=True), delta_color="off")
    k2.metric("Δ Operating margin", f.bps(t["d_margin_bps"]))
    k3.metric(
        "Δ EPS (industry)",
        f.pct(t["d_eps_pct"], signed=True),
        f"range {f.pct(lo['d_eps_pct'], signed=True)} to {f.pct(hi['d_eps_pct'], signed=True)}",
        delta_color="off",
        help="Σ Δ net income ÷ Σ baseline net income across the configured sample. Range = pessimistic / optimistic assumptions.",
    )
    k4.metric(
        "Implied Δ market cap",
        f.money(t["d_mcap"], signed=True),
        f.pct(t["d_mcap_pct"], signed=True),
        delta_color="off",
        help="Constant-multiple valuation: " + persistence_label(an.base.policy.persistence),
    )

    if an.long or an.short:
        c1, c2 = st.columns(2)
        if an.long:
            with c1:
                st.markdown(f"#### ▲ Long **{an.long.ticker}**")
                st.markdown(f"{an.long.name}: {reason(an, an.long, reg)}")
        if an.short:
            with c2:
                st.markdown(f"#### ▼ Short **{an.short.ticker}**")
                st.markdown(f"{an.short.name}: {reason(an, an.short, reg)}")
        if an.low_conviction:
            st.caption("⚠ Low conviction: the long's pessimistic case overlaps the short's optimistic case.")
    for n in an.notes:
        st.caption(n)


def companies(an: Analysis) -> None:
    key, label = value_metric(an)
    lo_key, hi_key = ("Δ price % low", "Δ price % high") if key == "dP_pct" else ("Δ EPS % low", "Δ EPS % high")
    df = company_frame(an)
    col = "Implied Δ price %" if key == "dP_pct" else "Δ EPS %"
    plot = df[df[col].notna()].sort_values(col)
    if len(plot):
        base = plot[col]
        fig = go.Figure(
            go.Bar(
                x=base,
                y=plot["Ticker"],
                orientation="h",
                marker=dict(color=[POS if v >= 0 else NEG for v in base], cornerradius=4),
                error_x=dict(
                    type="data",
                    symmetric=False,
                    array=(plot[hi_key] - base).clip(lower=0),
                    arrayminus=(base - plot[lo_key]).clip(lower=0),
                    color=INK_2,
                    thickness=1.5,
                    width=5,
                ),
                customdata=plot[[lo_key, hi_key, "Company", "Main driver"]].values,
                hovertemplate="<b>%{y}</b> %{customdata[2]}<br>Base %{x:+.2%}<br>Range %{customdata[0]:+.2%} to %{customdata[1]:+.2%}<br>Driver: %{customdata[3]}<extra></extra>",
            )
        )
        st.plotly_chart(_layout(fig, 70 + 44 * len(plot), f"{label} (base, whiskers = low–high)"), width="stretch")
        if len(plot) < len(df):
            st.caption("Companies with negative baseline EPS have no meaningful P/E-based value and are omitted from the chart.")
    st.dataframe(
        df.drop(columns=["Δ EPS % low", "Δ EPS % high"]),
        hide_index=True,
        width="stretch",
        column_config={
            **{c: st.column_config.NumberColumn(format="%,.0f") for c in ["Revenue ($M)", "Δ Revenue ($M)", "Δ EBIT ($M)", "Δ Net income ($M)", "Implied Δ market cap ($M)", "Δ op. margin (bps)"]},
            "Δ EPS ($)": st.column_config.NumberColumn(format="%.3f"),
            **{c: st.column_config.NumberColumn(format="percent") for c in ["Δ EPS %", "Implied Δ price %", "Δ price % low", "Δ price % high"]},
        },
    )


def tornado(an: Analysis) -> None:
    if not an.tornado:
        st.info("This scenario has no uncertain assumptions.")
        return
    base = an.base.totals()[an.metric] or 0.0
    metric_name = "industry Δ EPS" if an.metric == "d_eps_pct" else "industry Δ market value"
    bars = list(reversed(an.tornado))  # biggest at top
    labels = [b.driver.label + ("" if b.driver.low is None else f"  ({f.number(b.driver.low)} – {f.number(b.driver.high)})") for b in bars]
    fig = go.Figure()
    fig.add_bar(y=labels, x=[b.low_value - base for b in bars], base=base, orientation="h", name="Driver at low", marker=dict(color=LOW_C, cornerradius=4),
                customdata=[b.low_value for b in bars], hovertemplate="%{y}<br>at low: %{customdata:+.2%}<extra></extra>")
    fig.add_bar(y=labels, x=[b.high_value - base for b in bars], base=base, orientation="h", name="Driver at high", marker=dict(color=HIGH_C, cornerradius=4),
                customdata=[b.high_value for b in bars], hovertemplate="%{y}<br>at high: %{customdata:+.2%}<extra></extra>")
    fig.add_vline(x=base, line_color=INK_2, line_width=1, annotation_text=f"base {f.pct(base, signed=True)}", annotation_position="top")
    fig.update_layout(barmode="overlay", legend=dict(orientation="h", y=-0.25))
    st.plotly_chart(_layout(fig, 120 + 50 * len(bars), f"{metric_name.capitalize()} with one driver moved, others at base"), width="stretch")
    st.caption("Exposure drivers move every company's exposure to its own low/high value together.")
    st.dataframe(
        pd.DataFrame([{"Driver": b.driver.label, "At low": b.low_value, "At high": b.high_value, "Swing": b.swing} for b in an.tornado]),
        hide_index=True,
        width="stretch",
        column_config={c: st.column_config.NumberColumn(format="percent") for c in ["At low", "At high", "Swing"]},
    )


def assumptions_frame(an: Analysis, reg: Registry, ranges: dict) -> pd.DataFrame:
    pol = an.base.policy
    rows = []
    for u in pol.user_inputs:
        rows.append({"Type": "Policy input", "Item": u.label, "Company": "", "Low": None, "Base": an.base.inputs.get(u.key), "High": None, "Unit": u.unit, "Source": "user input", "Link": None})
    for a in pol.assumptions:
        lo, base, hi = ranges[a.key]
        edited = (lo, base, hi) != (a.low, a.base, a.high)
        src = a.rationale if a.is_estimate else a.source
        rows.append({"Type": "Assumption", "Item": a.label, "Company": "", "Low": lo, "Base": base, "High": hi, "Unit": a.unit,
                     "Source": ("user-edited · " if edited else "") + ("Estimate: " if a.is_estimate else "") + (src or ""), "Link": a.source_url})
    for key in pol.exposure_keys:
        d = reg.exposure_defs[key]
        for c in an.base.companies:
            ev = reg.exposures[c.ticker][key]
            rows.append({"Type": "Exposure", "Item": d.label, "Company": c.ticker, "Low": ev.low, "Base": ev.value, "High": ev.high, "Unit": d.unit,
                         "Source": ("Estimate: " + (ev.rationale or "")) if ev.is_estimate else ev.source, "Link": ev.source_url})
    return pd.DataFrame(rows)


def assumptions(an: Analysis, reg: Registry, ranges: dict) -> pd.DataFrame:
    df = assumptions_frame(an, reg, ranges)
    st.dataframe(df, hide_index=True, width="stretch", column_config={"Link": st.column_config.LinkColumn(display_text="source"), "Source": st.column_config.TextColumn(width="large")})
    st.markdown("**Baseline data**: each company's latest 10-K via SEC EDGAR (see the Data page for tags and flags).")
    refs = an.base.policy.references
    if refs:
        st.markdown("**References**: " + " · ".join(f"[{i + 1}]({u})" for i, u in enumerate(refs)))
    return df

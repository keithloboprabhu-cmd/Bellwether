"""Full Market: run one macro shock across every configured industry and company.

The applied scenario lives in the URL (`?s=<token>`, mode "market"; see ui/state.py), so a
result can be shared and reloads to the same numbers. Aggregation is defined in
macro/aggregate.py and METHODOLOGY §4.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

import pandas as pd  # noqa: E402
import plotly.graph_objects as go  # noqa: E402
import streamlit as st  # noqa: E402

from policyshock.config import load_universe  # noqa: E402
from policyshock.data import fred  # noqa: E402
from policyshock.engine.valuation import persistence_label  # noqa: E402
from policyshock.macro.aggregate import build_market_runner, analyze_market, industry_metric  # noqa: E402
from policyshock.narrative import formatting as f  # noqa: E402
from policyshock.narrative.templates import explain_market  # noqa: E402
from policyshock.policies.loader import ConfigError, registry  # noqa: E402
from policyshock.ui.common import cached_prices, footer, page_setup  # noqa: E402
from policyshock.ui.results import HIGH_C, INK_2, LOW_C, NEG, POS, _layout  # noqa: E402
from policyshock.ui.state import decode, encode  # noqa: E402

page_setup("Full Market")

try:
    reg = registry()
except ConfigError as exc:
    st.error(f"```\n{exc}\n```")
    st.stop()

universe = load_universe()
names = {i.slug: i.name for i in universe.industries}
shocks = reg.macro_shocks()
ids = [s.id for s in shocks]

# ---------------------------------------------------------------- initial state from URL
if "m_applied" not in st.session_state:
    a = decode(st.query_params.get("s", ""))
    st.session_state.m_applied = a if a.get("m") == "market" and a.get("x") in ids else None
    if st.session_state.m_applied:
        st.session_state["w_shock"] = a["x"]
        for k, v in a.get("in", {}).items():
            st.session_state[f"w_min_{a['x']}_{k}"] = v
        for k, vals in a.get("a", {}).items():
            for case, v in zip(("low", "base", "high"), vals):
                st.session_state[f"w_mas_{a['x']}_{k}_{case}"] = v

# ---------------------------------------------------------------- sidebar
with st.sidebar:
    st.header("Macro shock")
    if st.session_state.get("w_shock") not in ids:
        st.session_state["w_shock"] = next((s.id for s in shocks if s.showcase), ids[0])
    shock_id = st.selectbox("Shock", ids, format_func=lambda i: ("★ " if reg.macro[i].showcase else "") + reg.macro[i].name, key="w_shock")
    shock = reg.macro[shock_id]
    st.caption(shock.description)
    st.caption(f"Persistence: {persistence_label(shock.persistence)}")

    st.subheader("Shock inputs")
    inputs = {}
    for u in shock.user_inputs:
        k = f"w_min_{shock.id}_{u.key}"
        if k not in st.session_state:
            st.session_state[k] = u.default
        inputs[u.key] = st.number_input(f"{u.label} ({u.unit})", min_value=u.min, max_value=u.max, step=u.step, key=k, help=u.help)

    ranges, bad = {}, []
    with st.expander("Advanced assumptions"):
        for a in shock.all_assumptions():
            st.markdown(f"**{a.label}** ({a.unit})")
            st.caption(("Estimate: " + a.rationale) if a.is_estimate else a.source)
            cols = st.columns(3)
            vals = []
            for col, case in zip(cols, ("low", "base", "high")):
                k = f"w_mas_{shock.id}_{a.key}_{case}"
                if k not in st.session_state:
                    st.session_state[k] = float(getattr(a, case))
                vals.append(col.number_input(case, key=k, format="%.4g"))
            if not vals[0] <= vals[1] <= vals[2]:
                bad.append(a.label)
            ranges[a.key] = tuple(vals)
    comps = set()
    for comp in shock.components:
        label = shock.component_labels.get(comp, comp.replace("_", " "))
        if st.checkbox(f"Include: {label}", value=True, key=f"w_mc_{shock.id}_{comp}", help="A second-round effect, shown separately from the direct impact."):
            comps.add(comp)
    if bad:
        st.error("Low ≤ base ≤ high is required for: " + ", ".join(bad))
    run = st.button("Run", type="primary", width="stretch", disabled=bool(bad))

defaults = {a.key: (a.low, a.base, a.high) for a in shock.all_assumptions()}
edited = {k: list(v) for k, v in ranges.items() if v != defaults[k]}
current = {"m": "market", "x": shock.id, "in": {k: float(v) for k, v in inputs.items()}, "a": edited}
if shock.components:
    current["c"] = sorted(comps)
if run:
    st.session_state.m_applied = current
    st.query_params["s"] = encode(current)

# ---------------------------------------------------------------- results
st.title("Full Market")
applied = st.session_state.m_applied
if not applied:
    st.info(
        f"Pick a macro shock in the sidebar and press **Run**. It is applied to all {len(universe.industries)} industries "
        f"and {len(universe.all_tickers)} companies at once, using the same channels as the industry simulator."
    )
    footer()
    st.stop()


@st.cache_data(max_entries=32, show_spinner="Running the shock across every industry…")
def run_market(token: str, prices_df):
    s = decode(token)
    sh = reg.macro[s["x"]]
    rng = {a.key: (a.low, a.base, a.high) for a in sh.all_assumptions()} | {k: tuple(v) for k, v in s.get("a", {}).items()}
    comps = set(s["c"]) if "c" in s else None
    mr = build_market_runner(s["x"], inputs=s.get("in"), assumption_ranges=rng, components=comps, prices_df=prices_df, macro=fred.macro_context())
    return analyze_market(mr), rng


token = encode(applied)
try:
    an, rng = run_market(token, cached_prices())
except Exception as exc:  # a bad deep link shouldn't crash the page
    st.error(f"Couldn't run this scenario: {exc}")
    st.stop()

shock = an.base.shock
t = an.base.totals()
lo_t, hi_t = an.market_low.totals(), an.market_high.totals()
st.subheader(shock.name)
st.markdown(" · ".join(f"{u.label}: **{an.base.inputs[u.key]:g} {u.unit}**" for u in shock.user_inputs))
# compare on a normalised basis: a deep link may omit inputs at their defaults and components (all on)
applied_full = {**applied, "in": {k: float(v) for k, v in {**shock.default_inputs(), **applied.get("in", {})}.items()}, "a": applied.get("a", {})}
if shock.components:
    applied_full["c"] = sorted(applied.get("c", shock.components))
if decode(encode(current)) != decode(encode(applied_full)):
    st.caption("Sidebar has changes that aren't applied yet; press **Run** to update.")

k1, k2, k3 = st.columns(3)
k1.metric(
    "Δ EPS, cap-weighted",
    f.pct(t["cw_d_eps_pct"], signed=True),
    f"range {f.pct(lo_t['cw_d_eps_pct'], signed=True)} to {f.pct(hi_t['cw_d_eps_pct'], signed=True)}",
    delta_color="off",
    help="Σ market cap × company Δ EPS % ÷ Σ market cap, over companies with a meaningful Δ EPS %. Range = assumptions oriented pessimistic / optimistic for the market as a whole.",
)
k2.metric("Implied Δ market value", f.money(t["d_mcap"], signed=True), f.pct(t["d_mcap_pct"], signed=True), delta_color="off",
          help="Σ implied Δ market cap ÷ Σ market cap. Constant-multiple valuation: " + persistence_label(shock.persistence))
k3.metric("Δ Net income", f.money(t["d_ni"], signed=True), f.pct(t["d_ni_pct"], signed=True), delta_color="off")
st.caption(
    f"**{t['n']}-company sample across {len(an.base.industries)} industries, cap-weighted** (${t['market_cap'] / 1e6:,.1f}T of market value). "
    "This is a curated teaching sample, not the whole market or an index forecast."
)

if an.long_industry and an.short_industry:
    c1, c2 = st.columns(2)
    for col, slug, arrow, side in ((c1, an.long_industry, "▲", "Long"), (c2, an.short_industry, "▼", "Short")):
        with col:
            r = an.base.industries[slug]
            eff = shock.industry_effects[slug]
            st.markdown(f"#### {arrow} {side} **{names[slug]}**")
            st.markdown(f"{f.pct(industry_metric(r), signed=True)} implied value. {eff.reason or ''}")
for n in an.notes:
    st.caption(n)

link = f"{(st.context.url or '').split('?')[0]}?s={token}"
with st.popover("🔗 Copy scenario link"):
    st.code(link, language=None)
    st.caption("Opening this link reproduces exactly this scenario.")

tab_ind, tab_co, tab_sens, tab_expl, tab_src = st.tabs(["Industries", "Companies", "Sensitivity", "Explanation", "Assumptions & sources"])

# ---------------------------------------------------------------- industries
with tab_ind:
    rows = []
    for slug, r in an.base.industries.items():
        tt = r.totals()
        eff = shock.industry_effects[slug]
        rows.append({
            "Industry": names[slug], "Companies": len(r.companies),
            "Δ Revenue %": tt["d_revenue_pct"], "Δ Op. margin (bps)": tt["d_margin_bps"], "Δ EPS %": tt["d_eps_pct"],
            "Δ EPS % low": an.industry_low[slug].totals()["d_eps_pct"], "Δ EPS % high": an.industry_high[slug].totals()["d_eps_pct"],
            "Implied Δ value %": tt["d_mcap_pct"], "Implied Δ value ($M)": tt["d_mcap"],
            "How the shock reaches it": eff.reason if eff.effect != "none" else "No direct effect: " + (eff.rationale or ""),
        })
    idf = pd.DataFrame(rows)
    plot = idf.assign(v=idf["Implied Δ value %"].fillna(idf["Δ EPS %"])).sort_values("v")
    fig = go.Figure(go.Bar(
        x=plot["v"], y=plot["Industry"], orientation="h",
        marker=dict(color=[POS if v >= 0 else NEG for v in plot["v"].fillna(0)], cornerradius=4),
        customdata=plot[["Δ EPS %", "Δ Revenue %"]].values,
        hovertemplate="<b>%{y}</b><br>Implied Δ value %{x:+.2%}<br>Δ EPS %{customdata[0]:+.2%}<br>Δ revenue %{customdata[1]:+.2%}<extra></extra>",
    ))
    st.plotly_chart(_layout(fig, 90 + 40 * len(plot), "Implied Δ market value by industry"), width="stretch")
    st.dataframe(
        idf, hide_index=True, width="stretch",
        column_config={
            **{c: st.column_config.NumberColumn(format="percent") for c in ["Δ Revenue %", "Δ EPS %", "Δ EPS % low", "Δ EPS % high", "Implied Δ value %"]},
            "Δ Op. margin (bps)": st.column_config.NumberColumn(format="%+.0f"),
            "Implied Δ value ($M)": st.column_config.NumberColumn(format="%,.0f"),
            "How the shock reaches it": st.column_config.TextColumn(width="large"),
        },
    )
    st.download_button("Download industry results (CSV)", idf.to_csv(index=False), f"{shock.id}_industries.csv", "text/csv")

# ---------------------------------------------------------------- companies
company_rows = []
for slug, r in an.base.industries.items():
    for c in r.companies:
        e = an.envelopes[c.ticker]
        dom = c.dominant
        company_rows.append({
            "Ticker": c.ticker, "Company": c.name, "Industry": names[slug],
            "Δ EPS %": c.dEPS_pct, "Δ EPS % low": e.low.dEPS_pct, "Δ EPS % high": e.high.dEPS_pct,
            "Implied Δ price %": c.dP_pct, "Δ Net income ($M)": c.dNI, "Implied Δ market cap ($M)": c.d_mcap,
            "Main driver": dom.label if dom else "",
            "Notes": "; ".join(c.notes),
        })
cdf = pd.DataFrame(company_rows)
with tab_co:
    ranked = an.ranked_companies()
    affected = [c for c in ranked if abs(c.dNI) > 1e-6]
    n_show = st.slider("Companies shown at each end", 3, 15, 8)
    top, bottom = affected[:n_show], affected[-n_show:][::-1]
    c1, c2 = st.columns(2)
    for col, title, cs in ((c1, "Most helped", top), (c2, "Most hurt", bottom)):
        with col:
            st.markdown(f"**{title}**")
            st.dataframe(
                pd.DataFrame([{"Ticker": c.ticker, "Industry": names[c.baseline["industry"]], "Δ EPS %": c.dEPS_pct, "Implied Δ price %": c.dP_pct} for c in cs]),
                hide_index=True, width="stretch",
                column_config={k: st.column_config.NumberColumn(format="percent") for k in ["Δ EPS %", "Implied Δ price %"]},
            )
    st.caption(f"{len(affected)} of {len(an.base.companies)} companies are directly affected. Ranked by implied Δ price (Δ EPS where price is not meaningful).")
    st.markdown("**All companies**")
    st.dataframe(
        cdf, hide_index=True, width="stretch",
        column_config={
            **{k: st.column_config.NumberColumn(format="percent") for k in ["Δ EPS %", "Δ EPS % low", "Δ EPS % high", "Implied Δ price %"]},
            **{k: st.column_config.NumberColumn(format="%,.0f") for k in ["Δ Net income ($M)", "Implied Δ market cap ($M)"]},
        },
    )
    st.download_button("Download company results (CSV)", cdf.to_csv(index=False), f"{shock.id}_companies.csv", "text/csv")

# ---------------------------------------------------------------- sensitivity
with tab_sens:
    if not an.tornado:
        st.info("This shock has no uncertain assumptions.")
    else:
        base = t[an.metric] or 0.0
        metric_name = "Cap-weighted Δ EPS" if an.metric == "cw_d_eps_pct" else "Implied Δ market value"
        bars = list(reversed(an.tornado[:12]))
        labels = [b.driver.label for b in bars]
        fig = go.Figure()
        fig.add_bar(y=labels, x=[b.low_value - base for b in bars], base=base, orientation="h", name="Driver at low", marker=dict(color=LOW_C, cornerradius=4),
                    customdata=[b.low_value for b in bars], hovertemplate="%{y}<br>at low: %{customdata:+.2%}<extra></extra>")
        fig.add_bar(y=labels, x=[b.high_value - base for b in bars], base=base, orientation="h", name="Driver at high", marker=dict(color=HIGH_C, cornerradius=4),
                    customdata=[b.high_value for b in bars], hovertemplate="%{y}<br>at high: %{customdata:+.2%}<extra></extra>")
        fig.add_vline(x=base, line_color=INK_2, line_width=1, annotation_text=f"base {f.pct(base, signed=True)}", annotation_position="top")
        fig.update_layout(barmode="overlay", legend=dict(orientation="h", y=-0.25))
        st.plotly_chart(_layout(fig, 120 + 46 * len(bars), f"{metric_name} with one driver moved, others at base"), width="stretch")
        st.caption("Each driver is moved to its low and high value in every industry at once. Exposure drivers move every company's exposure to its own low/high value.")
        st.dataframe(
            pd.DataFrame([{"Driver": b.driver.label, "At low": b.low_value, "At high": b.high_value, "Swing": b.swing} for b in an.tornado]),
            hide_index=True, width="stretch",
            column_config={c: st.column_config.NumberColumn(format="percent") for c in ["At low", "At high", "Swing"]},
        )

# ---------------------------------------------------------------- explanation
with tab_expl:
    st.markdown(explain_market(an, reg, names))
    st.caption("Generated from a template using the numbers above; no AI model is called.")

# ---------------------------------------------------------------- assumptions & sources
with tab_src:
    rows = [{"Type": "Shock input", "Scope": "All", "Item": u.label, "Low": None, "Base": an.base.inputs.get(u.key), "High": None, "Unit": u.unit, "Source": "user input", "Link": None}
            for u in shock.user_inputs]
    for a in shock.assumptions:
        lo, b, hi = rng[a.key]
        rows.append({"Type": "Assumption", "Scope": "All", "Item": a.label, "Low": lo, "Base": b, "High": hi, "Unit": a.unit,
                     "Source": ("Estimate: " + (a.rationale or "")) if a.is_estimate else a.source, "Link": a.source_url})
    for slug, eff in shock.industry_effects.items():
        if eff.effect == "none":
            rows.append({"Type": "No direct effect", "Scope": names[slug], "Item": "", "Low": None, "Base": None, "High": None, "Unit": "", "Source": eff.rationale, "Link": None})
        for a in eff.assumptions:
            lo, b, hi = rng[a.key]
            rows.append({"Type": "Assumption", "Scope": names[slug], "Item": a.label, "Low": lo, "Base": b, "High": hi, "Unit": a.unit,
                         "Source": ("Estimate: " + (a.rationale or "")) if a.is_estimate else a.source, "Link": a.source_url})
        for key in eff.exposure_keys:
            rows.append({"Type": "Exposure", "Scope": names[slug], "Item": reg.exposure_defs[key].label, "Low": None, "Base": None, "High": None,
                         "Unit": reg.exposure_defs[key].unit, "Source": "Per company; see the downloadable exposure table", "Link": None})
    adf = pd.DataFrame(rows)
    st.dataframe(adf, hide_index=True, width="stretch",
                 column_config={"Link": st.column_config.LinkColumn(display_text="source"), "Source": st.column_config.TextColumn(width="large")})
    exp_rows = []
    for slug, eff in shock.industry_effects.items():
        for key in eff.exposure_keys:
            for tk in universe.industry(slug).tickers:
                ev = reg.exposures[tk][key]
                exp_rows.append({"Industry": names[slug], "Ticker": tk, "Exposure": reg.exposure_defs[key].label, "Low": ev.low, "Base": ev.value, "High": ev.high,
                                 "Source": ("Estimate: " + (ev.rationale or "")) if ev.is_estimate else ev.source, "Link": ev.source_url})
    st.download_button("Download per-company exposures (CSV)", pd.DataFrame(exp_rows).to_csv(index=False), f"{shock.id}_exposures.csv", "text/csv")
    if shock.references:
        st.markdown("**References**: " + " · ".join(f"[{i + 1}]({u})" for i, u in enumerate(shock.references)))
    st.markdown("**Baseline data**: each company's latest 10-K via SEC EDGAR (see the Data page for tags and flags).")
footer()

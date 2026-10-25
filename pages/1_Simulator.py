"""Simulator: pick an industry and policy, set inputs, run, and read the impact.

The applied scenario lives in the URL (`?s=<token>`, see ui/state.py), so any result
can be shared or linked from the PDF and reloads to exactly the same numbers.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

import streamlit as st  # noqa: E402

from policyshock.config import load_universe  # noqa: E402
from policyshock.data import fred  # noqa: E402
from policyshock.engine.simulate import simulate  # noqa: E402
from policyshock.engine.valuation import persistence_label  # noqa: E402
from policyshock.narrative import templates  # noqa: E402
from policyshock.policies.loader import ConfigError, registry  # noqa: E402
from policyshock.ui import results  # noqa: E402
from policyshock.ui.common import cached_prices, footer, macro_strip, page_setup  # noqa: E402
from policyshock.ui.state import decode, encode  # noqa: E402

page_setup("Simulator")

try:
    reg = registry()
except ConfigError as exc:  # refuse to run on invalid configs
    st.error(f"```\n{exc}\n```")
    st.stop()

universe = load_universe()
industries = [i for i in universe.industries if reg.industry_policies(i.slug)]

# ---------------------------------------------------------------- initial state from URL
if "applied" not in st.session_state:
    st.session_state.applied = decode(st.query_params.get("s", "")) or None
    if st.session_state.applied:
        a = st.session_state.applied
        st.session_state["w_industry"] = a.get("i")
        st.session_state["w_policy"] = a.get("p")
        for k, v in a.get("in", {}).items():
            st.session_state[f"w_in_{a.get('p')}_{k}"] = v
        for k, (lo, base, hi) in a.get("a", {}).items():
            for case, v in zip(("low", "base", "high"), (lo, base, hi)):
                st.session_state[f"w_as_{a.get('p')}_{k}_{case}"] = v

# ---------------------------------------------------------------- sidebar
with st.sidebar:
    st.header("Scenario")
    slugs = [i.slug for i in industries]
    if st.session_state.get("w_industry") not in slugs:
        st.session_state["w_industry"] = "consumer_retail" if "consumer_retail" in slugs else slugs[0]
    industry = st.selectbox("Industry", slugs, format_func=lambda s: universe.industry(s).name, key="w_industry")
    pols = reg.industry_policies(industry)
    ids = [p.id for p in pols]
    if st.session_state.get("w_policy") not in ids:
        st.session_state["w_policy"] = ids[0]
    policy_id = st.selectbox("Policy", ids, format_func=lambda i: ("★ " if reg.policy(industry, i).showcase else "") + reg.policy(industry, i).name, key="w_policy")
    pol = reg.policy(industry, policy_id)
    st.caption(pol.description)
    st.caption(f"Persistence: {persistence_label(pol.persistence)}")
    st.caption(f"Mode: Industry ({len(universe.industry(industry).tickers)} companies). For a macro shock across every industry, use Full Market.")

    st.subheader("Policy inputs")
    inputs = {}
    for u in pol.user_inputs:
        k = f"w_in_{pol.id}_{u.key}"
        if k not in st.session_state:
            st.session_state[k] = u.default
        inputs[u.key] = st.number_input(
            f"{u.label} ({u.unit})", min_value=u.min, max_value=u.max, step=u.step, key=k, help=u.help
        )

    ranges, bad = {}, []
    with st.expander("Advanced assumptions"):
        for a in pol.assumptions:
            st.markdown(f"**{a.label}** ({a.unit})")
            src = ("Estimate: " + a.rationale) if a.is_estimate else a.source
            st.caption(src + (f" [link]({a.source_url})" if a.source_url else ""))
            cols = st.columns(3)
            vals = []
            for col, case in zip(cols, ("low", "base", "high")):
                k = f"w_as_{pol.id}_{a.key}_{case}"
                if k not in st.session_state:
                    st.session_state[k] = float(getattr(a, case))
                vals.append(col.number_input(case, key=k, format="%.4g"))
            if not vals[0] <= vals[1] <= vals[2]:
                bad.append(a.label)
            ranges[a.key] = tuple(vals)
        comps = set()
        for comp in pol.components:
            if st.checkbox(f"Include {comp.replace('_', ' ')} effects", value=True, key=f"w_c_{pol.id}_{comp}"):
                comps.add(comp)
    if bad:
        st.error("Low ≤ base ≤ high is required for: " + ", ".join(bad))
    run = st.button("Run", type="primary", width="stretch", disabled=bool(bad))

edited = {k: list(v) for k, v in ranges.items() if v != (pol.assumption(k).low, pol.assumption(k).base, pol.assumption(k).high)}
current = {"m": "industry", "i": industry, "p": pol.id, "in": {k: float(v) for k, v in inputs.items()}, "a": edited}
if pol.components:
    current["c"] = sorted(comps)
if run:
    st.session_state.applied = current
    st.query_params["s"] = encode(current)

# ---------------------------------------------------------------- results
st.title("Policy simulator")
applied = st.session_state.applied
if not applied:
    st.info("Choose an industry and a policy in the sidebar, adjust the inputs, then press **Run**.")
    macro_strip()
    footer()
    st.stop()


@st.cache_data(max_entries=64, show_spinner="Running scenario…")
def run_scenario(token: str, prices_df):
    s = decode(token)
    p = reg.policy(s["i"], s["p"])
    rng = {a.key: (a.low, a.base, a.high) for a in p.assumptions} | {k: tuple(v) for k, v in s.get("a", {}).items()}
    comps = set(s["c"]) if "c" in s else None
    return simulate(s["i"], s["p"], inputs=s.get("in"), assumption_ranges=rng, components=comps, prices_df=prices_df, macro=fred.macro_context()), rng


token = encode(applied)
try:
    an, rng = run_scenario(token, cached_prices())
except Exception as exc:  # a bad deep link shouldn't crash the page
    st.error(f"Couldn't run this scenario: {exc}")
    st.stop()

pol = an.base.policy
st.subheader(f"{pol.name} · {universe.industry(pol.industry).name}")
inputs_txt = " · ".join(f"{u.label}: **{an.base.inputs[u.key]:g} {u.unit}**" for u in pol.user_inputs)
st.markdown(inputs_txt)
# compare on a normalised basis: a deep link may omit inputs that are at their defaults
applied_full = {**applied, "in": {k: float(v) for k, v in {**pol.default_inputs(), **applied.get("in", {})}.items()}, "a": applied.get("a", {})}
if decode(encode(current)) != decode(encode(applied_full)):
    st.caption("Sidebar has changes that aren't applied yet; press **Run** to update.")

link = f"{(st.context.url or '').split('?')[0]}?s={token}"
with st.popover("🔗 Copy scenario link"):
    st.code(link, language=None)
    st.caption("Opening this link reproduces exactly this scenario.")

tab_over, tab_co, tab_sens, tab_expl, tab_src = st.tabs(["Overview", "Companies", "Sensitivity", "Explanation", "Assumptions & sources"])
with tab_over:
    results.overview(an, reg)
    st.markdown("**Macro context** (FRED)")
    macro_strip()
with tab_co:
    results.companies(an)
    df = results.company_frame(an)
    st.download_button("Download company results (CSV)", df.to_csv(index=False), f"{pol.id}_companies.csv", "text/csv")
with tab_sens:
    results.tornado(an)
with tab_expl:
    st.markdown(templates.explain(an, reg))
    st.caption("Generated from a template using the numbers above; no AI model is called.")
with tab_src:
    adf = results.assumptions(an, reg, rng)
    st.download_button("Download assumptions (CSV)", adf.to_csv(index=False), f"{pol.id}_assumptions.csv", "text/csv")
footer()

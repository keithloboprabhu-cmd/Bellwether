"""Bellwether landing page. Run with:  streamlit run app.py"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))

import streamlit as st  # noqa: E402

from policyshock.config import load_universe  # noqa: E402
from policyshock.data import fred  # noqa: E402
from policyshock.engine.simulate import simulate  # noqa: E402
from policyshock.macro.aggregate import simulate_market  # noqa: E402
from policyshock.narrative import formatting as f  # noqa: E402
from policyshock.policies.loader import registry  # noqa: E402
from policyshock.ui.common import cached_prices, footer, macro_strip, page_setup  # noqa: E402
from policyshock.ui.state import encode  # noqa: E402

page_setup("Home")
universe = load_universe()
reg = registry()

st.title("Bellwether")
st.markdown(
    "**See how a policy could affect company earnings: revenue, margins, EPS and implied value for real companies, "
    "built from their latest SEC filings.**"
)
c1, c2, c3 = st.columns(3)
c1.markdown(f"**1. Pick an industry and a policy**  \n{len(universe.industries)} industries, {len(universe.all_tickers)} companies, or a macro shock across all of them.")
c2.markdown("**2. Set the inputs**  \nTariff %, rate change, rebate size… every assumption is editable and sourced.")
c3.markdown("**3. Read the impact**  \nCompany-level ΔEPS with low/base/high ranges, winners and losers, and what drives the result.")
l1, l2 = st.columns(2)
l1.page_link("pages/1_Simulator.py", label="Industry simulator →", icon="▶️")
l2.page_link("pages/2_Full_Market.py", label="Full Market (macro shocks) →", icon="🌐")


@st.cache_data(show_spinner="Running the showcase scenarios…")
def showcase_results(prices_df) -> list[dict]:
    """Headline numbers for each showcase scenario at its default inputs (real engine runs)."""
    macro = fred.macro_context()
    out = []
    for sh in reg.macro_shocks():
        if not sh.showcase:
            continue
        an = simulate_market(sh.id, prices_df=prices_df, macro=macro)
        t = an.base.totals()
        ranked = [c for c in an.ranked_companies() if abs(c.dNI) > 1e-6]
        out.append({
            "title": sh.name, "scope": f"Full Market · {t['n']} companies",
            "inputs": " · ".join(f"{u.label}: {u.default:g} {u.unit}" for u in sh.user_inputs),
            "headline": f"Cap-weighted Δ EPS {f.pct(t['cw_d_eps_pct'], signed=True)}; implied value {f.money(t['d_mcap'], signed=True)}.",
            "detail": f"Most helped {ranked[0].ticker}, most hurt {ranked[-1].ticker}." if ranked else "",
            "url": "Full_Market?s=" + encode({"m": "market", "x": sh.id, "in": {k: float(v) for k, v in sh.default_inputs().items()}, "a": {}}),
        })
    showcases = [(ind.slug, p) for ind in universe.industries for p in reg.industry_policies(ind.slug) if p.showcase]
    for slug, pol in showcases:
        an = simulate(slug, pol.id, prices_df=prices_df, macro=macro)
        t = an.base.totals()
        bits = [c for c in (an.long, an.short) if c is not None]
        out.append({
            "title": pol.name, "scope": f"{universe.industry(slug).name} · {len(an.base.companies)} companies",
            "inputs": " · ".join(f"{u.label}: {u.default:g} {u.unit}" for u in pol.user_inputs),
            "headline": f"Industry Δ EPS {f.pct(t['d_eps_pct'], signed=True)}; implied value {f.money(t['d_mcap'], signed=True)}.",
            "detail": " ".join(f"{'Long' if c is an.long else 'Short'} {c.ticker}." for c in bits),
            "url": "Simulator?s=" + encode({"m": "industry", "i": slug, "p": pol.id, "in": {k: float(v) for k, v in pol.default_inputs().items()}, "a": {}}),
        })
    return out


st.subheader("Showcase scenarios")
st.caption("Computed live from the engine at each scenario's default inputs. Open one to change the inputs and see why.")
cards = showcase_results(cached_prices())
for row in range(0, len(cards), 3):
    cols = st.columns(3)
    for col, c in zip(cols, cards[row : row + 3]):
        with col.container(border=True):
            st.markdown(f"**{c['title']}**  \n{c['scope']}")
            st.caption(c["inputs"])
            st.markdown(f"{c['headline']} {c['detail']}")
            st.markdown(f"[Open this scenario →]({c['url']})")

st.markdown("**Macro context** (FRED)")
macro_strip()
footer()

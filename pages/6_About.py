"""About: purpose, scope, data sources, limits and attribution."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

import streamlit as st  # noqa: E402

from policyshock.config import load_universe  # noqa: E402
from policyshock.policies.loader import registry  # noqa: E402
from policyshock.ui.common import footer, page_setup  # noqa: E402

page_setup("About")
universe = load_universe()
reg = registry()
n_pol = sum(len(reg.industry_policies(i.slug)) for i in universe.industries)

st.title("About PolicyShock")
st.markdown(
    f"""
PolicyShock is a teaching tool built for **Duke FMKT 256**. It asks a narrow question: *if this policy changed
tomorrow, what would the first-order effect be on the revenue, margins, earnings per share and implied value of
specific companies?* It covers **{len(universe.all_tickers)} public companies in {len(universe.industries)} industries**,
**{n_pol} industry policies** and **{len(reg.macro)} macro shocks** that run across every industry at once.

### What it does
- Starts from each company's latest annual 10-K (SEC EDGAR) and recent share price.
- Passes a policy through explicit channels (costs, prices, demand, taxes, financing, government budgets),
  each a short formula documented on the Methodology page.
- Shows a base case and a low/high range built from sourced assumptions, the drivers that matter most,
  the most helped and hurt companies, and a template-generated explanation of the result.
- Checks itself against history on the Backtests page (the 2017 tax cut and the 2018 steel tariffs).

### What it doesn't do
- It is **first-order and partial-equilibrium**: it adds up direct effects and holds everything else fixed.
  Feedback through the Fed, exchange rates, competitors' responses or the wider economy is left out unless a
  scenario switches it on as a labelled second-round component.
- Ranges are **scenario bounds**, not statistical confidence intervals.
- The companies are a **curated teaching sample**, not an index; Full Market totals describe that sample only.
- Company exposures are sourced from filings where possible; the rest are labelled estimates with a rationale,
  and companies added to broaden coverage use peer-based estimates that should be reviewed before relying on them.
- **Not investment advice.** The long/short labels illustrate how a policy separates winners from losers.

### Data
- **SEC EDGAR** XBRL company facts: annual financials (free, keyless).
- **FRED** (St. Louis Fed): interest rates, inflation, unemployment, GDP and consumer spending (free, keyless).
- **Yahoo Finance** via the open-source `yfinance` library: share prices, with a committed snapshot as fallback.
- No paid data or APIs, and no AI model is called when the app runs; every explanation is a fixed template filled
  with the computed numbers.

### Credits
Built by a Duke FMKT 256 student team. Every assumption lists its source or is marked as an estimate with a
one-line reason; the Assumptions & sources tab on each result and the Data page show where each number comes from.
"""
)
footer()

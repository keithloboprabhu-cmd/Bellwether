"""PolicyShock landing page. Run with:  streamlit run app.py"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))

import streamlit as st  # noqa: E402

from policyshock.ui.common import footer, macro_strip, page_setup  # noqa: E402

page_setup("Home")
st.title("PolicyShock")
st.markdown(
    "**Simulate how a policy change hits the revenue, margins, EPS and value of real companies, "
    "using their latest SEC filings.**"
)
c1, c2, c3 = st.columns(3)
c1.markdown("**1. Pick an industry and a policy**  \nTen industries, 60 companies, or the full market.")
c2.markdown("**2. Set the inputs**  \nTariff %, rate change, rebate size… every assumption is editable and sourced.")
c3.markdown("**3. Read the impact**  \nCompany-level ΔEPS with low/base/high ranges, winners and losers, and what drives the result.")
st.page_link("pages/1_Simulator.py", label="Open the simulator →", icon="▶️")
macro_strip()
footer()

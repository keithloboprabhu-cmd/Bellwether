"""Methodology: the model write-up (METHODOLOGY.md) plus estimated GDP revenue betas."""

import sys
from pathlib import Path

ROOT = Path(__file__).parents[1]
sys.path.insert(0, str(ROOT / "src"))

import pandas as pd  # noqa: E402
import streamlit as st  # noqa: E402

from policyshock.config import load_universe  # noqa: E402
from policyshock.macro import gdp_beta  # noqa: E402
from policyshock.ui.common import footer, page_setup  # noqa: E402

page_setup("Methodology")
st.markdown((ROOT / "METHODOLOGY.md").read_text())

st.header("Industry revenue betas to real GDP")
st.markdown(
    "Pooled OLS of annual revenue growth on real GDP growth (FRED GDPC1), FY2009 to latest, six companies per industry. "
    "Used by the Full Market recession shock. These are **small, noisy samples**: read β with its standard error, "
    "and compare with the estimate that drops pandemic years (FY ending 2020–21)."
)
names = {i.slug: i.name for i in load_universe().industries}
b = pd.DataFrame(gdp_beta.load().values())
st.dataframe(
    pd.DataFrame(
        {
            "Industry": b["industry"].map(names),
            "β (all years)": b["beta"],
            "s.e.": b["se"],
            "R²": b["r2"],
            "n": b["n"],
            "β ex-2020/21": b["beta_ex_covid"],
            "s.e. ex-2020/21": b["se_ex_covid"],
            "R² ex-2020/21": b["r2_ex_covid"],
            "n ex-2020/21": b["n_ex_covid"],
            "Winsorized points": b["n_clipped"],
        }
    ),
    hide_index=True,
    width="stretch",
    column_config={c: st.column_config.NumberColumn(format="%.2f") for c in ["β (all years)", "s.e.", "R²", "β ex-2020/21", "s.e. ex-2020/21", "R² ex-2020/21"]},
)
st.caption("A β of 2 means revenue grows about 2% faster than usual for each extra 1% of real GDP growth. Revenue growth is winsorized at −50%/+100% to limit M&A effects.")
footer()

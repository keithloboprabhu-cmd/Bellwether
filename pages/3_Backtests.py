"""Ten-industry historical policy replays and a defined directional score."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

import pandas as pd
import streamlit as st

from policyshock.backtests.suite import report
from policyshock.ui.common import page_setup

page_setup("Backtests")
st.title("Historical backtests")


@st.cache_data
def backtest_report():
    """Run deterministic comparisons against committed historical observations."""
    return report()


result = backtest_report()
s = result["summary"]
a, b, c = st.columns(3)
a.metric("Overall directional accuracy", f"{s['accuracy_pct']:.1f}%", f"{s['hits']} / {s['n']} comparisons", delta_color="off")
b.metric("Industry coverage", f"{s['industries']} / 10")
c.metric("Equal-industry score", f"{s['industry_balanced_pct']:.1f}%")
st.write(result["definition"])
st.caption(result["limits"])
st.dataframe(pd.DataFrame([{
    "Industry": case["industry_name"], "Policy": case["title"],
    "Correct": case["summary"]["hits"], "Eligible": case["summary"]["n"],
    "Accuracy (%)": case["summary"]["accuracy_pct"],
    "Model MAE": case["summary"]["mae"], "No-change MAE": case["summary"]["no_change_mae"], "Unit": case["unit"],
} for case in result["cases"]]), hide_index=True)
for case in result["cases"]:
    with st.expander(f"{case['industry_name']} / {case['title']}"):
        st.write(case["event"])
        st.write(case["context"])
        st.caption(case["cohort_rule"])
        for source in case["sources"]:
            st.markdown(f"[{source['label']}]({source['url']})")
        st.dataframe(pd.DataFrame([{
            "Company": r["ticker"], "Before": r["base_period"], "After": ", ".join(r["post_periods"]),
            f"Predicted ({case['unit']})": r["predicted"], f"Observed ({case['unit']})": r["actual"],
            "Direction": "Correct" if r["direction_ok"] else "Miss", "Notes": " · ".join(r["notes"]),
        } for r in case["rows"]]), hide_index=True)
        st.caption(f"Excluded: {len(case['excluded'])}")
        st.dataframe(pd.DataFrame(case["excluded"]), hide_index=True)

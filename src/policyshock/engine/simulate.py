"""One-call entry point: registry + snapshots → full Analysis for an industry policy."""

from __future__ import annotations

import pandas as pd

from policyshock.config import load_universe
from policyshock.data import fred, prices, store
from policyshock.engine.scenarios import prepare_baselines
from policyshock.engine.sensitivity import Analysis, Runner, analyze
from policyshock.policies.loader import Registry, registry


def industry_baselines(industry: str, prices_df: pd.DataFrame | None = None) -> list[dict]:
    """Prepared baselines for every company in an industry (snapshot prices by default)."""
    tickers = load_universe().industry(industry).tickers
    px = prices.load_snapshot() if prices_df is None else prices_df
    return prepare_baselines(store.baseline_frame(tickers, px))


def build_runner(
    industry: str,
    policy_id: str,
    inputs: dict | None = None,
    assumption_ranges: dict[str, tuple[float, float, float]] | None = None,
    components: set[str] | None = None,
    prices_df: pd.DataFrame | None = None,
    macro: dict | None = None,
    reg: Registry | None = None,
    baselines: list[dict] | None = None,
) -> Runner:
    """Build the shared engine runner, optionally with captured live annual inputs."""
    reg = reg or registry()
    pol = reg.policy(industry, policy_id)
    ranges = {a.key: (a.low, a.base, a.high) for a in pol.assumptions} | (assumption_ranges or {})
    return Runner(
        policy=pol,
        baselines=industry_baselines(industry, prices_df) if baselines is None else baselines,
        inputs={**pol.default_inputs(), **(inputs or {})},
        assumption_ranges=ranges,
        exposure_cfg=reg.exposures,
        components=None if components is None else frozenset(components),
        macro=macro if macro is not None else fred.macro_context(),
        exposure_labels={k: d.label for k, d in reg.exposure_defs.items()},
    )


def simulate(industry: str, policy_id: str, **kw) -> Analysis:
    """Run base case, tornado, ranges and long/short for one industry policy."""
    return analyze(build_runner(industry, policy_id, **kw))

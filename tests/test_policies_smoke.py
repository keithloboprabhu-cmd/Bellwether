"""Smoke test: every policy runs with defaults on every company in its industry.

Fails on exceptions or NaN/inf; reports (as warnings, for human review) any company
whose |ΔEPS %| exceeds 100%.
"""

from __future__ import annotations

import math
import warnings

import pytest

from policyshock.engine.simulate import simulate
from policyshock.policies.loader import registry

POLICIES = sorted(registry().policies)


def _finite(x) -> bool:
    return x is None or math.isfinite(x)


@pytest.mark.parametrize("key", POLICIES)
def test_policy_runs_with_defaults(key):
    industry, pid = key.split("/")
    an = simulate(industry, pid)
    for c in an.base.companies:
        for field in ("dR", "dEBIT", "dNI", "dEPS", "dEPS_pct", "dP", "dP_pct", "d_mcap", "d_margin_bps"):
            assert _finite(getattr(c, field)), f"{key} {c.ticker} {field} not finite"
        if c.dEPS_pct is not None and abs(c.dEPS_pct) > 1.0:
            warnings.warn(f"REVIEW {key}: {c.ticker} ΔEPS {c.dEPS_pct:+.0%} at defaults")
    assert all(_finite(v) for v in an.base.totals().values() if isinstance(v, float))
    assert an.tornado, f"{key}: no uncertain drivers — every policy should have a range"


@pytest.mark.parametrize("key", POLICIES)
def test_envelope_brackets_base(key):
    """Each company's pessimistic ≤ base ≤ optimistic (in $/share value terms)."""
    industry, pid = key.split("/")
    an = simulate(industry, pid)
    for c in an.base.companies:
        e = an.envelopes[c.ticker]
        m = lambda r: r.dP if r.dP is not None else r.dEPS  # noqa: E731
        assert m(e.low) <= m(c) + 1e-9 <= m(e.high) + 2e-9, f"{key} {c.ticker}"


@pytest.mark.parametrize("key", POLICIES)
def test_zero_inputs_give_zero_effect(key):
    """Setting every numeric input to zero (where allowed) should switch the policy off."""
    industry, pid = key.split("/")
    pol = registry().policy(industry, pid)
    zeros = {u.key: 0 for u in pol.user_inputs if u.type == "number" and (u.min is None or u.min <= 0)}
    if len(zeros) < len([u for u in pol.user_inputs if u.type == "number"]):
        pytest.skip("not every input can be zero")
    an = simulate(industry, pid, inputs=zeros)
    assert all(abs(c.dNI) < 1e-9 for c in an.base.companies)

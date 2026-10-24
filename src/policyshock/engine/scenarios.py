"""Run a policy on a set of companies: resolve parameters, run channels, aggregate.

A scenario is fully described by (policy, user inputs, assumption values, exposure
case, enabled components). Everything is deterministic, so the same scenario (e.g.
from a deep link) always reproduces the same numbers.
"""

from __future__ import annotations

import math
import statistics
from dataclasses import dataclass, field
from typing import Literal

import pandas as pd

from policyshock.engine.channels import CHANNELS, run_channel
from policyshock.engine.expressions import evaluate, references
from policyshock.engine.model import BASELINE_FIELDS, ChannelOutcome, CompanyResult, aggregate
from policyshock.policies.schema import Policy

Case = Literal["low", "base", "high"]


# --------------------------------------------------------------------------- baselines


def prepare_baselines(frame: pd.DataFrame) -> list[dict]:
    """Model-ready baseline dicts with gaps filled (and noted) for one industry.

    - missing contribution margin → industry median (flagged estimate)
    - missing cost of revenue → R × (1 − cm)
    - missing pretax income → EBIT − interest
    """
    rows = frame.to_dict("records")
    cms = [r["contribution_margin"] for r in rows if _ok(r.get("contribution_margin"))]
    median_cm = statistics.median(cms) if cms else 0.3
    out = []
    for r in rows:
        r = {k: (None if (isinstance(v, float) and math.isnan(v)) else v) for k, v in r.items()}
        r["model_flags"] = []
        if not _ok(r.get("contribution_margin")):
            if r["kind"] == "bank":
                r["contribution_margin"] = 1.0  # bank revenue is net revenue; changes fall to pretax
            else:
                r["contribution_margin"] = median_cm
                r["model_flags"].append(f"contribution margin set to industry median {median_cm:.0%}")
        if not _ok(r.get("cost_of_revenue")) and r["revenue"]:
            r["cost_of_revenue"] = r["revenue"] * (1 - r["contribution_margin"]) if r["kind"] != "bank" else 0.0
        if not _ok(r.get("pretax_income")):
            r["pretax_income"] = (r["operating_income"] or 0.0) - (r.get("interest_expense") or 0.0)
            r["model_flags"].append("pretax income approximated as EBIT − interest")
        out.append(r)
    return out


def _ok(v) -> bool:
    return v is not None and not (isinstance(v, float) and math.isnan(v))


# --------------------------------------------------------------------------- results


@dataclass
class IndustryResult:
    policy: Policy
    inputs: dict
    assumptions: dict[str, float]
    companies: list[CompanyResult]
    components: frozenset[str] = frozenset()
    derived: dict[str, float] = field(default_factory=dict)

    def totals(self) -> dict:
        """Industry totals: sums of $ deltas, % changes = Σ deltas / Σ baselines."""
        cs = self.companies
        R = sum(c.baseline["revenue"] or 0 for c in cs)
        EBIT = sum(c.baseline["operating_income"] or 0 for c in cs)
        NI_model = sum(c.baseline["pretax_income"] * (1 - c.tax_rate) for c in cs)
        dR = sum(c.dR for c in cs)
        dEBIT = sum(c.dEBIT for c in cs)
        dNI = sum(c.dNI for c in cs)
        mcap = sum(c.baseline.get("market_cap") or 0 for c in cs)
        d_mcap_known = [c.d_mcap for c in cs if c.d_mcap is not None]
        return {
            "revenue": R,
            "d_revenue": dR,
            "d_revenue_pct": dR / R if R else None,
            "d_ebit": dEBIT,
            "d_margin_bps": ((EBIT + dEBIT) / (R + dR) - EBIT / R) * 10_000 if R and R + dR else None,
            "d_ni": dNI,
            # industry "ΔEPS %" = Σ ΔNI / Σ baseline NI (model baseline, so a zero shock is exactly 0)
            "d_eps_pct": dNI / NI_model if NI_model > 0 else None,
            "market_cap": mcap,
            "d_mcap": sum(d_mcap_known) if d_mcap_known else None,
            "d_mcap_pct": sum(d_mcap_known) / mcap if (d_mcap_known and mcap) else None,
            "n_mcap_nm": len(cs) - len(d_mcap_known),
        }

    def company(self, ticker: str) -> CompanyResult:
        return next(c for c in self.companies if c.ticker == ticker)


# --------------------------------------------------------------------------- runner


def exposure_values(policy: Policy, tickers: list[str], exposures: dict, case: dict[str, Case] | None = None) -> dict:
    """{ticker: {key: value}} at the requested case per exposure key (default base)."""
    case = case or {}
    out: dict[str, dict[str, float]] = {}
    for t in tickers:
        out[t] = {}
        for key in policy.exposure_keys:
            ev = exposures[t][key]
            c = case.get(key, "base")
            out[t][key] = ev.low if c == "low" else ev.high if c == "high" else ev.value
    return out


def run_policy(
    policy: Policy,
    baselines: list[dict],
    inputs: dict | None = None,
    assumptions: dict[str, float] | None = None,
    exposures: dict[str, dict[str, float]] | None = None,
    components: set[str] | frozenset[str] | None = None,
    macro: dict[str, float] | None = None,
) -> IndustryResult:
    """Run `policy` on every company in `baselines`.

    inputs       user inputs (missing keys take defaults)
    assumptions  assumption values (missing keys take base)
    exposures    {ticker: {key: value}} (required for every exposure key the policy uses)
    components   enabled optional components (e.g. {"second_round"}); default: all
    macro        macro context for macro.<key> names
    """
    inputs = {**policy.default_inputs(), **(inputs or {})}
    a_vals = {a.key: a.base for a in policy.assumptions} | (assumptions or {})
    comps = frozenset(policy.components if components is None else components)
    results = []
    derived_shown: dict[str, float] = {}
    for b in baselines:
        role = policy.role_of(b["ticker"])
        ctx = {
            "input": inputs,
            "assumption": a_vals,
            "exposure": (exposures or {}).get(b["ticker"], {}),
            "baseline": {k: b.get(k) for k in BASELINE_FIELDS},
            "macro": macro or {},
            "role": {"is_importer": role == "importer", "is_domestic_producer": role == "domestic_producer", "is_neutral": role == "neutral"},
            "derived": {},
        }
        for key, expr in policy.derived.items():  # in file order; later ones may use earlier ones
            ctx["derived"][key] = evaluate(expr, ctx)
        if not derived_shown:
            derived_shown = {k: v for k, v in ctx["derived"].items() if isinstance(v, (int, float))}
        outcomes = []
        for spec in policy.channels:
            if spec.roles and role not in spec.roles:
                continue
            if spec.component and spec.component not in comps:
                continue
            params = {k: float(evaluate(v, ctx)) for k, v in spec.params.items()}
            delta = run_channel(spec.type, b, params)
            exp_refs = tuple(sorted({k for v in spec.params.values() for ns, k in references(v) if ns == "exposure"}))
            outcomes.append(
                ChannelOutcome(
                    label=spec.label or spec.type.replace("_", " "),
                    family=CHANNELS[spec.type].family,
                    persistence=spec.persistence or policy.persistence,
                    delta=delta,
                    exposure_refs=exp_refs,
                )
            )
        res = aggregate(b, outcomes, role=role)
        res.notes = list(b.get("model_flags", [])) + res.notes
        results.append(res)
    return IndustryResult(policy, inputs, a_vals, results, comps, derived_shown)

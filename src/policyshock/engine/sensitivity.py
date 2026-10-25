"""Ranges, tornado chart and long/short picks.

Why not just "all-low vs all-high"? A low value is not always bad news: low tariff
pass-through hurts an importer, but low demand elasticity helps it. So we first run
each uncertain driver one at a time (the tornado), note which end hurts each company,
then build that company's pessimistic case from all its hurtful ends and its
optimistic case from all its helpful ends. The industry range is built the same way
using the industry-level metric.

Drivers are the policy's uncertain assumptions plus each exposure key (moving every
company's exposure to its own low/high together).
"""

from __future__ import annotations

from dataclasses import dataclass, field

from policyshock.engine.model import CompanyResult
from policyshock.engine.scenarios import IndustryResult, exposure_values, run_policy
from policyshock.policies.schema import Policy


@dataclass(frozen=True)
class Driver:
    kind: str  # "assumption" | "exposure"
    key: str
    label: str
    low: float | None = None  # shown in the tornado (None for exposures: per-company)
    high: float | None = None
    unit: str = ""


@dataclass
class TornadoBar:
    driver: Driver
    low_value: float  # industry metric with driver at low
    high_value: float
    swing: float


@dataclass
class Envelope:
    low: CompanyResult
    high: CompanyResult


@dataclass
class Analysis:
    base: IndustryResult
    metric: str  # "d_eps_pct" or "d_mcap_pct"
    tornado: list[TornadoBar]
    envelopes: dict[str, Envelope]  # ticker → pessimistic / optimistic company results
    industry_low: IndustryResult
    industry_high: IndustryResult
    long: CompanyResult | None = None
    short: CompanyResult | None = None
    low_conviction: bool = False
    notes: list[str] = field(default_factory=list)


@dataclass
class Runner:
    """Everything needed to re-run one scenario with drivers moved to low/high."""

    policy: Policy
    baselines: list[dict]
    inputs: dict
    assumption_ranges: dict[str, tuple[float, float, float]]  # key → (low, base, high), user-editable
    exposure_cfg: dict  # ticker → key → ExposureValue
    components: frozenset[str] | None = None
    macro: dict | None = None
    exposure_labels: dict[str, str] = field(default_factory=dict)

    @property
    def tickers(self) -> list[str]:
        return [b["ticker"] for b in self.baselines]

    def drivers(self) -> list[Driver]:
        out = []
        for a in self.policy.assumptions:
            lo, _, hi = self.assumption_ranges[a.key]
            if lo != hi:
                out.append(Driver("assumption", a.key, a.label, lo, hi, a.unit))
        for key in self.policy.exposure_keys:
            vals = [self.exposure_cfg[t][key] for t in self.tickers]
            if any(v.low != v.high for v in vals):
                out.append(Driver("exposure", key, self.exposure_labels.get(key, key.replace("_", " ")), unit="per company"))
        return out

    def run(self, case: dict[Driver, str] | None = None) -> IndustryResult:
        case = case or {}
        a_vals = {k: v[1] for k, v in self.assumption_ranges.items()}
        exp_case = {}
        for d, c in case.items():
            if d.kind == "assumption":
                if d.key not in self.assumption_ranges:  # driver from another industry (Full Market)
                    continue
                lo, base, hi = self.assumption_ranges[d.key]
                a_vals[d.key] = lo if c == "low" else hi if c == "high" else base
            else:
                exp_case[d.key] = c
        ex = exposure_values(self.policy, self.tickers, self.exposure_cfg, exp_case)
        return run_policy(self.policy, self.baselines, self.inputs, a_vals, ex, self.components, self.macro)


def _company_metric(c: CompanyResult) -> float:
    """Per-share value change, or ΔEPS when value isn't meaningful."""
    return c.dP if c.dP is not None else c.dEPS


def _industry_metric(r: IndustryResult, metric: str) -> float:
    v = r.totals()[metric]
    return 0.0 if v is None else v


def analyze(runner: Runner) -> Analysis:
    """Base case, tornado, per-company and industry ranges, and long/short."""
    base = runner.run()
    drivers = runner.drivers()
    one_at_a_time = {d: (runner.run({d: "low"}), runner.run({d: "high"})) for d in drivers}

    # Tornado on industry ΔEPS %; fall back to Δ value % for value-only policies.
    metric = "d_eps_pct"
    if all(abs(_industry_metric(lo, metric) - _industry_metric(hi, metric)) < 1e-12 for lo, hi in one_at_a_time.values()):
        if base.totals()["d_mcap_pct"] is not None:
            metric = "d_mcap_pct"
    bars = []
    for d, (lo, hi) in one_at_a_time.items():
        lv, hv = _industry_metric(lo, metric), _industry_metric(hi, metric)
        bars.append(TornadoBar(d, lv, hv, abs(hv - lv)))
    bars.sort(key=lambda b: b.swing, reverse=True)

    # Oriented envelopes per company
    envelopes = {}
    for t in runner.tickers:
        pess, opt = {}, {}
        for d, (lo, hi) in one_at_a_time.items():
            m_lo, m_hi = _company_metric(lo.company(t)), _company_metric(hi.company(t))
            pess[d], opt[d] = ("low", "high") if m_lo <= m_hi else ("high", "low")
        envelopes[t] = Envelope(runner.run(pess).company(t), runner.run(opt).company(t))

    # Oriented industry range
    pess, opt = {}, {}
    for d, (lo, hi) in one_at_a_time.items():
        lv, hv = _industry_metric(lo, metric), _industry_metric(hi, metric)
        pess[d], opt[d] = ("low", "high") if lv <= hv else ("high", "low")
    ind_low, ind_high = runner.run(pess), runner.run(opt)

    an = Analysis(base, metric, bars, envelopes, ind_low, ind_high)
    _pick_long_short(an)
    return an


def _range_pct(c_low: CompanyResult, c_high: CompanyResult) -> tuple[float, float]:
    return c_low.rank_value, c_high.rank_value


def _pick_long_short(an: Analysis) -> None:
    """Long = most helped, short = most hurt (by implied Δprice %, else ΔEPS %).

    Only companies the policy actually moves are eligible: unaffected names and names whose
    % change is n/m (negative baseline EPS) are left out rather than ranked as zero.
    """
    def metric(c):
        return c.dP_pct if c.dP_pct is not None else c.dEPS_pct

    affected = [c for c in an.base.companies if metric(c) is not None and abs(metric(c)) > 1e-6]
    affected.sort(key=metric, reverse=True)
    if not affected:
        an.notes.append("No company is meaningfully affected, so there is no long/short call.")
        return
    if len(affected) == 1:
        c = affected[0]
        if metric(c) > 0:
            an.long = c
        else:
            an.short = c
        an.notes.append(f"Only {c.ticker} is materially affected, so there is a single call rather than a pair.")
        return
    an.long, an.short = affected[0], affected[-1]
    long_lo, _ = _range_pct(an.envelopes[an.long.ticker].low, an.envelopes[an.long.ticker].high)
    _, short_hi = _range_pct(an.envelopes[an.short.ticker].low, an.envelopes[an.short.ticker].high)
    # Ranges overlap when the long's pessimistic case is worse than the short's optimistic case.
    an.low_conviction = long_lo < short_hi
    if metric(an.long) <= 0:
        an.notes.append("Every affected company is hurt; the 'long' is simply the least-hurt name (a relative-value pair).")
    if metric(an.short) >= 0:
        an.notes.append("Every affected company is helped; the 'short' is simply the least-helped name (a relative-value pair).")
    skipped = [c.ticker for c in an.base.companies if c not in affected]
    if skipped:
        an.notes.append("Not ranked (unaffected or n/m): " + ", ".join(skipped) + ".")

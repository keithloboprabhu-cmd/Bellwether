"""Full Market mode: run one macro shock across all 10 industries and 60 companies.

Each industry's block of a macro config is an ordinary industry Policy, so the same
channels, aggregation, valuation and range logic apply. This module adds the market
layer:

- **Market headline:** cap-weighted Δ EPS % (Σ mcap·ΔEPS% / Σ mcap over companies with a
  meaningful ΔEPS %) and implied Δ market value (Σ Δmcap / Σ mcap). Always labelled
  "60-company sample, cap-weighted", never "the market".
- **Market tornado and range:** drivers are the union of all industries' uncertain
  assumptions and exposures. Each is moved low/high with the rest at base across *all*
  industries; the market range orients every driver by its effect on the market metric.
- **Per-company and per-industry ranges** are oriented within the company's own industry
  (see engine/sensitivity.py).

First-order, partial equilibrium: industries' effects are summed. Second-round effects
appear only as separately labelled, toggleable `component`s in the config.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from policyshock.config import load_universe
from policyshock.engine.model import CompanyResult, aggregate
from policyshock.engine.scenarios import IndustryResult
from policyshock.engine.sensitivity import Driver, Envelope, Runner, TornadoBar, _company_metric
from policyshock.engine.simulate import industry_baselines
from policyshock.policies.loader import Registry, registry
from policyshock.policies.schema import MacroShock


@dataclass
class MarketResult:
    shock: MacroShock
    inputs: dict
    industries: dict[str, IndustryResult]  # slug → result (zero results for effect: none)

    @property
    def companies(self) -> list[CompanyResult]:
        return [c for r in self.industries.values() for c in r.companies]

    def totals(self) -> dict:
        cs = self.companies
        eps_w = [(c.baseline.get("market_cap") or 0, c.dEPS_pct) for c in cs if c.dEPS_pct is not None and c.baseline.get("market_cap")]
        w = sum(m for m, _ in eps_w)
        mcap = sum(c.baseline.get("market_cap") or 0 for c in cs)
        d_mcap = [c.d_mcap for c in cs if c.d_mcap is not None]
        ni = sum(c.baseline["pretax_income"] * (1 - c.tax_rate) * c.baseline.get("parent_share", 1.0) for c in cs)
        return {
            "cw_d_eps_pct": sum(m * e for m, e in eps_w) / w if w else None,
            "d_mcap": sum(d_mcap) if d_mcap else None,
            "d_mcap_pct": sum(d_mcap) / mcap if mcap else None,
            "d_ni": sum(c.dNI for c in cs),
            "d_ni_pct": sum(c.dNI for c in cs) / ni if ni > 0 else None,
            "market_cap": mcap,
            "n": len(cs),
        }


@dataclass
class MarketAnalysis:
    base: MarketResult
    metric: str  # "cw_d_eps_pct" or "d_mcap_pct"
    tornado: list[TornadoBar]
    envelopes: dict[str, Envelope]  # ticker → company low/high
    industry_low: dict[str, IndustryResult]
    industry_high: dict[str, IndustryResult]
    market_low: MarketResult
    market_high: MarketResult
    long_industry: str | None = None
    short_industry: str | None = None
    notes: list[str] = field(default_factory=list)

    def ranked_companies(self) -> list[CompanyResult]:
        """All companies with a meaningful result, most helped first."""
        cs = [c for c in self.base.companies if (c.dP_pct if c.dP_pct is not None else c.dEPS_pct) is not None]
        return sorted(cs, key=lambda c: c.rank_value, reverse=True)


@dataclass
class MarketRunner:
    shock: MacroShock
    runners: dict[str, Runner | None]  # None for effect: none
    baselines: dict[str, list[dict]]
    inputs: dict

    def drivers(self) -> list[Driver]:
        seen: dict[tuple[str, str], Driver] = {}
        for r in self.runners.values():
            if r is None:
                continue
            for d in r.drivers():
                if d.kind == "exposure":
                    d = Driver("exposure", d.key, d.label, unit=d.unit)  # same key, any industry
                seen.setdefault((d.kind, d.key), d)
        return list(seen.values())

    def run(self, case: dict[Driver, str] | None = None) -> MarketResult:
        out = {}
        for slug, r in self.runners.items():
            if r is None:
                out[slug] = _zero_result(self.baselines[slug], self.inputs)
            else:
                out[slug] = r.run(case)
        return MarketResult(self.shock, self.inputs, out)


def _zero_result(baselines: list[dict], inputs: dict) -> IndustryResult:
    """An industry with `effect: none`: every company unchanged."""
    return IndustryResult(policy=None, inputs=inputs, assumptions={}, companies=[aggregate(b, []) for b in baselines])


def build_market_runner(
    shock_id: str,
    inputs: dict | None = None,
    assumption_ranges: dict[str, tuple[float, float, float]] | None = None,
    components: set[str] | None = None,
    prices_df=None,
    macro: dict | None = None,
    reg: Registry | None = None,
) -> MarketRunner:
    from policyshock.data import fred

    reg = reg or registry()
    shock = reg.macro[shock_id]
    inputs = {**shock.default_inputs(), **(inputs or {})}
    macro = macro if macro is not None else fred.macro_context()
    ranges = {a.key: (a.low, a.base, a.high) for a in shock.all_assumptions()} | (assumption_ranges or {})
    runners: dict[str, Runner | None] = {}
    baselines = {}
    for ind in load_universe().industries:
        baselines[ind.slug] = industry_baselines(ind.slug, prices_df)
        pol = shock.industry_policy(ind.slug)
        if pol is None:
            runners[ind.slug] = None
            continue
        runners[ind.slug] = Runner(
            policy=pol,
            baselines=baselines[ind.slug],
            inputs=inputs,
            assumption_ranges={a.key: ranges[a.key] for a in pol.assumptions},
            exposure_cfg=reg.exposures,
            components=None if components is None else frozenset(components),
            macro=macro,
            exposure_labels={k: d.label for k, d in reg.exposure_defs.items()},
        )
    return MarketRunner(shock, runners, baselines, inputs)


def _mkt_metric(r: MarketResult, metric: str) -> float:
    v = r.totals()[metric]
    return 0.0 if v is None else v


def analyze_market(mr: MarketRunner) -> MarketAnalysis:
    base = mr.run()
    drivers = mr.drivers()
    oat = {d: (mr.run({d: "low"}), mr.run({d: "high"})) for d in drivers}

    metric = "cw_d_eps_pct"
    if all(abs(_mkt_metric(lo, metric) - _mkt_metric(hi, metric)) < 1e-12 for lo, hi in oat.values()):
        if base.totals()["d_mcap_pct"] is not None:
            metric = "d_mcap_pct"
    bars = [TornadoBar(d, _mkt_metric(lo, metric), _mkt_metric(hi, metric), abs(_mkt_metric(hi, metric) - _mkt_metric(lo, metric))) for d, (lo, hi) in oat.items()]
    bars.sort(key=lambda b: b.swing, reverse=True)

    # Per-company envelopes and per-industry ranges, oriented within each industry.
    envelopes: dict[str, Envelope] = {}
    ind_low, ind_high = {}, {}
    for slug, runner in mr.runners.items():
        if runner is None:
            ind_low[slug] = ind_high[slug] = base.industries[slug]
            for c in base.industries[slug].companies:
                envelopes[c.ticker] = Envelope(c, c)
            continue
        for c in base.industries[slug].companies:
            pess, opt = {}, {}
            for d, (lo, hi) in oat.items():
                a, b = _company_metric(lo.industries[slug].company(c.ticker)), _company_metric(hi.industries[slug].company(c.ticker))
                pess[d], opt[d] = ("low", "high") if a <= b else ("high", "low")
            envelopes[c.ticker] = Envelope(runner.run(pess).company(c.ticker), runner.run(opt).company(c.ticker))
        pess, opt = {}, {}
        for d, (lo, hi) in oat.items():
            a = lo.industries[slug].totals()["d_eps_pct"] or 0.0
            b = hi.industries[slug].totals()["d_eps_pct"] or 0.0
            pess[d], opt[d] = ("low", "high") if a <= b else ("high", "low")
        ind_low[slug], ind_high[slug] = runner.run(pess), runner.run(opt)

    # Market range, oriented by the market metric.
    pess, opt = {}, {}
    for d, (lo, hi) in oat.items():
        a, b = _mkt_metric(lo, metric), _mkt_metric(hi, metric)
        pess[d], opt[d] = ("low", "high") if a <= b else ("high", "low")
    an = MarketAnalysis(base, metric, bars, envelopes, ind_low, ind_high, mr.run(pess), mr.run(opt))
    _sector_pair(an)
    return an


def industry_metric(r: IndustryResult) -> float | None:
    """Industry ranking metric: implied Δ market value %, else Δ EPS %."""
    t = r.totals()
    return t["d_mcap_pct"] if t["d_mcap_pct"] is not None else t["d_eps_pct"]


def _sector_pair(an: MarketAnalysis) -> None:
    scored = [(slug, industry_metric(r)) for slug, r in an.base.industries.items()]
    scored = [(s, v) for s, v in scored if v is not None and abs(v) > 1e-6]
    if len(scored) < 2:
        an.notes.append("Fewer than two industries are meaningfully affected, so there is no sector pair.")
        return
    scored.sort(key=lambda x: x[1], reverse=True)
    an.long_industry, an.short_industry = scored[0][0], scored[-1][0]
    if scored[0][1] <= 0:
        an.notes.append("Every affected industry is hurt; the long is the least-hurt sector (a relative-value pair).")
    if scored[-1][1] >= 0:
        an.notes.append("Every affected industry is helped; the short is the least-helped sector (a relative-value pair).")


def simulate_market(shock_id: str, **kw) -> MarketAnalysis:
    return analyze_market(build_market_runner(shock_id, **kw))

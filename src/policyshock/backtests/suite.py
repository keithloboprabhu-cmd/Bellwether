"""Retrospective policy replays for all ten industries, with explicit scoring.

These are current-model historical comparisons, not point-in-time forecasts or
causal estimates. Cohorts are selected by industry and predeclared data rules,
never by whether the observed outcome agrees with the model.
"""

from __future__ import annotations

import calendar
import math
from datetime import date, timedelta
from statistics import mean

import pandas as pd

from policyshock.backtests import steel_232
from policyshock.config import load_universe
from policyshock.data import fred, store
from policyshock.engine.channels import run_channel
from policyshock.engine.model import ChannelOutcome, aggregate
from policyshock.engine.scenarios import prepare_baselines
from policyshock.engine.sensitivity import Runner
from policyshock.policies.loader import registry

TCJA_SOURCE = "https://www.irs.gov/irb/2018-18_IRB"
STEEL_SOURCE = "https://public-inspection.federalregister.gov/2018-05478.pdf"
PELL_SOURCE = "https://fsapartners.ed.gov/knowledge-center/library/electronic-announcements/2023-03-07/operational-implementation-guidance-federal-student-aids-implementation-2023-24-federal-pell-grant-payment-and-disbursement-schedules"
DEFENSE_SOURCE = "https://www.congress.gov/115/crec/2018/12/11/CREC-2018-12-11-pt1-PgS7412.pdf"
FRED_SOURCE = "https://fred.stlouisfed.org/series/DFF"
EPSILON = 1e-9


def score(rows: list[dict]) -> dict:
    """Count strict sign matches; missing/zero predictions are excluded explicitly.

    An observed zero is a miss for a nonzero prediction. Epsilon is numerical
    roundoff only, not a fitted tolerance. MAE retains each case's stated units.
    """
    eligible = [r for r in rows if all(isinstance(r.get(k), (int, float)) and math.isfinite(r[k]) for k in ("predicted", "actual")) and abs(r["predicted"]) > EPSILON]
    n = len(eligible)
    hits = sum(r["predicted"] * r["actual"] > 0 and abs(r["actual"]) > EPSILON for r in eligible)
    return {"n": n, "hits": hits, "accuracy_pct": 100 * hits / n if n else None,
            "mae": mean(abs(r["predicted"] - r["actual"]) for r in eligible) if n else None,
            "no_change_mae": mean(abs(r["actual"]) for r in eligible) if n else None}


def _start(y: dict, years: list[dict]) -> date:
    end = date.fromisoformat(y["period_end"])
    prior = [date.fromisoformat(p["period_end"]) for p in years if 350 <= (end - date.fromisoformat(p["period_end"])).days <= 380]
    if prior:
        return max(prior) + timedelta(days=1)
    return date(end.year - 1, end.month, min(end.day, calendar.monthrange(end.year - 1, end.month)[1])) + timedelta(days=1)


def _window(ticker: str, effective: date, count: int = 1, cutoff: date | None = None) -> tuple[dict, list[dict]]:
    years = sorted(store.company_years(ticker), key=lambda y: y["period_end"])
    pre = [y for y in years if date.fromisoformat(y["period_end"]) < (cutoff or effective)]
    post = [y for y in years if _start(y, years) >= effective][:count]
    if not pre or len(post) != count:
        raise ValueError("Missing complete pre-policy or post-policy annual periods")
    return pre[-1], post


def _finite(it: dict, *keys: str) -> bool:
    return all(isinstance(it.get(k), (float, int)) and math.isfinite(it[k]) for k in keys)


def _row(ticker: str, base: dict, post: list[dict], predicted: float, actual: float, notes: list[str], assumptions: list[dict] | None = None) -> dict:
    return {"ticker": ticker, "name": store.load_baselines()["companies"][ticker]["name"],
            "base_period": base["period_end"], "post_periods": [p["period_end"] for p in post],
            "predicted": predicted, "actual": actual, "error": predicted - actual,
            "direction_ok": predicted * actual > 0 and abs(actual) > EPSILON,
            "filings": [{"period": y["period_end"], "url": y.get("filing_url"), "filed": y.get("source_filed")} for y in [base, *post]],
            "notes": notes, "assumptions": assumptions or []}


def _tax_case(slug: str) -> dict:
    industry = load_universe().industry(slug)
    case = {"id": f"tcja-{slug}", "industry": slug, "industry_name": industry.name,
            "title": "2017 corporate tax cut", "event": "TCJA · 35% → 21% from January 2018",
            "metric": "Effective tax-rate change", "unit": "pp", "sources": [{"label": "IRS · TCJA and fiscal-year timing", "url": TCJA_SOURCE}],
            "context": "Last annual period ending before December 2017 versus the mean of the first two full annual periods beginning in 2018 or later. Enactment periods are excluded. Raw reported effective tax rates are compared with the engine's tax channel; credits, foreign provisions and one-offs remain in the observed result.",
            "cohort_rule": "Every configured non-REIT with positive pretax income, a 0–100% reported base tax rate, complete engine inputs and two full post-policy tax observations. Domestic share uses only the pre-policy tax note; missing splits use a disclosed 100% estimate.",
            "rows": [], "excluded": []}
    for co in industry.companies:
        try:
            if co.kind == "reit":
                raise ValueError("REIT: corporate tax treatment is outside this channel")
            base, post = _window(co.ticker, date(2018, 1, 1), 2, date(2017, 12, 1))
            it = base["items"]
            if not _finite(it, "revenue", "operating_income", "pretax_income", "effective_tax_rate_raw", "diluted_shares") or it["pretax_income"] <= 0 or it["diluted_shares"] <= 0 or not 0 <= it["effective_tax_rate_raw"] <= 1:
                raise ValueError("Missing engine inputs, nonpositive pretax income/shares, or base tax rate outside 0–100%")
            if not all(_finite(p["items"], "effective_tax_rate_raw") for p in post):
                raise ValueError("Missing post-policy tax-rate observation")
            domestic, foreign = it.get("pretax_domestic"), it.get("pretax_foreign")
            assumptions = []
            if _finite(it, "pretax_domestic", "pretax_foreign") and domestic + foreign > 0:
                share = min(1., max(0., domestic / (domestic + foreign)))
            else:
                share = 1.
                assumptions = [{"key": "domestic_income_share", "value": 1., "source": "estimate", "rationale": "No complete pre-policy domestic/foreign pretax split; assume domestic income rather than use a future exposure."}]
            b = store.baseline_row(co.ticker, None, year=base["fiscal_year"])
            b["effective_tax_rate"] = it["effective_tax_rate_raw"]
            delta = run_channel("tax_rate", b, {"d_statutory_rate": -.14, "domestic_income_share": share})
            res = aggregate(b, [ChannelOutcome("TCJA", "tax", "permanent", delta)])
            if abs(res.tax_rate_new - it["effective_tax_rate_raw"]) <= EPSILON:
                raise ValueError("Zero modeled domestic tax-rate change; excluded from directional denominator")
            observed = mean(p["items"]["effective_tax_rate_raw"] for p in post)
            case["rows"].append(_row(co.ticker, base, post, (res.tax_rate_new - it["effective_tax_rate_raw"]) * 100, (observed - it["effective_tax_rate_raw"]) * 100, [f"Pre-policy domestic share: {share:.1%}", "Latest-restated historical facts; no point-in-time filing archive."], assumptions))
        except (ValueError, KeyError) as exc:
            case["excluded"].append({"ticker": co.ticker, "reason": str(exc)})
    return case


def _policy_case(slug: str, policy_id: str, effective: date, inputs: dict, title: str, event: str, context: str, sources: list[dict], metric: str = "Revenue change") -> dict:
    industry, reg = load_universe().industry(slug), registry()
    pol = reg.policy(slug, policy_id)
    case = {"id": policy_id, "industry": slug, "industry_name": industry.name, "title": title, "event": event,
            "metric": metric, "unit": "%", "context": context,
            "cohort_rule": "All configured companies with nonzero modeled exposure and complete annual pre/post data. Zero-exposure names and missing observations are disclosed as exclusions.",
            "sources": sources, "inputs": inputs, "rows": [], "excluded": []}
    for co in industry.companies:
        try:
            if policy_id == "fed_rate_change" and co.kind != "bank":
                raise ValueError("Not a bank: NII channel does not apply")
            if not any(reg.exposures[co.ticker][k].applicable and reg.exposures[co.ticker][k].value != 0 for k in pol.exposure_keys):
                raise ValueError("No nonzero configured exposure to this policy")
            base, post = _window(co.ticker, effective)
            b = store.baseline_row(co.ticker, None, year=base["fiscal_year"])
            if not _finite(b, "revenue", "cost_of_revenue", "operating_income", "pretax_income", "effective_tax_rate", "diluted_shares") or b["revenue"] <= 0 or b["diluted_shares"] <= 0:
                if co.kind != "bank" or not _finite(b, "revenue", "operating_income", "pretax_income", "effective_tax_rate", "diluted_shares") or b["revenue"] <= 0 or b["diluted_shares"] <= 0:
                    raise ValueError("Incomplete annual financial inputs")
            field = "net_interest_income" if policy_id == "fed_rate_change" else "revenue"
            if not _finite(base["items"], field) or not _finite(post[0]["items"], field) or base["items"][field] <= 0:
                raise ValueError(f"Missing or nonpositive baseline {field} / missing observed value")
            runner = Runner(pol, prepare_baselines(pd.DataFrame([b])), inputs,
                            {a.key: (a.low, a.base, a.high) for a in pol.assumptions}, reg.exposures)
            c = runner.run().companies[0]
            predicted = (c.dEBIT if field == "net_interest_income" else c.dR) / base["items"][field] * 100
            if abs(predicted) <= EPSILON:
                raise ValueError("Zero modeled change; excluded from directional denominator")
            actual = (post[0]["items"][field] / base["items"][field] - 1) * 100
            assumptions = [{"key": k, **reg.exposures[co.ticker][k].model_dump()} for k in pol.exposure_keys]
            assumptions += [{"key": a.key, "value": a.base, "source": a.source, "rationale": a.rationale} for a in pol.assumptions]
            case["rows"].append(_row(co.ticker, base, post, predicted, actual,
                ["Current configured exposures applied to old financials: retrospective replay with look-ahead exposure risk.", "Observed growth includes organic demand, acquisitions, pricing and other policies."], assumptions))
        except (ValueError, KeyError) as exc:
            case["excluded"].append({"ticker": co.ticker, "reason": str(exc)})
    return case


def _steel_case() -> dict:
    rows = []
    for r in steel_232.run():
        base, post = store.fiscal_year(r.ticker, 2017), store.fiscal_year(r.ticker, 2018)
        row = _row(r.ticker, base, [post], r.pred_bps / 100, r.actual_bps / 100, [r.note or "Same reported cost definition across periods", "Current steel exposures; demand and contract timing confound observed margins."])
        row.update({"low": r.pred_low_bps / 100, "high": r.pred_high_bps / 100})
        rows.append(row)
    return {"id": "steel-232", "industry": "industrials", "industry_name": load_universe().industry("industrials").name,
            "title": "2018 steel tariffs", "event": "Section 232 · 25% steel tariff · March 2018",
            "metric": "Gross-margin change", "unit": "pp", "context": "FY2017 → FY2018. Uses the existing steel-tariff engine replay with like-for-like cost definitions. Strong demand and partial-year tariff timing confound the observed change.",
            "cohort_rule": "Existing preselected steel benchmark: NUE (producer), CAT and DE (equipment users). Not the full industrial sample.",
            "sources": [{"label": "Federal Register · steel tariff proclamation", "url": STEEL_SOURCE}], "rows": rows,
            "excluded": [{"ticker": t, "reason": "Outside the existing producer/equipment benchmark cohort"} for t in load_universe().industry("industrials").tickers if t not in steel_232.TICKERS]}


def report() -> dict:
    """Return ten industry cases and a reproducible pooled directional hit rate."""
    cases = [_tax_case(s) for s in ["tmt", "consumer_retail", "healthcare", "energy_resources", "transportation_logistics", "real_estate_hospitality"]]
    rates = fred.load_snapshot()
    dff = rates[rates.series_id == "DFF"]
    annual = {y: float(dff[dff.date.dt.year == y].value.mean()) for y in (2021, 2022)}
    if not all(math.isfinite(v) for v in annual.values()):
        raise ValueError("Historical 2021/2022 DFF observations are required for the bank replay")
    rate_bps = (annual[2022] - annual[2021]) * 100
    bank = _policy_case("financial_services", "fed_rate_change", date(2022, 1, 1), {"d_rate_bps": rate_bps},
        "2022 Fed tightening", f"Annual-average DFF {annual[2021]:.3f}% → {annual[2022]:.3f}%",
        "FY2021 → FY2022 bank NII. Shock equals the change in annual-average effective federal funds rates, not the year-end target jump. Current bank sensitivities are scaled linearly; balance-sheet growth and deposit repricing remain confounders.",
        [{"label": "FRED · daily effective federal funds rate", "url": FRED_SOURCE}], "Net interest income change")
    cases += [bank, _steel_case(), _policy_case("public_sector", "defense_budget_increase", date(2018, 10, 1), {"d_budget_pct": (716 / 700 - 1) * 100},
        "FY2019 defense budget expansion", "National-defense budget agreement · $700B → $716B",
        "Last annual period before October 2018 versus the first full annual period starting thereafter. The budget-agreement topline is an allocation proxy, not contractor cash receipts. Fiscal lags, acquisitions and civilian contracts affect observed total revenue.",
        [{"label": "Congressional Record · FY2018/2019 defense toplines", "url": DEFENSE_SOURCE}]),
        _policy_case("education", "pell_grant_change", date(2023, 7, 1), {"pell_change_pct": (7395 / 6895 - 1) * 100},
        "2023–24 Pell Grant increase", "Maximum annual award · $6,895 → $7,395",
        "Last annual period before July 2023 versus the first full annual period beginning thereafter. Uses the maximum-award percentage as the model funding-per-student proxy. Enrollment mix, acquisitions and tuition changes confound total-revenue growth.",
        [{"label": "Federal Student Aid · enacted Pell award increase", "url": PELL_SOURCE}])]
    order = {i.slug: n for n, i in enumerate(load_universe().industries)}
    cases.sort(key=lambda c: order[c["industry"]])
    for case in cases:
        case["summary"] = score(case["rows"])
    pooled = score([r for c in cases for r in c["rows"]])
    # Do not pool magnitudes expressed in different metrics and units.
    pooled.pop("mae"); pooled.pop("no_change_mae")
    per_industry = [c["summary"]["accuracy_pct"] for c in cases if c["summary"]["n"]]
    pooled.update({"industries": len(per_industry), "cases": len(cases), "excluded": sum(len(c["excluded"]) for c in cases),
                   "industry_balanced_pct": mean(per_industry) if per_industry else None})
    return {"summary": pooled, "cases": cases,
            "definition": "Directional accuracy = 100 × same-sign modeled/observed company changes ÷ eligible company comparisons. Every eligible company-case has equal weight; zero observed changes are misses for a nonzero prediction. Missing inputs and zero modeled exposures are listed as exclusions.",
            "limits": "Retrospective current-model replays, not out-of-sample forecast validation or causal policy attribution. Six industry cases share the same TCJA episode; cases and company outcomes are correlated. Current exposures and restated historical statements can introduce look-ahead bias. No overall magnitude percentage is calculated across incompatible metrics.",
            "data_as_of": store.load_baselines()["as_of"]}

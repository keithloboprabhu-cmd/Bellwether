"""Reproducible policy scope, accounting, boundary and provenance audit.

Economic expectations are maintained independently in policy_review.yaml. These
checks establish internal consistency and declared business scope, not causal
forecast accuracy. They use committed data, never mutable live prices.
"""

from __future__ import annotations

from dataclasses import replace
from itertools import product
import math

import yaml

from policyshock.company.exposure_audit import review_rules
from policyshock.config import CONFIG_DIR, load_universe
from policyshock.engine.sensitivity import analyze
from policyshock.engine.simulate import build_runner
from policyshock.macro.aggregate import build_market_runner
from policyshock.policies.loader import registry
from policyshock.policies.coverage import coverage_reviews, economic_effect

FIELDS = ('dR', 'dC', 'dOpex', 'dEBIT', 'dInt', 'dPTI', 'dNI', 'dEPS', 'dEPS_pct', 'dP', 'dP_pct', 'd_mcap', 'd_margin_bps')


def input_cases(policy) -> list[dict]:
    """Defaults, each input endpoint, all endpoint combinations, and legal all-zero."""
    default = policy.default_inputs()
    cases = [default]
    choices = []
    for u in policy.user_inputs:
        ends = ([v for v in (u.min, u.max) if v is not None] if u.type == 'number'
                else u.options if u.type == 'select' else [False, True])
        ends = ends or [u.default]
        choices.append((u.key, ends))
        cases.extend(default | {u.key: v} for v in ends)
    cases.extend(dict(zip([k for k, _ in choices], vs)) for vs in product(*(vs for _, vs in choices)))
    nums = [u for u in policy.user_inputs if u.type == 'number']
    if nums and all((u.min is None or u.min <= 0) and (u.max is None or u.max >= 0) for u in nums):
        cases.append(default | {u.key: 0 for u in nums})
    return list({tuple(sorted(c.items())): c for c in cases}.values())


def check_results(companies, context: str) -> list[str]:
    """Check finite values, accounting, attribution and admissible financial levels."""
    errors = []
    for c in companies:
        prefix = f'{context}/{c.ticker}'
        for field in FIELDS:
            v = getattr(c, field)
            if v is not None and not math.isfinite(v):
                errors.append(f'{prefix}: nonfinite {field}')
        for name, level in [('revenue', c.baseline['revenue'] + c.dR), ('cost of revenue', c.baseline['cost_of_revenue'] + c.dC)]:
            if level < -1e-6:
                errors.append(f'{prefix}: negative projected {name}')
        if not math.isclose(c.dEPS * c.baseline['diluted_shares'], c.dNI, rel_tol=1e-9, abs_tol=1e-7):
            errors.append(f'{prefix}: EPS/share identity')
        if not math.isclose(sum(o.dNI for o in c.outcomes), c.dNI, rel_tol=1e-9, abs_tol=1e-7):
            errors.append(f'{prefix}: NI attribution does not reconcile')
        if c.dP is not None and not math.isclose(sum(o.dP for o in c.outcomes), c.dP, rel_tol=1e-9, abs_tol=1e-7):
            errors.append(f'{prefix}: value attribution does not reconcile')
        if not 0 <= c.tax_rate_new <= 1:
            errors.append(f'{prefix}: tax rate outside 0..1')
    return errors


def has_impact(company) -> bool:
    """Recognize direct valuation effects even when all earnings deltas are zero."""
    return economic_effect(company)


def direction_value(company, metric: str) -> float | None:
    """Read the declared economic direction, including unpriced raw value channels."""
    if metric in ('dValue_pct', 'dValue_pv'):
        return sum(getattr(o.delta, metric) for o in company.outcomes)
    if metric == 'tax_rate_change':
        return company.tax_rate_new - company.tax_rate
    return getattr(company, metric)


def check_coverage_results(companies, decisions: dict, context: str, *, driver_case: bool = False) -> list[str]:
    """Reject missing/extra firms and impacts outside independently declared coverage."""
    errors = []
    tickers = [c.ticker for c in companies]
    if len(tickers) != len(set(tickers)) or set(tickers) != set(decisions):
        errors.append(f'{context}: result roster differs from complete reviewed company roster')
    for c in companies:
        group = decisions.get(c.ticker)
        excluded = group and (group['status'] in ('outside_scope', 'conditional') or (group['status'] == 'unquantified' and not driver_case))
        if excluded and has_impact(c):
            errors.append(f'{context}/{c.ticker}: unexpected effect for {group["status"]} company')
    return errors


def audit_policy(key: str, *, ranges: bool = True) -> dict:
    """Audit one industry's policy against independent business expectations."""
    reg = registry()
    p = reg.policies[key]
    review = yaml.safe_load((CONFIG_DIR / 'policy_review.yaml').read_text())['reviews'].get(key)
    runner = build_runner(p.industry, p.id)
    base = runner.run()
    errors, warnings = [], []
    coverage = coverage_reviews().get(key, {})
    groups = coverage.get('groups', [])
    members = [t for g in groups for t in g['tickers']]
    decisions = {t: g for g in groups for t in g['tickers']}
    if len(members) != len(set(members)) or set(members) != set(runner.tickers):
        errors.append(f'{key}: incomplete/duplicate independent company coverage decisions')
    if any(g.get('status') not in ('included', 'outside_scope', 'conditional', 'unquantified') or not g.get('reason') for g in groups):
        errors.append(f'{key}: missing coverage status or business rationale')
    possible = set()
    cases = input_cases(p)
    for inputs in cases:
        results = replace(runner, inputs=inputs).run()
        errors.extend(check_results(results.companies, f'{key}/{inputs}'))
        errors.extend(check_coverage_results(results.companies, decisions, f'{key}/{inputs}'))
        possible.update(c.ticker for c in results.companies if has_impact(c))
        if inputs and all(isinstance(v, (int, float)) and v == 0 for v in inputs.values()):
            if any(has_impact(c) for c in results.companies):
                errors.append(f'{key}: legal zero shock changes earnings/revenue/value')
    # Every uncertain coefficient/exposure is also checked at both endpoints.
    driver_runs = 0
    for d in runner.drivers():
        for end in ('low', 'high'):
            driver_result = runner.run({d: end})
            errors.extend(check_results(driver_result.companies, f'{key}/{d.key}:{end}'))
            errors.extend(check_coverage_results(driver_result.companies, decisions, f'{key}/{d.key}:{end}', driver_case=True))
            driver_runs += 1
    company_checks = []
    for c in base.companies:
        group = decisions.get(c.ticker, {})
        status = group.get('status')
        if status == 'included':
            if c.ticker not in possible:
                errors.append(f'{key}/{c.ticker}: reviewed in-scope firm has no effect at any tested input')
            expectation = group.get('direction_overrides', {}).get(c.ticker, group.get('default_direction'))
            if not expectation:
                errors.append(f'{key}/{c.ticker}: missing default economic direction')
            else:
                value = direction_value(c, expectation['metric'])
                if c.ticker in group.get('default_zero', []):
                    if has_impact(c):
                        errors.append(f'{key}/{c.ticker}: default should be nonbinding')
                elif value is None or value * expectation['sign'] <= 1e-8:
                    errors.append(f'{key}/{c.ticker}: wrong/missing default {expectation["metric"]} direction; got {value}')
        company_checks.append(dict(ticker=c.ticker, status=status, reason=group.get('reason'),
                                   default_affected=has_impact(c), any_input_affected=c.ticker in possible))
    if not review:
        errors.append(f'{key}: missing independent economic review')
    else:
        for expectation in review['expect']:
            c = base.company(expectation['ticker'])
            value = getattr(c, expectation['metric'])
            if value is None or value * expectation['sign'] <= 1e-8:
                errors.append(f'{key}/{c.ticker}: expected {expectation["metric"]} sign {expectation["sign"]}, got {value}')
        for ticker in review.get('unaffected', []):
            if has_impact(base.company(ticker)):
                errors.append(f'{key}/{ticker}: direct effect outside reviewed policy scope')
    # Zero-policy exceptions require an explicit, independently maintained coverage explanation.
    affected = [c.ticker for c in base.companies if has_impact(c)]
    if not affected and not (review or {}).get('zero_coverage_reason'):
        errors.append(f'{key}: no affected firms and no reviewed coverage explanation')
    if not affected:
        warnings.append(review.get('zero_coverage_reason', 'No modeled effect'))
    scope_count = 0
    for rule in review_rules()[0]:
        if rule['industry'] != p.industry or rule['key'] not in p.exposure_keys:
            continue
        for t in runner.tickers:
            v = reg.exposure(t, rule['key'])
            if t not in rule['allowed'] and v.applicable and any(abs(x) > 1e-12 for x in (v.value, v.low, v.high)):
                errors.append(f'{key}/{t}: {rule["key"]} assigned to unrelated business')
            scope_count += 1
    estimates = 0
    for t in runner.tickers:
        for k in p.exposure_keys:
            v = reg.exposure(t, k)
            if not v.source or (v.is_estimate and not v.rationale):
                errors.append(f'{key}/{t}/{k}: missing provenance')
            estimates += v.is_estimate
    if not p.references:
        errors.append(f'{key}: no policy references')
    if ranges:
        an = analyze(runner)
        for c in base.companies:
            e = an.envelopes[c.ticker]
            metric = 'dP' if all(x.dP is not None for x in (e.low, c, e.high)) else 'dEPS'
            lo, value, hi = (getattr(x, metric) for x in (e.low, c, e.high))
            if not lo - 1e-7 <= value <= hi + 1e-7:
                errors.append(f'{key}/{c.ticker}: scenario range does not bracket base')
    for c in base.companies:
        if c.dEPS_pct is not None and abs(c.dEPS_pct) > 1:
            warnings.append(f'{c.ticker}: >100% earnings change; small/loss baseline or linear approximation needs caution')
        if c.dP_pct is not None and c.dP_pct < -1:
            warnings.append(f'{c.ticker}: implied loss exceeds equity value; constant-multiple approximation outside useful range')
    return dict(policy=key, companies=len(base.companies), input_cases=len(cases), driver_cases=driver_runs,
                affected=affected, neutral=[c.ticker for c in base.companies if not has_impact(c)],
                value_only=bool(affected) and all(abs(c.dNI)<1e-8 for c in base.companies),
                estimate_exposures=estimates, scope_checks=scope_count, references=p.references,
                company_checks=company_checks,
                rationale=(review or {}).get('rationale'), warnings=warnings, errors=errors)


def audit_all(*, ranges: bool = True) -> dict:
    """Audit every industry policy and every macro shock's valid input corners."""
    reg = registry()
    reviews = yaml.safe_load((CONFIG_DIR / 'policy_review.yaml').read_text())['reviews']
    errors = [f'Stale policy review: {k}' for k in set(reviews) - set(reg.policies)]
    errors += [f'Stale company coverage review: {k}' for k in set(coverage_reviews()) - set(reg.policies)]
    policies = [audit_policy(k, ranges=ranges) for k in sorted(reg.policies)]
    macros = []
    for key, shock in sorted(reg.macro.items()):
        runner = build_market_runner(key)
        cases = input_cases(shock)
        failures = []
        for inputs in cases:
            runners = {slug: replace(r, inputs=inputs) if r is not None else None for slug, r in runner.runners.items()}
            result = replace(runner, inputs=inputs, runners=runners).run()
            failures.extend(check_results(result.companies, f'macro/{key}/{inputs}'))
            if {c.ticker for c in result.companies} != set(load_universe().all_tickers) or len(result.companies) != len(load_universe().all_tickers):
                failures.append(f'macro/{key}: missing/duplicate companies in complete market roster')
            for slug, effect in shock.industry_effects.items():
                if effect.effect == 'none' and any(has_impact(c) for c in result.industries[slug].companies):
                    failures.append(f'{key}/{slug}: explicit unaffected industry moved')
            if inputs and all(isinstance(v, (float, int)) and v == 0 for v in inputs.values()) and any(has_impact(c) for c in result.companies):
                failures.append(f'macro/{key}: legal zero shock changes results')
        driver_cases = 0
        for driver in runner.drivers():
            for end in ('low', 'high'):
                result = runner.run({driver: end})
                failures.extend(check_results(result.companies, f'macro/{key}/{driver.key}:{end}'))
                for slug, effect in shock.industry_effects.items():
                    if effect.effect == 'none' and any(has_impact(c) for c in result.industries[slug].companies):
                        failures.append(f'macro/{key}/{driver.key}:{end}/{slug}: unaffected industry moved')
                driver_cases += 1
        macros.append(dict(shock=key, companies=len(load_universe().all_tickers), input_cases=len(cases), driver_cases=driver_cases, errors=failures))
    return dict(policies=policies, macro_shocks=macros, errors=errors + [e for p in policies for e in p['errors']] + [e for m in macros for e in m['errors']])

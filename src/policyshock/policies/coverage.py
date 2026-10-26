"""Explicit company/activity coverage, separate from exposures and calculated results.

These are internal model scope decisions, not legal advice or a guarantee that
unmodeled spillovers are zero. Coverage must be reviewed when a firm is added.
"""

from functools import lru_cache

import yaml

from policyshock.config import CONFIG_DIR


@lru_cache(maxsize=1)
def coverage_reviews() -> dict:
    """Load the complete, independently authored policy/company coverage matrix."""
    return yaml.safe_load((CONFIG_DIR / 'policy_company_coverage.yaml').read_text())['policies']


def company_coverage(policy, ticker: str) -> dict | None:
    """Find an explicit reference-company scope decision; custom firms remain unreviewed."""
    review = coverage_reviews().get(f'{policy.industry}/{policy.id}', {})
    return next((g for g in review.get('groups', []) if ticker in g['tickers']), None)


def economic_effect(company) -> bool:
    """Detect earnings or raw value effects even when a price/valuation is unavailable."""
    return any(abs(getattr(company, f) or 0) > 1e-8 for f in ('dR', 'dNI', 'dP')) or any(
        abs(o.delta.dValue_pct) > 1e-12 or abs(o.delta.dValue_pv) > 1e-8
        for o in company.outcomes
    )


def coverage_result(policy, company, inputs: dict, exposures: dict, *, custom: bool = False) -> dict:
    """Explain an actual zero without confusing business scope, settings and missing data."""
    group = None if custom else company_coverage(policy, company.ticker)
    changed = economic_effect(company)
    if group and group['status'] in ('outside_scope', 'unquantified') and not changed:
        return dict(status=group['status'], reason=group['reason'])
    if changed:
        value_only = abs(company.dNI) < 1e-8 and abs(company.dR) < 1e-8
        return dict(status='value_only' if value_only else 'modeled', reason=(
            'This channel changes modeled equity value, while earnings/EPS stay unchanged.'
            if value_only else (group or {}).get('reason', 'Effect calculated from the supplied company inputs.')
        ))
    if inputs and all(isinstance(v, (int, float)) and v == 0 for v in inputs.values()):
        return dict(status='zero_shock', reason='The selected policy changes are zero; no modeled change is expected.')
    if policy.id == 'minimum_wage_increase' and inputs['new_min'] <= exposures['us_starting_wage'].value:
        return dict(status='nonbinding', reason='The selected wage floor is no higher than this company’s modeled starting wage.')
    if policy.id in ('credit_card_interchange_cap', 'app_store_commission_cap'):
        current = policy.assumption('current_rate_pct' if policy.id == 'credit_card_interchange_cap' else 'current_rate').base
        cap = inputs['cap_pct'] if policy.id == 'credit_card_interchange_cap' else inputs['max_commission_pct'] / 100
        if cap >= current:
            return dict(status='nonbinding', reason='The selected cap is at or above the modeled current fee; it does not bind.')
    if policy.id == 'ninety_ten_rule_change':
        ratios = [exposures[k].value for k in ('ninety_ten_hi_ratio', 'ninety_ten_lo_ratio')]
        if max(ratios) <= inputs['cap_pct'] / 100:
            return dict(status='nonbinding', reason='The modeled federal-aid shares are below the selected cap; no enrollment reduction is required.')
    if group and group['status'] == 'conditional':
        return dict(status='nonbinding', reason=group['reason'])
    if policy.exposure_keys and all(not exposures[k].applicable or (exposures[k].value == exposures[k].high == 0) for k in policy.exposure_keys):
        return dict(status='unquantified', reason='No quantified exposure was supplied for this company. This is a coverage gap, not proof of no economic effect.')
    return dict(status='neutral', reason='The selected settings produce no net modeled change. Inspect channel offsets, exposure estimates and input thresholds.')

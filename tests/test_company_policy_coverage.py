"""Regression checks for business scope, meaningful zeros and sourced bank bases."""

from dataclasses import replace
import importlib.util
import json

import pytest

from policyshock.config import ROOT, load_universe
from policyshock.engine.simulate import build_runner
from policyshock.policies.audit import audit_policy, check_coverage_results
from policyshock.policies.coverage import coverage_reviews
from policyshock.policies.loader import registry
from policyshock.ui.api import calculate


def test_every_company_and_policy_requires_explicit_independent_coverage():
    """New firms cannot silently inherit scope or escape coverage tests."""
    covered = set()
    assert set(coverage_reviews()) == set(registry().policies)
    for key, review in coverage_reviews().items():
        members = [t for group in review['groups'] for t in group['tickers']]
        assert len(members) == len(set(members))
        assert set(members) == set(load_universe().industry(key.split('/')[0]).tickers)
        assert all(group['reason'] for group in review['groups'])
        covered.update(members)
    assert covered == set(load_universe().all_tickers)


def test_audit_detects_missing_impact_at_a_nonrepresentative_bank(monkeypatch):
    """A zero at Ally fails even though representative JPMorgan still moves."""
    runner = build_runner('financial_services', 'fdic_assessment_increase')
    exposures = dict(runner.exposure_cfg)
    exposures['ALLY'] = dict(exposures['ALLY'])
    value = exposures['ALLY']['fdic_assessment_base_musd']
    exposures['ALLY']['fdic_assessment_base_musd'] = value.model_copy(update=dict(value=0., low=0., high=0.))
    broken = replace(runner, exposure_cfg=exposures)
    monkeypatch.setattr('policyshock.policies.audit.build_runner', lambda *args: broken)
    errors = audit_policy('financial_services/fdic_assessment_increase', ranges=False)['errors']
    assert any('ALLY' in e and 'no effect at any tested input' in e for e in errors)


def test_audit_detects_an_out_of_scope_effect_and_an_incomplete_roster():
    """The checker rejects both a false AIG assessment and a missing company."""
    result = build_runner('financial_services', 'fdic_assessment_increase').run()
    review = coverage_reviews()['financial_services/fdic_assessment_increase']
    decisions = {t: g for g in review['groups'] for t in g['tickers']}
    bad = [replace(c, dNI=-1.) if c.ticker == 'AIG' else c for c in result.companies]
    assert any('AIG' in e and 'outside_scope' in e for e in check_coverage_results(bad, decisions, 'corruption'))
    assert any('roster' in e for e in check_coverage_results(bad[:-1], decisions, 'missing'))


def test_fdic_excludes_insurer_premiums_and_explains_why():
    """A bank pays the recurring assessment; AIG is not a depository insurer."""
    result = calculate(dict(industry='financial_services', policy='fdic_assessment_increase'))
    companies = {c['id']: c for c in result['companies']}
    assert companies['COF']['dNI'] < 0
    aig = companies['AIG']
    assert aig['dNI'] == 0 and aig['revenue'] == 0
    assert aig['coverage']['status'] == 'outside_scope'
    assert 'insured bank' in aig['reason'] and 'premiums' in aig['reason']


@pytest.mark.parametrize('industry,policy,inputs,ticker,status', [
    ('financial_services','credit_card_interchange_cap',{'cap_pct':2.5},'JPM','nonbinding'),
    ('consumer_retail','minimum_wage_increase',{'new_min':17},'COST','nonbinding'),
    ('financial_services','fdic_assessment_increase',{'d_rate_bp':0},'JPM','zero_shock'),
    ('financial_services','bank_capital_requirement',{},'JPM','value_only'),
    ('real_estate_hospitality','lihtc_expansion',{},'PLD','unquantified'),
])
def test_coverage_reason_distinguishes_different_zero_results(industry,policy,inputs,ticker,status):
    """A zero EPS never silently conflates scope, missing estimates and value effects."""
    result = calculate(dict(industry=industry,policy=policy,inputs=inputs))
    c = next(c for c in result['companies'] if c['id'] == ticker)
    assert c['coverage']['status'] == status
    assert c['reason']


def test_margin_conversion_does_not_invent_a_sales_change():
    """Fixed-price efficiency/overrun assumptions change profit at constant revenue."""
    runner = build_runner('public_sector','fixed_price_shift')
    result = runner.run()
    for c in result.companies:
        expected = c.baseline['revenue'] * registry().exposure(c.ticker,'govcon_cost_plus_share').value * .2 * -.01
        assert c.dR == 0
        assert c.dEBIT == pytest.approx(expected)
        assert c.dNI < 0


def test_spr_does_not_transfer_upstream_earnings_to_refiners_or_mineral_sales():
    """Constant refining margins and an explicit diesel-cost benefit stay distinct."""
    result = build_runner('energy_resources','spr_release').run()
    for t in ['PSX','VLO','MPC','SLB','HAL']:
        assert result.company(t).dR == result.company(t).dNI == 0
    assert result.company('COP').dR < 0
    assert result.company('FCX').dR == 0 and result.company('FCX').dNI > 0


def test_fdic_reports_are_identified_and_not_revenue_scaled():
    """Reported bank units and parent identities constrain the assessment proxy."""
    spec = importlib.util.spec_from_file_location('fdic_refresh', ROOT/'scripts/refresh_fdic_exposures.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    snapshot = json.loads((ROOT/'data/snapshots/fdic_assessment_bases.json').read_text())
    records = [r for r in snapshot['records'] if r['CERT'] == 4297]
    m = dict(certs=[4297], parent_contains='CAPITAL ONE')
    proxy = module.assessment_proxy(records, m)
    assert proxy['value'] == pytest.approx((records[0]['ASSET']-records[0]['RBCT1J'])/1000)
    assert registry().exposure('COF','fdic_assessment_base_musd').value == pytest.approx(proxy['value'])
    assert proxy['value'] < proxy['reported_assets_musd']
    with pytest.raises(ValueError, match='Unexpected parent'):
        module.assessment_proxy(records, dict(certs=[4297], parent_contains='AIG'))
    with pytest.raises(ValueError, match='Missing/duplicate'):
        module.assessment_proxy([], m)

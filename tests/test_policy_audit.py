"""Guard every policy's boundaries and independent economic business scope."""

import yaml
import pytest

from policyshock.company.exposure_audit import reviewed_exposures
from policyshock.config import CONFIG_DIR
from policyshock.policies.audit import audit_all, audit_policy
from policyshock.policies.loader import registry


@pytest.mark.parametrize('key', sorted(registry().policies))
def test_every_policy_has_consistent_boundaries_and_reviewed_scope(key):
    """Catch wrong firms/signs, missing direct effects, accounting and input failures."""
    result = audit_policy(key, ranges=False)
    assert not result['errors'], '\n'.join(result['errors'])


def test_macro_input_corners_and_zero_shocks():
    """Audit every macro shock, not only the industry dropdown policies."""
    result = audit_all(ranges=False)
    assert not result['errors'], '\n'.join(result['errors'])


def test_economic_review_cannot_silently_omit_new_policies():
    """Require a business/sign decision when a future policy is introduced."""
    reviews = yaml.safe_load((CONFIG_DIR/'policy_review.yaml').read_text())['reviews']
    assert set(reviews) == set(registry().policies)
    assert all(r['rationale'] and (r['expect'] or r.get('zero_coverage_reason')) for r in reviews.values())


def test_universe_regeneration_preserves_reviewed_company_business():
    """Peer expansion cannot reintroduce foreign aid or missing US manufacturing."""
    for industry, ticker in [('tmt','INTC'), ('healthcare','MOH'), ('education','LAUR'), ('transportation_logistics','RIVN')]:
        before = {k: v.model_dump() for k,v in registry().exposures[ticker].items()}
        corrected = reviewed_exposures(industry, ticker, before)
        assert corrected == before
    inherited = {'us_app_store_fee_share':dict(value=.1,low=.05,high=.2,source='estimate',rationale='Bad generic peer')}
    assert reviewed_exposures('tmt','NFLX',inherited)['us_app_store_fee_share']['value'] == 0
    assert reviewed_exposures('tmt','INTC',{})['us_semis_mfg_capex_musd']['value'] > 0


def test_nonbinding_cap_and_unquantified_policy_do_not_force_an_impact():
    """A justified zero is correct; coverage gaps must be explicit in the API."""
    from policyshock.ui.api import calculate
    cap = calculate({'industry':'financial_services','policy':'credit_card_interchange_cap','inputs':{'cap_pct':2.5}})
    assert all(c['dNI'] == 0 and (c['value'] is None or c['value'] == 0) for c in cap['companies'])
    lihtc = calculate({'industry':'real_estate_hospitality','policy':'lihtc_expansion'})
    assert lihtc['coverage_notice']
    assert all(c['dNI'] == 0 for c in lihtc['companies'])


def test_drug_tariff_scope_does_not_disable_broad_device_import_tariffs():
    """A device maker is outside a pharma tariff but still imports goods in macro shocks."""
    from policyshock.engine.simulate import simulate
    from policyshock.macro.aggregate import build_market_runner
    drug = simulate('healthcare','pharma_tariffs').base
    broad = build_market_runner('universal_tariff').run().industries['healthcare']
    for t in ('TMO','ABT','MDT'):
        assert registry().exposure(t,'us_import_share_of_cogs').value > 0
        assert drug.company(t).dNI == 0
        assert broad.company(t).dNI < 0

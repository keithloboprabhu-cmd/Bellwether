"""Quantitative audit admission, scope and rate-only policy regressions."""
import json
import pytest
from policyshock.config import ROOT,load_universe
from policyshock.data import store
from policyshock.engine.simulate import build_runner
from policyshock.policies.loader import registry

NEW_POLICIES=[k for k,p in registry().policies.items() if p.id.startswith('us_corporate_tax_')]


@pytest.mark.parametrize('key',NEW_POLICIES)
def test_rate_only_tax_arithmetic_and_unknown_scope_at_endpoints(key):
    """The proposed rate change taxes the sourced book proxy once; unknown bases stay inactive."""
    p=registry().policies[key]
    for shock in (0,7):
        runner=build_runner(p.industry,p.id,inputs={'d_rate_pts':shock})
        for c in runner.run().companies:
            e=registry().exposure(c.ticker,'audit_us_pretax_income_musd')
            expected=-shock/100*e.value*c.baseline.get('parent_share',1.) if e.applicable else 0.
            assert c.dNI==pytest.approx(expected,abs=1e-7)
            assert c.dR==0 and c.dPTI==0
            assert c.dEPS*c.baseline['diluted_shares']==pytest.approx(c.dNI)


def test_admitted_companies_have_quantified_default_earnings_effect():
    """A candidate cannot count as covered solely through an unquantified exposure."""
    added=json.loads((ROOT/'data/universe_sources/admission_decisions.json').read_text())['added']
    covered=set()
    for p in registry().policies.values():
        covered.update(c.ticker for c in build_runner(p.industry,p.id).run().companies if abs(c.dEPS)>1e-9)
    assert set(added)<=covered


def test_visa_equivalent_shares_and_insurer_claims_are_not_generic_defaults():
    """Do not mix Visa share classes or merchandise costs with insurer loss expense."""
    v=store.baseline_row('V',100.)
    assert v['eps_diluted']==10.2 and v['diluted_shares']==2216.
    for ticker in ('ALL','MET','TRV'):
        b=store.baseline_row(ticker,100.)
        assert b['kind']=='insurer'
        assert 'PolicyholderBenefitsAndClaimsIncurredNet' in b['tags']['cost_of_revenue']
    assert store.baseline_row('EXR',100.)['total_debt']==pytest.approx(13230.651)

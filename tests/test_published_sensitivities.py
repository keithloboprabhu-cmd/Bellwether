"""Match the simulator to manually reviewed published bank shock sensitivities."""
import json
import pytest
from policyshock.config import ROOT
from policyshock.engine.simulate import simulate
from policyshock.policies.loader import registry
from policyshock.engine.sensitivity import Runner

CASES=json.loads((ROOT/'reports/evidence/published_benchmarks.json').read_text())


@pytest.mark.parametrize('case',CASES,ids=[f"{r['ticker']}-{r['inputs']['d_rate_bps']}" for r in CASES])
def test_exact_published_shock_has_correct_direction_and_magnitude(case):
    """Use the disclosure's dollar NII metric and horizon, never stock returns or annual EPS growth."""
    a=simulate('financial_services','fed_rate_change',inputs=case['inputs'])
    c=a.base.company(case['ticker']);value=getattr(c,case['metric']);target=case['benchmark']
    lo,hi=sorted([getattr(a.envelopes[c.ticker].low,case['metric']),getattr(a.envelopes[c.ticker].high,case['metric'])])
    assert value*target>0
    assert abs(value-target)<=abs(target)*.25 or lo<=target<=hi


def test_gradual_disclosure_does_not_get_verified_as_instantaneous():
    """Schwab's gradual 4.1% response cannot silently calibrate the instantaneous scenario."""
    value=registry().exposure('SCHW','nii_sens_up_per_100bp')
    assert value.is_estimate
    records=json.loads((ROOT/'reports/evidence/verified_bank_parameters.json').read_text())
    assert not any(r['company']=='SCHW' for r in records)


def test_capital_one_and_ally_use_their_own_current_table_cells():
    """Discover-era NII and instant-versus-gradual effects replace unrelated peer averages."""
    assert registry().exposure('COF','nii_sens_down_per_100bp').value==pytest.approx(.007)
    a=simulate('financial_services','fed_rate_change',inputs={'d_rate_bps':-100})
    assert a.base.company('ALLY').dR==pytest.approx(22.)
    assert a.base.company('COF').dR/a.base.company('COF').baseline['net_interest_income']==pytest.approx(-.007)

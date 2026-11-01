"""Independently transcribed cost and carrier observations from the November audit."""

import json

import pytest

from policyshock.config import ROOT, load_universe
from policyshock.data import store
from policyshock.data.baseline import build_baseline
from policyshock.engine.simulate import build_runner
from policyshock.macro.aggregate import build_market_runner
from policyshock.policies.loader import registry


def test_partial_cost_tag_requires_explicit_reconciled_opt_in():
    """A valid-looking subcomponent must not silently become the entire cost base."""
    values = {'Revenues': 5442.590, 'CostOfGoodsAndServicesSold': 825.230,
              'GrossProfit': 961.344, 'NetIncomeLoss': 100}
    facts = {'facts': {'us-gaap': {k: {'units': {'USD': [{
        'val': v * 1e6, 'start': '2024-09-30', 'end': '2025-09-28',
        'filed': '2025-11-13', 'form': '10-K', 'accn': 'test'}]}}
        for k, v in values.items()}}}
    assert build_baseline(facts)[0].items['cost_of_revenue'] == 825.230
    corrected = build_baseline(facts, cost_basis='revenue_less_gross_profit')[0]
    assert corrected.items['cost_of_revenue'] == pytest.approx(4481.246)
    assert any('subcomponent' in f for f in corrected.flags)


@pytest.mark.parametrize('year,revenue,cost,gross', [
    (2025, 5442.590, 825.230 + 3656.016, 961.344),
    (2024, 5198.679, 876.817 + 3455.422, 866.440),
    (2023, 4522.550, 771.461 + 3026.060, 725.029),
])
def test_tetra_tech_full_cost_history_reconciles(year, revenue, cost, gross):
    """Every comparative year uses the consolidated statement, not subcontractors alone."""
    company = store.load_baselines()['companies']['TTEK']
    y = next(y for y in company['years'] if y['fiscal_year'] == year)['items']
    assert y['revenue'] == pytest.approx(revenue)
    assert y['cost_of_revenue'] == pytest.approx(cost)
    assert y['revenue'] - y['cost_of_revenue'] == pytest.approx(gross)
    assert load_universe().company('TTEK').cost_basis == 'revenue_less_gross_profit'


@pytest.mark.parametrize('ticker,fees', [
    ('AAL', 1465.339192), ('DAL', 1089.832), ('UAL', 1351.302143), ('LUV', 582.416),
])
def test_baggage_policy_uses_own_observed_carrier_fees(ticker, fees):
    """At a 50% fee reduction and 50% recapture, pretax loss is one-quarter of fees."""
    runner = build_runner('transportation_logistics', 'airline_bag_fee_cap')
    c = runner.run().company(ticker)
    assert c.dR == pytest.approx(-fees * .5)
    assert c.dPTI == pytest.approx(-fees * .25)
    assert sum(registry().exposure(t, 'tl_checked_bag_fee_revenue_share').value *
               store.fiscal_year(t)['items']['revenue'] for t in ['AAL', 'DAL', 'UAL', 'LUV']) < 7439.725895


@pytest.mark.parametrize('ticker,gallons', [('DAL', 4269), ('AAL', 4488), ('UAL', 4663), ('LUV', 2169)])
def test_global_fuel_shock_does_not_use_domestic_carbon_volume(ticker, gallons):
    """Isolate gross physical cost before demand; .42 dollars/barrel is .01/gallon."""
    runner = build_market_runner('oil_supply_shock', inputs={'d_brent_usd': .42},
                                assumption_ranges={'elasticity': (0, 0, 0)})
    c = runner.run().industries['transportation_logistics'].company(ticker)
    assert c.outcomes[0].delta.dOpex == pytest.approx(gallons * .01)
    # A global oil shock must not expand the separately scoped US carbon-tax base.
    assert 'tl_global_fuel_gallons_m' not in registry().policy(
        'transportation_logistics', 'carbon_tax_transport_fuel').exposure_keys


def test_bts_transcription_preserves_original_units_and_quarter_sums():
    """The official workbook is in USD thousands, not millions or billions."""
    source = json.loads((ROOT / 'reports/evidence/bts_baggage_transcription.json').read_text())
    assert source['unit'] == 'USD thousands'
    for year in source['sheets'].values():
        for carrier in year.values():
            assert sum(carrier['quarters']) == pytest.approx(carrier['annual'])

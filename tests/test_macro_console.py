"""Full-market console requests preserve the existing engine and industry contracts."""
import math

import pytest

from policyshock.config import load_universe
from policyshock.data import live
from policyshock.macro.aggregate import build_market_runner
from policyshock.policies.loader import registry
from policyshock.ui.api import calculate, catalog


def test_macro_scope_is_separate_from_real_industries():
    """Adding the selector choice cannot double-count the catalog's actual universe."""
    cat = catalog()
    assert len(cat['industries']) == 10
    assert cat['macro']['id'] == 'macro'
    assert cat['macro']['count'] == cat['company_count']
    assert {p['id'] for p in cat['macro']['policies']} == set(registry().macro)
    assert all(p['industry'] == 'macro' for p in cat['macro']['policies'])


@pytest.mark.parametrize('shock_id', sorted(registry().macro))
def test_every_macro_shock_has_complete_industry_and_company_results(shock_id):
    """All ten existing shocks are usable through the real command API, not UI fixtures."""
    result = calculate(dict(industry='macro', policy=shock_id))
    reference = build_market_runner(shock_id).run()
    assert result['mode'] == 'macro'
    assert {c['id'] for c in result['companies']} == set(load_universe().all_tickers)
    assert {i['id'] for i in result['industries']} == {i.slug for i in load_universe().industries}
    assert result['totals']['d_ni'] == pytest.approx(reference.totals()['d_ni'])
    assert result['totals']['d_eps_pct'] == pytest.approx(reference.totals()['cw_d_eps_pct'])
    assert sum(i['totals']['d_ni'] for i in result['industries']) == pytest.approx(result['totals']['d_ni'])
    assert sum(c['dNI'] for c in result['channels']) == pytest.approx(result['totals']['d_ni'])
    for industry in result['industries']:
        rows = [c for c in result['companies'] if c['baseline']['industry'] == industry['id']]
        assert len(rows) == industry['count']
        assert industry['net_income_projected'] == pytest.approx(industry['net_income_baseline'] + industry['totals']['d_ni'])
        assert industry['reason']
    for company in result['companies']:
        assert math.isfinite(company['dNI']) and company['coverage']['reason']
        assert company['metrics']['price']['projected'] is None or company['metrics']['price']['projected'] >= -1e-9


def test_macro_zero_input_and_invalid_requests():
    """Rate zero remains exactly zero; macro inputs and profiles cannot silently misroute."""
    result = calculate(dict(industry='macro', policy='fed_rate_change', inputs={'d_ff_bps': 0}))
    assert result['totals']['d_ni'] == 0
    assert all(c['dNI'] == c['revenue'] == 0 for c in result['companies'])
    with pytest.raises(ValueError, match='unsupported input'):
        calculate(dict(industry='macro', policy='fed_rate_change', inputs={'d_rate_bps': 100}))
    with pytest.raises(ValueError, match='between'):
        calculate(dict(industry='macro', policy='fed_rate_change', inputs={'d_ff_bps': 301}))
    with pytest.raises(ValueError, match='company profile'):
        calculate(dict(industry='macro', policy='fed_rate_change', company={}))


def test_supplied_live_market_baselines_are_used_without_mutation():
    """Every sector uses its portion of one capture rather than a second snapshot read."""
    original = build_market_runner('fed_rate_change')
    rows = {slug: [dict(b) for b in bs] for slug, bs in original.baselines.items()}
    company = next(b for b in rows['tmt'] if b['ticker'] == 'AAPL')
    company['total_debt'] = 123456.
    runner = build_market_runner('fed_rate_change', baselines=rows)
    result = runner.run()
    c = next(c for c in result.companies if c.ticker == 'AAPL')
    assert c.baseline['total_debt'] == 123456.
    assert rows['tmt'] == runner.baselines['tmt']


def test_macro_uses_exactly_one_live_capture(monkeypatch):
    """The API cannot mix market data captured separately for each industry."""
    capture = live.service.capture()
    calls = []
    monkeypatch.setattr(live.service, 'active', True)
    monkeypatch.setattr(live.service, 'request_driven', False)
    monkeypatch.setattr(live.service, 'capture', lambda: calls.append('capture') or capture)
    result = calculate(dict(industry='macro', policy='fed_rate_change'))
    assert calls == ['capture']
    assert result['captured_at'] == capture['captured_at']

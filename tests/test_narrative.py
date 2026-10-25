"""The template narrative renders for every policy and macro shock with no empty slots."""

import re

import pytest

from policyshock.config import load_universe
from policyshock.engine.simulate import simulate
from policyshock.macro.aggregate import simulate_market
from policyshock.narrative.templates import explain, explain_market
from policyshock.policies.loader import registry

POLICIES = sorted(registry().policies)
SHOCKS = sorted(registry().macro)
# unfilled slots or raw Python values (": None", "nan", "inf"), not English words like "None of these"
BAD = re.compile(r"\{|\}|[:(=] ?None\b|\bNone[%)]|\bnan\b|\binf\b|  ")


def _check(text: str):
    assert BAD.search(text) is None, BAD.search(text)
    words = len(text.split())
    assert 60 <= words <= 230, words


@pytest.mark.parametrize("key", POLICIES)
def test_policy_narrative(key):
    ind, pid = key.split("/")
    _check(explain(simulate(ind, pid), registry()))


@pytest.mark.parametrize("shock_id", SHOCKS)
def test_market_narrative(shock_id):
    names = {i.slug: i.name for i in load_universe().industries}
    _check(explain_market(simulate_market(shock_id), registry(), names))


def test_numbers_come_from_results():
    an = simulate("consumer_retail", "import_tariffs", inputs={"tariff_pct": 30})
    text = explain(an, registry())
    assert "30%" in text
    from policyshock.narrative import formatting as f

    assert f.pct(an.base.totals()["d_eps_pct"], signed=True) in text

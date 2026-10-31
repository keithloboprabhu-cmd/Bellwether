"""Admission safeguards for publisher lists and separately staged expansion evidence."""
import json
from policyshock.config import ROOT


def test_fortune_publisher_ranking_has_exactly_100_unique_positions():
    """Require the requested edition and a complete publisher roster."""
    data = json.loads((ROOT/'data/universe_sources/fortune_100_2026.json').read_text())
    assert data['year'] == 2026
    assert sorted(int(r['rank']) for r in data['rows']) == list(range(1,101))
    assert len(data['profiles']) == 100
    assert not data['failures']


def test_index_proxy_is_not_claimed_as_publisher_verification():
    """An ETF roster cannot silently become certified S&P index membership."""
    data = json.loads((ROOT/'data/universe_sources/sp100_access.json').read_text())
    assert data['full_constituent_list_verified'] is False
    assert len(data['public_top_ten']) == 10


def test_staged_candidates_have_unique_issuer_identities_and_evidence():
    """Unresolved firms retain a reason; fetched firms have their SEC source."""
    rows = json.loads((ROOT/'data/universe_sources/expansion_candidates.json').read_text())['candidates']
    assert len({r['ticker'] for r in rows}) == len(rows)
    assert not {'GOOG','BRK-B'} & {r['ticker'] for r in rows}
    assert all(r.get('reason') for r in rows)
    assert all(r.get('identity_source','').startswith('https://data.sec.gov/') for r in rows if r.get('years'))

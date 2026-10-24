"""SEC EDGAR client (keyless): ticker→CIK map, XBRL company facts, and filing lists.

Every request carries the SEC_USER_AGENT contact string (SEC returns 403 without one)
and passes through an 8 req/s limiter. Raw responses are cached on disk in data/cache/
(git-ignored) so repeated refreshes don't re-download unchanged filings.
"""

from __future__ import annotations

import json
import time
from pathlib import Path

from policyshock.config import ROOT
from policyshock.data.http import DEFAULT_SEC_USER_AGENT, RateLimiter, get_secret, get_with_retry

TICKER_MAP_URL = "https://www.sec.gov/files/company_tickers.json"
FACTS_URL = "https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json"
SUBMISSIONS_URL = "https://data.sec.gov/submissions/CIK{cik:010d}.json"

CACHE_DIR = ROOT / "data" / "cache" / "edgar"
_limiter = RateLimiter(rate=8)


def _headers() -> dict:
    return {"User-Agent": get_secret("SEC_USER_AGENT", DEFAULT_SEC_USER_AGENT), "Accept-Encoding": "gzip, deflate"}


def _cached_json(url: str, cache_file: Path, max_age_s: float) -> dict:
    """Return JSON from disk if fresher than `max_age_s`, else fetch and store it."""
    if cache_file.exists() and time.time() - cache_file.stat().st_mtime < max_age_s:
        return json.loads(cache_file.read_text())
    data = get_with_retry(url, headers=_headers(), limiter=_limiter).json()
    cache_file.parent.mkdir(parents=True, exist_ok=True)
    cache_file.write_text(json.dumps(data))
    return data


def ticker_to_cik(max_age_s: float = 86400) -> dict[str, int]:
    """Map upper-case ticker → integer CIK using SEC's company_tickers.json."""
    raw = _cached_json(TICKER_MAP_URL, CACHE_DIR / "company_tickers.json", max_age_s)
    return {row["ticker"].upper(): int(row["cik_str"]) for row in raw.values()}


def company_facts(cik: int, max_age_s: float = 86400) -> dict:
    """All XBRL facts ever filed by a registrant (companyfacts endpoint)."""
    return _cached_json(FACTS_URL.format(cik=cik), CACHE_DIR / f"facts_{cik:010d}.json", max_age_s)


def submissions(cik: int, max_age_s: float = 86400) -> dict:
    """Filing history for a registrant (used to link each fiscal year to its 10-K)."""
    return _cached_json(SUBMISSIONS_URL.format(cik=cik), CACHE_DIR / f"subs_{cik:010d}.json", max_age_s)


def filing_url(cik: int, accession: str) -> str:
    """EDGAR filing index URL for an accession number like 0000320193-24-000123."""
    return f"https://www.sec.gov/Archives/edgar/data/{cik}/{accession.replace('-', '')}/{accession}-index.htm"


def merged_company_facts(ciks: list[int], max_age_s: float = 86400) -> dict:
    """Company facts for a current CIK plus predecessors, merged tag by tag.

    Used when a company re-registers under a new CIK (e.g. a holding-company
    reorganization), so its 10-K history stays under the old CIK. Duplicate
    facts (same accession, period and value) are dropped. Each fact is tagged with the
    `_cik` it came from so filing links point at the right EDGAR folder.
    """
    merged: dict = {}
    for cik in ciks:
        facts = company_facts(cik, max_age_s)
        if not merged:
            merged = {"cik": facts.get("cik"), "entityName": facts.get("entityName"), "facts": {}}
        for ns, tags in facts.get("facts", {}).items():
            for tag, body in tags.items():
                dst = merged["facts"].setdefault(ns, {}).setdefault(tag, {"units": {}})
                for unit, rows in body.get("units", {}).items():
                    existing = dst["units"].setdefault(unit, [])
                    seen = {(r["accn"], r.get("start"), r["end"], r["val"]) for r in existing}
                    existing.extend(
                        {**r, "_cik": cik} for r in rows if (r["accn"], r.get("start"), r["end"], r["val"]) not in seen
                    )
    return merged

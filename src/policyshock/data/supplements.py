"""Verified, period-specific filing facts omitted by the SEC companyfacts feed."""

from functools import lru_cache
import json

from policyshock.config import SNAPSHOT_DIR


@lru_cache(maxsize=1)
def statement_supplements() -> dict:
    """Read reviewed inline-XBRL facts; absent evidence never supplies a number."""
    path = SNAPSHOT_DIR / "statement_supplements.json"
    return json.loads(path.read_text()) if path.exists() else {}


def supplement_year(facts: dict, year) -> None:
    """Apply only a matching issuer/period and retain each fact's exact source."""
    entry = statement_supplements().get(str(facts.get("cik")), {})
    if entry.get("period_end") != year.period_end:
        return
    for key, record in entry.get("items", {}).items():
        year.items[key] = record["value"]
        year.tags[key] = record["document_location"]
        year.estimates[key] = {"source": "verified SEC filing", "source_url": record["source_url"],
                               "rationale": record["rationale"], "accessed": record["accessed"]}
        if key == "total_debt":
            year.flags = [f for f in year.flags if not f.startswith("total interest-bearing debt unavailable")]
        if key == "cost_of_revenue":
            year.flags = [f for f in year.flags if not f.startswith("cost of revenue not found")]
        year.flags.append(record["rationale"])

"""Reviewed firm/business scope and sourced corrections to broad peer priors.

Used by the expansion generator and the explicit configuration repair script.
Runtime calculations still read ordinary validated exposure YAML files.
"""

from __future__ import annotations

from copy import deepcopy
from functools import lru_cache

import yaml

from policyshock.config import CONFIG_DIR
from policyshock.data import store


@lru_cache(maxsize=1)
def review_rules() -> tuple[list[dict], dict]:
    """Load independent scope rules and company-specific exposure corrections."""
    rules = yaml.safe_load((CONFIG_DIR / "exposure_scope_audit.yaml").read_text())["rules"]
    overrides = yaml.safe_load((CONFIG_DIR / "company_exposure_overrides.yaml").read_text())["companies"]
    return rules, overrides


def reviewed_exposures(industry: str, ticker: str, values: dict) -> dict:
    """Apply reviewed corrections without transferring unrelated peer businesses."""
    rules, overrides = review_rules()
    out = deepcopy(values)
    out.update(deepcopy(overrides.get(ticker, {})))
    for rule in rules:
        key = rule["key"]
        if industry != rule["industry"] or ticker in rule["allowed"] or key not in out:
            continue
        old = out[key]
        if old["value"] == old.get("low", old["value"]) == old.get("high", old["value"]) == 0:
            continue
        out[key] = {"value": 0., "low": 0., "high": 0., "source": "estimate",
                    "source_url": store.fiscal_year(ticker).get("filing_url"),
                    "rationale": "Company-specific scope estimate: " + rule["rationale"] + " This is a model boundary, not a reported zero measurement.",
                    "applicable": True}
    return out

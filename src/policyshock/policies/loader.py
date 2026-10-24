"""Load and validate every YAML config; the app refuses to start if any is invalid.

    config/exposure_definitions.yaml      label/unit/help/bounds for each exposure key
    config/exposures/<industry>.yaml      per-company exposure values with sources
    config/policies/<industry>/<id>.yaml  industry policies
    config/macro/<id>.yaml                Full Market shocks (milestone M4)
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

import yaml
from pydantic import ValidationError

from policyshock.config import CONFIG_DIR, load_universe
from policyshock.policies.schema import ExposureDefinition, ExposureValue, IndustryExposures, Policy


class ConfigError(RuntimeError):
    """Raised with a readable message listing every invalid config file."""


@dataclass
class Registry:
    policies: dict[str, Policy]  # keyed by "<industry>/<id>"
    exposure_defs: dict[str, ExposureDefinition]
    exposures: dict[str, dict[str, ExposureValue]]  # ticker → key → value

    def industry_policies(self, industry: str) -> list[Policy]:
        return sorted(
            (p for p in self.policies.values() if p.industry == industry),
            key=lambda p: (not p.showcase, p.name),
        )

    def policy(self, industry: str, policy_id: str) -> Policy:
        return self.policies[f"{industry}/{policy_id}"]

    def exposure(self, ticker: str, key: str) -> ExposureValue:
        return self.exposures[ticker][key]


def _read(path: Path) -> dict:
    with open(path) as f:
        return yaml.safe_load(f) or {}


def _fmt(path: Path, exc: Exception) -> str:
    rel = path.relative_to(CONFIG_DIR.parent)
    if isinstance(exc, ValidationError):
        lines = [f"  - {'.'.join(str(x) for x in e['loc'])}: {e['msg']}" for e in exc.errors()]
        return f"{rel}:\n" + "\n".join(lines)
    return f"{rel}: {exc}"


def load_registry(config_dir: Path = CONFIG_DIR) -> Registry:
    """Parse every config file, collecting all errors before raising ConfigError."""
    errors: list[str] = []
    universe = load_universe()

    defs: dict[str, ExposureDefinition] = {}
    # One shared file; config/exposure_definitions.d/*.yaml is also read (used while industries
    # are authored in parallel, then merged). A key defined twice must be defined identically.
    def_paths = [config_dir / "exposure_definitions.yaml", *sorted((config_dir / "exposure_definitions.d").glob("*.yaml"))]
    for defs_path in def_paths:
        try:
            for row in _read(defs_path).get("exposures", []):
                d = ExposureDefinition.model_validate(row)
                if d.key in defs and defs[d.key] != d:
                    raise ValueError(f"exposure {d.key!r} defined differently in two files")
                defs[d.key] = d
        except Exception as exc:
            errors.append(_fmt(defs_path, exc))

    exposures: dict[str, dict[str, ExposureValue]] = {}
    for path in sorted((config_dir / "exposures").glob("*.yaml")):
        try:
            ie = IndustryExposures.model_validate(_read(path))
            for ticker, vals in ie.companies.items():
                if ticker not in universe.industry(ie.industry).tickers:
                    raise ValueError(f"{ticker} is not in industry {ie.industry}")
                for key, v in vals.items():
                    if key not in defs:
                        raise ValueError(f"{ticker}.{key}: not in exposure_definitions.yaml")
                    d = defs[key]
                    if (d.min is not None and v.low < d.min) or (d.max is not None and v.high > d.max):
                        raise ValueError(f"{ticker}.{key}: outside [{d.min}, {d.max}]")
                exposures.setdefault(ticker, {}).update(vals)
        except Exception as exc:
            errors.append(_fmt(path, exc))

    policies: dict[str, Policy] = {}
    for path in sorted((config_dir / "policies").glob("*/*.yaml")):
        try:
            pol = Policy.model_validate(_read(path))
            if pol.industry != path.parent.name:
                raise ValueError(f"industry {pol.industry!r} doesn't match folder {path.parent.name!r}")
            ind = universe.industry(pol.industry)
            for key in pol.exposure_keys:
                if key not in defs:
                    raise ValueError(f"exposure key {key!r} not in exposure_definitions.yaml")
                missing = [t for t in ind.tickers if key not in exposures.get(t, {})]
                if missing:
                    raise ValueError(f"exposure {key!r} missing for {missing}")
            for t in pol.roles:
                if t not in ind.tickers:
                    raise ValueError(f"role given for {t}, which is not in {pol.industry}")
            policies[f"{pol.industry}/{pol.id}"] = pol
        except Exception as exc:
            errors.append(_fmt(path, exc))

    if errors:
        raise ConfigError("Invalid configuration:\n" + "\n".join(errors))
    return Registry(policies=policies, exposure_defs=defs, exposures=exposures)


@lru_cache(maxsize=1)
def registry() -> Registry:
    """Cached registry for the app."""
    return load_registry()

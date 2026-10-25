"""Load and validate every YAML config; the app refuses to start if any is invalid.

    config/exposure_definitions.yaml      label/unit/help/bounds for each exposure key
    config/exposures/<industry>.yaml      per-company exposure values with sources
    config/policies/<industry>/<id>.yaml  industry policies
    config/macro/<id>.yaml                Full Market shocks (every industry: channels or effect: none)
Several exposure files may cover the same industry (e.g. macro-specific exposures); a
ticker's key may only be defined once.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

import yaml
from pydantic import ValidationError

from policyshock.config import CONFIG_DIR, load_universe
from policyshock.policies.schema import ExposureDefinition, ExposureValue, IndustryExposures, MacroShock, Policy


class ConfigError(RuntimeError):
    """Raised with a readable message listing every invalid config file."""


@dataclass
class Registry:
    policies: dict[str, Policy]  # keyed by "<industry>/<id>"
    macro: dict[str, MacroShock]  # keyed by shock id
    exposure_defs: dict[str, ExposureDefinition]
    exposures: dict[str, dict[str, ExposureValue]]  # ticker → key → value

    def macro_shocks(self) -> list[MacroShock]:
        return sorted(self.macro.values(), key=lambda m: (not m.showcase, m.name))

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
                dup = set(vals) & set(exposures.get(ticker, {}))
                if dup:
                    raise ValueError(f"{ticker}: exposure keys {sorted(dup)} already defined in another file")
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

    macro: dict[str, MacroShock] = {}
    for path in sorted((config_dir / "macro").glob("*.yaml")):
        try:
            shock = MacroShock.model_validate(_read(path))
            slugs = {i.slug for i in universe.industries}
            missing = slugs - set(shock.industry_effects)
            extra = set(shock.industry_effects) - slugs
            if missing or extra:
                raise ValueError(f"industry_effects must cover every industry exactly (missing {sorted(missing)}, unknown {sorted(extra)})")
            for slug in sorted(slugs):
                pol = shock.industry_policy(slug)  # validates the block's expressions
                if pol is None:
                    continue
                ind = universe.industry(slug)
                for key in pol.exposure_keys:
                    if key not in defs:
                        raise ValueError(f"{slug}: exposure key {key!r} not in exposure definitions")
                    gaps = [t for t in ind.tickers if key not in exposures.get(t, {})]
                    if gaps:
                        raise ValueError(f"{slug}: exposure {key!r} missing for {gaps}")
                for t in pol.roles:
                    if t not in ind.tickers:
                        raise ValueError(f"{slug}: role given for {t}, which is not in that industry")
            macro[shock.id] = shock
        except Exception as exc:
            errors.append(_fmt(path, exc))

    if errors:
        raise ConfigError("Invalid configuration:\n" + "\n".join(errors))
    return Registry(policies=policies, macro=macro, exposure_defs=defs, exposures=exposures)


@lru_cache(maxsize=1)
def registry() -> Registry:
    """Cached registry for the app."""
    return load_registry()

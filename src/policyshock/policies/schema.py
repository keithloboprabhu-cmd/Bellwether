"""Pydantic models for policy, macro-shock, exposure and exposure-definition YAML.

The app validates every config at startup and refuses to run if any is invalid
(see loader.py). Rules enforced here:
- every assumption has units, low ≤ base ≤ high, and a source (or `source: estimate`
  plus a one-line rationale);
- every channel type exists, and every expression only references names the policy
  actually defines (inputs, assumptions, derived values, declared exposure keys).
"""

from __future__ import annotations

import re
from typing import Literal

from pydantic import BaseModel, Field, field_validator, model_validator

from policyshock.engine.expressions import references

ESTIMATE = "estimate"
Role = Literal["importer", "domestic_producer", "neutral"]


class Sourced(BaseModel):
    """Mixin: a value that must cite a source or be an explicit, explained estimate."""

    source: str
    source_url: str | None = None
    rationale: str | None = None

    @model_validator(mode="after")
    def _source_rules(self):
        if not self.source or self.source.strip().upper() == "TODO":
            raise ValueError("source is required (use `source: estimate` + rationale if unsourced)")
        if self.source.strip().lower() == ESTIMATE and not (self.rationale and self.rationale.strip()):
            raise ValueError("`source: estimate` needs a one-line rationale")
        return self

    @property
    def is_estimate(self) -> bool:
        return self.source.strip().lower() == ESTIMATE


class UserInput(BaseModel):
    key: str
    label: str
    unit: str
    type: Literal["number", "select", "toggle"] = "number"
    min: float | None = None
    max: float | None = None
    step: float | None = None
    default: float | str | bool | None = None
    options: list[str] | None = None
    optional: bool = False
    help: str | None = None

    @model_validator(mode="after")
    def _bounds(self):
        if self.type == "number" and not self.optional and self.default is None:
            raise ValueError(f"input {self.key}: default required")
        if self.type == "number" and self.default is not None and self.min is not None and self.max is not None:
            if not self.min <= float(self.default) <= self.max:
                raise ValueError(f"input {self.key}: default outside [min, max]")
        if self.type == "select" and not self.options:
            raise ValueError(f"input {self.key}: select needs options")
        return self


class Assumption(Sourced):
    key: str
    label: str
    unit: str
    low: float
    base: float
    high: float
    help: str | None = None

    @model_validator(mode="after")
    def _ordered(self):
        if not self.low <= self.base <= self.high:
            raise ValueError(f"assumption {self.key}: need low ≤ base ≤ high")
        return self

    @property
    def uncertain(self) -> bool:
        return self.low != self.high


class ChannelSpec(BaseModel):
    type: str
    label: str | None = None
    params: dict[str, float | str] = Field(default_factory=dict)
    roles: list[Role] | None = None  # apply only to companies with these roles
    component: str | None = None  # optional, user-toggleable component (e.g. "second_round")
    persistence: str | None = None  # override the policy's persistence for this channel

    @field_validator("type")
    @classmethod
    def _known_type(cls, v: str) -> str:
        from policyshock.engine.channels import CHANNELS

        if v not in CHANNELS:
            raise ValueError(f"unknown channel type {v!r}; known: {sorted(CHANNELS)}")
        return v

    @model_validator(mode="after")
    def _required_params(self):
        from policyshock.engine.channels import CHANNELS

        missing = set(CHANNELS[self.type].required) - set(self.params)
        if missing:
            raise ValueError(f"channel {self.type}: missing params {sorted(missing)}")
        unknown = set(self.params) - set(CHANNELS[self.type].required) - set(CHANNELS[self.type].optional)
        if unknown:
            raise ValueError(f"channel {self.type}: unknown params {sorted(unknown)}")
        return self


class Narrative(BaseModel):
    what: str | None = None  # overrides sentence 1 (may use {input_key} placeholders)
    extra: str | None = None  # one policy-specific sentence


def parse_persistence(v) -> str:
    """Accept 'permanent', 'one_time', 'years: N' or {years: N}; normalise to a string."""
    if isinstance(v, dict) and "years" in v:
        return f"years:{int(v['years'])}"
    s = str(v).replace(" ", "")
    if s in ("permanent", "one_time") or re.fullmatch(r"years:\d+", s):
        return s
    raise ValueError(f"persistence must be permanent, one_time or 'years: N' (got {v!r})")


class Policy(BaseModel):
    id: str
    industry: str
    name: str
    description: str
    persistence: str = "permanent"
    user_inputs: list[UserInput] = Field(default_factory=list)
    assumptions: list[Assumption] = Field(default_factory=list)
    derived: dict[str, str | float] = Field(default_factory=dict)
    channels: list[ChannelSpec] = Field(min_length=1)
    exposure_keys: list[str] = Field(default_factory=list)
    roles: dict[str, Role] = Field(default_factory=dict)
    default_role: Role = "importer"
    references: list[str] = Field(default_factory=list)
    narrative: Narrative | None = None
    showcase: bool = False

    _persistence_v = field_validator("persistence", mode="before")(classmethod(lambda cls, v: parse_persistence(v)))

    @model_validator(mode="after")
    def _references_resolve(self):
        """Every name used in derived values or channel params must be defined."""
        from policyshock.engine.model import BASELINE_FIELDS
        from policyshock.data.fred import MACRO_KEYS

        defined = {
            "input": {u.key for u in self.user_inputs},
            "assumption": {a.key for a in self.assumptions},
            "exposure": set(self.exposure_keys),
            "derived": set(self.derived),
            "baseline": BASELINE_FIELDS,
            "macro": MACRO_KEYS,
            "role": {"is_importer", "is_domestic_producer", "is_neutral"},
        }
        exprs = list(self.derived.values()) + [p for c in self.channels for p in c.params.values()]
        for e in exprs:
            for ns, key in references(e):
                if key not in defined[ns]:
                    raise ValueError(f"policy {self.id}: {ns}.{key} is not defined (in {e!r})")
        dupes = {k for k in defined["input"] if k in defined["assumption"]}
        if dupes:
            raise ValueError(f"policy {self.id}: keys used as both input and assumption: {dupes}")
        return self

    def assumption(self, key: str) -> Assumption:
        return next(a for a in self.assumptions if a.key == key)

    def default_inputs(self) -> dict:
        return {u.key: u.default for u in self.user_inputs}

    def role_of(self, ticker: str) -> str:
        return self.roles.get(ticker, self.default_role)

    @property
    def components(self) -> list[str]:
        return sorted({c.component for c in self.channels if c.component})


# ----------------------------------------------------------------------------- exposures


class ExposureDefinition(BaseModel):
    key: str
    label: str
    unit: Literal["fraction", "usd_m", "count_m", "number", "per_100bp"]
    help: str
    min: float | None = None
    max: float | None = None


class ExposureValue(Sourced):
    value: float
    low: float | None = None
    high: float | None = None

    @model_validator(mode="after")
    def _range(self):
        self.low = self.value if self.low is None else self.low
        self.high = self.value if self.high is None else self.high
        if not self.low <= self.value <= self.high:
            raise ValueError("exposure needs low ≤ value ≤ high")
        return self


class IndustryExposures(BaseModel):
    industry: str
    companies: dict[str, dict[str, ExposureValue]]

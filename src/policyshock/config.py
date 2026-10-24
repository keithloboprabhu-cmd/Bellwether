"""Project paths and the industry/company universe loaded from config/industries.yaml."""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Literal

import yaml
from pydantic import BaseModel, Field

ROOT = Path(__file__).resolve().parents[2]
CONFIG_DIR = ROOT / "config"
SNAPSHOT_DIR = ROOT / "data" / "snapshots"


class Company(BaseModel):
    ticker: str
    name: str
    kind: Literal["standard", "bank", "reit", "managed_care"] = "standard"
    # Older CIKs whose filings belong to this company (e.g. after a holding-company reorganization).
    predecessor_ciks: list[int] = Field(default_factory=list)
    # "total_costs_less_overhead" when tagged cost of revenue omits big variable costs (see baseline.py).
    cost_basis: Literal["reported", "total_costs_less_overhead"] = "reported"


class Industry(BaseModel):
    slug: str
    name: str
    companies: list[Company] = Field(min_length=1)

    @property
    def tickers(self) -> list[str]:
        return [c.ticker for c in self.companies]


class Universe(BaseModel):
    industries: list[Industry]

    def industry(self, slug: str) -> Industry:
        for ind in self.industries:
            if ind.slug == slug:
                return ind
        raise KeyError(slug)

    def company(self, ticker: str) -> Company:
        for ind in self.industries:
            for c in ind.companies:
                if c.ticker == ticker:
                    return c
        raise KeyError(ticker)

    def industry_of(self, ticker: str) -> Industry:
        for ind in self.industries:
            if ticker in ind.tickers:
                return ind
        raise KeyError(ticker)

    @property
    def all_tickers(self) -> list[str]:
        return [t for ind in self.industries for t in ind.tickers]


@lru_cache(maxsize=1)
def load_universe() -> Universe:
    """Load and validate config/industries.yaml (raises on invalid config)."""
    with open(CONFIG_DIR / "industries.yaml") as f:
        return Universe.model_validate(yaml.safe_load(f))

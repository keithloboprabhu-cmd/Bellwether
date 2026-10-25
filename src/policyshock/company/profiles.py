"""Public-company lookup and validated user-company profiles, using the same engine.

SEC companyfacts provides financial statements, not policy-specific exposures.
Unknown exposures stay empty until the user supplies them or explicitly chooses
labelled peer estimates. Profiles are request-local; no company inputs are published.
"""

from __future__ import annotations

import hashlib
import math
import re
import statistics
from typing import Literal
from urllib.parse import urlsplit

import pandas as pd
from pydantic import BaseModel, ConfigDict, Field, model_validator

from policyshock.config import load_universe
from policyshock.data import edgar, fred, prices, store
from policyshock.data.baseline import build_baseline, shares_outstanding
from policyshock.engine.scenarios import prepare_baselines
from policyshock.engine.sensitivity import Runner, TornadoBar, analyze
from policyshock.policies.loader import registry
from policyshock.policies.schema import ExposureValue


class Financials(BaseModel):
    """USD millions and millions of shares; EPS/price are USD per share, tax a fraction."""

    model_config = ConfigDict(extra="forbid", allow_inf_nan=False, strict=True)
    revenue: float = Field(gt=0, le=1e12)
    cost_of_revenue: float | None = Field(default=None, ge=0, le=1e12)
    operating_income: float = Field(ge=-1e12, le=1e12)
    interest_expense: float = Field(ge=0, le=1e12)
    other_nonoperating_income: float = Field(ge=-1e12, le=1e12)
    pretax_income: float = Field(ge=-1e12, le=1e12)
    effective_tax_rate: float = Field(ge=0, le=1)
    net_income: float = Field(ge=-1e12, le=1e12)
    nci_income: float | None = Field(default=None, ge=-1e12, le=1e12)
    diluted_shares: float = Field(gt=0, le=1e9)
    shares_outstanding: float | None = Field(default=None, gt=0, le=1e9)
    eps_diluted: float | None = Field(default=None, ge=-1e9, le=1e9)
    total_debt: float | None = Field(default=None, ge=0, le=1e12)
    total_assets: float | None = Field(default=None, gt=0, le=1e12)
    net_interest_income: float | None = Field(default=None, ge=-1e12, le=1e12)
    price: float | None = Field(default=None, gt=0, le=1e9)

    @model_validator(mode="after")
    def _identities(self):
        expected = self.operating_income - self.interest_expense + self.other_nonoperating_income
        if abs(self.pretax_income - expected) > max(.01, abs(expected) * .0001):
            raise ValueError("Pretax income must equal operating income − interest expense + other nonoperating income (all in $M).")
        return self


class CompanyProfile(BaseModel):
    """Portable, bounded user profile, with provenance separated from financial values."""

    model_config = ConfigDict(extra="forbid", allow_inf_nan=False, strict=True)
    schema_version: Literal[1] = 1
    name: str = Field(min_length=1, max_length=160)
    ticker: str = Field(default="", max_length=20)
    industry: str = Field(max_length=80)
    kind: Literal["standard", "bank", "reit", "managed_care"] = "standard"
    role: Literal["importer", "domestic_producer", "neutral"] = "neutral"
    financials: Financials
    exposures: dict[str, ExposureValue] = Field(default_factory=dict, max_length=100)
    financial_sources: dict[str, str] = Field(default_factory=dict, max_length=30)
    filing_url: str | None = Field(default=None, max_length=2000)
    fiscal_year: int | None = Field(default=None, ge=1900, le=2200)
    price_date: str | None = Field(default=None, max_length=30)
    warnings: list[str] = Field(default_factory=list, max_length=100)

    @model_validator(mode="after")
    def _valid_sources(self):
        if self.industry not in {i.slug for i in load_universe().industries}:
            raise ValueError("Choose a configured policy industry for this profile.")
        if set(self.exposures) - set(registry().exposure_defs):
            raise ValueError("The profile contains unsupported policy exposure keys.")
        if len(self.exposures) > 100 or any(len(v) > 2500 for v in self.financial_sources.values()):
            raise ValueError("Profile source descriptions are too large.")
        for url in [self.filing_url, *(e.source_url for e in self.exposures.values())]:
            if url and urlsplit(url).scheme not in {"http", "https"}:
                raise ValueError("Source links must use http or https.")
        for exposure in self.exposures.values():
            if not all(math.isfinite(v) for v in (exposure.low, exposure.value, exposure.high)):
                raise ValueError("Exposures must contain finite numeric values.")
        return self


def search_companies(query: str) -> list[dict]:
    """Search actual SEC directory names/tickers locally; never synthesize an issuer."""
    q = query.strip().upper()
    if not 1 <= len(q) <= 80:
        raise ValueError("Enter a ticker or company name using 1–80 characters.")
    rows = [r for r in edgar.company_directory() if q in r["ticker"].upper() or all(word in r["title"].upper() for word in q.split())]
    rows.sort(key=lambda r: (r["ticker"] != q, not r["ticker"].startswith(q), len(r["ticker"]), r["ticker"]))
    return [{"ticker": r["ticker"], "name": r["title"], "cik": r["cik_str"]} for r in rows[:20]]


def lookup_company(ticker: str, industry: str) -> dict:
    """Fetch a supported issuer's annual financials; leave undisclosed exposures unset."""
    ticker = ticker.strip().upper()
    if not re.fullmatch(r"[A-Z0-9][A-Z0-9.\-]{0,19}", ticker):
        raise ValueError("Choose a valid ticker from the SEC company search.")
    load_universe().industry(industry)
    known = store.load_baselines()["companies"].get(ticker)
    if known:
        px = prices.load_snapshot()
        row = store.baseline_row(ticker, px.set_index("ticker")["close"].get(ticker), px.set_index("ticker")["date"].get(ticker))
        year = store.fiscal_year(ticker)
        kind = known["kind"]
    else:
        identity = next((r for r in edgar.company_directory() if r["ticker"] == ticker), None)
        if not identity:
            raise ValueError("This ticker is not in SEC's issuer directory. Search another ticker or enter a manual profile.")
        cik = int(identity["cik_str"])
        facts = edgar.company_facts(cik)
        metadata = edgar.submissions(cik)
        sic = str(metadata.get("sic", ""))
        kind = "bank" if sic.startswith(("602", "603", "609")) else "reit" if sic == "6798" else "managed_care" if sic == "6324" else "standard"
        years = build_baseline(facts, kind)
        if not years:
            raise ValueError("No supported US-GAAP annual 10-K financials were found. Foreign-reporting or private companies can be entered manually.")
        year = years[0].to_dict()
        year["filing_url"] = edgar.filing_url(cik, years[0].source_accn) if years[0].source_accn else None
        row = {**year["items"], "name": facts.get("entityName") or identity["title"], "fiscal_year": year["fiscal_year"], "filing_url": year["filing_url"], "flags": year["flags"]}
        quote = prices.fetch_live([ticker])
        row["price"] = float(quote.iloc[0]["close"]) if len(quote) else None
        row["price_date"] = str(quote.iloc[0]["date"]) if len(quote) else None
        cover = shares_outstanding(facts)
        row["shares_outstanding"] = cover["value"] if cover else None
    fields = {}
    sources = {}
    for key in Financials.model_fields:
        if key == "other_nonoperating_income":
            continue
        value = row.get(key)
        fields[key] = None if value is None or (isinstance(value, float) and not math.isfinite(value)) else float(value)
        if fields[key] is not None:
            sources[key] = ("Price snapshot / public quote" if key == "price" else f"SEC EDGAR: {year.get('tags', {}).get(key, key)}; {year.get('filing_url') or 'filing link unavailable'}")
        else:
            sources[key] = "Unavailable from the API; enter a value or leave optional fields blank."
    # These are accounting derivations, not fabricated financial measurements.
    if all(fields.get(k) is not None for k in ("pretax_income", "operating_income", "interest_expense")):
        fields["other_nonoperating_income"] = fields["pretax_income"] - fields["operating_income"] + (fields.get("interest_expense") or 0)
        sources["other_nonoperating_income"] = "Derived: pretax income − operating income + interest expense."
    else:
        fields["other_nonoperating_income"] = None
    # Some issuer XBRL facts incorrectly label counts expressed in millions as shares.
    # Never guess an unknown issuer's scale: require review against the filing.
    warnings = list(row.get("flags", []))
    shares, eps, ni = fields.get("diluted_shares"), fields.get("eps_diluted"), fields.get("net_income")
    if shares and eps and ni and abs(ni / (eps * shares)) >= 100:
        fields["diluted_shares"] = None
        fields["shares_outstanding"] = None
        warnings.append("Share-count units conflict with reported EPS and net income. Enter diluted shares in millions from the annual filing before modeling.")
    for key, note in year.get("estimates", {}).items():
        sources[key] = "Estimate: " + str(note)
    exposures = {k: v.model_dump() for k, v in registry().exposures.get(ticker, {}).items()} if known and known["industry"] == industry else {}
    return {"schema_version": 1, "name": row["name"], "ticker": ticker, "industry": industry, "kind": kind, "role": "neutral",
            "financials": fields, "financial_sources": sources, "exposures": exposures, "filing_url": row.get("filing_url"),
            "fiscal_year": row.get("fiscal_year"), "price_date": row.get("price_date"),
            "warnings": warnings + (["Policy exposures are not provided by SEC's financial API. Enter the required exposures or explicitly use peer estimates."] if not exposures else [])}


def peer_exposures(industry: str, policy_id: str, revenue: float) -> dict:
    """Offer explicit, reproducible industry priors only on the user's request."""
    if not math.isfinite(revenue) or revenue <= 0:
        raise ValueError("Enter positive revenue in $M before using peer estimates.")
    reg = registry()
    pol = reg.policy(industry, policy_id)
    # Use the original curated reference cohort, not estimates of estimates.
    peers = [c.ticker for c in load_universe().industry(industry).companies if c.subsector is None]
    result = {}
    for key in pol.exposure_keys:
        definition = reg.exposure_defs[key]
        absolute = definition.unit in {"usd_m", "count_m"} or key in {"us_methane_kt_ch4", "us_scope1_co2e_mt", "tl_fuel_co2_mt"}
        samples = []
        for peer in peers:
            e = reg.exposures[peer][key]
            if not e.applicable:
                continue
            scale = revenue / store.fiscal_year(peer)["items"]["revenue"] if absolute else 1
            samples.append((e.low * scale, e.value * scale, e.high * scale))
        if not samples:
            raise ValueError(f"No applicable peer estimate for {definition.label}; enter this exposure yourself.")
        values = [min(x[0] for x in samples), statistics.median(x[1] for x in samples), max(x[2] for x in samples)]
        if definition.min is not None:
            values = [max(definition.min, x) for x in values]
        if definition.max is not None:
            values = [min(definition.max, x) for x in values]
        result[key] = {"low": values[0], "value": values[1], "high": values[2], "source": "estimate", "rationale": f"User-selected reference-cohort prior from {', '.join(peers)}: median base, outer low/high; {'absolute values scaled by annual revenue' if absolute else 'dimensionless values unchanged'}. Not reported by this company."}
    return result


def run_company(profile: CompanyProfile, policy_id: str, inputs: dict):
    """Run a validated user-company profile through the existing range/channel engine."""
    reg = registry()
    policy = reg.policy(profile.industry, policy_id)
    missing = set(policy.exposure_keys) - set(profile.exposures)
    if missing:
        raise ValueError("Enter required policy exposures: " + ", ".join(reg.exposure_defs[k].label for k in sorted(missing)))
    for key in policy.exposure_keys:
        e, d = profile.exposures[key], reg.exposure_defs[key]
        if d.min is not None and e.low < d.min or d.max is not None and e.high > d.max:
            raise ValueError(f"{d.label}: exposure values must be within configured bounds {d.min} to {d.max}.")
    f = profile.financials.model_dump()
    if profile.kind != "bank" and f["cost_of_revenue"] is None:
        raise ValueError("Enter cost of revenue in $M. The API did not provide a usable value.")
    if profile.kind == "bank" and any(c.type == "bank_nii" for c in policy.channels) and f["net_interest_income"] is None:
        raise ValueError("Enter net interest income in $M for the bank rate policy.")
    if any(c.type == "financing_debt" for c in policy.channels) and f["total_debt"] is None:
        raise ValueError("Enter total debt in $M before modeling a debt-financing policy.")
    if any(c.type == "bank_capital" for c in policy.channels) and profile.kind == "bank" and profile.exposures["cet1_ratio_std"].low <= 0:
        raise ValueError("A bank CET1 ratio must be positive, including its low estimate.")
    ticker = "CUSTOM_" + hashlib.sha256((profile.name + profile.ticker).encode()).hexdigest()[:8]
    eps = f["eps_diluted"] if f["eps_diluted"] is not None else f["net_income"] / f["diluted_shares"]
    reference_price = f["price"]
    outstanding = f["shares_outstanding"] or f["diluted_shares"]
    row = {**f, "ticker": ticker, "name": profile.name, "kind": profile.kind, "industry": profile.industry,
           "eps_diluted": eps, "fiscal_year": profile.fiscal_year, "price_date": profile.price_date,
           "filing_url": profile.filing_url, "pe": reference_price / eps if reference_price is not None and eps > 0 else None,
           "shares_outstanding": outstanding, "market_cap": reference_price * outstanding if reference_price is not None else None,
           "contribution_margin": (f["revenue"] - f["cost_of_revenue"]) / f["revenue"] if f["cost_of_revenue"] is not None else None}
    policy = policy.model_copy(update={"roles": {ticker: profile.role}})
    prepared = prepare_baselines(pd.DataFrame([row]))
    prepared[0]["model_flags"] += profile.warnings
    runner = Runner(policy, prepared, inputs, {a.key: (a.low, a.base, a.high) for a in policy.assumptions}, {ticker: profile.exposures},
                    macro=fred.macro_context(), exposure_labels={k: d.label for k, d in reg.exposure_defs.items()})
    analysis = analyze(runner)
    # Company percentages use reported EPS, whereas industry percentages use model NI.
    # Re-evaluate sensitivity on the same company metric shown in the headline.
    if analysis.metric == "d_mcap_pct" and analysis.base.companies[0].dP_pct is not None:
        metric, measure = "d_mcap_pct", lambda c: c.dP_pct
    elif eps > 0:
        metric, measure = "d_eps_pct", lambda c: c.dEPS_pct
    else:
        metric, measure = "d_eps", lambda c: c.dEPS
    bars = []
    for driver in runner.drivers():
        low = measure(runner.run({driver: "low"}).companies[0])
        high = measure(runner.run({driver: "high"}).companies[0])
        bars.append(TornadoBar(driver, low, high, abs(high - low)))
    analysis.metric = metric
    analysis.tornado = sorted(bars, key=lambda b: b.swing, reverse=True)
    return analysis

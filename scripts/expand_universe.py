"""Stage API-backed representative company samples before activating configuration.

Financials and issuer names come from SEC APIs. Policy exposures are separately
generated, explicitly labelled peer estimates; these are not API measurements.
Run with --activate only after staged data passes validation.
"""

from __future__ import annotations

import argparse
import json
import statistics
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import pandas as pd
import yaml

from policyshock.config import ROOT, SNAPSHOT_DIR
from policyshock.data import edgar, prices, store
from policyshock.data.baseline import build_baseline, shares_outstanding
from policyshock.policies.loader import registry

STAGE = ROOT / "data/cache/universe_expansion"
SHARE_UNITS = {
    "MCD": ("millions", "https://www.sec.gov/Archives/edgar/data/63908/000006390826000035/mcd-20251231.htm"),
    "LINC": ("thousands", "https://www.sec.gov/Archives/edgar/data/1286613/000114036126007380/ef20060592_10k.htm"),
}
SHARE_UNIT_SINCE_FILED = {"MCD": "2024-02-22", "LINC": "2026-03-02"}
ADDITIONS = {
    "tmt": "IBM ORCL CRM ADBE INTC AMD QCOM MU AVGO CSCO T CMCSA NFLX DIS",
    "financial_services": "MS SCHW BNY STT USB PNC TFC COF FITB HBAN KEY ALLY MA BLK AIG PRU PGR",
    "consumer_retail": "LOW KR DG DLTR TJX ROST SBUX MCD KO PEP PG CL ULTA BBY",
    "healthcare": "CI CNC MOH JNJ MRK ABBV AMGN GILD HCA THC UHS TMO ABT MDT",
    "industrials": "BA ETN EMR ITW PH CMI PCAR DOV ROK STLD CLF CARR OTIS IR",
    "energy_resources": "EOG OXY DVN SLB HAL WMB PSX VLO MPC DUK SO AEP EXC CEG",
    "transportation_logistics": "F RIVN CHRW JBHT ODFL XPO SAIA CSX NSC UAL AAL LUV UBER LYFT",
    "public_sector": "LMT NOC RTX HII OSK KBR KTOS AVAV BWXT TXT ICFI TTEK MRCY VSEC",
    "real_estate_hospitality": "O EQIX DLR WELL VTR ESS MAA PSA EXR VICI WY HST RLJ PK",
    "education": "UTI PRDO APEI LAUR NRDY LINC SKIL CHGG SCHL KLC BFAM WLY FC SLM",
}
NONBANKS = set("V MA BLK AIG PRU PGR".split())
PAYERS = set("CI CNC MOH".split())
PHARMA = set("JNJ MRK ABBV AMGN GILD".split())
HOSPITALS = set("HCA THC UHS".split())
REITS = set(ADDITIONS["real_estate_hospitality"].split())
GROUPS = {
    "tmt": [("Semiconductors", "INTC AMD QCOM MU AVGO", "NVDA"), ("Enterprise software and services", "IBM ORCL CRM ADBE", "MSFT"), ("Telecom and networking", "CSCO T CMCSA", "VZ"), ("Media and entertainment", "NFLX DIS", "GOOGL META")],
    "financial_services": [("Capital markets and custody", "MS SCHW BNY STT", "GS"), ("Regional and consumer banking", "USB PNC TFC COF FITB HBAN KEY ALLY", "JPM BAC WFC C AXP"), ("Payments, asset management and insurance", "V MA BLK AIG PRU PGR", "JPM BAC WFC GS C AXP")],
    "consumer_retail": [("Home improvement", "LOW", "HD"), ("Groceries and discount retail", "KR DG DLTR", "WMT COST TGT"), ("Apparel and specialty retail", "TJX ROST ULTA BBY", "TGT NKE"), ("Restaurants and consumer staples", "SBUX MCD KO PEP PG CL", "WMT COST NKE")],
    "healthcare": [("Managed care", "CI CNC MOH", "UNH ELV HUM CVS"), ("Pharmaceuticals and biotechnology", "JNJ MRK ABBV AMGN GILD", "PFE LLY"), ("Hospitals", "HCA THC UHS", "UNH CVS"), ("Medical devices and life science tools", "TMO ABT MDT", "PFE LLY")],
    "industrials": [("Steel production", "STLD CLF", "NUE"), ("Aerospace and diversified manufacturing", "BA ETN EMR ITW PH CMI PCAR DOV ROK CARR OTIS IR", "CAT DE GE HON MMM")],
    "energy_resources": [("Oil production and services", "EOG OXY DVN SLB HAL", "XOM CVX COP"), ("Midstream pipelines", "WMB", "XOM CVX COP"), ("Refining", "PSX VLO MPC", "XOM CVX"), ("Utilities and generation", "DUK SO AEP EXC CEG", "NEE")],
    "transportation_logistics": [("Automotive", "F RIVN", "TSLA GM"), ("Freight and logistics", "CHRW JBHT ODFL XPO SAIA", "UPS FDX"), ("Rail", "CSX NSC", "UNP"), ("Passenger aviation", "UAL AAL LUV", "DAL"), ("Mobility platforms", "UBER LYFT", "DAL UPS")],
    "public_sector": [("Defense platforms and equipment", "LMT NOC RTX HII OSK KTOS AVAV BWXT TXT MRCY VSEC", "GD"), ("Government engineering and advisory", "KBR ICFI TTEK", "BAH LDOS SAIC CACI PSN")],
    "real_estate_hospitality": [("Property REITs: housing, storage, digital infrastructure, timber and hospitality", ADDITIONS["real_estate_hospitality"], "PLD AMT SPG")],
    "education": [("Postsecondary and workforce institutions", "UTI PRDO APEI LAUR LINC", "LOPE CVSA STRA"), ("Digital learning and training", "NRDY SKIL CHGG FC", "DUOL COUR"), ("Publishing and childcare", "SCHL KLC BFAM WLY", "LRN DUOL COUR"), ("Student financing", "SLM", "LRN LOPE CVSA STRA DUOL COUR")],
}


def classification(industry: str, ticker: str) -> tuple[str, list[str]]:
    """Return the documented sampling stratum and existing exposure reference pool."""
    for label, tickers, peers in GROUPS[industry]:
        if ticker in tickers.split():
            return label, peers.split()
    raise ValueError(f"No sampling stratum for {ticker}")


def statement_kind(industry: str, ticker: str) -> str:
    """Choose an existing statement template without changing financial definitions."""
    if (industry == "financial_services" and ticker not in NONBANKS) or ticker == "SLM":
        return "bank"
    if ticker in PAYERS:
        return "managed_care"
    if ticker in REITS:
        return "reit"
    return "standard"


def fetch_company(industry: str, ticker: str, identity: dict) -> dict:
    """Fetch actual annual facts and issuer classification; reject unusable baselines."""
    cik = int(identity["cik_str"])
    facts = edgar.company_facts(cik)
    kind = statement_kind(industry, ticker)
    unit = SHARE_UNITS.get(ticker, ("shares", None))[0]
    years = build_baseline(facts, kind, share_scale={"shares": 1, "thousands": 1000, "millions": 1000000}[unit], share_scale_since_filed=SHARE_UNIT_SINCE_FILED.get(ticker))
    if not years:
        raise ValueError("No supported US-GAAP 10-K annual financials")
    latest = years[0]
    required = ["revenue", "net_income", "diluted_shares", "operating_income"]
    missing = [k for k in required if latest.items.get(k) is None]
    if missing or not latest.items.get("diluted_shares", 0) > 0:
        raise ValueError(f"Incomplete latest annual financials: {missing}")
    return {"ticker": ticker, "name": facts.get("entityName") or identity["title"], "entity_name": facts.get("entityName"),
            "cik": cik, "industry": industry, "kind": kind, "shares_outstanding": shares_outstanding(facts),
            "retrieved_at": datetime.now(timezone.utc).isoformat(),
            "years": [{**y.to_dict(), "filing_url": edgar.filing_url(y.source_cik or cik, y.source_accn) if y.source_accn else None} for y in years]}


def exposure_estimates(industry: str, ticker: str, company: dict, reg, original: dict) -> dict:
    """Derive transparent peer priors; never call these issuer-reported measurements."""
    label, peers = classification(industry, ticker)
    keys = set().union(*(reg.exposures[t].keys() for t in peers))
    revenue = company["years"][0]["items"]["revenue"]
    out = {}
    for key in sorted(keys):
        definition = reg.exposure_defs[key]
        scale = definition.unit in ("usd_m", "count_m") or key in {"us_methane_kt_ch4", "us_scope1_co2e_mt", "tl_fuel_co2_mt"}
        sample = []
        for peer in peers:
            if key not in reg.exposures[peer]:
                continue
            value = reg.exposures[peer][key]
            factor = revenue / original[peer]["years"][0]["items"]["revenue"] if scale else 1
            sample.append((value.low * factor, value.value * factor, value.high * factor))
        low = min(v[0] for v in sample)
        base = statistics.median(v[1] for v in sample)
        high = max(v[2] for v in sample)
        # Do not transfer payer, manufacturing, or bank-only channels to unrelated businesses.
        not_applicable = (industry == "financial_services" and ticker in NONBANKS)
        structural_zero = (industry == "healthcare" and ticker not in PAYERS and key in {"medicare_advantage_revenue_share", "medicaid_revenue_share", "aca_exchange_revenue_share", "pbm_retained_rebate_share", "hospital_outpatient_cost_share"})
        structural_zero |= (industry == "healthcare" and ticker not in PHARMA and key == "negotiated_drug_medicare_revenue_share")
        structural_zero |= (industry == "industrials" and ticker not in {"STLD", "CLF"} and key == "ind_domestic_steel_sales_share")
        structural_zero |= ticker == "WMB" and key in {"us_crude_sales_share", "oil_price_sensitivity", "ni_per_usd_bbl_musd", "federal_upstream_revenue_share", "clean_generation_credits_musd", "manufacturing_credits_45x_musd", "us_solar_module_revenue_share", "us_critical_mineral_production_cost_musd"}
        structural_zero |= (industry == "education" and ticker in {"NRDY", "SKIL", "CHGG", "SCHL", "KLC", "BFAM", "WLY", "FC", "SLM"} and key in {"ninety_ten_hi_revenue_share", "ninety_ten_lo_revenue_share", "pell_revenue_share", "grad_plus_dependent_revenue_share", "earnings_test_at_risk_revenue_share"})
        if not_applicable or structural_zero:
            low = base = high = 0.0
        if definition.min is not None:
            low, base, high = (max(definition.min, v) for v in (low, base, high))
        if definition.max is not None:
            low, base, high = (min(definition.max, v) for v in (low, base, high))
        rationale = (f"Explicit modeling prior, not an issuer disclosure. {label}; median base and outer low/high from {'/'.join(peers)} in committed exposure configuration. "
                     + ("Absolute exposure intensity scaled by SEC annual revenue." if scale else "Dimensionless peer prior; review before relying on this company result."))
        if not_applicable:
            rationale = "Not applicable to this non-bank's modeled business. Stored zero is a placeholder, not a reported bank measure; bank-only channels exclude this statement template."
        elif structural_zero:
            rationale = f"Explicit scope estimate: {label} is outside this direct policy channel; indirect effects are not modeled. This is not a reported zero exposure."
        out[key] = {"value": base, "low": low, "high": high, "source": "estimate", "rationale": rationale, "applicable": not not_applicable}
    return out


def main() -> int:
    """Stage real data, then optionally activate validated expanded samples atomically."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--activate", action="store_true")
    args = parser.parse_args()
    STAGE.mkdir(parents=True, exist_ok=True)
    config = yaml.safe_load((ROOT / "config/industries.yaml").read_text())
    raw_map = edgar._cached_json(edgar.TICKER_MAP_URL, edgar.CACHE_DIR / "company_tickers.json", 86400)
    identities = {r["ticker"]: r for r in raw_map.values()}
    baseline = json.loads((SNAPSHOT_DIR / "baselines.json").read_text())
    original = dict(baseline["companies"])
    reg = registry()
    jobs = [(slug, t) for slug, tickers in ADDITIONS.items() for t in tickers.split()]
    missing = [t for _, t in jobs if t not in identities]
    if missing:
        raise ValueError(f"Tickers absent from SEC's current directory: {missing}")
    failures = {}
    with ThreadPoolExecutor(max_workers=3) as pool:
        futures = {pool.submit(fetch_company, slug, t, identities[t]): (slug, t) for slug, t in jobs}
        for future in as_completed(futures):
            slug, ticker = futures[future]
            try:
                company = future.result()
                baseline["companies"][ticker] = company
                (STAGE / f"{ticker}.json").write_text(json.dumps(company, indent=1))
                print(f"{ticker}: {company['years'][0]['period_end']}", flush=True)
            except Exception as exc:
                failures[ticker] = str(exc)
                print(f"{ticker}: FAILED {exc}", flush=True)
    (STAGE / "failures.json").write_text(json.dumps(failures, indent=2))
    if failures:
        print("Staged usable issuers; did not change active samples.", flush=True)
        return 1
    roster = []
    for ind in config["industries"]:
        additions = []
        estimates = {}
        for ticker in ADDITIONS[ind["slug"]].split():
            company = baseline["companies"][ticker]
            label, peers = classification(ind["slug"], ticker)
            additions.append({"ticker": ticker, "name": company["name"], "kind": company["kind"], "subsector": label})
            if ticker in SHARE_UNITS:
                additions[-1].update(reported_share_unit=SHARE_UNITS[ticker][0], share_unit_source=SHARE_UNITS[ticker][1], share_unit_since_filed=SHARE_UNIT_SINCE_FILED[ticker])
            estimates[ticker] = exposure_estimates(ind["slug"], ticker, company, reg, original)
            roster.append({"industry": ind["slug"], "ticker": ticker, "name": company["name"], "subsector": label, "cik": company["cik"], "financial_source": company["years"][0]["filing_url"], "exposure_status": "peer estimate", "reference_peers": peers})
        existing_tickers = {c["ticker"] for c in ind["companies"]}
        for item in ind["companies"]:
            replacement = next((c for c in additions if c["ticker"] == item["ticker"]), None)
            if replacement:
                item.update(replacement)
        ind["companies"].extend(c for c in additions if c["ticker"] not in existing_tickers)
        if not 20 <= len(ind["companies"]) <= 30:
            raise ValueError(f"Invalid sample count for {ind['slug']}")
        (STAGE / f"{ind['slug']}__expanded.yaml").write_text(yaml.safe_dump({"industry": ind["slug"], "companies": estimates}, sort_keys=False))
    baseline["as_of"] = datetime.now(timezone.utc).isoformat()
    (STAGE / "baselines.json").write_text(json.dumps(baseline, indent=1))
    (STAGE / "industries.yaml").write_text(yaml.safe_dump(config, sort_keys=False))
    (STAGE / "coverage.json").write_text(json.dumps(roster, indent=1))
    new_prices = prices.fetch_live([t for _, t in jobs])
    existing = prices.load_snapshot()
    combined = pd.concat([existing, new_prices]).drop_duplicates("ticker", keep="last")
    missing_prices = sorted(set(baseline["companies"]) - set(combined["ticker"]))
    combined.drop(columns="source", errors="ignore").sort_values("ticker").to_csv(STAGE / "prices.csv", index=False)
    print(f"Staged {len(baseline['companies'])} companies. Missing prices: {missing_prices}", flush=True)
    if missing_prices:
        return 1
    if args.activate:
        for path, target in [(STAGE / "industries.yaml", ROOT / "config/industries.yaml"), (STAGE / "baselines.json", SNAPSHOT_DIR / "baselines.json"), (STAGE / "prices.csv", SNAPSHOT_DIR / "prices.csv"), (STAGE / "coverage.json", SNAPSHOT_DIR / "sample_coverage.json")]:
            temporary = target.with_suffix(target.suffix + ".tmp")
            temporary.write_bytes(path.read_bytes())
            temporary.replace(target)
        for path in STAGE.glob("*__expanded.yaml"):
            (ROOT / "config/exposures" / path.name).write_bytes(path.read_bytes())
        meta_path = SNAPSHOT_DIR / "meta.json"
        meta = json.loads(meta_path.read_text())
        meta["baselines"] = {"as_of": baseline["as_of"], "companies": len(baseline["companies"])}
        meta["prices"] = {"as_of": baseline["as_of"], "prices": len(combined), "missing": []}
        meta_path.write_text(json.dumps(meta, indent=1))
        print("Activated expanded samples. Rebuild GDP betas next.", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

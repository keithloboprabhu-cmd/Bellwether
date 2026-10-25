"""Rebuild every committed data snapshot from free public sources.

    python scripts/refresh_data.py            # everything
    python scripts/refresh_data.py --only prices fred

Outputs (data/snapshots/):
    baselines.json  per-company annual financials from SEC EDGAR XBRL (FY2008→latest)
    prices.csv      latest close per ticker (yfinance)
    fred.csv        macro series from FRED (keyless CSV endpoint)
    gdp_betas.json  industry revenue betas to real GDP (derived from the two above)
    meta.json       as-of timestamps for each snapshot

Run daily by .github/workflows/refresh.yml so new 10-Ks, prices and macro data flow
into the app automatically. A failed source leaves its previous snapshot untouched.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import pandas as pd  # noqa: E402

from policyshock.config import SNAPSHOT_DIR, load_universe  # noqa: E402
from policyshock.data import edgar, fred, prices  # noqa: E402
from policyshock.data.baseline import build_baseline, shares_outstanding  # noqa: E402
from policyshock.macro import gdp_beta  # noqa: E402

META_FILE = SNAPSHOT_DIR / "meta.json"


def _atomic_write(path: Path, text: str) -> None:
    """Write via a temp file + rename so readers never see a half-written snapshot."""
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text)
    tmp.replace(path)


def _now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def refresh_baselines(max_age_s: float) -> dict:
    """Fetch company facts for all tickers and write baselines.json. Returns a summary."""
    universe = load_universe()
    cik_map = edgar.ticker_to_cik(max_age_s)
    companies = {}
    for ind in universe.industries:
        for c in ind.companies:
            cik = cik_map[c.ticker]
            facts = edgar.merged_company_facts([cik, *c.predecessor_ciks], max_age_s)
            years = build_baseline(facts, c.kind, cost_basis=c.cost_basis, share_scale={"shares": 1, "thousands": 1000, "millions": 1000000}[c.reported_share_unit], share_scale_since_filed=c.share_unit_since_filed)
            so = shares_outstanding(facts)
            companies[c.ticker] = {
                "ticker": c.ticker,
                "name": c.name,
                "entity_name": facts.get("entityName"),
                "cik": cik,
                "industry": ind.slug,
                "kind": c.kind,
                "shares_outstanding": so,
                "years": [
                    {
                        **y.to_dict(),
                        "filing_url": edgar.filing_url(y.source_cik or cik, y.source_accn) if y.source_accn else None,
                    }
                    for y in years
                ],
            }
            latest = years[0] if years else None
            print(f"  {c.ticker:6} {latest.period_end if latest else '—':10}  {len(years):2d} yrs  {len(latest.flags) if latest else 0} flags")
    out = {"as_of": _now(), "source": "SEC EDGAR XBRL companyfacts", "companies": companies}
    _atomic_write(SNAPSHOT_DIR / "baselines.json", json.dumps(out, indent=1))
    return {"companies": len(companies)}


def refresh_prices() -> dict:
    tickers = load_universe().all_tickers
    live = prices.fetch_live(tickers)
    if live.empty:
        raise RuntimeError("yfinance returned no prices")
    missing = sorted(set(tickers) - set(live["ticker"]))
    df = live.drop(columns="source")
    if prices.SNAPSHOT_FILE.exists() and missing:  # keep old rows for tickers that failed today
        old = pd.read_csv(prices.SNAPSHOT_FILE, dtype={"ticker": str})
        df = pd.concat([df, old[old["ticker"].isin(missing)]])
    df.sort_values("ticker").to_csv(prices.SNAPSHOT_FILE, index=False)
    return {"prices": len(live), "missing": missing}


def refresh_fred() -> dict:
    df = fred.fetch_all()
    df["date"] = df["date"].dt.date
    df.to_csv(fred.SNAPSHOT_FILE, index=False)
    return {"rows": len(df), "latest": {k: v["date"] for k, v in fred.latest_values(fred.load_snapshot()).items()}}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--only", nargs="*", choices=["baselines", "prices", "fred", "gdp_betas"])
    ap.add_argument("--max-age-hours", type=float, default=20, help="reuse cached EDGAR responses younger than this")
    args = ap.parse_args()
    targets = args.only or ["baselines", "prices", "fred", "gdp_betas"]

    SNAPSHOT_DIR.mkdir(parents=True, exist_ok=True)
    meta = json.loads(META_FILE.read_text()) if META_FILE.exists() else {}
    jobs = {
        "baselines": lambda: refresh_baselines(args.max_age_hours * 3600),
        "prices": refresh_prices,
        "fred": refresh_fred,
        "gdp_betas": gdp_beta.write_snapshot,
    }
    failed = []
    for name in targets:
        print(f"[{name}] refreshing…")
        try:
            summary = jobs[name]()
            meta[name] = {"as_of": _now(), **summary}
            print(f"[{name}] ok: {summary}")
        except Exception as exc:  # keep going; the old snapshot stays in place
            failed.append(name)
            print(f"[{name}] FAILED: {exc!r}")
    META_FILE.write_text(json.dumps(meta, indent=1, default=str))
    return 1 if len(failed) == len(targets) else 0


if __name__ == "__main__":
    raise SystemExit(main())

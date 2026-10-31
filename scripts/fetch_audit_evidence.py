"""Save primary SEC inline-XBRL evidence missing from the companyfacts API."""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import gzip
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from policyshock.config import CACHE_DIR, ROOT
from policyshock.data import edgar, store
from policyshock.data.filing import parse_inline
from policyshock.data.http import get_with_retry

TARGETS = "F GM DE PCAR TXT O EQIX DLR ESS MAA EXR ULTA LOPE STRA DUOL COUR PRDO LINC CHGG FC MRCY PGR KR THC UHS NEE XPO SAIA CSX LUV CMCSA MA NKE SCHL".split()


def fetch(ticker: str) -> dict:
    """Fetch an issuer's actual annual document and retain exact fact contexts."""
    company = store.load_baselines()["companies"][ticker]
    latest = company["years"][0]
    recent = edgar.submissions(company["cik"])["filings"]["recent"]
    index = recent["accessionNumber"].index(latest["source_accn"])
    document = recent["primaryDocument"][index]
    url = f'https://www.sec.gov/Archives/edgar/data/{company["cik"]}/{latest["source_accn"].replace("-", "")}/{document}'
    cache = CACHE_DIR / "filings" / (ticker + "-" + latest["source_accn"] + ".html.gz")
    if cache.exists():
        html = gzip.decompress(cache.read_bytes()).decode()
    else:
        html = get_with_retry(url, headers=edgar._headers(), limiter=edgar._limiter, retries=1, timeout=30).text
        cache.parent.mkdir(parents=True, exist_ok=True)
        cache.write_bytes(gzip.compress(html.encode()))
    parsed = parse_inline(html)
    facts = []
    for fact in parsed.facts:
        context = parsed.contexts.get(fact["context"], {})
        if len(context.get("dimensions", {})) <= 1:
            facts.append({**fact, **context})
    return {"ticker": ticker, "period_end": latest["period_end"], "source_url": url,
            "accessed": datetime.now(timezone.utc).date().isoformat(), "facts": facts}


def main() -> None:
    """Download primary evidence with bounded SEC concurrency; record every failure."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tickers", nargs="+", default=TARGETS)
    args = parser.parse_args()
    output = ROOT / "reports/evidence/filings.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    results = json.loads(output.read_text()) if output.exists() else {}

    def one(ticker):
        try:
            return ticker, fetch(ticker)
        except Exception as exc:
            return ticker, {"ticker": ticker, "error": str(exc), "verified": False}

    with ThreadPoolExecutor(max_workers=3) as pool:
        for ticker, result in pool.map(one, args.tickers):
            results[ticker] = result
            print(ticker, result.get("error") or f'{len(result["facts"])} primary facts', flush=True)
            output.write_text(json.dumps(results, indent=1))


if __name__ == "__main__":
    main()

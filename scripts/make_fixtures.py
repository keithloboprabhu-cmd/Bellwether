"""Save trimmed SEC company-facts fixtures (one company per industry) for parser tests.

Only the tags the baseline parser reads are kept, so fixtures stay small while
exercising the real fallback chains:  python scripts/make_fixtures.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from policyshock.config import load_universe  # noqa: E402
from policyshock.data import baseline as b  # noqa: E402
from policyshock.data import edgar  # noqa: E402

FIXTURE_TICKERS = ["AAPL", "JPM", "WMT", "UNH", "NUE", "XOM", "DAL", "BAH", "PLD", "CVSA"]
TAGS = set(
    b.REVENUE_TAGS + b.COST_TAGS + b.OPINC_TAGS + b.INTEREST_TAGS + b.PRETAX_TAGS + b.TAX_TAGS
    + b.NET_INCOME_TAGS + b.EPS_TAGS + b.DILUTED_SHARES_TAGS + b.GROSS_PROFIT_TAGS + b.SGA_TAGS
    + b.RND_TAGS + b.DA_TAGS + b.NII_TAGS + b.ASSETS_TAGS + b.DEBT_TAGS + b.DEBT_NONCURRENT_TAGS
    + b.DEBT_CURRENT_TAGS + b.COSTS_AND_EXPENSES_TAGS + b.CLAIMS_TAGS
    + b.PRETAX_DOMESTIC_TAGS + b.PRETAX_FOREIGN_TAGS
    + ["EntityCommonStockSharesOutstanding"]
)


def main() -> None:
    universe = load_universe()
    cik_map = edgar.ticker_to_cik()
    out_dir = ROOT / "tests" / "fixtures"
    out_dir.mkdir(parents=True, exist_ok=True)
    for t in FIXTURE_TICKERS:
        c = universe.company(t)
        facts = edgar.merged_company_facts([cik_map[t], *c.predecessor_ciks])
        trimmed = {
            "cik": facts.get("cik"),
            "entityName": facts.get("entityName"),
            "facts": {
                ns: {tag: body for tag, body in tags.items() if tag in TAGS}
                for ns, tags in facts["facts"].items()
            },
        }
        path = out_dir / f"companyfacts_{t}.json"
        path.write_text(json.dumps(trimmed, separators=(",", ":")))
        print(f"{t}: {path.stat().st_size / 1e3:.0f} KB")


if __name__ == "__main__":
    main()

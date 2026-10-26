"""Apply reviewed company/scope corrections to canonical exposure YAML in place.

Preserves unrelated exposure blocks and formatting. The expansion generator uses
the same reviewed inputs so regeneration cannot silently undo these corrections.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import yaml

from policyshock.company.exposure_audit import reviewed_exposures
from policyshock.config import CONFIG_DIR


def main() -> None:
    """Replace only corrected existing exposure blocks; refuse misplaced new keys."""
    files = {}
    merged = {}
    owners = {}
    for path in sorted((CONFIG_DIR / "exposures").glob("*.yaml")):
        source = path.read_text()
        doc = yaml.safe_load(source)
        files[path] = (source, doc)
        for ticker, vals in doc["companies"].items():
            slug, current = merged.setdefault(ticker, (doc["industry"], {}))
            current.update(vals)
            for key in vals:
                owners[ticker, key] = path
    count = 0
    for ticker, (industry, before) in merged.items():
        after = reviewed_exposures(industry, ticker, before)
        for key, value in after.items():
            if before.get(key) == value:
                continue
            path = owners.get((ticker, key))
            if path is None:
                raise ValueError(f"Add a canonical exposure location for {ticker}.{key} before applying")
            text, doc = files[path]
            company = re.search(r"(?ms)^  " + re.escape(ticker) + r":\n.*?(?=^  \S|\Z)", text)
            if not company:
                raise ValueError(f"Cannot locate company block {ticker}")
            old = company.group()
            body = yaml.safe_dump({key: value}, sort_keys=False, width=100)
            body = "".join("    " + line if line.strip() else line for line in body.splitlines(True))
            updated, n = re.subn(r"(?ms)^    " + re.escape(key) + r":.*?(?=^    \S|\Z)", lambda _: body, old, count=1)
            if n != 1:
                raise ValueError(f"Cannot locate exposure {ticker}.{key}")
            text = text[:company.start()] + updated + text[company.end():]
            files[path] = text, doc
            count += 1
    for path, (text, _) in files.items():
        if text != path.read_text():
            path.write_text(text)
    print(f"Applied {count} reviewed exposure corrections")


if __name__ == "__main__":
    main()

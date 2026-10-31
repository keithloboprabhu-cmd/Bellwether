"""Archive Fortune's public 2026 ranking and primary company-profile identifiers."""
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date
import json
from pathlib import Path
import re
import sys
import requests

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'data/universe_sources'


def embedded(html: str) -> dict:
    """Read the publisher's public Next.js page data without any account access."""
    found = re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', html, re.S)
    if not found:
        raise ValueError('Publisher page has no public embedded ranking data')
    return json.loads(found.group(1))


def profile(row: dict) -> dict:
    """Archive public company information used to identify traded-equity exclusions."""
    slug = row['slug'].strip('/').split('/')[-1]
    path = OUT / 'fortune_profiles' / (slug + '.json')
    if path.exists():
        return json.loads(path.read_text())
    url = 'https://fortune.com/company/' + slug + '/'
    response = requests.get(url, timeout=35)
    response.raise_for_status()
    company = embedded(response.text)['props']['pageProps']['company']
    result = dict(name=row['name'], rank=row['rank'], source_url=url,
                  accessed='2026-10-31', companyInfo=company.get('companyInfo', {}),
                  companyRankingLists=company.get('companyRankingLists', []))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(result, indent=2) + '\n')
    return result


def main() -> None:
    """Fetch exactly the primary publisher's first 100 rows, with individual failures recorded."""
    OUT.mkdir(exist_ok=True, parents=True)
    path = OUT / 'fortune_2026_embedded.json'
    if not path.exists():
        response = requests.get('https://fortune.com/ranking/fortune500/', timeout=40)
        response.raise_for_status()
        (OUT / 'fortune_2026.html').write_text(response.text)
        path.write_text(json.dumps(embedded(response.text)))
    ranking = json.loads(path.read_text())['props']['pageProps']['franchiseSearch']
    if int(ranking['year']) != 2026:
        raise ValueError('Ranking is not the requested 2026 edition')
    rows = sorted(ranking['items'], key=lambda r: int(r['rank']))[:100]
    result, failures = [], []
    with ThreadPoolExecutor(max_workers=3) as pool:
        jobs = {pool.submit(profile, row): row for row in rows}
        for future in as_completed(jobs):
            row = jobs[future]
            try:
                result.append(future.result())
            except Exception as exc:
                failures.append(dict(name=row['name'], rank=row['rank'], error=str(exc)))
    (OUT / 'fortune_100_2026.json').write_text(json.dumps(dict(
        source_url='https://fortune.com/ranking/fortune500/', accessed='2026-10-31', year=2026,
        rows=rows, profiles=sorted(result, key=lambda r: int(r['rank'])), failures=failures), indent=2) + '\n')
    print(f'{len(rows)} ranking rows; {len(result)} profiles; {len(failures)} profile failures')


if __name__ == '__main__':
    main()

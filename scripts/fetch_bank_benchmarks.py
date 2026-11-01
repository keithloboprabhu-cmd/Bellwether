"""Archive published rate-sensitivity tables for manual calibration review."""
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
from pathlib import Path
import gzip,json,re,sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from policyshock.config import ROOT,CACHE_DIR,load_universe
from policyshock.data import edgar,store
from policyshock.data.http import get_with_retry
from policyshock.policies.loader import registry


class Tables(HTMLParser):
    """Collect nested source tables without interpreting the financial columns."""
    def __init__(self):
        super().__init__(convert_charrefs=True);self.stack=[];self.tables=[]
    def handle_starttag(self,tag,attrs):
        """Track each table and readable cell separators."""
        if tag=='table':self.stack.append([])
        if tag in ('td','th','tr'):
            for b in self.stack:b.append(' | ' if tag!='tr' else '\n')
    def handle_data(self,data):
        """Retain the publisher's row/column values for review."""
        for b in self.stack:b.append(data)
    def handle_endtag(self,tag):
        """Save a finished table with internal whitespace normalized."""
        if tag=='table' and self.stack:
            self.tables.append(' '.join(''.join(self.stack.pop()).split()))


def fetch(ticker: str) -> dict:
    """Fetch the already-cited primary filing and retain potential +/-100bp tables."""
    url=registry().exposure(ticker,'nii_sens_up_per_100bp').source_url
    if not url:
        company=store.load_baselines()['companies'][ticker]
        accession=company['years'][0]['source_accn']
        recent=edgar.submissions(company['cik'])['filings']['recent']
        document=recent['primaryDocument'][recent['accessionNumber'].index(accession)]
        url=f'https://www.sec.gov/Archives/edgar/data/{company["cik"]}/{accession.replace("-","")}/{document}'
    path=CACHE_DIR/'filings'/('benchmark-'+ticker+'.html.gz')
    if path.exists():s=gzip.decompress(path.read_bytes()).decode()
    else:
        s=get_with_retry(url,headers=edgar._headers(),limiter=edgar._limiter,retries=1).text;path.write_bytes(gzip.compress(s.encode()))
    p=Tables();p.feed(s)
    tables=[t for t in p.tables if 80<len(t)<12000 and (re.search(r'100\s*(?:bps|basis)',t,re.I) or ('+100' in t and '-100' in t))]
    return dict(ticker=ticker,source_url=url,accessed='2026-10-31',tables=list(dict.fromkeys(tables)))


def main() -> None:
    """Keep raw evidence distinct from benchmark values approved by a reviewer."""
    tickers=[c.ticker for c in load_universe().industry('financial_services').companies if c.kind=='bank']
    def safe(ticker):
        try:return fetch(ticker)
        except Exception as exc:return dict(ticker=ticker,error=str(exc),tables=[])
    with ThreadPoolExecutor(max_workers=3) as pool:rows=list(pool.map(safe,tickers))
    (ROOT/'reports/evidence/bank_sensitivity_tables.json').write_text(json.dumps(rows,indent=2)+'\n')
    for r in rows:print(r['ticker'],len(r['tables']),'tables')


if __name__=='__main__':main()

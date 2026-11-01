"""Inventory model parameters without confusing a citation with verified calibration."""

from pathlib import Path
import csv
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from policyshock.config import ROOT
from policyshock.data.supplements import statement_supplements
from policyshock.data import store
from policyshock.policies.loader import registry

FIELDS = ["parameter", "company", "value", "low", "high", "source_url", "document_location", "date_accessed", "verified", "verification_basis"]


def main() -> None:
    """Save verified filing facts separately from existing unverified modeling priors."""
    reg = registry()
    rows = []
    for ticker, exposures in reg.exposures.items():
        for key, value in exposures.items():
            rows.append(dict(parameter="exposure." + key, company=ticker, value=value.value, low=value.low,
                high=value.high, source_url=value.source_url or "", document_location=value.source + "; " + (value.rationale or ""),
                date_accessed="", verified="N", verification_basis="Existing value retained; this audit has not independently verified the exact numeric exposure against its source."))
    admissions = ROOT / 'data/universe_sources/admission_decisions.json'
    if admissions.exists():
        for ticker in json.loads(admissions.read_text())['added']:
            company = store.load_baselines()['companies'][ticker]
            year = company['years'][0]
            for key, value in year['items'].items():
                if value is None:
                    continue
                rows.append(dict(parameter='baseline.'+key, company=ticker, value=value, low=value, high=value,
                    source_url=f'https://data.sec.gov/api/xbrl/companyfacts/CIK{company["cik"]:010d}.json',
                    document_location=year['period_end']+' / '+year['tags'].get(key,'documented parser normalization'),
                    date_accessed='2026-10-31', verified='N', verification_basis='Primary-source parser output; normalization flags retained. Not independently hand-reconciled; reviewed exact supplements are separate verified rows.'))
    for key, policy in reg.policies.items():
        for a in policy.assumptions:
            verified = key == "industrials/steel_tariffs" and a.key in ("price_response", "producer_price_response")
            rows.append(dict(parameter=key + ".assumption." + a.key, company="ALL", value=a.base, low=a.low,
                high=a.high, source_url=a.source_url or "", document_location=a.source + "; " + (a.rationale or ""),
                date_accessed="2026-10-31" if verified else "", verified="Y" if verified else "N",
                verification_basis="USITC table 5.2, each annual effect divided by 25%; exact historical price metric, not company EPS." if verified else "UNVERIFIED: citation/estimate is not an independently checked benchmark."))
        for u in policy.user_inputs:
            rows.append(dict(parameter=key + ".input." + u.key, company="USER", value=u.default, low=u.min,
                high=u.max, source_url="; ".join(policy.references), document_location=u.help or u.label,
                date_accessed="", verified="N", verification_basis="Scenario control; legal scope and realistic bounds require per-policy review."))
    for entry in statement_supplements().values():
        for key, value in entry["items"].items():
            rows.append(dict(parameter="baseline." + key, company=entry["ticker"], value=value["value"], low=value["value"], high=value["value"],
                source_url=value["source_url"], document_location=value["document_location"], date_accessed=value["accessed"], verified="Y", verification_basis=value["rationale"]))
        s = entry.get("shares_outstanding")
        if s:
            rows.append(dict(parameter="baseline.shares_outstanding", company=entry["ticker"], value=s["value"], low=s["value"], high=s["value"],
                source_url=s["source_url"], document_location=s["document_location"], date_accessed=s["accessed"], verified="Y", verification_basis="Latest annual cover date; unique share-class contexts summed; millions of shares."))
    for name, value, reason in [("valuation.price_floor", 0, "Audit specification, Phase 1: equity limited-liability floor"),
                                ("valuation.median_years", 3, "Audit specification, Phase 1: three-year median valuation fallback"),
                                ("valuation.depressed_threshold", .6, "Audit specification: current EPS more than 40% below three-year median"),
                                ("audit.eps_review_threshold", .5, "Audit specification: absolute EPS change above 50% triggers review")]:
        rows.append(dict(parameter=name, company="ALL", value=value, low=value, high=value, source_url="",
            document_location=reason + "; user brief dated 2026-10-31", date_accessed="2026-10-31", verified="Y",
            verification_basis="User-specified model control, not an empirical financial calibration."))
    for name, value, source, location, verified in [
        ("tax.post_2017_statutory", .21, "https://www.irs.gov/irb/2018-18_IRB", "Corporate rate 21%; TCJA fiscal-year transition", "Y"),
        ("tax.pre_2018_statutory", .35, "https://www.irs.gov/irb/2018-18_IRB", "Corporate rate 35% before TCJA", "Y"),
        ("tax.prior_normalization_years", 3, "", "Documented audit model convention; preceding fiscal years only", "N"),
        ("tax.ordinary_rate_screen_low", 0, "", "Existing model judgment retained; not a legal rate floor", "N"),
        ("tax.ordinary_rate_screen_high", .40, "", "Existing model judgment retained; not a legal rate ceiling", "N"),
    ]:
        rows.append(dict(parameter=name, company="ALL", value=value, low=value, high=value,
            source_url=source, document_location=location, date_accessed="2026-10-31" if verified == "Y" else "",
            verified=verified, verification_basis="Statutory rule" if verified == "Y" else "UNVERIFIED empirical convention; explicitly documented, not a reported company rate."))
    checked = {}
    for path in [ROOT / 'data/universe_sources/verified_tax_parameters.json', ROOT / 'reports/evidence/verified_bank_parameters.json', ROOT / 'reports/evidence/verified_round2_parameters.json']:
        if path.exists():
            checked.update({(r['parameter'], r['company']): r for r in json.loads(path.read_text())})
    rows = [checked.pop((r['parameter'], r['company']), r) for r in rows]
    rows.extend(checked.values())
    covers = ROOT / 'data/universe_sources/incorporation_cover_verifications.json'
    if covers.exists():
        for r in json.loads(covers.read_text()):
            rows.append(dict(parameter='identity.incorporation', company=r['ticker'], value=r['value'], low='', high='',
                source_url=r['source_url'], document_location=r['document_location'], date_accessed=r['date_accessed'],
                verified='Y', verification_basis='Exact original annual cover; archived raw-document SHA-256 in incorporation_cover_verifications.json.'))
    for ticker, annual in store.load_valuation_adjustments().items():
        for period, record in annual.items():
            value=record['adjusted_eps']
            rows.append(dict(parameter='valuation.adjusted_eps.'+period,company=ticker,value=value,low=value,high=value,
                source_url=record['source_url'],document_location=record['document_location'],date_accessed=record['accessed'],verified='Y',verification_basis=record['rationale']))
    from policyshock.data import fred
    rates=fred.load_snapshot();dff=rates[rates.series_id=='DFF']
    for year in (2017,2018,2019,2020):
        value=float(dff[dff.date.dt.year==year].value.mean())
        rows.append(dict(parameter='backtest.dff_annual_mean.'+str(year),company='ALL',value=value,low=value,high=value,
            source_url='https://fred.stlouisfed.org/series/DFF',document_location=f'Calendar {year}; arithmetic mean of committed daily observations',date_accessed='2026-10-31',verified='Y',verification_basis='Observed annual average, not an instantaneous rate-path shock or causal NII estimate.'))
    for year,value,url in [('2021',6495,'https://fsapartners.ed.gov/knowledge-center/library/dear-colleague-letters/2021-01-22/2021-2022-federal-pell-grant-payment-and-disbursement-schedules'),('2022',6895,'https://fsapartners.ed.gov/sites/default/files/attachments/2022-03/2223RevisedPaymentSchedule.pdf')]:
        rows.append(dict(parameter='backtest.pell_maximum.'+year,company='ALL',value=value,low=value,high=value,source_url=url,
            document_location='Award-year maximum annual Pell Grant, full-time schedule',date_accessed='2026-10-31',verified='Y',verification_basis='Published award maximum; not a company-specific revenue sensitivity.'))
    path = ROOT / "data/sources_registry.csv"
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)
    print(f"{len(rows)} source rows; {sum(r['verified'] == 'Y' for r in rows)} verified exact facts/rules")


if __name__ == "__main__":
    main()

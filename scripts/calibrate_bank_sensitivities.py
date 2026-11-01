"""Replace reviewed peer NII priors with the bank's own exact published shock table."""
import json
from pathlib import Path
import sys
import yaml
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from policyshock.config import ROOT,CONFIG_DIR
from policyshock.data import store
from policyshock.policies.loader import registry

# Signed percentage changes under the indicated instantaneous shock. USD-only
# components are used where separately disclosed. No ramp is treated as instant.
REVIEWED={
 'MS':dict(up=209,down=-244,unit='usd_m',shock=100,location='2025 Form 10-K, Wealth Management Net Interest Income Sensitivity Analysis (quantified WM component only), December 2025 sensitivity table; +100 +$209M / -100 -$244M'),
 'STT':dict(up=82,down=-84,unit='usd_m',shock=100,location='2025 Form 10-K Table 33; U.S. Dollar column, +100 +$82M / -100 -$84M; excludes other-currency sensitivities'),
 'COF':dict(up=.006,down=-.007,unit='fraction',shock=100,location='2025 Form 10-K Table 32; estimated impact on projected baseline NII, +100 0.6% / -100 -0.7%; not the EVE table'),
 'ALLY':dict(up=-106,down=22,unit='usd_m',shock=100,location='2025 Form 10-K Market Risk, NII sensitivity table; Instantaneous 2025 column, +100 -$106M / -100 +$22M; gradual scenarios excluded'),
 'PNC':dict(up=.020,down=-.029,unit='fraction',shock=200,location='2025 Form 10-K Table 33; instantaneous +/-200bp NII 2.0% / -2.9%; footnote (a) explicitly states 100bp is approximately half'),
 'TFC':dict(up=-.001,down=-.002,unit='fraction',shock=50,location='2025 Form 10-K Table 30; instantaneous +/-50bp NII -0.1% / -0.2%; 200bp gradual rows excluded; linear interpolation beyond 50bp unverified'),
}


def main() -> None:
    """Apply only reviewed table cells; preserve unresolved benchmarks and historical uncertainty."""
    tables={r['ticker']:r for r in json.loads((ROOT/'reports/evidence/bank_sensitivity_tables.json').read_text())}
    reg=registry(); changes=[]; records=[]
    previous_path=ROOT/'reports/evidence/bank_parameter_changes.json'
    previous={(r['ticker'],r['parameter']):r for r in json.loads(previous_path.read_text())} if previous_path.exists() else {}
    for ticker,bench in REVIEWED.items():
        nii=store.baseline_row(ticker,None)['net_interest_income']
        for direction in ['up','down']:
            key='nii_sens_'+direction+'_per_100bp';old=reg.exposure(ticker,key)
            value=bench[direction]*(100/bench['shock'])*(1 if direction=='up' else -1)
            if bench['unit']=='usd_m':value/=nii
            # Keep uncertainty explicitly honest: exact source point replaces the
            # prior range at this shock, not a fabricated confidence interval.
            row=dict(value=value,low=value,high=value,source='verified bank annual NII sensitivity',source_url=tables[ticker]['source_url'],rationale=bench['location']+'. Accessed 2026-10-31. Divided by reported annual NII only when source is dollars. Point calibration does not validate long-run persistence or other shock sizes.')
            for file in (CONFIG_DIR/'exposures').glob('*.yaml'):
                doc=yaml.safe_load(file.read_text())
                if ticker in doc.get('companies',{}) and key in doc['companies'][ticker]:
                    doc['companies'][ticker][key]=row;file.write_text(yaml.safe_dump(doc,sort_keys=False,width=105))
            override=CONFIG_DIR/'company_exposure_overrides.yaml';doc=yaml.safe_load(override.read_text());doc['companies'].setdefault(ticker,{})[key]=row;override.write_text(yaml.safe_dump(doc,sort_keys=False,width=105))
            changes.append(dict(policy='financial_services/fed_rate_change',ticker=ticker,parameter=key,before=previous.get((ticker,key),{}).get('before',old.value),after=value,source_url=tables[ticker]['source_url'],location=bench['location']))
            records.append(dict(parameter='exposure.'+key,company=ticker,value=value,low=value,high=value,source_url=tables[ticker]['source_url'],document_location=bench['location'],date_accessed='2026-10-31',verified='Y',verification_basis='Manually reviewed published shock table; coefficient mechanically converted to engine fraction per 100bp. No claim of a confidence interval or permanent forecast.'))
    coverage=CONFIG_DIR/'policy_company_coverage.yaml';doc=yaml.safe_load(coverage.read_text());groups=doc['policies']['financial_services/fed_rate_change']['groups']
    for g in groups:
        if 'ALLY' in g['tickers']:
            g.setdefault('direction_overrides',{})['ALLY']=dict(metric='dNI',sign=1)
            note='Ally benefits from a 100bp instantaneous cut under its own current sensitivity table.'
            if note not in g['reason']:
                g['reason']+=' '+note
    coverage.write_text(yaml.safe_dump(doc,sort_keys=False,width=105))
    (ROOT/'reports/evidence/bank_parameter_changes.json').write_text(json.dumps(changes,indent=2)+'\n')
    (ROOT/'reports/evidence/verified_bank_parameters.json').write_text(json.dumps(records,indent=2)+'\n')
    benchmarks=[]
    for ticker,b in REVIEWED.items():
        for direction in ['up','down']:
            benchmarks.append(dict(policy='financial_services/fed_rate_change',ticker=ticker,inputs={'d_rate_bps':b['shock']*(1 if direction=='up' else -1)},metric='dR',benchmark=b[direction] if b['unit']=='usd_m' else b[direction]*store.baseline_row(ticker,None)['net_interest_income'],unit='USD millions NII',source_url=tables[ticker]['source_url'],document_location=b['location'],publication_basis='Forecast NII sensitivity, not realized causal outcome; exact published shock size'))
    # Unchanged original banks are independently checked against current source cells.
    for ticker,up,down in [('JPM',2100,-2400),('BAC',700,-2000),('WFC',1900,-2300),('GS',154,-273),('AXP',19,-11),('C',-33,None)]:
        for shock,value in [(100,up),(-100,down)]:
            if value is not None:benchmarks.append(dict(policy='financial_services/fed_rate_change',ticker=ticker,inputs={'d_rate_bps':shock},metric='dR',benchmark=value,unit='USD millions NII',source_url=tables[ticker]['source_url'],document_location='2025 Form 10-K current instantaneous sensitivity table, U.S. dollar component where separately disclosed; AXP Table 22 current assumptions',publication_basis='Own disclosed 12-month NII sensitivity'))
    (ROOT/'reports/evidence/published_benchmarks.json').write_text(json.dumps(benchmarks,indent=2)+'\n')
    print(f'{len(changes)} sourced coefficient replacements; {len(benchmarks)} exact-shock benchmark comparisons')


if __name__=='__main__':main()

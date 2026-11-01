"""Build the final audit inventory and like-for-like backtest comparison from artifacts.

Missing empirical verification is a failed audit requirement, even when software
tests pass. Publisher membership and fund holdings are deliberately kept separate.
"""
from collections import Counter
import csv
import json
from pathlib import Path
from statistics import mean
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from policyshock.config import ROOT


def read(name: str):
    """Read an audit JSON artifact relative to the repository root."""
    return json.loads((ROOT / name).read_text())


def fmt(value) -> str:
    """Format an observed metric without presenting unavailable values as zero."""
    return '—' if value is None else f'{value:.3f}'


def main() -> None:
    """Save the review summary, coverage decisions and common-cohort comparison."""
    ledger = read('data/universe_sources/admission_decisions.json')
    active = set(read('data/snapshots/baselines.json')['companies'])
    coverage = read('reports/coverage_summary.json')
    before = read('reports/backtests_before.json')
    after = read('reports/backtests_after.json')
    scorecard = read('reports/policy_scorecard.json')
    membership = list(csv.DictReader((ROOT / 'data/universe_sources/membership_decisions.csv').open()))
    fortune = [r for r in membership if r['list'] == 'Fortune 100 2026']
    proxy = {r['ticker'] for r in membership if r['list'].startswith('OEF')}
    fortune_active = sum(r['ticker'] in active for r in fortune)
    deferred = [d for d in ledger['decisions'] if d['status'] != 'admitted']
    lines = ['# Bellwether quantitative audit', '', 'Evidence collected 31 October–1 November 2026. Changes are local phase commits; this audit has not been pushed to GitHub or deployed.', '',
        '**The requested full empirical certification is not achieved.** All configured policies have A–F reports, but all 72 remain FAIL-UNRESOLVED under the requested full-cohort, legal-scope, matched-benchmark, totals and duration requirements. Passing software checks is not a policy-accuracy certification. No missing evidence was replaced with invented parameters.', '',
        '## Inventory and coverage', '', '| Item | Before | After |', '|---|---:|---:|',
        f'| Active companies | 203 | {len(active)} |', '| Industries | 10 | 10 |',
        f'| Industry policies | 66 | {len(scorecard)} |', '| Macro shocks | 10 | 10 |',
        f'| Explicit own-industry company/policy decisions | 1,338 | {coverage["decisions"]:,} |',
        f'| Nonzero default EPS/value coverage | Not established by the old scope audit | {coverage["covered"]}/{len(active)} |', '',
        'The five remaining coverage failures are **' + ', '.join(coverage['gaps']) + '**. Revenue-only effects and inactive missing-exposure sentinels do not qualify. See [coverage matrix](coverage_matrix.csv) and [gap explanations](coverage_gaps.md).', '',
        '### Publisher lists and admission decisions', '',
        f'- **Fortune 100 (2026):** all 100 publisher ranking rows and company profiles archived. {fortune_active}/100 active, or {fortune_active}/90 public ordinary-equity candidates. Eight private/mutual companies are explicitly excluded; FNMA and FMCC remain in a separate conservatorship category. Nine public candidates are deferred.',
        f'- **S&P 100:** full current publisher constituent list was not obtained. The publisher page verified its top ten and 101 securities only; HTTP access to the complete resource was blocked. No full S&P membership percentage is certified. The separately labeled iShares OEF cross-check has 101 securities/100 deduplicated issuers, {len(proxy & active)}/100 active. It is fund-issuer evidence, not the requested S&P publisher list.',
        '- Share-class deduplication maps GOOG/GOOGL to GOOGL and Berkshire A/B to a single deferred BRK-A identity. Visa uses Class A-equivalent diluted shares rather than an unweighted sum of unequal classes. Existing ticker changes remain in the identity pipeline.',
        '- New issuers use their SEC SIC and actual segment/business descriptions. No original issuer was removed. Exact statements are retained with normalization flags; unsupported borrowing/cost quantities are not represented as reported zeros. New legacy-policy/macro exposures remain explicitly unquantified until measured; no peer exposure was copied.',
        '- Palantir and PayPal were admitted after actual annual covers confirmed Delaware despite blank SEC submissions metadata. Charter is also Delaware, but its positive US pretax exposure was not separately quantified; US revenue alone is insufficient.', '',
        'Primary sources: [Fortune publisher ranking](https://fortune.com/ranking/fortune500/), [S&P publisher](https://www.spglobal.com/spdji/en/indices/equity/sp-100/#data), [OEF issuer holdings](https://www.ishares.com/us/products/239723/ishares-s-p-100-etf/latest-holdings.csv). Raw sources and every initial membership decision are in `data/universe_sources/`; final active/deferred decisions are in `admission_decisions.json`.', '',
        '**Added (' + str(len(ledger['added'])) + '):** ' + ', '.join(ledger['added']) + '.', '',
        '| Deferred public candidate | Reason |', '|---|---|']
    lines += [f'| {d["ticker"]} | {d["reason"].replace("|", "/")} |' for d in deferred]
    excluded = [r for r in fortune if r['status'] in ('excluded_no_traded_equity', 'conservatorship')]
    lines += ['', '| Fortune exclusion/separate category | Decision |', '|---|---|']
    lines += [f'| {r["name"]} | {r["reason"]} |' for r in excluded]
    lines += ['', '### Six new policies', '',
        'One submitted federal rate proposal, [S.Amdt.2428, section 71117](https://www.congress.gov/amendment/119th-congress/senate-amendment/2428/text), is represented in six industry entries. It proposed 21% → 28%; it was submitted, **not enacted**. Positive reported US book pretax income is a labeled taxable-income proxy; credits, tax losses, deferred-tax remeasurement and behavioral response are omitted. Historical income bounds are not confidence intervals. Exact company lists are in the coverage-gap report.', '']
    lines += ['- `' + s['policy'] + '`' for s in scorecard if 'us_corporate_tax_' in s['policy']]
    lines += ['', '## Phase 1 findings and final disposition', '', '| Issue | Root cause and final action | Unresolved limit |', '|---|---|---|',
        '| KR/BBY/TGT tariffs | KR cost line $113,240M added from actual filing. Losses remain uncapped and >50% default EPS effects are flagged. | Import shares, pass-through and demand priors remain UNVERIFIED. KR still has an implausibly large modeled loss; this is unresolved, not a successful tariff calibration. |',
        '| Steel tariffs | Separate buyer and producer responses: USITC table 5.2 gives +2.39% and +0.74% under 25% tariffs, replacing a conflated response. | Company shares and earnings flow-through unverified; full-year EPS/margin growth is not a causal tariff response. |',
        '| AMD / Intel | Revenue can rise while unrecovered imported costs reduce profit; this is algebraically consistent. Intel is now explicitly unavailable for permanent P/E valuation without supported normalized earnings. | AMD imported-cost denominator and pass-through not independently verified. No invented positive Intel valuation. |',
        '| COF rate / valuation | Own Table 32 NII sensitivities replace peer assumptions. Three issuer-adjusted annual EPS values, 12.52/13.96/19.61, support a 13.96 valuation median. Reported EPS percentage denominator is unchanged. | Non-GAAP exclusions can recur; pre-Discover years are not merged-company pro-forma history. Rate sensitivity horizon is not permanent equity persistence. |',
        '| AmEx / networks | Hypothetical four-party credit-issuer cap excludes three-party merchant discount and network service fees as written; Visa added. | No enacted US credit-card counterpart to debit Regulation II claimed. Expansion of the hypothetical scope needs judgment. |',
        '| Negative Humana price | Projected equity price floored at zero, equity-wiped-out label and value-reconciliation adjustment; earnings losses remain uncapped. | Other issuers without verified adjusted earnings stay unavailable, rather than using an unsupported P/E. |',
        '| Debt / finance arms | Alternate GAAP/custom facts and actual filing supplements. F/GM/DE/PCAR/TXT industrial borrowings separated from captive finance; leases are not indiscriminately added. EXR complete term plus revolver/commercial-paper debt is $13,230.651M. | Several education borrowing bases remain unquantified. A missing tag is not a reported zero. |',
        '| Missing costs | Exact alternate tags/filing supplements; insurer claims and loss expense replaces merchandise COGS. | Operating/gross cost is not necessarily incremental cost; service-company profit transmission remains open. |',
        '| Old cover shares | Latest period before filing-order selection; dimensional class counts from current annual covers for CMCSA/MA/NKE/SCHL. | Annual diluted EPS and current economic shares can differ; Visa Class A-equivalent proxy explicitly flagged. |',
        '| Tax clipping | Preserve raw rate; preceding ordinary-rate median or era-appropriate federal statutory fallback replaces hard clipping. | 0–40% anomaly screen is a judgment, not a legal bound; state/foreign/special-item normalization incomplete. |',
        '| Only 12 live quotes | Removed 12-ticker request cap; all due tickers use bounded batching/retries. Added issuers have actual Yahoo observations. Old parser caches invalidated by normalization version. | Free providers can fail or lag; per-record observation dates and snapshot fallbacks remain visible. |', '',
        'Regression tests cover these code/data rules. Unverified economic coefficients were retained per the brief. Phase 1 checkpoint values in `PHASE1_ISSUES.md` are superseded by the stricter final adjusted-EPS guard and peer-sensitivity changes documented here.', '',
        '## Policy scorecard', '',
        'Whole-policy verdict counts: ' + ', '.join(f'{k}: {v}' for k, v in sorted(Counter(s['verdict'] for s in scorecard).items())) + '.', '',
        'Twenty-three exact bank sensitivity comparisons pass direction and size after twelve coefficient changes at six banks. Steel has a verified sector-price calibration. These are in-sample checks; neither validates every company, official total, legal omission or permanent valuation horizon. Per-policy reports include source/value rows, unmatched evidence, tornado outputs and ranking where at least five like-for-like observations exist.', '',
        '| Policy / report | Verdict | Matched / passed benchmarks | Changed parameters |', '|---|---|---:|---:|']
    lines += [f'| [{s["policy"]}]({Path(s["report"]).relative_to("reports")}) | {s["verdict"]} | {s["matched_benchmarks"]} / {s["benchmark_passes"]} | {s["recalibrated_parameters"]} |' for s in scorecard]
    old = {c['id']: c for c in before['cases']}
    paired = []
    lines += ['', '## Backtests: unchanged sample and expanded sample', '',
        f'Original sample: {before["summary"]["hits"]}/{before["summary"]["n"]} ({before["summary"]["accuracy_pct"]:.1f}%). Expanded sample: {after["summary"]["hits"]}/{after["summary"]["n"]} ({after["summary"]["accuracy_pct"]:.1f}%), {after["summary"]["cases"]} cases across ten industries. Industry-balanced expanded score: {after["summary"]["industry_balanced_pct"]:.2f}%. Excluded company-cases: {after["summary"]["excluded"]}.', '',
        'Each row compares a specific financial metric, not stock-return prediction. MAE units differ and must not be pooled. Before MAE is on the original cohort; after MAE uses the expanded cohort. The common-cohort table below isolates recalibration from additions.', '',
        '| Case | Metric unit | Before n / hit % | Before MAE / no-change | After n / hit % | After MAE / no-change |', '|---|---|---:|---:|---:|---:|']
    for c in after['cases']:
        prior = old.get(c['id'])
        s = c['summary']
        b = prior['summary'] if prior else None
        lines.append(f'| {c["id"]} | {c["unit"]} | ' + (f'{b["n"]} / {fmt(b["accuracy_pct"])}' if b else 'New') + ' | ' + (f'{fmt(b["mae"])} / {fmt(b["no_change_mae"])}' if b else '—') + f' | {s["n"]} / {fmt(s["accuracy_pct"])} | {fmt(s["mae"])} / {fmt(s["no_change_mae"])} |')
        if prior:
            old_rows = {r['ticker']: r for r in prior['rows']}
            new_rows = {r['ticker']: r for r in c['rows']}
            assert old_rows.keys() <= new_rows.keys(), 'Original cohort was silently dropped'
            original = list(old_rows.values())
            current = [new_rows[t] for t in old_rows]
            paired.append(dict(case=c['id'], n=len(current), before_hits=sum(r['direction_ok'] for r in original), after_hits=sum(r['direction_ok'] for r in current),
                before_mae=mean(abs(r['error']) for r in original), after_mae=mean(abs(r['error']) for r in current)))
    n = sum(r['n'] for r in paired)
    hits = sum(r['after_hits'] for r in paired)
    lines += ['', f'**Common original cohort after changes: {hits}/{n} ({100*hits/n:.1f}%), versus 104/120 before.** All original eligible company-cases remain present.', '',
        '| Original case | n | Hits before → after | MAE before → after |', '|---|---:|---:|---:|']
    lines += [f'| {r["case"]} | {r["n"]} | {r["before_hits"]} → {r["after_hits"]} | {fmt(r["before_mae"])} → {fmt(r["after_mae"])} |' for r in paired]
    (ROOT / 'reports/backtest_comparison.json').write_text(json.dumps(dict(common_original_cohort=paired, after_original_hits=hits, after_original_n=n, expanded_summary=after['summary']), indent=2) + '\n')
    lines += ['', 'Steel common-cohort MAE worsens because the sourced causal sector-price response replaces a coefficient that happened to fit total annual earnings better. It is retained: fitting annual volume, tax and mix would misattribute non-policy effects. Expanded consumer MAE also worsens because the admitted companies change the cohort; the common original consumer cohort is unchanged. The original bank cohort magnitude improves slightly. No observation or company was dropped to preserve a headline.', '',
        'Three new non-TCJA cases are **2018 Fed tightening, 2020 Fed easing and the 2022–23 Pell maximum increase**. The steel case also expands beyond its original three companies. Daily FRED annual means and enacted Pell maximum schedules are sourced. Bank annual-average rate paths are not instantaneous sensitivity shocks; Pell award maxima are not company revenue effects. The 2020 pandemic, balance-sheet changes, enrollment and acquisitions are major confounders. Six other industry cases share one TCJA episode; current exposures and restated filings introduce look-ahead risk. These are retrospective diagnostics, not independent causal forecasts or a probability of future correctness.', '',
        '## Arithmetic and software validation', '',
        'The reproducible stratified random draw (seed 20261031, one affected default scenario per industry) independently recomputes channel effects, pretax-to-tax-to-parent income, diluted-share EPS and duration-specific value. It reuses the configured expression evaluator but not the engine channel/aggregation/valuation implementations. Ten calculations match EPS and price to the cent; unavailable price remains unavailable. Formulas and intermediate values are in [spotchecks.md](spotchecks.md).', '']
    validation = ROOT / 'reports/validation_results.json'
    if validation.exists():
        for k, v in json.loads(validation.read_text()).items():
            lines.append(f'- **{k}:** {v}')
    else:
        lines.append('Final software check results pending; do not treat this draft as complete.')
    lines += ['', 'Scenario URLs, original policy IDs, CSV export columns and schema-version-1 profile JSON remain compatible. Reference-company profile import/lookup follows the same sourced normalization guard when the financial basis matches; edited financials do not silently borrow another basis.', '',
        '## Open items requiring judgment, ranked by impact', '',
        '1. **Large tariff/cost projections:** obtain company-specific import denominators, realized tariff cost and pass-through. KR/BBY/TGT and AMD values remain UNVERIFIED. Do not publish extreme EPS losses as calibrated forecasts. Operating costs can include fixed expenses; TTEK’s reported cost proxy implies an 84.8% contribution margin, which is not an independently supported incremental margin. Preserve reported facts and review the transmission model.',
        '2. **Full empirical and legal certification:** most policy cohorts lack matched published sensitivities, official comparable totals or independently checked thresholds, effective dates and horizons. Bank instantaneous annual NII sensitivity does not justify permanent valuation. All 72 full-policy verdicts therefore remain unresolved, even where a coefficient was repaired. Prioritize regulated-bank, MA and tariff scenarios with obtainable exact disclosures before broader claims.',
        '3. **Five mandatory coverage gaps:** BLK parent/minority tax-base reconciliation; PGR US taxable base; SLM insured-bank NII/assessment data in the education bucket; LYFT loss-year/nonbinding tax base and unquantified buyback excise tax; MDT Irish-versus-US geography. Do not infer FDIC insurance for insurer policyholders or tuition exposure for a lender.',
        '4. **Incomplete target universe:** obtain the full publisher S&P list, then resolve the deferred public issuers. Berkshire needs insurer/investment accounting and economically equivalent shares; ET/EPD partnership taxation differs from corporate tax; foreign domicile requires an explicit US base; negative or missing domestic income cannot be replaced with a guessed positive amount.',
        '5. **Normalized valuation:** verify adjusted three-year histories or a fully reconciled EV/EBITDA method for other depressed/negative-EPS issuers. COF issuer non-GAAP amortization exclusions can recur and its acquisition changes comparability. No unadjusted median is labeled normalized.',
        '6. **Data definitions and timing:** remaining unknown borrowing balances, fixed-versus-variable cost definitions, annual/current share mismatches and geographic book-to-tax conversion need exact evidence. Cloud provider availability and per-record freshness are not guaranteed.',
        '7. **Historical validation design:** source point-in-time exposures and independent event studies. The 81.6% expanded score combines correlated, confounded episodes and is not forecast certification. Additional genuine events should not be manufactured from mismatched metrics.', '',
        'No unsourced judgment above was silently changed. Review failures and missing evidence are part of the delivered audit, not passed checks.', '',
        '## Artifacts and reproduction', '',
        '- [Architecture and phase-0 baseline](../docs/ARCHITECTURE_AUDIT.md)',
        '- [Source registry](../data/sources_registry.csv): exact verified facts versus UNVERIFIED coefficients and model controls.',
        '- [Coverage matrix](coverage_matrix.csv), [coverage failures/new-policy company lists](coverage_gaps.md).',
        '- [Per-policy scorecard CSV](policy_scorecard.csv), [matched benchmarks](benchmark_checks.json).',
        '- [Before](backtests_before.json), [after](backtests_after.json), [common-cohort comparison](backtest_comparison.json).',
        '- [Arithmetic report](spotchecks.md), [methodology](../METHODOLOGY.md), [changelog](../CHANGELOG.md).', '',
        'Run the commands in README’s quantitative-audit section. The admission scripts deliberately refuse a repeated mutation; cached raw SEC documents and their exact contexts support review. No paid API, runtime LLM or new dependency was added.', '']
    (ROOT / 'reports/AUDIT_SUMMARY.md').write_text('\n'.join(lines))
    print(f'Summary: {len(active)} companies, {coverage["decisions"]} decisions, {hits}/{n} original comparisons retained.')


if __name__ == '__main__':
    main()

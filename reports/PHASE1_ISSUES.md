# Phase 1 — known issues

Access date: 2026-10-31. Full baseline retained in scenarios_before.json and backtests_before.json. Verified facts are distinguished from modeling estimates in data/sources_registry.csv.

| Issue | Root cause and action | Remaining uncertainty |
|---|---|---|
| Retail tariffs | KR lacked its reported $113,240M cost line. Added exact alternate XBRL tag. Losses remain uncapped; an earnings loss can exceed annual earnings. | KR import share 27% and peer-based BBY/TGT shares remain UNVERIFIED; no disclosed numeric import-cost denominator found. Extreme outputs are review flags, not calibrated forecasts. |
| Steel | Conflated domestic-mill and blended buyer prices; recalibrated separately to USITC table 5.2: 0.74% and 2.39% under 25% tariffs. | Company shares, pass-through and flow-through remain UNVERIFIED. Total annual EPS growth is not a causal tariff sensitivity. |
| AMD / Intel | Positive revenue with negative EPS follows price pass-through plus unrecovered costs and demand response; not an accounting contradiction. Intel negative EPS no longer automatically blocks valuation if positive historical median exists. | AMD outsources wafers, but this does not establish the US-imported share of its global cost denominator. Retained exposure UNVERIFIED. |
| Capital One | Depressed reported EPS inflated constant-P/E valuation. Three-year median replaces depressed EPS only for valuation; reported EPS changes preserved. | Median uses reported historical EPS; special-item-adjusted three-year EPS not independently verified. No invented adjusted denominator. |
| AmEx / Mastercard | Existing policy explicitly covers a hypothetical four-party credit-issuer interchange cap. AmEx three-party merchant discount and network fees are excluded as written. | Not an enacted US credit-card analogue of Regulation II; legal scope and exemptions require judgment. Visa candidate tracked in universe phase. |
| Negative equity | Constant-multiple losses were allowed below zero. Floor projected equity price at $0 with explicit equity-wiped-out label and separate value reconciliation channel. | Operating losses and EPS are intentionally not capped. |
| Debt | Companyfacts omits custom/dimensional tags; several overlapping GAAP concepts were missed. Corrected generic chains and added exact inline filing supplements; captive finance debt separated. | LOPE, STRA, DUOL, COUR, PRDO, CHGG remain unquantified where no complete borrowing balance could be verified. Missing is not zero. EXR term-debt/revolver completeness needs further review. |
| Cost base | Missing industry-specific tags and reported operating cost lines. Added exact tags/sourced supplements; PGR uses claims and loss-adjustment expense. | Operating cost proxies include fixed costs and are labeled; not independently calibrated incremental margins. |
| Cover shares | Companyfacts omitted newer class-dimensional DEI facts and filing-first sorting selected stale counts. Latest period selected first; current annual class contexts summed for four cases. | Current price and annual diluted EPS can have different share bases. |
| Tax | Hard clipping distorted anomalous reported rates. Preserve raw rates; use preceding three-year ordinary-rate median where available, otherwise era-appropriate federal statutory rate. | Ordinary-rate screen 0–40% is an existing modeling judgment; state taxes and special items not fully normalized. |
| Live quotes | Vercel request refresh limited the all-company request to 12 tickers. Request all due tickers with existing batches and per-record cache/retry handling. | Provider failures retain visibly dated snapshots; no real-time guarantee. SEC financial refresh remains rate-limited and rotates. |

## Default scenario changes

| Policy / company | EPS before | EPS after | Implied price before | Implied price after |
|---|---:|---:|---:|---:|
| consumer_retail/import_tariffs / KR | -263.65% | -271.96% | $-109.27 | $0.00 |
| consumer_retail/import_tariffs / BBY | -109.45% | -109.45% | $-9.43 | $0.00 |
| consumer_retail/import_tariffs / TGT | -87.19% | -87.19% | $19.56 | $19.56 |
| financial_services/fed_rate_change / COF | -45.16% | -45.16% | $110.41 | $169.72 |
| healthcare/medicare_advantage_rate_change / HUM | -62.78% | -62.78% | $157.07 | $157.07 |
| industrials/steel_tariffs / NUE | 78.25% | 5.79% | $460.09 | $273.06 |
| industrials/steel_tariffs / STLD | 74.99% | 5.55% | $422.65 | $254.93 |
| tmt/semiconductor_tariffs / AMD | -31.16% | -25.29% | $355.75 | $386.10 |
| tmt/semiconductor_tariffs / INTC | n/m | n/m | unavailable | unavailable |

Defaults above use the committed original quote snapshot for comparability; the Humana regression separately runs the exact -4% shock. User-specific 25% semiconductor and -100bp rate scenarios are retained in regression/validation artifacts.

## Verification

525 Python tests passed, 5 skipped; 16 frontend tests passed; production frontend build passed. Complete internal audit: 66 policies, 10 macro shocks, 0 failures. These checks establish arithmetic/scope consistency, not independent empirical calibration.

The 2018 steel backtest now misses the observed Nucor annual margin magnitude by more. This is disclosed rather than widening the range to absorb demand, volume and mix. The official causal price metric is better evidence for the price channel than fitting a whole-year earnings outcome.


## Final superseding resolutions — 1 November 2026

The table above is the Phase 1 checkpoint, not the final valuation result. The
final audit disables an unadjusted historical-median P/E fallback. Capital One's
verified issuer-adjusted 2023/2024/2025 EPS is 12.52/13.96/19.61, so its valuation
median is 13.96. Other depressed/negative-EPS firms without verified adjustments
remain unavailable for permanent earnings valuation. COF bank sensitivities also
use its own current table. Reported EPS remains the percentage denominator.

EXR's complete term plus revolver/commercial-paper borrowing base is now verified
at $13,230.651M; included unsecured term debt is not added twice. Visa is active
with Class A-equivalent diluted shares. Insurer statement templates use claims.
See AUDIT_SUMMARY.md for final counts, tests, remaining failures and backtests.

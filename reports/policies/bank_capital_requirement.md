# Higher bank capital requirements (CET1)

Policy `financial_services/bank_capital_requirement` · evidence checkpoint 2026-11-01 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

Regulators raise required common equity tier 1 capital (for example a Basel III endgame or GSIB surcharge change), so banks hold more equity against the same assets. Earnings don't change but return on equity falls, which lowers value; banks running closest to their minimums feel it most.

Duration: `permanent`. Default inputs: `{"d_ratio_pp": 1.0}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| bank_capital | ['bank'] / unavailable | {"cet1_ratio": "exposure.cet1_ratio_std", "d_ratio": "input.d_ratio_pp / 100", "mm_offset": "assumption.mm_offset"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://www.sec.gov/Archives/edgar/data/19617/000162828026008131/jpm-20251231.htm
- https://www.sec.gov/Archives/edgar/data/72971/000007297126000133/wfc-20251231.htm
- https://www.bankofengland.co.uk/external-mpc-discussion-paper/2011/optimal-bank-capital

| Company | Configured status | Basis |
|---|---|---|
| JPM | included | Higher CET1 lowers modeled ROE/value while EPS remains unchanged. |
| BAC | included | Higher CET1 lowers modeled ROE/value while EPS remains unchanged. |
| WFC | included | Higher CET1 lowers modeled ROE/value while EPS remains unchanged. |
| GS | included | Higher CET1 lowers modeled ROE/value while EPS remains unchanged. |
| C | included | Higher CET1 lowers modeled ROE/value while EPS remains unchanged. |
| AXP | included | Higher CET1 lowers modeled ROE/value while EPS remains unchanged. |
| MS | included | Higher CET1 lowers modeled ROE/value while EPS remains unchanged. |
| SCHW | included | Higher CET1 lowers modeled ROE/value while EPS remains unchanged. |
| BNY | included | Higher CET1 lowers modeled ROE/value while EPS remains unchanged. |
| STT | included | Higher CET1 lowers modeled ROE/value while EPS remains unchanged. |
| USB | included | Higher CET1 lowers modeled ROE/value while EPS remains unchanged. |
| PNC | included | Higher CET1 lowers modeled ROE/value while EPS remains unchanged. |
| TFC | included | Higher CET1 lowers modeled ROE/value while EPS remains unchanged. |
| COF | included | Higher CET1 lowers modeled ROE/value while EPS remains unchanged. |
| FITB | included | Higher CET1 lowers modeled ROE/value while EPS remains unchanged. |
| HBAN | included | Higher CET1 lowers modeled ROE/value while EPS remains unchanged. |
| KEY | included | Higher CET1 lowers modeled ROE/value while EPS remains unchanged. |
| ALLY | included | Higher CET1 lowers modeled ROE/value while EPS remains unchanged. |
| MA | outside_scope | CET1 is a bank capital standard. Insurance capital, asset-manager capital and payment-network regulation need separate policy channels. |
| BLK | outside_scope | CET1 is a bank capital standard. Insurance capital, asset-manager capital and payment-network regulation need separate policy channels. |
| AIG | outside_scope | CET1 is a bank capital standard. Insurance capital, asset-manager capital and payment-network regulation need separate policy channels. |
| PRU | outside_scope | CET1 is a bank capital standard. Insurance capital, asset-manager capital and payment-network regulation need separate policy channels. |
| PGR | outside_scope | CET1 is a bank capital standard. Insurance capital, asset-manager capital and payment-network regulation need separate policy channels. |
| ALL | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| MET | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| SNEX | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| SPGI | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| TRV | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| V | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| PYPL | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |

## B. Every in-scope exposure

Exact numeric checks are distinguished from filing links and estimates. UNVERIFIED values are retained, not silently replaced. Historical observed low/high values are not forecast confidence intervals.

| Company | Exposure | Base | Low | High | Exact-source status | Primary source / location / rationale |
|---|---|---:|---:|---:|---|---|
| JPM | cet1_ratio_std | 0.146 | 0.146 | 0.146 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/19617/000162828026008131/jpm-20251231.htm · JPMorgan 2025 10-K capital table: Standardized CET1 capital ratio 14.6% at Dec 31, 2025 (requirement 11.5%);  · unavailable |
| BAC | cet1_ratio_std | 0.114 | 0.114 | 0.114 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/70858/000007085826000157/bac-20251231.htm · Bank of America 2025 10-K regulatory capital table: CET1 ratio 11.4% Standardized (12.8% Advanced; requirement 10.0%) at Dec 31, 2025;  · unavailable |
| WFC | cet1_ratio_std | 0.1061 | 0.1061 | 0.1061 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/72971/000007297126000133/wfc-20251231.htm · Wells Fargo 2025 10-K: CET1 ratio 10.61% under the Standardized Approach (binding) vs 8.50% minimum plus buffers;  · unavailable |
| GS | cet1_ratio_std | 0.143 | 0.143 | 0.143 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/886982/000088698226000091/gs-20251231.htm · Goldman Sachs 2025 10-K: CET1 capital ratio 14.3% under the Standardized Capital Rules (15.1% Advanced) as of December 2025;  · unavailable |
| C | cet1_ratio_std | 0.1318 | 0.1318 | 0.1318 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/831001/000083100126000011/c-20251231.htm · Citigroup 2025 10-K: CET1 Capital ratio 13.18% (Standardized, binding) at Dec 31, 2025; required 11.6%;  · unavailable |
| AXP | cet1_ratio_std | 0.105 | 0.105 | 0.105 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/4962/000000496226000080/axp-20251231.htm · American Express 2025 10-K selected data: Common Equity Tier 1 10.5% (Standardized; target range 10–11%);  · unavailable |
| MS | cet1_ratio_std | 0.143 | 0.143 | 0.143 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Capital markets and custody; median base and outer low/high from GS in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Capital markets and custody; median base and outer low/high from GS in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| SCHW | cet1_ratio_std | 0.143 | 0.143 | 0.143 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Capital markets and custody; median base and outer low/high from GS in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Capital markets and custody; median base and outer low/high from GS in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| BNY | cet1_ratio_std | 0.143 | 0.143 | 0.143 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Capital markets and custody; median base and outer low/high from GS in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Capital markets and custody; median base and outer low/high from GS in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| STT | cet1_ratio_std | 0.143 | 0.143 | 0.143 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Capital markets and custody; median base and outer low/high from GS in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Capital markets and custody; median base and outer low/high from GS in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| USB | cet1_ratio_std | 0.114 | 0.105 | 0.146 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Regional and consumer banking; median base and outer low/high from JPM/BAC/WFC/C/AXP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Regional and consumer banking; median base and outer low/high from JPM/BAC/WFC/C/AXP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| PNC | cet1_ratio_std | 0.114 | 0.105 | 0.146 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Regional and consumer banking; median base and outer low/high from JPM/BAC/WFC/C/AXP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Regional and consumer banking; median base and outer low/high from JPM/BAC/WFC/C/AXP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| TFC | cet1_ratio_std | 0.114 | 0.105 | 0.146 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Regional and consumer banking; median base and outer low/high from JPM/BAC/WFC/C/AXP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Regional and consumer banking; median base and outer low/high from JPM/BAC/WFC/C/AXP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| COF | cet1_ratio_std | 0.114 | 0.105 | 0.146 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Regional and consumer banking; median base and outer low/high from JPM/BAC/WFC/C/AXP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Regional and consumer banking; median base and outer low/high from JPM/BAC/WFC/C/AXP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| FITB | cet1_ratio_std | 0.114 | 0.105 | 0.146 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Regional and consumer banking; median base and outer low/high from JPM/BAC/WFC/C/AXP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Regional and consumer banking; median base and outer low/high from JPM/BAC/WFC/C/AXP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| HBAN | cet1_ratio_std | 0.114 | 0.105 | 0.146 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Regional and consumer banking; median base and outer low/high from JPM/BAC/WFC/C/AXP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Regional and consumer banking; median base and outer low/high from JPM/BAC/WFC/C/AXP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| KEY | cet1_ratio_std | 0.114 | 0.105 | 0.146 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Regional and consumer banking; median base and outer low/high from JPM/BAC/WFC/C/AXP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Regional and consumer banking; median base and outer low/high from JPM/BAC/WFC/C/AXP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| ALLY | cet1_ratio_std | 0.114 | 0.105 | 0.146 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Regional and consumer banking; median base and outer low/high from JPM/BAC/WFC/C/AXP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Regional and consumer banking; median base and outer low/high from JPM/BAC/WFC/C/AXP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |

## C. Published sensitivity benchmark

| Company / input | Metric | Published | Modeled | Low / high | Relative error | Direction / size | Source |
|---|---|---:|---:|---|---:|---|---|
| — | No matched published company sensitivity obtained | — | — | — | — | FAIL-UNRESOLVED | The exact input, timing, business perimeter and financial metric must match before comparison. |

## D. Tolerances, totals and ranking

Direction must match; size must be within ±25% of the published value or contain it in the scenario range. No benchmark means no pass. Comparisons below are in-sample calibration checks, not independent prediction validation.

Totals: no like-for-like official score for this public-company sample and exact policy horizon was obtained. A national ten-year fiscal score cannot be compared directly with a one-year partial-company cost total. **UNVERIFIED.**

Spearman: unavailable; fewer than five matched published company observations. No ordering is inferred from unverified priors.

## E. One-at-a-time sensitivity

| Driver | Industry metric at low | At high | Absolute swing |
|---|---:|---:|---:|
| assumption.mm_offset | -0.042340568 | -0.010585142 | 0.031755426 |
| exposure.cet1_ratio_std | -0.025722211 | -0.024571176 | 0.0011510357 |

Dominant configured driver: `mm_offset` using `d_mcap_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.


## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 18 unchecked in-scope exposure values; 1 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

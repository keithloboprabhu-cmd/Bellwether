# Credit card late-fee cap

Policy `financial_services/credit_card_late_fee_cap` · evidence checkpoint 2026-11-01 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

Caps the late fee large card issuers may charge, like the CFPB's 2024 $8 rule (vacated by a federal court in April 2025). Citi, with its private-label Retail Services book, has the most late-fee revenue relative to its size; Apple Card (Goldman) charges no late fees.

Duration: `permanent`. Default inputs: `{"fee_cut_usd": 24.0}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| price | unavailable / unavailable | {"d_price": "-min(input.fee_cut_usd, assumption.current_avg_fee) / assumption.current_avg_fee", "exposed_revenue_share": "exposure.card_late_fee_revenue_share", "offset_share": "assumption.offset_share"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://www.consumerfinance.gov/compliance/compliance-resources/consumer-cards-resources/credit-card-penalty-fees/
- https://www.consumerfinance.gov/about-us/newsroom/cfpb-bans-excessive-credit-card-late-fees-lowers-typical-fee-from-32-to-8/
- https://www.hklaw.com/en/insights/publications/2025/04/cfpb-credit-card-late-fees-rule-vacated-by-texas-district-court

| Company | Configured status | Basis |
|---|---|---|
| JPM | included | Binding late-fee cap lowers issuer fee revenue. |
| BAC | included | Binding late-fee cap lowers issuer fee revenue. |
| WFC | included | Binding late-fee cap lowers issuer fee revenue. |
| GS | outside_scope | Non-issuers have no covered card late fees. Goldman's modeled Apple Card book charges no late fees; Ally sold its card business. |
| C | included | Binding late-fee cap lowers issuer fee revenue. |
| AXP | included | Binding late-fee cap lowers issuer fee revenue. |
| MS | outside_scope | Non-issuers have no covered card late fees. Goldman's modeled Apple Card book charges no late fees; Ally sold its card business. |
| SCHW | outside_scope | Non-issuers have no covered card late fees. Goldman's modeled Apple Card book charges no late fees; Ally sold its card business. |
| BNY | outside_scope | Non-issuers have no covered card late fees. Goldman's modeled Apple Card book charges no late fees; Ally sold its card business. |
| STT | outside_scope | Non-issuers have no covered card late fees. Goldman's modeled Apple Card book charges no late fees; Ally sold its card business. |
| USB | included | Binding late-fee cap lowers issuer fee revenue. |
| PNC | included | Binding late-fee cap lowers issuer fee revenue. |
| TFC | included | Binding late-fee cap lowers issuer fee revenue. |
| COF | included | Binding late-fee cap lowers issuer fee revenue. |
| FITB | included | Binding late-fee cap lowers issuer fee revenue. |
| HBAN | included | Binding late-fee cap lowers issuer fee revenue. |
| KEY | included | Binding late-fee cap lowers issuer fee revenue. |
| ALLY | outside_scope | Non-issuers have no covered card late fees. Goldman's modeled Apple Card book charges no late fees; Ally sold its card business. |
| MA | outside_scope | Non-issuers have no covered card late fees. Goldman's modeled Apple Card book charges no late fees; Ally sold its card business. |
| BLK | outside_scope | Non-issuers have no covered card late fees. Goldman's modeled Apple Card book charges no late fees; Ally sold its card business. |
| AIG | outside_scope | Non-issuers have no covered card late fees. Goldman's modeled Apple Card book charges no late fees; Ally sold its card business. |
| PRU | outside_scope | Non-issuers have no covered card late fees. Goldman's modeled Apple Card book charges no late fees; Ally sold its card business. |
| PGR | outside_scope | Non-issuers have no covered card late fees. Goldman's modeled Apple Card book charges no late fees; Ally sold its card business. |
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
| JPM | card_late_fee_revenue_share | 0.0177 | 0.012 | 0.022 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/19617/000162828026008131/jpm-20251231.htm · estimate; Not disclosed. Card Services loans $247.8B at Dec 2025 (10-K CCB table) × ~1.3% late fees per $ of balances (CFPB: >$14B of late fees in 2022 on roughly $1T of card balances) ≈ $3.2B of $182.4B net revenue. · Not disclosed. Card Services loans $247.8B at Dec 2025 (10-K CCB table) × ~1.3% late fees per $ of balances (CFPB: >$14B of late fees in 2022 on roughly $1T of card balances) ≈ $3.2B of $182.4B net revenue. |
| BAC | card_late_fee_revenue_share | 0.0103 | 0.007 | 0.014 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/70858/000007085826000157/bac-20251231.htm · estimate; Not disclosed. US credit card portfolio $106.0B at Dec 2025 (10-K) × ~1.1% late fees per $ of balances (below the CFPB industry ~1.4% for a prime-heavy book) ≈ $1.2B of $113.1B revenue. · Not disclosed. US credit card portfolio $106.0B at Dec 2025 (10-K) × ~1.1% late fees per $ of balances (below the CFPB industry ~1.4% for a prime-heavy book) ≈ $1.2B of $113.1B revenue. |
| WFC | card_late_fee_revenue_share | 0.0092 | 0.006 | 0.012 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/72971/000007297126000133/wfc-20251231.htm · estimate; Not disclosed. Credit card loans $59.5B at Dec 2025 (10-K Table 22) × ~1.3% late fees per $ of balances ≈ $0.8B of $83.7B revenue. · Not disclosed. Credit card loans $59.5B at Dec 2025 (10-K Table 22) × ~1.3% late fees per $ of balances ≈ $0.8B of $83.7B revenue. |
| C | card_late_fee_revenue_share | 0.0325 | 0.024 | 0.04 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/831001/000083100126000011/c-20251231.htm · estimate; Not disclosed. Total credit card loans $173.1B (10-K; Branded Cards ~$122B and Retail Services ~$50B average loans) × ~1.6% late fees per $ (private-label Retail Services runs higher than the CFPB ~1.4% average) ≈ $2.8B of $85.2B revenue. · Not disclosed. Total credit card loans $173.1B (10-K; Branded Cards ~$122B and Retail Services ~$50B average loans) × ~1.6% late fees per $ (private-label Retail Services runs higher than the CFPB ~1.4% average) ≈ $2.8B of $85.2B revenue. |
| AXP | card_late_fee_revenue_share | 0.0126 | 0.007 | 0.018 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/4962/000000496226000080/axp-20251231.htm · estimate; Not disclosed (delinquency fees sit in service fees and other revenue). Card Member loans $151.8B (10-K) × ~0.6% late fees per $ (prime base, 1.3% 30+ day delinquency) ≈ $0.9B of $72.2B revenue. · Not disclosed (delinquency fees sit in service fees and other revenue). Card Member loans $151.8B (10-K) × ~0.6% late fees per $ (prime base, 1.3% 30+ day delinquency) ≈ $0.9B of $72.2B revenue. |
| USB | card_late_fee_revenue_share | 0.0126 | 0.006 | 0.04 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Regional and consumer banking; median base and outer low/high from JPM/BAC/WFC/C/AXP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Regional and consumer banking; median base and outer low/high from JPM/BAC/WFC/C/AXP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| PNC | card_late_fee_revenue_share | 0.0126 | 0.006 | 0.04 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Regional and consumer banking; median base and outer low/high from JPM/BAC/WFC/C/AXP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Regional and consumer banking; median base and outer low/high from JPM/BAC/WFC/C/AXP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| TFC | card_late_fee_revenue_share | 0.0126 | 0.006 | 0.04 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Regional and consumer banking; median base and outer low/high from JPM/BAC/WFC/C/AXP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Regional and consumer banking; median base and outer low/high from JPM/BAC/WFC/C/AXP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| COF | card_late_fee_revenue_share | 0.0126 | 0.006 | 0.04 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Regional and consumer banking; median base and outer low/high from JPM/BAC/WFC/C/AXP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Regional and consumer banking; median base and outer low/high from JPM/BAC/WFC/C/AXP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| FITB | card_late_fee_revenue_share | 0.0126 | 0.006 | 0.04 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Regional and consumer banking; median base and outer low/high from JPM/BAC/WFC/C/AXP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Regional and consumer banking; median base and outer low/high from JPM/BAC/WFC/C/AXP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| HBAN | card_late_fee_revenue_share | 0.0126 | 0.006 | 0.04 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Regional and consumer banking; median base and outer low/high from JPM/BAC/WFC/C/AXP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Regional and consumer banking; median base and outer low/high from JPM/BAC/WFC/C/AXP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| KEY | card_late_fee_revenue_share | 0.0126 | 0.006 | 0.04 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Regional and consumer banking; median base and outer low/high from JPM/BAC/WFC/C/AXP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Regional and consumer banking; median base and outer low/high from JPM/BAC/WFC/C/AXP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |

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
| exposure.card_late_fee_revenue_share | -0.0093630144 | -0.023927759 | 0.014564745 |
| assumption.offset_share | -0.020840627 | -0.0083362506 | 0.012504376 |
| assumption.current_avg_fee | -0.015561001 | -0.013338001 | 0.0022230002 |

Dominant configured driver: `card_late_fee_revenue_share` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.


## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 12 unchecked in-scope exposure values; 2 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

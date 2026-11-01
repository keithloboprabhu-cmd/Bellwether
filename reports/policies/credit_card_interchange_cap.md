# Credit card interchange cap

Policy `financial_services/credit_card_interchange_cap` · reviewed 2026-10-31 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

A Durbin-style cap on the interchange fee card issuers earn on Visa and Mastercard credit card purchases. JPMorgan and Citi, the largest credit issuers, lose the most; issuers claw much of it back by cutting rewards. Amex's three-party network is assumed exempt, as under the Durbin amendment.

Duration: `permanent`. Default inputs: `{"cap_pct": 1.0}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| price | unavailable / unavailable | {"d_price": "min(0, input.cap_pct / assumption.current_rate_pct - 1)", "exposed_revenue_share": "exposure.credit_interchange_revenue_share", "offset_share": "assumption.rewards_offset"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://www.sec.gov/Archives/edgar/data/19617/000162828026008131/jpm-20251231.htm
- https://www.sec.gov/Archives/edgar/data/831001/000083100126000011/c-20251231.htm
- https://www.federalreserve.gov/econres/feds/bank-profitability-and-debit-card-interchange-regulation-bank-responses-to-the-durbin-amendment.htm

Scope finding: this is a hypothetical US four-party credit-issuer fee cap. AmEx three-party merchant discount is deliberately excluded as written; Visa/Mastercard network service fees are not issuer interchange. Regulation II is a debit-card rule and does not establish an enacted credit-card cap.

| Company | Configured status | Basis |
|---|---|---|
| JPM | included | Credit issuer interchange declines after a binding cap. |
| BAC | included | Credit issuer interchange declines after a binding cap. |
| WFC | included | Credit issuer interchange declines after a binding cap. |
| GS | included | Credit issuer interchange declines after a binding cap. |
| C | included | Credit issuer interchange declines after a binding cap. |
| AXP | outside_scope | The cap covers Visa/Mastercard credit-card issuer interchange. Amex is assumed exempt; Mastercard is a network rather than an issuer. Non-issuers and Ally after its card sale have no direct issuer-fee loss. |
| MS | outside_scope | The cap covers Visa/Mastercard credit-card issuer interchange. Amex is assumed exempt; Mastercard is a network rather than an issuer. Non-issuers and Ally after its card sale have no direct issuer-fee loss. |
| SCHW | outside_scope | The cap covers Visa/Mastercard credit-card issuer interchange. Amex is assumed exempt; Mastercard is a network rather than an issuer. Non-issuers and Ally after its card sale have no direct issuer-fee loss. |
| BNY | outside_scope | The cap covers Visa/Mastercard credit-card issuer interchange. Amex is assumed exempt; Mastercard is a network rather than an issuer. Non-issuers and Ally after its card sale have no direct issuer-fee loss. |
| STT | outside_scope | The cap covers Visa/Mastercard credit-card issuer interchange. Amex is assumed exempt; Mastercard is a network rather than an issuer. Non-issuers and Ally after its card sale have no direct issuer-fee loss. |
| USB | included | Credit issuer interchange declines after a binding cap. |
| PNC | included | Credit issuer interchange declines after a binding cap. |
| TFC | included | Credit issuer interchange declines after a binding cap. |
| COF | included | Credit issuer interchange declines after a binding cap. |
| FITB | included | Credit issuer interchange declines after a binding cap. |
| HBAN | included | Credit issuer interchange declines after a binding cap. |
| KEY | included | Credit issuer interchange declines after a binding cap. |
| ALLY | outside_scope | The cap covers Visa/Mastercard credit-card issuer interchange. Amex is assumed exempt; Mastercard is a network rather than an issuer. Non-issuers and Ally after its card sale have no direct issuer-fee loss. |
| MA | outside_scope | The cap covers Visa/Mastercard credit-card issuer interchange. Amex is assumed exempt; Mastercard is a network rather than an issuer. Non-issuers and Ally after its card sale have no direct issuer-fee loss. |
| BLK | outside_scope | The cap covers Visa/Mastercard credit-card issuer interchange. Amex is assumed exempt; Mastercard is a network rather than an issuer. Non-issuers and Ally after its card sale have no direct issuer-fee loss. |
| AIG | outside_scope | The cap covers Visa/Mastercard credit-card issuer interchange. Amex is assumed exempt; Mastercard is a network rather than an issuer. Non-issuers and Ally after its card sale have no direct issuer-fee loss. |
| PRU | outside_scope | The cap covers Visa/Mastercard credit-card issuer interchange. Amex is assumed exempt; Mastercard is a network rather than an issuer. Non-issuers and Ally after its card sale have no direct issuer-fee loss. |
| PGR | outside_scope | The cap covers Visa/Mastercard credit-card issuer interchange. Amex is assumed exempt; Mastercard is a network rather than an issuer. Non-issuers and Ally after its card sale have no direct issuer-fee loss. |
| ALL | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| MET | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| SNEX | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| SPGI | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| TRV | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| V | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |

## B. Every in-scope exposure

Exact numeric checks are distinguished from filing links and estimates. UNVERIFIED values are retained, not silently replaced. Historical observed low/high values are not forecast confidence intervals.

| Company | Exposure | Base | Low | High | Exact-source status | Primary source / location / rationale |
|---|---|---:|---:|---:|---|---|
| JPM | credit_interchange_revenue_share | 0.13 | 0.1 | 0.16 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/19617/000162828026008131/jpm-20251231.htm · estimate; 10-K Note 6: interchange and merchant processing income $36,222M (reward costs and partner payments $29,720M); that total also includes debit (Durbin-capped) and merchant processing, so we assume ~two-thirds (~$24B) is gross credit card interchange, of $182.4B net revenue. · 10-K Note 6: interchange and merchant processing income $36,222M (reward costs and partner payments $29,720M); that total also includes debit (Durbin-capped) and merchant processing, so we assume ~two-thirds (~$24B) is gross credit card interchange, of $182.4B net revenue. |
| BAC | credit_interchange_revenue_share | 0.062 | 0.045 | 0.08 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/70858/000007085826000157/bac-20251231.htm · estimate; 10-K Note 2 footnote: gross interchange fees and merchant income $13.8B in 2025 (net card income $6.4B after $9.9B rewards/partner costs). That includes debit and merchant income, so we take ~half (~$7B) as gross credit interchange, of $113.1B revenue. · 10-K Note 2 footnote: gross interchange fees and merchant income $13.8B in 2025 (net card income $6.4B after $9.9B rewards/partner costs). That includes debit and merchant income, so we take ~half (~$7B) as gross credit interchange, of $113.1B revenue. |
| WFC | credit_interchange_revenue_share | 0.044 | 0.035 | 0.047 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/72971/000007297126000133/wfc-20251231.htm · estimate; Credit card purchase volume $186.0B in 2025 (10-K) × ~2% interchange ≈ $3.7B of $83.7B revenue; 10-K reports interchange and merchant services fees of $3,973M, which caps the high case. · Credit card purchase volume $186.0B in 2025 (10-K) × ~2% interchange ≈ $3.7B of $83.7B revenue; 10-K reports interchange and merchant services fees of $3,973M, which caps the high case. |
| GS | credit_interchange_revenue_share | 0.02 | 0 | 0.03 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/886982/000088698226000091/gs-20251231.htm · estimate; Not disclosed. Apple Card interchange, guessed at ~$1.2B of $58.3B net revenue. GS agreed in Dec 2025 to transition Apple Card to another issuer (Chase) over ~24 months, so the low case is zero. · Not disclosed. Apple Card interchange, guessed at ~$1.2B of $58.3B net revenue. GS agreed in Dec 2025 to transition Apple Card to another issuer (Chase) over ~24 months, so the low case is zero. |
| C | credit_interchange_revenue_share | 0.109 | 0.09 | 0.116 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/831001/000083100126000011/c-20251231.htm · estimate; USPB interchange fees $9,878M in 2025 (10-K; card rewards and partner payments $12,075M); we take ~$9.3B as credit card after a small debit share from Retail Banking, of $85.2B revenue. · USPB interchange fees $9,878M in 2025 (10-K; card rewards and partner payments $12,075M); we take ~$9.3B as credit card after a small debit share from Retail Banking, of $85.2B revenue. |
| USB | credit_interchange_revenue_share | 0.062 | 0 | 0.16 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Regional and consumer banking; median base and outer low/high from JPM/BAC/WFC/C/AXP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Regional and consumer banking; median base and outer low/high from JPM/BAC/WFC/C/AXP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| PNC | credit_interchange_revenue_share | 0.062 | 0 | 0.16 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Regional and consumer banking; median base and outer low/high from JPM/BAC/WFC/C/AXP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Regional and consumer banking; median base and outer low/high from JPM/BAC/WFC/C/AXP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| TFC | credit_interchange_revenue_share | 0.062 | 0 | 0.16 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Regional and consumer banking; median base and outer low/high from JPM/BAC/WFC/C/AXP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Regional and consumer banking; median base and outer low/high from JPM/BAC/WFC/C/AXP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| COF | credit_interchange_revenue_share | 0.062 | 0 | 0.16 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Regional and consumer banking; median base and outer low/high from JPM/BAC/WFC/C/AXP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Regional and consumer banking; median base and outer low/high from JPM/BAC/WFC/C/AXP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| FITB | credit_interchange_revenue_share | 0.062 | 0 | 0.16 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Regional and consumer banking; median base and outer low/high from JPM/BAC/WFC/C/AXP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Regional and consumer banking; median base and outer low/high from JPM/BAC/WFC/C/AXP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| HBAN | credit_interchange_revenue_share | 0.062 | 0 | 0.16 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Regional and consumer banking; median base and outer low/high from JPM/BAC/WFC/C/AXP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Regional and consumer banking; median base and outer low/high from JPM/BAC/WFC/C/AXP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| KEY | credit_interchange_revenue_share | 0.062 | 0 | 0.16 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Regional and consumer banking; median base and outer low/high from JPM/BAC/WFC/C/AXP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Regional and consumer banking; median base and outer low/high from JPM/BAC/WFC/C/AXP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |

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
| assumption.rewards_offset | -0.053885239 | -0.017961746 | 0.035923492 |
| exposure.credit_interchange_revenue_share | -0.022143491 | -0.052257841 | 0.03011435 |
| assumption.current_rate_pct | -0.031931993 | -0.040609165 | 0.0086771721 |

Dominant configured driver: `rewards_offset` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.


## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 12 unchecked in-scope exposure values; 2 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

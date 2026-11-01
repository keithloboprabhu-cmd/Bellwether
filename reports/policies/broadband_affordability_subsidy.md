# Broadband affordability subsidy (ACP revival)

Policy `tmt/broadband_affordability_subsidy` · evidence checkpoint 2026-11-01 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

Hypothetically revives the Affordable Connectivity Program, which ended in June 2024. Providers with modeled subscriber exposure receive only the estimated incremental or retained revenue; the portion replacing existing customer payments is excluded. Current carrier shares and forward retention remain uncertain.

Duration: `years:3`. Default inputs: `{"households_m": 23.0, "monthly_benefit": 30.0}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| demand_transfer | unavailable / unavailable | {"total_transfer_musd": "derived.annual_program_musd", "mpc": "assumption.incremental_share", "capture_share": "exposure.broadband_subsidy_capture_share"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://consumercomplaints.fcc.gov/hc/en-us/articles/32636130998420-CONSUMER-ADVISORY-FEDERAL-COMMUNICATIONS-COMMISSION-WARNS-CONSUMERS-ABOUT-WEBSITES-ADVERTISING-THE-AFFORDABLE-CONNECTIVITY-PROGRAM
- https://broadbandbreakfast.com/verizon-reports-drop-in-prepaid-subscribers-after-acp-sunset

| Company | Configured status | Basis |
|---|---|---|
| AAPL | outside_scope | Household broadband subsidy payments reach retail access providers, not network-equipment or semiconductor vendors directly. |
| MSFT | outside_scope | Household broadband subsidy payments reach retail access providers, not network-equipment or semiconductor vendors directly. |
| GOOGL | outside_scope | Household broadband subsidy payments reach retail access providers, not network-equipment or semiconductor vendors directly. |
| META | outside_scope | Household broadband subsidy payments reach retail access providers, not network-equipment or semiconductor vendors directly. |
| NVDA | outside_scope | Household broadband subsidy payments reach retail access providers, not network-equipment or semiconductor vendors directly. |
| VZ | included | Broadband subsidies raise access-provider subscriber spending. |
| IBM | outside_scope | Household broadband subsidy payments reach retail access providers, not network-equipment or semiconductor vendors directly. |
| ORCL | outside_scope | Household broadband subsidy payments reach retail access providers, not network-equipment or semiconductor vendors directly. |
| CRM | outside_scope | Household broadband subsidy payments reach retail access providers, not network-equipment or semiconductor vendors directly. |
| ADBE | outside_scope | Household broadband subsidy payments reach retail access providers, not network-equipment or semiconductor vendors directly. |
| INTC | outside_scope | Household broadband subsidy payments reach retail access providers, not network-equipment or semiconductor vendors directly. |
| AMD | outside_scope | Household broadband subsidy payments reach retail access providers, not network-equipment or semiconductor vendors directly. |
| QCOM | outside_scope | Household broadband subsidy payments reach retail access providers, not network-equipment or semiconductor vendors directly. |
| MU | outside_scope | Household broadband subsidy payments reach retail access providers, not network-equipment or semiconductor vendors directly. |
| AVGO | outside_scope | Household broadband subsidy payments reach retail access providers, not network-equipment or semiconductor vendors directly. |
| CSCO | outside_scope | Household broadband subsidy payments reach retail access providers, not network-equipment or semiconductor vendors directly. |
| T | included | Broadband subsidies raise access-provider subscriber spending. |
| CMCSA | included | Broadband subsidies raise access-provider subscriber spending. |
| NFLX | outside_scope | Household broadband subsidy payments reach retail access providers, not network-equipment or semiconductor vendors directly. |
| DIS | outside_scope | Household broadband subsidy payments reach retail access providers, not network-equipment or semiconductor vendors directly. |
| AMAT | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| ANET | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| DELL | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| HPQ | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| INTU | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| LRCX | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| NOW | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| PANW | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| SNDK | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| SNX | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| TMUS | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| TXN | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| PLTR | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |

## B. Every in-scope exposure

Exact numeric checks are distinguished from filing links and estimates. UNVERIFIED values are retained, not silently replaced. Historical observed low/high values are not forecast confidence intervals.

| Company | Exposure | Base | Low | High | Exact-source status | Primary source / location / rationale |
|---|---|---:|---:|---:|---|---|
| VZ | broadband_subsidy_capture_share | 0.06 | 0.048 | 0.09 | UNVERIFIED | https://broadbandbreakfast.com/verizon-reports-drop-in-prepaid-subscribers-after-acp-sunset · estimate; Verizon CFO (Q2 2024 call): about 1.1M prepaid subscribers benefited from ACP, ~4.8% of the program's ~23M households; Fios and 5G home-internet ACP customers (not disclosed) push the total higher. · Verizon CFO (Q2 2024 call): about 1.1M prepaid subscribers benefited from ACP, ~4.8% of the program's ~23M households; Fios and 5G home-internet ACP customers (not disclosed) push the total higher. |
| T | broadband_subsidy_capture_share | 0.06 | 0.048 | 0.09 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Telecom and networking; median base and outer low/high from VZ in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Telecom and networking; median base and outer low/high from VZ in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| CMCSA | broadband_subsidy_capture_share | 0.06 | 0.048 | 0.09 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Telecom and networking; median base and outer low/high from VZ in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Telecom and networking; median base and outer low/high from VZ in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |

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
| assumption.incremental_share | 9.2675839e-05 | 0.00027802752 | 0.00018535168 |
| exposure.broadband_subsidy_capture_share | 0.00012974617 | 0.00024327408 | 0.0001135279 |

Dominant configured driver: `incremental_share` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.


## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 3 unchecked in-scope exposure values; 1 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

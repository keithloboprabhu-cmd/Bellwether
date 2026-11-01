# ACA premium subsidy change

Policy `healthcare/aca_subsidy_change` · reviewed 2026-10-31 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

A change in ACA premium tax credits (e.g. expiry of the enhanced subsidies) changes how many people buy exchange plans. Centene and Molina also have material exchange businesses; Humana and (from 2026) CVS/Aetna have exited the exchanges. Company-specific premium shares are used.

Duration: `permanent`. Default inputs: `{"enrollment_change_pct": -20.0}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| demand_volume | unavailable / unavailable | {"d_volume": "input.enrollment_change_pct / 100 * (1 - assumption.retained_share)", "exposed_revenue_share": "exposure.aca_exchange_revenue_share"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://www.sec.gov/Archives/edgar/data/64803/000006480326000010/cvs-20251231.htm

| Company | Configured status | Basis |
|---|---|---|
| UNH | included | Default subsidy loss reduces exchange enrollment. |
| ELV | included | Default subsidy loss reduces exchange enrollment. |
| HUM | outside_scope | The channel requires ACA exchange premiums. Humana and Aetna/CVS have exited; provider and drug-demand spillovers are outside this premium model. |
| CVS | outside_scope | The channel requires ACA exchange premiums. Humana and Aetna/CVS have exited; provider and drug-demand spillovers are outside this premium model. |
| PFE | outside_scope | The channel requires ACA exchange premiums. Humana and Aetna/CVS have exited; provider and drug-demand spillovers are outside this premium model. |
| LLY | outside_scope | The channel requires ACA exchange premiums. Humana and Aetna/CVS have exited; provider and drug-demand spillovers are outside this premium model. |
| CI | included | Default subsidy loss reduces exchange enrollment. |
| CNC | included | Default subsidy loss reduces exchange enrollment. |
| MOH | included | Default subsidy loss reduces exchange enrollment. |
| JNJ | outside_scope | The channel requires ACA exchange premiums. Humana and Aetna/CVS have exited; provider and drug-demand spillovers are outside this premium model. |
| MRK | outside_scope | The channel requires ACA exchange premiums. Humana and Aetna/CVS have exited; provider and drug-demand spillovers are outside this premium model. |
| ABBV | outside_scope | The channel requires ACA exchange premiums. Humana and Aetna/CVS have exited; provider and drug-demand spillovers are outside this premium model. |
| AMGN | outside_scope | The channel requires ACA exchange premiums. Humana and Aetna/CVS have exited; provider and drug-demand spillovers are outside this premium model. |
| GILD | outside_scope | The channel requires ACA exchange premiums. Humana and Aetna/CVS have exited; provider and drug-demand spillovers are outside this premium model. |
| HCA | outside_scope | The channel requires ACA exchange premiums. Humana and Aetna/CVS have exited; provider and drug-demand spillovers are outside this premium model. |
| THC | outside_scope | The channel requires ACA exchange premiums. Humana and Aetna/CVS have exited; provider and drug-demand spillovers are outside this premium model. |
| UHS | outside_scope | The channel requires ACA exchange premiums. Humana and Aetna/CVS have exited; provider and drug-demand spillovers are outside this premium model. |
| TMO | outside_scope | The channel requires ACA exchange premiums. Humana and Aetna/CVS have exited; provider and drug-demand spillovers are outside this premium model. |
| ABT | outside_scope | The channel requires ACA exchange premiums. Humana and Aetna/CVS have exited; provider and drug-demand spillovers are outside this premium model. |
| MDT | outside_scope | The channel requires ACA exchange premiums. Humana and Aetna/CVS have exited; provider and drug-demand spillovers are outside this premium model. |
| CAH | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| COR | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| ISRG | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| MCK | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |

## B. Every in-scope exposure

Exact numeric checks are distinguished from filing links and estimates. UNVERIFIED values are retained, not silently replaced. Historical observed low/high values are not forecast confidence intervals.

| Company | Exposure | Base | Low | High | Exact-source status | Primary source / location / rationale |
|---|---|---:|---:|---:|---|---|
| UNH | aca_exchange_revenue_share | 0.02 | 0.01 | 0.03 | UNVERIFIED | No source URL · estimate; Individual exchange plans sit inside UHC Employer & Individual ($79,228M, 18% of revenue) and are not split out; exchange business is a small part of E&I. · Individual exchange plans sit inside UHC Employer & Individual ($79,228M, 18% of revenue) and are not split out; exchange business is a small part of E&I. |
| ELV | aca_exchange_revenue_share | 0.045 | 0.035 | 0.055 | UNVERIFIED | No source URL · estimate; Elevance 2025 10-K: 1,307K Individual members (mostly ACA exchange); at ~$6–8K premium per member that is ~$8–10B of $199,125M revenue. · Elevance 2025 10-K: 1,307K Individual members (mostly ACA exchange); at ~$6–8K premium per member that is ~$8–10B of $199,125M revenue. |
| CI | aca_exchange_revenue_share | 0.01 | 0 | 0.055 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Managed care; median base and outer low/high from UNH/ELV/HUM/CVS in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Managed care; median base and outer low/high from UNH/ELV/HUM/CVS in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| CNC | aca_exchange_revenue_share | 0.20486428 | 0.17251729 | 0.21564661 | UNVERIFIED | https://investors.centene.com/2026-02-06-CENTENE-CORPORATION-REPORTS-2025-RESULTS-AND-ANNOUNCES-2026-GUIDANCE · estimate; Company-specific estimate: 2025 Commercial segment premium/service revenue $42,003M / consolidated revenue; estimate 95% (80–100%) belongs to Marketplace rather than group/off-exchange products. Not a separately reported pure-ACA revenue ratio. · Company-specific estimate: 2025 Commercial segment premium/service revenue $42,003M / consolidated revenue; estimate 95% (80–100%) belongs to Marketplace rather than group/off-exchange products. Not a separately reported pure-ACA revenue ratio. |
| MOH | aca_exchange_revenue_share | 0.098776031 | 0.09383723 | 0.10371483 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1179929/000117992926000005/moh-20251231.htm · Molina FY2025 10-K: Marketplace premium revenue $4,487M / total revenue $45,426M; Base is the stated filing ratio; low/high are an explicit ±5% relative modeling sensitivity, not reported confidence bounds. · Base is the stated filing ratio; low/high are an explicit ±5% relative modeling sensitivity, not reported confidence bounds. |

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
| exposure.aca_exchange_revenue_share | -0.0078609443 | -0.012743522 | 0.0048825774 |
| assumption.retained_share | -0.011382486 | -0.0085368644 | 0.0028456215 |

Dominant configured driver: `aca_exchange_revenue_share` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.


## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 5 unchecked in-scope exposure values; 1 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

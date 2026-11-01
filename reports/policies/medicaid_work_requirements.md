# Medicaid funding cuts and work requirements

Policy `healthcare/medicaid_work_requirements` · evidence checkpoint 2026-11-01 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

Work-reporting requirements and tighter eligibility checks reduce Medicaid enrollment, so managed-care plans lose members and premium revenue. The sample includes Medicaid-focused Centene and Molina as well as diversified plans, hospitals. Hospital losses use an estimated patient-volume proxy; uncompensated-care and supplemental-payment effects are outside this channel. Drugmaker prescription/rebate spillovers are outside this enrollment channel.

Duration: `permanent`. Default inputs: `{"enrollment_change_pct": -6.5}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| demand_volume | unavailable / unavailable | {"d_volume": "input.enrollment_change_pct / 100 * (1 - assumption.retained_share)", "exposed_revenue_share": "exposure.medicaid_revenue_share"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://www.cms.gov/newsroom/fact-sheets/medicaid-community-engagement-requirement-certain-individuals-interim-final-rule-comment-period-cms
- https://www.cbo.gov/system/files/2025-06/Wyden-Pallone-Neal_Letter_6-4-25.pdf
- https://www.sec.gov/Archives/edgar/data/731766/000073176626000062/unh-20251231.htm

| Company | Configured status | Basis |
|---|---|---|
| UNH | included | Eligibility loss reduces Medicaid premium and provider-volume revenue. |
| ELV | included | Eligibility loss reduces Medicaid premium and provider-volume revenue. |
| HUM | included | Eligibility loss reduces Medicaid premium and provider-volume revenue. |
| CVS | included | Eligibility loss reduces Medicaid premium and provider-volume revenue. |
| PFE | outside_scope | Only Medicaid plan premiums and an explicit hospital patient-volume proxy are modeled. Drugmaker prescriptions/rebates and supplier demand are not capitated insurance revenue. |
| LLY | outside_scope | Only Medicaid plan premiums and an explicit hospital patient-volume proxy are modeled. Drugmaker prescriptions/rebates and supplier demand are not capitated insurance revenue. |
| CI | outside_scope | Only Medicaid plan premiums and an explicit hospital patient-volume proxy are modeled. Drugmaker prescriptions/rebates and supplier demand are not capitated insurance revenue. |
| CNC | included | Eligibility loss reduces Medicaid premium and provider-volume revenue. |
| MOH | included | Eligibility loss reduces Medicaid premium and provider-volume revenue. |
| JNJ | outside_scope | Only Medicaid plan premiums and an explicit hospital patient-volume proxy are modeled. Drugmaker prescriptions/rebates and supplier demand are not capitated insurance revenue. |
| MRK | outside_scope | Only Medicaid plan premiums and an explicit hospital patient-volume proxy are modeled. Drugmaker prescriptions/rebates and supplier demand are not capitated insurance revenue. |
| ABBV | outside_scope | Only Medicaid plan premiums and an explicit hospital patient-volume proxy are modeled. Drugmaker prescriptions/rebates and supplier demand are not capitated insurance revenue. |
| AMGN | outside_scope | Only Medicaid plan premiums and an explicit hospital patient-volume proxy are modeled. Drugmaker prescriptions/rebates and supplier demand are not capitated insurance revenue. |
| GILD | outside_scope | Only Medicaid plan premiums and an explicit hospital patient-volume proxy are modeled. Drugmaker prescriptions/rebates and supplier demand are not capitated insurance revenue. |
| HCA | included | Eligibility loss reduces Medicaid premium and provider-volume revenue. |
| THC | included | Eligibility loss reduces Medicaid premium and provider-volume revenue. |
| UHS | included | Eligibility loss reduces Medicaid premium and provider-volume revenue. |
| TMO | outside_scope | Only Medicaid plan premiums and an explicit hospital patient-volume proxy are modeled. Drugmaker prescriptions/rebates and supplier demand are not capitated insurance revenue. |
| ABT | outside_scope | Only Medicaid plan premiums and an explicit hospital patient-volume proxy are modeled. Drugmaker prescriptions/rebates and supplier demand are not capitated insurance revenue. |
| MDT | outside_scope | Only Medicaid plan premiums and an explicit hospital patient-volume proxy are modeled. Drugmaker prescriptions/rebates and supplier demand are not capitated insurance revenue. |
| CAH | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| COR | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| ISRG | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| MCK | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |

## B. Every in-scope exposure

Exact numeric checks are distinguished from filing links and estimates. UNVERIFIED values are retained, not silently replaced. Historical observed low/high values are not forecast confidence intervals.

| Company | Exposure | Base | Low | High | Exact-source status | Primary source / location / rationale |
|---|---|---:|---:|---:|---|---|
| UNH | medicaid_revenue_share | 0.21 | 0.18 | 0.211 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/731766/000073176626000062/unh-20251231.htm · UnitedHealth 2025 10-K: UnitedHealthcare Community & State revenue $94,390M of $447,567M total (21%); ~7.4M Medicaid members;  · unavailable |
| ELV | medicaid_revenue_share | 0.25 | 0.2 | 0.3 | UNVERIFIED | No source URL · estimate; Elevance 2025 10-K: 8,500K Medicaid members; at roughly $5–7K premium per member per year that is ~$45–60B of $199,125M revenue. · Elevance 2025 10-K: 8,500K Medicaid members; at roughly $5–7K premium per member per year that is ~$45–60B of $199,125M revenue. |
| HUM | medicaid_revenue_share | 0.1 | 0.08 | 0.112 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/49071/000004907126000009/hum-20251231.htm · Humana 2025 10-K: state-based contracts and other (incl. Medicaid) premiums $14,477M, 11.2% of consolidated premiums and services revenue; 'other' trimmed off for the base;  · unavailable |
| CVS | medicaid_revenue_share | 0.035 | 0.025 | 0.045 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/64803/000006480326000009/cvs_ex99x1q4-25.htm · estimate; CVS Q4 2025 release: 1,952K insured Medicaid members; at ~$6–8K premium per member that is ~$12–16B of $402,067M revenue. · CVS Q4 2025 release: 1,952K insured Medicaid members; at ~$6–8K premium per member that is ~$12–16B of $402,067M revenue. |
| CNC | medicaid_revenue_share | 0.46328879 | 0.44012435 | 0.48645323 | UNVERIFIED | https://investors.centene.com/2026-02-06-CENTENE-CORPORATION-REPORTS-2025-RESULTS-AND-ANNOUNCES-2026-GUIDANCE · Centene FY2025 results: Medicaid premium/service revenue $90,238M / SEC consolidated revenue; Base is the stated filing ratio; low/high are an explicit ±5% relative modeling sensitivity, not reported confidence bounds. · Base is the stated filing ratio; low/high are an explicit ±5% relative modeling sensitivity, not reported confidence bounds. |
| MOH | medicaid_revenue_share | 0.70972571 | 0.67423942 | 0.74521199 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1179929/000117992926000005/moh-20251231.htm · Molina FY2025 10-K: Medicaid premium revenue $32,240M / total revenue $45,426M; Base is the stated filing ratio; low/high are an explicit ±5% relative modeling sensitivity, not reported confidence bounds. · Base is the stated filing ratio; low/high are an explicit ±5% relative modeling sensitivity, not reported confidence bounds. |
| HCA | medicaid_revenue_share | 0.12 | 0.06 | 0.2 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm · estimate; Company-specific estimate of consolidated revenue sensitive to Medicaid patient coverage, not a reported pure managed-care premium ratio. Includes a provider-volume proxy with wide payer-mix uncertainty; does not separately model uncompensated care, state supplemental payments or payer substitution. Hospital/service mix differs from insurers. · Company-specific estimate of consolidated revenue sensitive to Medicaid patient coverage, not a reported pure managed-care premium ratio. Includes a provider-volume proxy with wide payer-mix uncertainty; does not separately model uncompensated care, state supplemental payments or payer substitution. Hospital/service mix differs from insurers. |
| THC | medicaid_revenue_share | 0.08 | 0.04 | 0.14 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/70318/000007031826000012/0000070318-26-000012-index.htm · estimate; Company-specific estimate of consolidated revenue sensitive to Medicaid patient coverage, not a reported pure managed-care premium ratio. Includes a provider-volume proxy with wide payer-mix uncertainty; does not separately model uncompensated care, state supplemental payments or payer substitution. Hospital/service mix differs from insurers. · Company-specific estimate of consolidated revenue sensitive to Medicaid patient coverage, not a reported pure managed-care premium ratio. Includes a provider-volume proxy with wide payer-mix uncertainty; does not separately model uncompensated care, state supplemental payments or payer substitution. Hospital/service mix differs from insurers. |
| UHS | medicaid_revenue_share | 0.2 | 0.1 | 0.3 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/352915/000119312526071676/0001193125-26-071676-index.htm · estimate; Company-specific estimate of consolidated revenue sensitive to Medicaid patient coverage, not a reported pure managed-care premium ratio. Includes a provider-volume proxy with wide payer-mix uncertainty; does not separately model uncompensated care, state supplemental payments or payer substitution. Hospital/service mix differs from insurers. · Company-specific estimate of consolidated revenue sensitive to Medicaid patient coverage, not a reported pure managed-care premium ratio. Includes a provider-volume proxy with wide payer-mix uncertainty; does not separately model uncompensated care, state supplemental payments or payer substitution. Hospital/service mix differs from insurers. |

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
| exposure.medicaid_revenue_share | -0.013551586 | -0.017077194 | 0.0035256081 |
| assumption.retained_share | -0.017420806 | -0.013936645 | 0.0034841612 |

Dominant configured driver: `medicaid_revenue_share` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.


## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 9 unchecked in-scope exposure values; 1 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

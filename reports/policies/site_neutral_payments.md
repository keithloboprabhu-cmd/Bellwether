# Site-neutral payment rules

Policy `healthcare/site_neutral_payments` · reviewed 2026-10-31 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

Site-neutral reimbursement lowers payments for selected Medicare hospital outpatient services. The model captures hospital-provider revenue losses and managed-care claims savings, with separate scope and pass-through assumptions.

Duration: `permanent`. Default inputs: `{"rate_cut_pct": 30.0}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| cost | ['managed_care'] / unavailable | {"exposed_cost_share": "exposure.hospital_outpatient_cost_share", "shock_pct": "-input.rate_cut_pct / 100 * assumption.eligible_share", "pass_through": "assumption.pass_through"} |
| price | ['standard'] / unavailable | {"d_price": "-input.rate_cut_pct / 100 * assumption.eligible_share", "exposed_revenue_share": "exposure.hospital_outpatient_medicare_revenue_share"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://www.sec.gov/Archives/edgar/data/1156039/000115603926000013/R28.htm
- https://www.sec.gov/Archives/edgar/data/70318/000007031826000012/thc-20251231.htm
- https://www.cms.gov/files/document/2026-nfrm-opps-claims-accounting.pdf

| Company | Configured status | Basis |
|---|---|---|
| UNH | included | Lower hospital outpatient payments hurt providers and lower insurers claims cost. |
| ELV | included | Lower hospital outpatient payments hurt providers and lower insurers claims cost. |
| HUM | included | Lower hospital outpatient payments hurt providers and lower insurers claims cost. |
| CVS | included | Lower hospital outpatient payments hurt providers and lower insurers claims cost. |
| PFE | outside_scope | Only payer hospital-outpatient claims savings and provider Medicare outpatient losses are modeled; device and drug revenue is not a hospital payment. |
| LLY | outside_scope | Only payer hospital-outpatient claims savings and provider Medicare outpatient losses are modeled; device and drug revenue is not a hospital payment. |
| CI | included | Lower hospital outpatient payments hurt providers and lower insurers claims cost. |
| CNC | included | Lower hospital outpatient payments hurt providers and lower insurers claims cost. |
| MOH | included | Lower hospital outpatient payments hurt providers and lower insurers claims cost. |
| JNJ | outside_scope | Only payer hospital-outpatient claims savings and provider Medicare outpatient losses are modeled; device and drug revenue is not a hospital payment. |
| MRK | outside_scope | Only payer hospital-outpatient claims savings and provider Medicare outpatient losses are modeled; device and drug revenue is not a hospital payment. |
| ABBV | outside_scope | Only payer hospital-outpatient claims savings and provider Medicare outpatient losses are modeled; device and drug revenue is not a hospital payment. |
| AMGN | outside_scope | Only payer hospital-outpatient claims savings and provider Medicare outpatient losses are modeled; device and drug revenue is not a hospital payment. |
| GILD | outside_scope | Only payer hospital-outpatient claims savings and provider Medicare outpatient losses are modeled; device and drug revenue is not a hospital payment. |
| HCA | included | Lower hospital outpatient payments hurt providers and lower insurers claims cost. |
| THC | included | Lower hospital outpatient payments hurt providers and lower insurers claims cost. |
| UHS | included | Lower hospital outpatient payments hurt providers and lower insurers claims cost. |
| TMO | outside_scope | Only payer hospital-outpatient claims savings and provider Medicare outpatient losses are modeled; device and drug revenue is not a hospital payment. |
| ABT | outside_scope | Only payer hospital-outpatient claims savings and provider Medicare outpatient losses are modeled; device and drug revenue is not a hospital payment. |
| MDT | outside_scope | Only payer hospital-outpatient claims savings and provider Medicare outpatient losses are modeled; device and drug revenue is not a hospital payment. |
| CAH | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| COR | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| ISRG | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| MCK | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |

## B. Every in-scope exposure

Exact numeric checks are distinguished from filing links and estimates. UNVERIFIED values are retained, not silently replaced. Historical observed low/high values are not forecast confidence intervals.

| Company | Exposure | Base | Low | High | Exact-source status | Primary source / location / rationale |
|---|---|---:|---:|---:|---|---|
| UNH | hospital_outpatient_cost_share | 0.13 | 0.1 | 0.16 | UNVERIFIED | No source URL · estimate; Medical claims are roughly three-quarters of UNH cost of revenue (the rest is Optum Rx drug cost); hospital outpatient is ~15–20% of medical claims. · Medical claims are roughly three-quarters of UNH cost of revenue (the rest is Optum Rx drug cost); hospital outpatient is ~15–20% of medical claims. |
| UNH | hospital_outpatient_medicare_revenue_share | 0 | 0 | 0 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/731766/000073176626000062/0000731766-26-000062-index.htm · estimate; Direct provider scope estimate: no consolidated hospital outpatient billing book modeled; insurer claims savings use a separate channel. Not a reported zero measurement. · Direct provider scope estimate: no consolidated hospital outpatient billing book modeled; insurer claims savings use a separate channel. Not a reported zero measurement. |
| ELV | hospital_outpatient_cost_share | 0.15 | 0.12 | 0.18 | UNVERIFIED | No source URL · estimate; Benefit expense is most of ELV cost of revenue (premiums $164,639M of $197,584M operating revenue); hospital outpatient is ~15–20% of medical claims. · Benefit expense is most of ELV cost of revenue (premiums $164,639M of $197,584M operating revenue); hospital outpatient is ~15–20% of medical claims. |
| ELV | hospital_outpatient_medicare_revenue_share | 0 | 0 | 0 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1156039/000115603926000013/0001156039-26-000013-index.htm · estimate; Direct provider scope estimate: no consolidated hospital outpatient billing book modeled; insurer claims savings use a separate channel. Not a reported zero measurement. · Direct provider scope estimate: no consolidated hospital outpatient billing book modeled; insurer claims savings use a separate channel. Not a reported zero measurement. |
| HUM | hospital_outpatient_cost_share | 0.13 | 0.1 | 0.16 | UNVERIFIED | No source URL · estimate; Cost of revenue is almost all benefit expense (~85% of revenue); hospital outpatient is ~15% of MA medical claims. · Cost of revenue is almost all benefit expense (~85% of revenue); hospital outpatient is ~15% of MA medical claims. |
| HUM | hospital_outpatient_medicare_revenue_share | 0 | 0 | 0 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/49071/000004907126000009/0000049071-26-000009-index.htm · estimate; Direct provider scope estimate: no consolidated hospital outpatient billing book modeled; insurer claims savings use a separate channel. Not a reported zero measurement. · Direct provider scope estimate: no consolidated hospital outpatient billing book modeled; insurer claims savings use a separate channel. Not a reported zero measurement. |
| CVS | hospital_outpatient_cost_share | 0.06 | 0.04 | 0.08 | UNVERIFIED | No source URL · estimate; Most CVS cost of revenue is drug cost; HCB benefit costs (~$120B on $134,749M premiums) are ~35% of the $346,705M total, and hospital outpatient is ~15–20% of those. · Most CVS cost of revenue is drug cost; HCB benefit costs (~$120B on $134,749M premiums) are ~35% of the $346,705M total, and hospital outpatient is ~15–20% of those. |
| CVS | hospital_outpatient_medicare_revenue_share | 0 | 0 | 0 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/64803/000006480326000010/0000064803-26-000010-index.htm · estimate; Direct provider scope estimate: no consolidated hospital outpatient billing book modeled; insurer claims savings use a separate channel. Not a reported zero measurement. · Direct provider scope estimate: no consolidated hospital outpatient billing book modeled; insurer claims savings use a separate channel. Not a reported zero measurement. |
| CI | hospital_outpatient_cost_share | 0.13 | 0.04 | 0.18 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Managed care; median base and outer low/high from UNH/ELV/HUM/CVS in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Managed care; median base and outer low/high from UNH/ELV/HUM/CVS in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| CI | hospital_outpatient_medicare_revenue_share | 0 | 0 | 0 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1739940/000173994026000006/0001739940-26-000006-index.htm · estimate; Direct provider scope estimate: no consolidated hospital outpatient billing book modeled; insurer claims savings use a separate channel. Not a reported zero measurement. · Direct provider scope estimate: no consolidated hospital outpatient billing book modeled; insurer claims savings use a separate channel. Not a reported zero measurement. |
| CNC | hospital_outpatient_cost_share | 0.13 | 0.04 | 0.18 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Managed care; median base and outer low/high from UNH/ELV/HUM/CVS in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Managed care; median base and outer low/high from UNH/ELV/HUM/CVS in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| CNC | hospital_outpatient_medicare_revenue_share | 0 | 0 | 0 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1071739/000107173926000049/0001071739-26-000049-index.htm · estimate; Direct provider scope estimate: no consolidated hospital outpatient billing book modeled; insurer claims savings use a separate channel. Not a reported zero measurement. · Direct provider scope estimate: no consolidated hospital outpatient billing book modeled; insurer claims savings use a separate channel. Not a reported zero measurement. |
| MOH | hospital_outpatient_cost_share | 0.13 | 0.04 | 0.18 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Managed care; median base and outer low/high from UNH/ELV/HUM/CVS in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Managed care; median base and outer low/high from UNH/ELV/HUM/CVS in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| MOH | hospital_outpatient_medicare_revenue_share | 0 | 0 | 0 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1179929/000117992926000005/0001179929-26-000005-index.htm · estimate; Direct provider scope estimate: no consolidated hospital outpatient billing book modeled; insurer claims savings use a separate channel. Not a reported zero measurement. · Direct provider scope estimate: no consolidated hospital outpatient billing book modeled; insurer claims savings use a separate channel. Not a reported zero measurement. |
| HCA | hospital_outpatient_cost_share | 0 | 0 | 0 | UNVERIFIED | No source URL · estimate; Explicit scope estimate: Hospitals is outside this direct policy channel; indirect effects are not modeled. This is not a reported zero exposure. · Explicit scope estimate: Hospitals is outside this direct policy channel; indirect effects are not modeled. This is not a reported zero exposure. |
| HCA | hospital_outpatient_medicare_revenue_share | 0.08 | 0.04 | 0.12 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm · estimate; Company-specific estimate of Medicare hospital outpatient revenue as a share of consolidated revenue; payer-by-setting cross-tab is not disclosed. Excludes inpatient care and standalone ambulatory surgery centers. Wide range reflects service/payer mix; the policy separately limits eligible services. · Company-specific estimate of Medicare hospital outpatient revenue as a share of consolidated revenue; payer-by-setting cross-tab is not disclosed. Excludes inpatient care and standalone ambulatory surgery centers. Wide range reflects service/payer mix; the policy separately limits eligible services. |
| THC | hospital_outpatient_cost_share | 0 | 0 | 0 | UNVERIFIED | No source URL · estimate; Explicit scope estimate: Hospitals is outside this direct policy channel; indirect effects are not modeled. This is not a reported zero exposure. · Explicit scope estimate: Hospitals is outside this direct policy channel; indirect effects are not modeled. This is not a reported zero exposure. |
| THC | hospital_outpatient_medicare_revenue_share | 0.045 | 0.02 | 0.08 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/70318/000007031826000012/0000070318-26-000012-index.htm · estimate; Company-specific estimate of Medicare hospital outpatient revenue as a share of consolidated revenue; payer-by-setting cross-tab is not disclosed. Excludes inpatient care and standalone ambulatory surgery centers. Wide range reflects service/payer mix; the policy separately limits eligible services. · Company-specific estimate of Medicare hospital outpatient revenue as a share of consolidated revenue; payer-by-setting cross-tab is not disclosed. Excludes inpatient care and standalone ambulatory surgery centers. Wide range reflects service/payer mix; the policy separately limits eligible services. |
| UHS | hospital_outpatient_cost_share | 0 | 0 | 0 | UNVERIFIED | No source URL · estimate; Explicit scope estimate: Hospitals is outside this direct policy channel; indirect effects are not modeled. This is not a reported zero exposure. · Explicit scope estimate: Hospitals is outside this direct policy channel; indirect effects are not modeled. This is not a reported zero exposure. |
| UHS | hospital_outpatient_medicare_revenue_share | 0.04 | 0.02 | 0.08 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/352915/000119312526071676/0001193125-26-071676-index.htm · estimate; Company-specific estimate of Medicare hospital outpatient revenue as a share of consolidated revenue; payer-by-setting cross-tab is not disclosed. Excludes inpatient care and standalone ambulatory surgery centers. Wide range reflects service/payer mix; the policy separately limits eligible services. · Company-specific estimate of Medicare hospital outpatient revenue as a share of consolidated revenue; payer-by-setting cross-tab is not disclosed. Excludes inpatient care and standalone ambulatory surgery centers. Wide range reflects service/payer mix; the policy separately limits eligible services. |

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
| assumption.pass_through | 0.022139121 | 0.0043942674 | 0.017744853 |
| assumption.eligible_share | 0.008187246 | 0.024561738 | 0.016374492 |
| exposure.hospital_outpatient_cost_share | 0.0068330476 | 0.016293184 | 0.009460136 |
| exposure.hospital_outpatient_medicare_revenue_share | 0.013049071 | 0.011404249 | 0.001644822 |

Dominant configured driver: `pass_through` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.


## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 20 unchecked in-scope exposure values; 2 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

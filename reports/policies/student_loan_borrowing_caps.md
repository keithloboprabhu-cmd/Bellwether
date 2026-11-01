# Graduate student loan caps (end of Grad PLUS)

Policy `education/student_loan_borrowing_caps` · reviewed 2026-10-31 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

The 2025 reconciliation law (P.L. 119-21) ended Grad PLUS for new borrowers and set new annual, aggregate and lifetime caps on federal graduate and professional loans from July 1, 2026. Schools whose students borrowed beyond the caps lose some enrollment and must hold down tuition. Covista's Caribbean medical schools and Walden are the most exposed, then Strategic Education's Capella and Grand Canyon.

Duration: `permanent`. Default inputs: `{"affected_pct": 60.0}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| demand_volume | unavailable / unavailable | {"d_volume": "-input.affected_pct / 100 * assumption.lost_enrollment", "exposed_revenue_share": "exposure.grad_plus_dependent_revenue_share"} |
| price | unavailable / unavailable | {"d_price": "-input.affected_pct / 100 * assumption.price_concession * (1 - assumption.lost_enrollment)", "exposed_revenue_share": "exposure.grad_plus_dependent_revenue_share"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://www.nber.org/papers/w31291
- https://freopp.org/?p=3907
- https://www.sec.gov/Archives/edgar/data/730464/000110465926092044/cvsa-20260630x10k.htm

| Company | Configured status | Basis |
|---|---|---|
| LRN | outside_scope | Grad PLUS limits cover US graduate/professional programs or service partners; undergraduate vocational programs and private lenders do not inherit graduate tuition. |
| LOPE | included | Graduate borrowing limits reduce funded graduate tuition. |
| CVSA | included | Graduate borrowing limits reduce funded graduate tuition. |
| STRA | included | Graduate borrowing limits reduce funded graduate tuition. |
| DUOL | outside_scope | Grad PLUS limits cover US graduate/professional programs or service partners; undergraduate vocational programs and private lenders do not inherit graduate tuition. |
| COUR | included | Graduate borrowing limits reduce funded graduate tuition. |
| UTI | outside_scope | Grad PLUS limits cover US graduate/professional programs or service partners; undergraduate vocational programs and private lenders do not inherit graduate tuition. |
| PRDO | included | Graduate borrowing limits reduce funded graduate tuition. |
| APEI | included | Graduate borrowing limits reduce funded graduate tuition. |
| LAUR | outside_scope | Grad PLUS limits cover US graduate/professional programs or service partners; undergraduate vocational programs and private lenders do not inherit graduate tuition. |
| NRDY | outside_scope | Grad PLUS limits cover US graduate/professional programs or service partners; undergraduate vocational programs and private lenders do not inherit graduate tuition. |
| LINC | outside_scope | Grad PLUS limits cover US graduate/professional programs or service partners; undergraduate vocational programs and private lenders do not inherit graduate tuition. |
| SKIL | outside_scope | Grad PLUS limits cover US graduate/professional programs or service partners; undergraduate vocational programs and private lenders do not inherit graduate tuition. |
| CHGG | outside_scope | Grad PLUS limits cover US graduate/professional programs or service partners; undergraduate vocational programs and private lenders do not inherit graduate tuition. |
| SCHL | outside_scope | Grad PLUS limits cover US graduate/professional programs or service partners; undergraduate vocational programs and private lenders do not inherit graduate tuition. |
| KLC | outside_scope | Grad PLUS limits cover US graduate/professional programs or service partners; undergraduate vocational programs and private lenders do not inherit graduate tuition. |
| BFAM | outside_scope | Grad PLUS limits cover US graduate/professional programs or service partners; undergraduate vocational programs and private lenders do not inherit graduate tuition. |
| WLY | outside_scope | Grad PLUS limits cover US graduate/professional programs or service partners; undergraduate vocational programs and private lenders do not inherit graduate tuition. |
| FC | outside_scope | Grad PLUS limits cover US graduate/professional programs or service partners; undergraduate vocational programs and private lenders do not inherit graduate tuition. |
| SLM | outside_scope | Grad PLUS limits cover US graduate/professional programs or service partners; undergraduate vocational programs and private lenders do not inherit graduate tuition. |

## B. Every in-scope exposure

Exact numeric checks are distinguished from filing links and estimates. UNVERIFIED values are retained, not silently replaced. Historical observed low/high values are not forecast confidence intervals.

| Company | Exposure | Base | Low | High | Exact-source status | Primary source / location / rationale |
|---|---|---:|---:|---:|---|---|
| LOPE | grad_plus_dependent_revenue_share | 0.06 | 0.03 | 0.1 | UNVERIFIED | No source URL · estimate; GCU (89.5% of LOPE service revenue per the FY2025 10-K) enrolls many online master's and doctoral students in education, nursing and business; assumes ~30-35% of service revenue is from graduate students and ~20% of that from students who borrowed beyond the new caps through Grad PLUS. The degree-level split is not disclosed in the text read. · GCU (89.5% of LOPE service revenue per the FY2025 10-K) enrolls many online master's and doctoral students in education, nursing and business; assumes ~30-35% of service revenue is from graduate students and ~20% of that from students who borrowed beyond the new caps through Grad PLUS. The degree-level split is not disclosed in the text read. |
| CVSA | grad_plus_dependent_revenue_share | 0.25 | 0.15 | 0.35 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/730464/000110465926092044/cvsa-20260630x10k.htm · estimate; Covista FY2026 10-K: Medical & Veterinary revenue $398.9M (20%) from Caribbean medical and veterinary schools whose cost of attendance far exceeds the new professional-student loan limits; Walden $804.9M (41%) is mostly online master's and doctoral programs. The 10-K says the 2025 law's new annual/aggregate/lifetime limits and the end of Grad PLUS 'may materially reduce the amount of loan funding available to students'. Assumes ~70% of medical/vet and ~20-25% of Walden revenue depends on above-cap borrowing. · Covista FY2026 10-K: Medical & Veterinary revenue $398.9M (20%) from Caribbean medical and veterinary schools whose cost of attendance far exceeds the new professional-student loan limits; Walden $804.9M (41%) is mostly online master's and doctoral programs. The 10-K says the 2025 law's new annual/aggregate/lifetime limits and the end of Grad PLUS 'may materially reduce the amount of loan funding available to students'. Assumes ~70% of medical/vet and ~20-25% of Walden revenue depends on above-cap borrowing. |
| STRA | grad_plus_dependent_revenue_share | 0.07 | 0.04 | 0.12 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1013934/000101393426000006/stra-20251231.htm · estimate; Strategic Education 2025 10-K: US Higher Education revenue $868.2M (68% of $1,268.2M) from Capella and Strayer. Capella is mostly online master's and doctoral students; Strayer is mostly undergraduate. Assumes Capella is ~half of USHE, ~70% of it graduate, and ~25-30% of that from students who borrowed beyond the new caps. · Strategic Education 2025 10-K: US Higher Education revenue $868.2M (68% of $1,268.2M) from Capella and Strayer. Capella is mostly online master's and doctoral students; Strayer is mostly undergraduate. Assumes Capella is ~half of USHE, ~70% of it graduate, and ~25-30% of that from students who borrowed beyond the new caps. |
| COUR | grad_plus_dependent_revenue_share | 0.01 | 0 | 0.02 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1651562/000165156226000015/cour-20251231.htm · estimate; Coursera 2025 10-K: offers 50+ online degrees with university partners; some US master's students borrow federal loans at the partner university, and Coursera's revenue share of those degrees falls if enrolment does. Degrees are a small part of the $502.2M Consumer segment. · Coursera 2025 10-K: offers 50+ online degrees with university partners; some US master's students borrow federal loans at the partner university, and Coursera's revenue share of those degrees falls if enrolment does. Degrees are a small part of the $502.2M Consumer segment. |
| PRDO | grad_plus_dependent_revenue_share | 0.07 | 0.03 | 0.35 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| APEI | grad_plus_dependent_revenue_share | 0.07 | 0.03 | 0.35 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |

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
| exposure.grad_plus_dependent_revenue_share | -0.0096878611 | -0.03443737 | 0.024749508 |
| assumption.lost_enrollment | -0.010418038 | -0.027672105 | 0.017254067 |
| assumption.price_concession | -0.011397524 | -0.025610662 | 0.014213138 |

Dominant configured driver: `grad_plus_dependent_revenue_share` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.


## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 6 unchecked in-scope exposure values; 2 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

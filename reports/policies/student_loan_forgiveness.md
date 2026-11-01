# Student loan forgiveness

Policy `education/student_loan_forgiveness` · reviewed 2026-10-31 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

Cancelling federal student debt frees up borrowers' monthly payments, a small boost to household spending that reaches these companies only through their tiny share of all US consumer spending. Exposure in this universe is very small; the effect on future enrollment and borrowing behaviour is not modelled.

Duration: `years:10`. Default inputs: `{"forgiven_bn": 50.0}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| demand_transfer | unavailable / unavailable | {"total_transfer_musd": "input.forgiven_bn * 1000 * assumption.payment_rate", "mpc": "assumption.mpc", "capture_share": "baseline.revenue * exposure.us_consumer_revenue_share / macro.pce_musd"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://www.nber.org/papers/w31291

| Company | Configured status | Basis |
|---|---|---|
| LRN | included | Household transfer proxy increases discretionary education demand; not lender debt cancellation. |
| LOPE | included | Household transfer proxy increases discretionary education demand; not lender debt cancellation. |
| CVSA | included | Household transfer proxy increases discretionary education demand; not lender debt cancellation. |
| STRA | included | Household transfer proxy increases discretionary education demand; not lender debt cancellation. |
| DUOL | included | Household transfer proxy increases discretionary education demand; not lender debt cancellation. |
| COUR | included | Household transfer proxy increases discretionary education demand; not lender debt cancellation. |
| UTI | included | Household transfer proxy increases discretionary education demand; not lender debt cancellation. |
| PRDO | included | Household transfer proxy increases discretionary education demand; not lender debt cancellation. |
| APEI | included | Household transfer proxy increases discretionary education demand; not lender debt cancellation. |
| LAUR | outside_scope | Laureate operates continuing institutions in Mexico/Peru. Sallie Mae earns private-loan revenue. Neither is allocated US household education purchases in this scenario. |
| NRDY | included | Household transfer proxy increases discretionary education demand; not lender debt cancellation. |
| LINC | included | Household transfer proxy increases discretionary education demand; not lender debt cancellation. |
| SKIL | included | Household transfer proxy increases discretionary education demand; not lender debt cancellation. |
| CHGG | included | Household transfer proxy increases discretionary education demand; not lender debt cancellation. |
| SCHL | included | Household transfer proxy increases discretionary education demand; not lender debt cancellation. |
| KLC | included | Household transfer proxy increases discretionary education demand; not lender debt cancellation. |
| BFAM | included | Household transfer proxy increases discretionary education demand; not lender debt cancellation. |
| WLY | included | Household transfer proxy increases discretionary education demand; not lender debt cancellation. |
| FC | included | Household transfer proxy increases discretionary education demand; not lender debt cancellation. |
| SLM | outside_scope | Laureate operates continuing institutions in Mexico/Peru. Sallie Mae earns private-loan revenue. Neither is allocated US household education purchases in this scenario. |

## B. Every in-scope exposure

Exact numeric checks are distinguished from filing links and estimates. UNVERIFIED values are retained, not silently replaced. Historical observed low/high values are not forecast confidence intervals.

| Company | Exposure | Base | Low | High | Exact-source status | Primary source / location / rationale |
|---|---|---:|---:|---:|---|---|
| LRN | us_consumer_revenue_share | 0.03 | 0.01 | 0.05 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1157408/000110465926090515/lrn-20260630x10k.htm · estimate; Stride FY2026 10-K: 96% of General Education and 100% of middle/high school Career Learning revenue comes from funding-based contracts with schools (state/district money, not household spending). Household-paid revenue is private-school tuition and adult learning ($56.6M), about 2-4% of revenue. · Stride FY2026 10-K: 96% of General Education and 100% of middle/high school Career Learning revenue comes from funding-based contracts with schools (state/district money, not household spending). Household-paid revenue is private-school tuition and adult learning ($56.6M), about 2-4% of revenue. |
| LOPE | us_consumer_revenue_share | 0.9 | 0.8 | 0.95 | UNVERIFIED | No source URL · estimate; Service revenue is a share of US partner universities' tuition, which US students and families pay (with federal aid); treated as US household education spending. · Service revenue is a share of US partner universities' tuition, which US students and families pay (with federal aid); treated as US household education spending. |
| CVSA | us_consumer_revenue_share | 0.95 | 0.85 | 0.98 | UNVERIFIED | No source URL · estimate; Tuition paid by (mostly US) students with their own money and federal aid; the Caribbean medical and veterinary schools enrol mainly US students. · Tuition paid by (mostly US) students with their own money and federal aid; the Caribbean medical and veterinary schools enrol mainly US students. |
| STRA | us_consumer_revenue_share | 0.7 | 0.62 | 0.75 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1013934/000101393426000006/stra-20251231.htm · estimate; Strategic Education 2025 10-K: USHE revenue $868.2M (68%) is US students' tuition; Sophia subscriptions add a little; Workforce Edge is paid by employers and ANZ is outside the US. · Strategic Education 2025 10-K: USHE revenue $868.2M (68%) is US students' tuition; Sophia subscriptions add a little; Workforce Edge is paid by employers and ANZ is outside the US. |
| DUOL | us_consumer_revenue_share | 0.38 | 0.33 | 0.38 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1562088/000162828026012494/duol-20251231.htm · Duolingo 2025 10-K: customers located in the United States were 38% of total revenue ($392.2M of $1,037.6M); Low end allows for US advertising revenue paid by businesses rather than consumers. · Low end allows for US advertising revenue paid by businesses rather than consumers. |
| COUR | us_consumer_revenue_share | 0.34 | 0.25 | 0.45 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1651562/000165156226000015/cour-20251231.htm · Coursera 2025 10-K: United States revenue $384.7M of $757.5M (51%); Consumer segment $502.2M of $757.5M (66%); The US consumer split is not disclosed; assumes the US share of Consumer revenue matches the company-wide US share (51% × 66% ≈ 34%). · The US consumer split is not disclosed; assumes the US share of Consumer revenue matches the company-wide US share (51% × 66% ≈ 34%). |
| UTI | us_consumer_revenue_share | 0.9 | 0.62 | 0.98 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| PRDO | us_consumer_revenue_share | 0.9 | 0.62 | 0.98 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| APEI | us_consumer_revenue_share | 0.9 | 0.62 | 0.98 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| NRDY | us_consumer_revenue_share | 0.36 | 0.25 | 0.45 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Digital learning and training; median base and outer low/high from DUOL/COUR in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Digital learning and training; median base and outer low/high from DUOL/COUR in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| LINC | us_consumer_revenue_share | 0.9 | 0.62 | 0.98 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| SKIL | us_consumer_revenue_share | 0.36 | 0.25 | 0.45 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Digital learning and training; median base and outer low/high from DUOL/COUR in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Digital learning and training; median base and outer low/high from DUOL/COUR in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| CHGG | us_consumer_revenue_share | 0.36 | 0.25 | 0.45 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Digital learning and training; median base and outer low/high from DUOL/COUR in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Digital learning and training; median base and outer low/high from DUOL/COUR in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| SCHL | us_consumer_revenue_share | 0.34 | 0.01 | 0.45 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Publishing and childcare; median base and outer low/high from LRN/DUOL/COUR in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Publishing and childcare; median base and outer low/high from LRN/DUOL/COUR in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| KLC | us_consumer_revenue_share | 0.34 | 0.01 | 0.45 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Publishing and childcare; median base and outer low/high from LRN/DUOL/COUR in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Publishing and childcare; median base and outer low/high from LRN/DUOL/COUR in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| BFAM | us_consumer_revenue_share | 0.34 | 0.01 | 0.45 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Publishing and childcare; median base and outer low/high from LRN/DUOL/COUR in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Publishing and childcare; median base and outer low/high from LRN/DUOL/COUR in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| WLY | us_consumer_revenue_share | 0.34 | 0.01 | 0.45 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Publishing and childcare; median base and outer low/high from LRN/DUOL/COUR in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Publishing and childcare; median base and outer low/high from LRN/DUOL/COUR in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| FC | us_consumer_revenue_share | 0.36 | 0.25 | 0.45 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Digital learning and training; median base and outer low/high from DUOL/COUR in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Digital learning and training; median base and outer low/high from DUOL/COUR in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |

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
| assumption.payment_rate | 8.6265277e-05 | 0.00023722951 | 0.00015096423 |
| assumption.mpc | 0.00010064282 | 0.00020128565 | 0.00010064282 |
| exposure.us_consumer_revenue_share | 9.4256741e-05 | 0.00017201988 | 7.7763142e-05 |

Dominant configured driver: `payment_rate` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.


## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 18 unchecked in-scope exposure values; 2 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

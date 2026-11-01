# School choice expansion (ESAs, vouchers, tax-credit scholarships)

Policy `education/school_choice_esa` · evidence checkpoint 2026-11-01 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

New or larger education savings account, voucher and tax-credit scholarship programs give families public money to spend on private schooling and curriculum. Stride's tuition-based online private schools accept these funds, so it gains a little; the higher-ed and consumer-app companies are not affected. Exposure in this universe is small.

Duration: `permanent`. Default inputs: `{"new_choice_spending_bn": 5.0}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| demand_transfer | unavailable / unavailable | {"total_transfer_musd": "input.new_choice_spending_bn * 1000", "mpc": "assumption.spend_share", "capture_share": "exposure.esa_capture_share"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://www.edchoice.org/2026-edchoice-participation-rankings/
- https://www.sec.gov/Archives/edgar/data/1157408/000110465926090515/lrn-20260630x10k.htm

| Company | Configured status | Basis |
|---|---|---|
| LRN | included | ESA funding raises eligible education spending. |
| LOPE | outside_scope | This allocation covers modeled K–12 school/tutoring providers, not higher education tuition or general consumer apps. |
| CVSA | outside_scope | This allocation covers modeled K–12 school/tutoring providers, not higher education tuition or general consumer apps. |
| STRA | outside_scope | This allocation covers modeled K–12 school/tutoring providers, not higher education tuition or general consumer apps. |
| DUOL | outside_scope | This allocation covers modeled K–12 school/tutoring providers, not higher education tuition or general consumer apps. |
| COUR | outside_scope | This allocation covers modeled K–12 school/tutoring providers, not higher education tuition or general consumer apps. |
| UTI | outside_scope | This allocation covers modeled K–12 school/tutoring providers, not higher education tuition or general consumer apps. |
| PRDO | outside_scope | This allocation covers modeled K–12 school/tutoring providers, not higher education tuition or general consumer apps. |
| APEI | outside_scope | This allocation covers modeled K–12 school/tutoring providers, not higher education tuition or general consumer apps. |
| LAUR | outside_scope | This allocation covers modeled K–12 school/tutoring providers, not higher education tuition or general consumer apps. |
| NRDY | included | ESA funding raises eligible education spending. |
| LINC | outside_scope | This allocation covers modeled K–12 school/tutoring providers, not higher education tuition or general consumer apps. |
| SKIL | outside_scope | This allocation covers modeled K–12 school/tutoring providers, not higher education tuition or general consumer apps. |
| CHGG | outside_scope | This allocation covers modeled K–12 school/tutoring providers, not higher education tuition or general consumer apps. |
| SCHL | unquantified | No quantified central exposure. The high sensitivity case represents uncertain qualifying state ESA services/materials capture; eligibility/provider approval and awards require verification. |
| KLC | unquantified | No quantified central exposure. The high sensitivity case represents uncertain qualifying state ESA services/materials capture; eligibility/provider approval and awards require verification. |
| BFAM | unquantified | No quantified central exposure. The high sensitivity case represents uncertain qualifying state ESA services/materials capture; eligibility/provider approval and awards require verification. |
| WLY | outside_scope | This allocation covers modeled K–12 school/tutoring providers, not higher education tuition or general consumer apps. |
| FC | outside_scope | This allocation covers modeled K–12 school/tutoring providers, not higher education tuition or general consumer apps. |
| SLM | outside_scope | This allocation covers modeled K–12 school/tutoring providers, not higher education tuition or general consumer apps. |

## B. Every in-scope exposure

Exact numeric checks are distinguished from filing links and estimates. UNVERIFIED values are retained, not silently replaced. Historical observed low/high values are not forecast confidence intervals.

| Company | Exposure | Base | Low | High | Exact-source status | Primary source / location / rationale |
|---|---|---:|---:|---:|---|---|
| LRN | esa_capture_share | 0.005 | 0.001 | 0.015 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1157408/000110465926090515/lrn-20260630x10k.htm · estimate; Stride FY2026 10-K: its tuition-based online private schools accept education savings accounts, tax credits and vouchers, and 96% of General Education revenue ($1,417.8M) is from funding-based public contracts, so private-pay and curriculum sales are only ~$57M. Online private schools are a niche among the private schools ESA families choose, so Stride captures well under 1% of new choice dollars. · Stride FY2026 10-K: its tuition-based online private schools accept education savings accounts, tax credits and vouchers, and 96% of General Education revenue ($1,417.8M) is from funding-based public contracts, so private-pay and curriculum sales are only ~$57M. Online private schools are a niche among the private schools ESA families choose, so Stride captures well under 1% of new choice dollars. |
| NRDY | esa_capture_share | 0.001 | 0 | 0.003 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1819404/000181940426000015/0001819404-26-000015-index.htm · estimate; Company-specific estimate: Varsity Tutors can serve K–12 tutoring demand. Estimate 0.1% of incremental ESA spending (0–0.3%); state eligibility, provider approval and competition matter. Not a measured market share. · Company-specific estimate: Varsity Tutors can serve K–12 tutoring demand. Estimate 0.1% of incremental ESA spending (0–0.3%); state eligibility, provider approval and competition matter. Not a measured market share. |

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
| exposure.esa_capture_share | 0.00052572328 | 0.014304482 | 0.013778759 |
| assumption.spend_share | 0.0030758569 | 0.0038448212 | 0.00076896424 |

Dominant configured driver: `esa_capture_share` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.


## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 2 unchecked in-scope exposure values; 1 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

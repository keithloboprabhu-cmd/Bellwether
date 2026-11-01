# Pell Grant cut or increase

Policy `education/pell_grant_change` · evidence checkpoint 2026-11-01 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

A change in the maximum Pell Grant changes how much need-based federal aid low-income undergraduates bring to college. Many make up a cut with loans, but some drop out or enrol part-time. Strategic Education (Strayer) and Grand Canyon have the most Pell-funded undergraduates; Duolingo, Coursera and Stride are untouched.

Duration: `permanent`. Default inputs: `{"pell_change_pct": -10.0}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| demand_volume | unavailable / unavailable | {"d_volume": "input.pell_change_pct / 100 * (1 - assumption.loan_substitution)", "exposed_revenue_share": "exposure.pell_revenue_share"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://www.sec.gov/Archives/edgar/data/1013934/000101393426000006/stra-20251231.htm
- https://www.sec.gov/Archives/edgar/data/730464/000110465926092044/cvsa-20260630x10k.htm

| Company | Configured status | Basis |
|---|---|---|
| LRN | outside_scope | Pell enrollment exposure requires US Title IV undergraduate programs or an explicitly modeled service partner. |
| LOPE | included | Default grant reduction lowers funded undergraduate enrollment. |
| CVSA | included | Default grant reduction lowers funded undergraduate enrollment. |
| STRA | included | Default grant reduction lowers funded undergraduate enrollment. |
| DUOL | outside_scope | Pell enrollment exposure requires US Title IV undergraduate programs or an explicitly modeled service partner. |
| COUR | outside_scope | Pell enrollment exposure requires US Title IV undergraduate programs or an explicitly modeled service partner. |
| UTI | included | Default grant reduction lowers funded undergraduate enrollment. |
| PRDO | included | Default grant reduction lowers funded undergraduate enrollment. |
| APEI | included | Default grant reduction lowers funded undergraduate enrollment. |
| LAUR | outside_scope | Pell enrollment exposure requires US Title IV undergraduate programs or an explicitly modeled service partner. |
| NRDY | outside_scope | Pell enrollment exposure requires US Title IV undergraduate programs or an explicitly modeled service partner. |
| LINC | included | Default grant reduction lowers funded undergraduate enrollment. |
| SKIL | outside_scope | Pell enrollment exposure requires US Title IV undergraduate programs or an explicitly modeled service partner. |
| CHGG | outside_scope | Pell enrollment exposure requires US Title IV undergraduate programs or an explicitly modeled service partner. |
| SCHL | outside_scope | Pell enrollment exposure requires US Title IV undergraduate programs or an explicitly modeled service partner. |
| KLC | outside_scope | Pell enrollment exposure requires US Title IV undergraduate programs or an explicitly modeled service partner. |
| BFAM | outside_scope | Pell enrollment exposure requires US Title IV undergraduate programs or an explicitly modeled service partner. |
| WLY | outside_scope | Pell enrollment exposure requires US Title IV undergraduate programs or an explicitly modeled service partner. |
| FC | outside_scope | Pell enrollment exposure requires US Title IV undergraduate programs or an explicitly modeled service partner. |
| SLM | outside_scope | Pell enrollment exposure requires US Title IV undergraduate programs or an explicitly modeled service partner. |

## B. Every in-scope exposure

Exact numeric checks are distinguished from filing links and estimates. UNVERIFIED values are retained, not silently replaced. Historical observed low/high values are not forecast confidence intervals.

| Company | Exposure | Base | Low | High | Exact-source status | Primary source / location / rationale |
|---|---|---:|---:|---:|---|---|
| LOPE | pell_revenue_share | 0.08 | 0.04 | 0.12 | UNVERIFIED | https://www.highereddive.com/news/grand-canyon-ceo-were-being-selective-in-the-hunt-for-new-partners/572682/ · estimate; GCU's online and ground undergraduates include many Pell recipients. GCU took about 73% of revenue under the 90/10 rule from Title IV, per GCE's quarterly report as quoted by Higher Ed Dive (Feb 2020, stale). Pell is assumed to be a minority of that federal aid, with loans the majority. · GCU's online and ground undergraduates include many Pell recipients. GCU took about 73% of revenue under the 90/10 rule from Title IV, per GCE's quarterly report as quoted by Higher Ed Dive (Feb 2020, stale). Pell is assumed to be a minority of that federal aid, with loans the majority. |
| CVSA | pell_revenue_share | 0.06 | 0.03 | 0.1 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/730464/000110465926092044/cvsa-20260630x10k.htm · estimate; Covista FY2026 10-K: its Title IV institutions get 78% of revenue from federal education assistance, mostly loans. Pell goes only to undergraduates, mainly Chamberlain's pre-licensure BSN and RN-BSN students; Walden and the medical schools are mostly graduate/professional. · Covista FY2026 10-K: its Title IV institutions get 78% of revenue from federal education assistance, mostly loans. Pell goes only to undergraduates, mainly Chamberlain's pre-licensure BSN and RN-BSN students; Walden and the medical schools are mostly graduate/professional. |
| STRA | pell_revenue_share | 0.1 | 0.05 | 0.15 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1013934/000101393426000006/stra-20251231.htm · estimate; Strategic Education 2025 10-K: Strayer University took 89.64% of cash-basis revenue from federal funds in FY2024, and Strayer is mainly an undergraduate school, so Pell is a large part of its revenue. Assumes Pell is ~25% of Strayer's federal funds and Strayer is ~30% of company revenue, with a little Capella undergraduate Pell. · Strategic Education 2025 10-K: Strayer University took 89.64% of cash-basis revenue from federal funds in FY2024, and Strayer is mainly an undergraduate school, so Pell is a large part of its revenue. Assumes Pell is ~25% of Strayer's federal funds and Strayer is ~30% of company revenue, with a little Capella undergraduate Pell. |
| UTI | pell_revenue_share | 0.08 | 0.03 | 0.15 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| PRDO | pell_revenue_share | 0.08 | 0.03 | 0.15 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| APEI | pell_revenue_share | 0.08 | 0.03 | 0.15 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| LINC | pell_revenue_share | 0.08 | 0.03 | 0.15 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |

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
| exposure.pell_revenue_share | -0.0019096729 | -0.0074192381 | 0.0055095653 |
| assumption.loan_substitution | -0.0060541271 | -0.0025946259 | 0.0034595012 |

Dominant configured driver: `pell_revenue_share` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.


## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 7 unchecked in-scope exposure values; 1 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

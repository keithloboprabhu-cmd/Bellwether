# Online education compliance costs

Policy `education/online_compliance_costs` · reviewed 2026-10-31 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

New federal and state rules on distance education (attendance and return-of-aid tracking, state authorization, digital accessibility, subscription cancellation rules) add operating cost for every dollar of online revenue. Fully online Duolingo and Coursera, and largely online Stride and Strategic Education, carry the broadest exposure, though cost relative to their margins varies.

Duration: `permanent`. Default inputs: `{"cost_pct": 0.5}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| cost | unavailable / unavailable | {"exposed_cost_share": 0.0, "shock_pct": 0.0, "dcost_musd": "baseline.revenue * exposure.online_revenue_share * input.cost_pct / 100", "pass_through": "assumption.pass_through", "elasticity": "assumption.elasticity"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://www.sec.gov/Archives/edgar/data/1434588/000110465926017047/lope-20251231x10k.htm

| Company | Configured status | Basis |
|---|---|---|
| LRN | included | Online compliance increases operating costs. |
| LOPE | included | Online compliance increases operating costs. |
| CVSA | included | Online compliance increases operating costs. |
| STRA | included | Online compliance increases operating costs. |
| DUOL | included | Online compliance increases operating costs. |
| COUR | included | Online compliance increases operating costs. |
| UTI | included | Online compliance increases operating costs. |
| PRDO | included | Online compliance increases operating costs. |
| APEI | included | Online compliance increases operating costs. |
| LAUR | outside_scope | This scenario covers US online education activity, excluding foreign institutions, physical childcare centers and lending revenue. |
| NRDY | included | Online compliance increases operating costs. |
| LINC | included | Online compliance increases operating costs. |
| SKIL | included | Online compliance increases operating costs. |
| CHGG | included | Online compliance increases operating costs. |
| SCHL | included | Online compliance increases operating costs. |
| KLC | outside_scope | This scenario covers US online education activity, excluding foreign institutions, physical childcare centers and lending revenue. |
| BFAM | outside_scope | This scenario covers US online education activity, excluding foreign institutions, physical childcare centers and lending revenue. |
| WLY | included | Online compliance increases operating costs. |
| FC | included | Online compliance increases operating costs. |
| SLM | outside_scope | This scenario covers US online education activity, excluding foreign institutions, physical childcare centers and lending revenue. |

## B. Every in-scope exposure

Exact numeric checks are distinguished from filing links and estimates. UNVERIFIED values are retained, not silently replaced. Historical observed low/high values are not forecast confidence intervals.

| Company | Exposure | Base | Low | High | Exact-source status | Primary source / location / rationale |
|---|---|---:|---:|---:|---|---|
| LRN | online_revenue_share | 0.95 | 0.9 | 0.98 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1157408/000110465926090515/lrn-20260630x10k.htm · estimate; Stride FY2026 10-K: served 92 virtual and blended public schools; nearly all revenue is online instruction and curriculum, less blended-school in-person components and adult bootcamp campus programs. · Stride FY2026 10-K: served 92 virtual and blended public schools; nearly all revenue is online instruction and curriculum, less blended-school in-person components and adult bootcamp campus programs. |
| LOPE | online_revenue_share | 0.75 | 0.65 | 0.85 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1434588/000110465926017047/lope-20251231x10k.htm · estimate; Grand Canyon Education 2025 10-K: partner enrollments 136,239 of which GCU 131,826; GCU's traditional ground campus is a minority of enrollment, with most students online (plus 5,738 at off-campus hybrid sites). Revenue split by modality is not disclosed in the text read. · Grand Canyon Education 2025 10-K: partner enrollments 136,239 of which GCU 131,826; GCU's traditional ground campus is a minority of enrollment, with most students online (plus 5,738 at off-campus hybrid sites). Revenue split by modality is not disclosed in the text read. |
| CVSA | online_revenue_share | 0.55 | 0.45 | 0.65 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/730464/000110465926092044/cvsa-20260630x10k.htm · estimate; Covista FY2026 10-K: nearly all of Walden's programs ($804.9M, 41% of revenue) are online; Chamberlain's post-licensure nursing, MPH and MSW are online but its pre-licensure BSN is campus-based; the medical and veterinary schools are campus-based. · Covista FY2026 10-K: nearly all of Walden's programs ($804.9M, 41% of revenue) are online; Chamberlain's post-licensure nursing, MPH and MSW are online but its pre-licensure BSN is campus-based; the medical and veterinary schools are campus-based. |
| STRA | online_revenue_share | 0.75 | 0.65 | 0.82 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1013934/000101393426000006/stra-20251231.htm · estimate; Capella is online and Strayer is mostly online; ETS (Sophia, Workforce Edge) is online. The ANZ segment (Torrens University and other Australia/New Zealand institutions) is largely campus-based. Strategic's 2025 10-K: USHE $868.2M of $1,268.2M. · Capella is online and Strayer is mostly online; ETS (Sophia, Workforce Edge) is online. The ANZ segment (Torrens University and other Australia/New Zealand institutions) is largely campus-based. Strategic's 2025 10-K: USHE $868.2M of $1,268.2M. |
| DUOL | online_revenue_share | 1 | 0.98 | 1 | UNVERIFIED | No source URL · estimate; All revenue comes from the app (subscriptions, ads, in-app purchases) and the online Duolingo English Test. · All revenue comes from the app (subscriptions, ads, in-app purchases) and the online Duolingo English Test. |
| COUR | online_revenue_share | 1 | 0.98 | 1 | UNVERIFIED | No source URL · estimate; An online learning platform; all courses, certificates and degrees are delivered online. · An online learning platform; all courses, certificates and degrees are delivered online. |
| UTI | online_revenue_share | 0.75 | 0.45 | 0.85 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| PRDO | online_revenue_share | 0.75 | 0.45 | 0.85 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| APEI | online_revenue_share | 0.75 | 0.45 | 0.85 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| NRDY | online_revenue_share | 1 | 0.98 | 1 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Digital learning and training; median base and outer low/high from DUOL/COUR in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Digital learning and training; median base and outer low/high from DUOL/COUR in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| LINC | online_revenue_share | 0.75 | 0.45 | 0.85 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| SKIL | online_revenue_share | 1 | 0.98 | 1 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Digital learning and training; median base and outer low/high from DUOL/COUR in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Digital learning and training; median base and outer low/high from DUOL/COUR in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| CHGG | online_revenue_share | 1 | 0.98 | 1 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Digital learning and training; median base and outer low/high from DUOL/COUR in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Digital learning and training; median base and outer low/high from DUOL/COUR in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| SCHL | online_revenue_share | 1 | 0.9 | 1 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Publishing and childcare; median base and outer low/high from LRN/DUOL/COUR in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Publishing and childcare; median base and outer low/high from LRN/DUOL/COUR in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| WLY | online_revenue_share | 1 | 0.9 | 1 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Publishing and childcare; median base and outer low/high from LRN/DUOL/COUR in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Publishing and childcare; median base and outer low/high from LRN/DUOL/COUR in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| FC | online_revenue_share | 1 | 0.98 | 1 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Digital learning and training; median base and outer low/high from DUOL/COUR in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Digital learning and training; median base and outer low/high from DUOL/COUR in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |

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
| assumption.pass_through | -0.021183196 | -0.015543684 | 0.0056395115 |
| exposure.online_revenue_share | -0.016005802 | -0.019349321 | 0.003343519 |
| assumption.elasticity | -0.017653872 | -0.019304274 | 0.0016504019 |

Dominant configured driver: `pass_through` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.


## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 16 unchecked in-scope exposure values; 2 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

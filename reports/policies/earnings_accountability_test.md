# Program earnings test ("do no harm" accountability)

Policy `education/earnings_accountability_test` · reviewed 2026-10-31 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

Under the 2025 reconciliation law, degree programs whose graduates earn less than a benchmark (high-school graduates for undergraduate programs, bachelor's holders for graduate programs) lose Direct Loan eligibility. The first test runs in early 2027. Online for-profit graduate programs in counseling, psychology and education are the most at risk (Covista's Walden, Strategic's Capella, Grand Canyon); Stride and Duolingo are outside the rule.

Duration: `permanent`. Default inputs: `{"fail_share_pct": 50.0}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| demand_volume | unavailable / unavailable | {"d_volume": "-input.fail_share_pct / 100 * assumption.enrollment_loss", "exposed_revenue_share": "exposure.earnings_test_at_risk_revenue_share"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://edtrust.org/rti/federal-rulemaking-recap-for-postsecondary-program-accountability-what-changed-and-what-it-means-for-higher-education/
- https://ticas.org/accountability/earnings-metric-final-rule-blog/
- https://www.nasfaa.org/uploads/documents/Ppt3_ResultsofEarningsTestandGEChanges_v2.pdf

| Company | Configured status | Basis |
|---|---|---|
| LRN | outside_scope | This channel covers US aid-dependent programs or service partners, not foreign private-pay institutions, lenders or learning apps. |
| LOPE | included | Loss of aid eligibility reduces enrollment at exposed programs. |
| CVSA | included | Loss of aid eligibility reduces enrollment at exposed programs. |
| STRA | included | Loss of aid eligibility reduces enrollment at exposed programs. |
| DUOL | outside_scope | This channel covers US aid-dependent programs or service partners, not foreign private-pay institutions, lenders or learning apps. |
| COUR | included | Loss of aid eligibility reduces enrollment at exposed programs. |
| UTI | included | Loss of aid eligibility reduces enrollment at exposed programs. |
| PRDO | included | Loss of aid eligibility reduces enrollment at exposed programs. |
| APEI | included | Loss of aid eligibility reduces enrollment at exposed programs. |
| LAUR | outside_scope | This channel covers US aid-dependent programs or service partners, not foreign private-pay institutions, lenders or learning apps. |
| NRDY | outside_scope | This channel covers US aid-dependent programs or service partners, not foreign private-pay institutions, lenders or learning apps. |
| LINC | included | Loss of aid eligibility reduces enrollment at exposed programs. |
| SKIL | outside_scope | This channel covers US aid-dependent programs or service partners, not foreign private-pay institutions, lenders or learning apps. |
| CHGG | outside_scope | This channel covers US aid-dependent programs or service partners, not foreign private-pay institutions, lenders or learning apps. |
| SCHL | outside_scope | This channel covers US aid-dependent programs or service partners, not foreign private-pay institutions, lenders or learning apps. |
| KLC | outside_scope | This channel covers US aid-dependent programs or service partners, not foreign private-pay institutions, lenders or learning apps. |
| BFAM | outside_scope | This channel covers US aid-dependent programs or service partners, not foreign private-pay institutions, lenders or learning apps. |
| WLY | outside_scope | This channel covers US aid-dependent programs or service partners, not foreign private-pay institutions, lenders or learning apps. |
| FC | outside_scope | This channel covers US aid-dependent programs or service partners, not foreign private-pay institutions, lenders or learning apps. |
| SLM | outside_scope | This channel covers US aid-dependent programs or service partners, not foreign private-pay institutions, lenders or learning apps. |

## B. Every in-scope exposure

Exact numeric checks are distinguished from filing links and estimates. UNVERIFIED values are retained, not silently replaced. Historical observed low/high values are not forecast confidence intervals.

| Company | Exposure | Base | Low | High | Exact-source status | Primary source / location / rationale |
|---|---|---:|---:|---:|---|---|
| LOPE | earnings_test_at_risk_revenue_share | 0.04 | 0.01 | 0.08 | UNVERIFIED | https://edtrust.org/rti/federal-rulemaking-recap-for-postsecondary-program-accountability-what-changed-and-what-it-means-for-higher-education/ · estimate; ED's January 2026 estimate (as summarised by EdTrust and others; not confirmed against the ED slides) has ~4% of master's and ~1.2% of bachelor's programs failing. GCU's large online graduate programs in counseling and education are the likeliest failures, so a few percent of revenue is at risk. · ED's January 2026 estimate (as summarised by EdTrust and others; not confirmed against the ED slides) has ~4% of master's and ~1.2% of bachelor's programs failing. GCU's large online graduate programs in counseling and education are the likeliest failures, so a few percent of revenue is at risk. |
| CVSA | earnings_test_at_risk_revenue_share | 0.05 | 0.02 | 0.1 | UNVERIFIED | https://edtrust.org/rti/federal-rulemaking-recap-for-postsecondary-program-accountability-what-changed-and-what-it-means-for-higher-education/ · estimate; Nursing and medical programs clear the benchmark easily. Walden's online counseling, psychology, education and social-work master's and doctoral programs are the likeliest to fail; ED's January 2026 estimate (secondary summary, not confirmed against ED slides) has ~35% of for-profit programs failing, mostly undergraduate certificates, which Covista barely offers. · Nursing and medical programs clear the benchmark easily. Walden's online counseling, psychology, education and social-work master's and doctoral programs are the likeliest to fail; ED's January 2026 estimate (secondary summary, not confirmed against ED slides) has ~35% of for-profit programs failing, mostly undergraduate certificates, which Covista barely offers. |
| STRA | earnings_test_at_risk_revenue_share | 0.06 | 0.02 | 0.12 | UNVERIFIED | https://edtrust.org/rti/federal-rulemaking-recap-for-postsecondary-program-accountability-what-changed-and-what-it-means-for-higher-education/ · estimate; Capella's online counseling, psychology and education graduate programs and some Strayer associate/undergraduate programs are the likeliest failures. ED's January 2026 estimate (secondary summary, not confirmed against ED slides) has ~35% of for-profit programs failing, concentrated in undergraduate certificates, which Strategic offers little of. · Capella's online counseling, psychology and education graduate programs and some Strayer associate/undergraduate programs are the likeliest failures. ED's January 2026 estimate (secondary summary, not confirmed against ED slides) has ~35% of for-profit programs failing, concentrated in undergraduate certificates, which Strategic offers little of. |
| COUR | earnings_test_at_risk_revenue_share | 0.005 | 0 | 0.01 | UNVERIFIED | No source URL · estimate; Only partner-university degree programs fall under the test; computer science, data science and business master's degrees generally clear the bachelor's-earnings benchmark. · Only partner-university degree programs fall under the test; computer science, data science and business master's degrees generally clear the bachelor's-earnings benchmark. |
| UTI | earnings_test_at_risk_revenue_share | 0.05 | 0.01 | 0.12 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| PRDO | earnings_test_at_risk_revenue_share | 0.05 | 0.01 | 0.12 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| APEI | earnings_test_at_risk_revenue_share | 0.05 | 0.01 | 0.12 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| LINC | earnings_test_at_risk_revenue_share | 0.05 | 0.01 | 0.12 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |

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
| exposure.earnings_test_at_risk_revenue_share | -0.0049450206 | -0.037640443 | 0.032695423 |
| assumption.enrollment_loss | -0.011536753 | -0.0245156 | 0.012978847 |
| assumption.programs_failing_share | -0.017305129 | -0.017305129 | 0 |

Dominant configured driver: `earnings_test_at_risk_revenue_share` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.


## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 8 unchecked in-scope exposure values; 2 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

# Tighter 90/10 rule (e.g. 85/15)

Policy `education/ninety_ten_rule_change` · reviewed 2026-10-31 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

Lowers the cap on the share of a for-profit college's cash revenue that may come from federal education aid (90% today). An institution above the new cap must either raise non-federal revenue or shed federally funded students. Strayer University (89.64% federal in FY2024) is the most exposed, then Covista's medical schools (86%); Stride, Duolingo and Coursera own no proprietary Title IV school.

Duration: `permanent`. Default inputs: `{"cap_pct": 85.0}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| demand_volume | unavailable / unavailable | {"d_volume": "-(1 - assumption.mitigation_share) * max(0, 1 - (1 - exposure.ninety_ten_hi_ratio) / (1 - input.cap_pct / 100))", "exposed_revenue_share": "exposure.ninety_ten_hi_revenue_share"} |
| demand_volume | unavailable / unavailable | {"d_volume": "-(1 - assumption.mitigation_share) * max(0, 1 - (1 - exposure.ninety_ten_lo_ratio) / (1 - input.cap_pct / 100))", "exposed_revenue_share": "exposure.ninety_ten_lo_revenue_share"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://www.sec.gov/Archives/edgar/data/1013934/000101393426000006/stra-20251231.htm
- https://www.sec.gov/Archives/edgar/data/730464/000110465926092044/cvsa-20260630x10k.htm
- https://www.everycrsreport.com/reports/R46773.html

| Company | Configured status | Basis |
|---|---|---|
| LRN | outside_scope | No covered proprietary Title IV tuition/service-partner exposure. |
| LOPE | conditional | The configured federal-aid share is 73%, below every selectable cap (75–90%). The rule does not bind at these settings. |
| CVSA | included | Tighter federal revenue limit restricts exposed proprietary programs. |
| STRA | included | Tighter federal revenue limit restricts exposed proprietary programs. |
| DUOL | outside_scope | No covered proprietary Title IV tuition/service-partner exposure. |
| COUR | outside_scope | No covered proprietary Title IV tuition/service-partner exposure. |
| UTI | included | Tighter federal revenue limit restricts exposed proprietary programs. |
| PRDO | included | Tighter federal revenue limit restricts exposed proprietary programs. |
| APEI | included | Tighter federal revenue limit restricts exposed proprietary programs. |
| LAUR | outside_scope | No covered proprietary Title IV tuition/service-partner exposure. |
| NRDY | outside_scope | No covered proprietary Title IV tuition/service-partner exposure. |
| LINC | included | Tighter federal revenue limit restricts exposed proprietary programs. |
| SKIL | outside_scope | No covered proprietary Title IV tuition/service-partner exposure. |
| CHGG | outside_scope | No covered proprietary Title IV tuition/service-partner exposure. |
| SCHL | outside_scope | No covered proprietary Title IV tuition/service-partner exposure. |
| KLC | outside_scope | No covered proprietary Title IV tuition/service-partner exposure. |
| BFAM | outside_scope | No covered proprietary Title IV tuition/service-partner exposure. |
| WLY | outside_scope | No covered proprietary Title IV tuition/service-partner exposure. |
| FC | outside_scope | No covered proprietary Title IV tuition/service-partner exposure. |
| SLM | outside_scope | No covered proprietary Title IV tuition/service-partner exposure. |

## B. Every in-scope exposure

Exact numeric checks are distinguished from filing links and estimates. UNVERIFIED values are retained, not silently replaced. Historical observed low/high values are not forecast confidence intervals.

| Company | Exposure | Base | Low | High | Exact-source status | Primary source / location / rationale |
|---|---|---:|---:|---:|---|---|
| CVSA | ninety_ten_hi_ratio | 0.86 | 0.86 | 0.87 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/730464/000110465926092044/cvsa-20260630x10k.htm · Covista FY2026 10-K: audited FY2025 90/10 rates of 86% at both American University of the Caribbean School of Medicine and Ross University School of Medicine (87% in FY2024);  · unavailable |
| CVSA | ninety_ten_hi_revenue_share | 0.13 | 0.1 | 0.17 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/730464/000110465926092044/cvsa-20260630x10k.htm · estimate; Covista FY2026 10-K: Medical & Veterinary segment revenue $398.9M (20.4% of $1,954.1M) covers AUC, RUSM and the veterinary school (RUSVM); assumes the two medical schools are about two-thirds of the segment. · Covista FY2026 10-K: Medical & Veterinary segment revenue $398.9M (20.4% of $1,954.1M) covers AUC, RUSM and the veterinary school (RUSVM); assumes the two medical schools are about two-thirds of the segment. |
| CVSA | ninety_ten_lo_ratio | 0.763 | 0.74 | 0.78 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/730464/000110465926092044/cvsa-20260630x10k.htm · Covista FY2026 10-K: audited FY2025 90/10 rates Walden 82%, Chamberlain 70%, RUSVM 77% (consolidated 78%); weighted by FY2026 revenue (Walden $804.9M, Chamberlain $750.2M, RUSVM ~$140M) ≈ 76%; RUSVM's revenue is not disclosed separately and is estimated at about a third of the Medical & Veterinary segment. · RUSVM's revenue is not disclosed separately and is estimated at about a third of the Medical & Veterinary segment. |
| CVSA | ninety_ten_lo_revenue_share | 0.87 | 0.83 | 0.9 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/730464/000110465926092044/cvsa-20260630x10k.htm · estimate; Covista FY2026 10-K: Chamberlain $750.2M + Walden $804.9M = 79.6% of revenue, plus RUSVM (~7%, estimated share of the Medical & Veterinary segment). · Covista FY2026 10-K: Chamberlain $750.2M + Walden $804.9M = 79.6% of revenue, plus RUSVM (~7%, estimated share of the Medical & Veterinary segment). |
| STRA | ninety_ten_hi_ratio | 0.8964 | 0.88 | 0.9 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1013934/000101393426000006/stra-20251231.htm · Strategic Education 2025 10-K: Strayer University derived approximately 89.64% of its cash-basis revenues from federal funds in fiscal year 2024;  · unavailable |
| STRA | ninety_ten_hi_revenue_share | 0.3 | 0.25 | 0.36 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1013934/000101393426000006/stra-20251231.htm · estimate; Strategic Education 2025 10-K: USHE (Capella + Strayer) revenue $868.2M, 68% of the total; the Capella/Strayer split is not disclosed in the text read and is assumed to be roughly 55/45. · Strategic Education 2025 10-K: USHE (Capella + Strayer) revenue $868.2M, 68% of the total; the Capella/Strayer split is not disclosed in the text read and is assumed to be roughly 55/45. |
| STRA | ninety_ten_lo_ratio | 0.6788 | 0.66 | 0.7 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1013934/000101393426000006/stra-20251231.htm · Strategic Education 2025 10-K: Capella University derived approximately 67.88% of its cash-basis revenues from federal funds in fiscal year 2024;  · unavailable |
| STRA | ninety_ten_lo_revenue_share | 0.38 | 0.32 | 0.43 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1013934/000101393426000006/stra-20251231.htm · estimate; Remainder of USHE revenue (68% of the total, per the 2025 10-K) after Strayer's estimated share. · Remainder of USHE revenue (68% of the total, per the 2025 10-K) after Strayer's estimated share. |
| UTI | ninety_ten_hi_ratio | 0.86 | 0.68 | 0.9 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| UTI | ninety_ten_hi_revenue_share | 0.3 | 0.1 | 0.9 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| UTI | ninety_ten_lo_ratio | 0.6788 | 0 | 0.78 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| UTI | ninety_ten_lo_revenue_share | 0.38 | 0 | 0.9 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| PRDO | ninety_ten_hi_ratio | 0.86 | 0.68 | 0.9 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| PRDO | ninety_ten_hi_revenue_share | 0.3 | 0.1 | 0.9 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| PRDO | ninety_ten_lo_ratio | 0.6788 | 0 | 0.78 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| PRDO | ninety_ten_lo_revenue_share | 0.38 | 0 | 0.9 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| APEI | ninety_ten_hi_ratio | 0.86 | 0.68 | 0.9 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| APEI | ninety_ten_hi_revenue_share | 0.3 | 0.1 | 0.9 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| APEI | ninety_ten_lo_ratio | 0.6788 | 0 | 0.78 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| APEI | ninety_ten_lo_revenue_share | 0.38 | 0 | 0.9 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| LINC | ninety_ten_hi_ratio | 0.86 | 0.68 | 0.9 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| LINC | ninety_ten_hi_revenue_share | 0.3 | 0.1 | 0.9 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| LINC | ninety_ten_lo_ratio | 0.6788 | 0 | 0.78 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| LINC | ninety_ten_lo_revenue_share | 0.38 | 0 | 0.9 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Postsecondary and workforce institutions; median base and outer low/high from LOPE/CVSA/STRA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |

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
| exposure.ninety_ten_hi_ratio | -0.0066948814 | -0.036915596 | 0.030220714 |
| exposure.ninety_ten_hi_revenue_share | -0.0095236725 | -0.026744417 | 0.017220744 |
| assumption.mitigation_share | -0.021863014 | -0.0072876715 | 0.014575343 |
| exposure.ninety_ten_lo_ratio | -0.014575343 | -0.014575343 | 0 |
| exposure.ninety_ten_lo_revenue_share | -0.014575343 | -0.014575343 | 0 |

Dominant configured driver: `ninety_ten_hi_ratio` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.


## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 24 unchecked in-scope exposure values; 1 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

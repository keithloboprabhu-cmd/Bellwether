# Defense budget increase

Policy `public_sector/defense_budget_increase` · evidence checkpoint 2026-11-01 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

A higher defense and intelligence topline lifts contract spending at the DoW and the IC; defense-heavy CACI, SAIC and Booz Allen gain the most as a share of revenue, while Parsons and Leidos gain less.

Duration: `permanent`. Default inputs: `{"d_budget_pct": 5.0}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| gov_budget | unavailable / unavailable | {"gov_revenue_share": "exposure.govcon_defense_intel_share", "d_budget_pct": "input.d_budget_pct / 100", "program_relevance": "assumption.services_capture"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://www.sec.gov/Archives/edgar/data/16058/000162828026054195/caci-20260630.htm
- https://www.sec.gov/Archives/edgar/data/40533/000004053326000006/gd-20251231.htm

| Company | Configured status | Basis |
|---|---|---|
| BAH | included | Higher defense budget raises relevant contract demand. |
| LDOS | included | Higher defense budget raises relevant contract demand. |
| SAIC | included | Higher defense budget raises relevant contract demand. |
| CACI | included | Higher defense budget raises relevant contract demand. |
| PSN | included | Higher defense budget raises relevant contract demand. |
| GD | included | Higher defense budget raises relevant contract demand. |
| LMT | included | Higher defense budget raises relevant contract demand. |
| NOC | included | Higher defense budget raises relevant contract demand. |
| RTX | included | Higher defense budget raises relevant contract demand. |
| HII | included | Higher defense budget raises relevant contract demand. |
| OSK | included | Higher defense budget raises relevant contract demand. |
| KBR | included | Higher defense budget raises relevant contract demand. |
| KTOS | included | Higher defense budget raises relevant contract demand. |
| AVAV | included | Higher defense budget raises relevant contract demand. |
| BWXT | included | Higher defense budget raises relevant contract demand. |
| TXT | included | Higher defense budget raises relevant contract demand. |
| ICFI | included | Higher defense budget raises relevant contract demand. |
| TTEK | included | Higher defense budget raises relevant contract demand. |
| MRCY | included | Higher defense budget raises relevant contract demand. |
| VSEC | included | Higher defense budget raises relevant contract demand. |

## B. Every in-scope exposure

Exact numeric checks are distinguished from filing links and estimates. UNVERIFIED values are retained, not silently replaced. Historical observed low/high values are not forecast confidence intervals.

| Company | Exposure | Base | Low | High | Exact-source status | Primary source / location / rationale |
|---|---|---:|---:|---:|---|---|
| BAH | govcon_defense_intel_share | 0.71 | 0.69 | 0.73 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1443646/000162828026037521/bah-20260331.htm · Booz Allen FY2026 10-K, Note 3: Defense customers $6,069M (54%) + Intelligence customers $1,900M (17%) of $11,217M revenue;  · unavailable |
| LDOS | govcon_defense_intel_share | 0.49 | 0.48 | 0.51 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1336920/000133692026000030/ldos-20260102.htm · Leidos FY2025 10-K revenue disaggregation: DoW and U.S. Intelligence Community $8,426M of $17,107M (49%);  · unavailable |
| SAIC | govcon_defense_intel_share | 0.77 | 0.72 | 0.8 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1571123/000157112326000029/saic-20260130.htm · SAIC FY2026 10-K: Defense and Intelligence segment revenues $5,581M of $7,262M (77%); DoW alone ~52%;  · unavailable |
| CACI | govcon_defense_intel_share | 0.782 | 0.77 | 0.79 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/16058/000162828026054195/caci-20260630.htm · CACI FY2026 10-K: DoW $5,134M (53.6%) + Intelligence Community $2,352M (24.6%) of $9,568M revenue;  · unavailable |
| PSN | govcon_defense_intel_share | 0.31 | 0.29 | 0.4 | UNVERIFIED | No source URL · estimate; 10-K business-line table: Defense & Intelligence $1,873M of $6,364M (29%); Engineered Systems ($1,348M) adds some military-facility and missile-defense work. · 10-K business-line table: Defense & Intelligence $1,873M of $6,364M (29%); Engineered Systems ($1,348M) adds some military-facility and missile-defense work. |
| GD | govcon_defense_intel_share | 0.586 | 0.58 | 0.65 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/40533/000004053326000006/gd-20251231.htm · General Dynamics 2025 10-K: DoW $29,788M + FMS $1,015M of $52,550M revenue (58.6%); high end adds the IC part of non-DoW ($4,954M);  · unavailable |
| LMT | govcon_defense_intel_share | 0.586 | 0.58 | 0.65 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| NOC | govcon_defense_intel_share | 0.586 | 0.58 | 0.65 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| RTX | govcon_defense_intel_share | 0.586 | 0.58 | 0.65 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| HII | govcon_defense_intel_share | 0.586 | 0.58 | 0.65 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| OSK | govcon_defense_intel_share | 0.586 | 0.58 | 0.65 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| KBR | govcon_defense_intel_share | 0.71 | 0.29 | 0.8 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Government engineering and advisory; median base and outer low/high from BAH/LDOS/SAIC/CACI/PSN in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Government engineering and advisory; median base and outer low/high from BAH/LDOS/SAIC/CACI/PSN in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| KTOS | govcon_defense_intel_share | 0.586 | 0.58 | 0.65 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| AVAV | govcon_defense_intel_share | 0.586 | 0.58 | 0.65 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| BWXT | govcon_defense_intel_share | 0.586 | 0.58 | 0.65 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| TXT | govcon_defense_intel_share | 0.586 | 0.58 | 0.65 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| ICFI | govcon_defense_intel_share | 0.71 | 0.29 | 0.8 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Government engineering and advisory; median base and outer low/high from BAH/LDOS/SAIC/CACI/PSN in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Government engineering and advisory; median base and outer low/high from BAH/LDOS/SAIC/CACI/PSN in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| TTEK | govcon_defense_intel_share | 0.71 | 0.29 | 0.8 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Government engineering and advisory; median base and outer low/high from BAH/LDOS/SAIC/CACI/PSN in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Government engineering and advisory; median base and outer low/high from BAH/LDOS/SAIC/CACI/PSN in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| MRCY | govcon_defense_intel_share | 0.586 | 0.58 | 0.65 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| VSEC | govcon_defense_intel_share | 0.586 | 0.58 | 0.65 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |

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
| assumption.services_capture | 0.029130062 | 0.069912148 | 0.040782086 |
| exposure.govcon_defense_intel_share | 0.05029643 | 0.057556485 | 0.0072600549 |

Dominant configured driver: `services_capture` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.


## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 20 unchecked in-scope exposure values; 1 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

# Continuing resolution

Policy `public_sector/continuing_resolution` · reviewed 2026-10-31 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

A continuing resolution funds agencies at last year's level and bars new starts, so revenue from new awards and scope growth slips by the length of the CR. Revenue is delayed rather than lost, so it is a one-year hit.

Duration: `one_time`. Default inputs: `{"months_delayed": 3.0}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| gov_cr | unavailable / unavailable | {"gov_revenue_share": "exposure.govcon_us_gov_share", "months_delayed": "input.months_delayed", "new_award_share": "assumption.new_award_share"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://www.sec.gov/Archives/edgar/data/16058/000162828026054195/caci-20260630.htm
- https://www.sec.gov/Archives/edgar/data/1443646/000162828026037521/bah-20260331.htm

| Company | Configured status | Basis |
|---|---|---|
| BAH | included | New awards slip beyond the modeled fiscal year. |
| LDOS | included | New awards slip beyond the modeled fiscal year. |
| SAIC | included | New awards slip beyond the modeled fiscal year. |
| CACI | included | New awards slip beyond the modeled fiscal year. |
| PSN | included | New awards slip beyond the modeled fiscal year. |
| GD | included | New awards slip beyond the modeled fiscal year. |
| LMT | included | New awards slip beyond the modeled fiscal year. |
| NOC | included | New awards slip beyond the modeled fiscal year. |
| RTX | included | New awards slip beyond the modeled fiscal year. |
| HII | included | New awards slip beyond the modeled fiscal year. |
| OSK | included | New awards slip beyond the modeled fiscal year. |
| KBR | included | New awards slip beyond the modeled fiscal year. |
| KTOS | included | New awards slip beyond the modeled fiscal year. |
| AVAV | included | New awards slip beyond the modeled fiscal year. |
| BWXT | included | New awards slip beyond the modeled fiscal year. |
| TXT | included | New awards slip beyond the modeled fiscal year. |
| ICFI | included | New awards slip beyond the modeled fiscal year. |
| TTEK | included | New awards slip beyond the modeled fiscal year. |
| MRCY | included | New awards slip beyond the modeled fiscal year. |
| VSEC | included | New awards slip beyond the modeled fiscal year. |

## B. Every in-scope exposure

Exact numeric checks are distinguished from filing links and estimates. UNVERIFIED values are retained, not silently replaced. Historical observed low/high values are not forecast confidence intervals.

| Company | Exposure | Base | Low | High | Exact-source status | Primary source / location / rationale |
|---|---|---:|---:|---:|---|---|
| BAH | govcon_us_gov_share | 0.98 | 0.97 | 0.99 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1443646/000162828026037521/bah-20260331.htm · Booz Allen FY2026 10-K, Note 3: approximately 98% of revenue in fiscal 2026, 2025 and 2024 from contracts with the U.S. government;  · unavailable |
| LDOS | govcon_us_gov_share | 0.87 | 0.85 | 0.89 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1336920/000133692026000030/ldos-20260102.htm · Leidos FY2025 10-K: approximately 87% of total revenues from contracts with the U.S. government in fiscal 2025, 2024 and 2023;  · unavailable |
| SAIC | govcon_us_gov_share | 0.98 | 0.97 | 0.99 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1571123/000157112326000029/saic-20260130.htm · SAIC FY2026 10-K: 98% of total revenues in fiscal 2026, 2025 and 2024 from contracts with the U.S. government;  · unavailable |
| CACI | govcon_us_gov_share | 0.956 | 0.95 | 0.96 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/16058/000162828026054195/caci-20260630.htm · CACI FY2026 10-K: federal government contracts 95.6% of total revenues in fiscal 2026 (95.7% FY2025);  · unavailable |
| PSN | govcon_us_gov_share | 0.51 | 0.49 | 0.55 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/275880/000119312526045495/psn-20251231.htm · Parsons FY2025 10-K: approximately 51% of consolidated revenues from contracts with the U.S. federal government (59% in 2024);  · unavailable |
| GD | govcon_us_gov_share | 0.68 | 0.66 | 0.7 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/40533/000004053326000006/gd-20251231.htm · General Dynamics 2025 10-K: total U.S. government revenue $35,757M, 68% of total revenue (incl. FMS);  · unavailable |
| LMT | govcon_us_gov_share | 0.68 | 0.66 | 0.7 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| NOC | govcon_us_gov_share | 0.68 | 0.66 | 0.7 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| RTX | govcon_us_gov_share | 0.68 | 0.66 | 0.7 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| HII | govcon_us_gov_share | 0.68 | 0.66 | 0.7 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| OSK | govcon_us_gov_share | 0.68 | 0.66 | 0.7 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| KBR | govcon_us_gov_share | 0.956 | 0.49 | 0.99 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Government engineering and advisory; median base and outer low/high from BAH/LDOS/SAIC/CACI/PSN in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Government engineering and advisory; median base and outer low/high from BAH/LDOS/SAIC/CACI/PSN in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| KTOS | govcon_us_gov_share | 0.68 | 0.66 | 0.7 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| AVAV | govcon_us_gov_share | 0.68 | 0.66 | 0.7 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| BWXT | govcon_us_gov_share | 0.68 | 0.66 | 0.7 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| TXT | govcon_us_gov_share | 0.68 | 0.66 | 0.7 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| ICFI | govcon_us_gov_share | 0.956 | 0.49 | 0.99 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Government engineering and advisory; median base and outer low/high from BAH/LDOS/SAIC/CACI/PSN in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Government engineering and advisory; median base and outer low/high from BAH/LDOS/SAIC/CACI/PSN in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| TTEK | govcon_us_gov_share | 0.956 | 0.49 | 0.99 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Government engineering and advisory; median base and outer low/high from BAH/LDOS/SAIC/CACI/PSN in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Government engineering and advisory; median base and outer low/high from BAH/LDOS/SAIC/CACI/PSN in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| MRCY | govcon_us_gov_share | 0.68 | 0.66 | 0.7 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| VSEC | govcon_us_gov_share | 0.68 | 0.66 | 0.7 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |

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
| assumption.new_award_share | -0.018757949 | -0.075031796 | 0.056273847 |
| exposure.govcon_us_gov_share | -0.034697087 | -0.038545283 | 0.0038481958 |

Dominant configured driver: `new_award_share` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.


## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 20 unchecked in-scope exposure values; 1 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

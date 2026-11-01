# Shift to fixed-price contracts

Policy `public_sector/fixed_price_shift` · evidence checkpoint 2026-11-01 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

Converting part of cost-plus work to fixed-price changes the margin on converted contracts. Revenue is held constant; the modeled efficiency/overrun difference changes operating costs. The central assumption is a margin loss, with possible gains in the high case.

Duration: `permanent`. Default inputs: `{"conversion_pct": 20.0}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| cost | unavailable / unavailable | {"exposed_cost_share": 0.0, "shock_pct": 0.0, "dcost_musd": "-baseline.revenue * exposure.govcon_cost_plus_share * input.conversion_pct / 100 * assumption.d_margin_pp / 100"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://www.sec.gov/Archives/edgar/data/1443646/000162828026037521/bah-20260331.htm
- https://www.sec.gov/Archives/edgar/data/1571123/000157112326000029/saic-20260130.htm

| Company | Configured status | Basis |
|---|---|---|
| BAH | included | Cost overruns move from reimbursed to contractor-borne. |
| LDOS | included | Cost overruns move from reimbursed to contractor-borne. |
| SAIC | included | Cost overruns move from reimbursed to contractor-borne. |
| CACI | included | Cost overruns move from reimbursed to contractor-borne. |
| PSN | included | Cost overruns move from reimbursed to contractor-borne. |
| GD | included | Cost overruns move from reimbursed to contractor-borne. |
| LMT | included | Cost overruns move from reimbursed to contractor-borne. |
| NOC | included | Cost overruns move from reimbursed to contractor-borne. |
| RTX | included | Cost overruns move from reimbursed to contractor-borne. |
| HII | included | Cost overruns move from reimbursed to contractor-borne. |
| OSK | included | Cost overruns move from reimbursed to contractor-borne. |
| KBR | included | Cost overruns move from reimbursed to contractor-borne. |
| KTOS | included | Cost overruns move from reimbursed to contractor-borne. |
| AVAV | included | Cost overruns move from reimbursed to contractor-borne. |
| BWXT | included | Cost overruns move from reimbursed to contractor-borne. |
| TXT | included | Cost overruns move from reimbursed to contractor-borne. |
| ICFI | included | Cost overruns move from reimbursed to contractor-borne. |
| TTEK | included | Cost overruns move from reimbursed to contractor-borne. |
| MRCY | included | Cost overruns move from reimbursed to contractor-borne. |
| VSEC | included | Cost overruns move from reimbursed to contractor-borne. |

## B. Every in-scope exposure

Exact numeric checks are distinguished from filing links and estimates. UNVERIFIED values are retained, not silently replaced. Historical observed low/high values are not forecast confidence intervals.

| Company | Exposure | Base | Low | High | Exact-source status | Primary source / location / rationale |
|---|---|---:|---:|---:|---|---|
| BAH | govcon_cost_plus_share | 0.59 | 0.55 | 0.6 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1443646/000162828026037521/bah-20260331.htm · Booz Allen FY2026 10-K: cost-reimbursable $6,587M (59%) of revenue (57% FY2025, 55% FY2024);  · unavailable |
| LDOS | govcon_cost_plus_share | 0.44 | 0.4 | 0.44 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1336920/000133692026000030/ldos-20260102.htm · Leidos FY2025 10-K: cost-reimbursement and fixed-price-incentive-fee contracts 44% of revenues ($7,606M); low end strips out the FPIF part;  · unavailable |
| SAIC | govcon_cost_plus_share | 0.62 | 0.6 | 0.63 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1571123/000157112326000029/saic-20260130.htm · SAIC FY2026 10-K: cost reimbursement 62% of total revenues (79% of Defense & Intelligence, 3% of Civilian);  · unavailable |
| CACI | govcon_cost_plus_share | 0.56 | 0.56 | 0.605 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/16058/000162828026054195/caci-20260630.htm · CACI FY2026 10-K: cost-plus-fee $5,361M (56.0%) of revenue (60.5% FY2025);  · unavailable |
| PSN | govcon_cost_plus_share | 0.423 | 0.37 | 0.43 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/275880/000119312526045495/psn-20251231.htm · Parsons FY2025 10-K, Note 4: cost-plus revenue $2,689M of $6,364M (42%); 37% in 2024;  · unavailable |
| GD | govcon_cost_plus_share | 0.298 | 0.29 | 0.3 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/40533/000004053326000006/gd-20251231.htm · General Dynamics 2025 10-K: cost-reimbursement revenue $15,673M of $52,550M (29.8%); 44% of U.S. government revenue;  · unavailable |
| LMT | govcon_cost_plus_share | 0.298 | 0.29 | 0.3 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| NOC | govcon_cost_plus_share | 0.298 | 0.29 | 0.3 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| RTX | govcon_cost_plus_share | 0.298 | 0.29 | 0.3 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| HII | govcon_cost_plus_share | 0.298 | 0.29 | 0.3 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| OSK | govcon_cost_plus_share | 0.298 | 0.29 | 0.3 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| KBR | govcon_cost_plus_share | 0.56 | 0.37 | 0.63 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Government engineering and advisory; median base and outer low/high from BAH/LDOS/SAIC/CACI/PSN in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Government engineering and advisory; median base and outer low/high from BAH/LDOS/SAIC/CACI/PSN in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| KTOS | govcon_cost_plus_share | 0.298 | 0.29 | 0.3 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| AVAV | govcon_cost_plus_share | 0.298 | 0.29 | 0.3 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| BWXT | govcon_cost_plus_share | 0.298 | 0.29 | 0.3 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| TXT | govcon_cost_plus_share | 0.298 | 0.29 | 0.3 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| ICFI | govcon_cost_plus_share | 0.56 | 0.37 | 0.63 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Government engineering and advisory; median base and outer low/high from BAH/LDOS/SAIC/CACI/PSN in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Government engineering and advisory; median base and outer low/high from BAH/LDOS/SAIC/CACI/PSN in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| TTEK | govcon_cost_plus_share | 0.56 | 0.37 | 0.63 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Government engineering and advisory; median base and outer low/high from BAH/LDOS/SAIC/CACI/PSN in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Government engineering and advisory; median base and outer low/high from BAH/LDOS/SAIC/CACI/PSN in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| MRCY | govcon_cost_plus_share | 0.298 | 0.29 | 0.3 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| VSEC | govcon_cost_plus_share | 0.298 | 0.29 | 0.3 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |

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
| assumption.d_margin_pp | -0.022855858 | 0.015237238 | 0.038093096 |
| exposure.govcon_cost_plus_share | -0.0072175866 | -0.007752672 | 0.00053508545 |

Dominant configured driver: `d_margin_pp` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.


## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 20 unchecked in-scope exposure values; 1 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

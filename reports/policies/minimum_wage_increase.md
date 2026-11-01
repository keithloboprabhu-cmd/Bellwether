# Federal minimum wage increase

Policy `consumer_retail/minimum_wage_increase` · evidence checkpoint 2026-11-01 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

A higher federal minimum wage lifts pay for hourly store and warehouse staff paid below it (and some just above); retailers pass part of the cost into prices and sell a little less.

Duration: `permanent`. Default inputs: `{"new_min": 17.0}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| cost | unavailable / unavailable | {"exposed_cost_share": 0.0, "shock_pct": 0.0, "dcost_musd": "exposure.us_hourly_workers_m * assumption.annual_hours * max(0, input.new_min - exposure.us_starting_wage) * assumption.payroll_gap_factor", "pass_through": "assumption.pass_through", "elasticity": "assumption.elasticity"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://www.npr.org/2019/07/08/739607964/-15-minimum-wage-would-boost-17-million-workers-cut-1-3-million-jobs-cbo-says
- https://fred.stlouisfed.org/series/CES4200000007

| Company | Configured status | Basis |
|---|---|---|
| WMT | included | Higher wage floor raises exposed hourly payroll. |
| TGT | included | Higher wage floor raises exposed hourly payroll. |
| COST | included | Higher wage floor raises exposed hourly payroll. |
| AMZN | included | Higher wage floor raises exposed hourly payroll. |
| NKE | included | Higher wage floor raises exposed hourly payroll. |
| HD | included | Higher wage floor raises exposed hourly payroll. |
| LOW | included | Higher wage floor raises exposed hourly payroll. |
| KR | included | Higher wage floor raises exposed hourly payroll. |
| DG | included | Higher wage floor raises exposed hourly payroll. |
| DLTR | included | Higher wage floor raises exposed hourly payroll. |
| TJX | included | Higher wage floor raises exposed hourly payroll. |
| ROST | included | Higher wage floor raises exposed hourly payroll. |
| SBUX | included | Higher wage floor raises exposed hourly payroll. |
| MCD | included | Higher wage floor raises exposed hourly payroll. |
| KO | included | Higher wage floor raises exposed hourly payroll. |
| PEP | included | Higher wage floor raises exposed hourly payroll. |
| PG | included | Higher wage floor raises exposed hourly payroll. |
| CL | included | Higher wage floor raises exposed hourly payroll. |
| ULTA | included | Higher wage floor raises exposed hourly payroll. |
| BBY | included | Higher wage floor raises exposed hourly payroll. |
| MDLZ | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| MO | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| PFGC | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| PM | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| SYY | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| TSN | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |

## B. Every in-scope exposure

Exact numeric checks are distinguished from filing links and estimates. UNVERIFIED values are retained, not silently replaced. Historical observed low/high values are not forecast confidence intervals.

| Company | Exposure | Base | Low | High | Exact-source status | Primary source / location / rationale |
|---|---|---:|---:|---:|---|---|
| WMT | us_hourly_workers_m | 1.47 | 1.4 | 1.5 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/wmt-20260131.htm · Walmart FY2026 10-K: ~1.6 million US associates, ~92% hourly;  · unavailable |
| WMT | us_starting_wage | 14 | 14 | 16 | UNVERIFIED | https://corporate.walmart.com/askwalmart/how-much-do-walmart-associates-make · Walmart 'How much do Walmart associates make': team associate pay range $14–$37/hour; average US hourly frontline associate more than $18.50/hour; $14 is the floor of the range; high end reflects higher starting pay in many markets. · $14 is the floor of the range; high end reflects higher starting pay in many markets. |
| TGT | us_hourly_workers_m | 0.38 | 0.35 | 0.4 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/27419/000002741926000016/tgt-20260131.htm · Target FY2025 10-K: ~415,000 full-time, part-time and seasonal team members as of Jan 31 2026; US hourly store and supply-chain staff are 'the vast majority'; Base assumes ~92% of headcount is hourly, as at Walmart. · Base assumes ~92% of headcount is hourly, as at Walmart. |
| TGT | us_starting_wage | 15 | 15 | 17 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/27419/000002741926000016/tgt-20260131.htm · Target FY2025 10-K: starting wage range of $15 to $24 per hour for US hourly team members; Bottom of the disclosed range; high end for higher-cost markets. · Bottom of the disclosed range; high end for higher-cost markets. |
| COST | us_hourly_workers_m | 0.21 | 0.2 | 0.22 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/909832/000090983226000093/cost-20260830.htm · Costco FY2026 10-K: 232,000 US employees; average US hourly rate ~ $33; Base assumes ~90% of US employees are hourly warehouse staff. · Base assumes ~90% of US employees are hourly warehouse staff. |
| COST | us_starting_wage | 20 | 19.5 | 21 | UNVERIFIED | No source URL · estimate; Costco doesn't disclose starting pay in its 10-K; press reports of a Jan 2025 memo put bottom-of-scale pay at $20/hour, with later reports of ~$21. · Costco doesn't disclose starting pay in its 10-K; press reports of a Jan 2025 memo put bottom-of-scale pay at $20/hour, with later reports of ~$21. |
| AMZN | us_hourly_workers_m | 0.8 | 0.6 | 1 | UNVERIFIED | No source URL · estimate; 2025 10-K: ~1,576,000 employees worldwide; US share of hourly fulfillment and transportation staff not disclosed, assumed ~half. · 2025 10-K: ~1,576,000 employees worldwide; US share of hourly fulfillment and transportation staff not disclosed, assumed ~half. |
| AMZN | us_starting_wage | 19 | 18 | 21 | UNVERIFIED | https://www.aboutamazon.com/md/news/workplace/amazon-wage-increase-2025-fulfillment-transportation-employees · estimate; Amazon raised average starting pay for US front-line staff above $19 in 2022 (Bloomberg) and average pay above $23 in Sep 2025 (aboutamazon.com); current starting pay varies by site. · Amazon raised average starting pay for US front-line staff above $19 in 2022 (Bloomberg) and average pay above $23 in Sep 2025 (aboutamazon.com); current starting pay varies by site. |
| NKE | us_hourly_workers_m | 0.025 | 0.015 | 0.035 | UNVERIFIED | No source URL · estimate; FY2026 10-K: ~73,000 employees worldwide incl. retail; 347 US stores; assumes ~60–70 hourly staff per store plus US distribution centers. · FY2026 10-K: ~73,000 employees worldwide incl. retail; 347 US stores; assumes ~60–70 hourly staff per store plus US distribution centers. |
| NKE | us_starting_wage | 16 | 15 | 18 | UNVERIFIED | No source URL · estimate; Not disclosed; assumes Nike store pay a little above the $15 floor most large US retailers have adopted. · Not disclosed; assumes Nike store pay a little above the $15 floor most large US retailers have adopted. |
| HD | us_hourly_workers_m | 0.375 | 0.36 | 0.39 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/354950/000162828026019436/hd-20260201.htm · Home Depot FY2025 10-K: 422,500 US associates; ~53,400 salaried company-wide; Assumes ~90% of salaried staff are in the US. · Assumes ~90% of salaried staff are in the US. |
| HD | us_starting_wage | 15 | 15 | 17 | UNVERIFIED | No source URL · estimate; Not disclosed in the 10-K; Home Depot has publicly set a $15 starting floor in US stores, higher in many markets. · Not disclosed in the 10-K; Home Depot has publicly set a $15 starting floor in US stores, higher in many markets. |
| LOW | us_hourly_workers_m | 0.19648203 | 0.18862275 | 0.20434131 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Home improvement; median base and outer low/high from HD in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Home improvement; median base and outer low/high from HD in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| LOW | us_starting_wage | 15 | 15 | 17 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Home improvement; median base and outer low/high from HD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Home improvement; median base and outer low/high from HD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| KR | us_hourly_workers_m | 0.30432557 | 0.09740396 | 0.56362665 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Groceries and discount retail; median base and outer low/high from WMT/COST/TGT in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Groceries and discount retail; median base and outer low/high from WMT/COST/TGT in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| KR | us_starting_wage | 15 | 14 | 21 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Groceries and discount retail; median base and outer low/high from WMT/COST/TGT in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Groceries and discount retail; median base and outer low/high from WMT/COST/TGT in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| DG | us_hourly_workers_m | 0.088065172 | 0.028186578 | 0.16310124 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Groceries and discount retail; median base and outer low/high from WMT/COST/TGT in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Groceries and discount retail; median base and outer low/high from WMT/COST/TGT in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| DG | us_starting_wage | 15 | 14 | 21 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Groceries and discount retail; median base and outer low/high from WMT/COST/TGT in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Groceries and discount retail; median base and outer low/high from WMT/COST/TGT in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| DLTR | us_hourly_workers_m | 0.040012376 | 0.01280656 | 0.074104982 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Groceries and discount retail; median base and outer low/high from WMT/COST/TGT in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Groceries and discount retail; median base and outer low/high from WMT/COST/TGT in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| DLTR | us_starting_wage | 15 | 14 | 21 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Groceries and discount retail; median base and outer low/high from WMT/COST/TGT in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Groceries and discount retail; median base and outer low/high from WMT/COST/TGT in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| TJX | us_hourly_workers_m | 0.12573866 | 0.019517652 | 0.23047146 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Apparel and specialty retail; median base and outer low/high from TGT/NKE in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Apparel and specialty retail; median base and outer low/high from TGT/NKE in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| TJX | us_starting_wage | 15.5 | 15 | 18 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Apparel and specialty retail; median base and outer low/high from TGT/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Apparel and specialty retail; median base and outer low/high from TGT/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| ROST | us_hourly_workers_m | 0.047383302 | 0.0073550236 | 0.086850769 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Apparel and specialty retail; median base and outer low/high from TGT/NKE in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Apparel and specialty retail; median base and outer low/high from TGT/NKE in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| ROST | us_starting_wage | 15.5 | 15 | 18 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Apparel and specialty retail; median base and outer low/high from TGT/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Apparel and specialty retail; median base and outer low/high from TGT/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| SBUX | us_hourly_workers_m | 0.025758275 | 0.012021337 | 0.078210171 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Restaurants and consumer staples; median base and outer low/high from WMT/COST/NKE in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Restaurants and consumer staples; median base and outer low/high from WMT/COST/NKE in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| SBUX | us_starting_wage | 16 | 14 | 21 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Restaurants and consumer staples; median base and outer low/high from WMT/COST/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Restaurants and consumer staples; median base and outer low/high from WMT/COST/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| MCD | us_hourly_workers_m | 0.018623703 | 0.0086916462 | 0.056547381 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Restaurants and consumer staples; median base and outer low/high from WMT/COST/NKE in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Restaurants and consumer staples; median base and outer low/high from WMT/COST/NKE in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| MCD | us_starting_wage | 16 | 14 | 21 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Restaurants and consumer staples; median base and outer low/high from WMT/COST/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Restaurants and consumer staples; median base and outer low/high from WMT/COST/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| KO | us_hourly_workers_m | 0.033209557 | 0.015498836 | 0.10083459 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Restaurants and consumer staples; median base and outer low/high from WMT/COST/NKE in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Restaurants and consumer staples; median base and outer low/high from WMT/COST/NKE in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| KO | us_starting_wage | 16 | 14 | 21 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Restaurants and consumer staples; median base and outer low/high from WMT/COST/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Restaurants and consumer staples; median base and outer low/high from WMT/COST/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| PEP | us_hourly_workers_m | 0.065063466 | 0.030364994 | 0.19755301 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Restaurants and consumer staples; median base and outer low/high from WMT/COST/NKE in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Restaurants and consumer staples; median base and outer low/high from WMT/COST/NKE in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| PEP | us_starting_wage | 16 | 14 | 21 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Restaurants and consumer staples; median base and outer low/high from WMT/COST/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Restaurants and consumer staples; median base and outer low/high from WMT/COST/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| PG | us_hourly_workers_m | 0.060288566 | 0.028136558 | 0.18305493 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Restaurants and consumer staples; median base and outer low/high from WMT/COST/NKE in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Restaurants and consumer staples; median base and outer low/high from WMT/COST/NKE in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| PG | us_starting_wage | 16 | 14 | 21 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Restaurants and consumer staples; median base and outer low/high from WMT/COST/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Restaurants and consumer staples; median base and outer low/high from WMT/COST/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| CL | us_hourly_workers_m | 0.014118963 | 0.0065892926 | 0.042869582 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Restaurants and consumer staples; median base and outer low/high from WMT/COST/NKE in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Restaurants and consumer staples; median base and outer low/high from WMT/COST/NKE in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| CL | us_starting_wage | 16 | 14 | 21 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Restaurants and consumer staples; median base and outer low/high from WMT/COST/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Restaurants and consumer staples; median base and outer low/high from WMT/COST/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| ULTA | us_hourly_workers_m | 0.025810914 | 0.0040064723 | 0.047309868 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Apparel and specialty retail; median base and outer low/high from TGT/NKE in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Apparel and specialty retail; median base and outer low/high from TGT/NKE in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| ULTA | us_starting_wage | 15.5 | 15 | 18 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Apparel and specialty retail; median base and outer low/high from TGT/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Apparel and specialty retail; median base and outer low/high from TGT/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| BBY | us_hourly_workers_m | 0.086831151 | 0.013478275 | 0.15915633 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Apparel and specialty retail; median base and outer low/high from TGT/NKE in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Apparel and specialty retail; median base and outer low/high from TGT/NKE in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| BBY | us_starting_wage | 15.5 | 15 | 18 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Apparel and specialty retail; median base and outer low/high from TGT/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Apparel and specialty retail; median base and outer low/high from TGT/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |

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
| assumption.payroll_gap_factor | -0.0032024071 | -0.010665264 | 0.0074628572 |
| assumption.pass_through | -0.0096172046 | -0.0031912118 | 0.0064259928 |
| exposure.us_starting_wage | -0.0073465536 | -0.001151106 | 0.0061954476 |
| exposure.us_hourly_workers_m | -0.0052170284 | -0.0079228169 | 0.0027057885 |
| assumption.annual_hours | -0.0056026217 | -0.0072020074 | 0.0015993857 |
| assumption.elasticity | -0.0057683261 | -0.0072478093 | 0.0014794832 |

Dominant configured driver: `payroll_gap_factor` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.


## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 40 unchecked in-scope exposure values; 4 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

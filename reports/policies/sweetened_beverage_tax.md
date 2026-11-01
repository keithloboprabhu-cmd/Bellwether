# Sweetened beverage (soda) tax

Policy `consumer_retail/sweetened_beverage_tax` · evidence checkpoint 2026-11-01 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

A per-ounce excise on sugar- and artificially sweetened drinks, like Philadelphia's, raises shelf prices; shoppers buy fewer taxed drinks and shift a little spending to other items.

Duration: `permanent`. Default inputs: `{"coverage_pct": 100.0, "tax_cents_per_oz": 1.5}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| demand_price | unavailable / unavailable | {"dp_consumer": "input.tax_cents_per_oz * assumption.pass_through / assumption.price_per_oz", "elasticity": "assumption.elasticity", "exposed_revenue_share": "exposure.us_sweetened_beverage_revenue_share * input.coverage_pct / 100 * (1 - assumption.recapture)"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://doi.org/10.1001/jama.2019.4249
- https://doi.org/10.1111/obr.12002

| Company | Configured status | Basis |
|---|---|---|
| WMT | included | Covered beverage demand declines under a consumer tax. |
| TGT | included | Covered beverage demand declines under a consumer tax. |
| COST | included | Covered beverage demand declines under a consumer tax. |
| AMZN | included | Covered beverage demand declines under a consumer tax. |
| NKE | outside_scope | No quantified sales of covered sweetened beverages in this company channel; unrelated products do not inherit beverage taxes. |
| HD | included | Covered beverage demand declines under a consumer tax. |
| LOW | included | Covered beverage demand declines under a consumer tax. |
| KR | included | Covered beverage demand declines under a consumer tax. |
| DG | included | Covered beverage demand declines under a consumer tax. |
| DLTR | included | Covered beverage demand declines under a consumer tax. |
| TJX | outside_scope | No quantified sales of covered sweetened beverages in this company channel; unrelated products do not inherit beverage taxes. |
| ROST | outside_scope | No quantified sales of covered sweetened beverages in this company channel; unrelated products do not inherit beverage taxes. |
| SBUX | included | Covered beverage demand declines under a consumer tax. |
| MCD | included | Covered beverage demand declines under a consumer tax. |
| KO | included | Covered beverage demand declines under a consumer tax. |
| PEP | included | Covered beverage demand declines under a consumer tax. |
| PG | outside_scope | No quantified sales of covered sweetened beverages in this company channel; unrelated products do not inherit beverage taxes. |
| CL | outside_scope | No quantified sales of covered sweetened beverages in this company channel; unrelated products do not inherit beverage taxes. |
| ULTA | outside_scope | No quantified sales of covered sweetened beverages in this company channel; unrelated products do not inherit beverage taxes. |
| BBY | outside_scope | No quantified sales of covered sweetened beverages in this company channel; unrelated products do not inherit beverage taxes. |
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
| WMT | us_sweetened_beverage_revenue_share | 0.02 | 0.012 | 0.03 | UNVERIFIED | No source URL · estimate; FY2026 10-K: Walmart U.S. grocery $285,482M + Sam's Club grocery $64,706M = 49% of revenue; assumes sweetened drinks are ~4% (2.5–6%) of grocery sales. · FY2026 10-K: Walmart U.S. grocery $285,482M + Sam's Club grocery $64,706M = 49% of revenue; assumes sweetened drinks are ~4% (2.5–6%) of grocery sales. |
| TGT | us_sweetened_beverage_revenue_share | 0.014 | 0.008 | 0.02 | UNVERIFIED | No source URL · estimate; FY2025 10-K: food & beverage $24,136M = 23% of net sales; assumes sweetened drinks are ~6% (3.5–9%) of that category. · FY2025 10-K: food & beverage $24,136M = 23% of net sales; assumes sweetened drinks are ~6% (3.5–9%) of that category. |
| COST | us_sweetened_beverage_revenue_share | 0.015 | 0.009 | 0.022 | UNVERIFIED | No source URL · estimate; FY2026 10-K: Foods and Sundries $116,788M + Fresh Foods $41,715M = 53% of net sales, US ~72% of revenue; assumes sweetened drinks are ~4% (2.5–6%) of food sales. · FY2026 10-K: Foods and Sundries $116,788M + Fresh Foods $41,715M = 53% of net sales, US ~72% of revenue; assumes sweetened drinks are ~4% (2.5–6%) of food sales. |
| AMZN | us_sweetened_beverage_revenue_share | 0.002 | 0.001 | 0.004 | UNVERIFIED | No source URL · estimate; 2025 10-K: physical stores (mostly Whole Foods) $22,561M = 3.1% of net sales, plus online grocery; sweetened drinks are a small slice. · 2025 10-K: physical stores (mostly Whole Foods) $22,561M = 3.1% of net sales, plus online grocery; sweetened drinks are a small slice. |
| HD | us_sweetened_beverage_revenue_share | 0.001 | 0 | 0.002 | UNVERIFIED | No source URL · estimate; Checkout-lane drinks only. · Checkout-lane drinks only. |
| LOW | us_sweetened_beverage_revenue_share | 0.001 | 0 | 0.002 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Home improvement; median base and outer low/high from HD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Home improvement; median base and outer low/high from HD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| KR | us_sweetened_beverage_revenue_share | 0.015 | 0.008 | 0.03 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Groceries and discount retail; median base and outer low/high from WMT/COST/TGT in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Groceries and discount retail; median base and outer low/high from WMT/COST/TGT in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| DG | us_sweetened_beverage_revenue_share | 0.015 | 0.008 | 0.03 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Groceries and discount retail; median base and outer low/high from WMT/COST/TGT in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Groceries and discount retail; median base and outer low/high from WMT/COST/TGT in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| DLTR | us_sweetened_beverage_revenue_share | 0.015 | 0.008 | 0.03 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Groceries and discount retail; median base and outer low/high from WMT/COST/TGT in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Groceries and discount retail; median base and outer low/high from WMT/COST/TGT in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| SBUX | us_sweetened_beverage_revenue_share | 0.15 | 0.08 | 0.25 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/829224/000082922425000114/0000829224-25-000114-index.htm · estimate; Company-specific estimate: Company-specific US covered-beverage revenue proxy separating producer/restaurant exposure from grocery retailers. Geographic mix, drink mix and the tax's product coverage are not separately disclosed; use a wide sensitivity range, not a measured share. · Company-specific estimate: Company-specific US covered-beverage revenue proxy separating producer/restaurant exposure from grocery retailers. Geographic mix, drink mix and the tax's product coverage are not separately disclosed; use a wide sensitivity range, not a measured share. |
| MCD | us_sweetened_beverage_revenue_share | 0.06 | 0.03 | 0.12 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/63908/000006390826000035/0000063908-26-000035-index.htm · estimate; Company-specific estimate: Company-specific US covered-beverage revenue proxy separating producer/restaurant exposure from grocery retailers. Geographic mix, drink mix and the tax's product coverage are not separately disclosed; use a wide sensitivity range, not a measured share. · Company-specific estimate: Company-specific US covered-beverage revenue proxy separating producer/restaurant exposure from grocery retailers. Geographic mix, drink mix and the tax's product coverage are not separately disclosed; use a wide sensitivity range, not a measured share. |
| KO | us_sweetened_beverage_revenue_share | 0.2 | 0.1 | 0.3 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/21344/000162828026010047/0001628280-26-010047-index.htm · estimate; Company-specific estimate: Company-specific US covered-beverage revenue proxy separating producer/restaurant exposure from grocery retailers. Geographic mix, drink mix and the tax's product coverage are not separately disclosed; use a wide sensitivity range, not a measured share. · Company-specific estimate: Company-specific US covered-beverage revenue proxy separating producer/restaurant exposure from grocery retailers. Geographic mix, drink mix and the tax's product coverage are not separately disclosed; use a wide sensitivity range, not a measured share. |
| PEP | us_sweetened_beverage_revenue_share | 0.1 | 0.05 | 0.2 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/77476/000007747626000007/0000077476-26-000007-index.htm · estimate; Company-specific estimate: Company-specific US covered-beverage revenue proxy separating producer/restaurant exposure from grocery retailers. Geographic mix, drink mix and the tax's product coverage are not separately disclosed; use a wide sensitivity range, not a measured share. · Company-specific estimate: Company-specific US covered-beverage revenue proxy separating producer/restaurant exposure from grocery retailers. Geographic mix, drink mix and the tax's product coverage are not separately disclosed; use a wide sensitivity range, not a measured share. |

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
| exposure.us_sweetened_beverage_revenue_share | -0.0049515267 | -0.016186235 | 0.011234708 |
| assumption.elasticity | -0.0062621111 | -0.015655278 | 0.0093931666 |
| assumption.pass_through | -0.0067878675 | -0.015785738 | 0.0089978709 |
| assumption.recapture | -0.013530633 | -0.0067653165 | 0.0067653165 |
| assumption.price_per_oz | -0.0096867031 | -0.0077493625 | 0.0019373406 |

Dominant configured driver: `us_sweetened_beverage_revenue_share` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.


## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 13 unchecked in-scope exposure values; 4 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

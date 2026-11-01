# Import tariffs on consumer goods

Policy `consumer_retail/import_tariffs` · evidence checkpoint 2026-11-01 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

A tariff on imported goods raises retailers' merchandise costs; they pass part of it to shoppers, who buy a little less.

Duration: `permanent`. Default inputs: `{"tariff_pct": 20.0}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| cost | unavailable / unavailable | {"exposed_cost_share": "exposure.us_import_share_of_cogs", "shock_pct": "input.tariff_pct / 100", "pass_through": "assumption.pass_through", "elasticity": "assumption.elasticity"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://www.aeaweb.org/doi/10.1257/jep.33.4.187
- https://www.aeaweb.org/articles?id=10.1257/aeri.20190536

| Company | Configured status | Basis |
|---|---|---|
| WMT | included | Import duties raise importer input costs after partial pass-through. |
| TGT | included | Import duties raise importer input costs after partial pass-through. |
| COST | included | Import duties raise importer input costs after partial pass-through. |
| AMZN | included | Import duties raise importer input costs after partial pass-through. |
| NKE | included | Import duties raise importer input costs after partial pass-through. |
| HD | included | Import duties raise importer input costs after partial pass-through. |
| LOW | included | Import duties raise importer input costs after partial pass-through. |
| KR | included | Import duties raise importer input costs after partial pass-through. |
| DG | included | Import duties raise importer input costs after partial pass-through. |
| DLTR | included | Import duties raise importer input costs after partial pass-through. |
| TJX | included | Import duties raise importer input costs after partial pass-through. |
| ROST | included | Import duties raise importer input costs after partial pass-through. |
| SBUX | included | Import duties raise importer input costs after partial pass-through. |
| MCD | included | Import duties raise importer input costs after partial pass-through. |
| KO | included | Import duties raise importer input costs after partial pass-through. |
| PEP | included | Import duties raise importer input costs after partial pass-through. |
| PG | included | Import duties raise importer input costs after partial pass-through. |
| CL | included | Import duties raise importer input costs after partial pass-through. |
| ULTA | included | Import duties raise importer input costs after partial pass-through. |
| BBY | included | Import duties raise importer input costs after partial pass-through. |
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
| WMT | us_import_share_of_cogs | 0.27 | 0.2 | 0.33 | UNVERIFIED | https://www.foodbusinessnews.net/articles/28068-walmart-ready-for-tariff-clouded-trade-environment · estimate; CFO Rainey (Apr 9 2025): 'more than two-thirds of what we sell in the US is made, grown or assembled in the US'; under one-third imported × ~81% US share of sales; high allows for imported parts in US-assembled goods. · CFO Rainey (Apr 9 2025): 'more than two-thirds of what we sell in the US is made, grown or assembled in the US'; under one-third imported × ~81% US share of sales; high allows for imported parts in US-assembled goods. |
| TGT | us_import_share_of_cogs | 0.5 | 0.35 | 0.6 | UNVERIFIED | No source URL · estimate; Not disclosed. FY2025 10-K mix: apparel $15.7B, home $15.6B and hardlines $15.8B (45% of net sales) are largely imported; food & beverage $24.1B and household essentials $18.0B mostly domestic. · Not disclosed. FY2025 10-K mix: apparel $15.7B, home $15.6B and hardlines $15.8B (45% of net sales) are largely imported; food & beverage $24.1B and household essentials $18.0B mostly domestic. |
| COST | us_import_share_of_cogs | 0.24 | 0.18 | 0.28 | UNVERIFIED | https://www.nbcsandiego.com/news/business/money-report/costco-tops-earnings-and-revenue-estimates-as-sales-jump-8/3836279/ · CFO Millerchip, May 29 2025 earnings call: about a third of Costco's US sales are imported goods; China about 8% of US sales; One-third × US share of merchandise costs (FY2026 10-K: US $191,440M of $264,279M = 72%) = 0.24; low allows for gasoline and fresh food being mostly domestic. · One-third × US share of merchandise costs (FY2026 10-K: US $191,440M of $264,279M = 72%) = 0.24; low allows for gasoline and fresh food being mostly domestic. |
| AMZN | us_import_share_of_cogs | 0.15 | 0.1 | 0.25 | UNVERIFIED | No source URL · estimate; 2025 10-K: cost of sales $356,414M includes shipping and digital content; first-party online + physical store sales are $291,848M worldwide, ~60% US, a large share imported. · 2025 10-K: cost of sales $356,414M includes shipping and digital content; first-party online + physical store sales are $291,848M worldwide, ~60% US, a large share imported. |
| NKE | us_import_share_of_cogs | 0.42 | 0.38 | 0.44 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/320187/000032018726000088/nke-20260531.htm · Nike FY2026 10-K: 'Nearly all footwear, apparel and equipment products are manufactured outside the United States'; US ~44% of revenues; US-bound product cost ≈ US revenue share; base trims freight and other non-product cost of sales. · US-bound product cost ≈ US revenue share; base trims freight and other non-product cost of sales. |
| HD | us_import_share_of_cogs | 0.37 | 0.28 | 0.45 | UNVERIFIED | https://www.retaildive.com/news/home-depot-not-raise-prices-tariffs-first-quarter/748594/ · Home Depot Q1 FY2025 call (May 20 2025): over 50% of purchases are sourced in the US; Under half of purchases imported × ~92% US share of sales caps the share near 0.45; base assumes ~40% of US purchases are imported. · Under half of purchases imported × ~92% US share of sales caps the share near 0.45; base assumes ~40% of US purchases are imported. |
| LOW | us_import_share_of_cogs | 0.37 | 0.28 | 0.45 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Home improvement; median base and outer low/high from HD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Home improvement; median base and outer low/high from HD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| KR | us_import_share_of_cogs | 0.27 | 0.18 | 0.6 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Groceries and discount retail; median base and outer low/high from WMT/COST/TGT in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Groceries and discount retail; median base and outer low/high from WMT/COST/TGT in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| DG | us_import_share_of_cogs | 0.27 | 0.18 | 0.6 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Groceries and discount retail; median base and outer low/high from WMT/COST/TGT in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Groceries and discount retail; median base and outer low/high from WMT/COST/TGT in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| DLTR | us_import_share_of_cogs | 0.27 | 0.18 | 0.6 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Groceries and discount retail; median base and outer low/high from WMT/COST/TGT in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Groceries and discount retail; median base and outer low/high from WMT/COST/TGT in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| TJX | us_import_share_of_cogs | 0.46 | 0.35 | 0.6 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Apparel and specialty retail; median base and outer low/high from TGT/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Apparel and specialty retail; median base and outer low/high from TGT/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| ROST | us_import_share_of_cogs | 0.46 | 0.35 | 0.6 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Apparel and specialty retail; median base and outer low/high from TGT/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Apparel and specialty retail; median base and outer low/high from TGT/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| SBUX | us_import_share_of_cogs | 0.27 | 0.18 | 0.44 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Restaurants and consumer staples; median base and outer low/high from WMT/COST/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Restaurants and consumer staples; median base and outer low/high from WMT/COST/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| MCD | us_import_share_of_cogs | 0.27 | 0.18 | 0.44 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Restaurants and consumer staples; median base and outer low/high from WMT/COST/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Restaurants and consumer staples; median base and outer low/high from WMT/COST/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| KO | us_import_share_of_cogs | 0.27 | 0.18 | 0.44 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Restaurants and consumer staples; median base and outer low/high from WMT/COST/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Restaurants and consumer staples; median base and outer low/high from WMT/COST/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| PEP | us_import_share_of_cogs | 0.27 | 0.18 | 0.44 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Restaurants and consumer staples; median base and outer low/high from WMT/COST/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Restaurants and consumer staples; median base and outer low/high from WMT/COST/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| PG | us_import_share_of_cogs | 0.27 | 0.18 | 0.44 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Restaurants and consumer staples; median base and outer low/high from WMT/COST/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Restaurants and consumer staples; median base and outer low/high from WMT/COST/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| CL | us_import_share_of_cogs | 0.27 | 0.18 | 0.44 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Restaurants and consumer staples; median base and outer low/high from WMT/COST/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Restaurants and consumer staples; median base and outer low/high from WMT/COST/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| ULTA | us_import_share_of_cogs | 0.46 | 0.35 | 0.6 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Apparel and specialty retail; median base and outer low/high from TGT/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Apparel and specialty retail; median base and outer low/high from TGT/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| BBY | us_import_share_of_cogs | 0.46 | 0.35 | 0.6 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Apparel and specialty retail; median base and outer low/high from TGT/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Apparel and specialty retail; median base and outer low/high from TGT/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |

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
| assumption.pass_through | -0.26990214 | -0.12693137 | 0.14297077 |
| exposure.us_import_share_of_cogs | -0.14313696 | -0.27477872 | 0.13164176 |
| assumption.elasticity | -0.16761861 | -0.22656036 | 0.058941749 |

Dominant configured driver: `pass_through` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.

- REVIEW WMT: EPS -52.9%; Reported EPS denominator 2.73; dominant NI channel: Tariff on imported merchandise; estimated exposures: us_import_share_of_cogs. Review reported earnings, exposure denominator and linear transmission before use. Default scenario; realistic range not independently verified.
- REVIEW TGT: EPS -87.2%; Reported EPS denominator 8.13; dominant NI channel: Tariff on imported merchandise; estimated exposures: us_import_share_of_cogs. Review reported earnings, exposure denominator and linear transmission before use. Default scenario; realistic range not independently verified.
- REVIEW KR: EPS -272.0%; Reported EPS denominator 1.54; dominant NI channel: Tariff on imported merchandise; estimated exposures: us_import_share_of_cogs. Review reported earnings, exposure denominator and linear transmission before use. Default scenario; realistic range not independently verified.
- REVIEW BBY: EPS -109.4%; Reported EPS denominator 5.04; dominant NI channel: Tariff on imported merchandise; estimated exposures: us_import_share_of_cogs. Review reported earnings, exposure denominator and linear transmission before use. Default scenario; realistic range not independently verified.

## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 20 unchecked in-scope exposure values; 2 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

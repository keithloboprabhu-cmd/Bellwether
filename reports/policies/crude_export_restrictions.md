# Crude oil export restrictions

Policy `energy_resources/crude_export_restrictions` · reviewed 2026-10-31 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

Limits on US crude exports trap light crude at home and open a discount between US (WTI) and world (Brent) prices. US producers get less for their barrels; US refiners buy cheaper crude while product prices stay tied to world markets, so integrated XOM is roughly hedged, CVX loses slightly and COP takes the full hit. The likely rise in world prices, which would help the majors' overseas output, is not modeled. LNG export limits are not covered.

Duration: `permanent`. Default inputs: `{"restricted_pct": 50.0}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| price | unavailable / unavailable | {"d_price": "-derived.discount_pct", "exposed_revenue_share": "exposure.us_crude_sales_share"} |
| cost | unavailable / unavailable | {"exposed_cost_share": "exposure.us_refinery_domestic_crude_cost_share", "shock_pct": "-derived.discount_pct", "pass_through": "assumption.refiner_pass_through"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://www.eia.gov/analysis/requests/crude-exports
- https://www.sec.gov/Archives/edgar/data/1163165/000116316526000009/cop-20251231.htm

| Company | Configured status | Basis |
|---|---|---|
| XOM | included | Domestic upstream prices fall; refiner feedstock savings are a separate channel. |
| CVX | included | Domestic upstream prices fall; refiner feedstock savings are a separate channel. |
| COP | included | Domestic upstream prices fall; refiner feedstock savings are a separate channel. |
| NEE | outside_scope | This scenario covers US upstream crude sales and refinery feedstock savings, not oilfield-service orders or utilities. |
| FSLR | outside_scope | This scenario covers US upstream crude sales and refinery feedstock savings, not oilfield-service orders or utilities. |
| FCX | outside_scope | This scenario covers US upstream crude sales and refinery feedstock savings, not oilfield-service orders or utilities. |
| EOG | included | Domestic upstream prices fall; refiner feedstock savings are a separate channel. |
| OXY | included | Domestic upstream prices fall; refiner feedstock savings are a separate channel. |
| DVN | included | Domestic upstream prices fall; refiner feedstock savings are a separate channel. |
| SLB | outside_scope | This scenario covers US upstream crude sales and refinery feedstock savings, not oilfield-service orders or utilities. |
| HAL | outside_scope | This scenario covers US upstream crude sales and refinery feedstock savings, not oilfield-service orders or utilities. |
| WMB | outside_scope | This scenario covers US upstream crude sales and refinery feedstock savings, not oilfield-service orders or utilities. |
| PSX | included | Domestic upstream prices fall; refiner feedstock savings are a separate channel. |
| VLO | included | Domestic upstream prices fall; refiner feedstock savings are a separate channel. |
| MPC | included | Domestic upstream prices fall; refiner feedstock savings are a separate channel. |
| DUK | outside_scope | This scenario covers US upstream crude sales and refinery feedstock savings, not oilfield-service orders or utilities. |
| SO | outside_scope | This scenario covers US upstream crude sales and refinery feedstock savings, not oilfield-service orders or utilities. |
| AEP | outside_scope | This scenario covers US upstream crude sales and refinery feedstock savings, not oilfield-service orders or utilities. |
| EXC | outside_scope | This scenario covers US upstream crude sales and refinery feedstock savings, not oilfield-service orders or utilities. |
| CEG | outside_scope | This scenario covers US upstream crude sales and refinery feedstock savings, not oilfield-service orders or utilities. |

## B. Every in-scope exposure

Exact numeric checks are distinguished from filing links and estimates. UNVERIFIED values are retained, not silently replaced. Historical observed low/high values are not forecast confidence intervals.

| Company | Exposure | Base | Low | High | Exact-source status | Primary source / location / rationale |
|---|---|---:|---:|---:|---|---|
| XOM | us_crude_sales_share | 0.074 | 0.06 | 0.09 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/xom-20251231.htm · estimate; 2025 10-K US liquids production 1,522 kb/d; ~70% assumed crude (rest NGLs) × ~$63/bbl × 365 ≈ $24.5B of $332B revenue. · 2025 10-K US liquids production 1,522 kb/d; ~70% assumed crude (rest NGLs) × ~$63/bbl × 365 ≈ $24.5B of $332B revenue. |
| XOM | us_refinery_domestic_crude_cost_share | 0.115 | 0.08 | 0.14 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/xom-20251231.htm · estimate; 2025 10-K US refinery throughput 1,927 kb/d × $65 × 365 ≈ $45.7B; ~70% assumed domestic crude; ÷ $278.6B cost of revenue. · 2025 10-K US refinery throughput 1,927 kb/d × $65 × 365 ≈ $45.7B; ~70% assumed domestic crude; ÷ $278.6B cost of revenue. |
| CVX | us_crude_sales_share | 0.1 | 0.08 | 0.12 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/93410/000009341026000078/cvx-20251231.htm · estimate; 2025 10-K US liquids 1,341 kb/d at $48.13 = $23.6B (12.5% of revenue); ~80% of liquids revenue assumed crude (NGLs sell far lower). · 2025 10-K US liquids 1,341 kb/d at $48.13 = $23.6B (12.5% of revenue); ~80% of liquids revenue assumed crude (NGLs sell far lower). |
| CVX | us_refinery_domestic_crude_cost_share | 0.137 | 0.09 | 0.18 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/93410/000009341026000078/cvx-20251231.htm · estimate; 2025 10-K US refinery crude inputs 1,038 kb/d × $65 × 365 ≈ $24.6B; ~60% assumed domestic (10-K says CVX runs both imported and domestic crude; West Coast plants import heavily); ÷ $108.2B cost of revenue. · 2025 10-K US refinery crude inputs 1,038 kb/d × $65 × 365 ≈ $24.6B; ~60% assumed domestic (10-K says CVX runs both imported and domestic crude; West Coast plants import heavily); ÷ $108.2B cost of revenue. |
| COP | us_crude_sales_share | 0.372 | 0.33 | 0.4 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1163165/000116316526000009/cop-20251231.htm · COP 2025 10-K: Alaska crude 177 kb/d at $71.79, Lower 48 crude 749 kb/d at $63.18 → $21.9B of $58.9B revenue; Range allows for marketing revenue swings in the denominator. · Range allows for marketing revenue swings in the denominator. |
| COP | us_refinery_domestic_crude_cost_share | 0 | 0 | 0 | UNVERIFIED | No source URL · estimate; COP has no refining since the 2012 Phillips 66 spin-off. · COP has no refining since the 2012 Phillips 66 spin-off. |
| EOG | us_crude_sales_share | 0.1 | 0.06 | 0.4 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Oil production and services; median base and outer low/high from XOM/CVX/COP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Oil production and services; median base and outer low/high from XOM/CVX/COP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| EOG | us_refinery_domestic_crude_cost_share | 0 | 0 | 0 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/821189/000082118926000054/0000821189-26-000054-index.htm · estimate; Company-specific scope estimate: Domestic crude purchased by refiners. Upstream-only producers, service contractors and gas pipelines do not inherit refinery feedstock costs. This is a model boundary, not a reported zero measurement. · Company-specific scope estimate: Domestic crude purchased by refiners. Upstream-only producers, service contractors and gas pipelines do not inherit refinery feedstock costs. This is a model boundary, not a reported zero measurement. |
| OXY | us_crude_sales_share | 0.1 | 0.06 | 0.4 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Oil production and services; median base and outer low/high from XOM/CVX/COP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Oil production and services; median base and outer low/high from XOM/CVX/COP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| OXY | us_refinery_domestic_crude_cost_share | 0 | 0 | 0 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/797468/000162828026009059/0001628280-26-009059-index.htm · estimate; Company-specific scope estimate: Domestic crude purchased by refiners. Upstream-only producers, service contractors and gas pipelines do not inherit refinery feedstock costs. This is a model boundary, not a reported zero measurement. · Company-specific scope estimate: Domestic crude purchased by refiners. Upstream-only producers, service contractors and gas pipelines do not inherit refinery feedstock costs. This is a model boundary, not a reported zero measurement. |
| DVN | us_crude_sales_share | 0.1 | 0.06 | 0.4 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Oil production and services; median base and outer low/high from XOM/CVX/COP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Oil production and services; median base and outer low/high from XOM/CVX/COP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| DVN | us_refinery_domestic_crude_cost_share | 0 | 0 | 0 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1090012/000119312526056485/0001193125-26-056485-index.htm · estimate; Company-specific scope estimate: Domestic crude purchased by refiners. Upstream-only producers, service contractors and gas pipelines do not inherit refinery feedstock costs. This is a model boundary, not a reported zero measurement. · Company-specific scope estimate: Domestic crude purchased by refiners. Upstream-only producers, service contractors and gas pipelines do not inherit refinery feedstock costs. This is a model boundary, not a reported zero measurement. |
| PSX | us_crude_sales_share | 0 | 0 | 0 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1534701/000153470126000006/0001534701-26-000006-index.htm · estimate; Company-specific scope estimate: Direct upstream crude sales, excluding oilfield-service, pipeline and stand-alone refining revenue. This is a model boundary, not a reported zero measurement. · Company-specific scope estimate: Direct upstream crude sales, excluding oilfield-service, pipeline and stand-alone refining revenue. This is a model boundary, not a reported zero measurement. |
| PSX | us_refinery_domestic_crude_cost_share | 0.126 | 0.08 | 0.18 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Refining; median base and outer low/high from XOM/CVX in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Refining; median base and outer low/high from XOM/CVX in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| VLO | us_crude_sales_share | 0 | 0 | 0 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1035002/000162828026011499/0001628280-26-011499-index.htm · estimate; Company-specific scope estimate: Direct upstream crude sales, excluding oilfield-service, pipeline and stand-alone refining revenue. This is a model boundary, not a reported zero measurement. · Company-specific scope estimate: Direct upstream crude sales, excluding oilfield-service, pipeline and stand-alone refining revenue. This is a model boundary, not a reported zero measurement. |
| VLO | us_refinery_domestic_crude_cost_share | 0.126 | 0.08 | 0.18 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Refining; median base and outer low/high from XOM/CVX in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Refining; median base and outer low/high from XOM/CVX in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| MPC | us_crude_sales_share | 0 | 0 | 0 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1510295/000151029526000009/0001510295-26-000009-index.htm · estimate; Company-specific scope estimate: Direct upstream crude sales, excluding oilfield-service, pipeline and stand-alone refining revenue. This is a model boundary, not a reported zero measurement. · Company-specific scope estimate: Direct upstream crude sales, excluding oilfield-service, pipeline and stand-alone refining revenue. This is a model boundary, not a reported zero measurement. |
| MPC | us_refinery_domestic_crude_cost_share | 0.126 | 0.08 | 0.18 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Refining; median base and outer low/high from XOM/CVX in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Refining; median base and outer low/high from XOM/CVX in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |

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
| exposure.us_refinery_domestic_crude_cost_share | -0.00531032 | 0.011001072 | 0.016311392 |
| assumption.refiner_pass_through | 0.0087999884 | -0.0061023379 | 0.014902326 |
| exposure.us_crude_sales_share | 0.0068217322 | -0.0063126683 | 0.013134401 |
| assumption.full_ban_discount | 0.0014195289 | 0.0056781157 | 0.0042585868 |

Dominant configured driver: `us_refinery_domestic_crude_cost_share` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.


## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 18 unchecked in-scope exposure values; 2 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

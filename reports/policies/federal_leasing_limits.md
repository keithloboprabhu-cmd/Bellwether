# Federal oil & gas leasing limits

Policy `energy_resources/federal_leasing_limits` · evidence checkpoint 2026-11-01 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

A pause on new oil and gas leases on federal lands and waters. Existing leases keep producing, so output from federal acreage declines gradually as it depletes; the input is the eventual percentage drop in each company's federal-land production. Modeled with the price channel as lost revenue net of avoided costs (royalties, production taxes, operating costs), because company-wide contribution margins (16% for XOM, which includes refining) understate upstream margins. Any world oil-price response is ignored (federal lands are ~3% of world supply).

Duration: `permanent`. Default inputs: `{"production_decline_pct": 10.0}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| price | unavailable / unavailable | {"d_price": "-input.production_decline_pct / 100", "exposed_revenue_share": "exposure.federal_upstream_revenue_share", "offset_share": "assumption.avoided_cost_share"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://www.eia.gov/todayinenergy/detail.php?id=65804

| Company | Configured status | Basis |
|---|---|---|
| XOM | included | Limits reduce federal-lease production revenue. |
| CVX | included | Limits reduce federal-lease production revenue. |
| COP | included | Limits reduce federal-lease production revenue. |
| NEE | outside_scope | Production revenue on federal oil/gas leases is required. Contractors, refiners and utilities do not own this modeled upstream exposure. |
| FSLR | outside_scope | Production revenue on federal oil/gas leases is required. Contractors, refiners and utilities do not own this modeled upstream exposure. |
| FCX | outside_scope | Production revenue on federal oil/gas leases is required. Contractors, refiners and utilities do not own this modeled upstream exposure. |
| EOG | included | Limits reduce federal-lease production revenue. |
| OXY | included | Limits reduce federal-lease production revenue. |
| DVN | included | Limits reduce federal-lease production revenue. |
| SLB | outside_scope | Production revenue on federal oil/gas leases is required. Contractors, refiners and utilities do not own this modeled upstream exposure. |
| HAL | outside_scope | Production revenue on federal oil/gas leases is required. Contractors, refiners and utilities do not own this modeled upstream exposure. |
| WMB | outside_scope | Production revenue on federal oil/gas leases is required. Contractors, refiners and utilities do not own this modeled upstream exposure. |
| PSX | outside_scope | Production revenue on federal oil/gas leases is required. Contractors, refiners and utilities do not own this modeled upstream exposure. |
| VLO | outside_scope | Production revenue on federal oil/gas leases is required. Contractors, refiners and utilities do not own this modeled upstream exposure. |
| MPC | outside_scope | Production revenue on federal oil/gas leases is required. Contractors, refiners and utilities do not own this modeled upstream exposure. |
| DUK | outside_scope | Production revenue on federal oil/gas leases is required. Contractors, refiners and utilities do not own this modeled upstream exposure. |
| SO | outside_scope | Production revenue on federal oil/gas leases is required. Contractors, refiners and utilities do not own this modeled upstream exposure. |
| AEP | outside_scope | Production revenue on federal oil/gas leases is required. Contractors, refiners and utilities do not own this modeled upstream exposure. |
| EXC | outside_scope | Production revenue on federal oil/gas leases is required. Contractors, refiners and utilities do not own this modeled upstream exposure. |
| CEG | outside_scope | Production revenue on federal oil/gas leases is required. Contractors, refiners and utilities do not own this modeled upstream exposure. |

## B. Every in-scope exposure

Exact numeric checks are distinguished from filing links and estimates. UNVERIFIED values are retained, not silently replaced. Historical observed low/high values are not forecast confidence intervals.

| Company | Exposure | Base | Low | High | Exact-source status | Primary source / location / rationale |
|---|---|---:|---:|---:|---|---|
| XOM | federal_upstream_revenue_share | 0.025 | 0.015 | 0.04 | UNVERIFIED | https://www.eia.gov/todayinenergy/detail.php?id=65804 · estimate; US upstream (1,522 kb/d liquids + gas per 2025 10-K) is ~10% of revenue; ~25% of it assumed federal (New Mexico Delaware Basin federal acreage; Midland/Pioneer is mostly private Texas land). EIA - federal onshore 1.7 + offshore 1.8 of 13.2 mb/d US crude in 2024 (~27%). · US upstream (1,522 kb/d liquids + gas per 2025 10-K) is ~10% of revenue; ~25% of it assumed federal (New Mexico Delaware Basin federal acreage; Midland/Pioneer is mostly private Texas land). EIA - federal onshore 1.7 + offshore 1.8 of 13.2 mb/d US crude in 2024 (~27%). |
| CVX | federal_upstream_revenue_share | 0.038 | 0.025 | 0.05 | UNVERIFIED | https://www.eia.gov/todayinenergy/detail.php?id=65804 · estimate; US upstream ≈ $26B (10-K - 1,341 kb/d liquids at $48.13 + 3,099 MMcf/d gas at $2.05) = 14% of revenue; ~28% assumed federal (Gulf of America deepwater - Anchor, Ballymore, Stampede, Whale - plus New Mexico Permian). · US upstream ≈ $26B (10-K - 1,341 kb/d liquids at $48.13 + 3,099 MMcf/d gas at $2.05) = 14% of revenue; ~28% assumed federal (Gulf of America deepwater - Anchor, Ballymore, Stampede, Whale - plus New Mexico Permian). |
| COP | federal_upstream_revenue_share | 0.08 | 0.05 | 0.12 | UNVERIFIED | https://www.eia.gov/todayinenergy/detail.php?id=65804 · estimate; US production revenue ≈ 44% of total (10-K - Lower 48 1,484 kboe/d, Alaska 199 kboe/d); ~18% assumed federal (New Mexico Delaware Basin from Concho, NPR-A Greater Mooses Tooth; Prudhoe/Kuparuk are state lands). · US production revenue ≈ 44% of total (10-K - Lower 48 1,484 kboe/d, Alaska 199 kboe/d); ~18% assumed federal (New Mexico Delaware Basin from Concho, NPR-A Greater Mooses Tooth; Prudhoe/Kuparuk are state lands). |
| EOG | federal_upstream_revenue_share | 0.038 | 0.015 | 0.12 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Oil production and services; median base and outer low/high from XOM/CVX/COP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Oil production and services; median base and outer low/high from XOM/CVX/COP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| OXY | federal_upstream_revenue_share | 0.038 | 0.015 | 0.12 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Oil production and services; median base and outer low/high from XOM/CVX/COP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Oil production and services; median base and outer low/high from XOM/CVX/COP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| DVN | federal_upstream_revenue_share | 0.038 | 0.015 | 0.12 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Oil production and services; median base and outer low/high from XOM/CVX/COP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Oil production and services; median base and outer low/high from XOM/CVX/COP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |

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
| exposure.federal_upstream_revenue_share | -0.0047428551 | -0.013250959 | 0.0085081044 |
| assumption.avoided_cost_share | -0.01008014 | -0.0057600801 | 0.0043200601 |

Dominant configured driver: `federal_upstream_revenue_share` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.


## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 6 unchecked in-scope exposure values; 1 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

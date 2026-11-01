# New federal infrastructure program

Policy `industrials/infrastructure_spending` · evidence checkpoint 2026-11-01 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

New federal money for roads, bridges, water and the grid flows to contractors, who buy machinery and steel. Nucor and Caterpillar capture the most; GE Aerospace and Honeywell capture little.

Duration: `years:5`. Default inputs: `{"program_busd": 50.0}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| demand_transfer | unavailable / unavailable | {"total_transfer_musd": "input.program_busd * 1000", "mpc": "assumption.outlay_rate", "capture_share": "exposure.ind_infrastructure_capture_share"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://www.congress.gov/bill/117th-congress/house-bill/3684

| Company | Configured status | Basis |
|---|---|---|
| CAT | included | Public infrastructure purchases raise captured equipment/material demand. |
| DE | included | Public infrastructure purchases raise captured equipment/material demand. |
| GE | included | Public infrastructure purchases raise captured equipment/material demand. |
| HON | included | Public infrastructure purchases raise captured equipment/material demand. |
| MMM | included | Public infrastructure purchases raise captured equipment/material demand. |
| NUE | included | Public infrastructure purchases raise captured equipment/material demand. |
| BA | outside_scope | Boeing aerospace revenue is outside the domestic infrastructure equipment/materials allocation. |
| ETN | included | Public infrastructure purchases raise captured equipment/material demand. |
| EMR | included | Public infrastructure purchases raise captured equipment/material demand. |
| ITW | included | Public infrastructure purchases raise captured equipment/material demand. |
| PH | included | Public infrastructure purchases raise captured equipment/material demand. |
| CMI | included | Public infrastructure purchases raise captured equipment/material demand. |
| PCAR | included | Public infrastructure purchases raise captured equipment/material demand. |
| DOV | included | Public infrastructure purchases raise captured equipment/material demand. |
| ROK | included | Public infrastructure purchases raise captured equipment/material demand. |
| STLD | included | Public infrastructure purchases raise captured equipment/material demand. |
| CLF | included | Public infrastructure purchases raise captured equipment/material demand. |
| CARR | included | Public infrastructure purchases raise captured equipment/material demand. |
| OTIS | included | Public infrastructure purchases raise captured equipment/material demand. |
| IR | included | Public infrastructure purchases raise captured equipment/material demand. |
| GEV | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |

## B. Every in-scope exposure

Exact numeric checks are distinguished from filing links and estimates. UNVERIFIED values are retained, not silently replaced. Historical observed low/high values are not forecast confidence intervals.

| Company | Exposure | Base | Low | High | Exact-source status | Primary source / location / rationale |
|---|---|---:|---:|---:|---|---|
| CAT | ind_infrastructure_capture_share | 0.01 | 0.004 | 0.02 | UNVERIFIED | No source URL · estimate; Equipment is a modest share of highway and bridge construction cost, and Caterpillar is the largest US construction-equipment maker; about 1 cent of each new federal infrastructure dollar becomes Caterpillar revenue (machines bought or rented by contractors, plus parts). · Equipment is a modest share of highway and bridge construction cost, and Caterpillar is the largest US construction-equipment maker; about 1 cent of each new federal infrastructure dollar becomes Caterpillar revenue (machines bought or rented by contractors, plus parts). |
| DE | ind_infrastructure_capture_share | 0.004 | 0.001 | 0.008 | UNVERIFIED | No source URL · estimate; Deere's Construction & Forestry segment (road-building via Wirtgen, plus earthmoving) is much smaller than Caterpillar's construction business, so it captures well under half of Caterpillar's share. · Deere's Construction & Forestry segment (road-building via Wirtgen, plus earthmoving) is much smaller than Caterpillar's construction business, so it captures well under half of Caterpillar's share. |
| GE | ind_infrastructure_capture_share | 0.0002 | 0 | 0.001 | UNVERIFIED | No source URL · estimate; GE Aerospace sells aircraft engines and services; roads, bridges and water projects buy almost nothing from it (airport grants do not buy engines). · GE Aerospace sells aircraft engines and services; roads, bridges and water projects buy almost nothing from it (airport grants do not buy engines). |
| HON | ind_infrastructure_capture_share | 0.001 | 0 | 0.003 | UNVERIFIED | No source URL · estimate; Honeywell sells building automation, controls and safety products that go into public buildings, transit and utility projects, but roads and bridges buy little from it. · Honeywell sells building automation, controls and safety products that go into public buildings, transit and utility projects, but roads and bridges buy little from it. |
| MMM | ind_infrastructure_capture_share | 0.002 | 0.0005 | 0.004 | UNVERIFIED | No source URL · estimate; 3M sells reflective sheeting for road signs, pavement markings and other transportation-safety products, a small slice of road-project budgets. · 3M sells reflective sheeting for road signs, pavement markings and other transportation-safety products, a small slice of road-project budgets. |
| NUE | ind_infrastructure_capture_share | 0.015 | 0.008 | 0.025 | UNVERIFIED | No source URL · estimate; Rebar, beams, plate, piling (Skyline Steel) and fabricated products are a meaningful share of bridge, road and water project costs; Nucor is the largest US steelmaker, and Buy America rules steer federally funded steel to US mills. · Rebar, beams, plate, piling (Skyline Steel) and fabricated products are a meaningful share of bridge, road and water project costs; Nucor is the largest US steelmaker, and Buy America rules steer federally funded steel to US mills. |
| ETN | ind_infrastructure_capture_share | 0.002 | 0 | 0.02 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| EMR | ind_infrastructure_capture_share | 0.002 | 0 | 0.02 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| ITW | ind_infrastructure_capture_share | 0.002 | 0 | 0.02 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| PH | ind_infrastructure_capture_share | 0.002 | 0 | 0.02 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| CMI | ind_infrastructure_capture_share | 0.002 | 0 | 0.02 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| PCAR | ind_infrastructure_capture_share | 0.002 | 0 | 0.02 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| DOV | ind_infrastructure_capture_share | 0.002 | 0 | 0.02 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| ROK | ind_infrastructure_capture_share | 0.002 | 0 | 0.02 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| STLD | ind_infrastructure_capture_share | 0.015 | 0.008 | 0.025 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Steel production; median base and outer low/high from NUE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Steel production; median base and outer low/high from NUE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| CLF | ind_infrastructure_capture_share | 0.015 | 0.008 | 0.025 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Steel production; median base and outer low/high from NUE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Steel production; median base and outer low/high from NUE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| CARR | ind_infrastructure_capture_share | 0.002 | 0 | 0.02 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| OTIS | ind_infrastructure_capture_share | 0.002 | 0 | 0.02 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| IR | ind_infrastructure_capture_share | 0.002 | 0 | 0.02 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |

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
| exposure.ind_infrastructure_capture_share | 0.0011029789 | 0.032928388 | 0.031825409 |
| assumption.outlay_rate | 0.0033433522 | 0.0078011551 | 0.0044578029 |

Dominant configured driver: `ind_infrastructure_capture_share` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.


## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 19 unchecked in-scope exposure values; 1 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

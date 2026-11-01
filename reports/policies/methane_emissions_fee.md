# Methane emissions fee

Policy `energy_resources/methane_emissions_fee` · reviewed 2026-10-31 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

A per-tonne fee on methane from US oil and gas facilities, modeled on the IRA Waste Emissions Charge ($1,500/t once fully phased in), charged only on emissions above facility thresholds. The 2025 budget law pushed the charge back to 2034. Oil producers bear it; NEE, FSLR and FCX are essentially outside its scope. Even at the full rate the hit is small next to these companies' earnings.

Duration: `permanent`. Default inputs: `{"fee_per_ton": 1500.0}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| cost | unavailable / unavailable | {"exposed_cost_share": 0.0, "shock_pct": 0.0, "dcost_musd": "derived.fee_musd", "pass_through": "assumption.pass_through"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://www.everycrsreport.com/reports/R48906.html
- https://www.epa.gov/inflation-reduction-act/waste-emissions-charge
- https://corporate.exxonmobil.com/news/reporting-and-publications/sustainability-report/performance-data-table

| Company | Configured status | Basis |
|---|---|---|
| XOM | included | Fee raises covered oil/gas facility cost, not power combustion. |
| CVX | included | Fee raises covered oil/gas facility cost, not power combustion. |
| COP | included | Fee raises covered oil/gas facility cost, not power combustion. |
| NEE | outside_scope | Covered oil/gas-facility waste methane is distinct from combustion emissions or service-company footprints. |
| FSLR | outside_scope | Covered oil/gas-facility waste methane is distinct from combustion emissions or service-company footprints. |
| FCX | outside_scope | Covered oil/gas-facility waste methane is distinct from combustion emissions or service-company footprints. |
| EOG | included | Fee raises covered oil/gas facility cost, not power combustion. |
| OXY | included | Fee raises covered oil/gas facility cost, not power combustion. |
| DVN | included | Fee raises covered oil/gas facility cost, not power combustion. |
| SLB | outside_scope | Covered oil/gas-facility waste methane is distinct from combustion emissions or service-company footprints. |
| HAL | outside_scope | Covered oil/gas-facility waste methane is distinct from combustion emissions or service-company footprints. |
| WMB | included | Fee raises covered oil/gas facility cost, not power combustion. |
| PSX | included | Fee raises covered oil/gas facility cost, not power combustion. |
| VLO | included | Fee raises covered oil/gas facility cost, not power combustion. |
| MPC | included | Fee raises covered oil/gas facility cost, not power combustion. |
| DUK | outside_scope | Covered oil/gas-facility waste methane is distinct from combustion emissions or service-company footprints. |
| SO | outside_scope | Covered oil/gas-facility waste methane is distinct from combustion emissions or service-company footprints. |
| AEP | outside_scope | Covered oil/gas-facility waste methane is distinct from combustion emissions or service-company footprints. |
| EXC | outside_scope | Covered oil/gas-facility waste methane is distinct from combustion emissions or service-company footprints. |
| CEG | outside_scope | Covered oil/gas-facility waste methane is distinct from combustion emissions or service-company footprints. |

## B. Every in-scope exposure

Exact numeric checks are distinguished from filing links and estimates. UNVERIFIED values are retained, not silently replaced. Historical observed low/high values are not forecast confidence intervals.

| Company | Exposure | Base | Low | High | Exact-source status | Primary source / location / rationale |
|---|---|---:|---:|---:|---|---|
| XOM | us_methane_kt_ch4 | 96 | 60 | 130 | UNVERIFIED | https://corporate.exxonmobil.com/news/reporting-and-publications/sustainability-report/performance-data-table · estimate; XOM reports 0.16 Mt CH4 operated methane in 2024 (global); ~60% assumed US, where its unconventional (XTO/Permian) gas systems are. · XOM reports 0.16 Mt CH4 operated methane in 2024 (global); ~60% assumed US, where its unconventional (XTO/Permian) gas systems are. |
| CVX | us_methane_kt_ch4 | 55 | 30 | 100 | UNVERIFIED | No source URL · estimate; 2025 10-K US production 1,858 kboe/d (678 MMboe) × ~2.3 kg CO2e/boe methane intensity (CVX's 2028 target is 2) ÷ GWP 28 ≈ 56 kt CH4. · 2025 10-K US production 1,858 kboe/d (678 MMboe) × ~2.3 kg CO2e/boe methane intensity (CVX's 2028 target is 2) ÷ GWP 28 ≈ 56 kt CH4. |
| COP | us_methane_kt_ch4 | 61 | 40 | 90 | UNVERIFIED | https://www.conocophillips.com/sustainability/managing-climate-related-risks/metrics-targets · estimate; COP 2025 methane intensity 2.8 kg CO2e/BOE × 867 MMBOE ÷ GWP 28 ≈ 87 kt CH4; × 71% US production share. · COP 2025 methane intensity 2.8 kg CO2e/BOE × 867 MMBOE ÷ GWP 28 ≈ 87 kt CH4; × 71% US production share. |
| EOG | us_methane_kt_ch4 | 6.5849517 | 3.5917918 | 34.556189 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Oil production and services; median base and outer low/high from XOM/CVX/COP in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Oil production and services; median base and outer low/high from XOM/CVX/COP in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| OXY | us_methane_kt_ch4 | 6.2826468 | 3.4268982 | 32.969768 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Oil production and services; median base and outer low/high from XOM/CVX/COP in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Oil production and services; median base and outer low/high from XOM/CVX/COP in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| DVN | us_methane_kt_ch4 | 5.0009787 | 2.7278066 | 26.243893 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Oil production and services; median base and outer low/high from XOM/CVX/COP in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Oil production and services; median base and outer low/high from XOM/CVX/COP in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| WMB | us_methane_kt_ch4 | 3.4769429 | 1.8965143 | 18.246132 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Midstream pipelines; median base and outer low/high from XOM/CVX/COP in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Midstream pipelines; median base and outer low/high from XOM/CVX/COP in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| PSX | us_methane_kt_ch4 | 38.382888 | 21.008618 | 70.028725 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Refining; median base and outer low/high from XOM/CVX in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Refining; median base and outer low/high from XOM/CVX in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| VLO | us_methane_kt_ch4 | 35.573528 | 19.470933 | 64.903111 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Refining; median base and outer low/high from XOM/CVX in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Refining; median base and outer low/high from XOM/CVX in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| MPC | us_methane_kt_ch4 | 38.476543 | 21.059879 | 70.199597 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Refining; median base and outer low/high from XOM/CVX in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Refining; median base and outer low/high from XOM/CVX in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |

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
| assumption.chargeable_share | -0.00050456458 | -0.0020182583 | 0.0015136938 |
| exposure.us_methane_kt_ch4 | -0.00066929317 | -0.0021247966 | 0.0014555034 |
| assumption.pass_through | -0.0012038734 | -0.00096309872 | 0.00024077468 |

Dominant configured driver: `chargeable_share` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.


## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 10 unchecked in-scope exposure values; 2 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

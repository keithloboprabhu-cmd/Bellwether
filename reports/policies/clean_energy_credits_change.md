# Clean-energy tax credit change

Policy `energy_resources/clean_energy_credits_change` · evidence checkpoint 2026-11-01 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

Changes the value of clean-electricity credits (PTC/ITC, 45Y/48E) and the 45X manufacturing credit. A cut reduces NextEra's tax credits directly and First Solar's 45X credits (≈ all of its 2025 earnings), and lowers US module demand as solar projects pencil out less. Negative inputs are cuts; positive inputs are expansions. The oil majors and FCX have essentially no exposure.

Duration: `years:7`. Default inputs: `{"d_generation_credit_pct": -25.0, "d_manufacturing_credit_pct": -25.0}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| tax_credit | unavailable / unavailable | {"credit_rate": "input.d_generation_credit_pct / 100", "base_musd": "exposure.clean_generation_credits_musd"} |
| tax_credit | unavailable / unavailable | {"credit_rate": "input.d_manufacturing_credit_pct / 100", "base_musd": "exposure.manufacturing_credits_45x_musd"} |
| demand_volume | unavailable / unavailable | {"d_volume": "input.d_generation_credit_pct / 100 * assumption.module_demand_sensitivity", "exposed_revenue_share": "exposure.us_solar_module_revenue_share"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://www.sec.gov/Archives/edgar/data/37634/000075330826000015/nee-20251231.htm
- https://www.sec.gov/Archives/edgar/data/1274494/000127449426000021/fslr-20251231.htm

| Company | Configured status | Basis |
|---|---|---|
| XOM | outside_scope | No quantified qualifying generation/45X manufacturing credit or US solar-module demand in this model. Exelon is a separated transmission/distribution company. |
| CVX | outside_scope | No quantified qualifying generation/45X manufacturing credit or US solar-module demand in this model. Exelon is a separated transmission/distribution company. |
| COP | outside_scope | No quantified qualifying generation/45X manufacturing credit or US solar-module demand in this model. Exelon is a separated transmission/distribution company. |
| NEE | included | Default credit rollback reduces qualifying production benefits. |
| FSLR | included | Default credit rollback reduces qualifying production benefits. |
| FCX | unquantified | No quantified central exposure. The high sensitivity case represents uncertain qualifying molybdenum by-product production credits, not a reported credit stream or a credit for copper. |
| EOG | outside_scope | No quantified qualifying generation/45X manufacturing credit or US solar-module demand in this model. Exelon is a separated transmission/distribution company. |
| OXY | outside_scope | No quantified qualifying generation/45X manufacturing credit or US solar-module demand in this model. Exelon is a separated transmission/distribution company. |
| DVN | outside_scope | No quantified qualifying generation/45X manufacturing credit or US solar-module demand in this model. Exelon is a separated transmission/distribution company. |
| SLB | outside_scope | No quantified qualifying generation/45X manufacturing credit or US solar-module demand in this model. Exelon is a separated transmission/distribution company. |
| HAL | outside_scope | No quantified qualifying generation/45X manufacturing credit or US solar-module demand in this model. Exelon is a separated transmission/distribution company. |
| WMB | outside_scope | No quantified qualifying generation/45X manufacturing credit or US solar-module demand in this model. Exelon is a separated transmission/distribution company. |
| PSX | outside_scope | No quantified qualifying generation/45X manufacturing credit or US solar-module demand in this model. Exelon is a separated transmission/distribution company. |
| VLO | outside_scope | No quantified qualifying generation/45X manufacturing credit or US solar-module demand in this model. Exelon is a separated transmission/distribution company. |
| MPC | outside_scope | No quantified qualifying generation/45X manufacturing credit or US solar-module demand in this model. Exelon is a separated transmission/distribution company. |
| DUK | included | Default credit rollback reduces qualifying production benefits. |
| SO | included | Default credit rollback reduces qualifying production benefits. |
| AEP | included | Default credit rollback reduces qualifying production benefits. |
| EXC | outside_scope | No quantified qualifying generation/45X manufacturing credit or US solar-module demand in this model. Exelon is a separated transmission/distribution company. |
| CEG | included | Default credit rollback reduces qualifying production benefits. |

## B. Every in-scope exposure

Exact numeric checks are distinguished from filing links and estimates. UNVERIFIED values are retained, not silently replaced. Historical observed low/high values are not forecast confidence intervals.

| Company | Exposure | Base | Low | High | Exact-source status | Primary source / location / rationale |
|---|---|---:|---:|---:|---|---|
| NEE | clean_generation_credits_musd | 2,075 | 1,500 | 2,400 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/37634/000075330826000015/nee-20251231.htm · NEE 2025 10-K income-tax reconciliation: clean energy tax credits $(2,075)M in 2025 ($1,201M 2024; $605M 2023); Low end reflects that part of the credit value accrues to tax-equity partners/noncontrolling interests and that 2025 was a peak-growth year. · Low end reflects that part of the credit value accrues to tax-equity partners/noncontrolling interests and that 2025 was a peak-growth year. |
| NEE | manufacturing_credits_45x_musd | 0 | 0 | 0 | UNVERIFIED | No source URL · estimate; No §45X manufacturing. · No §45X manufacturing. |
| NEE | us_solar_module_revenue_share | 0 | 0 | 0 | UNVERIFIED | No source URL · estimate; Buys modules; does not sell them. · Buys modules; does not sell them. |
| FSLR | clean_generation_credits_musd | 0 | 0 | 0 | UNVERIFIED | No source URL · estimate; Sold its project development business; does not own generating fleet credits. · Sold its project development business; does not own generating fleet credits. |
| FSLR | manufacturing_credits_45x_musd | 1,600 | 1,400 | 1,800 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1274494/000127449426000021/fslr-20251231.htm · FSLR 2025 10-K: recognized $1.6 billion of Section 45X credits as a reduction to cost of sales in 2025 (~17¢/W for US-made modules); Range brackets US output growth (Louisiana plant) vs. lower volumes. · Range brackets US output growth (Louisiana plant) vs. lower volumes. |
| FSLR | us_solar_module_revenue_share | 0.957 | 0.9 | 0.97 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1274494/000127449426000021/fslr-20251231.htm · FSLR 2025 10-K: US net sales $4,994.7M of $5,219.4M (customer country of invoicing); Low end allows some US-invoiced sales for non-US projects. · Low end allows some US-invoiced sales for non-US projects. |
| DUK | clean_generation_credits_musd | 2,440.2369 | 1,764.0267 | 2,822.4427 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Utilities and generation; median base and outer low/high from NEE in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Utilities and generation; median base and outer low/high from NEE in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| DUK | manufacturing_credits_45x_musd | 0 | 0 | 0 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Utilities and generation; median base and outer low/high from NEE in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Utilities and generation; median base and outer low/high from NEE in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| DUK | us_solar_module_revenue_share | 0 | 0 | 0 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Utilities and generation; median base and outer low/high from NEE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Utilities and generation; median base and outer low/high from NEE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| SO | clean_generation_credits_musd | 2,237.0668 | 1,617.1567 | 2,587.4508 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Utilities and generation; median base and outer low/high from NEE in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Utilities and generation; median base and outer low/high from NEE in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| SO | manufacturing_credits_45x_musd | 0 | 0 | 0 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Utilities and generation; median base and outer low/high from NEE in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Utilities and generation; median base and outer low/high from NEE in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| SO | us_solar_module_revenue_share | 0 | 0 | 0 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Utilities and generation; median base and outer low/high from NEE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Utilities and generation; median base and outer low/high from NEE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| AEP | clean_generation_credits_musd | 1,655.9427 | 1,197.067 | 1,915.3072 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Utilities and generation; median base and outer low/high from NEE in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Utilities and generation; median base and outer low/high from NEE in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| AEP | manufacturing_credits_45x_musd | 0 | 0 | 0 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Utilities and generation; median base and outer low/high from NEE in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Utilities and generation; median base and outer low/high from NEE in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| AEP | us_solar_module_revenue_share | 0 | 0 | 0 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Utilities and generation; median base and outer low/high from NEE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Utilities and generation; median base and outer low/high from NEE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| CEG | clean_generation_credits_musd | 1,932.7658 | 1,397.1801 | 2,235.4881 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Utilities and generation; median base and outer low/high from NEE in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Utilities and generation; median base and outer low/high from NEE in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| CEG | manufacturing_credits_45x_musd | 0 | 0 | 0 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Utilities and generation; median base and outer low/high from NEE in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Utilities and generation; median base and outer low/high from NEE in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| CEG | us_solar_module_revenue_share | 0 | 0 | 0 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Utilities and generation; median base and outer low/high from NEE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Utilities and generation; median base and outer low/high from NEE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |

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
| exposure.clean_generation_credits_musd | -0.023064226 | -0.033744142 | 0.010679916 |
| assumption.module_demand_sensitivity | -0.028943804 | -0.031303058 | 0.0023592536 |
| exposure.manufacturing_credits_45x_musd | -0.029406404 | -0.030406915 | 0.0010005108 |
| exposure.us_solar_module_revenue_share | -0.029803194 | -0.029906734 | 0.00010354091 |

Dominant configured driver: `clean_generation_credits_musd` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.


## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 18 unchecked in-scope exposure values; 1 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

# Change in the US corporate tax rate

Policy `industrials/corporate_tax_rate_change` · reviewed 2026-10-31 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

A change in the 21% federal corporate rate hits only income earned in the US. Nucor earns almost all its profit at home and feels it fully; Honeywell, with most pretax income booked abroad, feels it least.

Duration: `permanent`. Default inputs: `{"d_rate_pts": 4.0}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| tax_rate | unavailable / unavailable | {"d_statutory_rate": "input.d_rate_pts / 100 * assumption.effective_share", "domestic_income_share": "exposure.ind_us_pretax_income_share"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://www.law.cornell.edu/uscode/text/26/11

| Company | Configured status | Basis |
|---|---|---|
| CAT | included | Default statutory tax increase lowers positive domestic pretax earnings after tax. |
| DE | included | Default statutory tax increase lowers positive domestic pretax earnings after tax. |
| GE | included | Default statutory tax increase lowers positive domestic pretax earnings after tax. |
| HON | included | Default statutory tax increase lowers positive domestic pretax earnings after tax. |
| MMM | included | Default statutory tax increase lowers positive domestic pretax earnings after tax. |
| NUE | included | Default statutory tax increase lowers positive domestic pretax earnings after tax. |
| BA | included | Default statutory tax increase lowers positive domestic pretax earnings after tax. |
| ETN | included | Default statutory tax increase lowers positive domestic pretax earnings after tax. |
| EMR | included | Default statutory tax increase lowers positive domestic pretax earnings after tax. |
| ITW | included | Default statutory tax increase lowers positive domestic pretax earnings after tax. |
| PH | included | Default statutory tax increase lowers positive domestic pretax earnings after tax. |
| CMI | included | Default statutory tax increase lowers positive domestic pretax earnings after tax. |
| PCAR | included | Default statutory tax increase lowers positive domestic pretax earnings after tax. |
| DOV | included | Default statutory tax increase lowers positive domestic pretax earnings after tax. |
| ROK | included | Default statutory tax increase lowers positive domestic pretax earnings after tax. |
| STLD | included | Default statutory tax increase lowers positive domestic pretax earnings after tax. |
| CLF | included | Default statutory tax increase lowers positive domestic pretax earnings after tax. |
| CARR | included | Default statutory tax increase lowers positive domestic pretax earnings after tax. |
| OTIS | included | Default statutory tax increase lowers positive domestic pretax earnings after tax. |
| IR | included | Default statutory tax increase lowers positive domestic pretax earnings after tax. |
| GEV | included | Reported US pretax-income share drives the statutory-rate channel. |

## B. Every in-scope exposure

Exact numeric checks are distinguished from filing links and estimates. UNVERIFIED values are retained, not silently replaced. Historical observed low/high values are not forecast confidence intervals.

| Company | Exposure | Base | Low | High | Exact-source status | Primary source / location / rationale |
|---|---|---:|---:|---:|---|---|
| CAT | ind_us_pretax_income_share | 0.47 | 0.4 | 0.5 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/18230/000001823026000008/cat-20251231.htm · Caterpillar 2025 10-K tax note: U.S. pretax income $5,407M of $11,541M (47%); 47% in 2024 and 50% in 2023;  · unavailable |
| DE | ind_us_pretax_income_share | 0.43 | 0.4 | 0.64 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/315189/000110465925122321/de-20251102x10k.htm · Deere FY2025 10-K tax note: U.S. pretax income $2.7B of $6.3B (43%); 64% in FY2024, 60% in FY2023, 55% in FY2022; FY2025 was a down year for US farm equipment, so the US share could recover toward its FY2022–24 level of 55–64%. · FY2025 was a down year for US farm equipment, so the US share could recover toward its FY2022–24 level of 55–64%. |
| GE | ind_us_pretax_income_share | 0.67 | 0.63 | 0.69 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/40545/000004054526000008/ge-20251231.htm · GE Aerospace 2025 10-K tax note: U.S. pretax income $6,659M of $10,000M (67%); 63% in 2024, 69% in 2023;  · unavailable |
| HON | ind_us_pretax_income_share | 0.2 | 0.07 | 0.27 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/773840/000077384026000013/hon-20251231.htm · Honeywell 2025 10-K tax note: U.S. pretax income $373M of $5,476M (7%) in 2025, $1,442M (23%) in 2024 and $1,652M (27%) in 2023; The 2025 US share looks depressed by one-off charges (the 2025 rate reconciliation shows $164M of impairment losses), so the base uses a share closer to 2023–24; the low end is the 2025 actual. · The 2025 US share looks depressed by one-off charges (the 2025 rate reconciliation shows $164M of impairment losses), so the base uses a share closer to 2023–24; the low end is the 2025 actual. |
| MMM | ind_us_pretax_income_share | 0.44 | 0.44 | 0.52 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/66740/000006674026000014/mmm-20251231.htm · 3M 2025 10-K tax note: United States pretax income $1,870M of $4,213M (44%); 48% in 2024, 52% in 2022 (2023 distorted by a $13.3B litigation charge);  · unavailable |
| NUE | ind_us_pretax_income_share | 0.98 | 0.98 | 0.99 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/73309/000119312526071575/nue-20251231.htm · Nucor 2025 10-K tax note: domestic pretax income $2,514M of $2,568M (98%); 99% in 2023 and 2024;  · unavailable |
| BA | ind_us_pretax_income_share | 0.44 | 0.07 | 0.69 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| ETN | ind_us_pretax_income_share | 0.44 | 0.07 | 0.69 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| EMR | ind_us_pretax_income_share | 0.44 | 0.07 | 0.69 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| ITW | ind_us_pretax_income_share | 0.44 | 0.07 | 0.69 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| PH | ind_us_pretax_income_share | 0.44 | 0.07 | 0.69 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| CMI | ind_us_pretax_income_share | 0.44 | 0.07 | 0.69 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| PCAR | ind_us_pretax_income_share | 0.44 | 0.07 | 0.69 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| DOV | ind_us_pretax_income_share | 0.44 | 0.07 | 0.69 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| ROK | ind_us_pretax_income_share | 0.44 | 0.07 | 0.69 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| STLD | ind_us_pretax_income_share | 0.98 | 0.98 | 0.99 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Steel production; median base and outer low/high from NUE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Steel production; median base and outer low/high from NUE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| CLF | ind_us_pretax_income_share | 0.98 | 0.98 | 0.99 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Steel production; median base and outer low/high from NUE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Steel production; median base and outer low/high from NUE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| CARR | ind_us_pretax_income_share | 0.44 | 0.07 | 0.69 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| OTIS | ind_us_pretax_income_share | 0.44 | 0.07 | 0.69 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| IR | ind_us_pretax_income_share | 0.44 | 0.07 | 0.69 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| GEV | ind_us_pretax_income_share | 0.02758133 | 0.02758133 | 0.51441153 | UNVERIFIED | https://data.sec.gov/api/xbrl/companyfacts/CIK0001996810.json · verified SEC companyfacts; US-incorporated issuer: reported domestic pretax / reported total pretax. Bounds are available three-year historical ratios, not confidence intervals. · US-incorporated issuer: reported domestic pretax / reported total pretax. Bounds are available three-year historical ratios, not confidence intervals. |

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
| exposure.ind_us_pretax_income_share | -0.011995259 | -0.028031014 | 0.016035754 |
| assumption.effective_share | -0.018343436 | -0.022929295 | 0.0045858589 |

Dominant configured driver: `ind_us_pretax_income_share` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.


## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 21 unchecked in-scope exposure values; 1 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

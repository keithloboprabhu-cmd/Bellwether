# Critical-minerals production credit

Policy `energy_resources/critical_minerals_credit` · evidence checkpoint 2026-11-01 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

A production tax credit worth a percentage of the cost of mining and processing critical minerals in the US, extended to copper (which today is not on the 45X list). Freeport's US copper mines are the only meaningful exposure in this group; XOM's and CVX's lithium projects are still pre-production.

Duration: `years:10`. Default inputs: `{"credit_pct": 10.0}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| tax_credit | unavailable / unavailable | {"credit_rate": "input.credit_pct / 100 * assumption.eligible_cost_share", "base_musd": "exposure.us_critical_mineral_production_cost_musd"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://www.sec.gov/Archives/edgar/data/831259/000083125926000012/fcx-20251231.htm

| Company | Configured status | Basis |
|---|---|---|
| XOM | outside_scope | The channel requires qualifying domestic mineral production costs; fuel production, utilities and imported solar materials do not automatically qualify. |
| CVX | outside_scope | The channel requires qualifying domestic mineral production costs; fuel production, utilities and imported solar materials do not automatically qualify. |
| COP | outside_scope | The channel requires qualifying domestic mineral production costs; fuel production, utilities and imported solar materials do not automatically qualify. |
| NEE | outside_scope | The channel requires qualifying domestic mineral production costs; fuel production, utilities and imported solar materials do not automatically qualify. |
| FSLR | outside_scope | The channel requires qualifying domestic mineral production costs; fuel production, utilities and imported solar materials do not automatically qualify. |
| FCX | included | Qualifying domestic mineral production gets an after-tax credit. |
| EOG | outside_scope | The channel requires qualifying domestic mineral production costs; fuel production, utilities and imported solar materials do not automatically qualify. |
| OXY | outside_scope | The channel requires qualifying domestic mineral production costs; fuel production, utilities and imported solar materials do not automatically qualify. |
| DVN | outside_scope | The channel requires qualifying domestic mineral production costs; fuel production, utilities and imported solar materials do not automatically qualify. |
| SLB | outside_scope | The channel requires qualifying domestic mineral production costs; fuel production, utilities and imported solar materials do not automatically qualify. |
| HAL | outside_scope | The channel requires qualifying domestic mineral production costs; fuel production, utilities and imported solar materials do not automatically qualify. |
| WMB | outside_scope | The channel requires qualifying domestic mineral production costs; fuel production, utilities and imported solar materials do not automatically qualify. |
| PSX | outside_scope | The channel requires qualifying domestic mineral production costs; fuel production, utilities and imported solar materials do not automatically qualify. |
| VLO | outside_scope | The channel requires qualifying domestic mineral production costs; fuel production, utilities and imported solar materials do not automatically qualify. |
| MPC | outside_scope | The channel requires qualifying domestic mineral production costs; fuel production, utilities and imported solar materials do not automatically qualify. |
| DUK | outside_scope | The channel requires qualifying domestic mineral production costs; fuel production, utilities and imported solar materials do not automatically qualify. |
| SO | outside_scope | The channel requires qualifying domestic mineral production costs; fuel production, utilities and imported solar materials do not automatically qualify. |
| AEP | outside_scope | The channel requires qualifying domestic mineral production costs; fuel production, utilities and imported solar materials do not automatically qualify. |
| EXC | outside_scope | The channel requires qualifying domestic mineral production costs; fuel production, utilities and imported solar materials do not automatically qualify. |
| CEG | outside_scope | The channel requires qualifying domestic mineral production costs; fuel production, utilities and imported solar materials do not automatically qualify. |

## B. Every in-scope exposure

Exact numeric checks are distinguished from filing links and estimates. UNVERIFIED values are retained, not silently replaced. Historical observed low/high values are not forecast confidence intervals.

| Company | Exposure | Base | Low | High | Exact-source status | Primary source / location / rationale |
|---|---|---:|---:|---:|---|---|
| FCX | us_critical_mineral_production_cost_musd | 4,549 | 4,000 | 5,000 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/831259/000083125926000012/fcx-20251231.htm · FCX 2025 10-K: U.S. copper mines sold 1,296M lbs (net of JV interests) at site production & delivery cost $3.51/lb (by-product method); 1,296 × $3.51 ≈ $4,549M; range for cost inflation/volume swings. · 1,296 × $3.51 ≈ $4,549M; range for cost inflation/volume swings. |

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
| assumption.eligible_cost_share | 0.00092938805 | 0.0023234701 | 0.0013940821 |
| exposure.us_critical_mineral_production_cost_musd | 0.0014301421 | 0.0017876776 | 0.00035753552 |

Dominant configured driver: `eligible_cost_share` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.


## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 1 unchecked in-scope exposure values; 1 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

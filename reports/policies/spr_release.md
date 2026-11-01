# Strategic Petroleum Reserve release

Policy `energy_resources/spr_release` · reviewed 2026-10-31 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

An emergency SPR sale temporarily lowers crude prices. Upstream producers lose revenue; Freeport benefits through its explicitly signed diesel-cost proxy. Stand-alone refiners have no direct modeled earnings change when refining margins are held constant. Oilfield-service order/capex responses need a separate lagged demand model.

Duration: `one_time`. Default inputs: `{"barrels_mb": 60.0}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| price | unavailable / ['domestic_producer'] | {"d_price": "derived.d_oil_pct", "exposed_revenue_share": "max(0, exposure.oil_price_sensitivity)"} |
| cost | unavailable / ['domestic_producer'] | {"exposed_cost_share": 0.0, "shock_pct": 0.0, "dcost_musd": "baseline.revenue * max(0, -exposure.oil_price_sensitivity) * derived.d_oil_pct"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://home.treasury.gov/news/featured-stories/the-price-impact-of-the-strategic-petroleum-reserve-release
- https://econpapers.repec.org/paper/zbwcfswop/647.htm
- https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/xom-20251231.htm

| Company | Configured status | Basis |
|---|---|---|
| XOM | included | Default reserve release depresses crude price for producers. |
| CVX | included | Default reserve release depresses crude price for producers. |
| COP | included | Default reserve release depresses crude price for producers. |
| NEE | outside_scope | This temporary-price scenario holds refining margins constant. Oilfield-service orders, utility dispatch and other lagged/indirect effects are not quantified. |
| FSLR | outside_scope | This temporary-price scenario holds refining margins constant. Oilfield-service orders, utility dispatch and other lagged/indirect effects are not quantified. |
| FCX | included | Default reserve release depresses crude price for producers. |
| EOG | included | Default reserve release depresses crude price for producers. |
| OXY | included | Default reserve release depresses crude price for producers. |
| DVN | included | Default reserve release depresses crude price for producers. |
| SLB | outside_scope | This temporary-price scenario holds refining margins constant. Oilfield-service orders, utility dispatch and other lagged/indirect effects are not quantified. |
| HAL | outside_scope | This temporary-price scenario holds refining margins constant. Oilfield-service orders, utility dispatch and other lagged/indirect effects are not quantified. |
| WMB | outside_scope | This temporary-price scenario holds refining margins constant. Oilfield-service orders, utility dispatch and other lagged/indirect effects are not quantified. |
| PSX | outside_scope | This temporary-price scenario holds refining margins constant. Oilfield-service orders, utility dispatch and other lagged/indirect effects are not quantified. |
| VLO | outside_scope | This temporary-price scenario holds refining margins constant. Oilfield-service orders, utility dispatch and other lagged/indirect effects are not quantified. |
| MPC | outside_scope | This temporary-price scenario holds refining margins constant. Oilfield-service orders, utility dispatch and other lagged/indirect effects are not quantified. |
| DUK | outside_scope | This temporary-price scenario holds refining margins constant. Oilfield-service orders, utility dispatch and other lagged/indirect effects are not quantified. |
| SO | outside_scope | This temporary-price scenario holds refining margins constant. Oilfield-service orders, utility dispatch and other lagged/indirect effects are not quantified. |
| AEP | outside_scope | This temporary-price scenario holds refining margins constant. Oilfield-service orders, utility dispatch and other lagged/indirect effects are not quantified. |
| EXC | outside_scope | This temporary-price scenario holds refining margins constant. Oilfield-service orders, utility dispatch and other lagged/indirect effects are not quantified. |
| CEG | outside_scope | This temporary-price scenario holds refining margins constant. Oilfield-service orders, utility dispatch and other lagged/indirect effects are not quantified. |

## B. Every in-scope exposure

Exact numeric checks are distinguished from filing links and estimates. UNVERIFIED values are retained, not silently replaced. Historical observed low/high values are not forecast confidence intervals.

| Company | Exposure | Base | Low | High | Exact-source status | Primary source / location / rationale |
|---|---|---:|---:|---:|---|---|
| XOM | oil_price_sensitivity | 0.2017 | 0.1729 | 0.2306 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/xom-20251231.htm · XOM 2025 10-K: for 2026, a $1/bbl change in Brent ≈ $700M annual after-tax Upstream earnings (excl. derivatives); 700 × $69.06 ÷ ((1 − 27.9% model tax rate) × $332.2B revenue); range uses $600–800M. · 700 × $69.06 ÷ ((1 − 27.9% model tax rate) × $332.2B revenue); range uses $600–800M. |
| CVX | oil_price_sensitivity | 0.3177 | 0.26 | 0.3755 | UNVERIFIED | No source URL · estimate; From ni_per_usd_bbl_musd (550) × $69.06 ÷ ((1 − 36.8% model tax rate) × $189.0B revenue); range uses $450–650M. · From ni_per_usd_bbl_musd (550) × $69.06 ÷ ((1 − 36.8% model tax rate) × $189.0B revenue); range uses $450–650M. |
| COP | oil_price_sensitivity | 0.6126 | 0.4641 | 0.7796 | UNVERIFIED | No source URL · estimate; From ni_per_usd_bbl_musd (330) × $69.06 ÷ ((1 − 36.9% model tax rate) × $58.9B revenue); range uses $250–420M. · From ni_per_usd_bbl_musd (330) × $69.06 ÷ ((1 − 36.9% model tax rate) × $58.9B revenue); range uses $250–420M. |
| FCX | oil_price_sensitivity | -0.0175 | -0.0293 | -0.008 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/831259/000083125926000012/fcx-20251231.htm · FCX 2025 10-K: energy was 15% of copper mine site operating costs in 2025, including ~275 million gallons of diesel; Diesel moves ~$1/42 per gallon per $1/bbl crude → 275M gal ≈ $6.5M pretax cost per $1/bbl; × $69.06 ÷ $25.9B revenue. Negative = oil consumer. Range $3–11M/bbl (other energy partly oil-linked; some diesel hedged/indexed). · Diesel moves ~$1/42 per gallon per $1/bbl crude → 275M gal ≈ $6.5M pretax cost per $1/bbl; × $69.06 ÷ $25.9B revenue. Negative = oil consumer. Range $3–11M/bbl (other energy partly oil-linked; some diesel hedged/indexed). |
| EOG | oil_price_sensitivity | 0.3177 | 0.1729 | 0.7796 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Oil production and services; median base and outer low/high from XOM/CVX/COP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Oil production and services; median base and outer low/high from XOM/CVX/COP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| OXY | oil_price_sensitivity | 0.3177 | 0.1729 | 0.7796 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Oil production and services; median base and outer low/high from XOM/CVX/COP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Oil production and services; median base and outer low/high from XOM/CVX/COP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| DVN | oil_price_sensitivity | 0.3177 | 0.1729 | 0.7796 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Oil production and services; median base and outer low/high from XOM/CVX/COP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Oil production and services; median base and outer low/high from XOM/CVX/COP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |

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
| assumption.duration_years | -0.01266236 | -0.050649438 | 0.037987079 |
| assumption.impact_per_100mb | -0.010129888 | -0.037987079 | 0.027857191 |
| exposure.oil_price_sensitivity | -0.019968937 | -0.033808544 | 0.013839607 |

Dominant configured driver: `duration_years` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.


## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 7 unchecked in-scope exposure values; 2 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

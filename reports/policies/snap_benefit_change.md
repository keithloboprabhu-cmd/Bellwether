# SNAP benefit cut or expansion

Policy `consumer_retail/snap_benefit_change` · evidence checkpoint 2026-11-01 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

A change in federal SNAP (food stamp) benefits shifts what low-income households spend on groceries; grocers that take the most SNAP dollars, above all Walmart, gain or lose the most.

Duration: `permanent`. Default inputs: `{"d_benefits_bn": -15.0}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| demand_transfer | unavailable / unavailable | {"total_transfer_musd": "input.d_benefits_bn * 1000", "mpc": "assumption.spend_response", "capture_share": "exposure.snap_grocery_spend_share"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://www.nber.org/papers/w23112
- https://supermarketnews.com/foodservice-retail/walmart-dominates-the-retail-field-in-snap-grocery-market-share
- https://www.everycrsreport.com/files/2025-07-23_R48552_542fa893b97030757b3aedac1b44930cac47cc88.html

| Company | Configured status | Basis |
|---|---|---|
| WMT | included | Default SNAP reduction lowers grocery spending. |
| TGT | included | Default SNAP reduction lowers grocery spending. |
| COST | included | Default SNAP reduction lowers grocery spending. |
| AMZN | included | Default SNAP reduction lowers grocery spending. |
| NKE | outside_scope | This model allocates SNAP redemptions to eligible grocery retailers. Manufacturer supply-chain effects and restaurant exceptions are not included. |
| HD | outside_scope | This model allocates SNAP redemptions to eligible grocery retailers. Manufacturer supply-chain effects and restaurant exceptions are not included. |
| LOW | outside_scope | This model allocates SNAP redemptions to eligible grocery retailers. Manufacturer supply-chain effects and restaurant exceptions are not included. |
| KR | included | Default SNAP reduction lowers grocery spending. |
| DG | included | Default SNAP reduction lowers grocery spending. |
| DLTR | included | Default SNAP reduction lowers grocery spending. |
| TJX | outside_scope | This model allocates SNAP redemptions to eligible grocery retailers. Manufacturer supply-chain effects and restaurant exceptions are not included. |
| ROST | outside_scope | This model allocates SNAP redemptions to eligible grocery retailers. Manufacturer supply-chain effects and restaurant exceptions are not included. |
| SBUX | outside_scope | This model allocates SNAP redemptions to eligible grocery retailers. Manufacturer supply-chain effects and restaurant exceptions are not included. |
| MCD | outside_scope | This model allocates SNAP redemptions to eligible grocery retailers. Manufacturer supply-chain effects and restaurant exceptions are not included. |
| KO | outside_scope | This model allocates SNAP redemptions to eligible grocery retailers. Manufacturer supply-chain effects and restaurant exceptions are not included. |
| PEP | outside_scope | This model allocates SNAP redemptions to eligible grocery retailers. Manufacturer supply-chain effects and restaurant exceptions are not included. |
| PG | outside_scope | This model allocates SNAP redemptions to eligible grocery retailers. Manufacturer supply-chain effects and restaurant exceptions are not included. |
| CL | outside_scope | This model allocates SNAP redemptions to eligible grocery retailers. Manufacturer supply-chain effects and restaurant exceptions are not included. |
| ULTA | outside_scope | This model allocates SNAP redemptions to eligible grocery retailers. Manufacturer supply-chain effects and restaurant exceptions are not included. |
| BBY | outside_scope | This model allocates SNAP redemptions to eligible grocery retailers. Manufacturer supply-chain effects and restaurant exceptions are not included. |
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
| WMT | snap_grocery_spend_share | 0.255 | 0.22 | 0.28 | UNVERIFIED | https://supermarketnews.com/foodservice-retail/walmart-dominates-the-retail-field-in-snap-grocery-market-share · Numerator SNAP Shopper Scorecard (year to Q1 2023), via Supermarket News: Walmart 25.5% of SNAP shoppers' annual grocery spend; Share of SNAP households' total grocery spend, used as a proxy for share of SNAP dollars; range allows for drift since 2023. · Share of SNAP households' total grocery spend, used as a proxy for share of SNAP dollars; range allows for drift since 2023. |
| TGT | snap_grocery_spend_share | 0.018 | 0.012 | 0.025 | UNVERIFIED | https://supermarketnews.com/foodservice-retail/walmart-dominates-the-retail-field-in-snap-grocery-market-share · Numerator SNAP Shopper Scorecard (year to Q1 2023), via Supermarket News: Target 1.8% of SNAP shoppers' annual grocery spend;  · unavailable |
| COST | snap_grocery_spend_share | 0.06 | 0.03 | 0.06 | UNVERIFIED | https://supermarketnews.com/foodservice-retail/walmart-dominates-the-retail-field-in-snap-grocery-market-share · Numerator SNAP Shopper Scorecard (year to Q1 2023), via Supermarket News: Costco 6% of SNAP shoppers' annual grocery spend; Low end assumes SNAP households pay at Costco disproportionately with non-SNAP funds (bulk, membership-gated shopping). · Low end assumes SNAP households pay at Costco disproportionately with non-SNAP funds (bulk, membership-gated shopping). |
| AMZN | snap_grocery_spend_share | 0.013 | 0.008 | 0.02 | UNVERIFIED | https://supermarketnews.com/foodservice-retail/walmart-dominates-the-retail-field-in-snap-grocery-market-share · Numerator SNAP Shopper Scorecard (year to Q1 2023), via Supermarket News: Amazon 1.3% of SNAP shoppers' annual grocery spend;  · unavailable |
| KR | snap_grocery_spend_share | 0.06 | 0.012 | 0.28 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Groceries and discount retail; median base and outer low/high from WMT/COST/TGT in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Groceries and discount retail; median base and outer low/high from WMT/COST/TGT in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| DG | snap_grocery_spend_share | 0.06 | 0.012 | 0.28 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Groceries and discount retail; median base and outer low/high from WMT/COST/TGT in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Groceries and discount retail; median base and outer low/high from WMT/COST/TGT in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| DLTR | snap_grocery_spend_share | 0.06 | 0.012 | 0.28 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Groceries and discount retail; median base and outer low/high from WMT/COST/TGT in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Groceries and discount retail; median base and outer low/high from WMT/COST/TGT in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |

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
| exposure.snap_grocery_spend_share | -0.002729664 | -0.012674629 | 0.0099449649 |
| assumption.spend_response | -0.0035187037 | -0.0063336667 | 0.002814963 |

Dominant configured driver: `snap_grocery_spend_share` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.


## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 7 unchecked in-scope exposure values; 1 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

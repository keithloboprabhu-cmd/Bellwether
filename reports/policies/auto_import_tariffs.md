# Tariffs on imported vehicles and auto parts

Policy `transportation_logistics/auto_import_tariffs` · evidence checkpoint 2026-11-01 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

Tariffs on imported vehicles and parts, with USMCA-content relief. GM, which builds many US-sold vehicles in Mexico and Korea, carries most of it. Tesla's exposure is through parts. The parcel, rail and airline companies see it only in fleet costs.

Duration: `permanent`. Default inputs: `{"tariff_pct": 25.0}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| cost | unavailable / unavailable | {"exposed_cost_share": 0.0, "shock_pct": 0.0, "dcost_musd": "exposure.tl_auto_tariff_cost_at_25pct_musd * input.tariff_pct / 25", "pass_through": "assumption.pass_through", "elasticity": "assumption.elasticity"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://www.sec.gov/Archives/edgar/data/1467858/000146785826000013/gm-20251231.htm
- https://www.sec.gov/Archives/edgar/data/1318605/000162828026003952/tsla-20251231.htm

| Company | Configured status | Basis |
|---|---|---|
| UPS | included | Imported vehicles/parts and owned-fleet procurement face tariff costs. |
| FDX | included | Imported vehicles/parts and owned-fleet procurement face tariff costs. |
| UNP | included | Imported vehicles/parts and owned-fleet procurement face tariff costs. |
| DAL | included | Imported vehicles/parts and owned-fleet procurement face tariff costs. |
| TSLA | included | Imported vehicles/parts and owned-fleet procurement face tariff costs. |
| GM | included | Imported vehicles/parts and owned-fleet procurement face tariff costs. |
| F | included | Imported vehicles/parts and owned-fleet procurement face tariff costs. |
| RIVN | included | Imported vehicles/parts and owned-fleet procurement face tariff costs. |
| CHRW | outside_scope | Direct vehicle/parts and owned-fleet procurement costs are modeled. Independent drivers and brokered carrier fleets are not the platforms' or broker's import bill. |
| JBHT | included | Imported vehicles/parts and owned-fleet procurement face tariff costs. |
| ODFL | included | Imported vehicles/parts and owned-fleet procurement face tariff costs. |
| XPO | included | Imported vehicles/parts and owned-fleet procurement face tariff costs. |
| SAIA | included | Imported vehicles/parts and owned-fleet procurement face tariff costs. |
| CSX | included | Imported vehicles/parts and owned-fleet procurement face tariff costs. |
| NSC | included | Imported vehicles/parts and owned-fleet procurement face tariff costs. |
| UAL | included | Imported vehicles/parts and owned-fleet procurement face tariff costs. |
| AAL | included | Imported vehicles/parts and owned-fleet procurement face tariff costs. |
| LUV | included | Imported vehicles/parts and owned-fleet procurement face tariff costs. |
| UBER | outside_scope | Direct vehicle/parts and owned-fleet procurement costs are modeled. Independent drivers and brokered carrier fleets are not the platforms' or broker's import bill. |
| LYFT | outside_scope | Direct vehicle/parts and owned-fleet procurement costs are modeled. Independent drivers and brokered carrier fleets are not the platforms' or broker's import bill. |

## B. Every in-scope exposure

Exact numeric checks are distinguished from filing links and estimates. UNVERIFIED values are retained, not silently replaced. Historical observed low/high values are not forecast confidence intervals.

| Company | Exposure | Base | Low | High | Exact-source status | Primary source / location / rationale |
|---|---|---:|---:|---:|---|---|
| UPS | tl_auto_tariff_cost_at_25pct_musd | 80 | 20 | 200 | UNVERIFIED | No source URL · estimate; UPS buys delivery vans and tractors, mostly assembled in the US; a 25% tariff on imported parts and trucks raises fleet capex modestly and reaches earnings slowly through depreciation. · UPS buys delivery vans and tractors, mostly assembled in the US; a 25% tariff on imported parts and trucks raises fleet capex modestly and reaches earnings slowly through depreciation. |
| FDX | tl_auto_tariff_cost_at_25pct_musd | 80 | 20 | 200 | UNVERIFIED | No source URL · estimate; Same logic as UPS. FedEx's pickup-and-delivery vans and tractors are mostly US-assembled, and its aircraft are covered by civil-aircraft tariff exemptions. · Same logic as UPS. FedEx's pickup-and-delivery vans and tractors are mostly US-assembled, and its aircraft are covered by civil-aircraft tariff exemptions. |
| UNP | tl_auto_tariff_cost_at_25pct_musd | 20 | 0 | 60 | UNVERIFIED | No source URL · estimate; Locomotives and railcars are largely US-built; small exposure through imported parts. The larger effect, lost cross-border auto traffic, is not modelled here. · Locomotives and railcars are largely US-built; small exposure through imported parts. The larger effect, lost cross-border auto traffic, is not modelled here. |
| DAL | tl_auto_tariff_cost_at_25pct_musd | 10 | 0 | 50 | UNVERIFIED | No source URL · estimate; Civil aircraft and parts are largely exempt from the auto tariffs; only ground-support vehicles are exposed. · Civil aircraft and parts are largely exempt from the auto tariffs; only ground-support vehicles are exposed. |
| TSLA | tl_auto_tariff_cost_at_25pct_musd | 600 | 300 | 1,200 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1318605/000162828026003952/tsla-20251231.htm · estimate; The Tesla 10-K says tariffs affected product pricing but does not quantify them. US-sold Teslas are assembled in California and Texas, so exposure comes from imported parts only, well below GM's. · The Tesla 10-K says tariffs affected product pricing but does not quantify them. US-sold Teslas are assembled in California and Texas, so exposure comes from imported parts only, well below GM's. |
| GM | tl_auto_tariff_cost_at_25pct_musd | 3,500 | 3,000 | 4,000 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1467858/000146785826000013/gm-20251231.htm · GM 2025 10-K: tariff impact on EBIT-adjusted $3.1B in 2025; 2026 estimate $3.0B-$4.0B under the current tariff regime;  · unavailable |
| F | tl_auto_tariff_cost_at_25pct_musd | 2,363.711 | 592.44835 | 4,048.6004 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Automotive; median base and outer low/high from TSLA/GM in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Automotive; median base and outer low/high from TSLA/GM in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| RIVN | tl_auto_tariff_cost_at_25pct_musd | 67.99549 | 17.042614 | 116.46371 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Automotive; median base and outer low/high from TSLA/GM in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Automotive; median base and outer low/high from TSLA/GM in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| JBHT | tl_auto_tariff_cost_at_25pct_musd | 10.480658 | 2.5335929 | 27.06736 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Freight and logistics; median base and outer low/high from UPS/FDX in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Freight and logistics; median base and outer low/high from UPS/FDX in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| ODFL | tl_auto_tariff_cost_at_25pct_musd | 4.8008427 | 1.1605551 | 12.398662 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Freight and logistics; median base and outer low/high from UPS/FDX in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Freight and logistics; median base and outer low/high from UPS/FDX in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| XPO | tl_auto_tariff_cost_at_25pct_musd | 7.1247639 | 1.7223395 | 18.400424 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Freight and logistics; median base and outer low/high from UPS/FDX in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Freight and logistics; median base and outer low/high from UPS/FDX in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| SAIA | tl_auto_tariff_cost_at_25pct_musd | 2.8249999 | 0.68291512 | 7.2958482 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Freight and logistics; median base and outer low/high from UPS/FDX in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Freight and logistics; median base and outer low/high from UPS/FDX in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| CSX | tl_auto_tariff_cost_at_25pct_musd | 11.49898 | 0 | 34.49694 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Rail; median base and outer low/high from UNP in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Rail; median base and outer low/high from UNP in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| NSC | tl_auto_tariff_cost_at_25pct_musd | 9.9388005 | 0 | 29.816401 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Rail; median base and outer low/high from UNP in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Rail; median base and outer low/high from UNP in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| UAL | tl_auto_tariff_cost_at_25pct_musd | 9.3223281 | 0 | 46.611641 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Passenger aviation; median base and outer low/high from DAL in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Passenger aviation; median base and outer low/high from DAL in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| AAL | tl_auto_tariff_cost_at_25pct_musd | 8.6220883 | 0 | 43.110441 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Passenger aviation; median base and outer low/high from DAL in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Passenger aviation; median base and outer low/high from DAL in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| LUV | tl_auto_tariff_cost_at_25pct_musd | 4.4288555 | 0 | 22.144278 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Passenger aviation; median base and outer low/high from DAL in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Passenger aviation; median base and outer low/high from DAL in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |

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
| exposure.tl_auto_tariff_cost_at_25pct_musd | -0.064568302 | -0.15565932 | 0.091091019 |
| assumption.pass_through | -0.13501957 | -0.064554029 | 0.070465543 |
| assumption.elasticity | -0.1024081 | -0.11096171 | 0.0085536092 |

Dominant configured driver: `tl_auto_tariff_cost_at_25pct_musd` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.

- REVIEW GM: EPS -63.5%; Reported EPS denominator 3.27; dominant NI channel: Tariff on imported vehicles and parts; estimated exposures: none labeled estimate. Review reported earnings, exposure denominator and linear transmission before use. Default scenario; realistic range not independently verified.

## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 17 unchecked in-scope exposure values; 2 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

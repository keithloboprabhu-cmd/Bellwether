# Carbon price on transport fuel

Policy `transportation_logistics/carbon_tax_transport_fuel` · reviewed 2026-10-31 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

A per-tonne CO2 charge on jet fuel, diesel and other fossil fuels burned in the US. Delta carries the largest bill and recovers the least of it; UPS, FedEx and Union Pacific pass most of theirs through fuel surcharges. Tesla's and GM's direct fuel use is small.

Duration: `permanent`. Default inputs: `{"price_per_ton": 50.0}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| cost | unavailable / unavailable | {"exposed_cost_share": 0.0, "shock_pct": 0.0, "dcost_musd": "derived.carbon_cost_musd", "pass_through": "exposure.tl_fuel_cost_recovery_share", "elasticity": "assumption.elasticity", "variable_cost_share": "assumption.variable_cost_share"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://www.eia.gov/environment/emissions/co2_vol_mass.php
- https://www.sec.gov/Archives/edgar/data/27904/000002790426000013/dal-20251231.htm
- https://www.sec.gov/Archives/edgar/data/100885/000010088526000037/unp-20251231.htm

| Company | Configured status | Basis |
|---|---|---|
| UPS | included | Owned-fleet fuel carbon cost is partially recovered through pricing. |
| FDX | included | Owned-fleet fuel carbon cost is partially recovered through pricing. |
| UNP | included | Owned-fleet fuel carbon cost is partially recovered through pricing. |
| DAL | included | Owned-fleet fuel carbon cost is partially recovered through pricing. |
| TSLA | included | Owned-fleet fuel carbon cost is partially recovered through pricing. |
| GM | included | Owned-fleet fuel carbon cost is partially recovered through pricing. |
| F | included | Owned-fleet fuel carbon cost is partially recovered through pricing. |
| RIVN | included | Owned-fleet fuel carbon cost is partially recovered through pricing. |
| CHRW | outside_scope | The direct operating-fuel channel excludes independent-driver and brokered-carrier Scope 3 fuel. Fare, demand and supplier feedback require separate channels. |
| JBHT | included | Owned-fleet fuel carbon cost is partially recovered through pricing. |
| ODFL | included | Owned-fleet fuel carbon cost is partially recovered through pricing. |
| XPO | included | Owned-fleet fuel carbon cost is partially recovered through pricing. |
| SAIA | included | Owned-fleet fuel carbon cost is partially recovered through pricing. |
| CSX | included | Owned-fleet fuel carbon cost is partially recovered through pricing. |
| NSC | included | Owned-fleet fuel carbon cost is partially recovered through pricing. |
| UAL | included | Owned-fleet fuel carbon cost is partially recovered through pricing. |
| AAL | included | Owned-fleet fuel carbon cost is partially recovered through pricing. |
| LUV | included | Owned-fleet fuel carbon cost is partially recovered through pricing. |
| UBER | outside_scope | The direct operating-fuel channel excludes independent-driver and brokered-carrier Scope 3 fuel. Fare, demand and supplier feedback require separate channels. |
| LYFT | outside_scope | The direct operating-fuel channel excludes independent-driver and brokered-carrier Scope 3 fuel. Fare, demand and supplier feedback require separate channels. |

## B. Every in-scope exposure

Exact numeric checks are distinguished from filing links and estimates. UNVERIFIED values are retained, not silently replaced. Historical observed low/high values are not forecast confidence intervals.

| Company | Exposure | Base | Low | High | Exact-source status | Primary source / location / rationale |
|---|---|---:|---:|---:|---|---|
| UPS | tl_fuel_co2_mt | 13 | 10 | 16 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1090727/000162828026008432/ups-20251231.htm · estimate; UPS 2025 10-K: fuel expense $4,316M (jet, diesel, gasoline) but no gallons disclosed. At a blended ~$2.6/gal that is ~1.65B gal x ~9.8 kg = ~16 Mt; base removes ~20% for fuel bought outside the US. · UPS 2025 10-K: fuel expense $4,316M (jet, diesel, gasoline) but no gallons disclosed. At a blended ~$2.6/gal that is ~1.65B gal x ~9.8 kg = ~16 Mt; base removes ~20% for fuel bought outside the US. |
| UPS | tl_fuel_cost_recovery_share | 0.85 | 0.7 | 0.95 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1090727/000162828026008432/ups-20251231.htm · estimate; UPS 10-K says its air and ground fuel surcharges are indexed to fuel prices (international air to the DOE Gulf Coast jet fuel spot price) and reset frequently, so most of a fuel-cost rise is recovered with a short lag. · UPS 10-K says its air and ground fuel surcharges are indexed to fuel prices (international air to the DOE Gulf Coast jet fuel spot price) and reset frequently, so most of a fuel-cost rise is recovered with a short lag. |
| FDX | tl_fuel_co2_mt | 12 | 9.5 | 15.8 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1048911/000104891126000105/fdx-20260531.htm · estimate; FedEx FY2026 10-K: fuel $4,052M, of which jet fuel $3,050M. ~$3,050M / ~$2.3 = ~1.33B gal x 9.75 kg = ~12.9 Mt; vehicle fuel ~$1,000M / ~$3.3 = ~0.3B gal = ~2.9 Mt. High is the ~15.8 Mt total; base removes ~25% for fuel bought abroad. · FedEx FY2026 10-K: fuel $4,052M, of which jet fuel $3,050M. ~$3,050M / ~$2.3 = ~1.33B gal x 9.75 kg = ~12.9 Mt; vehicle fuel ~$1,000M / ~$3.3 = ~0.3B gal = ~2.9 Mt. High is the ~15.8 Mt total; base removes ~25% for fuel bought abroad. |
| FDX | tl_fuel_cost_recovery_share | 0.85 | 0.7 | 0.95 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1048911/000104891126000105/fdx-20260531.htm · estimate; FedEx 10-K says Express fuel surcharges are indexed to a weekly fuel price with about a two-week lag and that higher fuel prices raised yields through surcharges in FY2026. · FedEx 10-K says Express fuel surcharges are indexed to a weekly fuel price with about a two-week lag and that higher fuel prices raised yields through surcharges in FY2026. |
| UNP | tl_fuel_co2_mt | 9.8 | 9.3 | 10.3 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/100885/000010088526000037/unp-20251231.htm · Union Pacific 2025 10-K: fuel expense $2,390M at an average $2.49/gal = ~960M gal; x EIA 10.19 kg CO2/gal diesel = 9.8 Mt;  · unavailable |
| UNP | tl_fuel_cost_recovery_share | 0.85 | 0.7 | 0.95 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/100885/000010088526000037/unp-20251231.htm · estimate; UNP 10-K says fuel surcharge programs recover a significant amount of fuel expense with about a two-month lag; 2025 fuel surcharge revenue was ~$2.3B against $2,390M of fuel expense. · UNP 10-K says fuel surcharge programs recover a significant amount of fuel expense with about a two-month lag; 2025 fuel surcharge revenue was ~$2.3B against $2,390M of fuel expense. |
| DAL | tl_fuel_co2_mt | 32.5 | 25 | 41.6 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/27904/000002790426000013/dal-20251231.htm · estimate; Delta 2025 10-K: 4,269M gallons of jet fuel (incl. regional carriers) x EIA 9.75 kg = 41.6 Mt (high). Domestic is 56% of passenger revenue; assuming about half of international fuel is uplifted abroad leaves ~78% bought in the US (base). · Delta 2025 10-K: 4,269M gallons of jet fuel (incl. regional carriers) x EIA 9.75 kg = 41.6 Mt (high). Domestic is 56% of passenger revenue; assuming about half of international fuel is uplifted abroad leaves ~78% bought in the US (base). |
| DAL | tl_fuel_cost_recovery_share | 0.5 | 0.3 | 0.7 | UNVERIFIED | No source URL · estimate; US airlines have no fuel surcharge on domestic fares and recover fuel shocks only partly and with a lag, by cutting capacity and raising fares. · US airlines have no fuel surcharge on domestic fares and recover fuel shocks only partly and with a lag, by cutting capacity and raising fares. |
| TSLA | tl_fuel_co2_mt | 0.3 | 0.1 | 0.6 | UNVERIFIED | No source URL · estimate; Tesla burns little fuel (factory natural gas, logistics); its 10-K gives no figure. The EV-demand gain a carbon price on gasoline would bring is not modelled. · Tesla burns little fuel (factory natural gas, logistics); its 10-K gives no figure. The EV-demand gain a carbon price on gasoline would bring is not modelled. |
| TSLA | tl_fuel_cost_recovery_share | 0.2 | 0 | 0.4 | UNVERIFIED | No source URL · estimate; Automakers cannot pass a small factory-energy cost directly into vehicle prices. · Automakers cannot pass a small factory-energy cost directly into vehicle prices. |
| GM | tl_fuel_co2_mt | 1.5 | 1 | 2.5 | UNVERIFIED | No source URL · estimate; GM's direct emissions come mainly from natural gas at its North American plants; the 10-K gives no figure. Tailpipe emissions of vehicles sold are excluded. · GM's direct emissions come mainly from natural gas at its North American plants; the 10-K gives no figure. Tailpipe emissions of vehicles sold are excluded. |
| GM | tl_fuel_cost_recovery_share | 0.2 | 0 | 0.4 | UNVERIFIED | No source URL · estimate; Automakers cannot pass a small factory-energy cost directly into vehicle prices. · Automakers cannot pass a small factory-energy cost directly into vehicle prices. |
| F | tl_fuel_co2_mt | 1.0553368 | 0.19748278 | 2.5303753 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Automotive; median base and outer low/high from TSLA/GM in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Automotive; median base and outer low/high from TSLA/GM in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| F | tl_fuel_cost_recovery_share | 0.2 | 0 | 0.4 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Automotive; median base and outer low/high from TSLA/GM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Automotive; median base and outer low/high from TSLA/GM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| RIVN | tl_fuel_co2_mt | 0.030358254 | 0.0056808715 | 0.072789822 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Automotive; median base and outer low/high from TSLA/GM in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Automotive; median base and outer low/high from TSLA/GM in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| RIVN | tl_fuel_cost_recovery_share | 0.2 | 0 | 0.4 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Automotive; median base and outer low/high from TSLA/GM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Automotive; median base and outer low/high from TSLA/GM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| JBHT | tl_fuel_co2_mt | 1.6397671 | 1.2034566 | 2.1653888 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Freight and logistics; median base and outer low/high from UPS/FDX in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Freight and logistics; median base and outer low/high from UPS/FDX in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| JBHT | tl_fuel_cost_recovery_share | 0.85 | 0.7 | 0.95 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Freight and logistics; median base and outer low/high from UPS/FDX in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Freight and logistics; median base and outer low/high from UPS/FDX in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| ODFL | tl_fuel_co2_mt | 0.75112306 | 0.55126368 | 0.99189299 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Freight and logistics; median base and outer low/high from UPS/FDX in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Freight and logistics; median base and outer low/high from UPS/FDX in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| ODFL | tl_fuel_cost_recovery_share | 0.85 | 0.7 | 0.95 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Freight and logistics; median base and outer low/high from UPS/FDX in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Freight and logistics; median base and outer low/high from UPS/FDX in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| XPO | tl_fuel_co2_mt | 1.1147156 | 0.81811128 | 1.4720339 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Freight and logistics; median base and outer low/high from UPS/FDX in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Freight and logistics; median base and outer low/high from UPS/FDX in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| XPO | tl_fuel_cost_recovery_share | 0.85 | 0.7 | 0.95 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Freight and logistics; median base and outer low/high from UPS/FDX in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Freight and logistics; median base and outer low/high from UPS/FDX in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| SAIA | tl_fuel_co2_mt | 0.4419896 | 0.32438468 | 0.58366786 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Freight and logistics; median base and outer low/high from UPS/FDX in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Freight and logistics; median base and outer low/high from UPS/FDX in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| SAIA | tl_fuel_cost_recovery_share | 0.85 | 0.7 | 0.95 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Freight and logistics; median base and outer low/high from UPS/FDX in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Freight and logistics; median base and outer low/high from UPS/FDX in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| CSX | tl_fuel_co2_mt | 5.6345002 | 5.3470257 | 5.9219747 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Rail; median base and outer low/high from UNP in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Rail; median base and outer low/high from UNP in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| CSX | tl_fuel_cost_recovery_share | 0.85 | 0.7 | 0.95 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Rail; median base and outer low/high from UNP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Rail; median base and outer low/high from UNP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| NSC | tl_fuel_co2_mt | 4.8700122 | 4.6215422 | 5.1184823 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Rail; median base and outer low/high from UNP in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Rail; median base and outer low/high from UNP in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| NSC | tl_fuel_cost_recovery_share | 0.85 | 0.7 | 0.95 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Rail; median base and outer low/high from UNP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Rail; median base and outer low/high from UNP in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| UAL | tl_fuel_co2_mt | 30.297566 | 23.30582 | 38.780885 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Passenger aviation; median base and outer low/high from DAL in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Passenger aviation; median base and outer low/high from DAL in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| UAL | tl_fuel_cost_recovery_share | 0.5 | 0.3 | 0.7 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Passenger aviation; median base and outer low/high from DAL in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Passenger aviation; median base and outer low/high from DAL in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| AAL | tl_fuel_co2_mt | 28.021787 | 21.555221 | 35.867887 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Passenger aviation; median base and outer low/high from DAL in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Passenger aviation; median base and outer low/high from DAL in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| AAL | tl_fuel_cost_recovery_share | 0.5 | 0.3 | 0.7 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Passenger aviation; median base and outer low/high from DAL in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Passenger aviation; median base and outer low/high from DAL in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| LUV | tl_fuel_co2_mt | 14.39378 | 11.072139 | 18.424039 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Passenger aviation; median base and outer low/high from DAL in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Passenger aviation; median base and outer low/high from DAL in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| LUV | tl_fuel_cost_recovery_share | 0.5 | 0.3 | 0.7 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Passenger aviation; median base and outer low/high from DAL in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Passenger aviation; median base and outer low/high from DAL in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |

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
| exposure.tl_fuel_co2_mt | -0.084099404 | -0.13688123 | 0.05278183 |
| assumption.elasticity | -0.089305121 | -0.13197757 | 0.042672448 |
| exposure.tl_fuel_cost_recovery_share | -0.1295348 | -0.087563086 | 0.04197171 |
| assumption.variable_cost_share | -0.11312615 | -0.10206047 | 0.011065678 |

Dominant configured driver: `tl_fuel_co2_mt` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.

- REVIEW AAL: EPS -594.3%; Reported EPS denominator 0.17; dominant NI channel: Carbon charge on fuel burned; estimated exposures: tl_fuel_co2_mt, tl_fuel_cost_recovery_share. Review reported earnings, exposure denominator and linear transmission before use. Default scenario; realistic range not independently verified.
- REVIEW LUV: EPS -86.3%; Reported EPS denominator 0.79; dominant NI channel: Carbon charge on fuel burned; estimated exposures: tl_fuel_co2_mt, tl_fuel_cost_recovery_share. Review reported earnings, exposure denominator and linear transmission before use. Default scenario; realistic range not independently verified.

## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 34 unchecked in-scope exposure values; 2 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

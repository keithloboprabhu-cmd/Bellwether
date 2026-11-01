# Cap or ban on checked-bag fees

Policy `transportation_logistics/airline_bag_fee_cap` · evidence checkpoint 2026-11-01 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

A hypothetical federal restriction reduces reported airline baggage-fee revenue. American, Delta, United and Southwest use their own 2025 BTS observations. The input is a reduction in total baggage-fee revenue, not an exact mapping from a free-first-bag rule; fare recapture is an uncertain behavioral assumption.

Duration: `permanent`. Default inputs: `{"fee_cut_pct": 50.0}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| price | unavailable / unavailable | {"d_price": "-input.fee_cut_pct / 100", "exposed_revenue_share": "exposure.tl_checked_bag_fee_revenue_share", "offset_share": "assumption.fare_recapture"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://www.bts.gov/topics/airlines-and-airports/baggage-fees-airline-2025
- https://www.sec.gov/Archives/edgar/data/27904/000002790426000013/dal-20251231.htm

| Company | Configured status | Basis |
|---|---|---|
| UPS | outside_scope | The fee cap applies to airline checked baggage, not freight, rail, ride-hailing or vehicle sales. |
| FDX | outside_scope | The fee cap applies to airline checked baggage, not freight, rail, ride-hailing or vehicle sales. |
| UNP | outside_scope | The fee cap applies to airline checked baggage, not freight, rail, ride-hailing or vehicle sales. |
| DAL | included | Binding baggage cap reduces airline ancillary revenue. |
| TSLA | outside_scope | The fee cap applies to airline checked baggage, not freight, rail, ride-hailing or vehicle sales. |
| GM | outside_scope | The fee cap applies to airline checked baggage, not freight, rail, ride-hailing or vehicle sales. |
| F | outside_scope | The fee cap applies to airline checked baggage, not freight, rail, ride-hailing or vehicle sales. |
| RIVN | outside_scope | The fee cap applies to airline checked baggage, not freight, rail, ride-hailing or vehicle sales. |
| CHRW | outside_scope | The fee cap applies to airline checked baggage, not freight, rail, ride-hailing or vehicle sales. |
| JBHT | outside_scope | The fee cap applies to airline checked baggage, not freight, rail, ride-hailing or vehicle sales. |
| ODFL | outside_scope | The fee cap applies to airline checked baggage, not freight, rail, ride-hailing or vehicle sales. |
| XPO | outside_scope | The fee cap applies to airline checked baggage, not freight, rail, ride-hailing or vehicle sales. |
| SAIA | outside_scope | The fee cap applies to airline checked baggage, not freight, rail, ride-hailing or vehicle sales. |
| CSX | outside_scope | The fee cap applies to airline checked baggage, not freight, rail, ride-hailing or vehicle sales. |
| NSC | outside_scope | The fee cap applies to airline checked baggage, not freight, rail, ride-hailing or vehicle sales. |
| UAL | included | Binding baggage cap reduces airline ancillary revenue. |
| AAL | included | Binding baggage cap reduces airline ancillary revenue. |
| LUV | included | Binding baggage cap reduces airline ancillary revenue. |
| UBER | outside_scope | The fee cap applies to airline checked baggage, not freight, rail, ride-hailing or vehicle sales. |
| LYFT | outside_scope | The fee cap applies to airline checked baggage, not freight, rail, ride-hailing or vehicle sales. |

## B. Every in-scope exposure

Exact numeric checks are distinguished from filing links and estimates. UNVERIFIED values are retained, not silently replaced. Historical observed low/high values are not forecast confidence intervals.

| Company | Exposure | Base | Low | High | Exact-source status | Primary source / location / rationale |
|---|---|---:|---:|---:|---|---|
| DAL | tl_checked_bag_fee_revenue_share | 0.017199545 | 0.017199545 | 0.017199545 | VERIFIED observation; conversion limits retained | https://www.bts.gov/sites/bts.dot.gov/files/2026-05/Baggage%20Fees%202007-2025%204Q.xlsx · BTS Baggage Fees 2007-2025 4Q.xlsx, 2025 sheet, Delta row; annual sum $1089.832000M; SEC FY2025 total revenue $63364.0M · Observed FY2025 BTS carrier baggage fees / consolidated FY2025 operating revenue. BTS reporting-carrier perimeter can differ from consolidated regional operations. Fixed bounds identify the historical observation, not certainty about future fees. Fare recapture remains an unverified assumption. |
| UAL | tl_checked_bag_fee_revenue_share | 0.022876285 | 0.022876285 | 0.022876285 | VERIFIED observation; conversion limits retained | https://www.bts.gov/sites/bts.dot.gov/files/2026-05/Baggage%20Fees%202007-2025%204Q.xlsx · BTS Baggage Fees 2007-2025 4Q.xlsx, 2025 sheet, United row; annual sum $1351.302143M; SEC FY2025 total revenue $59070.0M · Observed FY2025 BTS carrier baggage fees / consolidated FY2025 operating revenue. BTS reporting-carrier perimeter can differ from consolidated regional operations. Fixed bounds identify the historical observation, not certainty about future fees. Fare recapture remains an unverified assumption. |
| AAL | tl_checked_bag_fee_revenue_share | 0.026821503 | 0.026821503 | 0.026821503 | VERIFIED observation; conversion limits retained | https://www.bts.gov/sites/bts.dot.gov/files/2026-05/Baggage%20Fees%202007-2025%204Q.xlsx · BTS Baggage Fees 2007-2025 4Q.xlsx, 2025 sheet, American row; annual sum $1465.339192M; SEC FY2025 total revenue $54633.0M · Observed FY2025 BTS carrier baggage fees / consolidated FY2025 operating revenue. BTS reporting-carrier perimeter can differ from consolidated regional operations. Fixed bounds identify the historical observation, not certainty about future fees. Fare recapture remains an unverified assumption. |
| LUV | tl_checked_bag_fee_revenue_share | 0.020753875 | 0.020753875 | 0.020753875 | VERIFIED observation; conversion limits retained | https://www.bts.gov/sites/bts.dot.gov/files/2026-05/Baggage%20Fees%202007-2025%204Q.xlsx · BTS Baggage Fees 2007-2025 4Q.xlsx, 2025 sheet, Southwest row; annual sum $582.416000M; SEC FY2025 total revenue $28063.0M · Observed FY2025 BTS carrier baggage fees / consolidated FY2025 operating revenue. BTS reporting-carrier perimeter can differ from consolidated regional operations. Fixed bounds identify the historical observation, not certainty about future fees. Fare recapture remains an unverified assumption. Southwest introduced broad checked-bag charges during 2025; this partial-year observation is not an annualized steady-state forecast. |

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
| assumption.fare_recapture | -0.035547107 | -0.015234474 | 0.020312633 |

Dominant configured driver: `fare_recapture` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.

- REVIEW AAL: EPS -239.0%; Reported EPS denominator 0.17; dominant NI channel: Lower checked-bag fee revenue; estimated exposures: none labeled estimate. Review reported earnings, exposure denominator and linear transmission before use. Default scenario; realistic range not independently verified.

## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 0 unchecked in-scope exposure values; 1 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| DAL | tl_checked_bag_fee_revenue_share | 0.0167 | 0.017199545 | https://www.bts.gov/sites/bts.dot.gov/files/2026-05/Baggage%20Fees%202007-2025%204Q.xlsx · BTS Baggage Fees 2007-2025 4Q.xlsx, 2025 sheet, Delta row; annual sum $1089.832000M |
| AAL | tl_checked_bag_fee_revenue_share | 0.0167 | 0.026821503 | https://www.bts.gov/sites/bts.dot.gov/files/2026-05/Baggage%20Fees%202007-2025%204Q.xlsx · BTS Baggage Fees 2007-2025 4Q.xlsx, 2025 sheet, American row; annual sum $1465.339192M |
| UAL | tl_checked_bag_fee_revenue_share | 0.0167 | 0.022876285 | https://www.bts.gov/sites/bts.dot.gov/files/2026-05/Baggage%20Fees%202007-2025%204Q.xlsx · BTS Baggage Fees 2007-2025 4Q.xlsx, 2025 sheet, United row; annual sum $1351.302143M |
| LUV | tl_checked_bag_fee_revenue_share | 0.0167 | 0.020753875 | https://www.bts.gov/sites/bts.dot.gov/files/2026-05/Baggage%20Fees%202007-2025%204Q.xlsx · BTS Baggage Fees 2007-2025 4Q.xlsx, 2025 sheet, Southwest row; annual sum $582.416000M |

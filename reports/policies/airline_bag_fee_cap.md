# Cap or ban on checked-bag fees

Policy `transportation_logistics/airline_bag_fee_cap` · reviewed 2026-10-31 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

A federal "junk fee" rule that cuts checked-bag fees, for example by making the first checked bag free. Delta is the only exposed company in this universe, and airlines would win back part of the lost revenue through higher base fares.

Duration: `permanent`. Default inputs: `{"fee_cut_pct": 50.0}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| price | unavailable / unavailable | {"d_price": "-input.fee_cut_pct / 100", "exposed_revenue_share": "exposure.tl_checked_bag_fee_revenue_share", "offset_share": "assumption.fare_recapture"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://www.aol.com/airlines-raked-over-7b-revenue-152456333.html
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
| DAL | tl_checked_bag_fee_revenue_share | 0.0167 | 0.0158 | 0.0182 | UNVERIFIED | https://www.aol.com/airlines-raked-over-7b-revenue-152456333.html · estimate; Delta's 10-K reports bag fees only inside travel-related services. BTS data reported in the press put Delta's 2024 checked-bag fees above $1B (~$1.06B); $1,000-1,150M of $63,364M 2025 revenue. · Delta's 10-K reports bag fees only inside travel-related services. BTS data reported in the press put Delta's 2024 checked-bag fees above $1B (~$1.06B); $1,000-1,150M of $63,364M 2025 revenue. |
| UAL | tl_checked_bag_fee_revenue_share | 0.0167 | 0.0158 | 0.0182 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Passenger aviation; median base and outer low/high from DAL in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Passenger aviation; median base and outer low/high from DAL in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| AAL | tl_checked_bag_fee_revenue_share | 0.0167 | 0.0158 | 0.0182 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Passenger aviation; median base and outer low/high from DAL in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Passenger aviation; median base and outer low/high from DAL in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| LUV | tl_checked_bag_fee_revenue_share | 0.0167 | 0.0158 | 0.0182 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Passenger aviation; median base and outer low/high from DAL in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Passenger aviation; median base and outer low/high from DAL in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |

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
| assumption.fare_recapture | -0.027295964 | -0.01169827 | 0.015597693 |
| exposure.tl_checked_bag_fee_revenue_share | -0.018446374 | -0.021248355 | 0.0028019809 |

Dominant configured driver: `fare_recapture` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.

- REVIEW AAL: EPS -148.8%; Reported EPS denominator 0.17; dominant NI channel: Lower checked-bag fee revenue; estimated exposures: tl_checked_bag_fee_revenue_share. Review reported earnings, exposure denominator and linear transmission before use. Default scenario; realistic range not independently verified.

## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 4 unchecked in-scope exposure values; 1 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

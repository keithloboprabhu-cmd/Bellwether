# Change in the domestic airline ticket tax

Policy `transportation_logistics/airline_ticket_tax_change` · evidence checkpoint 2026-11-01 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

Raises or lowers the federal percentage tax on taxable passenger air transportation from a 7.5% reference. American, Delta, United and Southwest have modeled passenger exposure; geographic passenger revenue is a proxy for the taxable fare base. The separate cargo and segment taxes are not changed.

Duration: `permanent`. Default inputs: `{"d_tax_pts": 2.5}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| demand_price | unavailable / unavailable | {"dp_consumer": "derived.dtax_rel * assumption.consumer_incidence", "elasticity": "assumption.elasticity", "exposed_revenue_share": "exposure.tl_domestic_passenger_revenue_share"} |
| price | unavailable / unavailable | {"d_price": "-derived.dtax_rel * (1 - assumption.consumer_incidence)", "exposed_revenue_share": "exposure.tl_domestic_passenger_revenue_share"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://www.sec.gov/Archives/edgar/data/27904/000002790426000013/dal-20251231.htm
- https://WWW.CAA.CO.UK/media/qcrcutdj/annex-3-stansted-s-own-airport-charge-elasticity-a-summary-of-the-evidence-and-research.pdf

| Company | Configured status | Basis |
|---|---|---|
| UPS | outside_scope | Domestic airline ticket excise tax is not a tax on ride-hailing fares, freight or vehicle sales. |
| FDX | outside_scope | Domestic airline ticket excise tax is not a tax on ride-hailing fares, freight or vehicle sales. |
| UNP | outside_scope | Domestic airline ticket excise tax is not a tax on ride-hailing fares, freight or vehicle sales. |
| DAL | included | Higher ticket tax reduces demand and modeled fare retention. |
| TSLA | outside_scope | Domestic airline ticket excise tax is not a tax on ride-hailing fares, freight or vehicle sales. |
| GM | outside_scope | Domestic airline ticket excise tax is not a tax on ride-hailing fares, freight or vehicle sales. |
| F | outside_scope | Domestic airline ticket excise tax is not a tax on ride-hailing fares, freight or vehicle sales. |
| RIVN | outside_scope | Domestic airline ticket excise tax is not a tax on ride-hailing fares, freight or vehicle sales. |
| CHRW | outside_scope | Domestic airline ticket excise tax is not a tax on ride-hailing fares, freight or vehicle sales. |
| JBHT | outside_scope | Domestic airline ticket excise tax is not a tax on ride-hailing fares, freight or vehicle sales. |
| ODFL | outside_scope | Domestic airline ticket excise tax is not a tax on ride-hailing fares, freight or vehicle sales. |
| XPO | outside_scope | Domestic airline ticket excise tax is not a tax on ride-hailing fares, freight or vehicle sales. |
| SAIA | outside_scope | Domestic airline ticket excise tax is not a tax on ride-hailing fares, freight or vehicle sales. |
| CSX | outside_scope | Domestic airline ticket excise tax is not a tax on ride-hailing fares, freight or vehicle sales. |
| NSC | outside_scope | Domestic airline ticket excise tax is not a tax on ride-hailing fares, freight or vehicle sales. |
| UAL | included | Higher ticket tax reduces demand and modeled fare retention. |
| AAL | included | Higher ticket tax reduces demand and modeled fare retention. |
| LUV | included | Higher ticket tax reduces demand and modeled fare retention. |
| UBER | outside_scope | Domestic airline ticket excise tax is not a tax on ride-hailing fares, freight or vehicle sales. |
| LYFT | outside_scope | Domestic airline ticket excise tax is not a tax on ride-hailing fares, freight or vehicle sales. |

## B. Every in-scope exposure

Exact numeric checks are distinguished from filing links and estimates. UNVERIFIED values are retained, not silently replaced. Historical observed low/high values are not forecast confidence intervals.

| Company | Exposure | Base | Low | High | Exact-source status | Primary source / location / rationale |
|---|---|---:|---:|---:|---|---|
| DAL | tl_domestic_passenger_revenue_share | 0.56390064 | 0.56390064 | 0.56390064 | VERIFIED observation; conversion limits retained | https://www.sec.gov/Archives/edgar/data/27904/000002790426000013/0000027904-26-000013-index.htm · DAL FY2025 Form 10-K, geographic passenger revenue: domestic $35731M / total $63364.0M · Reported domestic passenger revenue / consolidated total revenue, not a fully measured taxable-fare base. Statutory ticket-tax exclusions and US-border rules are not separately quantified. |
| UAL | tl_domestic_passenger_revenue_share | 0.564 | 0.564 | 0.564 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Passenger aviation; median base and outer low/high from DAL in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Passenger aviation; median base and outer low/high from DAL in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| AAL | tl_domestic_passenger_revenue_share | 0.64431754 | 0.64431754 | 0.64431754 | VERIFIED observation; conversion limits retained | https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm · AAL FY2025 Form 10-K, geographic passenger revenue: domestic $35201M / total $54633.0M · Reported domestic passenger revenue / consolidated total revenue, not a fully measured taxable-fare base. Statutory ticket-tax exclusions and US-border rules are not separately quantified. |
| LUV | tl_domestic_passenger_revenue_share | 0.564 | 0.564 | 0.564 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Passenger aviation; median base and outer low/high from DAL in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Passenger aviation; median base and outer low/high from DAL in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |

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
| assumption.consumer_incidence | -0.033848758 | -0.0042553498 | 0.029593408 |
| assumption.elasticity | -0.018254176 | -0.021445688 | 0.0031915123 |

Dominant configured driver: `consumer_incidence` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.

- REVIEW AAL: EPS -142.1%; Reported EPS denominator 0.17; dominant NI channel: Base fares cut to absorb part of the tax; estimated exposures: none labeled estimate. Review reported earnings, exposure denominator and linear transmission before use. Default scenario; realistic range not independently verified.

## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 2 unchecked in-scope exposure values; 2 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

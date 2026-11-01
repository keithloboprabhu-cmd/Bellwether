# Restore a consumer EV tax credit

Policy `transportation_logistics/ev_tax_credit` · reviewed 2026-10-31 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

Reinstates a point-of-sale federal credit for new electric vehicles, ended September 30, 2025 by the One Big Beautiful Bill Act. Tesla and GM, the two largest US EV sellers, gain volume and some price. The other four companies are unaffected.

Duration: `permanent`. Default inputs: `{"credit_usd": 7500.0}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| demand_price | unavailable / unavailable | {"dp_consumer": "derived.dp_buyer", "elasticity": "assumption.elasticity", "exposed_revenue_share": "derived.eligible_rev_share"} |
| price | unavailable / unavailable | {"d_price": "derived.dp_seller", "exposed_revenue_share": "derived.eligible_rev_share"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://www.nber.org/papers/w25359
- https://www.coxautoinc.com/insights/dec-2025-atp-report/
- https://electrek.co/2026/01/06/gm-sold-twice-as-many-evs-as-ford-2025/

| Company | Configured status | Basis |
|---|---|---|
| UPS | outside_scope | The modeled demand channel covers qualifying US EV sales. Fleet buyers, airlines and mobility-platform drivers are outside this manufacturer-sales channel. |
| FDX | outside_scope | The modeled demand channel covers qualifying US EV sales. Fleet buyers, airlines and mobility-platform drivers are outside this manufacturer-sales channel. |
| UNP | outside_scope | The modeled demand channel covers qualifying US EV sales. Fleet buyers, airlines and mobility-platform drivers are outside this manufacturer-sales channel. |
| DAL | outside_scope | The modeled demand channel covers qualifying US EV sales. Fleet buyers, airlines and mobility-platform drivers are outside this manufacturer-sales channel. |
| TSLA | included | Buyer incentive increases covered US EV demand. |
| GM | included | Buyer incentive increases covered US EV demand. |
| F | included | Buyer incentive increases covered US EV demand. |
| RIVN | included | Buyer incentive increases covered US EV demand. |
| CHRW | outside_scope | The modeled demand channel covers qualifying US EV sales. Fleet buyers, airlines and mobility-platform drivers are outside this manufacturer-sales channel. |
| JBHT | outside_scope | The modeled demand channel covers qualifying US EV sales. Fleet buyers, airlines and mobility-platform drivers are outside this manufacturer-sales channel. |
| ODFL | outside_scope | The modeled demand channel covers qualifying US EV sales. Fleet buyers, airlines and mobility-platform drivers are outside this manufacturer-sales channel. |
| XPO | outside_scope | The modeled demand channel covers qualifying US EV sales. Fleet buyers, airlines and mobility-platform drivers are outside this manufacturer-sales channel. |
| SAIA | outside_scope | The modeled demand channel covers qualifying US EV sales. Fleet buyers, airlines and mobility-platform drivers are outside this manufacturer-sales channel. |
| CSX | outside_scope | The modeled demand channel covers qualifying US EV sales. Fleet buyers, airlines and mobility-platform drivers are outside this manufacturer-sales channel. |
| NSC | outside_scope | The modeled demand channel covers qualifying US EV sales. Fleet buyers, airlines and mobility-platform drivers are outside this manufacturer-sales channel. |
| UAL | outside_scope | The modeled demand channel covers qualifying US EV sales. Fleet buyers, airlines and mobility-platform drivers are outside this manufacturer-sales channel. |
| AAL | outside_scope | The modeled demand channel covers qualifying US EV sales. Fleet buyers, airlines and mobility-platform drivers are outside this manufacturer-sales channel. |
| LUV | outside_scope | The modeled demand channel covers qualifying US EV sales. Fleet buyers, airlines and mobility-platform drivers are outside this manufacturer-sales channel. |
| UBER | outside_scope | The modeled demand channel covers qualifying US EV sales. Fleet buyers, airlines and mobility-platform drivers are outside this manufacturer-sales channel. |
| LYFT | outside_scope | The modeled demand channel covers qualifying US EV sales. Fleet buyers, airlines and mobility-platform drivers are outside this manufacturer-sales channel. |

## B. Every in-scope exposure

Exact numeric checks are distinguished from filing links and estimates. UNVERIFIED values are retained, not silently replaced. Historical observed low/high values are not forecast confidence intervals.

| Company | Exposure | Base | Low | High | Exact-source status | Primary source / location / rationale |
|---|---|---:|---:|---:|---|---|
| TSLA | tl_us_ev_revenue_share | 0.35 | 0.3 | 0.4 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1318605/000162828026003952/tsla-20251231.htm · estimate; Tesla 2025 10-K: automotive sales $65,821M (69% of $94,827M) and US revenue $47,627M (50%); assuming the US share of auto sales matches the total gives ~0.35. · Tesla 2025 10-K: automotive sales $65,821M (69% of $94,827M) and US revenue $47,627M (50%); assuming the US share of auto sales matches the total gives ~0.35. |
| GM | tl_us_ev_revenue_share | 0.053 | 0.045 | 0.06 | UNVERIFIED | https://electrek.co/2026/01/06/gm-sold-twice-as-many-evs-as-ford-2025/ · estimate; GM sold 169,887 EVs in the US in 2025 (Electrek, Jan 2026). At the Dec 2025 average EV transaction price of $58,034 (Cox/KBB) that is ~$9.9B of $185,019M revenue. · GM sold 169,887 EVs in the US in 2025 (Electrek, Jan 2026). At the Dec 2025 average EV transaction price of $58,034 (Cox/KBB) that is ~$9.9B of $185,019M revenue. |
| F | tl_us_ev_revenue_share | 0.025 | 0.015 | 0.045 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/37996/000003799626000015/0000037996-26-000015-index.htm · estimate; Company-specific estimate: US battery-electric sales are a small minority of Ford consolidated revenue; estimate 2.5% (1.5–4.5%), not the Tesla/GM median. · Company-specific estimate: US battery-electric sales are a small minority of Ford consolidated revenue; estimate 2.5% (1.5–4.5%), not the Tesla/GM median. |
| RIVN | tl_us_ev_revenue_share | 0.85 | 0.65 | 0.98 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1874178/000187417826000008/0001874178-26-000008-index.htm · estimate; Company-specific estimate: Rivian primarily sells battery-electric vehicles, but consolidated revenue also includes software/services and non-US sales. Estimate 85% (65–98%) US EV revenue, not the Tesla/GM median. · Company-specific estimate: Rivian primarily sells battery-electric vehicles, but consolidated revenue also includes software/services and non-US sales. Estimate 85% (65–98%) US EV revenue, not the Tesla/GM median. |

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
| assumption.elasticity | 0.029703033 | 0.061738952 | 0.03203592 |
| assumption.eligible_share | 0.031165495 | 0.056097892 | 0.024932396 |
| assumption.buyer_capture | 0.052318392 | 0.03277332 | 0.019545073 |
| exposure.tl_us_ev_revenue_share | 0.036470865 | 0.051488811 | 0.015017946 |
| assumption.avg_ev_price | 0.048694648 | 0.040840673 | 0.0078539755 |

Dominant configured driver: `elasticity` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.


## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 4 unchecked in-scope exposure values; 4 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

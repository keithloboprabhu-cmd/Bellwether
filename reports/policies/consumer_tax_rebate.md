# Consumer tax rebate / stimulus check

Policy `consumer_retail/consumer_tax_rebate` · reviewed 2026-10-31 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

A one-time payment to households; part of it is spent, raising retail revenue for a year.

Duration: `one_time`. Default inputs: `{"amount_per_recipient": 1000.0, "recipients": 130.0}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| demand_transfer | unavailable / unavailable | {"total_transfer_musd": "derived.total_transfer_musd", "mpc": "assumption.mpc", "capture_share": "baseline.revenue * exposure.us_consumer_revenue_share / macro.pce_musd", "tilt": "assumption.goods_tilt"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://www.nber.org/papers/w16684
- https://fred.stlouisfed.org/series/PCE

| Company | Configured status | Basis |
|---|---|---|
| WMT | included | Consumer transfers raise captured retailer spending. |
| TGT | included | Consumer transfers raise captured retailer spending. |
| COST | included | Consumer transfers raise captured retailer spending. |
| AMZN | included | Consumer transfers raise captured retailer spending. |
| NKE | included | Consumer transfers raise captured retailer spending. |
| HD | included | Consumer transfers raise captured retailer spending. |
| LOW | included | Consumer transfers raise captured retailer spending. |
| KR | included | Consumer transfers raise captured retailer spending. |
| DG | included | Consumer transfers raise captured retailer spending. |
| DLTR | included | Consumer transfers raise captured retailer spending. |
| TJX | included | Consumer transfers raise captured retailer spending. |
| ROST | included | Consumer transfers raise captured retailer spending. |
| SBUX | included | Consumer transfers raise captured retailer spending. |
| MCD | included | Consumer transfers raise captured retailer spending. |
| KO | included | Consumer transfers raise captured retailer spending. |
| PEP | included | Consumer transfers raise captured retailer spending. |
| PG | included | Consumer transfers raise captured retailer spending. |
| CL | included | Consumer transfers raise captured retailer spending. |
| ULTA | included | Consumer transfers raise captured retailer spending. |
| BBY | included | Consumer transfers raise captured retailer spending. |
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
| WMT | us_consumer_revenue_share | 0.8 | 0.72 | 0.81 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/wmt-20260131.htm · Walmart FY2026 10-K: Walmart U.S. net sales $482,975M + Sam's Club U.S. $93,015M = 80.8% of $713,163M total revenues; Base trims US advertising/other revenue; low end treats part of Sam's Club as business buyers. · Base trims US advertising/other revenue; low end treats part of Sam's Club as business buyers. |
| TGT | us_consumer_revenue_share | 0.98 | 0.95 | 0.98 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/27419/000002741926000016/tgt-20260131.htm · Target FY2025 10-K: merchandise sales $102,717M of $104,780M net sales (98.0%); all stores are in the US; Excludes advertising, credit-card profit sharing and other revenue; low end allows for some business purchasers. · Excludes advertising, credit-card profit sharing and other revenue; low end allows for some business purchasers. |
| COST | us_consumer_revenue_share | 0.7 | 0.6 | 0.725 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/909832/000090983226000093/cost-20260830.htm · Costco FY2026 10-K: United States segment total revenue $219,823M of $303,154M (72.5%); Base and low strip out business members (business centers, Executive/Business memberships). · Base and low strip out business members (business centers, Executive/Business memberships). |
| AMZN | us_consumer_revenue_share | 0.55 | 0.45 | 0.595 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm · Amazon 2025 10-K: North America segment net sales $426,305M of $716,924M (59.5%); United States net sales $489,657M incl. AWS; Base strips Canada/Mexico and advertising sold to businesses from North America; low also strips third-party seller fees. · Base strips Canada/Mexico and advertising sold to businesses from North America; low also strips third-party seller fees. |
| NKE | us_consumer_revenue_share | 0.44 | 0.4 | 0.44 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/320187/000032018726000088/nke-20260531.htm · Nike FY2026 10-K: NIKE Brand and Converse sales in the United States ~44% of total revenues; Includes wholesale sales to US retailers, which reach US consumers; low trims team/institutional sales. · Includes wholesale sales to US retailers, which reach US consumers; low trims team/institutional sales. |
| HD | us_consumer_revenue_share | 0.88 | 0.45 | 0.92 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/354950/000162828026019436/hd-20260201.htm · Home Depot FY2025 10-K: net sales in the US $152,170M of $164,683M (92.4%); Roughly half of sales go to Pro (contractor) customers, so the low end counts only DIY consumers. · Roughly half of sales go to Pro (contractor) customers, so the low end counts only DIY consumers. |
| LOW | us_consumer_revenue_share | 0.88 | 0.45 | 0.92 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Home improvement; median base and outer low/high from HD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Home improvement; median base and outer low/high from HD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| KR | us_consumer_revenue_share | 0.8 | 0.6 | 0.98 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Groceries and discount retail; median base and outer low/high from WMT/COST/TGT in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Groceries and discount retail; median base and outer low/high from WMT/COST/TGT in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| DG | us_consumer_revenue_share | 0.8 | 0.6 | 0.98 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Groceries and discount retail; median base and outer low/high from WMT/COST/TGT in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Groceries and discount retail; median base and outer low/high from WMT/COST/TGT in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| DLTR | us_consumer_revenue_share | 0.8 | 0.6 | 0.98 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Groceries and discount retail; median base and outer low/high from WMT/COST/TGT in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Groceries and discount retail; median base and outer low/high from WMT/COST/TGT in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| TJX | us_consumer_revenue_share | 0.71 | 0.4 | 0.98 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Apparel and specialty retail; median base and outer low/high from TGT/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Apparel and specialty retail; median base and outer low/high from TGT/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| ROST | us_consumer_revenue_share | 0.71 | 0.4 | 0.98 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Apparel and specialty retail; median base and outer low/high from TGT/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Apparel and specialty retail; median base and outer low/high from TGT/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| SBUX | us_consumer_revenue_share | 0.7 | 0.4 | 0.81 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Restaurants and consumer staples; median base and outer low/high from WMT/COST/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Restaurants and consumer staples; median base and outer low/high from WMT/COST/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| MCD | us_consumer_revenue_share | 0.7 | 0.4 | 0.81 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Restaurants and consumer staples; median base and outer low/high from WMT/COST/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Restaurants and consumer staples; median base and outer low/high from WMT/COST/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| KO | us_consumer_revenue_share | 0.7 | 0.4 | 0.81 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Restaurants and consumer staples; median base and outer low/high from WMT/COST/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Restaurants and consumer staples; median base and outer low/high from WMT/COST/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| PEP | us_consumer_revenue_share | 0.7 | 0.4 | 0.81 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Restaurants and consumer staples; median base and outer low/high from WMT/COST/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Restaurants and consumer staples; median base and outer low/high from WMT/COST/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| PG | us_consumer_revenue_share | 0.7 | 0.4 | 0.81 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Restaurants and consumer staples; median base and outer low/high from WMT/COST/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Restaurants and consumer staples; median base and outer low/high from WMT/COST/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| CL | us_consumer_revenue_share | 0.7 | 0.4 | 0.81 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Restaurants and consumer staples; median base and outer low/high from WMT/COST/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Restaurants and consumer staples; median base and outer low/high from WMT/COST/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| ULTA | us_consumer_revenue_share | 0.71 | 0.4 | 0.98 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Apparel and specialty retail; median base and outer low/high from TGT/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Apparel and specialty retail; median base and outer low/high from TGT/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| BBY | us_consumer_revenue_share | 0.71 | 0.4 | 0.98 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Apparel and specialty retail; median base and outer low/high from TGT/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Apparel and specialty retail; median base and outer low/high from TGT/NKE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |

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
| assumption.goods_tilt | 0.0056468425 | 0.013175966 | 0.0075291234 |
| assumption.mpc | 0.0067224316 | 0.012100377 | 0.0053779453 |
| exposure.us_consumer_revenue_share | 0.007096877 | 0.010276853 | 0.0031799765 |

Dominant configured driver: `goods_tilt` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.


## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 20 unchecked in-scope exposure values; 2 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

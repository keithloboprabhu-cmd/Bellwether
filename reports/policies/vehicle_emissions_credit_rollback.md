# Weaker vehicle emissions standards (credit market shrinks)

Policy `transportation_logistics/vehicle_emissions_credit_rollback` · evidence checkpoint 2026-11-01 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

Loosening or repealing federal GHG/CAFE standards and California ZEV rules lowers the value of the regulatory credits automakers trade. Tesla loses high-margin credit revenue, and credit buyers save. Tesla and Rivian are modeled sellers; GM and Ford are modeled buyers. Firm-specific forward exposure is uncertain.

Duration: `permanent`. Default inputs: `{"credit_value_change_pct": -50.0}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| price | unavailable / unavailable | {"d_price": "input.credit_value_change_pct / 100", "exposed_revenue_share": "exposure.tl_regulatory_credit_revenue_share", "offset_share": "1 - assumption.margin_on_credits"} |
| cost | unavailable / unavailable | {"exposed_cost_share": 0.0, "shock_pct": 0.0, "dcost_musd": "exposure.tl_regulatory_credit_purchases_musd * input.credit_value_change_pct / 100"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://www.sec.gov/Archives/edgar/data/1318605/000162828026003952/tsla-20251231.htm
- https://www.sec.gov/Archives/edgar/data/1467858/000146785826000013/gm-20251231.htm

| Company | Configured status | Basis |
|---|---|---|
| UPS | outside_scope | Only separately identified manufacturer credit sales and purchases are covered; freight and travel companies do not sell these automotive compliance credits. |
| FDX | outside_scope | Only separately identified manufacturer credit sales and purchases are covered; freight and travel companies do not sell these automotive compliance credits. |
| UNP | outside_scope | Only separately identified manufacturer credit sales and purchases are covered; freight and travel companies do not sell these automotive compliance credits. |
| DAL | outside_scope | Only separately identified manufacturer credit sales and purchases are covered; freight and travel companies do not sell these automotive compliance credits. |
| TSLA | included | Weaker standards hurt credit sellers and help credit purchasers. |
| GM | included | Weaker standards hurt credit sellers and help credit purchasers. |
| F | included | Weaker standards hurt credit sellers and help credit purchasers. |
| RIVN | included | Weaker standards hurt credit sellers and help credit purchasers. |
| CHRW | outside_scope | Only separately identified manufacturer credit sales and purchases are covered; freight and travel companies do not sell these automotive compliance credits. |
| JBHT | outside_scope | Only separately identified manufacturer credit sales and purchases are covered; freight and travel companies do not sell these automotive compliance credits. |
| ODFL | outside_scope | Only separately identified manufacturer credit sales and purchases are covered; freight and travel companies do not sell these automotive compliance credits. |
| XPO | outside_scope | Only separately identified manufacturer credit sales and purchases are covered; freight and travel companies do not sell these automotive compliance credits. |
| SAIA | outside_scope | Only separately identified manufacturer credit sales and purchases are covered; freight and travel companies do not sell these automotive compliance credits. |
| CSX | outside_scope | Only separately identified manufacturer credit sales and purchases are covered; freight and travel companies do not sell these automotive compliance credits. |
| NSC | outside_scope | Only separately identified manufacturer credit sales and purchases are covered; freight and travel companies do not sell these automotive compliance credits. |
| UAL | outside_scope | Only separately identified manufacturer credit sales and purchases are covered; freight and travel companies do not sell these automotive compliance credits. |
| AAL | outside_scope | Only separately identified manufacturer credit sales and purchases are covered; freight and travel companies do not sell these automotive compliance credits. |
| LUV | outside_scope | Only separately identified manufacturer credit sales and purchases are covered; freight and travel companies do not sell these automotive compliance credits. |
| UBER | outside_scope | Only separately identified manufacturer credit sales and purchases are covered; freight and travel companies do not sell these automotive compliance credits. |
| LYFT | outside_scope | Only separately identified manufacturer credit sales and purchases are covered; freight and travel companies do not sell these automotive compliance credits. |

## B. Every in-scope exposure

Exact numeric checks are distinguished from filing links and estimates. UNVERIFIED values are retained, not silently replaced. Historical observed low/high values are not forecast confidence intervals.

| Company | Exposure | Base | Low | High | Exact-source status | Primary source / location / rationale |
|---|---|---:|---:|---:|---|---|
| TSLA | tl_regulatory_credit_revenue_share | 0.021 | 0.021 | 0.021 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1318605/000162828026003952/tsla-20251231.htm · Tesla 2025 10-K: automotive regulatory credits revenue $1,993M of $94,827M total revenue;  · unavailable |
| TSLA | tl_regulatory_credit_purchases_musd | 0 | 0 | 0 | UNVERIFIED | No source URL · estimate; Tesla sells credits and does not buy them. · Tesla sells credits and does not buy them. |
| GM | tl_regulatory_credit_revenue_share | 0 | 0 | 0 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1467858/000146785826000013/0001467858-26-000013-index.htm · estimate; Company-specific scope estimate: Modeled regulatory-credit sellers. Ford is treated as a purchaser rather than inheriting Tesla's seller revenue. This is a model boundary, not a reported zero measurement. · Company-specific scope estimate: Modeled regulatory-credit sellers. Ford is treated as a purchaser rather than inheriting Tesla's seller revenue. This is a model boundary, not a reported zero measurement. |
| GM | tl_regulatory_credit_purchases_musd | 100 | 0 | 500 | UNVERIFIED | No source URL · estimate; GM does not disclose credit purchases. Its rising EV volume earns it credits, so net purchases are likely modest; the high case allows for past GHG/CAFE credit buying. · GM does not disclose credit purchases. Its rising EV volume earns it credits, so net purchases are likely modest; the high case allows for past GHG/CAFE credit buying. |
| F | tl_regulatory_credit_revenue_share | 0 | 0 | 0 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/37996/000003799626000015/0000037996-26-000015-index.htm · estimate; Company-specific scope estimate: Modeled regulatory-credit sellers. Ford is treated as a purchaser rather than inheriting Tesla's seller revenue. This is a model boundary, not a reported zero measurement. · Company-specific scope estimate: Modeled regulatory-credit sellers. Ford is treated as a purchaser rather than inheriting Tesla's seller revenue. This is a model boundary, not a reported zero measurement. |
| F | tl_regulatory_credit_purchases_musd | 50.607505 | 0 | 506.07505 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Automotive; median base and outer low/high from TSLA/GM in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Automotive; median base and outer low/high from TSLA/GM in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| RIVN | tl_regulatory_credit_revenue_share | 0.05 | 0.02 | 0.12 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1874178/000187417826000008/0001874178-26-000008-index.htm · estimate; Company-specific estimate: Rivian is an EV regulatory-credit seller. Estimate 5% of consolidated revenue (2–12%) pending a normalized forward sales stream; do not also assign purchased credits. · Company-specific estimate: Rivian is an EV regulatory-credit seller. Estimate 5% of consolidated revenue (2–12%) pending a normalized forward sales stream; do not also assign purchased credits. |
| RIVN | tl_regulatory_credit_purchases_musd | 0 | 0 | 0 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1874178/000187417826000008/0001874178-26-000008-index.htm · estimate; Company-specific scope estimate: Modeled credit purchasers. Rivian is a seller; its Tesla/GM peer median must not imply simultaneous purchased credits. This is a model boundary, not a reported zero measurement. · Company-specific scope estimate: Modeled credit purchasers. Rivian is a seller; its Tesla/GM peer median must not imply simultaneous purchased credits. This is a model boundary, not a reported zero measurement. |

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
| exposure.tl_regulatory_credit_purchases_musd | -0.024100206 | -0.011901362 | 0.012198844 |
| exposure.tl_regulatory_credit_revenue_share | -0.02037511 | -0.026612859 | 0.0062377486 |
| assumption.margin_on_credits | -0.019836414 | -0.022246435 | 0.0024100206 |

Dominant configured driver: `tl_regulatory_credit_purchases_musd` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.


## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 8 unchecked in-scope exposure values; 1 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

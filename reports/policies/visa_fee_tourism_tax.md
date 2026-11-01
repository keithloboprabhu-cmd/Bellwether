# Visa fee / tourist entry tax

Policy `real_estate_hospitality/visa_fee_tourism_tax` · reviewed 2026-10-31 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

A new per-visitor fee on foreign travellers who need a US visa raises the cost of a trip and deters some visits, trimming hotel and short-term-rental demand from inbound tourists. Exposure is a few percent of revenue at most; logistics and tower REITs are untouched.

Duration: `permanent`. Default inputs: `{"fee_usd": 250.0}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| demand_price | unavailable / unavailable | {"dp_consumer": "input.fee_usd / assumption.trip_spend_usd", "elasticity": "assumption.elasticity", "exposed_revenue_share": "exposure.re_intl_inbound_revenue_share * assumption.visa_required_share"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://www.travelmole.com/news/economic-impact-overseas-visitors-usa/

| Company | Configured status | Basis |
|---|---|---|
| PLD | outside_scope | The tourism channel requires quantified inbound visitor sales; broad property rents are not automatically inbound tourism revenue. |
| AMT | outside_scope | The tourism channel requires quantified inbound visitor sales; broad property rents are not automatically inbound tourism revenue. |
| SPG | included | Higher entry costs reduce inbound visitor spending. |
| MAR | included | Higher entry costs reduce inbound visitor spending. |
| HLT | included | Higher entry costs reduce inbound visitor spending. |
| ABNB | included | Higher entry costs reduce inbound visitor spending. |
| O | outside_scope | The tourism channel requires quantified inbound visitor sales; broad property rents are not automatically inbound tourism revenue. |
| EQIX | outside_scope | The tourism channel requires quantified inbound visitor sales; broad property rents are not automatically inbound tourism revenue. |
| DLR | outside_scope | The tourism channel requires quantified inbound visitor sales; broad property rents are not automatically inbound tourism revenue. |
| WELL | outside_scope | The tourism channel requires quantified inbound visitor sales; broad property rents are not automatically inbound tourism revenue. |
| VTR | outside_scope | The tourism channel requires quantified inbound visitor sales; broad property rents are not automatically inbound tourism revenue. |
| ESS | outside_scope | The tourism channel requires quantified inbound visitor sales; broad property rents are not automatically inbound tourism revenue. |
| MAA | outside_scope | The tourism channel requires quantified inbound visitor sales; broad property rents are not automatically inbound tourism revenue. |
| PSA | outside_scope | The tourism channel requires quantified inbound visitor sales; broad property rents are not automatically inbound tourism revenue. |
| EXR | outside_scope | The tourism channel requires quantified inbound visitor sales; broad property rents are not automatically inbound tourism revenue. |
| VICI | outside_scope | The tourism channel requires quantified inbound visitor sales; broad property rents are not automatically inbound tourism revenue. |
| WY | outside_scope | The tourism channel requires quantified inbound visitor sales; broad property rents are not automatically inbound tourism revenue. |
| HST | included | Higher entry costs reduce inbound visitor spending. |
| RLJ | included | Higher entry costs reduce inbound visitor spending. |
| PK | included | Higher entry costs reduce inbound visitor spending. |

## B. Every in-scope exposure

Exact numeric checks are distinguished from filing links and estimates. UNVERIFIED values are retained, not silently replaced. Historical observed low/high values are not forecast confidence intervals.

| Company | Exposure | Base | Low | High | Exact-source status | Primary source / location / rationale |
|---|---|---:|---:|---:|---|---|
| SPG | re_intl_inbound_revenue_share | 0.02 | 0.005 | 0.04 | UNVERIFIED | No source URL · estimate; Rents are partly sales-linked and premium outlets draw foreign shoppers, but most rent is fixed; a small indirect share. · Rents are partly sales-linked and premium outlets draw foreign shoppers, but most rent is fixed; a small indirect share. |
| MAR | re_intl_inbound_revenue_share | 0.05 | 0.03 | 0.08 | UNVERIFIED | No source URL · estimate; ~70% of fees from US & Canada hotels, of which foreign visitors are assumed ~7% of room demand. · ~70% of fees from US & Canada hotels, of which foreign visitors are assumed ~7% of room demand. |
| HLT | re_intl_inbound_revenue_share | 0.055 | 0.03 | 0.08 | UNVERIFIED | No source URL · estimate; 79% of revenue from US hotels, of which foreign visitors are assumed ~7% of room demand. · 79% of revenue from US hotels, of which foreign visitors are assumed ~7% of room demand. |
| ABNB | re_intl_inbound_revenue_share | 0.04 | 0.02 | 0.07 | UNVERIFIED | No source URL · estimate; 39% of revenue is US (10-K); foreign guests assumed ~10% of US bookings. · 39% of revenue is US (10-K); foreign guests assumed ~10% of US bookings. |
| HST | re_intl_inbound_revenue_share | 0.05 | 0.02 | 0.1 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1070750/000107075026000054/0001070750-26-000054-index.htm · estimate; Company-specific estimate: Estimate inbound international guests contribute 5% of total hotel revenue (2–10%). Guest-origin revenue is not separately disclosed; no tower/logistics peer inference. · Company-specific estimate: Estimate inbound international guests contribute 5% of total hotel revenue (2–10%). Guest-origin revenue is not separately disclosed; no tower/logistics peer inference. |
| RLJ | re_intl_inbound_revenue_share | 0.05 | 0.02 | 0.1 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1511337/000151133726000007/0001511337-26-000007-index.htm · estimate; Company-specific estimate: Estimate inbound international guests contribute 5% of total hotel revenue (2–10%). Guest-origin revenue is not separately disclosed; no tower/logistics peer inference. · Company-specific estimate: Estimate inbound international guests contribute 5% of total hotel revenue (2–10%). Guest-origin revenue is not separately disclosed; no tower/logistics peer inference. |
| PK | re_intl_inbound_revenue_share | 0.05 | 0.02 | 0.1 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1617406/000161740626000006/0001617406-26-000006-index.htm · estimate; Company-specific estimate: Estimate inbound international guests contribute 5% of total hotel revenue (2–10%). Guest-origin revenue is not separately disclosed; no tower/logistics peer inference. · Company-specific estimate: Estimate inbound international guests contribute 5% of total hotel revenue (2–10%). Guest-origin revenue is not separately disclosed; no tower/logistics peer inference. |

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
| exposure.re_intl_inbound_revenue_share | -0.00032174257 | -0.0011210947 | 0.00079935211 |
| assumption.elasticity | -0.00032638371 | -0.00097915113 | 0.00065276742 |
| assumption.visa_required_share | -0.00043517828 | -0.00087035656 | 0.00043517828 |
| assumption.trip_spend_usd | -0.00089522389 | -0.00052221394 | 0.00037300996 |

Dominant configured driver: `re_intl_inbound_revenue_share` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.


## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 7 unchecked in-scope exposure values; 3 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

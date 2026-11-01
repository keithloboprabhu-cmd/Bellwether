# App-store commission cap

Policy `tmt/app_store_commission_cap` · reviewed 2026-10-31 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

A cap on the commission app-store operators may charge on US in-app and paid-app sales. It cuts Apple's and Google's high-margin store revenue; Meta and others that pay those fees are not credited with savings here.

Duration: `permanent`. Default inputs: `{"max_commission_pct": 15.0}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| price | unavailable / unavailable | {"d_price": "-max(0, assumption.current_rate - input.max_commission_pct / 100) / assumption.current_rate", "exposed_revenue_share": "exposure.us_app_store_fee_share", "offset_share": "assumption.offset_share"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/R69.htm
- https://www.sec.gov/Archives/edgar/data/1652044/000165204426000018/R44.htm

| Company | Configured status | Basis |
|---|---|---|
| AAPL | included | Binding app-store commission cap reduces platform fee revenue. |
| MSFT | outside_scope | Only the two modeled mobile app-store commission owners are covered. Customer fee savings and other software stores need a separate channel. |
| GOOGL | included | Binding app-store commission cap reduces platform fee revenue. |
| META | outside_scope | Only the two modeled mobile app-store commission owners are covered. Customer fee savings and other software stores need a separate channel. |
| NVDA | outside_scope | Only the two modeled mobile app-store commission owners are covered. Customer fee savings and other software stores need a separate channel. |
| VZ | outside_scope | Only the two modeled mobile app-store commission owners are covered. Customer fee savings and other software stores need a separate channel. |
| IBM | outside_scope | Only the two modeled mobile app-store commission owners are covered. Customer fee savings and other software stores need a separate channel. |
| ORCL | outside_scope | Only the two modeled mobile app-store commission owners are covered. Customer fee savings and other software stores need a separate channel. |
| CRM | outside_scope | Only the two modeled mobile app-store commission owners are covered. Customer fee savings and other software stores need a separate channel. |
| ADBE | outside_scope | Only the two modeled mobile app-store commission owners are covered. Customer fee savings and other software stores need a separate channel. |
| INTC | outside_scope | Only the two modeled mobile app-store commission owners are covered. Customer fee savings and other software stores need a separate channel. |
| AMD | outside_scope | Only the two modeled mobile app-store commission owners are covered. Customer fee savings and other software stores need a separate channel. |
| QCOM | outside_scope | Only the two modeled mobile app-store commission owners are covered. Customer fee savings and other software stores need a separate channel. |
| MU | outside_scope | Only the two modeled mobile app-store commission owners are covered. Customer fee savings and other software stores need a separate channel. |
| AVGO | outside_scope | Only the two modeled mobile app-store commission owners are covered. Customer fee savings and other software stores need a separate channel. |
| CSCO | outside_scope | Only the two modeled mobile app-store commission owners are covered. Customer fee savings and other software stores need a separate channel. |
| T | outside_scope | Only the two modeled mobile app-store commission owners are covered. Customer fee savings and other software stores need a separate channel. |
| CMCSA | outside_scope | Only the two modeled mobile app-store commission owners are covered. Customer fee savings and other software stores need a separate channel. |
| NFLX | outside_scope | Only the two modeled mobile app-store commission owners are covered. Customer fee savings and other software stores need a separate channel. |
| DIS | outside_scope | Only the two modeled mobile app-store commission owners are covered. Customer fee savings and other software stores need a separate channel. |
| AMAT | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| ANET | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| DELL | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| HPQ | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| INTU | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| LRCX | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| NOW | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| PANW | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| SNDK | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| SNX | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| TMUS | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| TXN | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| PLTR | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |

## B. Every in-scope exposure

Exact numeric checks are distinguished from filing links and estimates. UNVERIFIED values are retained, not silently replaced. Historical observed low/high values are not forecast confidence intervals.

| Company | Exposure | Base | Low | High | Exact-source status | Primary source / location / rationale |
|---|---|---:|---:|---:|---|---|
| AAPL | us_app_store_fee_share | 0.025 | 0.015 | 0.035 | UNVERIFIED | No source URL · estimate; Not disclosed. Sensor Tower data imply ~$160B/yr combined App Store + Google Play consumer spend (Q2 2025 $40.9B), roughly two-thirds App Store; ~25% effective commission gives ~$26B global, ~40% US => ~$10B of $416B revenue. · Not disclosed. Sensor Tower data imply ~$160B/yr combined App Store + Google Play consumer spend (Q2 2025 $40.9B), roughly two-thirds App Store; ~25% effective commission gives ~$26B global, ~40% US => ~$10B of $416B revenue. |
| GOOGL | us_app_store_fee_share | 0.008 | 0.004 | 0.013 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1652044/000165204426000018/R44.htm · estimate; Google Play sits inside 'subscriptions, platforms and devices' ($48,030M, Alphabet 2025 10-K) and isn't broken out; ~$55B global Play spend x ~20% effective fee x ~30% US => ~$3.3B of $403B. · Google Play sits inside 'subscriptions, platforms and devices' ($48,030M, Alphabet 2025 10-K) and isn't broken out; ~$55B global Play spend x ~20% effective fee x ~30% US => ~$3.3B of $403B. |

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
| exposure.us_app_store_fee_share | -0.0027168355 | -0.0068445792 | 0.0041277437 |
| assumption.current_rate | -0.0037480253 | -0.0054690574 | 0.001721032 |
| assumption.offset_share | -0.005235337 | -0.0039265027 | 0.0013088342 |

Dominant configured driver: `us_app_store_fee_share` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.


## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 2 unchecked in-scope exposure values; 2 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

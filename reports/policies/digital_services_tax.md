# Digital services tax (hypothetical US DST)

Policy `tmt/digital_services_tax` · reviewed 2026-10-31 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

A hypothetical US tax on revenue from digital advertising and app-marketplace commissions earned from US users, modelled on the UK and French DSTs. Alphabet and Meta carry almost all of it; they can pass part on to advertisers as Google did abroad.

Duration: `permanent`. Default inputs: `{"rate_pct": 3.0}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| tax_revenue | unavailable / unavailable | {"rate": "input.rate_pct / 100", "in_scope_share": "derived.in_scope_share"} |
| price | unavailable / unavailable | {"d_price": "input.rate_pct / 100 * assumption.pass_through", "exposed_revenue_share": "derived.in_scope_share"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://www.sec.gov/Archives/edgar/data/1652044/000165204426000018/R44.htm
- https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/R46.htm
- https://ppc.land/google-ads-to-pass-cost-of-digital-taxes-to-advertisers-starting-in-november/

| Company | Configured status | Basis |
|---|---|---|
| AAPL | included | Tax applies to US digital advertising and covered platform fees. |
| MSFT | included | Tax applies to US digital advertising and covered platform fees. |
| GOOGL | included | Tax applies to US digital advertising and covered platform fees. |
| META | included | Tax applies to US digital advertising and covered platform fees. |
| NVDA | outside_scope | This scenario taxes modeled US digital advertising and mobile app-store commissions. Hardware sales, telecom access and enterprise licenses are outside that defined tax base. |
| VZ | outside_scope | This scenario taxes modeled US digital advertising and mobile app-store commissions. Hardware sales, telecom access and enterprise licenses are outside that defined tax base. |
| IBM | outside_scope | This scenario taxes modeled US digital advertising and mobile app-store commissions. Hardware sales, telecom access and enterprise licenses are outside that defined tax base. |
| ORCL | outside_scope | This scenario taxes modeled US digital advertising and mobile app-store commissions. Hardware sales, telecom access and enterprise licenses are outside that defined tax base. |
| CRM | outside_scope | This scenario taxes modeled US digital advertising and mobile app-store commissions. Hardware sales, telecom access and enterprise licenses are outside that defined tax base. |
| ADBE | outside_scope | This scenario taxes modeled US digital advertising and mobile app-store commissions. Hardware sales, telecom access and enterprise licenses are outside that defined tax base. |
| INTC | outside_scope | This scenario taxes modeled US digital advertising and mobile app-store commissions. Hardware sales, telecom access and enterprise licenses are outside that defined tax base. |
| AMD | outside_scope | This scenario taxes modeled US digital advertising and mobile app-store commissions. Hardware sales, telecom access and enterprise licenses are outside that defined tax base. |
| QCOM | outside_scope | This scenario taxes modeled US digital advertising and mobile app-store commissions. Hardware sales, telecom access and enterprise licenses are outside that defined tax base. |
| MU | outside_scope | This scenario taxes modeled US digital advertising and mobile app-store commissions. Hardware sales, telecom access and enterprise licenses are outside that defined tax base. |
| AVGO | outside_scope | This scenario taxes modeled US digital advertising and mobile app-store commissions. Hardware sales, telecom access and enterprise licenses are outside that defined tax base. |
| CSCO | outside_scope | This scenario taxes modeled US digital advertising and mobile app-store commissions. Hardware sales, telecom access and enterprise licenses are outside that defined tax base. |
| T | outside_scope | This scenario taxes modeled US digital advertising and mobile app-store commissions. Hardware sales, telecom access and enterprise licenses are outside that defined tax base. |
| CMCSA | outside_scope | This scenario taxes modeled US digital advertising and mobile app-store commissions. Hardware sales, telecom access and enterprise licenses are outside that defined tax base. |
| NFLX | included | Tax applies to US digital advertising and covered platform fees. |
| DIS | included | Tax applies to US digital advertising and covered platform fees. |
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

## B. Every in-scope exposure

Exact numeric checks are distinguished from filing links and estimates. UNVERIFIED values are retained, not silently replaced. Historical observed low/high values are not forecast confidence intervals.

| Company | Exposure | Base | Low | High | Exact-source status | Primary source / location / rationale |
|---|---|---:|---:|---:|---|---|
| AAPL | us_digital_ad_revenue_share | 0.012 | 0.005 | 0.02 | UNVERIFIED | No source URL · estimate; Apple doesn't disclose advertising revenue (App Store search ads, News, TV); assumes ~$10B global, about half from US users, inside $109.2B Services. · Apple doesn't disclose advertising revenue (App Store search ads, News, TV); assumes ~$10B global, about half from US users, inside $109.2B Services. |
| AAPL | us_app_store_fee_share | 0.025 | 0.015 | 0.035 | UNVERIFIED | No source URL · estimate; Not disclosed. Sensor Tower data imply ~$160B/yr combined App Store + Google Play consumer spend (Q2 2025 $40.9B), roughly two-thirds App Store; ~25% effective commission gives ~$26B global, ~40% US => ~$10B of $416B revenue. · Not disclosed. Sensor Tower data imply ~$160B/yr combined App Store + Google Play consumer spend (Q2 2025 $40.9B), roughly two-thirds App Store; ~25% effective commission gives ~$26B global, ~40% US => ~$10B of $416B revenue. |
| MSFT | us_digital_ad_revenue_share | 0.035 | 0.025 | 0.05 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/R110.htm · estimate; Microsoft FY2026 10-K: search advertising revenue $15,176M of $331,839M; assumes ~60% from US users, plus a few $B of LinkedIn marketing solutions (not disclosed). · Microsoft FY2026 10-K: search advertising revenue $15,176M of $331,839M; assumes ~60% from US users, plus a few $B of LinkedIn marketing solutions (not disclosed). |
| MSFT | us_app_store_fee_share | 0 | 0 | 0 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm · estimate; Company-specific scope estimate: This channel covers the mobile app-store commission owners, not streaming subscriptions or enterprise software fees. This is a model boundary, not a reported zero measurement. · Company-specific scope estimate: This channel covers the mobile app-store commission owners, not streaming subscriptions or enterprise software fees. This is a model boundary, not a reported zero measurement. |
| GOOGL | us_digital_ad_revenue_share | 0.35 | 0.32 | 0.4 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1652044/000165204426000018/R44.htm · Alphabet 2025 10-K: Google advertising $294,691M of $402,836M revenue; United States $194,229M (48%) of revenue. 0.35 = 73% x 48%, assuming ads split by country like total revenue; Range covers US ads being a somewhat larger share of US revenue than of global revenue. · Range covers US ads being a somewhat larger share of US revenue than of global revenue. |
| GOOGL | us_app_store_fee_share | 0.008 | 0.004 | 0.013 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1652044/000165204426000018/R44.htm · estimate; Google Play sits inside 'subscriptions, platforms and devices' ($48,030M, Alphabet 2025 10-K) and isn't broken out; ~$55B global Play spend x ~20% effective fee x ~30% US => ~$3.3B of $403B. · Google Play sits inside 'subscriptions, platforms and devices' ($48,030M, Alphabet 2025 10-K) and isn't broken out; ~$55B global Play spend x ~20% effective fee x ~30% US => ~$3.3B of $403B. |
| META | us_digital_ad_revenue_share | 0.36 | 0.34 | 0.38 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/R46.htm · Meta 2025 10-K: advertising $196,175M of $200,966M revenue; United States $74,780M (37.2%; geography by user location). 0.36 = 97.6% x 37.2%;  · unavailable |
| META | us_app_store_fee_share | 0 | 0 | 0 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/0001628280-26-003942-index.htm · estimate; Company-specific scope estimate: This channel covers the mobile app-store commission owners, not streaming subscriptions or enterprise software fees. This is a model boundary, not a reported zero measurement. · Company-specific scope estimate: This channel covers the mobile app-store commission owners, not streaming subscriptions or enterprise software fees. This is a model boundary, not a reported zero measurement. |
| NFLX | us_digital_ad_revenue_share | 0.03 | 0.01 | 0.06 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1065280/000106528026000034/0001065280-26-000034-index.htm · estimate; Company-specific estimate: Ad-supported streaming is a minority of consolidated revenue; estimate US digital ad sales at 3% (1–6%), rather than inheriting Alphabet/Meta advertising-platform revenue shares. · Company-specific estimate: Ad-supported streaming is a minority of consolidated revenue; estimate US digital ad sales at 3% (1–6%), rather than inheriting Alphabet/Meta advertising-platform revenue shares. |
| NFLX | us_app_store_fee_share | 0 | 0 | 0 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1065280/000106528026000034/0001065280-26-000034-index.htm · estimate; Company-specific scope estimate: This channel covers the mobile app-store commission owners, not streaming subscriptions or enterprise software fees. This is a model boundary, not a reported zero measurement. · Company-specific scope estimate: This channel covers the mobile app-store commission owners, not streaming subscriptions or enterprise software fees. This is a model boundary, not a reported zero measurement. |
| DIS | us_digital_ad_revenue_share | 0.06 | 0.03 | 0.12 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1744489/000174448925000155/0001744489-25-000155-index.htm · estimate; Company-specific estimate: Estimate US digital streaming advertising at 6% of consolidated revenue (3–12%). Excludes subscription, parks, merchandise and linear-TV revenue; this is not a disclosed US digital-ad segment. · Company-specific estimate: Estimate US digital streaming advertising at 6% of consolidated revenue (3–12%). Excludes subscription, parks, merchandise and linear-TV revenue; this is not a disclosed US digital-ad segment. |
| DIS | us_app_store_fee_share | 0 | 0 | 0 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1744489/000174448925000155/0001744489-25-000155-index.htm · estimate; Company-specific scope estimate: This channel covers the mobile app-store commission owners, not streaming subscriptions or enterprise software fees. This is a model boundary, not a reported zero measurement. · Company-specific scope estimate: This channel covers the mobile app-store commission owners, not streaming subscriptions or enterprise software fees. This is a model boundary, not a reported zero measurement. |

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
| assumption.pass_through | -0.0054407764 | -0.00068009704 | 0.0047606793 |
| exposure.us_digital_ad_revenue_share | -0.0030459931 | -0.0039376129 | 0.00089161976 |
| exposure.us_app_store_fee_share | -0.003317207 | -0.0034895161 | 0.00017230907 |

Dominant configured driver: `pass_through` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.


## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 12 unchecked in-scope exposure values; 1 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

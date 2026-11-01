# Federal data-privacy mandate (opt-in consent)

Policy `tmt/data_privacy_mandate` · reviewed 2026-10-31 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

A GDPR-style federal privacy law requiring opt-in consent for targeted ads and adding compliance work per user. Ad platforms lose some targeting revenue; everyone with US user data pays compliance costs.

Duration: `permanent`. Default inputs: `{"ad_revenue_loss_pct": 5.0, "cost_per_user": 1.0}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| demand_volume | unavailable / unavailable | {"d_volume": "-input.ad_revenue_loss_pct / 100 * assumption.ad_loss_scale", "exposed_revenue_share": "exposure.us_digital_ad_revenue_share"} |
| cost | unavailable / unavailable | {"exposed_cost_share": 0.0, "shock_pct": 0.0, "dcost_musd": "input.cost_per_user * exposure.us_users_m"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://www.aeaweb.org/doi/10.1257/pol.20210309
- https://itpro.com/security/privacy/362151/meta-says-apples-ios-privacy-changes-will-cost-it-10-billion-in-2022

| Company | Configured status | Basis |
|---|---|---|
| AAPL | included | Ad-targeting loss and privacy compliance raise costs/reduce monetization. |
| MSFT | included | Ad-targeting loss and privacy compliance raise costs/reduce monetization. |
| GOOGL | included | Ad-targeting loss and privacy compliance raise costs/reduce monetization. |
| META | included | Ad-targeting loss and privacy compliance raise costs/reduce monetization. |
| NVDA | included | Ad-targeting loss and privacy compliance raise costs/reduce monetization. |
| VZ | included | Ad-targeting loss and privacy compliance raise costs/reduce monetization. |
| IBM | included | Ad-targeting loss and privacy compliance raise costs/reduce monetization. |
| ORCL | included | Ad-targeting loss and privacy compliance raise costs/reduce monetization. |
| CRM | included | Ad-targeting loss and privacy compliance raise costs/reduce monetization. |
| ADBE | included | Ad-targeting loss and privacy compliance raise costs/reduce monetization. |
| INTC | included | Ad-targeting loss and privacy compliance raise costs/reduce monetization. |
| AMD | included | Ad-targeting loss and privacy compliance raise costs/reduce monetization. |
| QCOM | included | Ad-targeting loss and privacy compliance raise costs/reduce monetization. |
| MU | included | Ad-targeting loss and privacy compliance raise costs/reduce monetization. |
| AVGO | included | Ad-targeting loss and privacy compliance raise costs/reduce monetization. |
| CSCO | included | Ad-targeting loss and privacy compliance raise costs/reduce monetization. |
| T | included | Ad-targeting loss and privacy compliance raise costs/reduce monetization. |
| CMCSA | included | Ad-targeting loss and privacy compliance raise costs/reduce monetization. |
| NFLX | included | Ad-targeting loss and privacy compliance raise costs/reduce monetization. |
| DIS | included | Ad-targeting loss and privacy compliance raise costs/reduce monetization. |
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
| AAPL | us_digital_ad_revenue_share | 0.012 | 0.005 | 0.02 | UNVERIFIED | No source URL · estimate; Apple doesn't disclose advertising revenue (App Store search ads, News, TV); assumes ~$10B global, about half from US users, inside $109.2B Services. · Apple doesn't disclose advertising revenue (App Store search ads, News, TV); assumes ~$10B global, about half from US users, inside $109.2B Services. |
| AAPL | us_users_m | 150 | 120 | 180 | UNVERIFIED | No source URL · estimate; Apple doesn't disclose US users; iPhone share of US smartphones is roughly half of ~300M adult and teen users. · Apple doesn't disclose US users; iPhone share of US smartphones is roughly half of ~300M adult and teen users. |
| MSFT | us_digital_ad_revenue_share | 0.035 | 0.025 | 0.05 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/R110.htm · estimate; Microsoft FY2026 10-K: search advertising revenue $15,176M of $331,839M; assumes ~60% from US users, plus a few $B of LinkedIn marketing solutions (not disclosed). · Microsoft FY2026 10-K: search advertising revenue $15,176M of $331,839M; assumes ~60% from US users, plus a few $B of LinkedIn marketing solutions (not disclosed). |
| MSFT | us_users_m | 200 | 150 | 250 | UNVERIFIED | No source URL · estimate; Windows, Outlook, LinkedIn and Xbox accounts reach most US adults; unique US users not disclosed. · Windows, Outlook, LinkedIn and Xbox accounts reach most US adults; unique US users not disclosed. |
| GOOGL | us_digital_ad_revenue_share | 0.35 | 0.32 | 0.4 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1652044/000165204426000018/R44.htm · Alphabet 2025 10-K: Google advertising $294,691M of $402,836M revenue; United States $194,229M (48%) of revenue. 0.35 = 73% x 48%, assuming ads split by country like total revenue; Range covers US ads being a somewhat larger share of US revenue than of global revenue. · Range covers US ads being a somewhat larger share of US revenue than of global revenue. |
| GOOGL | us_users_m | 300 | 250 | 330 | UNVERIFIED | No source URL · estimate; Search, YouTube, Gmail and Android reach nearly every US internet user. · Search, YouTube, Gmail and Android reach nearly every US internet user. |
| META | us_digital_ad_revenue_share | 0.36 | 0.34 | 0.38 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/R46.htm · Meta 2025 10-K: advertising $196,175M of $200,966M revenue; United States $74,780M (37.2%; geography by user location). 0.36 = 97.6% x 37.2%;  · unavailable |
| META | us_users_m | 250 | 220 | 280 | UNVERIFIED | No source URL · estimate; Facebook, Instagram and WhatsApp reach most US adults and teens; US-only users not disclosed (US & Canada reported together). · Facebook, Instagram and WhatsApp reach most US adults and teens; US-only users not disclosed (US & Canada reported together). |
| NVDA | us_digital_ad_revenue_share | 0 | 0 | 0 | UNVERIFIED | No source URL · estimate; No advertising business. · No advertising business. |
| NVDA | us_users_m | 10 | 5 | 20 | UNVERIFIED | No source URL · estimate; Consumer data exposure limited to GeForce NOW / NVIDIA app accounts. · Consumer data exposure limited to GeForce NOW / NVIDIA app accounts. |
| VZ | us_digital_ad_revenue_share | 0 | 0 | 0 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/732712/000073271226000007/0000732712-26-000007-index.htm · estimate; Company-specific scope estimate: Direct digital advertising and ad-supported media sales; enterprise software license and consulting revenue is not media advertising revenue. This is a model boundary, not a reported zero measurement. · Company-specific scope estimate: Direct digital advertising and ad-supported media sales; enterprise software license and consulting revenue is not media advertising revenue. This is a model boundary, not a reported zero measurement. |
| VZ | us_users_m | 120 | 100 | 146 | UNVERIFIED | No source URL · estimate; Verizon serves roughly 146M wireless connections (many are tablets, IoT or second lines); unique US people are fewer. · Verizon serves roughly 146M wireless connections (many are tablets, IoT or second lines); unique US people are fewer. |
| IBM | us_digital_ad_revenue_share | 0 | 0 | 0 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/51143/000005114326000010/0000051143-26-000010-index.htm · estimate; Company-specific scope estimate: Direct digital advertising and ad-supported media sales; enterprise software license and consulting revenue is not media advertising revenue. This is a model boundary, not a reported zero measurement. · Company-specific scope estimate: Direct digital advertising and ad-supported media sales; enterprise software license and consulting revenue is not media advertising revenue. This is a model boundary, not a reported zero measurement. |
| IBM | us_users_m | 40.703474 | 30.527605 | 50.879342 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Enterprise software and services; median base and outer low/high from MSFT in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Enterprise software and services; median base and outer low/high from MSFT in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| ORCL | us_digital_ad_revenue_share | 0 | 0 | 0 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm · estimate; Company-specific scope estimate: Direct digital advertising and ad-supported media sales; enterprise software license and consulting revenue is not media advertising revenue. This is a model boundary, not a reported zero measurement. · Company-specific scope estimate: Direct digital advertising and ad-supported media sales; enterprise software license and consulting revenue is not media advertising revenue. This is a model boundary, not a reported zero measurement. |
| ORCL | us_users_m | 40.596193 | 30.447145 | 50.745241 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Enterprise software and services; median base and outer low/high from MSFT in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Enterprise software and services; median base and outer low/high from MSFT in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| CRM | us_digital_ad_revenue_share | 0 | 0 | 0 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1108524/000110852426000060/0001108524-26-000060-index.htm · estimate; Company-specific scope estimate: Direct digital advertising and ad-supported media sales; enterprise software license and consulting revenue is not media advertising revenue. This is a model boundary, not a reported zero measurement. · Company-specific scope estimate: Direct digital advertising and ad-supported media sales; enterprise software license and consulting revenue is not media advertising revenue. This is a model boundary, not a reported zero measurement. |
| CRM | us_users_m | 25.027197 | 18.770398 | 31.283996 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Enterprise software and services; median base and outer low/high from MSFT in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Enterprise software and services; median base and outer low/high from MSFT in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| ADBE | us_digital_ad_revenue_share | 0 | 0 | 0 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/796343/000079634326000003/0000796343-26-000003-index.htm · estimate; Company-specific scope estimate: Direct digital advertising and ad-supported media sales; enterprise software license and consulting revenue is not media advertising revenue. This is a model boundary, not a reported zero measurement. · Company-specific scope estimate: Direct digital advertising and ad-supported media sales; enterprise software license and consulting revenue is not media advertising revenue. This is a model boundary, not a reported zero measurement. |
| ADBE | us_users_m | 14.325622 | 10.744216 | 17.907027 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Enterprise software and services; median base and outer low/high from MSFT in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Enterprise software and services; median base and outer low/high from MSFT in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| INTC | us_digital_ad_revenue_share | 0 | 0 | 0 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Semiconductors; median base and outer low/high from NVDA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Semiconductors; median base and outer low/high from NVDA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| INTC | us_users_m | 2.4476007 | 1.2238004 | 4.8952014 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Semiconductors; median base and outer low/high from NVDA in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Semiconductors; median base and outer low/high from NVDA in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| AMD | us_digital_ad_revenue_share | 0 | 0 | 0 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Semiconductors; median base and outer low/high from NVDA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Semiconductors; median base and outer low/high from NVDA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| AMD | us_users_m | 1.6041178 | 0.80205892 | 3.2082357 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Semiconductors; median base and outer low/high from NVDA in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Semiconductors; median base and outer low/high from NVDA in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| QCOM | us_digital_ad_revenue_share | 0 | 0 | 0 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Semiconductors; median base and outer low/high from NVDA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Semiconductors; median base and outer low/high from NVDA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| QCOM | us_users_m | 2.0507738 | 1.0253869 | 4.1015477 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Semiconductors; median base and outer low/high from NVDA in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Semiconductors; median base and outer low/high from NVDA in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| MU | us_digital_ad_revenue_share | 0 | 0 | 0 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Semiconductors; median base and outer low/high from NVDA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Semiconductors; median base and outer low/high from NVDA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| MU | us_users_m | 6.1678815 | 3.0839408 | 12.335763 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Semiconductors; median base and outer low/high from NVDA in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Semiconductors; median base and outer low/high from NVDA in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| AVGO | us_digital_ad_revenue_share | 0 | 0 | 0 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Semiconductors; median base and outer low/high from NVDA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Semiconductors; median base and outer low/high from NVDA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| AVGO | us_users_m | 2.9585807 | 1.4792904 | 5.9171614 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Semiconductors; median base and outer low/high from NVDA in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Semiconductors; median base and outer low/high from NVDA in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| CSCO | us_digital_ad_revenue_share | 0 | 0 | 0 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/858877/000085887726000132/0000858877-26-000132-index.htm · estimate; Company-specific scope estimate: Direct digital advertising and ad-supported media sales; enterprise software license and consulting revenue is not media advertising revenue. This is a model boundary, not a reported zero measurement. · Company-specific scope estimate: Direct digital advertising and ad-supported media sales; enterprise software license and consulting revenue is not media advertising revenue. This is a model boundary, not a reported zero measurement. |
| CSCO | us_users_m | 54.989109 | 45.824258 | 66.903416 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Telecom and networking; median base and outer low/high from VZ in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Telecom and networking; median base and outer low/high from VZ in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| T | us_digital_ad_revenue_share | 0 | 0 | 0 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/732717/000073271726000120/0000732717-26-000120-index.htm · estimate; Company-specific scope estimate: Direct digital advertising and ad-supported media sales; enterprise software license and consulting revenue is not media advertising revenue. This is a model boundary, not a reported zero measurement. · Company-specific scope estimate: Direct digital advertising and ad-supported media sales; enterprise software license and consulting revenue is not media advertising revenue. This is a model boundary, not a reported zero measurement. |
| T | us_users_m | 109.10812 | 90.923432 | 132.74821 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Telecom and networking; median base and outer low/high from VZ in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Telecom and networking; median base and outer low/high from VZ in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| CMCSA | us_digital_ad_revenue_share | 0 | 0 | 0 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1166691/000162828026004994/0001628280-26-004994-index.htm · estimate; Company-specific scope estimate: Direct digital advertising and ad-supported media sales; enterprise software license and consulting revenue is not media advertising revenue. This is a model boundary, not a reported zero measurement. · Company-specific scope estimate: Direct digital advertising and ad-supported media sales; enterprise software license and consulting revenue is not media advertising revenue. This is a model boundary, not a reported zero measurement. |
| CMCSA | us_users_m | 107.42263 | 89.518854 | 130.69753 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Telecom and networking; median base and outer low/high from VZ in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Telecom and networking; median base and outer low/high from VZ in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| NFLX | us_digital_ad_revenue_share | 0.03 | 0.01 | 0.06 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1065280/000106528026000034/0001065280-26-000034-index.htm · estimate; Company-specific estimate: Ad-supported streaming is a minority of consolidated revenue; estimate US digital ad sales at 3% (1–6%), rather than inheriting Alphabet/Meta advertising-platform revenue shares. · Company-specific estimate: Ad-supported streaming is a minority of consolidated revenue; estimate US digital ad sales at 3% (1–6%), rather than inheriting Alphabet/Meta advertising-platform revenue shares. |
| NFLX | us_users_m | 44.928011 | 28.04059 | 62.952191 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Media and entertainment; median base and outer low/high from GOOGL/META in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Media and entertainment; median base and outer low/high from GOOGL/META in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| DIS | us_digital_ad_revenue_share | 0.06 | 0.03 | 0.12 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1744489/000174448925000155/0001744489-25-000155-index.htm · estimate; Company-specific estimate: Estimate US digital streaming advertising at 6% of consolidated revenue (3–12%). Excludes subscription, parks, merchandise and linear-TV revenue; this is not a disclosed US digital-ad segment. · Company-specific estimate: Estimate US digital streaming advertising at 6% of consolidated revenue (3–12%). Excludes subscription, parks, merchandise and linear-TV revenue; this is not a disclosed US digital-ad segment. |
| DIS | us_users_m | 93.89204 | 58.60015 | 131.55957 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Media and entertainment; median base and outer low/high from GOOGL/META in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Media and entertainment; median base and outer low/high from GOOGL/META in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |

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
| assumption.ad_loss_scale | -0.0048990933 | -0.0097681694 | 0.004869076 |
| exposure.us_digital_ad_revenue_share | -0.0064256662 | -0.0078136466 | 0.0013879803 |
| exposure.us_users_m | -0.0066962307 | -0.007289282 | 0.00059305136 |

Dominant configured driver: `ad_loss_scale` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.


## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 40 unchecked in-scope exposure values; 1 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

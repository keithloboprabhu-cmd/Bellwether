# Tighter advanced-chip export controls on China

Policy `tmt/chip_export_controls` · evidence checkpoint 2026-11-01 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

The US blocks more chip sales to China and China retaliates against US tech firms. NVIDIA loses restricted chip sales (partly resold elsewhere); Apple is most exposed to retaliation through its Greater China sales.

Duration: `permanent`. Default inputs: `{"restricted_loss_pct": 75.0, "retaliation_pct": 5.0}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| demand_volume | unavailable / unavailable | {"d_volume": "-input.restricted_loss_pct / 100 * (1 - assumption.resale_share)", "exposed_revenue_share": "exposure.restricted_chip_china_share"} |
| demand_volume | unavailable / unavailable | {"d_volume": "-input.retaliation_pct / 100", "exposed_revenue_share": "max(0, exposure.greater_china_revenue_share - exposure.restricted_chip_china_share)"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/R84.htm
- https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/R68.htm

| Company | Configured status | Basis |
|---|---|---|
| AAPL | included | Restricted chip exports reduce merchant chip sales; retaliation is a separate channel. |
| MSFT | included | Restricted chip exports reduce merchant chip sales; retaliation is a separate channel. |
| GOOGL | included | Restricted chip exports reduce merchant chip sales; retaliation is a separate channel. |
| META | included | Restricted chip exports reduce merchant chip sales; retaliation is a separate channel. |
| NVDA | included | Restricted chip exports reduce merchant chip sales; retaliation is a separate channel. |
| VZ | outside_scope | No quantified restricted-chip exports or China retaliation exposure in this channel. Equipment/software supplier effects need separately supported exposure. |
| IBM | included | Restricted chip exports reduce merchant chip sales; retaliation is a separate channel. |
| ORCL | included | Restricted chip exports reduce merchant chip sales; retaliation is a separate channel. |
| CRM | included | Restricted chip exports reduce merchant chip sales; retaliation is a separate channel. |
| ADBE | included | Restricted chip exports reduce merchant chip sales; retaliation is a separate channel. |
| INTC | included | Restricted chip exports reduce merchant chip sales; retaliation is a separate channel. |
| AMD | included | Restricted chip exports reduce merchant chip sales; retaliation is a separate channel. |
| QCOM | included | Restricted chip exports reduce merchant chip sales; retaliation is a separate channel. |
| MU | included | Restricted chip exports reduce merchant chip sales; retaliation is a separate channel. |
| AVGO | included | Restricted chip exports reduce merchant chip sales; retaliation is a separate channel. |
| CSCO | included | Restricted chip exports reduce merchant chip sales; retaliation is a separate channel. |
| T | outside_scope | No quantified restricted-chip exports or China retaliation exposure in this channel. Equipment/software supplier effects need separately supported exposure. |
| CMCSA | outside_scope | No quantified restricted-chip exports or China retaliation exposure in this channel. Equipment/software supplier effects need separately supported exposure. |
| NFLX | included | Restricted chip exports reduce merchant chip sales; retaliation is a separate channel. |
| DIS | included | Restricted chip exports reduce merchant chip sales; retaliation is a separate channel. |
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
| AAPL | restricted_chip_china_share | 0 | 0 | 0 | UNVERIFIED | No source URL · estimate; Apple's China sales are consumer devices, which advanced-computing export controls do not restrict. · Apple's China sales are consumer devices, which advanced-computing export controls do not restrict. |
| AAPL | greater_china_revenue_share | 0.155 | 0.12 | 0.155 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/R68.htm · Apple FY2025 10-K: Greater China net sales $64,377M of $416,161M (15.5%; includes Hong Kong and Taiwan); Low end strips Taiwan, which Chinese retaliation would not reach. · Low end strips Taiwan, which Chinese retaliation would not reach. |
| MSFT | restricted_chip_china_share | 0 | 0 | 0 | UNVERIFIED | No source URL · estimate; Microsoft doesn't sell chips into China. · Microsoft doesn't sell chips into China. |
| MSFT | greater_china_revenue_share | 0.015 | 0.01 | 0.025 | UNVERIFIED | No source URL · estimate; Microsoft doesn't break out China (FY2026 10-K reports only U.S. $170.8B vs other countries $161.0B); piracy and local-cloud rules keep China sales to low single digits. · Microsoft doesn't break out China (FY2026 10-K reports only U.S. $170.8B vs other countries $161.0B); piracy and local-cloud rules keep China sales to low single digits. |
| GOOGL | restricted_chip_china_share | 0 | 0 | 0 | UNVERIFIED | No source URL · estimate; Alphabet doesn't sell chips (TPUs are used in-house or rented through Cloud, not shipped to China). · Alphabet doesn't sell chips (TPUs are used in-house or rented through Cloud, not shipped to China). |
| GOOGL | greater_china_revenue_share | 0.01 | 0.005 | 0.03 | UNVERIFIED | No source URL · estimate; Google services are blocked in China; exposure is China-based advertisers (exporters, apps) buying ads aimed at users abroad, which only escalation would cut. · Google services are blocked in China; exposure is China-based advertisers (exporters, apps) buying ads aimed at users abroad, which only escalation would cut. |
| META | restricted_chip_china_share | 0 | 0 | 0 | UNVERIFIED | No source URL · estimate; Meta doesn't sell chips. · Meta doesn't sell chips. |
| META | greater_china_revenue_share | 0.03 | 0 | 0.11 | UNVERIFIED | https://adnews.com.au/news/meta-s-billions-of-ad-dollars-from-china-at-risk-from-trade-war · estimate; Meta has no users in China, but China-based advertisers were reported at ~11% of 2024 revenue ($18.35B); chip controls only reach them if China retaliates against US platforms, so base takes a small slice. · Meta has no users in China, but China-based advertisers were reported at ~11% of 2024 revenue ($18.35B); chip controls only reach them if China retaliates against US platforms, so base takes a small slice. |
| NVDA | restricted_chip_china_share | 0.06 | 0.03 | 0.091 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/R84.htm · estimate; NVDA FY2026 10-K: China (incl. Hong Kong) revenue $19,677M of $215,938M (9.1%), already after the H20 license requirement ($4.5B charge) shut it out of China data-center compute. Base assumes about two-thirds of what's left (gaming GPUs, licensed parts) could fall under tighter controls; high is all of it. · NVDA FY2026 10-K: China (incl. Hong Kong) revenue $19,677M of $215,938M (9.1%), already after the H20 license requirement ($4.5B charge) shut it out of China data-center compute. Base assumes about two-thirds of what's left (gaming GPUs, licensed parts) could fall under tighter controls; high is all of it. |
| NVDA | greater_china_revenue_share | 0.091 | 0.06 | 0.12 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/R84.htm · NVIDIA FY2026 10-K: China (including Hong Kong) revenue $19,677M of $215,938M total (9.1%), by direct-customer headquarters; Range reflects that end-customer location can differ from the headquarters basis NVIDIA reports. · Range reflects that end-customer location can differ from the headquarters basis NVIDIA reports. |
| IBM | restricted_chip_china_share | 0 | 0 | 0 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Enterprise software and services; median base and outer low/high from MSFT in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Enterprise software and services; median base and outer low/high from MSFT in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| IBM | greater_china_revenue_share | 0.015 | 0.01 | 0.025 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Enterprise software and services; median base and outer low/high from MSFT in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Enterprise software and services; median base and outer low/high from MSFT in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| ORCL | restricted_chip_china_share | 0 | 0 | 0 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Enterprise software and services; median base and outer low/high from MSFT in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Enterprise software and services; median base and outer low/high from MSFT in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| ORCL | greater_china_revenue_share | 0.015 | 0.01 | 0.025 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Enterprise software and services; median base and outer low/high from MSFT in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Enterprise software and services; median base and outer low/high from MSFT in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| CRM | restricted_chip_china_share | 0 | 0 | 0 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Enterprise software and services; median base and outer low/high from MSFT in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Enterprise software and services; median base and outer low/high from MSFT in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| CRM | greater_china_revenue_share | 0.015 | 0.01 | 0.025 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Enterprise software and services; median base and outer low/high from MSFT in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Enterprise software and services; median base and outer low/high from MSFT in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| ADBE | restricted_chip_china_share | 0 | 0 | 0 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Enterprise software and services; median base and outer low/high from MSFT in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Enterprise software and services; median base and outer low/high from MSFT in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| ADBE | greater_china_revenue_share | 0.015 | 0.01 | 0.025 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Enterprise software and services; median base and outer low/high from MSFT in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Enterprise software and services; median base and outer low/high from MSFT in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| INTC | restricted_chip_china_share | 0.06 | 0.03 | 0.091 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Semiconductors; median base and outer low/high from NVDA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Semiconductors; median base and outer low/high from NVDA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| INTC | greater_china_revenue_share | 0.091 | 0.06 | 0.12 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Semiconductors; median base and outer low/high from NVDA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Semiconductors; median base and outer low/high from NVDA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| AMD | restricted_chip_china_share | 0.06 | 0.03 | 0.091 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Semiconductors; median base and outer low/high from NVDA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Semiconductors; median base and outer low/high from NVDA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| AMD | greater_china_revenue_share | 0.091 | 0.06 | 0.12 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Semiconductors; median base and outer low/high from NVDA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Semiconductors; median base and outer low/high from NVDA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| QCOM | restricted_chip_china_share | 0.06 | 0.03 | 0.091 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Semiconductors; median base and outer low/high from NVDA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Semiconductors; median base and outer low/high from NVDA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| QCOM | greater_china_revenue_share | 0.091 | 0.06 | 0.12 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Semiconductors; median base and outer low/high from NVDA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Semiconductors; median base and outer low/high from NVDA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| MU | restricted_chip_china_share | 0.06 | 0.03 | 0.091 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Semiconductors; median base and outer low/high from NVDA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Semiconductors; median base and outer low/high from NVDA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| MU | greater_china_revenue_share | 0.091 | 0.06 | 0.12 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Semiconductors; median base and outer low/high from NVDA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Semiconductors; median base and outer low/high from NVDA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| AVGO | restricted_chip_china_share | 0.06 | 0.03 | 0.091 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Semiconductors; median base and outer low/high from NVDA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Semiconductors; median base and outer low/high from NVDA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| AVGO | greater_china_revenue_share | 0.091 | 0.06 | 0.12 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Semiconductors; median base and outer low/high from NVDA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Semiconductors; median base and outer low/high from NVDA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| CSCO | restricted_chip_china_share | 0 | 0 | 0 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Telecom and networking; median base and outer low/high from VZ in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Telecom and networking; median base and outer low/high from VZ in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| CSCO | greater_china_revenue_share | 0.02 | 0 | 0.05 | UNVERIFIED | https://www.cisco.com/c/dam/en_us/about/annual-report/2025-cisco-full-annual-report.pdf · estimate; Company-specific scenario estimate: Cisco reports APJC at about 14% of FY2025 revenue. Estimate Greater China at 2% of consolidated revenue (0–5%), a subset of APJC, rather than inheriting Verizon's zero China customer base. This is not a reported China split and does not imply restricted AI-chip exports. · Company-specific scenario estimate: Cisco reports APJC at about 14% of FY2025 revenue. Estimate Greater China at 2% of consolidated revenue (0–5%), a subset of APJC, rather than inheriting Verizon's zero China customer base. This is not a reported China split and does not imply restricted AI-chip exports. |
| NFLX | restricted_chip_china_share | 0 | 0 | 0 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Media and entertainment; median base and outer low/high from GOOGL/META in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Media and entertainment; median base and outer low/high from GOOGL/META in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| NFLX | greater_china_revenue_share | 0.02 | 0 | 0.11 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Media and entertainment; median base and outer low/high from GOOGL/META in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Media and entertainment; median base and outer low/high from GOOGL/META in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| DIS | restricted_chip_china_share | 0 | 0 | 0 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Media and entertainment; median base and outer low/high from GOOGL/META in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Media and entertainment; median base and outer low/high from GOOGL/META in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| DIS | greater_china_revenue_share | 0.02 | 0 | 0.11 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Media and entertainment; median base and outer low/high from GOOGL/META in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Media and entertainment; median base and outer low/high from GOOGL/META in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |

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
| exposure.restricted_chip_china_share | -0.0088468728 | -0.019246653 | 0.01039978 |
| assumption.resale_share | -0.018806973 | -0.0091160647 | 0.0096909081 |
| exposure.greater_china_revenue_share | -0.012655481 | -0.015661061 | 0.0030055802 |

Dominant configured driver: `restricted_chip_china_share` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.


## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 34 unchecked in-scope exposure values; 1 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

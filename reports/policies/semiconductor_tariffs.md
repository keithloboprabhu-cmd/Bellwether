# Tariffs on imported semiconductors and electronics

Policy `tmt/semiconductor_tariffs` · reviewed 2026-10-31 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

A tariff on imported chips and the devices and servers that contain them raises the cost of imported hardware. Apple, NVIDIA and Verizon (handsets) carry most of it; for the cloud and ad platforms it mainly arrives slowly through server depreciation.

Duration: `permanent`. Default inputs: `{"tariff_pct": 25.0}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| cost | unavailable / unavailable | {"exposed_cost_share": "exposure.us_import_share_of_cogs", "shock_pct": "input.tariff_pct / 100", "pass_through": "assumption.pass_through", "elasticity": "assumption.elasticity"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://www.aeaweb.org/doi/10.1257/jep.33.4.187
- https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/R69.htm
- https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/R84.htm

| Company | Configured status | Basis |
|---|---|---|
| AAPL | included | Tariffs raise imported semiconductor/hardware cost. |
| MSFT | included | Tariffs raise imported semiconductor/hardware cost. |
| GOOGL | included | Tariffs raise imported semiconductor/hardware cost. |
| META | included | Tariffs raise imported semiconductor/hardware cost. |
| NVDA | included | Tariffs raise imported semiconductor/hardware cost. |
| VZ | included | Tariffs raise imported semiconductor/hardware cost. |
| IBM | included | Tariffs raise imported semiconductor/hardware cost. |
| ORCL | included | Tariffs raise imported semiconductor/hardware cost. |
| CRM | included | Tariffs raise imported semiconductor/hardware cost. |
| ADBE | included | Tariffs raise imported semiconductor/hardware cost. |
| INTC | included | Tariffs raise imported semiconductor/hardware cost. |
| AMD | included | Tariffs raise imported semiconductor/hardware cost. |
| QCOM | included | Tariffs raise imported semiconductor/hardware cost. |
| MU | included | Tariffs raise imported semiconductor/hardware cost. |
| AVGO | included | Tariffs raise imported semiconductor/hardware cost. |
| CSCO | included | Tariffs raise imported semiconductor/hardware cost. |
| T | included | Tariffs raise imported semiconductor/hardware cost. |
| CMCSA | included | Tariffs raise imported semiconductor/hardware cost. |
| NFLX | included | Tariffs raise imported semiconductor/hardware cost. |
| DIS | included | Tariffs raise imported semiconductor/hardware cost. |
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
| AAPL | us_import_share_of_cogs | 0.28 | 0.15 | 0.33 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/R69.htm · estimate; Apple FY2025 10-K: products $307.0B of $416.2B net sales and U.S. net sales $151.8B (36%); products are ~88% of $221.0B cost of sales and almost all are assembled abroad, so US-bound imported hardware is ~0.32 of COGS. Base trims for US-made Macs and exemptions tied to US investment pledges; low assumes a broad exemption. · Apple FY2025 10-K: products $307.0B of $416.2B net sales and U.S. net sales $151.8B (36%); products are ~88% of $221.0B cost of sales and almost all are assembled abroad, so US-bound imported hardware is ~0.32 of COGS. Base trims for US-made Macs and exemptions tied to US investment pledges; low assumes a broad exemption. |
| MSFT | us_import_share_of_cogs | 0.1 | 0.04 | 0.22 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/R110.htm · estimate; Xbox and Surface hardware (inside $21.8B Xbox and $17.1B Windows & Devices, FY2026 10-K) are imported; cost of revenue also carries depreciation of Azure servers, so a chip tariff on new servers phases in over their ~6-year lives. High case is a fully phased-in tariff on imported servers. · Xbox and Surface hardware (inside $21.8B Xbox and $17.1B Windows & Devices, FY2026 10-K) are imported; cost of revenue also carries depreciation of Azure servers, so a chip tariff on new servers phases in over their ~6-year lives. High case is a fully phased-in tariff on imported servers. |
| GOOGL | us_import_share_of_cogs | 0.08 | 0.03 | 0.18 | UNVERIFIED | No source URL · estimate; Pixel/Nest/Fitbit devices are imported; most cost of revenue is TAC, content and data-center costs, and server depreciation only reflects a server tariff gradually. High case is a fully phased-in tariff on imported servers. · Pixel/Nest/Fitbit devices are imported; most cost of revenue is TAC, content and data-center costs, and server depreciation only reflects a server tariff gradually. High case is a fully phased-in tariff on imported servers. |
| META | us_import_share_of_cogs | 0.08 | 0.03 | 0.25 | UNVERIFIED | No source URL · estimate; Cost of revenue ($36.2B) is mostly data-center and server depreciation plus Quest hardware; imported servers reach depreciation slowly. High case is a fully phased-in tariff on imported servers. · Cost of revenue ($36.2B) is mostly data-center and server depreciation plus Quest hardware; imported servers reach depreciation slowly. High case is a fully phased-in tariff on imported servers. |
| NVDA | us_import_share_of_cogs | 0.45 | 0.25 | 0.6 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/R84.htm · estimate; Customers headquartered in the US were $149.6B of $215.9B FY2026 revenue (NVDA 10-K), but some of that hardware is deployed abroad. GPUs are fabbed by TSMC in Taiwan and systems assembled in Taiwan/Mexico; Arizona and Texas production is still ramping. · Customers headquartered in the US were $149.6B of $215.9B FY2026 revenue (NVDA 10-K), but some of that hardware is deployed abroad. GPUs are fabbed by TSMC in Taiwan and systems assembled in Taiwan/Mexico; Arizona and Texas production is still ramping. |
| VZ | us_import_share_of_cogs | 0.25 | 0.18 | 0.386 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/732712/000073271226000007/R3.htm · estimate; Verizon 2025 10-K: cost of wireless equipment $28,976M of $75,114M cost of revenue (incl. D&A), i.e. 0.386, nearly all imported phones. Customs value is the OEM's import price, below Verizon's purchase price, so base takes ~two-thirds; high assumes OEMs pass the full duty on their wholesale price. · Verizon 2025 10-K: cost of wireless equipment $28,976M of $75,114M cost of revenue (incl. D&A), i.e. 0.386, nearly all imported phones. Customs value is the OEM's import price, below Verizon's purchase price, so base takes ~two-thirds; high assumes OEMs pass the full duty on their wholesale price. |
| IBM | us_import_share_of_cogs | 0.1 | 0.04 | 0.22 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Enterprise software and services; median base and outer low/high from MSFT in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Enterprise software and services; median base and outer low/high from MSFT in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| ORCL | us_import_share_of_cogs | 0.1 | 0.04 | 0.22 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Enterprise software and services; median base and outer low/high from MSFT in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Enterprise software and services; median base and outer low/high from MSFT in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| CRM | us_import_share_of_cogs | 0.01 | 0 | 0.03 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1108524/000110852426000060/0001108524-26-000060-index.htm · estimate; Company-specific estimate: Enterprise software has limited direct imported hardware cost. Use 1% of COGS (0–3%) as a phase-in proxy, rather than a device/cloud peer's 10%; indirect supplier pricing is not separately modeled. · Company-specific estimate: Enterprise software has limited direct imported hardware cost. Use 1% of COGS (0–3%) as a phase-in proxy, rather than a device/cloud peer's 10%; indirect supplier pricing is not separately modeled. |
| ADBE | us_import_share_of_cogs | 0.01 | 0 | 0.03 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/796343/000079634326000003/0000796343-26-000003-index.htm · estimate; Company-specific estimate: Enterprise software has limited direct imported hardware cost. Use 1% of COGS (0–3%) as a phase-in proxy, rather than a device/cloud peer's 10%; indirect supplier pricing is not separately modeled. · Company-specific estimate: Enterprise software has limited direct imported hardware cost. Use 1% of COGS (0–3%) as a phase-in proxy, rather than a device/cloud peer's 10%; indirect supplier pricing is not separately modeled. |
| INTC | us_import_share_of_cogs | 0.45 | 0.25 | 0.6 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Semiconductors; median base and outer low/high from NVDA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Semiconductors; median base and outer low/high from NVDA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| AMD | us_import_share_of_cogs | 0.45 | 0.25 | 0.6 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Semiconductors; median base and outer low/high from NVDA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Semiconductors; median base and outer low/high from NVDA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| QCOM | us_import_share_of_cogs | 0.45 | 0.25 | 0.6 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Semiconductors; median base and outer low/high from NVDA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Semiconductors; median base and outer low/high from NVDA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| MU | us_import_share_of_cogs | 0.45 | 0.25 | 0.6 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Semiconductors; median base and outer low/high from NVDA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Semiconductors; median base and outer low/high from NVDA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| AVGO | us_import_share_of_cogs | 0.45 | 0.25 | 0.6 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Semiconductors; median base and outer low/high from NVDA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Semiconductors; median base and outer low/high from NVDA in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| CSCO | us_import_share_of_cogs | 0.25 | 0.18 | 0.386 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Telecom and networking; median base and outer low/high from VZ in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Telecom and networking; median base and outer low/high from VZ in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| T | us_import_share_of_cogs | 0.25 | 0.18 | 0.386 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Telecom and networking; median base and outer low/high from VZ in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Telecom and networking; median base and outer low/high from VZ in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| CMCSA | us_import_share_of_cogs | 0.25 | 0.18 | 0.386 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Telecom and networking; median base and outer low/high from VZ in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Telecom and networking; median base and outer low/high from VZ in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| NFLX | us_import_share_of_cogs | 0.08 | 0.03 | 0.25 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Media and entertainment; median base and outer low/high from GOOGL/META in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Media and entertainment; median base and outer low/high from GOOGL/META in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| DIS | us_import_share_of_cogs | 0.08 | 0.03 | 0.25 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Media and entertainment; median base and outer low/high from GOOGL/META in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Media and entertainment; median base and outer low/high from GOOGL/META in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |

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
| exposure.us_import_share_of_cogs | -0.023206016 | -0.062300097 | 0.039094081 |
| assumption.pass_through | -0.05003005 | -0.030779825 | 0.019250225 |
| assumption.elasticity | -0.033906649 | -0.048400719 | 0.01449407 |

Dominant configured driver: `us_import_share_of_cogs` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.


## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 20 unchecked in-scope exposure values; 2 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

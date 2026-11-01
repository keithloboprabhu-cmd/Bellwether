# US corporate tax rate increase — book-income proxy

Policy `tmt/us_corporate_tax_tmt` · reviewed 2026-10-31 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Verified submitted text: S.Amdt.2428 (119th Congress), section 71117 proposed 21% → 28% for taxable years after 2025. This amendment was submitted, not enacted. The model covers only its rate provision using positive US book income as a taxable-income proxy. Credits, tax losses, AMT/GILTI and deferred-tax remeasurement are omitted. The direct after-tax channel does not remeasure the separately displayed effective tax-rate field.

Rate-only scenario based on S.Amdt.2428 (119th Congress), a submitted 21% to 28% proposal, not enacted law. Uses positive reported US book pretax income as a labeled taxable-income proxy; excludes unverified jurisdictions, loss carryforwards and deferred-tax remeasurement.

Duration: `permanent`. Default inputs: `{"d_rate_pts": 7.0}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| tax_credit | unavailable / unavailable | {"credit_rate": "-input.d_rate_pts / 100", "base_musd": "exposure.audit_us_pretax_income_musd"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://www.congress.gov/amendment/119th-congress/senate-amendment/2428/text
- https://uscode.house.gov/us/usc/119-121/t26/s11/

| Company | Configured status | Basis |
|---|---|---|
| AAPL | unquantified | Positive US taxable-income proxy not verified; jurisdiction, pass-through status or loss-tax treatment requires review. |
| MSFT | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| GOOGL | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| META | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| NVDA | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| VZ | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| IBM | unquantified | Positive US taxable-income proxy not verified; jurisdiction, pass-through status or loss-tax treatment requires review. |
| ORCL | unquantified | Positive US taxable-income proxy not verified; jurisdiction, pass-through status or loss-tax treatment requires review. |
| CRM | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| ADBE | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| INTC | unquantified | Positive US taxable-income proxy not verified; jurisdiction, pass-through status or loss-tax treatment requires review. |
| AMD | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| QCOM | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| MU | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| AVGO | unquantified | Positive US taxable-income proxy not verified; jurisdiction, pass-through status or loss-tax treatment requires review. |
| CSCO | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| T | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| CMCSA | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| NFLX | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| DIS | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| AMAT | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| ANET | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| DELL | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| HPQ | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| INTU | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| LRCX | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| NOW | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| PANW | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| SNDK | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| SNX | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| TMUS | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| TXN | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| PLTR | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |

## B. Every in-scope exposure

Exact numeric checks are distinguished from filing links and estimates. UNVERIFIED values are retained, not silently replaced. Historical observed low/high values are not forecast confidence intervals.

| Company | Exposure | Base | Low | High | Exact-source status | Primary source / location / rationale |
|---|---|---:|---:|---:|---|---|
| MSFT | audit_us_pretax_income_musd | 103,591 | 62,886 | 103,591 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0000789019.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2026-06-30 · US-incorporated issuer; 2026-06-30 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| GOOGL | audit_us_pretax_income_musd | 143,591 | 73,600 | 143,591 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0001652044.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-12-31 · US-incorporated issuer; 2025-12-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| META | audit_us_pretax_income_musd | 79,644 | 43,499 | 79,644 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0001326801.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-12-31 · US-incorporated issuer; 2025-12-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| NVDA | audit_us_pretax_income_musd | 123,181 | 29,495 | 123,181 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0001045810.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2026-01-25 · US-incorporated issuer; 2026-01-25 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| VZ | audit_us_pretax_income_musd | 20,150 | 15,668 | 21,253 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0000732712.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-12-31 · US-incorporated issuer; 2025-12-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| CRM | audit_us_pretax_income_musd | 6,627 | 4,045 | 6,627 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0001108524.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2026-01-31 · US-incorporated issuer; 2026-01-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| ADBE | audit_us_pretax_income_musd | 6,721 | 3,465 | 6,721 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0000796343.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-11-28 · US-incorporated issuer; 2025-11-28 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| AMD | audit_us_pretax_income_musd | 4,588 | 454 | 4,588 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0000002488.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-12-27 · US-incorporated issuer; 2025-12-27 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| QCOM | audit_us_pretax_income_musd | 11,174 | 6,400 | 11,174 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0000804328.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-09-28 · US-incorporated issuer; 2025-09-28 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| MU | audit_us_pretax_income_musd | 4,819 | 544 | 4,819 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0000723125.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2026-09-03 · US-incorporated issuer; 2026-09-03 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| CSCO | audit_us_pretax_income_musd | 14,062 | 9,500 | 14,062 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0000858877.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2026-07-25 · US-incorporated issuer; 2026-07-25 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| T | audit_us_pretax_income_musd | 26,993 | 16,674 | 26,993 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0000732717.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-12-31 · US-incorporated issuer; 2025-12-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| CMCSA | audit_us_pretax_income_musd | 26,766 | 19,615 | 26,766 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0001166691.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-12-31 · US-incorporated issuer; 2025-12-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| NFLX | audit_us_pretax_income_musd | 12,198.273 | 5,602.762 | 12,198.273 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0001065280.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-12-31 · US-incorporated issuer; 2025-12-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| DIS | audit_us_pretax_income_musd | 9,535 | 3,086 | 9,535 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0001744489.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-09-27 · US-incorporated issuer; 2025-09-27 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| AMAT | audit_us_pretax_income_musd | 56 | 56 | 1,234 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0000006951.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-10-26 · US-incorporated issuer; 2025-10-26 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| ANET | audit_us_pretax_income_musd | 3,369.6 | 1,977.7 | 3,369.6 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0001596532.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-12-31 · US-incorporated issuer; 2025-12-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| DELL | audit_us_pretax_income_musd | 986 | 986 | 986 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0001571996.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2026-01-30 · US-incorporated issuer; 2026-01-30 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| HPQ | audit_us_pretax_income_musd | 107 | 107 | 650 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0000047217.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-10-31 · US-incorporated issuer; 2025-10-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| INTU | audit_us_pretax_income_musd | 5,875 | 3,449 | 5,875 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0000896878.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2026-07-31 · US-incorporated issuer; 2026-07-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| LRCX | audit_us_pretax_income_musd | 535.542 | 219.435 | 535.542 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0000707549.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2026-06-28 · US-incorporated issuer; 2026-06-28 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| NOW | audit_us_pretax_income_musd | 1,302 | 523 | 1,302 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0001373715.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-12-31 · US-incorporated issuer; 2025-12-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| PANW | audit_us_pretax_income_musd | 466 | 466 | 1,125 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0001327567.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2026-07-31 · US-incorporated issuer; 2026-07-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| SNDK | audit_us_pretax_income_musd | 10,874 | 40 | 10,874 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0002023554.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2026-07-03 · US-incorporated issuer; 2026-07-03 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| SNX | audit_us_pretax_income_musd | 557.284 | 263.321 | 557.284 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0001177394.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-11-30 · US-incorporated issuer; 2025-11-30 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| TMUS | audit_us_pretax_income_musd | 14,018 | 10,943 | 14,607 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0001283699.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-12-31 · US-incorporated issuer; 2025-12-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| TXN | audit_us_pretax_income_musd | 4,503 | 4,438 | 6,445 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0000097476.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-12-31 · US-incorporated issuer; 2025-12-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| PLTR | audit_us_pretax_income_musd | 1,584.577 | 174.637 | 1,584.577 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0001321655.json · IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / 2025-12-31 · Delaware verified on annual cover (https://www.sec.gov/Archives/edgar/data/1321655/000132165526000011/pltr-20251231.htm); 2025-12-31 domestic pretax book income. Historical annual bounds are not forecast confidence intervals; book income is not taxable income. |

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
| exposure.audit_us_pretax_income_musd | -0.02530162 | -0.051235365 | 0.025933744 |

Dominant configured driver: `audit_us_pretax_income_musd` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.


## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 0 unchecked in-scope exposure values; 0 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

# US corporate tax rate increase — book-income proxy

Policy `consumer_retail/us_corporate_tax_consumer_retail` · reviewed 2026-10-31 · **FAIL-UNRESOLVED**

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
| WMT | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| TGT | unquantified | Positive US taxable-income proxy not verified; jurisdiction, pass-through status or loss-tax treatment requires review. |
| COST | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| AMZN | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| NKE | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| HD | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| LOW | unquantified | Positive US taxable-income proxy not verified; jurisdiction, pass-through status or loss-tax treatment requires review. |
| KR | unquantified | Positive US taxable-income proxy not verified; jurisdiction, pass-through status or loss-tax treatment requires review. |
| DG | unquantified | Positive US taxable-income proxy not verified; jurisdiction, pass-through status or loss-tax treatment requires review. |
| DLTR | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| TJX | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| ROST | unquantified | Positive US taxable-income proxy not verified; jurisdiction, pass-through status or loss-tax treatment requires review. |
| SBUX | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| MCD | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| KO | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| PEP | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| PG | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| CL | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| ULTA | unquantified | Positive US taxable-income proxy not verified; jurisdiction, pass-through status or loss-tax treatment requires review. |
| BBY | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| MDLZ | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| MO | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| PFGC | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| PM | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| SYY | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| TSN | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |

## B. Every in-scope exposure

Exact numeric checks are distinguished from filing links and estimates. UNVERIFIED values are retained, not silently replaced. Historical observed low/high values are not forecast confidence intervals.

| Company | Exposure | Base | Low | High | Exact-source status | Primary source / location / rationale |
|---|---|---:|---:|---:|---|---|
| WMT | audit_us_pretax_income_musd | 23,272 | 18,571 | 23,272 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0000104169.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2026-01-31 · US-incorporated issuer; 2026-01-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| COST | audit_us_pretax_income_musd | 9,070 | 7,255 | 9,070 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0000909832.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2026-08-30 · US-incorporated issuer; 2026-08-30 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| AMZN | audit_us_pretax_income_musd | 89,537 | 32,328 | 89,537 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0001018724.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-12-31 · US-incorporated issuer; 2025-12-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| NKE | audit_us_pretax_income_musd | 2,680 | 2,680 | 5,588 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0000320187.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2026-05-31 · US-incorporated issuer; 2026-05-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| HD | audit_us_pretax_income_musd | 17,431 | 17,431 | 18,681 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0000354950.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2026-02-01 · US-incorporated issuer; 2026-02-01 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| DLTR | audit_us_pretax_income_musd | 1,621.6 | 1,361 | 1,638.9 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0000935703.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2026-01-31 · US-incorporated issuer; 2026-01-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| TJX | audit_us_pretax_income_musd | 6,264 | 5,077 | 6,264 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0000109198.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2026-01-31 · US-incorporated issuer; 2026-01-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| SBUX | audit_us_pretax_income_musd | 1,850.1 | 1,850.1 | 4,488.6 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0000829224.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-09-28 · US-incorporated issuer; 2025-09-28 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| MCD | audit_us_pretax_income_musd | 3,291 | 3,282 | 3,665 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0000063908.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-12-31 · US-incorporated issuer; 2025-12-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| KO | audit_us_pretax_income_musd | 5,678 | 1,991 | 5,678 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021344.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-12-31 · US-incorporated issuer; 2025-12-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| PEP | audit_us_pretax_income_musd | 806 | 806 | 4,120 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077476.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-12-27 · US-incorporated issuer; 2025-12-27 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| PG | audit_us_pretax_income_musd | 13,728 | 12,246 | 13,911 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0000080424.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2026-06-30 · US-incorporated issuer; 2026-06-30 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| CL | audit_us_pretax_income_musd | 1,419 | 692 | 1,419 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021665.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-12-31 · US-incorporated issuer; 2025-12-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| BBY | audit_us_pretax_income_musd | 1,223 | 1,095 | 1,389 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0000764478.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2026-01-31 · US-incorporated issuer; 2026-01-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| MDLZ | audit_us_pretax_income_musd | 750 | 750 | 1,688 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0001103982.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-12-31 · US-incorporated issuer; 2025-12-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| MO | audit_us_pretax_income_musd | 9,382 | 9,382 | 13,680 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0000764180.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-12-31 · US-incorporated issuer; 2025-12-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| PFGC | audit_us_pretax_income_musd | 479 | 461.6 | 579.6 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0001618673.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2026-06-27 · US-incorporated issuer; 2026-06-27 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| PM | audit_us_pretax_income_musd | 870 | 870 | 870 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0001413329.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-12-31 · US-incorporated issuer; 2025-12-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| SYY | audit_us_pretax_income_musd | 2,056 | 2,056 | 2,260 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0000096021.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2026-06-27 · US-incorporated issuer; 2026-06-27 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| TSN | audit_us_pretax_income_musd | 278 | 278 | 864 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0000100493.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-09-27 · US-incorporated issuer; 2025-09-27 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |

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
| exposure.audit_us_pretax_income_musd | -0.03766461 | -0.06529169 | 0.02762708 |

Dominant configured driver: `audit_us_pretax_income_musd` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.


## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 0 unchecked in-scope exposure values; 0 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

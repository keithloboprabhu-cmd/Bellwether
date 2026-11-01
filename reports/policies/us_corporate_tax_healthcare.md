# US corporate tax rate increase — book-income proxy

Policy `healthcare/us_corporate_tax_healthcare` · evidence checkpoint 2026-11-01 · **FAIL-UNRESOLVED**

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
| UNH | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| ELV | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| HUM | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| CVS | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| PFE | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| LLY | unquantified | Positive US taxable-income proxy not verified; jurisdiction, pass-through status or loss-tax treatment requires review. |
| CI | unquantified | Positive US taxable-income proxy not verified; jurisdiction, pass-through status or loss-tax treatment requires review. |
| CNC | unquantified | Positive US taxable-income proxy not verified; jurisdiction, pass-through status or loss-tax treatment requires review. |
| MOH | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| JNJ | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| MRK | unquantified | Positive US taxable-income proxy not verified; jurisdiction, pass-through status or loss-tax treatment requires review. |
| ABBV | unquantified | Positive US taxable-income proxy not verified; jurisdiction, pass-through status or loss-tax treatment requires review. |
| AMGN | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| GILD | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| HCA | unquantified | Positive US taxable-income proxy not verified; jurisdiction, pass-through status or loss-tax treatment requires review. |
| THC | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| UHS | unquantified | Positive US taxable-income proxy not verified; jurisdiction, pass-through status or loss-tax treatment requires review. |
| TMO | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| ABT | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| MDT | unquantified | Positive US taxable-income proxy not verified; jurisdiction, pass-through status or loss-tax treatment requires review. |
| CAH | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| COR | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| ISRG | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| MCK | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |

## B. Every in-scope exposure

Exact numeric checks are distinguished from filing links and estimates. UNVERIFIED values are retained, not silently replaced. Historical observed low/high values are not forecast confidence intervals.

| Company | Exposure | Base | Low | High | Exact-source status | Primary source / location / rationale |
|---|---|---:|---:|---:|---|---|
| UNH | audit_us_pretax_income_musd | 14,893 | 14,893 | 29,210 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0000731766.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-12-31 · US-incorporated issuer; 2025-12-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| ELV | audit_us_pretax_income_musd | 6,322 | 6,322 | 7,629 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0001156039.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-12-31 · US-incorporated issuer; 2025-12-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| HUM | audit_us_pretax_income_musd | 1,485 | 1,485 | 3,351 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0000049071.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-12-31 · US-incorporated issuer; 2025-12-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| CVS | audit_us_pretax_income_musd | 1,335 | 1,335 | 11,107 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0000064803.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-12-31 · US-incorporated issuer; 2025-12-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| PFE | audit_us_pretax_income_musd | 776 | 776 | 776 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0000078003.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-12-31 · US-incorporated issuer; 2025-12-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| MOH | audit_us_pretax_income_musd | 589 | 589 | 1,582 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0001179929.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-12-31 · US-incorporated issuer; 2025-12-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| JNJ | audit_us_pretax_income_musd | 15,254 | 15,254 | 15,254 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0000200406.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-12-28 · US-incorporated issuer; 2025-12-28 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| AMGN | audit_us_pretax_income_musd | 8,220 | 4,040 | 8,220 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0000318154.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-12-31 · US-incorporated issuer; 2025-12-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| GILD | audit_us_pretax_income_musd | 8,310 | 5,467 | 8,310 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0000882095.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-12-31 · US-incorporated issuer; 2025-12-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| THC | audit_us_pretax_income_musd | 2,805 | 1,620 | 5,251 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0000070318.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-12-31 · US-incorporated issuer; 2025-12-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| TMO | audit_us_pretax_income_musd | 2,608 | 2,226 | 2,608 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0000097745.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-12-31 · US-incorporated issuer; 2025-12-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| ABT | audit_us_pretax_income_musd | 1,762 | 947 | 1,762 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0000001800.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-12-31 · US-incorporated issuer; 2025-12-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| CAH | audit_us_pretax_income_musd | 1,753 | 892 | 1,753 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0000721371.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2026-06-30 · US-incorporated issuer; 2026-06-30 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| COR | audit_us_pretax_income_musd | 1,611.725 | 1,288.983 | 1,611.725 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0001140859.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-09-30 · US-incorporated issuer; 2025-09-30 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| ISRG | audit_us_pretax_income_musd | 2,283.8 | 1,251.1 | 2,283.8 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0001035267.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-12-31 · US-incorporated issuer; 2025-12-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| MCK | audit_us_pretax_income_musd | 4,300 | 2,597 | 4,300 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0000927653.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2026-03-31 · US-incorporated issuer; 2026-03-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |

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
| exposure.audit_us_pretax_income_musd | -0.027052956 | -0.046037238 | 0.018984282 |

Dominant configured driver: `audit_us_pretax_income_musd` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.


## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 0 unchecked in-scope exposure values; 0 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

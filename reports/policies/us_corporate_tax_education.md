# US corporate tax rate increase — book-income proxy

Policy `education/us_corporate_tax_education` · reviewed 2026-10-31 · **FAIL-UNRESOLVED**

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
| LRN | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| LOPE | unquantified | Positive US taxable-income proxy not verified; jurisdiction, pass-through status or loss-tax treatment requires review. |
| CVSA | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| STRA | unquantified | Positive US taxable-income proxy not verified; jurisdiction, pass-through status or loss-tax treatment requires review. |
| DUOL | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| COUR | unquantified | Positive US taxable-income proxy not verified; jurisdiction, pass-through status or loss-tax treatment requires review. |
| UTI | unquantified | Positive US taxable-income proxy not verified; jurisdiction, pass-through status or loss-tax treatment requires review. |
| PRDO | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| APEI | unquantified | Positive US taxable-income proxy not verified; jurisdiction, pass-through status or loss-tax treatment requires review. |
| LAUR | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| NRDY | unquantified | Positive US taxable-income proxy not verified; jurisdiction, pass-through status or loss-tax treatment requires review. |
| LINC | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| SKIL | unquantified | Positive US taxable-income proxy not verified; jurisdiction, pass-through status or loss-tax treatment requires review. |
| CHGG | unquantified | Positive US taxable-income proxy not verified; jurisdiction, pass-through status or loss-tax treatment requires review. |
| SCHL | unquantified | Positive US taxable-income proxy not verified; jurisdiction, pass-through status or loss-tax treatment requires review. |
| KLC | unquantified | Positive US taxable-income proxy not verified; jurisdiction, pass-through status or loss-tax treatment requires review. |
| BFAM | unquantified | Positive US taxable-income proxy not verified; jurisdiction, pass-through status or loss-tax treatment requires review. |
| WLY | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| FC | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| SLM | unquantified | Positive US taxable-income proxy not verified; jurisdiction, pass-through status or loss-tax treatment requires review. |

## B. Every in-scope exposure

Exact numeric checks are distinguished from filing links and estimates. UNVERIFIED values are retained, not silently replaced. Historical observed low/high values are not forecast confidence intervals.

| Company | Exposure | Base | Low | High | Exact-source status | Primary source / location / rationale |
|---|---|---:|---:|---:|---|---|
| LRN | audit_us_pretax_income_musd | 435.108 | 262.802 | 435.108 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0001157408.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2026-06-30 · US-incorporated issuer; 2026-06-30 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| CVSA | audit_us_pretax_income_musd | 254.316 | 89.752 | 254.316 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0000730464.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2026-06-30 · US-incorporated issuer; 2026-06-30 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| DUOL | audit_us_pretax_income_musd | 167.873 | 16.501 | 167.873 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0001562088.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-12-31 · US-incorporated issuer; 2025-12-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| PRDO | audit_us_pretax_income_musd | 216.836 | 192.121 | 216.836 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0001046568.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-12-31 · US-incorporated issuer; 2025-12-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| LAUR | audit_us_pretax_income_musd | 56.594 | 56.128 | 63.847 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0000912766.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-12-31 · US-incorporated issuer; 2025-12-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| LINC | audit_us_pretax_income_musd | 26.118 | 14.711 | 35.639 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0001286613.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-12-31 · US-incorporated issuer; 2025-12-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| WLY | audit_us_pretax_income_musd | 22.277 | 22.277 | 22.277 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0000107140.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2026-04-30 · US-incorporated issuer; 2026-04-30 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| FC | audit_us_pretax_income_musd | 8.698 | 8.698 | 32.456 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0000886206.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-08-31 · US-incorporated issuer; 2025-08-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |

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
| exposure.audit_us_pretax_income_musd | -0.018726396 | -0.034695254 | 0.015968857 |

Dominant configured driver: `audit_us_pretax_income_musd` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.


## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 0 unchecked in-scope exposure values; 0 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

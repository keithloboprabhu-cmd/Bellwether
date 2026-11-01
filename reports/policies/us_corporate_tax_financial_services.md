# US corporate tax rate increase — book-income proxy

Policy `financial_services/us_corporate_tax_financial_services` · reviewed 2026-10-31 · **FAIL-UNRESOLVED**

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
| JPM | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| BAC | unquantified | Positive US taxable-income proxy not verified; jurisdiction, pass-through status or loss-tax treatment requires review. |
| WFC | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| GS | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| C | unquantified | Positive US taxable-income proxy not verified; jurisdiction, pass-through status or loss-tax treatment requires review. |
| AXP | unquantified | Positive US taxable-income proxy not verified; jurisdiction, pass-through status or loss-tax treatment requires review. |
| MS | unquantified | Positive US taxable-income proxy not verified; jurisdiction, pass-through status or loss-tax treatment requires review. |
| SCHW | unquantified | Positive US taxable-income proxy not verified; jurisdiction, pass-through status or loss-tax treatment requires review. |
| BNY | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| STT | unquantified | Positive US taxable-income proxy not verified; jurisdiction, pass-through status or loss-tax treatment requires review. |
| USB | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| PNC | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| TFC | unquantified | Positive US taxable-income proxy not verified; jurisdiction, pass-through status or loss-tax treatment requires review. |
| COF | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| FITB | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| HBAN | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| KEY | unquantified | Positive US taxable-income proxy not verified; jurisdiction, pass-through status or loss-tax treatment requires review. |
| ALLY | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| MA | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| BLK | unquantified | Positive US taxable-income proxy not verified; jurisdiction, pass-through status or loss-tax treatment requires review. |
| AIG | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| PRU | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| PGR | unquantified | Positive US taxable-income proxy not verified; jurisdiction, pass-through status or loss-tax treatment requires review. |
| ALL | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| MET | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| SNEX | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| SPGI | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| TRV | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| V | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |
| PYPL | included | US-incorporated issuer with positive reported domestic pretax book income; rate-only linear proxy, not a cash-tax forecast. |

## B. Every in-scope exposure

Exact numeric checks are distinguished from filing links and estimates. UNVERIFIED values are retained, not silently replaced. Historical observed low/high values are not forecast confidence intervals.

| Company | Exposure | Base | Low | High | Exact-source status | Primary source / location / rationale |
|---|---|---:|---:|---:|---|---|
| JPM | audit_us_pretax_income_musd | 56,184 | 46,868 | 59,472 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0000019617.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-12-31 · US-incorporated issuer; 2025-12-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| WFC | audit_us_pretax_income_musd | 23,644 | 20,721 | 23,644 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0000072971.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-12-31 · US-incorporated issuer; 2025-12-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| GS | audit_us_pretax_income_musd | 13,764 | 13,764 | 13,764 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0000886982.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-12-31 · US-incorporated issuer; 2025-12-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| BNY | audit_us_pretax_income_musd | 4,431 | 2,196 | 4,431 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0001390777.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-12-31 · US-incorporated issuer; 2025-12-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| USB | audit_us_pretax_income_musd | 9,330 | 6,738 | 9,330 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0000036104.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-12-31 · US-incorporated issuer; 2025-12-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| PNC | audit_us_pretax_income_musd | 8,378 | 6,624 | 8,378 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0000713676.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-12-31 · US-incorporated issuer; 2025-12-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| COF | audit_us_pretax_income_musd | 1,918 | 1,918 | 5,815 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0000927628.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-12-31 · US-incorporated issuer; 2025-12-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| FITB | audit_us_pretax_income_musd | 3,211 | 2,919 | 3,211 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0000035527.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-12-31 · US-incorporated issuer; 2025-12-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| HBAN | audit_us_pretax_income_musd | 2,666 | 2,353 | 2,666 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0000049196.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-12-31 · US-incorporated issuer; 2025-12-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| ALLY | audit_us_pretax_income_musd | 1,031 | 817 | 1,086 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0000040729.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-12-31 · US-incorporated issuer; 2025-12-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| MA | audit_us_pretax_income_musd | 6,652 | 4,506 | 6,652 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0001141391.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-12-31 · US-incorporated issuer; 2025-12-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| AIG | audit_us_pretax_income_musd | 1,503 | 900 | 1,818 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0000005272.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-12-31 · US-incorporated issuer; 2025-12-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| PRU | audit_us_pretax_income_musd | 2,184 | 1,341 | 2,184 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0001137774.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-12-31 · US-incorporated issuer; 2025-12-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| ALL | audit_us_pretax_income_musd | 12,722 | 12,722 | 12,722 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0000899051.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-12-31 · US-incorporated issuer; 2025-12-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| MET | audit_us_pretax_income_musd | 599 | 599 | 3,955 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0001099219.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-12-31 · US-incorporated issuer; 2025-12-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| SNEX | audit_us_pretax_income_musd | 148.9 | 97.8 | 148.9 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0000913760.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-09-30 · US-incorporated issuer; 2025-09-30 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| SPGI | audit_us_pretax_income_musd | 3,356 | 1,899 | 3,436 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0000064040.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-12-31 · US-incorporated issuer; 2025-12-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| TRV | audit_us_pretax_income_musd | 7,372 | 3,122 | 7,372 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0000086312.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-12-31 · US-incorporated issuer; 2025-12-31 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| V | audit_us_pretax_income_musd | 14,776 | 13,339 | 14,776 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0001403161.json · us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / annual period 2025-09-30 · US-incorporated issuer; 2025-09-30 us-gaap domestic pretax book income. Low/high are observed available three-year values. Taxable income and future offsets are not disclosed; linear book-tax sensitivity is a model proxy. |
| PYPL | audit_us_pretax_income_musd | 1,453 | 946 | 1,453 | VERIFIED observation; conversion limits retained | https://data.sec.gov/api/xbrl/companyfacts/CIK0001633917.json · IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic / 2025-12-31 · Delaware verified on annual cover (https://www.sec.gov/Archives/edgar/data/1633917/000163391726000024/pypl-20251231.htm); 2025-12-31 domestic pretax book income. Historical annual bounds are not forecast confidence intervals; book income is not taxable income. |

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
| exposure.audit_us_pretax_income_musd | -0.033202242 | -0.042836121 | 0.0096338793 |

Dominant configured driver: `audit_us_pretax_income_musd` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.


## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 0 unchecked in-scope exposure values; 0 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

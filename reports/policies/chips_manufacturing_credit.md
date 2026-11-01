# CHIPS-style chip-manufacturing investment credit

Policy `tmt/chips_manufacturing_credit` · reviewed 2026-10-31 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

A tax credit on US capex for facilities that make semiconductors or chip-making equipment (like Section 48D). Intel and Micron have modeled US fabrication investment; fabless designers and software firms receive no direct credit without their own qualifying manufacturing property. US capex allocation and placed-in-service timing are explicit estimates.

Duration: `years:5`. Default inputs: `{"credit_pct": 35.0}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| tax_credit | unavailable / unavailable | {"credit_rate": "input.credit_pct / 100", "base_musd": "exposure.us_semis_mfg_capex_musd * assumption.qualifying_share"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://www.law.cornell.edu/uscode/text/26/48D

| Company | Configured status | Basis |
|---|---|---|
| AAPL | outside_scope | The credit requires qualifying US chip manufacturing investment. Fabless chip designers, software firms and device buyers do not inherit foundry capex. |
| MSFT | outside_scope | The credit requires qualifying US chip manufacturing investment. Fabless chip designers, software firms and device buyers do not inherit foundry capex. |
| GOOGL | outside_scope | The credit requires qualifying US chip manufacturing investment. Fabless chip designers, software firms and device buyers do not inherit foundry capex. |
| META | outside_scope | The credit requires qualifying US chip manufacturing investment. Fabless chip designers, software firms and device buyers do not inherit foundry capex. |
| NVDA | outside_scope | The credit requires qualifying US chip manufacturing investment. Fabless chip designers, software firms and device buyers do not inherit foundry capex. |
| VZ | outside_scope | The credit requires qualifying US chip manufacturing investment. Fabless chip designers, software firms and device buyers do not inherit foundry capex. |
| IBM | outside_scope | The credit requires qualifying US chip manufacturing investment. Fabless chip designers, software firms and device buyers do not inherit foundry capex. |
| ORCL | outside_scope | The credit requires qualifying US chip manufacturing investment. Fabless chip designers, software firms and device buyers do not inherit foundry capex. |
| CRM | outside_scope | The credit requires qualifying US chip manufacturing investment. Fabless chip designers, software firms and device buyers do not inherit foundry capex. |
| ADBE | outside_scope | The credit requires qualifying US chip manufacturing investment. Fabless chip designers, software firms and device buyers do not inherit foundry capex. |
| INTC | included | Credit applies to qualifying estimated US manufacturing capex, including Intel/Micron. |
| AMD | outside_scope | The credit requires qualifying US chip manufacturing investment. Fabless chip designers, software firms and device buyers do not inherit foundry capex. |
| QCOM | outside_scope | The credit requires qualifying US chip manufacturing investment. Fabless chip designers, software firms and device buyers do not inherit foundry capex. |
| MU | included | Credit applies to qualifying estimated US manufacturing capex, including Intel/Micron. |
| AVGO | outside_scope | The credit requires qualifying US chip manufacturing investment. Fabless chip designers, software firms and device buyers do not inherit foundry capex. |
| CSCO | outside_scope | The credit requires qualifying US chip manufacturing investment. Fabless chip designers, software firms and device buyers do not inherit foundry capex. |
| T | outside_scope | The credit requires qualifying US chip manufacturing investment. Fabless chip designers, software firms and device buyers do not inherit foundry capex. |
| CMCSA | outside_scope | The credit requires qualifying US chip manufacturing investment. Fabless chip designers, software firms and device buyers do not inherit foundry capex. |
| NFLX | outside_scope | The credit requires qualifying US chip manufacturing investment. Fabless chip designers, software firms and device buyers do not inherit foundry capex. |
| DIS | outside_scope | The credit requires qualifying US chip manufacturing investment. Fabless chip designers, software firms and device buyers do not inherit foundry capex. |
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
| INTC | us_semis_mfg_capex_musd | 7,323 | 3,661.5 | 10,984.5 | UNVERIFIED | https://www.intc.com/filings-reports/annual-reports/content/0000050863-26-000011/intc-20251227.htm · estimate; Company-specific estimate: SEC FY2025 PaymentsToAcquirePropertyPlantAndEquipment = $14,646M worldwide. Apply an estimated US manufacturing share of 50% (25–75% range); this is not a disclosed US capex amount. Includes US fabs; geographic allocation and placed-in-service eligibility require review. The policy applies its separate qualifying-share assumption. · Company-specific estimate: SEC FY2025 PaymentsToAcquirePropertyPlantAndEquipment = $14,646M worldwide. Apply an estimated US manufacturing share of 50% (25–75% range); this is not a disclosed US capex amount. Includes US fabs; geographic allocation and placed-in-service eligibility require review. The policy applies its separate qualifying-share assumption. |
| MU | us_semis_mfg_capex_musd | 7,678 | 3,071.2 | 12,284.8 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/723125/000072312526000023/mu-20260903.htm · estimate; Company-specific estimate: SEC FY2026 PaymentsToAcquirePropertyPlantAndEquipment = $30,712M worldwide. Apply an estimated US share of 25% (10–40% range), reflecting Idaho/New York construction and Virginia alongside large overseas fabs. Not a disclosed US annual spend; construction spending and placed-in-service credit timing differ. · Company-specific estimate: SEC FY2026 PaymentsToAcquirePropertyPlantAndEquipment = $30,712M worldwide. Apply an estimated US share of 25% (10–40% range), reflecting Idaho/New York construction and Virginia alongside large overseas fabs. Not a disclosed US annual spend; construction spending and placed-in-service credit timing differ. |

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
| exposure.us_semis_mfg_capex_musd | 0.0024262704 | 0.0083855827 | 0.0059593124 |
| assumption.qualifying_share | 0.0042046095 | 0.0060065851 | 0.0018019755 |

Dominant configured driver: `us_semis_mfg_capex_musd` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.


## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 2 unchecked in-scope exposure values; 1 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

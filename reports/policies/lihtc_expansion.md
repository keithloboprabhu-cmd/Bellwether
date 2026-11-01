# Low-income housing tax credit expansion

Policy `real_estate_hospitality/lihtc_expansion` · reviewed 2026-10-31 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

A bigger Low-Income Housing Tax Credit raises credits on affordable-housing investment. No qualified affordable-housing investment basis has been sourced for the current company sample, so this direct-credit channel has no quantified exposure. This is a coverage limitation, not proof that every company has no economic exposure.

Duration: `permanent`. Default inputs: `{"credit_increase_pct": 12.5}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| tax_credit | unavailable / unavailable | {"credit_rate": "assumption.annual_credit_rate * input.credit_increase_pct / 100", "base_musd": "exposure.re_lihtc_investment_musd"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://www.sec.gov/Archives/edgar/data/1063761/000110465926019419/

| Company | Configured status | Basis |
|---|---|---|
| PLD | unquantified | No qualifying LIHTC investment base has been quantified for this sample. This is missing model coverage, not evidence that these companies are legally ineligible or cannot be affected. |
| AMT | unquantified | No qualifying LIHTC investment base has been quantified for this sample. This is missing model coverage, not evidence that these companies are legally ineligible or cannot be affected. |
| SPG | unquantified | No qualifying LIHTC investment base has been quantified for this sample. This is missing model coverage, not evidence that these companies are legally ineligible or cannot be affected. |
| MAR | unquantified | No qualifying LIHTC investment base has been quantified for this sample. This is missing model coverage, not evidence that these companies are legally ineligible or cannot be affected. |
| HLT | unquantified | No qualifying LIHTC investment base has been quantified for this sample. This is missing model coverage, not evidence that these companies are legally ineligible or cannot be affected. |
| ABNB | unquantified | No qualifying LIHTC investment base has been quantified for this sample. This is missing model coverage, not evidence that these companies are legally ineligible or cannot be affected. |
| O | unquantified | No qualifying LIHTC investment base has been quantified for this sample. This is missing model coverage, not evidence that these companies are legally ineligible or cannot be affected. |
| EQIX | unquantified | No qualifying LIHTC investment base has been quantified for this sample. This is missing model coverage, not evidence that these companies are legally ineligible or cannot be affected. |
| DLR | unquantified | No qualifying LIHTC investment base has been quantified for this sample. This is missing model coverage, not evidence that these companies are legally ineligible or cannot be affected. |
| WELL | unquantified | No qualifying LIHTC investment base has been quantified for this sample. This is missing model coverage, not evidence that these companies are legally ineligible or cannot be affected. |
| VTR | unquantified | No qualifying LIHTC investment base has been quantified for this sample. This is missing model coverage, not evidence that these companies are legally ineligible or cannot be affected. |
| ESS | unquantified | No qualifying LIHTC investment base has been quantified for this sample. This is missing model coverage, not evidence that these companies are legally ineligible or cannot be affected. |
| MAA | unquantified | No qualifying LIHTC investment base has been quantified for this sample. This is missing model coverage, not evidence that these companies are legally ineligible or cannot be affected. |
| PSA | unquantified | No qualifying LIHTC investment base has been quantified for this sample. This is missing model coverage, not evidence that these companies are legally ineligible or cannot be affected. |
| EXR | unquantified | No qualifying LIHTC investment base has been quantified for this sample. This is missing model coverage, not evidence that these companies are legally ineligible or cannot be affected. |
| VICI | unquantified | No qualifying LIHTC investment base has been quantified for this sample. This is missing model coverage, not evidence that these companies are legally ineligible or cannot be affected. |
| WY | unquantified | No qualifying LIHTC investment base has been quantified for this sample. This is missing model coverage, not evidence that these companies are legally ineligible or cannot be affected. |
| HST | unquantified | No qualifying LIHTC investment base has been quantified for this sample. This is missing model coverage, not evidence that these companies are legally ineligible or cannot be affected. |
| RLJ | unquantified | No qualifying LIHTC investment base has been quantified for this sample. This is missing model coverage, not evidence that these companies are legally ineligible or cannot be affected. |
| PK | unquantified | No qualifying LIHTC investment base has been quantified for this sample. This is missing model coverage, not evidence that these companies are legally ineligible or cannot be affected. |

## B. Every in-scope exposure

Exact numeric checks are distinguished from filing links and estimates. UNVERIFIED values are retained, not silently replaced. Historical observed low/high values are not forecast confidence intervals.

| Company | Exposure | Base | Low | High | Exact-source status | Primary source / location / rationale |
|---|---|---:|---:|---:|---|---|
| — | No quantified in-scope company exposure | — | — | — | FAIL-UNRESOLVED | Absence of a measured base is not proof of no economic exposure. |

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
| assumption.annual_credit_rate | 0 | 0 | 0 |

Dominant configured driver: `annual_credit_rate` using `d_mcap_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.


## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 0 unchecked in-scope exposure values; 1 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

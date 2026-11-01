# PBM rebate pass-through reform

Policy `healthcare/pbm_rebate_pass_through` · evidence checkpoint 2026-11-01 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

Rules requiring PBMs to pass manufacturer rebates through to plan sponsors (or delink PBM pay from drug prices) remove rebate income that CVS Caremark, Optum Rx and CarelonRx keep today. PBMs recoup part of it through flat service fees.

Duration: `permanent`. Default inputs: `{"pass_through_pct": 50.0}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| price | unavailable / unavailable | {"d_price": "-input.pass_through_pct / 100", "exposed_revenue_share": "exposure.pbm_retained_rebate_share", "offset_share": "assumption.fee_offset"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://www.sec.gov/Archives/edgar/data/64803/000006480326000009/cvs_ex99x1q4-25.htm
- https://www.sec.gov/Archives/edgar/data/731766/000073176626000062/unh-20251231.htm

| Company | Configured status | Basis |
|---|---|---|
| UNH | included | Owned PBMs lose retained rebates after partial service-fee offset. |
| ELV | included | Owned PBMs lose retained rebates after partial service-fee offset. |
| HUM | included | Owned PBMs lose retained rebates after partial service-fee offset. |
| CVS | included | Owned PBMs lose retained rebates after partial service-fee offset. |
| PFE | outside_scope | Owned PBM retained rebates are modeled. Outsourced PBM contracts and manufacturer rebates are distinct from retained PBM income. |
| LLY | outside_scope | Owned PBM retained rebates are modeled. Outsourced PBM contracts and manufacturer rebates are distinct from retained PBM income. |
| CI | included | Owned PBMs lose retained rebates after partial service-fee offset. |
| CNC | outside_scope | Owned PBM retained rebates are modeled. Outsourced PBM contracts and manufacturer rebates are distinct from retained PBM income. |
| MOH | outside_scope | Owned PBM retained rebates are modeled. Outsourced PBM contracts and manufacturer rebates are distinct from retained PBM income. |
| JNJ | outside_scope | Owned PBM retained rebates are modeled. Outsourced PBM contracts and manufacturer rebates are distinct from retained PBM income. |
| MRK | outside_scope | Owned PBM retained rebates are modeled. Outsourced PBM contracts and manufacturer rebates are distinct from retained PBM income. |
| ABBV | outside_scope | Owned PBM retained rebates are modeled. Outsourced PBM contracts and manufacturer rebates are distinct from retained PBM income. |
| AMGN | outside_scope | Owned PBM retained rebates are modeled. Outsourced PBM contracts and manufacturer rebates are distinct from retained PBM income. |
| GILD | outside_scope | Owned PBM retained rebates are modeled. Outsourced PBM contracts and manufacturer rebates are distinct from retained PBM income. |
| HCA | outside_scope | Owned PBM retained rebates are modeled. Outsourced PBM contracts and manufacturer rebates are distinct from retained PBM income. |
| THC | outside_scope | Owned PBM retained rebates are modeled. Outsourced PBM contracts and manufacturer rebates are distinct from retained PBM income. |
| UHS | outside_scope | Owned PBM retained rebates are modeled. Outsourced PBM contracts and manufacturer rebates are distinct from retained PBM income. |
| TMO | outside_scope | Owned PBM retained rebates are modeled. Outsourced PBM contracts and manufacturer rebates are distinct from retained PBM income. |
| ABT | outside_scope | Owned PBM retained rebates are modeled. Outsourced PBM contracts and manufacturer rebates are distinct from retained PBM income. |
| MDT | outside_scope | Owned PBM retained rebates are modeled. Outsourced PBM contracts and manufacturer rebates are distinct from retained PBM income. |
| CAH | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| COR | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| ISRG | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| MCK | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |

## B. Every in-scope exposure

Exact numeric checks are distinguished from filing links and estimates. UNVERIFIED values are retained, not silently replaced. Historical observed low/high values are not forecast confidence intervals.

| Company | Exposure | Base | Low | High | Exact-source status | Primary source / location / rationale |
|---|---|---:|---:|---:|---|---|
| UNH | pbm_retained_rebate_share | 0.008 | 0.004 | 0.015 | UNVERIFIED | No source URL · estimate; Optum Rx ($154,726M revenue, $7,193M earnings from operations, $188B of drug spend managed in 2025 per the 10-K) does not disclose retained rebates; assumes retained rebates/fees of roughly 2% of managed drug spend (~$3.5B). · Optum Rx ($154,726M revenue, $7,193M earnings from operations, $188B of drug spend managed in 2025 per the 10-K) does not disclose retained rebates; assumes retained rebates/fees of roughly 2% of managed drug spend (~$3.5B). |
| ELV | pbm_retained_rebate_share | 0.005 | 0.002 | 0.01 | UNVERIFIED | No source URL · estimate; CarelonRx operating revenue $43,400M and operating gain $2,418M in 2025 (Elevance 10-K segment note); retained rebates/fees not disclosed, assumed ~2% of drug spend (~$1B). · CarelonRx operating revenue $43,400M and operating gain $2,418M in 2025 (Elevance 10-K segment note); retained rebates/fees not disclosed, assumed ~2% of drug spend (~$1B). |
| HUM | pbm_retained_rebate_share | 0.002 | 0 | 0.005 | UNVERIFIED | No source URL · estimate; Humana's PBM serves mainly its own plan members, so rebates largely stay inside its own Part D/MA economics rather than being retained from outside clients. · Humana's PBM serves mainly its own plan members, so rebates largely stay inside its own Part D/MA economics rather than being retained from outside clients. |
| CVS | pbm_retained_rebate_share | 0.01 | 0.005 | 0.02 | UNVERIFIED | No source URL · estimate; Caremark (Health Services revenue $190,425M, adjusted operating income $7,151M in 2025 per the Q4 release) does not disclose retained rebates; assumes ~$4B retained rebates and rebate-linked fees. · Caremark (Health Services revenue $190,425M, adjusted operating income $7,151M in 2025 per the Q4 release) does not disclose retained rebates; assumes ~$4B retained rebates and rebate-linked fees. |
| CI | pbm_retained_rebate_share | 0.0065 | 0 | 0.02 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Managed care; median base and outer low/high from UNH/ELV/HUM/CVS in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Managed care; median base and outer low/high from UNH/ELV/HUM/CVS in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |

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
| exposure.pbm_retained_rebate_share | -0.0055963159 | -0.030063034 | 0.024466718 |
| assumption.fee_offset | -0.022469047 | -0.0056172617 | 0.016851785 |

Dominant configured driver: `pbm_retained_rebate_share` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.


## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 5 unchecked in-scope exposure values; 1 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

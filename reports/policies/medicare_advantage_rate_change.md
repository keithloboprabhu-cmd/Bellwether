# Medicare Advantage rate change

Policy `healthcare/medicare_advantage_rate_change` · evidence checkpoint 2026-11-01 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

CMS changes Medicare Advantage payment rates relative to what plans expected. Insurers recover part of a cut by raising premiums and trimming benefits; the rest hits margins. Humana, with about three-quarters of revenue in MA, is by far the most exposed; Pfizer and Lilly are not directly affected.

Duration: `permanent`. Default inputs: `{"rate_change_pct": -2.0}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| price | unavailable / unavailable | {"d_price": "input.rate_change_pct / 100", "exposed_revenue_share": "exposure.medicare_advantage_revenue_share", "offset_share": "assumption.offset_share"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://www.nber.org/papers/w20470
- https://www.sec.gov/Archives/edgar/data/49071/000004907126000009/hum-20251231.htm
- https://www.sec.gov/Archives/edgar/data/731766/000073176626000062/unh-20251231.htm
- https://www.sec.gov/Archives/edgar/data/64803/000006480326000010/cvs-20251231.htm

| Company | Configured status | Basis |
|---|---|---|
| UNH | included | Default MA payment cut lowers premium revenue. |
| ELV | included | Default MA payment cut lowers premium revenue. |
| HUM | included | Default MA payment cut lowers premium revenue. |
| CVS | included | Default MA payment cut lowers premium revenue. |
| PFE | outside_scope | This is a Medicare Advantage premium-rate shock, not a hospital fee schedule or drug price. Cigna sold its Medicare businesses. |
| LLY | outside_scope | This is a Medicare Advantage premium-rate shock, not a hospital fee schedule or drug price. Cigna sold its Medicare businesses. |
| CI | outside_scope | This is a Medicare Advantage premium-rate shock, not a hospital fee schedule or drug price. Cigna sold its Medicare businesses. |
| CNC | included | Default MA payment cut lowers premium revenue. |
| MOH | included | Default MA payment cut lowers premium revenue. |
| JNJ | outside_scope | This is a Medicare Advantage premium-rate shock, not a hospital fee schedule or drug price. Cigna sold its Medicare businesses. |
| MRK | outside_scope | This is a Medicare Advantage premium-rate shock, not a hospital fee schedule or drug price. Cigna sold its Medicare businesses. |
| ABBV | outside_scope | This is a Medicare Advantage premium-rate shock, not a hospital fee schedule or drug price. Cigna sold its Medicare businesses. |
| AMGN | outside_scope | This is a Medicare Advantage premium-rate shock, not a hospital fee schedule or drug price. Cigna sold its Medicare businesses. |
| GILD | outside_scope | This is a Medicare Advantage premium-rate shock, not a hospital fee schedule or drug price. Cigna sold its Medicare businesses. |
| HCA | outside_scope | This is a Medicare Advantage premium-rate shock, not a hospital fee schedule or drug price. Cigna sold its Medicare businesses. |
| THC | outside_scope | This is a Medicare Advantage premium-rate shock, not a hospital fee schedule or drug price. Cigna sold its Medicare businesses. |
| UHS | outside_scope | This is a Medicare Advantage premium-rate shock, not a hospital fee schedule or drug price. Cigna sold its Medicare businesses. |
| TMO | outside_scope | This is a Medicare Advantage premium-rate shock, not a hospital fee schedule or drug price. Cigna sold its Medicare businesses. |
| ABT | outside_scope | This is a Medicare Advantage premium-rate shock, not a hospital fee schedule or drug price. Cigna sold its Medicare businesses. |
| MDT | outside_scope | This is a Medicare Advantage premium-rate shock, not a hospital fee schedule or drug price. Cigna sold its Medicare businesses. |
| CAH | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| COR | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| ISRG | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| MCK | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |

## B. Every in-scope exposure

Exact numeric checks are distinguished from filing links and estimates. UNVERIFIED values are retained, not silently replaced. Historical observed low/high values are not forecast confidence intervals.

| Company | Exposure | Base | Low | High | Exact-source status | Primary source / location / rationale |
|---|---|---:|---:|---:|---|---|
| UNH | medicare_advantage_revenue_share | 0.34 | 0.3 | 0.38 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/731766/000073176626000062/unh-20251231.htm · UnitedHealth 2025 10-K: UnitedHealthcare Medicare & Retirement revenue $171,285M of $447,567M total (38%); 8.4M MA members. M&R also includes PDP and Medicare Supplement, so the MA-only share is set below 38%.; MA-only split is not disclosed; PDP + Med Supp assumed ~10% of M&R revenue. · MA-only split is not disclosed; PDP + Med Supp assumed ~10% of M&R revenue. |
| ELV | medicare_advantage_revenue_share | 0.15 | 0.12 | 0.19 | UNVERIFIED | No source URL · estimate; Elevance 2025 10-K: 2,230K Medicare Advantage members of 45,232K medical members; at roughly $13–16K premium per MA member that is ~$30B of $199,125M revenue. Premium split by line not found in the filing text read. · Elevance 2025 10-K: 2,230K Medicare Advantage members of 45,232K medical members; at roughly $13–16K premium per MA member that is ~$30B of $199,125M revenue. Premium split by line not found in the filing text read. |
| HUM | medicare_advantage_revenue_share | 0.767 | 0.75 | 0.77 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/49071/000004907126000009/hum-20251231.htm · Humana 2025 10-K: individual MA premiums $90,403M + group MA $9,014M = $99,417M, 77% of $129,664M revenue (70.3% + 7.0% of consolidated premiums and services revenue);  · unavailable |
| CVS | medicare_advantage_revenue_share | 0.14 | 0.12 | 0.158 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/64803/000006480326000010/cvs-20251231.htm · CVS 2025 10-K: Health Care Benefits revenue from the federal government ~20% of consolidated revenue, of which Medicare contracts with CMS ~79% (=15.8% of revenue, incl. PDP); 4,267K MA members at Dec 31 2025 (Q4 2025 release); PDP premiums are removed from the 15.8% CMS share to get an MA-only base. · PDP premiums are removed from the 15.8% CMS share to get an MA-only base. |
| CNC | medicare_advantage_revenue_share | 0.06 | 0.03 | 0.1 | UNVERIFIED | https://investors.centene.com/2026-02-06-CENTENE-CORPORATION-REPORTS-2025-RESULTS-AND-ANNOUNCES-2026-GUIDANCE · estimate; Company-specific estimate: Medicare segment includes a large standalone Part D business; its full revenue is not MA exposure. Use 6% of total revenue (3–10%) as an explicitly estimated MA premium share pending a separated revenue disclosure. · Company-specific estimate: Medicare segment includes a large standalone Part D business; its full revenue is not MA exposure. Use 6% of total revenue (3–10%) as an explicitly estimated MA premium share pending a separated revenue disclosure. |
| MOH | medicare_advantage_revenue_share | 0.1372562 | 0.13039339 | 0.14411901 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1179929/000117992926000005/moh-20251231.htm · estimate; Medicare segment premium revenue $6,235M / total revenue $45,426M is used as an MA exposure proxy; no pure MA revenue cross-tab is asserted. Low/high are a ±5% relative modeling sensitivity, not reported confidence bounds. · Medicare segment premium revenue $6,235M / total revenue $45,426M is used as an MA exposure proxy; no pure MA revenue cross-tab is asserted. Low/high are a ±5% relative modeling sensitivity, not reported confidence bounds. |

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
| assumption.offset_share | -0.02961217 | -0.0064539345 | 0.023158235 |
| exposure.medicare_advantage_revenue_share | -0.015489001 | -0.019503431 | 0.0040144296 |

Dominant configured driver: `offset_share` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.

- REVIEW HUM: EPS -62.8%; Reported EPS denominator 9.84; dominant NI channel: Medicare Advantage payment rates; estimated exposures: none labeled estimate. Review reported earnings, exposure denominator and linear transmission before use. Default scenario; realistic range not independently verified.

## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 6 unchecked in-scope exposure values; 1 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

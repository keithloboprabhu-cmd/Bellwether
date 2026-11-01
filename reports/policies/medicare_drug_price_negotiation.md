# Medicare drug price negotiation

Policy `healthcare/medicare_drug_price_negotiation` · evidence checkpoint 2026-11-01 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

Negotiated Medicare prices (IRA program) cut net prices on selected drugs. Pfizer (Eliquis, Ibrance, Xtandi, Xeljanz) and Lilly (Jardiance, Tradjenta, Trulicity, Verzenio) lose revenue on their Medicare sales; insurers' Part D effects are bid through and not modelled.

Duration: `permanent`. Default inputs: `{"net_price_cut_pct": 30.0}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| price | unavailable / unavailable | {"d_price": "-input.net_price_cut_pct / 100", "exposed_revenue_share": "exposure.negotiated_drug_medicare_revenue_share", "offset_share": "assumption.volume_offset"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://www.cms.gov/newsroom/press-releases/cms-delivers-savings-seniors-15-major-drugs-cancer-chronic-disease
- https://www.milliman.com/en-GB/insight/key-takeaways-third-medicare-drug-price-negotiation

| Company | Configured status | Basis |
|---|---|---|
| UNH | outside_scope | The manufacturer net-price channel requires exposed Medicare drugs. Plan savings, pharmacy reimbursement, hospital billing and medical devices need separate models. |
| ELV | outside_scope | The manufacturer net-price channel requires exposed Medicare drugs. Plan savings, pharmacy reimbursement, hospital billing and medical devices need separate models. |
| HUM | outside_scope | The manufacturer net-price channel requires exposed Medicare drugs. Plan savings, pharmacy reimbursement, hospital billing and medical devices need separate models. |
| CVS | outside_scope | The manufacturer net-price channel requires exposed Medicare drugs. Plan savings, pharmacy reimbursement, hospital billing and medical devices need separate models. |
| PFE | included | Lower net prices on exposed Medicare drugs reduce manufacturer revenue. |
| LLY | included | Lower net prices on exposed Medicare drugs reduce manufacturer revenue. |
| CI | outside_scope | The manufacturer net-price channel requires exposed Medicare drugs. Plan savings, pharmacy reimbursement, hospital billing and medical devices need separate models. |
| CNC | outside_scope | The manufacturer net-price channel requires exposed Medicare drugs. Plan savings, pharmacy reimbursement, hospital billing and medical devices need separate models. |
| MOH | outside_scope | The manufacturer net-price channel requires exposed Medicare drugs. Plan savings, pharmacy reimbursement, hospital billing and medical devices need separate models. |
| JNJ | included | Lower net prices on exposed Medicare drugs reduce manufacturer revenue. |
| MRK | included | Lower net prices on exposed Medicare drugs reduce manufacturer revenue. |
| ABBV | included | Lower net prices on exposed Medicare drugs reduce manufacturer revenue. |
| AMGN | included | Lower net prices on exposed Medicare drugs reduce manufacturer revenue. |
| GILD | included | Lower net prices on exposed Medicare drugs reduce manufacturer revenue. |
| HCA | outside_scope | The manufacturer net-price channel requires exposed Medicare drugs. Plan savings, pharmacy reimbursement, hospital billing and medical devices need separate models. |
| THC | outside_scope | The manufacturer net-price channel requires exposed Medicare drugs. Plan savings, pharmacy reimbursement, hospital billing and medical devices need separate models. |
| UHS | outside_scope | The manufacturer net-price channel requires exposed Medicare drugs. Plan savings, pharmacy reimbursement, hospital billing and medical devices need separate models. |
| TMO | outside_scope | The manufacturer net-price channel requires exposed Medicare drugs. Plan savings, pharmacy reimbursement, hospital billing and medical devices need separate models. |
| ABT | outside_scope | The manufacturer net-price channel requires exposed Medicare drugs. Plan savings, pharmacy reimbursement, hospital billing and medical devices need separate models. |
| MDT | outside_scope | The manufacturer net-price channel requires exposed Medicare drugs. Plan savings, pharmacy reimbursement, hospital billing and medical devices need separate models. |
| CAH | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| COR | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| ISRG | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| MCK | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |

## B. Every in-scope exposure

Exact numeric checks are distinguished from filing links and estimates. UNVERIFIED values are retained, not silently replaced. Historical observed low/high values are not forecast confidence intervals.

| Company | Exposure | Base | Low | High | Exact-source status | Primary source / location / rationale |
|---|---|---:|---:|---:|---|---|
| PFE | negotiated_drug_medicare_revenue_share | 0.08 | 0.05 | 0.12 | UNVERIFIED | https://www.milliman.com/en-GB/insight/key-takeaways-third-medicare-drug-price-negotiation · estimate; Selected Pfizer drugs: Eliquis (IPAY 2026, BMS alliance), Ibrance and Xtandi (IPAY 2027; 2027 MFPs roughly half of 2024 list), Xeljanz (IPAY 2028, $1.0B Medicare spend per Milliman). Medicare net sales of these assumed ~$4–7B of $62,579M revenue. · Selected Pfizer drugs: Eliquis (IPAY 2026, BMS alliance), Ibrance and Xtandi (IPAY 2027; 2027 MFPs roughly half of 2024 list), Xeljanz (IPAY 2028, $1.0B Medicare spend per Milliman). Medicare net sales of these assumed ~$4–7B of $62,579M revenue. |
| LLY | negotiated_drug_medicare_revenue_share | 0.05 | 0.03 | 0.08 | UNVERIFIED | https://www.milliman.com/en-GB/insight/key-takeaways-third-medicare-drug-price-negotiation · estimate; Selected Lilly drugs: Jardiance (IPAY 2026) and Tradjenta (IPAY 2027, renegotiated for 2028) via the Boehringer alliance; Trulicity ($4.9B Medicare gross spend) and Verzenio ($1.4B) on the IPAY 2028 list per Milliman. Net Medicare sales assumed ~$2–5B of $65,179M revenue. · Selected Lilly drugs: Jardiance (IPAY 2026) and Tradjenta (IPAY 2027, renegotiated for 2028) via the Boehringer alliance; Trulicity ($4.9B Medicare gross spend) and Verzenio ($1.4B) on the IPAY 2028 list per Milliman. Net Medicare sales assumed ~$2–5B of $65,179M revenue. |
| JNJ | negotiated_drug_medicare_revenue_share | 0.065 | 0.03 | 0.12 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Pharmaceuticals and biotechnology; median base and outer low/high from PFE/LLY in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Pharmaceuticals and biotechnology; median base and outer low/high from PFE/LLY in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| MRK | negotiated_drug_medicare_revenue_share | 0.065 | 0.03 | 0.12 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Pharmaceuticals and biotechnology; median base and outer low/high from PFE/LLY in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Pharmaceuticals and biotechnology; median base and outer low/high from PFE/LLY in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| ABBV | negotiated_drug_medicare_revenue_share | 0.065 | 0.03 | 0.12 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Pharmaceuticals and biotechnology; median base and outer low/high from PFE/LLY in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Pharmaceuticals and biotechnology; median base and outer low/high from PFE/LLY in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| AMGN | negotiated_drug_medicare_revenue_share | 0.065 | 0.03 | 0.12 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Pharmaceuticals and biotechnology; median base and outer low/high from PFE/LLY in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Pharmaceuticals and biotechnology; median base and outer low/high from PFE/LLY in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| GILD | negotiated_drug_medicare_revenue_share | 0.065 | 0.03 | 0.12 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Pharmaceuticals and biotechnology; median base and outer low/high from PFE/LLY in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Pharmaceuticals and biotechnology; median base and outer low/high from PFE/LLY in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |

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
| exposure.negotiated_drug_medicare_revenue_share | -0.019884156 | -0.067920073 | 0.048035917 |
| assumption.volume_offset | -0.043212654 | -0.032409491 | 0.010803164 |

Dominant configured driver: `negotiated_drug_medicare_revenue_share` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.


## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 7 unchecked in-scope exposure values; 1 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

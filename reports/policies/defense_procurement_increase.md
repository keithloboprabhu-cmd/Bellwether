# Higher defense spending

Policy `industrials/defense_procurement_increase` · reviewed 2026-10-31 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

A bigger defense budget buys more military engines, avionics and spares. Honeywell and GE Aerospace, each with about a tenth of revenue from the Department of Defense, gain; the others have little defense business.

Duration: `permanent`. Default inputs: `{"d_budget_pct": 5.0}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| gov_budget | unavailable / unavailable | {"gov_revenue_share": "exposure.govcon_defense_intel_share", "d_budget_pct": "input.d_budget_pct / 100", "program_relevance": "assumption.hardware_capture"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://www.sec.gov/Archives/edgar/data/773840/000077384026000013/hon-20251231.htm
- https://www.sec.gov/Archives/edgar/data/40545/000004054526000008/ge-20251231.htm

| Company | Configured status | Basis |
|---|---|---|
| CAT | included | Higher defense procurement raises exposed suppliers revenue. |
| DE | outside_scope | No quantified defense/IC revenue share. Military demand through customer supply chains is not separately modeled. |
| GE | included | Higher defense procurement raises exposed suppliers revenue. |
| HON | included | Higher defense procurement raises exposed suppliers revenue. |
| MMM | included | Higher defense procurement raises exposed suppliers revenue. |
| NUE | outside_scope | No quantified defense/IC revenue share. Military demand through customer supply chains is not separately modeled. |
| BA | included | Higher defense procurement raises exposed suppliers revenue. |
| ETN | included | Higher defense procurement raises exposed suppliers revenue. |
| EMR | included | Higher defense procurement raises exposed suppliers revenue. |
| ITW | included | Higher defense procurement raises exposed suppliers revenue. |
| PH | included | Higher defense procurement raises exposed suppliers revenue. |
| CMI | included | Higher defense procurement raises exposed suppliers revenue. |
| PCAR | included | Higher defense procurement raises exposed suppliers revenue. |
| DOV | included | Higher defense procurement raises exposed suppliers revenue. |
| ROK | included | Higher defense procurement raises exposed suppliers revenue. |
| STLD | outside_scope | No quantified defense/IC revenue share. Military demand through customer supply chains is not separately modeled. |
| CLF | outside_scope | No quantified defense/IC revenue share. Military demand through customer supply chains is not separately modeled. |
| CARR | included | Higher defense procurement raises exposed suppliers revenue. |
| OTIS | included | Higher defense procurement raises exposed suppliers revenue. |
| IR | included | Higher defense procurement raises exposed suppliers revenue. |
| GEV | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |

## B. Every in-scope exposure

Exact numeric checks are distinguished from filing links and estimates. UNVERIFIED values are retained, not silently replaced. Historical observed low/high values are not forecast confidence intervals.

| Company | Exposure | Base | Low | High | Exact-source status | Primary source / location / rationale |
|---|---|---:|---:|---:|---|---|
| CAT | govcon_defense_intel_share | 0.01 | 0.005 | 0.02 | UNVERIFIED | No source URL · estimate; Caterpillar sells engines and machines to the US military but does not disclose government sales, implying they are small relative to $67.6B revenue. · Caterpillar sells engines and machines to the US military but does not disclose government sales, implying they are small relative to $67.6B revenue. |
| GE | govcon_defense_intel_share | 0.1 | 0.09 | 0.11 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/40545/000004054526000008/ge-20251231.htm · GE Aerospace 2025 10-K: sales of equipment and services to agencies of the U.S. Government were 10% of total revenue (12% in 2024, 14% in 2023); Almost all GE's US government sales are military engines and services (including foreign military sales through the US Air Force), so the government share approximates the defense share. · Almost all GE's US government sales are military engines and services (including foreign military sales through the US Air Force), so the government share approximates the defense share. |
| HON | govcon_defense_intel_share | 0.11 | 0.1 | 0.13 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/773840/000077384026000013/hon-20251231.htm · Honeywell 2025 10-K: sales to the U.S. Department of Defense $4,209M (as prime and subcontractor) of $37,442M net sales = 11.2%; total U.S. government sales $4,752M;  · unavailable |
| MMM | govcon_defense_intel_share | 0.01 | 0.005 | 0.02 | UNVERIFIED | No source URL · estimate; 3M sells safety and industrial products to the military but does not disclose government sales as material; 56% of 2025 revenue came from outside the US. · 3M sells safety and industrial products to the military but does not disclose government sales as material; 56% of 2025 revenue came from outside the US. |
| BA | govcon_defense_intel_share | 0.3 | 0.25 | 0.4 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/12927/000162828026004357/0001628280-26-004357-index.htm · estimate; Company-specific estimate: Defense, Space & Security is a material Boeing business. Estimate 30% of consolidated revenue (25–40%) for defense/IC procurement rather than a 1% mixed-industrial median. · Company-specific estimate: Defense, Space & Security is a material Boeing business. Estimate 30% of consolidated revenue (25–40%) for defense/IC procurement rather than a 1% mixed-industrial median. |
| ETN | govcon_defense_intel_share | 0.06 | 0.03 | 0.1 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1551182/000155118226000007/0001551182-26-000007-index.htm · estimate; Company-specific estimate: Eaton aerospace has military customers alongside commercial and electrical businesses; estimate 6% defense/IC revenue (3–10%). · Company-specific estimate: Eaton aerospace has military customers alongside commercial and electrical businesses; estimate 6% defense/IC revenue (3–10%). |
| EMR | govcon_defense_intel_share | 0.01 | 0 | 0.13 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| ITW | govcon_defense_intel_share | 0.01 | 0 | 0.13 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| PH | govcon_defense_intel_share | 0.08 | 0.04 | 0.15 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/76334/000007633426000105/0000076334-26-000105-index.htm · estimate; Company-specific estimate: Parker aerospace includes military systems; estimate 8% defense/IC revenue (4–15%) instead of the generic 1% industrial median. · Company-specific estimate: Parker aerospace includes military systems; estimate 8% defense/IC revenue (4–15%) instead of the generic 1% industrial median. |
| CMI | govcon_defense_intel_share | 0.01 | 0 | 0.13 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| PCAR | govcon_defense_intel_share | 0.01 | 0 | 0.13 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| DOV | govcon_defense_intel_share | 0.01 | 0 | 0.13 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| ROK | govcon_defense_intel_share | 0.01 | 0 | 0.13 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| CARR | govcon_defense_intel_share | 0.01 | 0 | 0.13 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| OTIS | govcon_defense_intel_share | 0.01 | 0 | 0.13 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| IR | govcon_defense_intel_share | 0.01 | 0 | 0.13 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |

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
| exposure.govcon_defense_intel_share | 0.0028719212 | 0.0090289217 | 0.0061570006 |
| assumption.hardware_capture | 0.0022144848 | 0.0053147634 | 0.0031002787 |

Dominant configured driver: `govcon_defense_intel_share` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.


## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 16 unchecked in-scope exposure values; 1 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

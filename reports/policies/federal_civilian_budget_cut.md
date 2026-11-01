# Federal civilian budget cut

Policy `public_sector/federal_civilian_budget_cut` · reviewed 2026-10-31 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

A cut to non-defense discretionary appropriations shrinks civilian-agency contract spending; contractors with large civil portfolios (Leidos, Booz Allen, SAIC) lose the most, defense-heavy General Dynamics the least.

Duration: `permanent`. Default inputs: `{"d_budget_pct": -5.0}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| gov_budget | unavailable / unavailable | {"gov_revenue_share": "exposure.govcon_civilian_share", "d_budget_pct": "input.d_budget_pct / 100", "program_relevance": "assumption.contract_beta"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://www.sec.gov/Archives/edgar/data/1336920/000133692026000030/ldos-20260102.htm
- https://www.sec.gov/Archives/edgar/data/1443646/000162828026037521/bah-20260331.htm

| Company | Configured status | Basis |
|---|---|---|
| BAH | included | Civilian budget cuts reduce exposed federal demand. |
| LDOS | included | Civilian budget cuts reduce exposed federal demand. |
| SAIC | included | Civilian budget cuts reduce exposed federal demand. |
| CACI | included | Civilian budget cuts reduce exposed federal demand. |
| PSN | included | Civilian budget cuts reduce exposed federal demand. |
| GD | included | Civilian budget cuts reduce exposed federal demand. |
| LMT | included | Civilian budget cuts reduce exposed federal demand. |
| NOC | included | Civilian budget cuts reduce exposed federal demand. |
| RTX | included | Civilian budget cuts reduce exposed federal demand. |
| HII | included | Civilian budget cuts reduce exposed federal demand. |
| OSK | included | Civilian budget cuts reduce exposed federal demand. |
| KBR | included | Civilian budget cuts reduce exposed federal demand. |
| KTOS | included | Civilian budget cuts reduce exposed federal demand. |
| AVAV | included | Civilian budget cuts reduce exposed federal demand. |
| BWXT | included | Civilian budget cuts reduce exposed federal demand. |
| TXT | included | Civilian budget cuts reduce exposed federal demand. |
| ICFI | included | Civilian budget cuts reduce exposed federal demand. |
| TTEK | included | Civilian budget cuts reduce exposed federal demand. |
| MRCY | included | Civilian budget cuts reduce exposed federal demand. |
| VSEC | included | Civilian budget cuts reduce exposed federal demand. |

## B. Every in-scope exposure

Exact numeric checks are distinguished from filing links and estimates. UNVERIFIED values are retained, not silently replaced. Historical observed low/high values are not forecast confidence intervals.

| Company | Exposure | Base | Low | High | Exact-source status | Primary source / location / rationale |
|---|---|---:|---:|---:|---|---|
| BAH | govcon_civilian_share | 0.27 | 0.25 | 0.29 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1443646/000162828026037521/bah-20260331.htm · Booz Allen FY2026 10-K, Note 3: Civil and Commercial customers $3,248M (29%) of revenue; ~2% is non-US-government (98% US gov), leaving ~27% civil agencies;  · unavailable |
| LDOS | govcon_civilian_share | 0.377 | 0.35 | 0.39 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1336920/000133692026000030/ldos-20260102.htm · Leidos FY2025 10-K revenue disaggregation: Other U.S. government agencies $6,458M of $17,107M (37.7%);  · unavailable |
| SAIC | govcon_civilian_share | 0.23 | 0.2 | 0.26 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1571123/000157112326000029/saic-20260130.htm · SAIC FY2026 10-K: Civilian segment revenues $1,681M of $7,262M (23%);  · unavailable |
| CACI | govcon_civilian_share | 0.174 | 0.166 | 0.18 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/16058/000162828026054195/caci-20260630.htm · CACI FY2026 10-K: Federal civilian agencies $1,661M (17.4%) of revenue (16.6% FY2025);  · unavailable |
| PSN | govcon_civilian_share | 0.2 | 0.12 | 0.22 | UNVERIFIED | No source URL · estimate; Federal revenue 51% (10-K) minus Defense & Intelligence 29% leaves ≤22% for civil agencies (FAA, DOE, State); part of Engineered Systems is defense. · Federal revenue 51% (10-K) minus Defense & Intelligence 29% leaves ≤22% for civil agencies (FAA, DOE, State); part of Engineered Systems is defense. |
| GD | govcon_civilian_share | 0.07 | 0.04 | 0.094 | UNVERIFIED | No source URL · estimate; 10-K shows non-DoW U.S. government revenue of $4,954M (9.4% of revenue), which includes the intelligence community; civil agencies are the larger part (mainly GDIT). · 10-K shows non-DoW U.S. government revenue of $4,954M (9.4% of revenue), which includes the intelligence community; civil agencies are the larger part (mainly GDIT). |
| LMT | govcon_civilian_share | 0.07 | 0.04 | 0.094 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| NOC | govcon_civilian_share | 0.07 | 0.04 | 0.094 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| RTX | govcon_civilian_share | 0.07 | 0.04 | 0.094 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| HII | govcon_civilian_share | 0.07 | 0.04 | 0.094 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| OSK | govcon_civilian_share | 0.07 | 0.04 | 0.094 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| KBR | govcon_civilian_share | 0.23 | 0.12 | 0.39 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Government engineering and advisory; median base and outer low/high from BAH/LDOS/SAIC/CACI/PSN in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Government engineering and advisory; median base and outer low/high from BAH/LDOS/SAIC/CACI/PSN in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| KTOS | govcon_civilian_share | 0.07 | 0.04 | 0.094 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| AVAV | govcon_civilian_share | 0.07 | 0.04 | 0.094 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| BWXT | govcon_civilian_share | 0.07 | 0.04 | 0.094 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| TXT | govcon_civilian_share | 0.07 | 0.04 | 0.094 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| ICFI | govcon_civilian_share | 0.23 | 0.12 | 0.39 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Government engineering and advisory; median base and outer low/high from BAH/LDOS/SAIC/CACI/PSN in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Government engineering and advisory; median base and outer low/high from BAH/LDOS/SAIC/CACI/PSN in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| TTEK | govcon_civilian_share | 0.23 | 0.12 | 0.39 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Government engineering and advisory; median base and outer low/high from BAH/LDOS/SAIC/CACI/PSN in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Government engineering and advisory; median base and outer low/high from BAH/LDOS/SAIC/CACI/PSN in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| MRCY | govcon_civilian_share | 0.07 | 0.04 | 0.094 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| VSEC | govcon_civilian_share | 0.07 | 0.04 | 0.094 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |

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
| assumption.contract_beta | -0.006969736 | -0.01742434 | 0.010454604 |
| exposure.govcon_civilian_share | -0.0079614698 | -0.015054148 | 0.0070926778 |

Dominant configured driver: `contract_beta` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.


## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 20 unchecked in-scope exposure values; 1 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

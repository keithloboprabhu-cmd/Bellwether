# Tariffs on imported pharmaceuticals

Policy `healthcare/pharma_tariffs` · reviewed 2026-10-31 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

A US tariff on imported branded drugs and ingredients raises Pfizer's and Lilly's cost of US-sold product; company deals with the administration and new US plants shield part of it. Insurers' indirect cost from higher drug prices is not modelled.

Duration: `permanent`. Default inputs: `{"tariff_pct": 15.0}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| cost | unavailable / ['importer'] | {"exposed_cost_share": "exposure.pharma_import_share_of_cogs", "shock_pct": "input.tariff_pct / 100 * (1 - assumption.exempt_share)", "pass_through": "assumption.pass_through", "elasticity": "assumption.elasticity"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://www.aeaweb.org/articles?id=10.1257/aeri.20190536

| Company | Configured status | Basis |
|---|---|---|
| UNH | outside_scope | This tariff covers branded drugs/API, not devices, diagnostics or instruments. Insurer supplier-cost spillovers are outside the direct importer channel. |
| ELV | outside_scope | This tariff covers branded drugs/API, not devices, diagnostics or instruments. Insurer supplier-cost spillovers are outside the direct importer channel. |
| HUM | outside_scope | This tariff covers branded drugs/API, not devices, diagnostics or instruments. Insurer supplier-cost spillovers are outside the direct importer channel. |
| CVS | outside_scope | This tariff covers branded drugs/API, not devices, diagnostics or instruments. Insurer supplier-cost spillovers are outside the direct importer channel. |
| PFE | included | Drug/API import tariffs raise exposed pharmaceutical costs. |
| LLY | included | Drug/API import tariffs raise exposed pharmaceutical costs. |
| CI | outside_scope | This tariff covers branded drugs/API, not devices, diagnostics or instruments. Insurer supplier-cost spillovers are outside the direct importer channel. |
| CNC | outside_scope | This tariff covers branded drugs/API, not devices, diagnostics or instruments. Insurer supplier-cost spillovers are outside the direct importer channel. |
| MOH | outside_scope | This tariff covers branded drugs/API, not devices, diagnostics or instruments. Insurer supplier-cost spillovers are outside the direct importer channel. |
| JNJ | included | Drug/API import tariffs raise exposed pharmaceutical costs. |
| MRK | included | Drug/API import tariffs raise exposed pharmaceutical costs. |
| ABBV | included | Drug/API import tariffs raise exposed pharmaceutical costs. |
| AMGN | included | Drug/API import tariffs raise exposed pharmaceutical costs. |
| GILD | included | Drug/API import tariffs raise exposed pharmaceutical costs. |
| HCA | outside_scope | This tariff covers branded drugs/API, not devices, diagnostics or instruments. Insurer supplier-cost spillovers are outside the direct importer channel. |
| THC | outside_scope | This tariff covers branded drugs/API, not devices, diagnostics or instruments. Insurer supplier-cost spillovers are outside the direct importer channel. |
| UHS | outside_scope | This tariff covers branded drugs/API, not devices, diagnostics or instruments. Insurer supplier-cost spillovers are outside the direct importer channel. |
| TMO | outside_scope | This tariff covers branded drugs/API, not devices, diagnostics or instruments. Insurer supplier-cost spillovers are outside the direct importer channel. |
| ABT | outside_scope | This tariff covers branded drugs/API, not devices, diagnostics or instruments. Insurer supplier-cost spillovers are outside the direct importer channel. |
| MDT | outside_scope | This tariff covers branded drugs/API, not devices, diagnostics or instruments. Insurer supplier-cost spillovers are outside the direct importer channel. |
| CAH | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| COR | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| ISRG | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| MCK | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |

## B. Every in-scope exposure

Exact numeric checks are distinguished from filing links and estimates. UNVERIFIED values are retained, not silently replaced. Historical observed low/high values are not forecast confidence intervals.

| Company | Exposure | Base | Low | High | Exact-source status | Primary source / location / rationale |
|---|---|---:|---:|---:|---|---|
| PFE | pharma_import_share_of_cogs | 0.3 | 0.2 | 0.45 | UNVERIFIED | No source URL · estimate; Roughly 60% of Pfizer sales are US and a large share of branded supply is made in Ireland, Belgium and other EU sites; about half of US-sold product cost assumed imported. · Roughly 60% of Pfizer sales are US and a large share of branded supply is made in Ireland, Belgium and other EU sites; about half of US-sold product cost assumed imported. |
| LLY | pharma_import_share_of_cogs | 0.3 | 0.2 | 0.45 | UNVERIFIED | No source URL · estimate; About two-thirds of Lilly sales are US; much incretin and API supply has come from Ireland and other EU sites while new US plants ramp; about half of US-sold product cost assumed imported. · About two-thirds of Lilly sales are US; much incretin and API supply has come from Ireland and other EU sites while new US plants ramp; about half of US-sold product cost assumed imported. |
| JNJ | pharma_import_share_of_cogs | 0.3 | 0.2 | 0.45 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Pharmaceuticals and biotechnology; median base and outer low/high from PFE/LLY in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Pharmaceuticals and biotechnology; median base and outer low/high from PFE/LLY in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| MRK | pharma_import_share_of_cogs | 0.3 | 0.2 | 0.45 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Pharmaceuticals and biotechnology; median base and outer low/high from PFE/LLY in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Pharmaceuticals and biotechnology; median base and outer low/high from PFE/LLY in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| ABBV | pharma_import_share_of_cogs | 0.3 | 0.2 | 0.45 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Pharmaceuticals and biotechnology; median base and outer low/high from PFE/LLY in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Pharmaceuticals and biotechnology; median base and outer low/high from PFE/LLY in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| AMGN | pharma_import_share_of_cogs | 0.3 | 0.2 | 0.45 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Pharmaceuticals and biotechnology; median base and outer low/high from PFE/LLY in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Pharmaceuticals and biotechnology; median base and outer low/high from PFE/LLY in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| GILD | pharma_import_share_of_cogs | 0.3 | 0.2 | 0.45 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Pharmaceuticals and biotechnology; median base and outer low/high from PFE/LLY in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Pharmaceuticals and biotechnology; median base and outer low/high from PFE/LLY in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |

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
| assumption.exempt_share | -0.021850695 | -0.0043718159 | 0.017478879 |
| exposure.pharma_import_share_of_cogs | -0.0087427933 | -0.019666568 | 0.010923775 |
| assumption.pass_through | -0.015823086 | -0.0090512394 | 0.0067718463 |
| assumption.elasticity | -0.0128857 | -0.013567396 | 0.00068169549 |

Dominant configured driver: `exempt_share` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.


## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 7 unchecked in-scope exposure values; 3 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

# Government shutdown

Policy `public_sector/government_shutdown` · evidence checkpoint 2026-11-01 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

A lapse in appropriations stops non-excepted contract work; part of the lost revenue is made up after the shutdown ends. Services contractors paid from annual funds are hit; GD's multi-year-funded production mostly keeps running.

Duration: `one_time`. Default inputs: `{"days": 35.0}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| gov_shutdown | unavailable / unavailable | {"gov_revenue_share": "exposure.govcon_services_share", "days": "input.days", "affected_share": "assumption.affected_share", "recovery_share": "assumption.recovery_share"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://www.sec.gov/Archives/edgar/data/1443646/000162828026003186/finalbahexhibit991q3fy26.htm
- https://www.sec.gov/Archives/edgar/data/1571123/000157112326000029/saic-20260130.htm
- https://www.sec.gov/Archives/edgar/data/40533/000004053326000006/gd-20251231.htm

| Company | Configured status | Basis |
|---|---|---|
| BAH | included | Unrecovered service revenue is lost during a shutdown. |
| LDOS | included | Unrecovered service revenue is lost during a shutdown. |
| SAIC | included | Unrecovered service revenue is lost during a shutdown. |
| CACI | included | Unrecovered service revenue is lost during a shutdown. |
| PSN | included | Unrecovered service revenue is lost during a shutdown. |
| GD | included | Unrecovered service revenue is lost during a shutdown. |
| LMT | included | Unrecovered service revenue is lost during a shutdown. |
| NOC | included | Unrecovered service revenue is lost during a shutdown. |
| RTX | included | Unrecovered service revenue is lost during a shutdown. |
| HII | included | Unrecovered service revenue is lost during a shutdown. |
| OSK | included | Unrecovered service revenue is lost during a shutdown. |
| KBR | included | Unrecovered service revenue is lost during a shutdown. |
| KTOS | included | Unrecovered service revenue is lost during a shutdown. |
| AVAV | included | Unrecovered service revenue is lost during a shutdown. |
| BWXT | included | Unrecovered service revenue is lost during a shutdown. |
| TXT | included | Unrecovered service revenue is lost during a shutdown. |
| ICFI | included | Unrecovered service revenue is lost during a shutdown. |
| TTEK | included | Unrecovered service revenue is lost during a shutdown. |
| MRCY | included | Unrecovered service revenue is lost during a shutdown. |
| VSEC | included | Unrecovered service revenue is lost during a shutdown. |

## B. Every in-scope exposure

Exact numeric checks are distinguished from filing links and estimates. UNVERIFIED values are retained, not silently replaced. Historical observed low/high values are not forecast confidence intervals.

| Company | Exposure | Base | Low | High | Exact-source status | Primary source / location / rationale |
|---|---|---:|---:|---:|---|---|
| BAH | govcon_services_share | 0.98 | 0.95 | 0.98 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1443646/000162828026037521/bah-20260331.htm · Booz Allen FY2026 10-K: substantially all revenue is from services under U.S. government contracts; ~98% from the U.S. government;  · unavailable |
| LDOS | govcon_services_share | 0.75 | 0.7 | 0.85 | UNVERIFIED | No source URL · estimate; 87% US-government revenue (10-K) less most of the Defense Systems segment (13% of revenue, hardware and production programs) and some security-product sales. · 87% US-government revenue (10-K) less most of the Defense Systems segment (13% of revenue, hardware and production programs) and some security-product sales. |
| SAIC | govcon_services_share | 0.98 | 0.95 | 0.98 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1571123/000157112326000029/saic-20260130.htm · SAIC FY2026 10-K: 98% of revenues from U.S. government contracts; SAIC is a technology-integration and services provider;  · unavailable |
| CACI | govcon_services_share | 0.9 | 0.85 | 0.956 | UNVERIFIED | No source URL · estimate; 95.6% federal revenue (10-K), less technology products and work funded from multi-year procurement/RDT&E money that keeps flowing in a lapse. · 95.6% federal revenue (10-K), less technology products and work funded from multi-year procurement/RDT&E money that keeps flowing in a lapse. |
| PSN | govcon_services_share | 0.51 | 0.45 | 0.51 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/275880/000119312526045495/psn-20251231.htm · Parsons FY2025 10-K: ~51% of revenue from the U.S. federal government (Federal Solutions); low end allows for multi-year-funded engineered systems;  · unavailable |
| GD | govcon_services_share | 0.2 | 0.15 | 0.26 | UNVERIFIED | No source URL · estimate; Technologies segment (GDIT + Mission Systems) is $13,471M, 26% of revenue (10-K), mostly US government; shipbuilding, combat vehicles and munitions are multi-year-funded production that continues through a lapse. GD says only its IT services business was 'somewhat impacted' by the 2025 shutdown. · Technologies segment (GDIT + Mission Systems) is $13,471M, 26% of revenue (10-K), mostly US government; shipbuilding, combat vehicles and munitions are multi-year-funded production that continues through a lapse. GD says only its IT services business was 'somewhat impacted' by the 2025 shutdown. |
| LMT | govcon_services_share | 0.2 | 0.15 | 0.26 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| NOC | govcon_services_share | 0.2 | 0.15 | 0.26 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| RTX | govcon_services_share | 0.2 | 0.15 | 0.26 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| HII | govcon_services_share | 0.2 | 0.15 | 0.26 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| OSK | govcon_services_share | 0.2 | 0.15 | 0.26 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| KBR | govcon_services_share | 0.9 | 0.45 | 0.98 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Government engineering and advisory; median base and outer low/high from BAH/LDOS/SAIC/CACI/PSN in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Government engineering and advisory; median base and outer low/high from BAH/LDOS/SAIC/CACI/PSN in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| KTOS | govcon_services_share | 0.2 | 0.15 | 0.26 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| AVAV | govcon_services_share | 0.2 | 0.15 | 0.26 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| BWXT | govcon_services_share | 0.2 | 0.15 | 0.26 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| TXT | govcon_services_share | 0.2 | 0.15 | 0.26 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| ICFI | govcon_services_share | 0.9 | 0.45 | 0.98 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Government engineering and advisory; median base and outer low/high from BAH/LDOS/SAIC/CACI/PSN in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Government engineering and advisory; median base and outer low/high from BAH/LDOS/SAIC/CACI/PSN in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| TTEK | govcon_services_share | 0.9 | 0.45 | 0.98 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Government engineering and advisory; median base and outer low/high from BAH/LDOS/SAIC/CACI/PSN in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Government engineering and advisory; median base and outer low/high from BAH/LDOS/SAIC/CACI/PSN in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| MRCY | govcon_services_share | 0.2 | 0.15 | 0.26 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| VSEC | govcon_services_share | 0.2 | 0.15 | 0.26 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Defense platforms and equipment; median base and outer low/high from GD in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |

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
| assumption.affected_share | -0.0011305076 | -0.0042394034 | 0.0031088958 |
| assumption.recovery_share | -0.0037369556 | -0.0016015524 | 0.0021354032 |
| exposure.govcon_services_share | -0.001940101 | -0.0028137566 | 0.0008736556 |

Dominant configured driver: `affected_share` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.


## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 20 unchecked in-scope exposure values; 2 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

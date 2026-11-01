# Consulting contract cancellations

Policy `public_sector/consulting_contract_cancellations` · reviewed 2026-10-31 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

An efficiency drive (like the 2025 DOGE/GSA review of consulting contracts) cancels part of the federal management-consulting and advisory portfolio. Booz Allen is by far the most exposed; only separately identified advisory/services businesses are exposed; hardware-only contract revenue is outside this cancellation channel.

Duration: `years:4`. Default inputs: `{"cut_pct": 15.0}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| gov_budget | unavailable / unavailable | {"gov_revenue_share": "exposure.govcon_advisory_share", "d_budget_pct": "-(input.cut_pct / 100) * (1 - assumption.replacement_offset)"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://www.sec.gov/Archives/edgar/data/1443646/000162828026037521/bah-20260331.htm
- https://www.sec.gov/Archives/edgar/data/40533/000004053326000006/gd-20251231.htm

| Company | Configured status | Basis |
|---|---|---|
| BAH | included | Canceled federal advisory contracts reduce exposed revenue. |
| LDOS | included | Canceled federal advisory contracts reduce exposed revenue. |
| SAIC | included | Canceled federal advisory contracts reduce exposed revenue. |
| CACI | included | Canceled federal advisory contracts reduce exposed revenue. |
| PSN | included | Canceled federal advisory contracts reduce exposed revenue. |
| GD | included | Canceled federal advisory contracts reduce exposed revenue. |
| LMT | outside_scope | The selected policy cancels management-consulting/advisory scope; weapons, ship, drone, truck, aircraft and nuclear-component purchases are not consulting task orders. |
| NOC | outside_scope | The selected policy cancels management-consulting/advisory scope; weapons, ship, drone, truck, aircraft and nuclear-component purchases are not consulting task orders. |
| RTX | outside_scope | The selected policy cancels management-consulting/advisory scope; weapons, ship, drone, truck, aircraft and nuclear-component purchases are not consulting task orders. |
| HII | outside_scope | The selected policy cancels management-consulting/advisory scope; weapons, ship, drone, truck, aircraft and nuclear-component purchases are not consulting task orders. |
| OSK | outside_scope | The selected policy cancels management-consulting/advisory scope; weapons, ship, drone, truck, aircraft and nuclear-component purchases are not consulting task orders. |
| KBR | included | Canceled federal advisory contracts reduce exposed revenue. |
| KTOS | outside_scope | The selected policy cancels management-consulting/advisory scope; weapons, ship, drone, truck, aircraft and nuclear-component purchases are not consulting task orders. |
| AVAV | outside_scope | The selected policy cancels management-consulting/advisory scope; weapons, ship, drone, truck, aircraft and nuclear-component purchases are not consulting task orders. |
| BWXT | outside_scope | The selected policy cancels management-consulting/advisory scope; weapons, ship, drone, truck, aircraft and nuclear-component purchases are not consulting task orders. |
| TXT | outside_scope | The selected policy cancels management-consulting/advisory scope; weapons, ship, drone, truck, aircraft and nuclear-component purchases are not consulting task orders. |
| ICFI | included | Canceled federal advisory contracts reduce exposed revenue. |
| TTEK | included | Canceled federal advisory contracts reduce exposed revenue. |
| MRCY | outside_scope | The selected policy cancels management-consulting/advisory scope; weapons, ship, drone, truck, aircraft and nuclear-component purchases are not consulting task orders. |
| VSEC | outside_scope | The selected policy cancels management-consulting/advisory scope; weapons, ship, drone, truck, aircraft and nuclear-component purchases are not consulting task orders. |

## B. Every in-scope exposure

Exact numeric checks are distinguished from filing links and estimates. UNVERIFIED values are retained, not silently replaced. Historical observed low/high values are not forecast confidence intervals.

| Company | Exposure | Base | Low | High | Exact-source status | Primary source / location / rationale |
|---|---|---:|---:|---:|---|---|
| BAH | govcon_advisory_share | 0.3 | 0.2 | 0.45 | UNVERIFIED | No source URL · estimate; Booz Allen's management-consulting heritage makes it the most exposed name; its 10-K shows Civil & Commercial revenue fell from $4,170M to $3,248M (−22%) in FY2026 amid efficiency reviews and contract cancellations. Advisory work is a large part of civil plus some defense staff-support work. · Booz Allen's management-consulting heritage makes it the most exposed name; its 10-K shows Civil & Commercial revenue fell from $4,170M to $3,248M (−22%) in FY2026 amid efficiency reviews and contract cancellations. Advisory work is a large part of civil plus some defense staff-support work. |
| LDOS | govcon_advisory_share | 0.05 | 0.02 | 0.1 | UNVERIFIED | No source URL · estimate; Leidos is mainly IT, engineering, health-services and hardware; pure management-consulting task orders are a small slice. · Leidos is mainly IT, engineering, health-services and hardware; pure management-consulting task orders are a small slice. |
| SAIC | govcon_advisory_share | 0.05 | 0.02 | 0.1 | UNVERIFIED | No source URL · estimate; SAIC's work is mostly IT integration, engineering and mission support; advisory-only task orders are a small share. · SAIC's work is mostly IT integration, engineering and mission support; advisory-only task orders are a small share. |
| CACI | govcon_advisory_share | 0.06 | 0.03 | 0.12 | UNVERIFIED | No source URL · estimate; CACI's 'Expertise' offerings include some functional/advisory support, but most revenue is technology and mission work for DoW and the IC. · CACI's 'Expertise' offerings include some functional/advisory support, but most revenue is technology and mission work for DoW and the IC. |
| PSN | govcon_advisory_share | 0.05 | 0.02 | 0.1 | UNVERIFIED | No source URL · estimate; Parsons' federal work is engineering, missile defense, cyber and program management; advisory-only federal work is small. Its 2025 Federal Solutions decline came from a reduced State Department contract, not consulting. · Parsons' federal work is engineering, missile defense, cyber and program management; advisory-only federal work is small. Its 2025 Federal Solutions decline came from a reduced State Department contract, not consulting. |
| GD | govcon_advisory_share | 0.02 | 0.01 | 0.05 | UNVERIFIED | No source URL · estimate; GD's 10-K says 2025 efficiency-driven contract terminations were 'largely limited to our IT services business'; professional-support work is a small part of GDIT. · GD's 10-K says 2025 efficiency-driven contract terminations were 'largely limited to our IT services business'; professional-support work is a small part of GDIT. |
| KBR | govcon_advisory_share | 0.05 | 0.02 | 0.45 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Government engineering and advisory; median base and outer low/high from BAH/LDOS/SAIC/CACI/PSN in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Government engineering and advisory; median base and outer low/high from BAH/LDOS/SAIC/CACI/PSN in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| ICFI | govcon_advisory_share | 0.05 | 0.02 | 0.45 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Government engineering and advisory; median base and outer low/high from BAH/LDOS/SAIC/CACI/PSN in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Government engineering and advisory; median base and outer low/high from BAH/LDOS/SAIC/CACI/PSN in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| TTEK | govcon_advisory_share | 0.05 | 0.02 | 0.45 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Government engineering and advisory; median base and outer low/high from BAH/LDOS/SAIC/CACI/PSN in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Government engineering and advisory; median base and outer low/high from BAH/LDOS/SAIC/CACI/PSN in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |

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
| exposure.govcon_advisory_share | -0.0033235047 | -0.017274397 | 0.013950892 |
| assumption.replacement_offset | -0.0079757579 | -0.0039878789 | 0.0039878789 |

Dominant configured driver: `govcon_advisory_share` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.


## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 9 unchecked in-scope exposure values; 1 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

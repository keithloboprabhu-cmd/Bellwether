# Federal IT modernization funding

Policy `public_sector/it_modernization_funding` · reviewed 2026-10-31 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

New federal money for IT modernization (in the style of the Technology Modernization Fund) flows to IT contractors in proportion to their share of all federal IT spending. SAIC, Booz Allen and Leidos benefit most; Parsons little.

Duration: `years:3`. Default inputs: `{"program_busd": 3.0}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| demand_transfer | unavailable / unavailable | {"total_transfer_musd": "input.program_busd * 1000", "mpc": "assumption.outlay_share", "capture_share": "baseline.revenue * exposure.govcon_fed_it_share / assumption.fed_it_market_musd"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://www.gao.gov/podcast/which-critical-government-it-systems-are-most-need-modernization
- https://www.sec.gov/Archives/edgar/data/40533/000004053326000006/gd-20251231.htm

| Company | Configured status | Basis |
|---|---|---|
| BAH | included | Incremental federal IT awards raise captured revenue. |
| LDOS | included | Incremental federal IT awards raise captured revenue. |
| SAIC | included | Incremental federal IT awards raise captured revenue. |
| CACI | included | Incremental federal IT awards raise captured revenue. |
| PSN | included | Incremental federal IT awards raise captured revenue. |
| GD | included | Incremental federal IT awards raise captured revenue. |
| LMT | included | Incremental federal IT awards raise captured revenue. |
| NOC | included | Incremental federal IT awards raise captured revenue. |
| RTX | included | Incremental federal IT awards raise captured revenue. |
| HII | included | Incremental federal IT awards raise captured revenue. |
| OSK | outside_scope | Agency IT/cyber-services allocation excludes defense hardware-only suppliers; a GD peer share is not transferred to every manufacturer. |
| KBR | included | Incremental federal IT awards raise captured revenue. |
| KTOS | outside_scope | Agency IT/cyber-services allocation excludes defense hardware-only suppliers; a GD peer share is not transferred to every manufacturer. |
| AVAV | outside_scope | Agency IT/cyber-services allocation excludes defense hardware-only suppliers; a GD peer share is not transferred to every manufacturer. |
| BWXT | outside_scope | Agency IT/cyber-services allocation excludes defense hardware-only suppliers; a GD peer share is not transferred to every manufacturer. |
| TXT | outside_scope | Agency IT/cyber-services allocation excludes defense hardware-only suppliers; a GD peer share is not transferred to every manufacturer. |
| ICFI | included | Incremental federal IT awards raise captured revenue. |
| TTEK | included | Incremental federal IT awards raise captured revenue. |
| MRCY | outside_scope | Agency IT/cyber-services allocation excludes defense hardware-only suppliers; a GD peer share is not transferred to every manufacturer. |
| VSEC | outside_scope | Agency IT/cyber-services allocation excludes defense hardware-only suppliers; a GD peer share is not transferred to every manufacturer. |

## B. Every in-scope exposure

Exact numeric checks are distinguished from filing links and estimates. UNVERIFIED values are retained, not silently replaced. Historical observed low/high values are not forecast confidence intervals.

| Company | Exposure | Base | Low | High | Exact-source status | Primary source / location / rationale |
|---|---|---:|---:|---:|---|---|
| BAH | govcon_fed_it_share | 0.45 | 0.35 | 0.6 | UNVERIFIED | No source URL · estimate; Booz Allen calls itself the government's largest AI provider and lists digital modernization, cloud, data and cyber as core lines; no revenue split by offering is disclosed. · Booz Allen calls itself the government's largest AI provider and lists digital modernization, cloud, data and cyber as core lines; no revenue split by offering is disclosed. |
| LDOS | govcon_fed_it_share | 0.4 | 0.3 | 0.5 | UNVERIFIED | No source URL · estimate; National Security & Digital is 44% of revenue (10-K) and Health & Civil (30%) includes large IT programs; part of each is non-IT (health services, engineering). · National Security & Digital is 44% of revenue (10-K) and Health & Civil (30%) includes large IT programs; part of each is non-IT (health services, engineering). |
| SAIC | govcon_fed_it_share | 0.7 | 0.55 | 0.85 | UNVERIFIED | No source URL · estimate; SAIC positions itself as a technology integrator (enterprise IT, cloud, software, mission IT); engineering and logistics work make up the rest. · SAIC positions itself as a technology integrator (enterprise IT, cloud, software, mission IT); engineering and logistics work make up the rest. |
| CACI | govcon_fed_it_share | 0.45 | 0.35 | 0.6 | UNVERIFIED | No source URL · estimate; CACI sells enterprise IT, software development and network modernization alongside mission technology (signals intelligence, electronic warfare) that is not classic IT. · CACI sells enterprise IT, software development and network modernization alongside mission technology (signals intelligence, electronic warfare) that is not classic IT. |
| PSN | govcon_fed_it_share | 0.08 | 0.04 | 0.15 | UNVERIFIED | No source URL · estimate; Parsons is mainly engineering and infrastructure; federal IT/cyber is a modest part of Defense & Intelligence. · Parsons is mainly engineering and infrastructure; federal IT/cyber is a modest part of Defense & Intelligence. |
| GD | govcon_fed_it_share | 0.17 | 0.15 | 0.172 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/40533/000004053326000006/gd-20251231.htm · General Dynamics 2025 10-K: Technologies IT services revenue $9,057M of $52,550M (17.2%); includes a little state and commercial work;  · unavailable |
| LMT | govcon_fed_it_share | 0.02 | 0 | 0.05 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/936468/000162828026004195/0001628280-26-004195-index.htm · estimate; Company-specific scenario estimate: isolate agency IT/cyber and digital-services opportunities from weapons platforms, engineering and environmental work. Do not inherit a 17% GD or 45% services-peer share for all revenue. The filing supplies business context; the 2.0% share is an estimate with a wide range, not disclosed eligible modernization revenue. · Company-specific scenario estimate: isolate agency IT/cyber and digital-services opportunities from weapons platforms, engineering and environmental work. Do not inherit a 17% GD or 45% services-peer share for all revenue. The filing supplies business context; the 2.0% share is an estimate with a wide range, not disclosed eligible modernization revenue. |
| NOC | govcon_fed_it_share | 0.03 | 0.005 | 0.08 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1133421/000113342126000003/0001133421-26-000003-index.htm · estimate; Company-specific scenario estimate: isolate agency IT/cyber and digital-services opportunities from weapons platforms, engineering and environmental work. Do not inherit a 17% GD or 45% services-peer share for all revenue. The filing supplies business context; the 3.0% share is an estimate with a wide range, not disclosed eligible modernization revenue. · Company-specific scenario estimate: isolate agency IT/cyber and digital-services opportunities from weapons platforms, engineering and environmental work. Do not inherit a 17% GD or 45% services-peer share for all revenue. The filing supplies business context; the 3.0% share is an estimate with a wide range, not disclosed eligible modernization revenue. |
| RTX | govcon_fed_it_share | 0.01 | 0 | 0.04 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/101829/000010182926000006/0000101829-26-000006-index.htm · estimate; Company-specific scenario estimate: isolate agency IT/cyber and digital-services opportunities from weapons platforms, engineering and environmental work. Do not inherit a 17% GD or 45% services-peer share for all revenue. The filing supplies business context; the 1.0% share is an estimate with a wide range, not disclosed eligible modernization revenue. · Company-specific scenario estimate: isolate agency IT/cyber and digital-services opportunities from weapons platforms, engineering and environmental work. Do not inherit a 17% GD or 45% services-peer share for all revenue. The filing supplies business context; the 1.0% share is an estimate with a wide range, not disclosed eligible modernization revenue. |
| HII | govcon_fed_it_share | 0.05 | 0.01 | 0.12 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1501585/000150158526000006/0001501585-26-000006-index.htm · estimate; Company-specific scenario estimate: isolate agency IT/cyber and digital-services opportunities from weapons platforms, engineering and environmental work. Do not inherit a 17% GD or 45% services-peer share for all revenue. The filing supplies business context; the 5.0% share is an estimate with a wide range, not disclosed eligible modernization revenue. · Company-specific scenario estimate: isolate agency IT/cyber and digital-services opportunities from weapons platforms, engineering and environmental work. Do not inherit a 17% GD or 45% services-peer share for all revenue. The filing supplies business context; the 5.0% share is an estimate with a wide range, not disclosed eligible modernization revenue. |
| KBR | govcon_fed_it_share | 0.05 | 0.01 | 0.15 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1357615/000135761526000051/0001357615-26-000051-index.htm · estimate; Company-specific scenario estimate: isolate agency IT/cyber and digital-services opportunities from weapons platforms, engineering and environmental work. Do not inherit a 17% GD or 45% services-peer share for all revenue. The filing supplies business context; the 5.0% share is an estimate with a wide range, not disclosed eligible modernization revenue. · Company-specific scenario estimate: isolate agency IT/cyber and digital-services opportunities from weapons platforms, engineering and environmental work. Do not inherit a 17% GD or 45% services-peer share for all revenue. The filing supplies business context; the 5.0% share is an estimate with a wide range, not disclosed eligible modernization revenue. |
| ICFI | govcon_fed_it_share | 0.2 | 0.08 | 0.35 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1362004/000119312526082536/0001193125-26-082536-index.htm · estimate; Company-specific scenario estimate: isolate agency IT/cyber and digital-services opportunities from weapons platforms, engineering and environmental work. Do not inherit a 17% GD or 45% services-peer share for all revenue. The filing supplies business context; the 20.0% share is an estimate with a wide range, not disclosed eligible modernization revenue. · Company-specific scenario estimate: isolate agency IT/cyber and digital-services opportunities from weapons platforms, engineering and environmental work. Do not inherit a 17% GD or 45% services-peer share for all revenue. The filing supplies business context; the 20.0% share is an estimate with a wide range, not disclosed eligible modernization revenue. |
| TTEK | govcon_fed_it_share | 0.02 | 0 | 0.06 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/831641/000083164125000032/0000831641-25-000032-index.htm · estimate; Company-specific scenario estimate: isolate agency IT/cyber and digital-services opportunities from weapons platforms, engineering and environmental work. Do not inherit a 17% GD or 45% services-peer share for all revenue. The filing supplies business context; the 2.0% share is an estimate with a wide range, not disclosed eligible modernization revenue. · Company-specific scenario estimate: isolate agency IT/cyber and digital-services opportunities from weapons platforms, engineering and environmental work. Do not inherit a 17% GD or 45% services-peer share for all revenue. The filing supplies business context; the 2.0% share is an estimate with a wide range, not disclosed eligible modernization revenue. |

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
| assumption.outlay_share | 0.0022779358 | 0.0051253555 | 0.0028474197 |
| exposure.govcon_fed_it_share | 0.0025934255 | 0.0053725706 | 0.0027791451 |
| assumption.fed_it_market_musd | 0.0040718102 | 0.0031321617 | 0.00093964851 |

Dominant configured driver: `outlay_share` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.


## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 13 unchecked in-scope exposure values; 2 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

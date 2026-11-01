# Return-to-office mandate

Policy `real_estate_hospitality/return_to_office_mandate` · reviewed 2026-10-31 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

A federal push that raises office attendance nationwide adds weekday mall and hotel traffic a little and trims remote-work long stays on Airbnb. The hotel exposure includes owners as well as brand/managers. Effects are uncertain attendance-to-spending scenarios; no office-rent channel is modeled.

Duration: `permanent`. Default inputs: `{"d_attendance_pct": 3.0}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| demand_volume | unavailable / unavailable | {"d_volume": "input.d_attendance_pct / 100 * assumption.spend_elasticity", "exposed_revenue_share": "exposure.re_office_linked_revenue_share"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/
- https://ir.hosthotels.com/news-releases/news-release-details/host-hotels-resorts-inc-reports-results-2025

| Company | Configured status | Basis |
|---|---|---|
| PLD | outside_scope | This scenario models attendance-linked retail/business travel and remote-work stays. No office-rental channel or indirect local-economy multiplier is estimated for other property types. |
| AMT | outside_scope | This scenario models attendance-linked retail/business travel and remote-work stays. No office-rental channel or indirect local-economy multiplier is estimated for other property types. |
| SPG | included | More office-linked activity raises exposed footfall. |
| MAR | included | More office-linked activity raises exposed footfall. |
| HLT | included | More office-linked activity raises exposed footfall. |
| ABNB | included | More office-linked activity raises exposed footfall. |
| O | outside_scope | This scenario models attendance-linked retail/business travel and remote-work stays. No office-rental channel or indirect local-economy multiplier is estimated for other property types. |
| EQIX | outside_scope | This scenario models attendance-linked retail/business travel and remote-work stays. No office-rental channel or indirect local-economy multiplier is estimated for other property types. |
| DLR | outside_scope | This scenario models attendance-linked retail/business travel and remote-work stays. No office-rental channel or indirect local-economy multiplier is estimated for other property types. |
| WELL | outside_scope | This scenario models attendance-linked retail/business travel and remote-work stays. No office-rental channel or indirect local-economy multiplier is estimated for other property types. |
| VTR | outside_scope | This scenario models attendance-linked retail/business travel and remote-work stays. No office-rental channel or indirect local-economy multiplier is estimated for other property types. |
| ESS | outside_scope | This scenario models attendance-linked retail/business travel and remote-work stays. No office-rental channel or indirect local-economy multiplier is estimated for other property types. |
| MAA | outside_scope | This scenario models attendance-linked retail/business travel and remote-work stays. No office-rental channel or indirect local-economy multiplier is estimated for other property types. |
| PSA | outside_scope | This scenario models attendance-linked retail/business travel and remote-work stays. No office-rental channel or indirect local-economy multiplier is estimated for other property types. |
| EXR | outside_scope | This scenario models attendance-linked retail/business travel and remote-work stays. No office-rental channel or indirect local-economy multiplier is estimated for other property types. |
| VICI | outside_scope | This scenario models attendance-linked retail/business travel and remote-work stays. No office-rental channel or indirect local-economy multiplier is estimated for other property types. |
| WY | outside_scope | This scenario models attendance-linked retail/business travel and remote-work stays. No office-rental channel or indirect local-economy multiplier is estimated for other property types. |
| HST | included | More office-linked activity raises exposed footfall. |
| RLJ | included | More office-linked activity raises exposed footfall. |
| PK | included | More office-linked activity raises exposed footfall. |

## B. Every in-scope exposure

Exact numeric checks are distinguished from filing links and estimates. UNVERIFIED values are retained, not silently replaced. Historical observed low/high values are not forecast confidence intervals.

| Company | Exposure | Base | Low | High | Exact-source status | Primary source / location / rationale |
|---|---|---:|---:|---:|---|---|
| SPG | re_office_linked_revenue_share | 0.02 | 0 | 0.05 | UNVERIFIED | No source URL · estimate; Weekday office workers add some mall traffic and percentage rent; most rent is fixed minimum rent. · Weekday office workers add some mall traffic and percentage rent; most rent is fixed minimum rent. |
| MAR | re_office_linked_revenue_share | 0.01 | 0 | 0.03 | UNVERIFIED | No source URL · estimate; Business transient travel is tied to company activity more than to daily office attendance. · Business transient travel is tied to company activity more than to daily office attendance. |
| HLT | re_office_linked_revenue_share | 0.01 | 0 | 0.03 | UNVERIFIED | No source URL · estimate; Business transient travel is tied to company activity more than to daily office attendance. · Business transient travel is tied to company activity more than to daily office attendance. |
| ABNB | re_office_linked_revenue_share | -0.05 | -0.1 | 0 | UNVERIFIED | No source URL · estimate; Stays of 28+ nights (a 10-K reported category) are partly remote-work driven and fall when workers must be in the office. · Stays of 28+ nights (a 10-K reported category) are partly remote-work driven and fall when workers must be in the office. |
| HST | re_office_linked_revenue_share | 0.02 | 0 | 0.08 | UNVERIFIED | https://ir.hosthotels.com/news-releases/news-release-details/host-hotels-resorts-inc-reports-results-2025 · estimate; Scenario estimate: hotel owners have business/transient and group customers as do hotel managers. Use a small 2.0% attendance-linked revenue share (0–8%), not zero inherited from non-hotel property REITs. Attendance-to-travel transmission is uncertain, not a reported business-traveler share. · Scenario estimate: hotel owners have business/transient and group customers as do hotel managers. Use a small 2.0% attendance-linked revenue share (0–8%), not zero inherited from non-hotel property REITs. Attendance-to-travel transmission is uncertain, not a reported business-traveler share. |
| RLJ | re_office_linked_revenue_share | 0.03 | 0 | 0.08 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1511337/000151133726000007/0001511337-26-000007-index.htm · estimate; Scenario estimate: hotel owners have business/transient and group customers as do hotel managers. Use a small 3.0% attendance-linked revenue share (0–8%), not zero inherited from non-hotel property REITs. Attendance-to-travel transmission is uncertain, not a reported business-traveler share. · Scenario estimate: hotel owners have business/transient and group customers as do hotel managers. Use a small 3.0% attendance-linked revenue share (0–8%), not zero inherited from non-hotel property REITs. Attendance-to-travel transmission is uncertain, not a reported business-traveler share. |
| PK | re_office_linked_revenue_share | 0.02 | 0 | 0.08 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1617406/000161740626000006/0001617406-26-000006-index.htm · estimate; Scenario estimate: hotel owners have business/transient and group customers as do hotel managers. Use a small 2.0% attendance-linked revenue share (0–8%), not zero inherited from non-hotel property REITs. Attendance-to-travel transmission is uncertain, not a reported business-traveler share. · Scenario estimate: hotel owners have business/transient and group customers as do hotel managers. Use a small 2.0% attendance-linked revenue share (0–8%), not zero inherited from non-hotel property REITs. Attendance-to-travel transmission is uncertain, not a reported business-traveler share. |

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
| exposure.re_office_linked_revenue_share | -0.00085981056 | 0.00054492852 | 0.0014047391 |
| assumption.spend_elasticity | -0.00011822267 | -0.00035466802 | 0.00023644534 |

Dominant configured driver: `re_office_linked_revenue_share` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.


## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 7 unchecked in-scope exposure values; 1 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

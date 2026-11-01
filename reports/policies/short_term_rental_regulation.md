# Short-term rental restrictions

Policy `real_estate_hospitality/short_term_rental_regulation` · reviewed 2026-10-31 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

A wave of US city and state rules (registration caps, primary-residence requirements, outright bans like New York City's 2023 law) removes a share of US short-term-rental listings. Airbnb loses US bookings it can't move to other listings; hotel franchisors win back a little demand.

Duration: `permanent`. Default inputs: `{"listings_removed_pct": 10.0}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| demand_volume | unavailable / unavailable | {"d_volume": "-(input.listings_removed_pct / 100) * (1 - assumption.recapture_share)", "exposed_revenue_share": "exposure.re_us_str_revenue_share"} |
| demand_volume | unavailable / unavailable | {"d_volume": "assumption.hotel_elasticity * input.listings_removed_pct / 100", "exposed_revenue_share": "exposure.re_us_hotel_revenue_share"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://people.bu.edu/zg/publications/airbnb.pdf
- https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/

| Company | Configured status | Basis |
|---|---|---|
| PLD | outside_scope | The modeled short-stay/hotel substitution channel excludes housing leases, storage, industrial, telecom, healthcare, timber and gaming-lease properties. |
| AMT | outside_scope | The modeled short-stay/hotel substitution channel excludes housing leases, storage, industrial, telecom, healthcare, timber and gaming-lease properties. |
| SPG | outside_scope | The modeled short-stay/hotel substitution channel excludes housing leases, storage, industrial, telecom, healthcare, timber and gaming-lease properties. |
| MAR | included | Restrictions lower covered short-term rental bookings; hotels can gain. |
| HLT | included | Restrictions lower covered short-term rental bookings; hotels can gain. |
| ABNB | included | Restrictions lower covered short-term rental bookings; hotels can gain. |
| O | outside_scope | The modeled short-stay/hotel substitution channel excludes housing leases, storage, industrial, telecom, healthcare, timber and gaming-lease properties. |
| EQIX | outside_scope | The modeled short-stay/hotel substitution channel excludes housing leases, storage, industrial, telecom, healthcare, timber and gaming-lease properties. |
| DLR | outside_scope | The modeled short-stay/hotel substitution channel excludes housing leases, storage, industrial, telecom, healthcare, timber and gaming-lease properties. |
| WELL | outside_scope | The modeled short-stay/hotel substitution channel excludes housing leases, storage, industrial, telecom, healthcare, timber and gaming-lease properties. |
| VTR | outside_scope | The modeled short-stay/hotel substitution channel excludes housing leases, storage, industrial, telecom, healthcare, timber and gaming-lease properties. |
| ESS | outside_scope | The modeled short-stay/hotel substitution channel excludes housing leases, storage, industrial, telecom, healthcare, timber and gaming-lease properties. |
| MAA | outside_scope | The modeled short-stay/hotel substitution channel excludes housing leases, storage, industrial, telecom, healthcare, timber and gaming-lease properties. |
| PSA | outside_scope | The modeled short-stay/hotel substitution channel excludes housing leases, storage, industrial, telecom, healthcare, timber and gaming-lease properties. |
| EXR | outside_scope | The modeled short-stay/hotel substitution channel excludes housing leases, storage, industrial, telecom, healthcare, timber and gaming-lease properties. |
| VICI | outside_scope | The modeled short-stay/hotel substitution channel excludes housing leases, storage, industrial, telecom, healthcare, timber and gaming-lease properties. |
| WY | outside_scope | The modeled short-stay/hotel substitution channel excludes housing leases, storage, industrial, telecom, healthcare, timber and gaming-lease properties. |
| HST | included | Restrictions lower covered short-term rental bookings; hotels can gain. |
| RLJ | included | Restrictions lower covered short-term rental bookings; hotels can gain. |
| PK | included | Restrictions lower covered short-term rental bookings; hotels can gain. |

## B. Every in-scope exposure

Exact numeric checks are distinguished from filing links and estimates. UNVERIFIED values are retained, not silently replaced. Historical observed low/high values are not forecast confidence intervals.

| Company | Exposure | Base | Low | High | Exact-source status | Primary source / location / rationale |
|---|---|---:|---:|---:|---|---|
| MAR | re_us_str_revenue_share | 0 | 0 | 0 | UNVERIFIED | No source URL · estimate; Homes & Villas by Marriott is immaterial to revenue. · Homes & Villas by Marriott is immaterial to revenue. |
| MAR | re_us_hotel_revenue_share | 0.7 | 0.6 | 0.75 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1048286/000104828626000007/ · Marriott FY2025 10-K segments: U.S. & Canada net fee revenues $2,921M of $4,172M across the four reportable segments (70%); Fee share used because reimbursed-cost revenue is pass-through. · Fee share used because reimbursed-cost revenue is pass-through. |
| HLT | re_us_str_revenue_share | 0 | 0 | 0 | UNVERIFIED | No source URL · estimate; No short-term-rental business. · No short-term-rental business. |
| HLT | re_us_hotel_revenue_share | 0.79 | 0.7 | 0.82 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1585689/000158568926000007/ · Hilton FY2025 10-K: U.S. revenues $9,523M of $12,039M (79%);  · unavailable |
| ABNB | re_us_str_revenue_share | 0.39 | 0.35 | 0.42 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/ · Airbnb FY2025 10-K: United States revenue $4,814M of $12,241M (39%);  · unavailable |
| ABNB | re_us_hotel_revenue_share | 0 | 0 | 0 | UNVERIFIED | No source URL · estimate; Hotel listings are a small part of Airbnb; its loss is in the STR channel. · Hotel listings are a small part of Airbnb; its loss is in the STR channel. |
| HST | re_us_str_revenue_share | 0 | 0 | 0 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Property REITs: housing, storage, digital infrastructure, timber and hospitality; median base and outer low/high from PLD/AMT/SPG in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Property REITs: housing, storage, digital infrastructure, timber and hospitality; median base and outer low/high from PLD/AMT/SPG in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| HST | re_us_hotel_revenue_share | 0.95 | 0.85 | 1 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1070750/000107075026000054/0001070750-26-000054-index.htm · estimate; Company-specific estimate: Hotel-owner portfolio exposure: estimate 95% (85–100%) of consolidated revenue from US hotel operations. This is a hotel-specific proxy, not the zero hotel share of logistics/tower/mall REIT peers. · Company-specific estimate: Hotel-owner portfolio exposure: estimate 95% (85–100%) of consolidated revenue from US hotel operations. This is a hotel-specific proxy, not the zero hotel share of logistics/tower/mall REIT peers. |
| RLJ | re_us_str_revenue_share | 0 | 0 | 0 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Property REITs: housing, storage, digital infrastructure, timber and hospitality; median base and outer low/high from PLD/AMT/SPG in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Property REITs: housing, storage, digital infrastructure, timber and hospitality; median base and outer low/high from PLD/AMT/SPG in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| RLJ | re_us_hotel_revenue_share | 0.95 | 0.85 | 1 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1511337/000151133726000007/0001511337-26-000007-index.htm · estimate; Company-specific estimate: Hotel-owner portfolio exposure: estimate 95% (85–100%) of consolidated revenue from US hotel operations. This is a hotel-specific proxy, not the zero hotel share of logistics/tower/mall REIT peers. · Company-specific estimate: Hotel-owner portfolio exposure: estimate 95% (85–100%) of consolidated revenue from US hotel operations. This is a hotel-specific proxy, not the zero hotel share of logistics/tower/mall REIT peers. |
| PK | re_us_str_revenue_share | 0 | 0 | 0 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Property REITs: housing, storage, digital infrastructure, timber and hospitality; median base and outer low/high from PLD/AMT/SPG in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Property REITs: housing, storage, digital infrastructure, timber and hospitality; median base and outer low/high from PLD/AMT/SPG in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| PK | re_us_hotel_revenue_share | 0.95 | 0.85 | 1 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1617406/000161740626000006/0001617406-26-000006-index.htm · estimate; Company-specific estimate: Hotel-owner portfolio exposure: estimate 95% (85–100%) of consolidated revenue from US hotel operations. This is a hotel-specific proxy, not the zero hotel share of logistics/tower/mall REIT peers. · Company-specific estimate: Hotel-owner portfolio exposure: estimate 95% (85–100%) of consolidated revenue from US hotel operations. This is a hotel-specific proxy, not the zero hotel share of logistics/tower/mall REIT peers. |

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
| assumption.recapture_share | -0.0093131479 | -0.004842133 | 0.0044710149 |
| exposure.re_us_str_revenue_share | -0.0062751506 | -0.0076795078 | 0.0014043572 |
| assumption.hotel_elasticity | -0.007441386 | -0.0066756059 | 0.00076578013 |
| exposure.re_us_hotel_revenue_share | -0.0071721718 | -0.0070348508 | 0.00013732101 |

Dominant configured driver: `recapture_share` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.


## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 12 unchecked in-scope exposure values; 2 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

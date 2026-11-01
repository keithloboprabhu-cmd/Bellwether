# Rolling back 100% bonus depreciation

Policy `industrials/bonus_depreciation_rollback` · evidence checkpoint 2026-11-01 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

Lowering the permanent 100% bonus depreciation rate means companies deduct less of their new US equipment up front. It changes when tax is paid, not how much, so earnings barely move but value falls a little. Nucor, with by far the largest US capex relative to its size, loses the most.

Duration: `permanent`. Default inputs: `{"bonus_cut_pts": 60.0}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| tax_timing | unavailable / unavailable | {"capex_musd": "exposure.ind_us_capex_musd", "expensed_share": "-input.bonus_cut_pts / 100 * assumption.eligible_share", "recovery_years": "assumption.recovery_years"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://www.bdo.com/insights/tax/irs-issues-interim-guidance-on-bonus-depreciation-rules
- https://www.law.cornell.edu/uscode/text/26/168

| Company | Configured status | Basis |
|---|---|---|
| CAT | included | Lost cash-tax deferral lowers value, without a GAAP EPS change. |
| DE | included | Lost cash-tax deferral lowers value, without a GAAP EPS change. |
| GE | included | Lost cash-tax deferral lowers value, without a GAAP EPS change. |
| HON | included | Lost cash-tax deferral lowers value, without a GAAP EPS change. |
| MMM | included | Lost cash-tax deferral lowers value, without a GAAP EPS change. |
| NUE | included | Lost cash-tax deferral lowers value, without a GAAP EPS change. |
| BA | included | Lost cash-tax deferral lowers value, without a GAAP EPS change. |
| ETN | included | Lost cash-tax deferral lowers value, without a GAAP EPS change. |
| EMR | included | Lost cash-tax deferral lowers value, without a GAAP EPS change. |
| ITW | included | Lost cash-tax deferral lowers value, without a GAAP EPS change. |
| PH | included | Lost cash-tax deferral lowers value, without a GAAP EPS change. |
| CMI | included | Lost cash-tax deferral lowers value, without a GAAP EPS change. |
| PCAR | included | Lost cash-tax deferral lowers value, without a GAAP EPS change. |
| DOV | included | Lost cash-tax deferral lowers value, without a GAAP EPS change. |
| ROK | included | Lost cash-tax deferral lowers value, without a GAAP EPS change. |
| STLD | included | Lost cash-tax deferral lowers value, without a GAAP EPS change. |
| CLF | included | Lost cash-tax deferral lowers value, without a GAAP EPS change. |
| CARR | included | Lost cash-tax deferral lowers value, without a GAAP EPS change. |
| OTIS | included | Lost cash-tax deferral lowers value, without a GAAP EPS change. |
| IR | included | Lost cash-tax deferral lowers value, without a GAAP EPS change. |
| GEV | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |

## B. Every in-scope exposure

Exact numeric checks are distinguished from filing links and estimates. UNVERIFIED values are retained, not silently replaced. Historical observed low/high values are not forecast confidence intervals.

| Company | Exposure | Base | Low | High | Exact-source status | Primary source / location / rationale |
|---|---|---:|---:|---:|---|---|
| CAT | ind_us_capex_musd | 1,750 | 1,500 | 2,000 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/18230/000001823026000008/cat-20251231.htm · Caterpillar 2025 10-K: capex $2,821M (XBRL PaymentsToAcquirePropertyPlantAndEquipment) × 62% of net PP&E inside the US ($9,455M of $15,140M); Allocates capex by the US share of the PP&E stock; the range allows for the US share of new spending to differ. · Allocates capex by the US share of the PP&E stock; the range allows for the US share of new spending to differ. |
| DE | ind_us_capex_musd | 707 | 600 | 850 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/315189/000110465925122321/de-20251102x10k.htm · Deere FY2025 10-K: capex $1,360M (XBRL PaymentsToAcquirePropertyPlantAndEquipment) × 52% of property and equipment in the U.S. ($4,198M of $8,079M);  · unavailable |
| GE | ind_us_capex_musd | 917 | 800 | 1,050 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/40545/000004054526000008/ge-20251231.htm · GE Aerospace 2025 10-K: capex $1,273M (XBRL PaymentsToAcquireProductiveAssets) × 72% of long-lived assets in the U.S. ($5,736M of $7,988M);  · unavailable |
| HON | ind_us_capex_musd | 680 | 590 | 780 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/773840/000077384026000013/hon-20251231.htm · Honeywell 2025 10-K: capex $986M (XBRL PaymentsToAcquirePropertyPlantAndEquipment) × 69% of long-lived assets in the United States ($3,192M of $4,628M);  · unavailable |
| MMM | ind_us_capex_musd | 565 | 500 | 663 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/66740/000006674026000014/mmm-20251231.htm · 3M 2025 10-K: capital spending $910M, of which Americas $663M (73%); US share assumed ~62% (Americas includes Canada and Latin America); The high end treats all Americas capex as US. · The high end treats all Americas capex as US. |
| NUE | ind_us_capex_musd | 3,350 | 3,200 | 3,422 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/73309/000119312526071575/nue-20251231.htm · Nucor 2025 10-K: capex $3,422M (XBRL PaymentsToAcquirePropertyPlantAndEquipment); nearly all facilities are in the US (one DRI plant in Trinidad, some products plants in Canada/Mexico);  · unavailable |
| BA | ind_us_capex_musd | 1,789.0649 | 1,174.9803 | 2,647.2651 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| ETN | ind_us_capex_musd | 548.90014 | 360.49383 | 812.20317 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| EMR | ind_us_capex_musd | 360.28071 | 236.61676 | 533.1045 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| ITW | ind_us_capex_musd | 320.84501 | 210.7171 | 474.75181 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| PH | ind_us_capex_musd | 429.93312 | 282.36144 | 636.16861 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| CMI | ind_us_capex_musd | 673.32657 | 442.21172 | 996.31597 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| PCAR | ind_us_capex_musd | 568.83397 | 373.5855 | 841.69909 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| DOV | ind_us_capex_musd | 161.83377 | 106.28541 | 239.46414 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| ROK | ind_us_capex_musd | 166.82181 | 109.56133 | 246.8449 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| STLD | ind_us_capex_musd | 1,873.932 | 1,790.0246 | 1,914.2076 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Steel production; median base and outer low/high from NUE in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Steel production; median base and outer low/high from NUE in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| CLF | ind_us_capex_musd | 1,918.6157 | 1,832.7076 | 1,959.8517 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Steel production; median base and outer low/high from NUE in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Steel production; median base and outer low/high from NUE in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| CARR | ind_us_capex_musd | 434.89257 | 285.6186 | 643.50708 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| OTIS | ind_us_capex_musd | 288.58853 | 189.53244 | 427.02215 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| IR | ind_us_capex_musd | 153.00132 | 100.48463 | 226.39483 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |

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
| assumption.eligible_share | -0.00016891745 | -0.00025337617 | 8.4458723e-05 |
| exposure.ind_us_capex_musd | -0.0001756004 | -0.00025546106 | 7.9860659e-05 |
| assumption.recovery_years | -0.0001668619 | -0.00021114681 | 4.4284907e-05 |

Dominant configured driver: `eligible_share` using `d_mcap_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.


## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 20 unchecked in-scope exposure values; 2 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

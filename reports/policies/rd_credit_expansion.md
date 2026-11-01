# Bigger federal R&D tax credit

Policy `industrials/rd_credit_expansion` · evidence checkpoint 2026-11-01 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

Raising the research credit rate cuts tax for companies that do a lot of US research. GE Aerospace, Honeywell and Deere gain the most; Nucor gains a little on process engineering.

Duration: `permanent`. Default inputs: `{"d_credit_pts": 6.0}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| tax_credit | unavailable / unavailable | {"credit_rate": "input.d_credit_pts / 100 * assumption.incremental_share", "base_musd": "exposure.ind_us_qre_musd"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://www.law.cornell.edu/uscode/text/26/41

| Company | Configured status | Basis |
|---|---|---|
| CAT | included | Incremental qualifying R&D credit is after-tax income. |
| DE | included | Incremental qualifying R&D credit is after-tax income. |
| GE | included | Incremental qualifying R&D credit is after-tax income. |
| HON | included | Incremental qualifying R&D credit is after-tax income. |
| MMM | included | Incremental qualifying R&D credit is after-tax income. |
| NUE | included | Incremental qualifying R&D credit is after-tax income. |
| BA | included | Incremental qualifying R&D credit is after-tax income. |
| ETN | included | Incremental qualifying R&D credit is after-tax income. |
| EMR | included | Incremental qualifying R&D credit is after-tax income. |
| ITW | included | Incremental qualifying R&D credit is after-tax income. |
| PH | included | Incremental qualifying R&D credit is after-tax income. |
| CMI | included | Incremental qualifying R&D credit is after-tax income. |
| PCAR | included | Incremental qualifying R&D credit is after-tax income. |
| DOV | included | Incremental qualifying R&D credit is after-tax income. |
| ROK | included | Incremental qualifying R&D credit is after-tax income. |
| STLD | included | Incremental qualifying R&D credit is after-tax income. |
| CLF | included | Incremental qualifying R&D credit is after-tax income. |
| CARR | included | Incremental qualifying R&D credit is after-tax income. |
| OTIS | included | Incremental qualifying R&D credit is after-tax income. |
| IR | included | Incremental qualifying R&D credit is after-tax income. |
| GEV | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |

## B. Every in-scope exposure

Exact numeric checks are distinguished from filing links and estimates. UNVERIFIED values are retained, not silently replaced. Historical observed low/high values are not forecast confidence intervals.

| Company | Exposure | Base | Low | High | Exact-source status | Primary source / location / rationale |
|---|---|---:|---:|---:|---|---|
| CAT | ind_us_qre_musd | 1,300 | 900 | 2,000 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/18230/000001823026000008/cat-20251231.htm · estimate; R&D expense was $2,148M in 2025 (XBRL); about 60% assumed performed in the US. The 10-K gives no research-credit amount, and peers' reported credits (DE, HON, GE) imply qualifying spend above their R&D expense, so the high end is wide. · R&D expense was $2,148M in 2025 (XBRL); about 60% assumed performed in the US. The 10-K gives no research-credit amount, and peers' reported credits (DE, HON, GE) imply qualifying spend above their R&D expense, so the high end is wide. |
| DE | ind_us_qre_musd | 1,600 | 1,200 | 1,900 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/315189/000110465925122321/de-20251102x10k.htm · estimate; R&D expense $2,311M in FY2025 (XBRL), roughly 60% in the US ≈ $1.4B; the 10-K tax note shows research and business credits of $131M, which at the 14% alternative simplified credit on about half of QREs implies up to ~$1.9B. · R&D expense $2,311M in FY2025 (XBRL), roughly 60% in the US ≈ $1.4B; the 10-K tax note shows research and business credits of $131M, which at the 14% alternative simplified credit on about half of QREs implies up to ~$1.9B. |
| GE | ind_us_qre_musd | 2,500 | 1,250 | 5,000 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/40545/000004054526000008/ge-20251231.htm · estimate; Company-funded R&D was $1,580M in 2025 (XBRL), mostly US; the 10-K tax note shows a $354M R&D credit, which at ~7% of QREs (14% on the half above the base) implies up to ~$5B, likely including customer- and partner-funded engineering and prior-year claims. Base sits between the two. · Company-funded R&D was $1,580M in 2025 (XBRL), mostly US; the 10-K tax note shows a $354M R&D credit, which at ~7% of QREs (14% on the half above the base) implies up to ~$5B, likely including customer- and partner-funded engineering and prior-year claims. Base sits between the two. |
| HON | ind_us_qre_musd | 2,000 | 1,000 | 3,000 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/773840/000077384026000013/hon-20251231.htm · estimate; R&D expense was $1,812M in 2025 (XBRL), of which about 60% is US-based ≈ $1.1B; the 10-K tax note shows a $214M research credit, which at ~7% of QREs implies ~$3B including engineering charged to cost of sales. · R&D expense was $1,812M in 2025 (XBRL), of which about 60% is US-based ≈ $1.1B; the 10-K tax note shows a $214M research credit, which at ~7% of QREs implies ~$3B including engineering charged to cost of sales. |
| MMM | ind_us_qre_musd | 700 | 450 | 1,000 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/66740/000006674026000014/mmm-20251231.htm · estimate; 3M 2025 10-K: research, development and related expenses $1,169M (4.7% of sales); about 60% assumed US-based and qualifying. The 2024 rate reconciliation shows a US R&D credit of 0.7% of pretax income (~$34M), consistent with the lower end. · 3M 2025 10-K: research, development and related expenses $1,169M (4.7% of sales); about 60% assumed US-based and qualifying. The 2024 rate reconciliation shows a US R&D credit of 0.7% of pretax income (~$34M), consistent with the lower end. |
| NUE | ind_us_qre_musd | 500 | 300 | 650 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/73309/000119312526071575/nue-20251231.htm · estimate; Nucor reports no R&D expense line, but its rate reconciliation shows a federal research credit of 1.55% of 2024 pretax income (~$45M), which at ~7% of QREs implies ~$650M of qualifying process engineering; 0.51% in 2023 implies less. · Nucor reports no R&D expense line, but its rate reconciliation shows a federal research credit of 1.55% of 2024 pretax income (~$45M), which at ~7% of QREs implies ~$650M of qualifying process engineering; 0.51% in 2023 implies less. |
| BA | ind_us_qre_musd | 3,133.2808 | 1,191.2693 | 9,754.9886 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| ETN | ind_us_qre_musd | 961.31687 | 365.49143 | 2,992.9124 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| EMR | ind_us_qre_musd | 630.97802 | 239.89702 | 1,964.4532 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| ITW | ind_us_qre_musd | 561.91227 | 213.63831 | 1,749.4275 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| PH | ind_us_qre_musd | 752.96384 | 286.27587 | 2,344.2373 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| CMI | ind_us_qre_musd | 1,179.2312 | 448.34219 | 3,671.3554 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| PCAR | ind_us_qre_musd | 996.228 | 378.76459 | 3,101.6029 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| DOV | ind_us_qre_musd | 283.42776 | 107.75886 | 882.40879 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| ROK | ind_us_qre_musd | 292.16356 | 111.08021 | 909.60637 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| STLD | ind_us_qre_musd | 279.69134 | 167.81481 | 363.59875 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Steel production; median base and outer low/high from NUE in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Steel production; median base and outer low/high from NUE in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| CLF | ind_us_qre_musd | 286.36056 | 171.81634 | 372.26873 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Steel production; median base and outer low/high from NUE in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Steel production; median base and outer low/high from NUE in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| CARR | ind_us_qre_musd | 761.64959 | 289.57819 | 2,371.279 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| OTIS | ind_us_qre_musd | 505.41984 | 192.15997 | 1,573.5471 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |
| IR | ind_us_qre_musd | 267.95902 | 101.87767 | 834.24926 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Absolute exposure intensity scaled by SEC annual revenue. |

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
| exposure.ind_us_qre_musd | 0.0047106405 | 0.02334867 | 0.01863803 |
| assumption.incremental_share | 0.0088204178 | 0.011760557 | 0.0029401393 |

Dominant configured driver: `ind_us_qre_musd` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.


## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 20 unchecked in-scope exposure values; 1 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

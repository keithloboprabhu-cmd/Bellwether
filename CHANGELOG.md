# Changelog

## 2026-11-01 — audit round 3: credibility matrix and corrections

- Add `scripts/audit_matrix.py`: every policy × company pair at defaults, input endpoints, zero and a sweep, with anomaly flags and an exposure-basis label (sourced / company estimate / peer prior).
- Consumer and auto tariff inputs are now additional duty above what FY2025/26 baselines already contain (the 2025 cost was previously counted twice).
- A statutory rate increase no longer books a gain for loss-making companies (`tax_rate` channel).
- Corporate-tax book-income proxy extended to 42 more issuers; audit additions get filing-based Full Market US pretax shares.
- Replace material peer priors (chipmakers' China shares, grocers' import shares, defense contractors' government shares and others) with company-specific estimates or committed 10-K XBRL values.
- Rate policy reaches insurer portfolios and corporate cash; borrowing caps credit Sallie Mae; new tobacco excise and medical device tariff policies.
- Coverage: companies without an industry-specific effect fall from 44 to 16, and companies without any default effect from 5 to 1. See `reports/AUDIT_ROUND3.md` for limitations and judgment calls.

## 2026-11-01 — continuing economic audit

- Reconcile Tetra Tech's three-year full revenue costs; exclude the partial subcontractor tag as its full cost base and invalidate older live financial normalization caches.
- Replace four copied airline baggage-fee shares with official BTS carrier observations; reconcile American and Delta domestic passenger revenue to their own filings.
- Separate reported global airline fuel gallons from US-only carbon-tax volume in the macro oil shock.
- Clarify hypothetical policy status, CHIPS property eligibility, education's two-of-three-year earnings test, and limits on extrapolating historical MA pass-through.
- Archive primary evidence and regression checks. Whole-policy evidence certification remains unresolved; this checkpoint does not claim the economic audit is complete.

## 2026-11-01 — macro console

- Add Macro · All industries to the industry selector, using the existing ten macro shocks.
- Compare all ten industries with ranked signed bars, projected financials and dollar/percentage changes; drill into company Fields and telemetry.
- Add a separate industry CSV export; retain company CSV columns, profile schema and industry scenario links.
- Use one immutable live-data capture for every sector; show unquantified and unavailable valuation counts explicitly.
- Verify all ten macro APIs, zero/invalid inputs, shared captures and unchanged legacy industry behavior. Final suite: 610 Python tests and 16 frontend tests passed; 303 local API input cases passed (261 industry + 42 macro); frontend production build passed.


## 2026-11-01 — quantitative audit

- Preserve the original 203-company/66-policy baseline and architecture inventory.
- Add 31 supported issuers (234 total), six submitted corporate-rate scenarios
  (72 total), 1,694 explicit coverage decisions and source/admission ledgers.
  Five default earnings/value coverage gaps remain; no copied peer priors fill them.
- Repair alternate debt/cost facts, separate captive-finance borrowings, add insurer
  claims templates and current multi-class shares, preserve raw tax anomalies with
  documented normalization, and refresh all due Yahoo quote tickers.
- Floor projected traded-equity prices at zero with attribution reconciliation.
  Depressed/negative earnings require verified adjusted three-year EPS for permanent
  valuation. Capital One uses issuer reconciliations; unsupported cases stay missing.
- Replace twelve bank sensitivity coefficients with exact published scenarios and
  separate USITC buyer/producer steel-price responses. Twenty-three bank comparison
  points pass; all 72 whole-policy empirical verdicts remain FAIL-UNRESOLVED.
- Add three non-TCJA historical cases and expand steel beyond three firms. Expanded
  directional score: 155/190 (81.6%); original cohort unchanged at 104/120 (86.7%).
  Document case-level MAE regressions and confounding rather than fitting them away.
- Add ten independent arithmetic checks and the final audit summary. Preserve
  original policy IDs, scenario URLs, CSV columns and profile JSON schema.
- Verification: 596 Python tests passed, five skipped; 16 frontend tests passed;
  production frontend build passed; internal audit: 72 policies/10 macro shocks,
  zero invariant failures. Empirical evidence gaps are separate from software tests.

See [AUDIT_SUMMARY](reports/AUDIT_SUMMARY.md) for scope, sources and open decisions.
Audit findings and unresolved items are preserved with the code; deployment status is separate from economic certification.

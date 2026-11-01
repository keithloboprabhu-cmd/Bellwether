# Changelog

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
This local audit has not been pushed or deployed.

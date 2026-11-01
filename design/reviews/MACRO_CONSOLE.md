# Macro console verification — 1 November 2026

The Industry selector now includes **Macro · All industries**. It exposes the ten
existing full-market shocks without changing any economic coefficient: Fed rates,
oil supply, corporate tax, shutdown, household stimulus, inflation, recession,
strong dollar, US–China trade and universal tariffs.

The overview compares all ten industries using a shared signed bar scale and a
financial table. Dollar levels, dollar deltas and percentages stay separate.
Selecting an industry reveals its company Field, exposure plot, inspector and
filtered telemetry. The all-company grid remains available. The new industry CSV
has its own schema; the original company CSV columns are unchanged.

The headline EPS metric retains the existing cap-weighted macro convention;
industry earnings percentages retain summed delta NI / model baseline NI.
One immutable live capture supplies every industry. Missing valuations and
unquantified effects are counted explicitly. Estimates remain estimates; no new
empirical calibration is implied by this interface addition.

Verification completed:

- 610 Python tests passed, five skipped; six retained extreme-EPS review warnings.
- 16 frontend tests passed; TypeScript/Vite production build passed.
- Running HTTP API: 72 industry policies / 261 valid input cases and ten macro
  shocks / 42 valid input cases, zero failures.
- Macro deep link restored the all-industries scope, Fed shock and 100 bp input.
- Financial Services drilldown showed all 30 companies.
- Downloaded industry CSV contains ten industry rows, 19 columns and 234 firms;
  exported NI deltas reconcile to the displayed aggregate.
- Phone layout at 375 px: document width equals viewport width; the financial
  table scrolls inside its own labeled region. Bars have direct signed labels
  and keyboard-operable selection buttons. Existing motion-off/reduced-motion
  rules apply. No browser console errors were observed.
- Methodology shows the dated audit status, current counts and aggregation rules;
  Backtests still displays the actual expanded 81.6% score.

Local preview: `http://127.0.0.1:8788/`. Changes are committed locally, not deployed.
The full audit's five coverage gaps and 72 unresolved empirical verdicts remain
documented in `reports/AUDIT_SUMMARY.md`.

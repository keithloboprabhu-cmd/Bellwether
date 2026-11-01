# Architecture audit — 2026-10-31

## Scope and starting inventory

This is a map of the existing implementation, before the requested calibration changes. The starting inventory is 203 companies, 10 industries, 66 industry policies and 10 market-wide macro shocks. Policy-company coverage has 1,338 explicit decisions. These counts describe configured coverage, not independently verified financial forecasts. `reports/scenarios_before.json` and `reports/backtests_before.json` preserve the starting calculations.

## Configuration and accounting

| Concern | Location | Interpretation |
|---|---|---|
| Industry/company roster | `config/industries.yaml`; `src/policyshock/config.py` | Company identity, industry, subsector, accounting kind, share-unit corrections and predecessor CIKs |
| Industry policies | `config/policies/<industry>/*.yaml`; `policies/schema.py`, `loader.py` | Stable policy ID, input units/defaults/limits, assumptions, channel expressions, persistence and references |
| Exposure definitions | `config/exposure_definitions.yaml` | Units and bounds for company-specific exposure fields |
| Exposure values | `config/exposures/*.yaml` | Low/base/high values, source URL and rationale; `source: estimate` means an assumption, not verified evidence |
| Scope overlays | `config/exposure_scope_audit.yaml`, `company/exposure_audit.py` | Narrow-business scope corrections applied to configured exposures |
| Coverage decisions | `config/policy_company_coverage.yaml`, `policies/coverage.py` | Included, excluded, conditional or unquantified scope, with reasons and independently maintained directions |
| Six channel families | `engine/channels.py` | Tax, cost, demand, price/fees, financing and government spending |
| Accounting templates | `data/baseline.py` | Standard, bank, REIT and managed-care templates; there is no distinct property/casualty insurer template at the start |
| Policy roles | `policies/schema.py`; each policy's `default_role` and `role_overrides` | Neutral, importer, domestic producer; role filters choose channel applicability |
| Macro shocks | `config/macro_shocks/*.yaml`, `macro/aggregate.py` | Shared channels applied across industry baselines |

## Engine path

`engine/simulate.py` builds a runner from registry, annual financial baselines, quote snapshot and FRED macro context. `engine/scenarios.py` resolves `input`, `assumption`, `exposure`, `baseline`, `derived`, `macro` and `role` expressions. Each resolved channel returns a `Delta`.

For a cost shock, exposed costs × shock determine the initial cost increase. Pass-through raises selling prices; elasticity changes volume and therefore sales and variable costs. The code retains revenue and cost changes separately. Other channel families use their own explicit tax, fee, demand, financing or spending formulas.

`engine/model.py` aggregates ΔEBIT and Δinterest into Δpretax. For an unchanged tax rate, ΔNI = Δpretax × (1 − tax rate), adjusted for minority interests. A tax-rate shock also changes the baseline tax burden. Direct after-tax credits enter separately. ΔNI is measured against model baseline pretax × (1 − tax), so a zero shock is exactly zero even when reported net income contains other items. ΔEPS = ΔNI / diluted weighted shares.

`engine/valuation.py` values each channel independently: permanent earnings changes use P/E, one-time changes use one year's ΔEPS, fixed years use an annuity present value at the existing 9% assumption, and direct value channels enter in dollars or as a fraction of share price. The starting implementation has no equity floor and no normalized-earnings fallback: a positive but depressed EPS denominator can exaggerate value changes; negative EPS makes permanent P/E valuation unavailable.

`engine/sensitivity.py` evaluates one-at-a-time drivers and orients low/high endpoints per company rather than applying every numerical low together. These are assumption envelopes, not statistical confidence intervals. Industry bounds and company bounds are calculated separately.

## Data pipeline and limitations

`data/edgar.py` downloads keyless SEC companyfacts and submission metadata, sends a descriptive contact User-Agent and limits each process to eight SEC requests/second. `data/baseline.py` selects full-year 10-K/10-K/A facts (350–380 days), preserves tags and flags, uses latest-filed restatements, and retains the original annual-filing reference. Dollars and share counts become millions; EPS stays dollars/share. Explicit configuration corrects known share-unit changes and predecessor-CIK histories.

At the start, missing debt can become a zero financing exposure, some missing costs use industry-median margins, effective tax rates are clamped to 0–40%, and old companyfacts cover shares can survive into a current baseline. Those are audit targets, not endorsed accounting treatments.

`data/prices.py`/`data/live.py` wrap unofficial Yahoo/yfinance prices and market metrics. `data/fred.py` uses keyless FRED fredgraph CSV. `scripts/refresh_data.py` rebuilds committed snapshots; GitHub Actions schedules weekday updates. Runtime live overlays never rewrite backtest histories.

Minimum refresh ages are five minutes for quotes, one hour for FRED and six hours for SEC financials. The local server uses background jobs. Vercel completes refresh work within requests, prioritizes the scenario industry, rotates Data-page batches (initially 12 quotes, one SEC company, two FRED series), and caches in `/tmp/bellwether`. This is an ephemeral per-instance cache, not a shared database or an always-running market feed. Cold starts read committed snapshots. Provider errors retain usable prior records and their observation times.

## Interfaces and compatibility boundary

The tactical React/Vite interface is `web/`, served with the Python JSON contract in `ui/api.py` and the Vercel `api/index.py` adapter. Streamlit remains in `app.py` and `pages/`. Preserve policy IDs, scenario URLs (`?s={"industry","policy","inputs"}`), the CSV export columns in `web/src/main.tsx`, and `company/profiles.py`'s profile schema. Additional result metadata can be additive.

## Existing validation versus calibration

`policies/audit.py` and `scripts/audit_policies.py` check all policy/company coverage decisions, default/endpoint/zero inputs, six-channel attribution, accounting identities, per-company uncertainty bounds and all ten macro shocks. Separate business-scope and direction expectations detect some exposure errors. Passing these checks does not establish benchmark accuracy: many exposures and transmission parameters are estimates.

`backtests/suite.py` builds ten industry replays, including six correlated TCJA cases, 2022 bank NII, 2018 steel, defense spending and Pell awards. It reports strict directional matches, case-level MAE and no-change MAE. Units differ by case, so there is no pooled magnitude score. Starting pooled directional accuracy is recorded in `reports/backtests_before.json`; historical observations are restated annual data and current exposures, not a point-in-time causal test.

## Reproduce locally

```bash
.venv/bin/python -m pytest -q
npm --prefix web test
npm --prefix web run build
.venv/bin/python scripts/audit_policies.py
PYTHONPATH=src .venv/bin/python -c 'from policyshock.backtests.suite import report; import json; print(json.dumps(report(), indent=2))'
PYTHONPATH=src .venv/bin/python -m policyshock.ui.api
```

After starting the console, `scripts/audit_running_console.py` exercises the HTTP calculation contract. Source verification and per-policy benchmark calibration remain a separate task from these invariant tests. Internet access to primary source pages was confirmed in Phase 0; inaccessible or restricted full constituent lists must be logged, never reconstructed from memory.


## Final audit changes — 1 November 2026

The starting inventory above remains the phase-0 baseline. The active inventory
is now 234 companies, 72 industry policies and ten macro shocks, with 1,694 own-
industry coverage decisions and five unresolved default-coverage gaps. An insurer
template, exact filing supplements, raw tax-rate preservation/normalization,
finance-arm debt separation, current class shares, sourced adjusted-EPS guards and
a zero equity-price floor supersede the starting behaviors described above.
Current paths are `config/macro/` (not `macro_shocks/`) and
`src/policyshock/macro/aggregate.py`. See reports/AUDIT_SUMMARY.md for the evidence
boundary: internal invariant checks pass, but none of the 72 policies has complete
empirical certification.

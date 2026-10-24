# Authoring policies and exposures

How to add a policy to PolicyShock without touching code. Read METHODOLOGY.md §2 for the math.
The worked examples are `config/policies/consumer_retail/*.yaml` and `config/exposures/consumer_retail.yaml`.

## Golden rules
1. **Never invent a number or a citation.** If you can't find a public source, use `source: estimate`
   and a one-line `rationale` that says *why* the value is reasonable. An honest estimate beats a fake cite.
2. **A cited source must say what you claim.** Open the URL and confirm the figure before citing it.
   Prefer the company's own 10-K (segment/geographic revenue notes, risk-factor sensitivities, MD&A),
   government data (BEA, BLS, CMS, EIA, USDA, FRED, CBO, ED), or peer-reviewed papers.
   Put the exact figure and year in `source`, e.g.
   `"Delta 2025 10-K: fuel expense $10.2B of $57.1B operating expense"`, and the link in `source_url`.
3. Every assumption and exposure needs `low ≤ base ≤ high` (fractions for shares: 0.25 = 25%).
4. Defaults should be realistic, middle-of-the-road policy sizes, not extreme ones.
5. If a policy has little real exposure in our 6 companies, keep it and say so in the `description`
   (e.g. "LIHTC exposure in this universe is small"). Don't stretch.

## Files
| What | Where |
|---|---|
| Exposure key definitions | `config/exposure_definitions.yaml` (one file, grouped by industry). Re-use existing keys where they fit; never redefine a key differently. For parallel authoring you may use `config/exposure_definitions.d/<industry>.yaml` temporarily; the loader reads both and rejects conflicting duplicates. |
| Company exposure values | `config/exposures/<industry>.yaml`: **every** exposure key a policy lists must have a value for **all 6** companies in the industry |
| Policies | `config/policies/<industry>/<policy_id>.yaml` |

Exposure definition: `{key, label, unit: fraction|usd_m|count_m|number|per_100bp, help, min, max}`.
Exposure value: `{value, low, high, source, source_url?, rationale?}`.

## Policy schema
```yaml
id: snake_case_id               # == file name; never rename once shipped (deep links use it)
industry: <industry slug>       # == folder name
name: Short human title
description: One or two plain sentences on what the policy does and who it hits.
persistence: permanent | one_time | "years: N"
showcase: false                 # only for the curated demo scenarios
user_inputs:                    # what the user sets; sensible default, min, max, step, unit, help
  - {key, label, unit, min, max, step, default, help}
assumptions:                    # uncertain parameters: low/base/high + source
  - {key, label, unit, low, base, high, source, source_url?, rationale?}
derived:                        # optional named intermediate values (expressions)
  name: expression
channels:                       # one or more; params are numbers or expressions
  - type: <channel type>
    label: Short phrase used in reasons, e.g. "Lower Medicare Advantage rates"
    params: {...}
    roles: [importer]           # optional: apply only to companies with these roles
exposure_keys: [keys used]      # every exposure.<key> you reference must be listed
roles: {NUE: domestic_producer} # optional per-ticker role overrides
default_role: importer          # importer | domestic_producer | neutral
references: [urls]
narrative:                      # optional
  extra: One policy-specific sentence for the auto-generated explanation.
```

### Expressions
Params and `derived` values are arithmetic over these names:
`input.<key>`, `assumption.<key>`, `exposure.<key>`, `derived.<key>`, `baseline.<field>`,
`macro.<key>`, `role.is_importer | role.is_domestic_producer | role.is_neutral`.
Allowed: `+ - * / **`, comparisons, `a if cond else b`, `min()`, `max()`, `abs()`.
Baseline fields ($ millions): revenue, cost_of_revenue, contribution_margin, operating_income,
interest_expense, pretax_income, effective_tax_rate, net_income, diluted_shares, eps_diluted,
total_debt, da, net_interest_income, total_assets, shares_outstanding, price, pe, market_cap.
Macro: fed_funds, treasury_10y, mortgage_30y (all in %), unemployment, pce_musd.
**Convert units explicitly**: inputs in percent → `input.x / 100`; bps → keep as `_bps` params.

### Channel types and params (required, then optional=default)
| type | family | params |
|---|---|---|
| tax_rate | tax | d_statutory_rate; domestic_income_share=1 |
| tax_credit | tax | credit_rate, base_musd |
| tax_revenue | tax | rate, in_scope_share |
| tax_timing | tax | capex_musd, expensed_share; statutory_rate=0.21, discount_rate=0.09, recovery_years=7 |
| cost | cost | exposed_cost_share, shock_pct; pass_through=0, elasticity=0, variable_cost_share=1, dcost_musd=0 |
| domestic_uplift | cost | domestic_sales_share, price_uplift; flow_through=1 |
| demand_transfer | demand | total_transfer_musd, mpc, capture_share; tilt=1 |
| demand_price | demand | dp_consumer, elasticity, exposed_revenue_share |
| demand_volume | demand | d_volume, exposed_revenue_share |
| price | price | d_price, exposed_revenue_share; offset_share=0 |
| financing_debt | financing | d_rate_bps; floating_share=0.3, maturing_share=0 |
| bank_nii | financing | d_rate_bps, nii_sensitivity_per_100bp |
| bank_capital | financing | cet1_ratio, d_ratio; mm_offset=0 |
| reit_nav | financing | d_10y_bps, cap_rate; cap_rate_beta=0.5 |
| gov_budget | government | gov_revenue_share, d_budget_pct; program_relevance=1, fixed_cost_absorption=1 |
| gov_shutdown | government | gov_revenue_share, days; affected_share=1, recovery_share=0, fixed_cost_absorption=1 |
| gov_cr | government | gov_revenue_share, months_delayed; new_award_share=0.1, fixed_cost_absorption=1 |

Notes:
- `cost` with a $-denominated shock (carbon $/t, wage $/hr): set `shock_pct: 0` and put the $M amount in
  `dcost_musd` (e.g. `input.price_per_ton * exposure.scope1_mt` where scope1 is in million tonnes).
- A program in $ (e.g. infrastructure $B) can feed `gov_budget` via a derived share,
  or `demand_transfer` with `mpc: 1` and a capture-share exposure.
- Company kinds: **banks** have revenue = net revenue, cost_of_revenue = 0, contribution_margin = 1, and
  net_interest_income populated. **managed_care** (UNH, ELV, HUM, CVS) cost includes medical claims.
  **REITs** (PLD, AMT, SPG). A demand/price change hits EBIT through contribution_margin.
- Value-only effects (REIT NAV, bank capital, tax timing) show no EPS change; that's intended.

## Check your work
```bash
.venv/bin/python -c "import sys; sys.path.insert(0,'src'); from policyshock.policies.loader import load_registry; load_registry()"
.venv/bin/python -m pytest -q tests/test_policies_smoke.py -k <industry_slug> -W always
```
The smoke test fails on errors or NaN, and warns `REVIEW` for any |ΔEPS| > 100% at defaults. Fix the
defaults or explain why the result is plausible.

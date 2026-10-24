# Methodology

PolicyShock is a **first-order, partial-equilibrium** model for education. It is not investment advice.
This document is kept in sync with the code; section numbers follow the engine modules.

## 1. Data

### 1.1 Baseline financials (SEC EDGAR)
Source: `data.sec.gov/api/xbrl/companyfacts` (all XBRL facts per filer), keyless, with a declared
User-Agent and throttled to 8 requests/second (SEC limit: 10).

Rules (`src/policyshock/data/baseline.py`):
- Only 10-K / 10-K/A / 10-KT facts. Income-statement items must cover **350–380 days**, which drops quarterly facts.
- A fiscal year is identified by its **period-end date** and labelled with that calendar year
  (Walmart's year ending 31 Jan 2026 = FY2026, matching the company's own convention).
- **Restatements:** when several 10-Ks report the same period, the most recently filed value wins.
  The *first* 10-K reporting the period is kept as that year's source link.
- **Tag fallback chains** are applied per year (companies change tags over time); the tag used is recorded.
- Derived values are always flagged:
  - Cost of revenue: `Revenue − GrossProfit`, else `CostsAndExpenses − SG&A − R&D`, else
    `Revenue − EBIT − SG&A − R&D` (only if SG&A or R&D exists; otherwise left missing rather than echoing the EBIT margin).
  - Operating income: `PretaxIncome + InterestExpense` when `OperatingIncomeLoss` isn't tagged.
  - Total debt: the largest available complete-debt measure (partial tags can only understate).
- **Effective tax rate** = tax / pretax income, clamped to [0%, 40%] (40% rather than 35% so pre-TCJA years
  aren't distorted). If pretax income ≤ 0 or tax is missing, 21% is used and flagged.
- **Company templates:** banks use net revenue and net interest income (no cost of revenue; EBIT = pretax income);
  managed-care insurers' cost of revenue = product costs + medical claims incurred; REITs use property operating costs.
- Per-share history is as reported in the latest filing covering each year and is **not split-adjusted across years**.
  Backtests therefore compare tax rates and margins, not EPS levels.

- **Cost-basis override:** a company can set `cost_basis: total_costs_less_overhead` in `config/industries.yaml` when
  its tagged cost of revenue omits large variable costs. Cost of revenue is then CostsAndExpenses − SG&A/G&A − R&D − D&A.
  It is used for Booz Allen, whose subcontractor "billable expenses" sit on a custom-tagged line, and it moves its
  contribution margin from 53% to 22%.

Known limitations: firms that report costs by nature (UPS, FDX, DAL, GD) get a cost of revenue close to total
operating costs, so their contribution margin ≈ operating margin, which understates operating leverage
in demand shocks. Some debt totals (GM, DE) aren't in the standard taxonomy and are flagged.

### 1.2 Prices and valuation
Latest close from yfinance, with a committed snapshot (`data/snapshots/prices.csv`, refreshed every weekday) as fallback.
Market cap = price × cover-page shares outstanding (diluted weighted shares for multi-class issuers whose
class-level counts aren't in companyfacts). P/E = price / diluted EPS, only when EPS > 0.

### 1.3 Macro series (FRED)
Keyless `fredgraph.csv` endpoint: DFF, DGS10, MORTGAGE30US, CPIAUCSL, UNRATE, GDPC1.

### 1.4 Share counts
Market cap uses cover-page shares outstanding, unless they differ from diluted weighted shares by more than 25%.
In that case (a share class missing from the cover page, as at NKE; tagging errors; post-year share issuance) we use diluted
shares and flag it, which keeps market cap on the same share basis as the EPS the model uses.
Near-duplicate period ends (52/53-week calendars tagged a day apart) are collapsed into one fiscal year.

### 1.5 Refresh
`.github/workflows/refresh.yml` runs `scripts/refresh_data.py` every weekday and commits changed snapshots,
so newly filed 10-Ks, prices and macro data reach the app without manual work.

## 2. Engine

Code: `src/policyshock/engine/`. Every policy is a YAML config (`config/policies/<industry>/`) that routes
user inputs, sourced assumptions and company exposures through one or more **channels**.
Parameters are small arithmetic expressions over `input.*`, `assumption.*`, `exposure.*`, `baseline.*`,
`derived.*` and `macro.*`, evaluated by a restricted parser (`expressions.py`) that only allows arithmetic,
comparisons, conditionals and min/max/abs, so a config can never run arbitrary code.

### 2.1 Baseline (latest fiscal year, $ millions)
R revenue · C cost of revenue · EBIT operating income · Int interest · PTI pretax income ·
t effective tax rate · S diluted shares · EPS · cm = (R − C)/R · D total debt · P price · P/E.
Gaps are filled and flagged: a missing cm uses the industry median; a missing PTI uses EBIT − Int.

### 2.2 Channels (`channels.py`)
| Family | Type | Formula |
|---|---|---|
| Tax | `tax_rate` | t' = t + Δτ × domestic income share |
| | `tax_credit` | ΔNI (after tax) = credit rate × base |
| | `tax_revenue` | ΔOpex = R × in-scope share × rate (deductible) |
| | `tax_timing` | full expensing: ≈0 EPS; value = PV of deferral τX(1 − AF(n,r)/n) |
| Cost | `cost` | ΔCost = C × exposed share × shock; dp = φΔCost/R; dQ = −ε·dp; ΔR = R[(1+dp)(1+dQ) − 1]; ΔC = ΔCost(1+dQ) + C·v·dQ |
| | `domestic_uplift` | ΔR = R × domestic share × price uplift; flow-through share to EBIT |
| Demand | `demand_transfer` | ΔR = transfer × MPC × firm capture share × tilt; ΔEBIT = ΔR × cm |
| | `demand_price` | ΔR = R × exposed share × (−ε × dp); ΔEBIT = ΔR × cm |
| | `demand_volume` | ΔR = R × exposed share × ΔVolume; ΔEBIT = ΔR × cm |
| Price | `price` | ΔR = R × exposed share × ΔPrice; ΔEBIT = ΔR × (1 − offset share) |
| Financing | `financing_debt` | ΔInt = D × (floating + maturing share) × Δr |
| | `bank_nii` | ΔNII = NII × sensitivity per 100 bp × Δbps/100 (falls to pretax) |
| | `bank_capital` | value % = ratio/(ratio + Δratio) − 1, scaled by (1 − MM offset); EPS unchanged |
| | `reit_nav` | value % = −β × Δ10yr / cap rate |
| Government | `gov_budget` | ΔR = R × gov share × relevance × ΔBudget%; ΔEBIT = ΔR × cm × absorption |
| | `gov_shutdown` | ΔR = −R × gov share × affected share × days/365 × (1 − recovery) |
| | `gov_cr` | ΔR = −R × gov share × new-award share × months/12 |

**Consumer transfers** are allocated by each firm's share of *all* US consumer spending
(firm US consumer revenue ÷ FRED PCE), not by its share of the six sample companies.
Allocating within the sample would hand the six firms 100% of the industry's spending and overstate the effect.

### 2.3 Aggregation (`model.py`)
```
ΔEBIT = Σ channel ΔEBIT        ΔPTI = ΔEBIT − ΔInt        t' = t + Σ Δt
ΔNI   = (PTI + ΔPTI)(1 − t') − PTI(1 − t) + Σ ΔNI_direct
ΔEPS  = ΔNI / S                ΔEPS% = ΔEPS / reported EPS (n/m if EPS ≤ 0)
```
ΔNI is multiplied by the **parent share** of consolidated profit, NI ÷ (NI + minority-interest income), when a company
reports material noncontrolling interests (FCX 53%, PSN 78%, NUE 86%), so ΔEPS matches EPS attributable to shareholders.
ΔNI is measured against the model's own baseline PTI(1 − t), so a zero shock gives exactly zero even though reported
NI includes minority interests, discontinued operations and so on. The tax-rate effect is applied **once** here; channels only report Δt.
ΔNI splits exactly into per-channel pieces: (ΔEBIT_c − ΔInt_c)(1 − t') + ΔNI_direct_c, plus PTI(t − t') assigned to the tax channels.

### 2.4 Valuation (`valuation.py`), constant-multiple
Each channel's ΔEPS is valued with its persistence: **permanent** × P/E; **one-time** × 1;
**N years** × annuity factor at 9%. Direct value effects (REIT NAV, bank capital, tax-deferral PV) are added.
If P/E isn't meaningful (EPS ≤ 0), a permanent change shows ΔEPS only and the implied price is "n/m".

### 2.5 Ranges and tornado (`sensitivity.py`)
Every uncertain assumption and exposure has low/base/high. **We do not run "all-low vs all-high"**, because
a low value isn't always bad news (low pass-through hurts an importer, but low elasticity helps it). Instead:
1. Tornado: move each driver to its low and then its high, with the others at base, and record industry ΔEPS%
   (Σ ΔNI ÷ Σ baseline NI; Δ market value % for value-only policies).
2. For each company, its pessimistic case sets every driver to whichever end hurt *that company*, and
   its optimistic case to the other end. The industry range uses the same rule on the industry metric.
Exposure drivers move every company's exposure to its own low/high together.

### 2.6 Winners, losers, long/short
Companies are ranked by implied Δprice % (ΔEPS % if n/m). Only companies the policy actually moves are eligible:
unaffected names and names whose % change is n/m (negative baseline EPS) are listed as "not ranked" rather than treated
as zero. If only one company is affected, there is a single call instead of a pair. Long = top, short = bottom, each with a
one-line reason built from its dominant channel and that channel's exposure. If the long's pessimistic
case is below the short's optimistic case, the call is labelled **low conviction**. If every company moves
the same way, the pair is labelled a relative-value trade.

## 3. Backtests
See the Backtests page. **TCJA (2017):** the tax channel run on each company's last pre-TCJA fiscal year predicts the
post-2018 effective tax rate. The fiscal year containing enactment (22 Dec 2017) is excluded as the base year because of
deferred-tax remeasurement, and "actual" is the average of the first two fiscal years starting after 1 Jan 2018.
**Section 232 steel (2018):** the Industrials steel-tariff policy run on FY2017 baselines, compared with FY2017→FY2018
gross-margin changes. Demand conditions confound it, so the test is direction and order of magnitude.

## 4. Out of scope
General-equilibrium and macro feedback, second-round competitive responses, timing within the year,
and non-US policy. This is a first-order, partial-equilibrium model for education, not investment advice.

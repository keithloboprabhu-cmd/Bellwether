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
(firm US consumer revenue ÷ FRED PCE), not by its share of the sample companies.
Allocating within the sample would hand the sampled firms 100% of the industry's spending and overstate the effect.

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

## 4. Full Market (macro shocks)
Code: `src/policyshock/macro/aggregate.py`; configs: `config/macro/*.yaml`. A macro shock has shared inputs and
assumptions plus one block per industry, either channels (an ordinary industry policy run through §2) or an explicit
`effect: none` with a one-line rationale. Effects are summed across industries (partial equilibrium).

- **Headline:** cap-weighted Δ EPS % = Σ market cap × company ΔEPS% ÷ Σ market cap (companies with a meaningful
  ΔEPS%), and implied Δ market value = Σ Δmcap ÷ Σ mcap. Always labelled as the configured-company sample, never "the market".
- **Ranges:** tornado drivers are the union of every industry's uncertain assumptions and exposures, each moved
  across all industries at once. The market range orients each driver by its effect on the headline; company and
  industry ranges are oriented within each industry (§2.5).
- **Sector pair:** industries ranked by implied Δ value % (Δ EPS % if no value); long = top, short = bottom among
  industries the shock actually moves.
- **Second round:** effects such as rate-sensitive spending or retaliation are separate `component`s the user can switch off.
- **Channel scope:** a channel can be limited to statement templates (`company_kinds`), e.g. corporate tax skips REITs and
  loan-loss provisions apply only to banks.

| Shock | Main transmission |
|---|---|
| Fed rate change ★ | bank NII; floating/maturing debt reprices; REIT values via cap rates; (2nd) car and home spending |
| Oil supply shock ★ | producers' realized prices (`oil_price_sensitivity`); carrier fuel cost from CO2 (EIA ≈100 gal/t) less surcharge recovery; manufacturers' energy cost; (2nd) gasoline bill crowds out retail spending (US use ≈137B gal/yr) |
| Inflation surprise | costs (revenue − pretax income) rise × cost β; each industry passes on a share; cost-plus contracts pass through |
| Universal tariff / US–China trade war | `cost` on imported COGS share with pass-through and demand elasticity; US steel uplift; auto tariff exposure scaled; (2nd, China) lost China sales |
| Recession | revenue × industry GDP β × ΔGDP (§4.1) through contribution margin; bank provisions = assets × loan share × Δloss rate |
| Stronger dollar | foreign pretax income × d/(1+d) × (1 − hedged share); importers' COGS fall by low exchange-rate pass-through |
| Corporate tax change | `tax_rate` with each company's US share of pretax income |
| Government shutdown | services contractors' lost billable work; airline capacity cuts in long lapses |
| Household stimulus | `demand_transfer` by share of US consumer spending, with category tilts |

**US share of pretax income** (`mx_us_pretax_share`, `scripts/build_us_pretax_share.py`): the average of up to three recent
years of the 10-K tax-note domestic/foreign split (domestic ÷ (domestic + foreign), or (PTI − foreign) ÷ PTI when only one
side is tagged), clamped to [0, 1], range = min/max year ± 3 pts. Untagged multinationals use explained estimates; other
untagged companies are assumed US-only (low 0.9). Years with US losses can push the share to 0.

### 4.1 GDP revenue betas
Pooled OLS per industry of annual revenue growth on real GDP growth (GDPC1, four-quarter average matched to the fiscal
year end), FY2009 onward, growth winsorized to [−50%, +100%] (`macro/gdp_beta.py`). The recession shock uses the full-sample β
as base and the widest of β ± 1 s.e. across the full and ex-2020–21 fits as its range; a test keeps the config in sync with
`data/snapshots/gdp_betas.json`. R² is low, so industry differences are indicative.

## 4b. Out of scope
General-equilibrium and macro feedback (beyond labelled second-round components), competitive responses, timing within
the year, and non-US policy. This is a first-order, partial-equilibrium model for education, not investment advice.

## 5. Instrument interface and the Field

The web interface calls the existing Python engine through a local HTTP adapter;
it does not implement a second financial model. The Industry headline retains
`Σ ΔNI / Σ model-baseline NI` from §2.3. This is a sample earnings-change measure,
not an average of company EPS percentages or an all-market forecast. The interface
labels its company coverage and scenario bounds explicitly. Long/short comparisons
retain §2.6's ranking and disclose one-sided outcomes as relative comparisons.

The Field encodes each company's fractional EPS change `e` using the fixed mapping
`A = tanh(e / 0.15)`. Thus `0.15` means a 15% EPS change. It never rescales by the
largest value in the current scenario. Undefined EPS percentages have no deformation;
zero has exactly zero deformation. Neither is substituted for the other in tables.

Entity IDs and seed 256 determine stable anchors independently of table order and
shock magnitude. The layout carries no geographical or economic-distance meaning.
For anchor `i`, use the compact weight `w_i = max(0, 1 − (d_i/r_i)^2)^2` inside its
radius and zero outside. Each support radius is 0.8 times the smaller grid spacing,
so no other entity's support reaches an anchor. The terrain is
`h = Σ(A_i w_i) / max(1, Σw_i)`. At an anchor, its own weight is one and all other
weights are zero, so its displayed elevation equals its mapped effect exactly.
The normalized interpolation cannot exceed the most extreme mapped node value.

The renderer uses 5 CSS-pixel cells, a 4×4 Bayer dither and 14 contour levels on each
side of zero, with stronger fifth contours. Positive stipple and negative diagonal
hatching supplement signed labels. Text sits on solid plates. An accessible DOM
table provides exact base/low/high values. The landing terrain is separately labeled
illustrative, with no interpretation as model output. Canvas errors do not prevent
the numerical calculator or table from working. Rendering occurs on data, size,
visibility or selection changes; there is no idle animation loop.

This checkpoint uses committed prices without live overlays. Share URLs and CSVs
carry engine/config and snapshot-content fingerprints. Earlier versions are not
archived by the adapter: a version mismatch is rejected with a route to rerun using
current snapshots. A fingerprint identifies contents; it does not make unavailable
historical versions reproducible.


## 6. Expanded company coverage and user-company scenarios

The configured teaching sample has 203 issuers: 20 in each of nine industries and
23 in Financial Services. Selection spans the business strata documented in
`data/snapshots/sample_coverage.json` (for example banks, custody, payments, asset
management and insurance; managed care, pharmaceuticals, hospitals and devices).
Names, CIKs, financial facts and public quotes are API-sourced. Selection is curated;
it is not a probability sample, industry census or market-representative index.

New issuer policy exposures in `config/exposures/*__expanded.yaml` are **estimates**,
not API financial disclosures. For each documented reference cohort, the base is
the median exposure, low is the minimum low and high the maximum high. Absolute
exposures are scaled by annual revenue; dimensionless values are unchanged. Bounds
are clamped to exposure-definition limits. Scope zeros are explicitly described as
modeling estimates. Bank-only capital/NII channels require the bank template;
non-bank financial issuers have `applicable: false` bank measures. Other economic
effects on those companies are outside these channels. The site-neutral insurer
cost channel applies only to managed-care templates; direct hospital payment
losses are not covered by it. Pharma tariffs apply to the configured drugmakers;
steel-production uplift applies to NUE, STLD and CLF. Peer priors need review before
any company-specific interpretation; their ranges are not confidence intervals.

Parser extensions accept reported operating/borrowing interest tags, bank net
revenue derived from net interest income plus noninterest income, and pretax income
derived from net income plus tax when a pretax tag is absent. Missing diluted share
counts in a loss year may use reported basic weighted shares, with `source: estimate`
and a rationale in the fiscal-year record. These are flagged in the Data page.
Issuer share-count units are normalized only with explicit configuration and a
filing source: MCD reports weighted shares in millions ([FY2025 filing](https://www.sec.gov/Archives/edgar/data/63908/000006390826000035/mcd-20251231.htm));
LINC reports them in thousands ([FY2025 filing](https://www.sec.gov/Archives/edgar/data/1286613/000114036126007380/ef20060592_10k.htm)).
`refresh_data.py` preserves those unit overrides. They apply only to facts filed on or after the documented tagging change (MCD: 2024-02-22; LINC: 2026-03-02); older correctly tagged facts retain their original units.

Public-company lookup searches SEC's issuer directory and uses supported US-GAAP
annual 10-K facts. It can fetch issuers outside the configured sample. Missing
required financials and policy exposures remain blank. Users supply them or
explicitly choose labeled reference-cohort exposure estimates. Unknown-issuer
share counts that conflict with EPS/net income by at least 100× are left blank for
filing review rather than automatically rescaled. Private companies and unsupported
foreign filings use manual profiles. An optional public quote enables valuation;
missing price or nonpositive EPS leaves a constant-P/E valuation undefined.

Profiles use USD millions, millions of diluted shares, USD/share EPS and fractional
tax rates/exposures. Validation rejects non-finite values, unknown fields, unsafe
source links, invalid denominators and broken PTI = operating income − interest +
other income identities. Missing non-bank cost of revenue, bank NII for rate
policies, or debt for debt-financing channels must be supplied. A user profile's
financials, source descriptions, template, role and exposure ranges travel together
in a versioned JSON schema. Import validates that schema before replacing a draft.
Profiles are request-local; inputs are not persisted to the server or encoded in
public share URLs. Browser-session drafts can be downloaded and imported as JSON.

Company scenarios use the same channel, aggregation and oriented-range engine.
Their headline EPS percentage and one-driver sensitivity use ΔEPS / stated positive
starting EPS. If starting EPS is nonpositive, the percentage is unavailable and
sensitivity retains absolute ΔEPS. The P&L bridge uses model NI = PTI × (1 − t)
with any parent-share adjustment, distinct from reported EPS. Industry reference
companies are shown alongside the user company but do not enter its totals,
channel attribution or range. Relative long/short comparisons describe only the
reference sample. Company CSV exports include the profile for reproducibility.


## 7. Tactical console display contract

The console changes presentation, not policy calculations. Its command sequence
unlocks policy selection after an industry, parameters after a policy, and execution
after valid numeric inputs. Parameter edits leave the previously applied scenario
labeled until execution. Loading telemetry shows actual browser request elapsed
time, not a fabricated progress percentage, live market feed or execution stage.

Per-company projected revenue and operating income equal their baseline plus the
engine delta. Projected net income uses the model baseline PTI × (1 − tax rate)
× parent share, plus ΔNI. Projected EPS starts from stated reported/derived baseline
EPS plus ΔEPS; it therefore need not equal projected model NI divided by shares.
Their baselines are identified separately in the grid and income statement bridge.
Each projected value is paired with its percentage change; nonpositive earnings
bases keep percentages undefined. Implied share price is the starting quote plus
the engine's Δprice, respecting each channel's persistence and direct-value effects.
Missing valuation stays undefined. A truly unaffected company can retain its
starting quote even when an earnings multiple is undefined.

EPS sparklines display up to eight actual annual fiscal-year observations from the
committed SEC financial snapshot. Missing observations break the line. Custom
profiles without committed annual history display “No history”; no price paths or
historical points are fabricated. The exposure scatter uses the selected policy's
configured base exposure on X and ΔEPS percentage on Y. Undefined/N/A points are
excluded and counted. Coincident points are not randomly displaced; the company
selector and grid remain available for exact selection. Error bars show configured
scenario bounds, not statistical confidence intervals. Sensitivity variance bars
show existing one-driver low/high runs while the other drivers remain at base.

Motion uses CSS entry/selection transitions, an initialization scan and a request
sweep while waiting. Text remains fully opaque throughout motion. OS reduced-motion
preferences and the console motion toggle disable nonessential animations; the
Canvas renderer remains event-driven and static at rest. Company editing uses
three stages and financial subgroups with preserved source disclosures and the
same validation/profile schema.

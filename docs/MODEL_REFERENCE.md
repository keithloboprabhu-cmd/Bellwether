# Modeling reference

Bellwether is a **first-order, partial-equilibrium** model for education. It is not investment advice.
Detailed accounting, calibration and data rules supporting the high-level methodology.

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
Latest available five-minute yfinance market observation, with a committed price snapshot as fallback; see §8 for refresh and observation timing.
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

## 3. Historical backtests and directional accuracy

`backtests/suite.py` supplies the web and Streamlit Backtests pages. There is one
historical case for each configured industry. Six industries (TMT, retail,
healthcare, energy, transportation, and corporate hospitality) replay the 2017
TCJA tax cut. Other cases are 2022 Fed tightening / bank net interest income,
2018 Section 232 tariffs / industrial gross margins, the FY2019 defense budget
agreement / contractor revenue, and the 2023–24 Pell increase / education revenue.
The original TCJA and steel modules remain available for their original checks.

**Overall directional accuracy** = 100 × same-sign modeled/observed changes ÷
eligible company-case comparisons. A zero observed change misses a nonzero
prediction. Missing values, zero modeled changes and out-of-scope companies are
excluded, with every configured company accounted for in the displayed exclusions.
A numerical epsilon of 1e-9 handles roundoff only. Company-cases have equal weight;
the separate equal-industry score averages the ten sector hit rates. Neither score
is a probability of a future forecast being correct. MAE = mean |predicted − observed|
and the zero-change benchmark MAE are reported separately for each case, in its own
units. Incompatible magnitudes are never pooled into an overall accuracy percentage.

TCJA uses every eligible non-REIT with positive pre-policy pretax income, complete
engine inputs and a raw base effective rate between 0% and 100%. The base ends
before December 2017; observed rates average the first two full fiscal years starting
on or after 1 January 2018. Pre-policy domestic/foreign pretax tags determine the
US income share; incomplete splits use `source: estimate` with an explicit 100%
domestic rationale. Raw post-policy tax observations, including one-offs, remain
in the comparison. REITs and missing/loss baselines are listed as exclusions.

Other cases use current policy channels, default assumption bases and current
exposures on historical statements. Bank shock = the FY2021→FY2022 change in
annual-average daily DFF from the committed FRED history. Defense input =
(716 / 700 − 1) × 100, the FY2019/FY2018 national-defense budget-agreement toplines,
not actual contractor receipts. Pell input = (7,395 / 6,895 − 1) × 100, the enacted
maximum award increase, used as a per-student-funding proxy. Revenue comparisons
use the last annual period ending before the policy date and the first full annual
period starting after it. Fiscal starts use the preceding annual end + one day
when available, otherwise the prior calendar-year anniversary + one day. Steel
retains its existing NUE/CAT/DE cohort and consistent-cost calculation.

Every case links the primary policy source and the actual SEC filing records.
These are **retrospective current-model replays**, not a point-in-time forecast
archive: current exposures, subsequently restated financials, fiscal timing,
acquisitions and other economic changes can affect results. Six cases share a
single TCJA episode, so outcomes are correlated. Annual actuals do not identify
an isolated causal policy effect. No thresholds, exposures or cohorts are fitted
to improve the displayed hit rate. Backtests always read committed historical
snapshots and never incorporate the live-data overlay described in §8.

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
effects on those companies are outside these channels. The site-neutral policy separates managed-care claims savings from estimated Medicare hospital-outpatient revenue losses at providers. Pharma tariffs apply to the configured drugmakers;
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


## 8. Current public data and source freshness

The local server starts independent background refreshes through `data/live.py`:
Yahoo five-minute quotes every five minutes, FRED series every hour, and SEC annual
financial statements every six hours. No paid service or runtime model call is
used. Cold starts immediately serve committed fallback data while providers load.
Successes are cached in ignored `data/cache/live/state.json`; failed/partial sources
retain prior values with original observation/retrieval times and a visible error.
The refresh endpoint coalesces concurrent jobs and obeys the provider intervals.

Yahoo intraday observations carry their actual UTC market timestamp, including
when the market is closed. Retrieval time is separate and does not make a Friday
observation a Sunday trade. Yahoo may delay or rate-limit data; this is not an
exchange-certified real-time feed. On-demand company metrics refresh with a
five-minute cache and identify Yahoo's market cap, enterprise value, trailing and
forward P/E/EPS, TTM revenue/net income/margins and shares separately from SEC annual
simulation inputs. Missing API fields remain unavailable. Provider-reported currency
is shown for market and financial metrics.

FRED uses its free keyless fredgraph CSV endpoint and keeps each series' observation
date; economic values update only on their release schedules. The latest values
feed the same `macro_context` names used by the policy engine. Current FRED values
never overwrite the committed history used for backtests or calibrated GDP betas.

SEC refreshes use the existing descriptive User-Agent, shared 8 requests/second
limit, predecessor-CIK merging, company templates and documented unit overrides.
The income statement remains the latest supported **annual** 10-K, not a real-time or TTM statement. Yahoo TTM figures are available separately and are not
mixed into annual statement identities. Unsupported or incomplete newer annual
records retain the prior baseline. Current financing and valuation inputs use the
latest captured quote and latest supported annual debt/share records.

Each simulation freezes one immutable capture of available prices, macro values and
annual company records. A concurrent refresh cannot change inputs partway through
a run. The capture fingerprint, timestamp and source status accompany results and
CSV exports. Existing results remain as calculated until executed again. User
company profiles retain their supplied financial inputs, use current macro context,
and can reload public company data explicitly. The Data page polls source status
and available rows every 30 seconds; provider polling remains server controlled.


## 9. Policy scope and regression audit

Run `.venv/bin/python scripts/audit_policies.py` to regenerate
`design/reviews/POLICY_AUDIT.md` and its machine-readable JSON. It covers all 66
industry policies and all 10 macro shocks using committed financial baselines.
The report records a code/config/data fingerprint, affected and neutral firms,
input and driver cases, source references, estimated inputs and remaining coverage
limits. `tests/test_policy_audit.py` makes the boundary, accounting and economic
expectations part of the normal test suite. A new industry policy requires a
review entry in `config/policy_review.yaml`; assertions are economic expectations
maintained separately from calculated output.

Checks include defaults, each legal input endpoint, all input endpoint combinations,
legal all-zero inputs (earnings **and valuation** must be zero), each uncertain
coefficient/exposure endpoint, finite values, nonnegative modeled revenue/COGS,
EPS/share identity, exact NI and value attribution, tax bounds and oriented
per-company scenario ranges. `config/policy_company_coverage.yaml` independently
records every valid industry-policy/company pair (1,338 across 203 companies and
66 policies), including status, business rationale and expected default direction
for each included firm. The audit rejects incomplete rosters, missing expected
effects, wrong directions and excluded firms changing at uncertainty endpoints.
Unquantified central exposures may have an explicitly estimated high sensitivity
case; that is disclosed as uncertainty rather than a measured zero. Macro checks
cover every input corner, each uncertain-driver endpoint and explicitly unaffected industries; the existing macro
suite also tests ranges and cross-sector directions. These tests do not establish
that every possible combination of uncertain assumptions is economically realistic.

`config/exposure_scope_audit.yaml` defines direct-channel business boundaries.
`config/company_exposure_overrides.yaml` retains company-specific corrections,
with filing context and an explicit rationale for every estimate. Both are applied
to canonical exposure YAML by `scripts/apply_exposure_audit.py`; universe expansion
uses the same rules so a peer median cannot silently undo reviewed business scope.

FDIC bases use `config/fdic_bank_subsidiaries.yaml` and the dated official reports
in `data/snapshots/fdic_assessment_bases.json`. Refresh with
`.venv/bin/python scripts/refresh_fdic_exposures.py --report-date YYYYMMDD`, then
`scripts/apply_exposure_audit.py`. The keyless FDIC request validates certificate
numbers, parent identities, complete responses and units before writing. The
assessment proxy is the sum of insured subsidiaries' quarter-end assets less
Tier 1 capital, in $M; it is not a holding-company revenue multiple. Statutory
quarterly averages and special adjustments are not reported by that request.
BNY/STT custody deductions use an explicit estimated residual factor (55%, 30–80%
range); other bases use ±10% timing sensitivity. These are estimates, not invoices.
The selected-bank mapping must be reviewed after mergers and is not a certified
inventory of every insured legal entity. AIG has no modeled insured-bank base;
insurance-guaranty-fund assessments and counterparty spillovers are distinct risks.

Fixed-price contract conversion holds revenue constant and changes operating
costs to match the assumed margin change. SPR/refinery assumptions hold stand-alone
refining margins unchanged; upstream peer sensitivities do not transfer to refinery
earnings. The signed FCX diesel proxy changes costs, not mineral sales revenue,
in both SPR and broad oil-price scenarios.
For example, continuing Cigna/Ally exposure excludes sold MA/card businesses;
Laureate's foreign institutions do not inherit US student-aid revenue; Intel/Micron
have estimated US manufacturing capex; hotels, vehicle-credit sellers/buyers and
securities-trading businesses use business-specific inputs. Pharmaceutical import
exposure has its own key: medical devices are excluded from drug/API tariffs but
retain their generic goods-import exposure for broad macro tariffs. A filing URL alone
does not make an estimated business/geographic share reported data. These static
exposures need re-review after corporate actions; refreshing SEC totals does not
refresh every policy-specific ratio automatically.

Site-neutral reimbursement includes separate insurer claims savings and hospital
Medicare outpatient revenue losses (HCA/THC/UHS). The provider share is an explicit
estimate excluding inpatient care and standalone ASCs, with a separate eligible-
services fraction. Medicaid provider exposure is a patient-volume proxy with wide
ranges; supplemental payments and uncompensated care are not separately modeled.
LIHTC has no sourced qualified investment basis in this sample and therefore shows
an explicit coverage notice instead of inventing a benefit. Custom companies may
supply a supported basis; unknown policy exposures still require user input or an
explicit opt-in to peer estimates.

CET1, depreciation timing and exchange-liquidity policies change equity value without changing GAAP earnings. Direct value attribution uses shares outstanding (diluted-share fallback), matching the market-value calculation. Undefined valuation stays missing.

Absolute-dollar operating cost changes in the generic cost channel are classified
as operating expense, while COGS-linked shocks remain in cost of revenue. Both
retain the original volume response and unchanged total EBIT/NI formula. This
prevents bank bonus savings or a property-tax cut from creating a negative COGS
line when the statement has zero/tiny cost of revenue.

The audit is internal model verification, not independent assurance or causal
forecast validation. Large percentage effects on small earnings bases and implied
losses beyond equity value are retained as review warnings rather than clipped or
claimed precise. The backtest headline remains calculated from actual eligible
comparisons; after the scope audit it is 104/120 = 86.7%, including liability-
sensitive Citi and excluding Laureate from the US Pell replay. No target accuracy
percentage is hardcoded or preserved by selecting favorable outcomes.

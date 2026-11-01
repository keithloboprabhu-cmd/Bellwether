# Methodology

Reported financials set the baseline. Company-specific exposure and policy assumptions determine the change in earnings and equity value.

## 1. Data & baselines

Build a consistent starting point from company filings, market observations and economic data.

### Data sources

| Source | What enters the model | Refresh checks |
|---|---|---|
| SEC EDGAR | Latest supported annual revenue, costs, profit, debt and shares | Every six hours |
| Yahoo Finance / yfinance | Latest available share-price observation; additional market and TTM metrics are available separately | Every five minutes |
| FRED | Interest rates, inflation, GDP, employment and consumer spending | Every hour |

### Reported figures

Company financials come from annual filings. Industry-specific accounting templates distinguish banks, insurers, REITs and operating companies. Dollar financials use USD millions; shares use millions; per-share figures use dollars.

### Estimated exposures

Filings and public APIs do not provide every policy-specific input. Domestic sales shares, covered labor, qualifying investment and pass-through can require sourced estimates or explained peer assumptions. Estimates have a rationale and a low, base and high value. Refreshing financial statements does not automatically update these exposures.

### Data quality & timing

Annual statements, market quotes and economic releases keep their own observation dates. Refresh checks do not create new observations: markets close, filings arrive periodically and FRED series follow release schedules. Missing or incomplete updates retain the last usable record. Derived financials and defaults are flagged; unsupported percentages remain undefined. Each calculation uses one frozen capture of the available inputs.

On Vercel, refreshes run during requests rather than continuously in the background. Scenarios prioritize quotes for their industry; each request checks at most one company's annual statements and two FRED series. The Data page requests all due company quotes through bounded Yahoo batches rather than stopping at twelve. The intervals above are per-record minimum ages, not guaranteed publication or refresh times. Temporary caches belong to each running instance and can reset; committed snapshots provide the cold-start fallback. Historical backtests always use committed records.

Reviewed inline-XBRL supplements recover facts omitted from companyfacts, including dimensional industrial/finance-arm debt and class-specific cover-page shares. They apply only to the verified issuer and fiscal period, retain the filing concept/context, and expire when a new annual period arrives. Ford, GM, Deere, PACCAR and Textron keep finance-arm debt separate; the ordinary debt-repricing channel uses industrial borrowings. Operating lease liabilities stay separate from floating-rate borrowing exposure. Missing debt is unquantified, not a reported zero.

Reported tax rates remain available. Rates outside the existing 0–40% anomaly screen use the median ordinary rate from the preceding three available annual periods, or the documented US federal statutory rate when history is insufficient. This replaces clipping to 0% or 40%; state and foreign adjustments are not fabricated. The screen and historical-median choice remain modeling conventions requiring judgment.

## 2. Policy transmission

A company is affected through the business it actually operates. Exposure determines which part of its revenue, costs, financing or asset value a policy reaches.

Steel tariffs distinguish average buyer prices from domestic mill selling prices. USITC Publication 5405, table 5.2 calibrates separate historical responses under 25% Section 232 tariffs: 2.39% for average steel prices and 0.74% for domestic producer prices. Observed company EPS growth includes tax, volume, mix and other changes, so it is not substituted for a causal tariff sensitivity.

### Transmission channels

| Channel | Financial mechanism | Typical policy |
|---|---|---|
| Tax | Change the tax rate, a qualifying credit or the timing of cash taxes | Corporate tax change; manufacturing investment credit |
| Costs | Apply a shock to covered costs, allowing for price pass-through and demand response | Import tariff; minimum-wage increase |
| Demand | Change sales volume or allocate new spending using a company capture share | Consumer rebate; enrollment change |
| Prices & fees | Change the price or fee earned on an exposed revenue stream | Card interchange cap; Medicare reimbursement |
| Financing | Reprice debt or bank interest income, or change returns on capital and property values | Interest-rate change; higher bank capital requirement |
| Government | Change relevant contract revenue, funding or the timing of awards | Defense budget; government shutdown |

### Company scope

Exposure follows the policy's direct business scope. A drug tariff excludes medical-device revenue; a card-fee cap affects covered issuers; a manufacturing credit requires qualifying investment. A firm can have no direct effect because it is outside scope, already above a wage floor, below a binding threshold, or lacks a quantified exposure. A zero is not automatically a model failure.

FDIC deposit-insurance assessments apply to insured bank subsidiaries, not insurance-company premiums. AIG therefore has no direct assessment in this channel. Bank-counterparty and insurance-guaranty-fund risks are separate effects. Bank assessment estimates use identified FDIC subsidiary reports; quarter-end assets less Tier 1 capital approximate the statutory quarterly-average base. Custodial deductions and timing remain explicit estimates.

Results distinguish an excluded business, a nonbinding setting, a zero shock, an unquantified exposure and an effect on equity value with unchanged EPS. An unquantified exposure is a coverage gap, not a measured economic zero. Some uncertain qualifications are explored only in the high sensitivity case.

### Assumptions & responses

Each policy defines the shock, company exposures and response assumptions. Pass-through describes how much cost reaches customers; elasticity describes how demand responds; offsets describe savings or replacement revenue. These assumptions vary by policy. Broad macro scenarios reuse the same financial channels across industries; additional spending or demand effects are included only when explicitly specified. All ten industries use a single captured set of statements, quotes and economic data. Industry earnings percentages divide summed net-income changes by model starting earnings. The cross-industry EPS headline is market-cap weighted across companies with meaningful EPS percentages and usable quotes. Industry/value totals include only supported valuations; missing effects are counted separately rather than asserted to be economic zeros.

### Consumer spending

Transfers are allocated against total US consumer spending from FRED, with company exposure and category tilts. The selected company sample does not receive the entire transfer.

## 3. Earnings & value

Calculate the change in revenue, operating profit, taxes and earnings. Then value the effect according to how long it lasts.

### An illustrative calculation

| Step | Calculation | Result |
|---|---|---|
| Cost increase | $600M annual costs × 40% exposed × 10% shock | +$24M costs |
| Net-income change | −$24M × (1 − 20% tax rate) | −$19.2M earnings |
| EPS change | −$19.2M ÷ 100M diluted shares | −$0.192 per share |
| Implied price change | −$0.192 EPS × 20× P/E | −$3.84 per share |

### Example assumptions

This is an illustrative company, not a reported issuer or a forecast. It assumes no cost pass-through, no demand change, a 20% tax rate, 100 million diluted shares and a permanent earnings effect valued at 20× earnings. Changing those assumptions changes the result.

### Valuation rules

| Duration | Valuation method |
|---|---|
| Permanent | Earnings-per-share change × supported earnings multiple |
| One-time | Approximately the one-time per-share earnings effect |
| Fixed number of years | Present value of annual per-share effects, discounted at 9% |
| Direct value effect | Separate capital, property-value or cash-tax-timing calculation |

### Earnings can stay unchanged

Higher bank capital requirements, tax-depreciation timing and property-liquidity effects can change equity value without changing current earnings. Conversely, a loss-making company can have a dollar earnings impact while its EPS percentage or P/E-based valuation is undefined. Implied price changes are scenario calculations, not price targets.

If reported EPS is nonpositive or more than 40% below the median of the latest three complete annual EPS observations, permanent valuation requires price divided by a positive, verified three-year median of issuer-adjusted EPS. Reported EPS and its percentage-change denominator remain unchanged. The method and source periods are labeled. Special items are removed only using sourced issuer reconciliations. An unadjusted reported median is not treated as normalized earnings; if no supported positive adjusted series exists, permanent valuation stays unavailable rather than inventing EV/EBITDA inputs.

Projected traded-equity prices cannot fall below $0. A binding floor is labeled **equity wiped out**. Operating losses and EPS changes remain uncapped. The unconstrained price delta is retained, and a separate limited-liability reconciliation preserves channel attribution. This is a valuation boundary, not proof of a bankruptcy forecast.

### Accounting details

Channel effects add to operating profit and interest expense. The combined pretax change is taxed once. Net-income change is measured against model baseline pretax profit × (1 − tax rate), then adjusted for material minority interests. EPS change equals net-income change divided by diluted shares. Reported starting EPS and model baseline net income can differ, so their projected levels are kept distinct.

## 4. Ranges & sensitivity

Use assumption ranges to understand what moves the result and which companies are most exposed.

### One driver at a time

Move one exposure or assumption to its low and high settings while keeping the others at base. This identifies the inputs that have the greatest effect on the estimate.

### Company-specific bounds

For each company, build a downside scenario from the ends that hurt it and an upside scenario from the ends that help it. A lower input is not always worse: lower cost pass-through can hurt an importer, while lower demand elasticity can help it. Sample-level ranges use the same process for the aggregate measure.

### What the range means

These are scenario bounds for the configured model and input ranges. They are not statistical confidence intervals, probabilities or guaranteed worst and best outcomes. Interactions, correlated assumptions and extreme shocks can extend beyond this approximation.

### Comparing companies

Sample earnings change is total net-income change divided by total model baseline earnings. It is not an average of company EPS percentages. Company comparisons use implied price percentage changes, with EPS percentage as a fallback when meaningful. If all affected firms move the same way, the comparison identifies relative exposure rather than an outright winner and loser.

## 5. Validation & limits

Check internal consistency and business scope, then compare selected historical policy episodes with observed company outcomes.

### Policy checks

Every configured industry policy has an explicit coverage decision for every company in its industry: 1,694 decisions across 234 companies and 72 policies. Covered firms have default-direction expectations; the audit also fails if an expected effect is missing across tested inputs. Excluded firms must stay unaffected at input limits and uncertainty endpoints. Checks cover valid zero shocks, attribution, accounting identities and scenario ranges. All 10 macro shocks are checked across the 234-company sample and at their input and driver endpoints. Passing an internal audit verifies these checks; it does not establish forecasting accuracy.

### Historical comparisons

Backtests compare modeled and observed changes for at least one historical case per industry, with additional non-TCJA episodes and expanded steel coverage. Directional accuracy is the share of eligible company-case comparisons with the same predicted and observed sign. Missing observations, unquantified exposure and zero modeled changes are excluded; a zero observed change is a miss for a nonzero prediction. Error magnitudes are compared within each case's own financial units.

### Interpreting backtests

These are retrospective replays using the current model, not forecasts saved before the event. Current exposures, restated statements, acquisitions and other economic changes can affect the comparison. Several industry cases share the same tax-cut episode, so outcomes are correlated. The historical hit rate is not the probability that a future prediction will be correct, and observed company changes do not isolate a policy's causal effect.

### Model boundaries

The model estimates direct, first-order effects while holding other relationships broadly fixed. It does not fully capture competition, substitution, management responses, policy implementation timing or economy-wide feedback. Company exposures can be estimates; sparse disclosures and small earnings bases can make percentage results unstable. Unknown custom-company inputs require user-supplied values or an explicit choice of peer estimates. A missing qualifying exposure remains unquantified instead of receiving an invented impact.


### Audit status (1 November 2026)

The active universe has 234 companies across ten industries, with 72 industry policies and ten macro shocks. The original roster and scenarios are preserved in the audit reports. Thirty-one supported public companies were added from the publisher-verified Fortune ranking, separately labeled OEF holdings cross-check and requested candidate list. This does not certify full S&P 100 membership: the publisher's complete roster was not obtained. Private/mutual companies and Fannie/Freddie are listed separately; unsupported statements and ambiguous share bases remain outside the active sample.

The insurer statement template uses incurred policy claims and loss-adjustment expenses rather than merchandise COGS. Visa uses class-A EPS and the filing's total class-A-equivalent diluted shares. Captive finance debt and operating leases are separated from industrial borrowings.

Tetra Tech explicitly uses revenue less reported gross profit as its full revenue-cost base: the generic cost tag captures subcontractors only. FY2025 cost is $4,481.246M, comprising $825.230M of subcontractor costs and $3,656.016M of other revenue costs. The resulting 17.66% gross-margin proxy still does not establish an incremental profit margin. This issuer-specific reconciliation is not automatically applied to excise-tax or premium-tax presentations.

The baggage-fee scenario uses each carrier's own FY2025 BTS observation for American, Delta, United and Southwest, divided by its consolidated annual revenue. Fixed measurement bounds describe historical observations; fare recapture remains uncertain. Southwest's fee introduction during 2025 makes its base a partial-year observation. American and Delta domestic passenger shares use their own annual geographic tables; geographic revenue remains a proxy for the statutory ticket-tax base.

The global oil-price scenario uses reported worldwide annual fuel consumption for those four airlines, separately from US-only carbon-charge exposure. Other carriers retain the existing CO2-derived fallback with geographic limitations. Converting barrels to gallons is a physical identity; one-for-one transmission from Brent to jet-fuel or diesel prices is an unverified model assumption.

Six rate-only corporate-tax scenarios use the submitted S.Amdt.2428 proposal (21% to 28%). They are explicitly proposed scenarios, not enacted law. Only positive, sourced US pretax book income from a US-incorporated issuer is quantified. Book income approximates taxable income; credits, minimum taxes, foreign-income provisions, tax losses and deferred-tax remeasurement are excluded. Income-history bounds are observed annual values, not confidence intervals. An Irish issuer's “domestic” income is not assumed to be US income.

Current default coverage is 229 of 234 companies. BLK, PGR, SLM, LYFT and MDT remain explicit coverage failures pending the reconciliations in `reports/coverage_gaps.md`. Passing accounting and scope tests does not resolve those failures or validate unsourced exposures. Every default absolute EPS change above 50% is flagged for review; input limits are not represented as independently verified realistic ranges.


Capital One has a sourced adjusted annual EPS series: 2023 $12.52, 2024 $13.96, 2025 $19.61; the median is $13.96. These are the issuer's non-GAAP reconciliations, not invented removals. Some excluded amortization can recur, and pre-Discover years are not pro-forma comparable with the merged company. Other depressed/negative-EPS issuers without a verified adjusted series retain unavailable permanent valuation; direct equity-value channels can still be calculated independently of EPS.

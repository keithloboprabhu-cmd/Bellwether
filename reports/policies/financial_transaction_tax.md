# Financial transaction tax

Policy `financial_services/financial_transaction_tax` · evidence checkpoint 2026-11-01 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

A tax on the value of US securities trades. Higher trading costs cut trading volume, which hurts dealers' sales-and-trading revenue; Goldman, with the largest markets business relative to its size, is hit hardest and Amex not at all.

Duration: `permanent`. Default inputs: `{"rate_bps": 5.0}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| demand_volume | unavailable / unavailable | {"d_volume": "derived.d_volume", "exposed_revenue_share": "exposure.trading_revenue_share"} |
| cost | unavailable / unavailable | {"exposed_cost_share": 0.0, "shock_pct": 0.0, "dcost_musd": "derived.d_trading_rev * assumption.variable_comp_ratio"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://www.sec.gov/Archives/edgar/data/886982/000088698226000091/gs-20251231.htm
- https://www.imf.org/en/Publications/WP/Issues/2016/12/31/Taxing-Financial-Transactions-Issues-and-Evidence-24702

| Company | Configured status | Basis |
|---|---|---|
| JPM | included | Transaction tax reduces trading volume and imposes modeled absorbed costs. |
| BAC | included | Transaction tax reduces trading volume and imposes modeled absorbed costs. |
| WFC | included | Transaction tax reduces trading volume and imposes modeled absorbed costs. |
| GS | included | Transaction tax reduces trading volume and imposes modeled absorbed costs. |
| C | included | Transaction tax reduces trading volume and imposes modeled absorbed costs. |
| AXP | outside_scope | This model covers dealer/trading revenue lost from lower securities volume. Investor portfolio taxes, insurer portfolios, asset-manager AUM and payment-network fees are separate effects. |
| MS | included | Transaction tax reduces trading volume and imposes modeled absorbed costs. |
| SCHW | included | Transaction tax reduces trading volume and imposes modeled absorbed costs. |
| BNY | included | Transaction tax reduces trading volume and imposes modeled absorbed costs. |
| STT | included | Transaction tax reduces trading volume and imposes modeled absorbed costs. |
| USB | included | Transaction tax reduces trading volume and imposes modeled absorbed costs. |
| PNC | included | Transaction tax reduces trading volume and imposes modeled absorbed costs. |
| TFC | included | Transaction tax reduces trading volume and imposes modeled absorbed costs. |
| COF | included | Transaction tax reduces trading volume and imposes modeled absorbed costs. |
| FITB | included | Transaction tax reduces trading volume and imposes modeled absorbed costs. |
| HBAN | included | Transaction tax reduces trading volume and imposes modeled absorbed costs. |
| KEY | included | Transaction tax reduces trading volume and imposes modeled absorbed costs. |
| ALLY | included | Transaction tax reduces trading volume and imposes modeled absorbed costs. |
| MA | outside_scope | This model covers dealer/trading revenue lost from lower securities volume. Investor portfolio taxes, insurer portfolios, asset-manager AUM and payment-network fees are separate effects. |
| BLK | outside_scope | This model covers dealer/trading revenue lost from lower securities volume. Investor portfolio taxes, insurer portfolios, asset-manager AUM and payment-network fees are separate effects. |
| AIG | outside_scope | This model covers dealer/trading revenue lost from lower securities volume. Investor portfolio taxes, insurer portfolios, asset-manager AUM and payment-network fees are separate effects. |
| PRU | outside_scope | This model covers dealer/trading revenue lost from lower securities volume. Investor portfolio taxes, insurer portfolios, asset-manager AUM and payment-network fees are separate effects. |
| PGR | outside_scope | This model covers dealer/trading revenue lost from lower securities volume. Investor portfolio taxes, insurer portfolios, asset-manager AUM and payment-network fees are separate effects. |
| ALL | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| MET | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| SNEX | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| SPGI | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| TRV | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| V | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |
| PYPL | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |

## B. Every in-scope exposure

Exact numeric checks are distinguished from filing links and estimates. UNVERIFIED values are retained, not silently replaced. Historical observed low/high values are not forecast confidence intervals.

| Company | Exposure | Base | Low | High | Exact-source status | Primary source / location / rationale |
|---|---|---:|---:|---:|---|---|
| JPM | trading_revenue_share | 0.149 | 0.12 | 0.2 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/19617/000162828026008131/jpm-20251231.htm · JPMorgan 2025 10-K consolidated statement of income: principal transactions $27,212M of $182,447M total net revenue; Principal transactions proxies volume-driven Markets revenue; high adds Markets NII and commissions, low strips financing-type revenue. · Principal transactions proxies volume-driven Markets revenue; high adds Markets NII and commissions, low strips financing-type revenue. |
| BAC | trading_revenue_share | 0.188 | 0.106 | 0.188 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/70858/000007085826000157/bac-20251231.htm · Bank of America 2025 10-K: Global Markets total revenue $24,096M less investment banking fees $2,837M = $21,259M sales and trading, of $113,097M total revenue; Low uses only consolidated market making and similar activities ($12,014M). · Low uses only consolidated market making and similar activities ($12,014M). |
| WFC | trading_revenue_share | 0.0615 | 0.05 | 0.09 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/72971/000007297126000133/wfc-20251231.htm · Wells Fargo 2025 10-K Table 6: net gains from trading activities $5,147M of $83,699M total revenue; High adds an allowance for Markets trading NII and commissions, which the 10-K does not split out. · High adds an allowance for Markets trading NII and commissions, which the 10-K does not split out. |
| GS | trading_revenue_share | 0.336 | 0.309 | 0.533 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/886982/000088698226000091/gs-20251231.htm · Goldman Sachs 2025 10-K: FICC intermediation $10,271M + Equities intermediation $9,340M = $19,611M of $58,283M net revenues; Low is consolidated market-making revenue ($17,993M); high adds FICC and Equities financing (total FICC + Equities $31,057M). · Low is consolidated market-making revenue ($17,993M); high adds FICC and Equities financing (total FICC + Equities $31,057M). |
| C | trading_revenue_share | 0.258 | 0.18 | 0.258 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/831001/000083100126000011/c-20251231.htm · Citigroup 2025 10-K segment revenues: Markets $21,970M of $85,225M total net revenues; Low strips out an estimated financing/securities-lending share less sensitive to per-trade costs. · Low strips out an estimated financing/securities-lending share less sensitive to per-trade costs. |
| MS | trading_revenue_share | 0.27 | 0.2 | 0.35 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/895421/000089542126000086/0000895421-26-000086-index.htm · estimate; Company-specific estimate of revenue sensitive to covered securities trading volume. Separates broker/dealer, custody, regional banking and card/auto lending business models instead of copying Goldman/JPMorgan shares. Excludes unrelated custody fees, net interest, FX-only trading and asset management. Wide range; not a disclosed US taxable-securities segment or transaction notional. · Company-specific estimate of revenue sensitive to covered securities trading volume. Separates broker/dealer, custody, regional banking and card/auto lending business models instead of copying Goldman/JPMorgan shares. Excludes unrelated custody fees, net interest, FX-only trading and asset management. Wide range; not a disclosed US taxable-securities segment or transaction notional. |
| SCHW | trading_revenue_share | 0.14 | 0.08 | 0.2 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/316709/000031670926000009/0000316709-26-000009-index.htm · estimate; Company-specific estimate of revenue sensitive to covered securities trading volume. Separates broker/dealer, custody, regional banking and card/auto lending business models instead of copying Goldman/JPMorgan shares. Excludes unrelated custody fees, net interest, FX-only trading and asset management. Wide range; not a disclosed US taxable-securities segment or transaction notional. · Company-specific estimate of revenue sensitive to covered securities trading volume. Separates broker/dealer, custody, regional banking and card/auto lending business models instead of copying Goldman/JPMorgan shares. Excludes unrelated custody fees, net interest, FX-only trading and asset management. Wide range; not a disclosed US taxable-securities segment or transaction notional. |
| BNY | trading_revenue_share | 0.02 | 0.005 | 0.06 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/1390777/000139077726000033/0001390777-26-000033-index.htm · estimate; Company-specific estimate of revenue sensitive to covered securities trading volume. Separates broker/dealer, custody, regional banking and card/auto lending business models instead of copying Goldman/JPMorgan shares. Excludes unrelated custody fees, net interest, FX-only trading and asset management. Wide range; not a disclosed US taxable-securities segment or transaction notional. · Company-specific estimate of revenue sensitive to covered securities trading volume. Separates broker/dealer, custody, regional banking and card/auto lending business models instead of copying Goldman/JPMorgan shares. Excludes unrelated custody fees, net interest, FX-only trading and asset management. Wide range; not a disclosed US taxable-securities segment or transaction notional. |
| STT | trading_revenue_share | 0.015 | 0.005 | 0.04 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/93751/000009375126000124/0000093751-26-000124-index.htm · estimate; Company-specific estimate of revenue sensitive to covered securities trading volume. Separates broker/dealer, custody, regional banking and card/auto lending business models instead of copying Goldman/JPMorgan shares. Excludes unrelated custody fees, net interest, FX-only trading and asset management. Wide range; not a disclosed US taxable-securities segment or transaction notional. · Company-specific estimate of revenue sensitive to covered securities trading volume. Separates broker/dealer, custody, regional banking and card/auto lending business models instead of copying Goldman/JPMorgan shares. Excludes unrelated custody fees, net interest, FX-only trading and asset management. Wide range; not a disclosed US taxable-securities segment or transaction notional. |
| USB | trading_revenue_share | 0.025 | 0.01 | 0.05 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/36104/000003610426000011/0000036104-26-000011-index.htm · estimate; Company-specific estimate of revenue sensitive to covered securities trading volume. Separates broker/dealer, custody, regional banking and card/auto lending business models instead of copying Goldman/JPMorgan shares. Excludes unrelated custody fees, net interest, FX-only trading and asset management. Wide range; not a disclosed US taxable-securities segment or transaction notional. · Company-specific estimate of revenue sensitive to covered securities trading volume. Separates broker/dealer, custody, regional banking and card/auto lending business models instead of copying Goldman/JPMorgan shares. Excludes unrelated custody fees, net interest, FX-only trading and asset management. Wide range; not a disclosed US taxable-securities segment or transaction notional. |
| PNC | trading_revenue_share | 0.025 | 0.01 | 0.05 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/713676/000071367626000020/0000713676-26-000020-index.htm · estimate; Company-specific estimate of revenue sensitive to covered securities trading volume. Separates broker/dealer, custody, regional banking and card/auto lending business models instead of copying Goldman/JPMorgan shares. Excludes unrelated custody fees, net interest, FX-only trading and asset management. Wide range; not a disclosed US taxable-securities segment or transaction notional. · Company-specific estimate of revenue sensitive to covered securities trading volume. Separates broker/dealer, custody, regional banking and card/auto lending business models instead of copying Goldman/JPMorgan shares. Excludes unrelated custody fees, net interest, FX-only trading and asset management. Wide range; not a disclosed US taxable-securities segment or transaction notional. |
| TFC | trading_revenue_share | 0.025 | 0.01 | 0.05 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/92230/000009223026000030/0000092230-26-000030-index.htm · estimate; Company-specific estimate of revenue sensitive to covered securities trading volume. Separates broker/dealer, custody, regional banking and card/auto lending business models instead of copying Goldman/JPMorgan shares. Excludes unrelated custody fees, net interest, FX-only trading and asset management. Wide range; not a disclosed US taxable-securities segment or transaction notional. · Company-specific estimate of revenue sensitive to covered securities trading volume. Separates broker/dealer, custody, regional banking and card/auto lending business models instead of copying Goldman/JPMorgan shares. Excludes unrelated custody fees, net interest, FX-only trading and asset management. Wide range; not a disclosed US taxable-securities segment or transaction notional. |
| COF | trading_revenue_share | 0.002 | 0 | 0.005 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/927628/000092762826000024/0000927628-26-000024-index.htm · estimate; Company-specific estimate of revenue sensitive to covered securities trading volume. Separates broker/dealer, custody, regional banking and card/auto lending business models instead of copying Goldman/JPMorgan shares. Excludes unrelated custody fees, net interest, FX-only trading and asset management. Wide range; not a disclosed US taxable-securities segment or transaction notional. · Company-specific estimate of revenue sensitive to covered securities trading volume. Separates broker/dealer, custody, regional banking and card/auto lending business models instead of copying Goldman/JPMorgan shares. Excludes unrelated custody fees, net interest, FX-only trading and asset management. Wide range; not a disclosed US taxable-securities segment or transaction notional. |
| FITB | trading_revenue_share | 0.03 | 0.01 | 0.06 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/35527/000003552726000124/0000035527-26-000124-index.htm · estimate; Company-specific estimate of revenue sensitive to covered securities trading volume. Separates broker/dealer, custody, regional banking and card/auto lending business models instead of copying Goldman/JPMorgan shares. Excludes unrelated custody fees, net interest, FX-only trading and asset management. Wide range; not a disclosed US taxable-securities segment or transaction notional. · Company-specific estimate of revenue sensitive to covered securities trading volume. Separates broker/dealer, custody, regional banking and card/auto lending business models instead of copying Goldman/JPMorgan shares. Excludes unrelated custody fees, net interest, FX-only trading and asset management. Wide range; not a disclosed US taxable-securities segment or transaction notional. |
| HBAN | trading_revenue_share | 0.01 | 0.002 | 0.03 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/49196/000004919626000015/0000049196-26-000015-index.htm · estimate; Company-specific estimate of revenue sensitive to covered securities trading volume. Separates broker/dealer, custody, regional banking and card/auto lending business models instead of copying Goldman/JPMorgan shares. Excludes unrelated custody fees, net interest, FX-only trading and asset management. Wide range; not a disclosed US taxable-securities segment or transaction notional. · Company-specific estimate of revenue sensitive to covered securities trading volume. Separates broker/dealer, custody, regional banking and card/auto lending business models instead of copying Goldman/JPMorgan shares. Excludes unrelated custody fees, net interest, FX-only trading and asset management. Wide range; not a disclosed US taxable-securities segment or transaction notional. |
| KEY | trading_revenue_share | 0.025 | 0.01 | 0.05 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/91576/000162828026010546/0001628280-26-010546-index.htm · estimate; Company-specific estimate of revenue sensitive to covered securities trading volume. Separates broker/dealer, custody, regional banking and card/auto lending business models instead of copying Goldman/JPMorgan shares. Excludes unrelated custody fees, net interest, FX-only trading and asset management. Wide range; not a disclosed US taxable-securities segment or transaction notional. · Company-specific estimate of revenue sensitive to covered securities trading volume. Separates broker/dealer, custody, regional banking and card/auto lending business models instead of copying Goldman/JPMorgan shares. Excludes unrelated custody fees, net interest, FX-only trading and asset management. Wide range; not a disclosed US taxable-securities segment or transaction notional. |
| ALLY | trading_revenue_share | 0.002 | 0 | 0.01 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/40729/000004072926000005/0000040729-26-000005-index.htm · estimate; Company-specific estimate of revenue sensitive to covered securities trading volume. Separates broker/dealer, custody, regional banking and card/auto lending business models instead of copying Goldman/JPMorgan shares. Excludes unrelated custody fees, net interest, FX-only trading and asset management. Wide range; not a disclosed US taxable-securities segment or transaction notional. · Company-specific estimate of revenue sensitive to covered securities trading volume. Separates broker/dealer, custody, regional banking and card/auto lending business models instead of copying Goldman/JPMorgan shares. Excludes unrelated custody fees, net interest, FX-only trading and asset management. Wide range; not a disclosed US taxable-securities segment or transaction notional. |

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
| assumption.elasticity | -0.023835982 | -0.08127996 | 0.057443977 |
| assumption.cost_bps | -0.075259222 | -0.020525242 | 0.05473398 |
| exposure.trading_revenue_share | -0.033115523 | -0.058076903 | 0.02496138 |
| assumption.variable_comp_ratio | -0.052578361 | -0.040206982 | 0.012371379 |

Dominant configured driver: `elasticity` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.


## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 17 unchecked in-scope exposure values; 3 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| — | Existing values retained | — | — | No unsourced numeric recalibration performed. |

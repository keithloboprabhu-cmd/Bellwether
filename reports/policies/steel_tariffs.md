# Higher tariffs on imported steel

Policy `industrials/steel_tariffs` · evidence checkpoint 2026-11-01 · **FAIL-UNRESOLVED**

## A. Mechanics and scope

Configured mechanics below are a model specification, not a certification of current law. Current legal thresholds, exemptions, effective dates and phase-ins have not all been independently verified. Treat unresolved legal scope as a failure, not an implicit approval.

A higher Section 232-style tariff on imported steel lets US mills raise prices, which helps Nucor and raises costs for steel buyers. Caterpillar and Deere are hit hardest because they use the most steel; GE Aerospace, Honeywell and 3M barely notice.

Duration: `permanent`. Default inputs: `{"tariff_pct": 25.0}`.

| Channel | Template/role limits | Parameters |
|---|---|---|
| cost | unavailable / ['importer'] | {"exposed_cost_share": "exposure.ind_steel_share_of_cogs", "shock_pct": "derived.steel_price_rise", "pass_through": "assumption.pass_through", "elasticity": "assumption.elasticity"} |
| domestic_uplift | unavailable / ['domestic_producer'] | {"domestic_sales_share": "exposure.ind_domestic_steel_sales_share", "price_uplift": "derived.domestic_steel_price_rise", "flow_through": "assumption.flow_through"} |

Threshold expressions are shown literally so omissions are reviewable. Input bounds alone do not establish a legal or realistic range.

Policy references (a citation is not numeric verification):

- https://www.polsinelli.com/publications/usitc-releases-report-on-the-economic-impact-of-the-section-232-and-301-tariffs-on-u-s-industries
- https://reason.com/2023/03/16/u-s-trade-commission-admits-tariffs-raised-prices-for-american-consumers/
- https://www.usitc.gov/publications/332/pub5405.pdf
- https://www.sec.gov/Archives/edgar/data/73309/000119312526071575/nue-20251231.htm
- https://www.sec.gov/Archives/edgar/data/18230/000001823026000008/cat-20251231.htm

| Company | Configured status | Basis |
|---|---|---|
| CAT | included | Domestic steel producer gains tariff pricing while equipment users face costs. |
| DE | included | Domestic steel producer gains tariff pricing while equipment users face costs. |
| GE | included | Domestic steel producer gains tariff pricing while equipment users face costs. |
| HON | included | Domestic steel producer gains tariff pricing while equipment users face costs. |
| MMM | included | Domestic steel producer gains tariff pricing while equipment users face costs. |
| NUE | included | Domestic steel producer gains tariff pricing while equipment users face costs. |
| BA | included | Domestic steel producer gains tariff pricing while equipment users face costs. |
| ETN | included | Domestic steel producer gains tariff pricing while equipment users face costs. |
| EMR | included | Domestic steel producer gains tariff pricing while equipment users face costs. |
| ITW | included | Domestic steel producer gains tariff pricing while equipment users face costs. |
| PH | included | Domestic steel producer gains tariff pricing while equipment users face costs. |
| CMI | included | Domestic steel producer gains tariff pricing while equipment users face costs. |
| PCAR | included | Domestic steel producer gains tariff pricing while equipment users face costs. |
| DOV | included | Domestic steel producer gains tariff pricing while equipment users face costs. |
| ROK | included | Domestic steel producer gains tariff pricing while equipment users face costs. |
| STLD | included | Domestic steel producer gains tariff pricing while equipment users face costs. |
| CLF | included | Domestic steel producer gains tariff pricing while equipment users face costs. |
| CARR | included | Domestic steel producer gains tariff pricing while equipment users face costs. |
| OTIS | included | Domestic steel producer gains tariff pricing while equipment users face costs. |
| IR | included | Domestic steel producer gains tariff pricing while equipment users face costs. |
| GEV | unquantified | Activity scope and numeric sensitivity have not been fully verified for this newly admitted issuer. Missing exposure is not evidence of no impact. |

## B. Every in-scope exposure

Exact numeric checks are distinguished from filing links and estimates. UNVERIFIED values are retained, not silently replaced. Historical observed low/high values are not forecast confidence intervals.

| Company | Exposure | Base | Low | High | Exact-source status | Primary source / location / rationale |
|---|---|---:|---:|---:|---|---|
| CAT | ind_steel_share_of_cogs | 0.15 | 0.1 | 0.2 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/18230/000001823026000008/cat-20251231.htm · estimate; Caterpillar's 10-K calls it 'a significant user of steel' and says unformed materials include a variety of steel products cut and machined in its plants; heavy machinery frames, buckets, castings and forgings make steel the largest single material input, but most of the $44.8B cost of goods sold is components, labor and overhead. · Caterpillar's 10-K calls it 'a significant user of steel' and says unformed materials include a variety of steel products cut and machined in its plants; heavy machinery frames, buckets, castings and forgings make steel the largest single material input, but most of the $44.8B cost of goods sold is components, labor and overhead. |
| CAT | ind_domestic_steel_sales_share | 0 | 0 | 0 | UNVERIFIED | No source URL · estimate; Caterpillar buys steel; it does not sell it. · Caterpillar buys steel; it does not sell it. |
| DE | ind_steel_share_of_cogs | 0.12 | 0.08 | 0.16 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/315189/000110465925122321/de-20251102x10k.htm · estimate; Deere's 10-K lists a variety of steel products, metal castings and forgings first among purchased materials; tractors and combines are somewhat less steel-intensive per dollar of cost than Caterpillar's earthmoving and mining machines. · Deere's 10-K lists a variety of steel products, metal castings and forgings first among purchased materials; tractors and combines are somewhat less steel-intensive per dollar of cost than Caterpillar's earthmoving and mining machines. |
| DE | ind_domestic_steel_sales_share | 0 | 0 | 0 | UNVERIFIED | No source URL · estimate; Deere buys steel; it does not sell it. · Deere buys steel; it does not sell it. |
| GE | ind_steel_share_of_cogs | 0.03 | 0.01 | 0.05 | UNVERIFIED | No source URL · estimate; Jet engines are built mainly from nickel superalloys, titanium and composites; specialty steel (shafts, bearings, cases) is a small share of a cost base dominated by high-value parts and labor. · Jet engines are built mainly from nickel superalloys, titanium and composites; specialty steel (shafts, bearings, cases) is a small share of a cost base dominated by high-value parts and labor. |
| GE | ind_domestic_steel_sales_share | 0 | 0 | 0 | UNVERIFIED | No source URL · estimate; GE Aerospace buys steel; it does not sell it. · GE Aerospace buys steel; it does not sell it. |
| HON | ind_steel_share_of_cogs | 0.03 | 0.01 | 0.06 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/773840/000077384026000013/hon-20251231.htm · estimate; Honeywell's 10-K names steel among Aerospace Technologies' metals (with nickel and titanium) and copper, aluminum and others in other segments; its automation, building and aerospace electronics are not steel-intensive. · Honeywell's 10-K names steel among Aerospace Technologies' metals (with nickel and titanium) and copper, aluminum and others in other segments; its automation, building and aerospace electronics are not steel-intensive. |
| HON | ind_domestic_steel_sales_share | 0 | 0 | 0 | UNVERIFIED | No source URL · estimate; Honeywell buys steel; it does not sell it. · Honeywell buys steel; it does not sell it. |
| MMM | ind_steel_share_of_cogs | 0.02 | 0.01 | 0.04 | UNVERIFIED | No source URL · estimate; 3M's materials are mainly resins, films, adhesives, chemicals and minerals; steel enters through equipment, packaging and a few products (abrasives backings, fasteners). · 3M's materials are mainly resins, films, adhesives, chemicals and minerals; steel enters through equipment, packaging and a few products (abrasives backings, fasteners). |
| MMM | ind_domestic_steel_sales_share | 0 | 0 | 0 | UNVERIFIED | No source URL · estimate; 3M buys steel; it does not sell it. · 3M buys steel; it does not sell it. |
| NUE | ind_steel_share_of_cogs | 0 | 0 | 0.05 | UNVERIFIED | No source URL · estimate; Nucor makes its own steel from scrap and DRI; the cost channel is not applied to it (domestic-producer role). Higher scrap costs are handled by the flow-through assumption instead. · Nucor makes its own steel from scrap and DRI; the cost channel is not applied to it (domestic-producer role). Higher scrap costs are handled by the flow-through assumption instead. |
| NUE | ind_domestic_steel_sales_share | 0.88 | 0.8 | 0.93 | UNVERIFIED | https://www.sec.gov/Archives/edgar/data/73309/000119312526071575/nue-20251231.htm · Nucor 2025 10-K: steel mills $20,003M + steel products $10,327M = 93% of $32,494M external sales (raw materials $2,164M); 98% of 2025 pretax income was domestic; Nucor gives no revenue by country; the base assumes ~5% of steel sales are to Canada/Mexico or exports and are not priced off the protected US market. · Nucor gives no revenue by country; the base assumes ~5% of steel sales are to Canada/Mexico or exports and are not priced off the protected US market. |
| BA | ind_steel_share_of_cogs | 0.03 | 0.01 | 0.2 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| BA | ind_domestic_steel_sales_share | 0 | 0 | 0 | UNVERIFIED | No source URL · estimate; Explicit scope estimate: Aerospace and diversified manufacturing is outside this direct policy channel; indirect effects are not modeled. This is not a reported zero exposure. · Explicit scope estimate: Aerospace and diversified manufacturing is outside this direct policy channel; indirect effects are not modeled. This is not a reported zero exposure. |
| ETN | ind_steel_share_of_cogs | 0.03 | 0.01 | 0.2 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| ETN | ind_domestic_steel_sales_share | 0 | 0 | 0 | UNVERIFIED | No source URL · estimate; Explicit scope estimate: Aerospace and diversified manufacturing is outside this direct policy channel; indirect effects are not modeled. This is not a reported zero exposure. · Explicit scope estimate: Aerospace and diversified manufacturing is outside this direct policy channel; indirect effects are not modeled. This is not a reported zero exposure. |
| EMR | ind_steel_share_of_cogs | 0.03 | 0.01 | 0.2 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| EMR | ind_domestic_steel_sales_share | 0 | 0 | 0 | UNVERIFIED | No source URL · estimate; Explicit scope estimate: Aerospace and diversified manufacturing is outside this direct policy channel; indirect effects are not modeled. This is not a reported zero exposure. · Explicit scope estimate: Aerospace and diversified manufacturing is outside this direct policy channel; indirect effects are not modeled. This is not a reported zero exposure. |
| ITW | ind_steel_share_of_cogs | 0.03 | 0.01 | 0.2 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| ITW | ind_domestic_steel_sales_share | 0 | 0 | 0 | UNVERIFIED | No source URL · estimate; Explicit scope estimate: Aerospace and diversified manufacturing is outside this direct policy channel; indirect effects are not modeled. This is not a reported zero exposure. · Explicit scope estimate: Aerospace and diversified manufacturing is outside this direct policy channel; indirect effects are not modeled. This is not a reported zero exposure. |
| PH | ind_steel_share_of_cogs | 0.03 | 0.01 | 0.2 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| PH | ind_domestic_steel_sales_share | 0 | 0 | 0 | UNVERIFIED | No source URL · estimate; Explicit scope estimate: Aerospace and diversified manufacturing is outside this direct policy channel; indirect effects are not modeled. This is not a reported zero exposure. · Explicit scope estimate: Aerospace and diversified manufacturing is outside this direct policy channel; indirect effects are not modeled. This is not a reported zero exposure. |
| CMI | ind_steel_share_of_cogs | 0.03 | 0.01 | 0.2 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| CMI | ind_domestic_steel_sales_share | 0 | 0 | 0 | UNVERIFIED | No source URL · estimate; Explicit scope estimate: Aerospace and diversified manufacturing is outside this direct policy channel; indirect effects are not modeled. This is not a reported zero exposure. · Explicit scope estimate: Aerospace and diversified manufacturing is outside this direct policy channel; indirect effects are not modeled. This is not a reported zero exposure. |
| PCAR | ind_steel_share_of_cogs | 0.03 | 0.01 | 0.2 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| PCAR | ind_domestic_steel_sales_share | 0 | 0 | 0 | UNVERIFIED | No source URL · estimate; Explicit scope estimate: Aerospace and diversified manufacturing is outside this direct policy channel; indirect effects are not modeled. This is not a reported zero exposure. · Explicit scope estimate: Aerospace and diversified manufacturing is outside this direct policy channel; indirect effects are not modeled. This is not a reported zero exposure. |
| DOV | ind_steel_share_of_cogs | 0.03 | 0.01 | 0.2 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| DOV | ind_domestic_steel_sales_share | 0 | 0 | 0 | UNVERIFIED | No source URL · estimate; Explicit scope estimate: Aerospace and diversified manufacturing is outside this direct policy channel; indirect effects are not modeled. This is not a reported zero exposure. · Explicit scope estimate: Aerospace and diversified manufacturing is outside this direct policy channel; indirect effects are not modeled. This is not a reported zero exposure. |
| ROK | ind_steel_share_of_cogs | 0.03 | 0.01 | 0.2 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| ROK | ind_domestic_steel_sales_share | 0 | 0 | 0 | UNVERIFIED | No source URL · estimate; Explicit scope estimate: Aerospace and diversified manufacturing is outside this direct policy channel; indirect effects are not modeled. This is not a reported zero exposure. · Explicit scope estimate: Aerospace and diversified manufacturing is outside this direct policy channel; indirect effects are not modeled. This is not a reported zero exposure. |
| STLD | ind_steel_share_of_cogs | 0 | 0 | 0.05 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Steel production; median base and outer low/high from NUE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Steel production; median base and outer low/high from NUE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| STLD | ind_domestic_steel_sales_share | 0.88 | 0.8 | 0.93 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Steel production; median base and outer low/high from NUE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Steel production; median base and outer low/high from NUE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| CLF | ind_steel_share_of_cogs | 0 | 0 | 0.05 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Steel production; median base and outer low/high from NUE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Steel production; median base and outer low/high from NUE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| CLF | ind_domestic_steel_sales_share | 0.88 | 0.8 | 0.93 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Steel production; median base and outer low/high from NUE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Steel production; median base and outer low/high from NUE in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| CARR | ind_steel_share_of_cogs | 0.03 | 0.01 | 0.2 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| CARR | ind_domestic_steel_sales_share | 0 | 0 | 0 | UNVERIFIED | No source URL · estimate; Explicit scope estimate: Aerospace and diversified manufacturing is outside this direct policy channel; indirect effects are not modeled. This is not a reported zero exposure. · Explicit scope estimate: Aerospace and diversified manufacturing is outside this direct policy channel; indirect effects are not modeled. This is not a reported zero exposure. |
| OTIS | ind_steel_share_of_cogs | 0.03 | 0.01 | 0.2 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| OTIS | ind_domestic_steel_sales_share | 0 | 0 | 0 | UNVERIFIED | No source URL · estimate; Explicit scope estimate: Aerospace and diversified manufacturing is outside this direct policy channel; indirect effects are not modeled. This is not a reported zero exposure. · Explicit scope estimate: Aerospace and diversified manufacturing is outside this direct policy channel; indirect effects are not modeled. This is not a reported zero exposure. |
| IR | ind_steel_share_of_cogs | 0.03 | 0.01 | 0.2 | UNVERIFIED | No source URL · estimate; Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. · Explicit modeling prior, not an issuer disclosure. Aerospace and diversified manufacturing; median base and outer low/high from CAT/DE/GE/HON/MMM in committed exposure configuration. Dimensionless peer prior; review before relying on this company result. |
| IR | ind_domestic_steel_sales_share | 0 | 0 | 0 | UNVERIFIED | No source URL · estimate; Explicit scope estimate: Aerospace and diversified manufacturing is outside this direct policy channel; indirect effects are not modeled. This is not a reported zero exposure. · Explicit scope estimate: Aerospace and diversified manufacturing is outside this direct policy channel; indirect effects are not modeled. This is not a reported zero exposure. |

## C. Published sensitivity benchmark

| Company / input | Metric | Published | Modeled | Low / high | Relative error | Direction / size | Source |
|---|---|---:|---:|---|---:|---|---|
| — | No matched published company sensitivity obtained | — | — | — | — | FAIL-UNRESOLVED | The exact input, timing, business perimeter and financial metric must match before comparison. |

Verified sector-price calibration: USITC Publication 5405, corrected May 2023, table 5.2 (p.125), 25% tariff: buyer steel prices +2.39%, domestic producer prices +0.74%. The engine gives 2.39% and 0.74%. These are price metrics, not company EPS. The observed 2018 gross-margin replay remains a confounded magnitude miss; it is not used to fit the tariff coefficient. Source: https://www.usitc.gov/publications/332/pub5405.pdf

## D. Tolerances, totals and ranking

Direction must match; size must be within ±25% of the published value or contain it in the scenario range. No benchmark means no pass. Comparisons below are in-sample calibration checks, not independent prediction validation.

Totals: no like-for-like official score for this public-company sample and exact policy horizon was obtained. A national ten-year fiscal score cannot be compared directly with a one-year partial-company cost total. **UNVERIFIED.**

Spearman: unavailable; fewer than five matched published company observations. No ordering is inferred from unverified priors.

## E. One-at-a-time sensitivity

| Driver | Industry metric at low | At high | Absolute swing |
|---|---:|---:|---:|
| exposure.ind_steel_share_of_cogs | 0.0020909583 | -0.0074631754 | 0.0095541337 |
| assumption.pass_through | -0.00064496356 | 0.0018937342 | 0.0025386978 |
| assumption.flow_through | -0.00075963005 | 0.0015013076 | 0.0022609377 |
| assumption.producer_price_response | -0.00080545987 | 0.0010659243 | 0.0018713842 |
| assumption.price_response | 0.0015258031 | -0.00024402816 | 0.0017698313 |
| assumption.elasticity | 0.00063221084 | 2.2342695e-05 | 0.00060986814 |
| exposure.ind_domestic_steel_sales_share | 1.114415e-05 | 0.00059564792 | 0.00058450377 |

Dominant configured driver: `ind_steel_share_of_cogs` using `d_eps_pct`. This identifies the algebraic driver; economic plausibility is **not independently confirmed** when its numeric exposure or transmission coefficient is UNVERIFIED. Historical exposure ranges cannot substitute for forecast uncertainty.


## F. Verdict and parameter changes

**FAIL-UNRESOLVED**. 40 unchecked in-scope exposure values; 3 unchecked assumptions; 0 matched numerical benchmark comparisons. Internal accounting/scope errors: 0.

A recalibrated coefficient does not make the entire policy pass. Unchecked thresholds, realistic ranges, company coverage, duration or a missing matched benchmark remain open.

| Company | Parameter | Before | After | Evidence |
|---|---|---:|---:|---|
| ALL | price_response | 0.4 | 0.0956 | https://www.usitc.gov/publications/332/pub5405.pdf · USITC Publication 5405, corrected May 2023, table 5.2, printed p.125 (PDF p.125), 2018–2021 average-steel-price effects |
| ALL | producer_price_response | unavailable | 0.0296 | https://www.usitc.gov/publications/332/pub5405.pdf · USITC Publication 5405 table 5.2, printed p.125, domestic steel producer prices: 0.52–0.87%, average 0.74%, under 25% tariffs |

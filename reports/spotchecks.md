# Ten stratified random arithmetic checks

Seed: 20261031. One affected reference-company scenario per industry, using default user inputs. Draws are independent of whether the arithmetic passes. This audit-only calculator separately implements channel arithmetic, aggregation and duration valuation; it does not call the engine calculation functions. Configured expressions are reused to capture the exact parameters, and are printed for manual review. These checks validate arithmetic, not the truth of an exposure or a forecast. USD millions except EPS, price and share counts (millions).

## 1. Technology, Media & Telecom / semiconductor_tariffs / IBM

Inputs: `{"tariff_pct": 25.0}`. Role: `importer`. Annual source: https://www.sec.gov/Archives/edgar/data/51143/000005114326000010/0000051143-26-000010-index.htm.

Baseline R=67535; C=28239; PTI=10328; tax=0.1353279632; parent share=1; diluted shares=948.675228; price=253.56; valuation P/E=22.700089525514773 (reported_eps).

**cost**: configured expressions `{"exposed_cost_share": "exposure.us_import_share_of_cogs", "shock_pct": "input.tariff_pct / 100", "pass_through": "assumption.pass_through", "elasticity": "assumption.elasticity"}`.

Evaluated parameters: `{"dcost_musd": 0.0, "elasticity": 0.8, "exposed_cost_share": 0.1, "pass_through": 0.5, "shock_pct": 0.25, "variable_cost_share": 1.0}`.

- Initial cost shock = 28239 × 0.1 × 0.25 + 0 = 705.975
- Price fraction = pass-through × cost / revenue = 0.005226734286; volume fraction = −elasticity × price fraction = -0.004181387429
- ΔR = R[(1+price)(1+volume)−1] = 69.12152251; ΔC = exposed shock × (1+volume) + variable costs × volume = 584.9448454; ΔOpex = 0

Combined forward tax rate = clip(0.1353279632 + 0,0,1) = 0.1353279632.

ΔNI = sum[(ΔEBIT−Δinterest) × (1−tax new) + direct after-tax items + PTI × tax-rate change] × parent share = **-446.0180033M**.

ΔEPS = -446.0180033 / 948.675228 = **$-0.4701482553** (engine $-0.4701482553).

Valuation: each channel uses its own duration (permanent: supported P/E; one-time: 1; fixed years: annual discount factors at 9%), plus direct value per economic share and direct value percentage × price. Raw Δprice=-10.672407484781157; floor-adjusted Δprice=-10.672407484781157; engine Δprice=-10.672407484781157.

Cent comparison: EPS -0.47 = -0.47; price -10.67 = -10.67. **PASS arithmetic**.

## 2. Financial Services / fed_rate_change / MS

Inputs: `{"d_rate_bps": -100.0}`. Role: `importer`. Annual source: https://www.sec.gov/Archives/edgar/data/895421/000089542126000086/0000895421-26-000086-index.htm.

Baseline R=70645; C=0; PTI=21954; tax=0.2245148948; parent share=1; diluted shares=1592; price=179.49; valuation P/E=17.579823702252693 (reported_eps).

**bank_nii**: configured expressions `{"d_rate_bps": "input.d_rate_bps", "nii_sensitivity_per_100bp": "derived.sensitivity"}`.

Evaluated parameters: `{"d_rate_bps": -100.0, "nii_sensitivity_per_100bp": 0.024288273939876568}`.

- ΔNII = 10046 × 0.02428827394 × -100/100 = -244; ΔEBIT = ΔNII

Combined forward tax rate = clip(0.2245148948 + 0,0,1) = 0.2245148948.

ΔNI = sum[(ΔEBIT−Δinterest) × (1−tax new) + direct after-tax items + PTI × tax-rate change] × parent share = **-189.2183657M**.

ΔEPS = -189.2183657 / 1592 = **$-0.1188557573** (engine $-0.1188557573).

Valuation: each channel uses its own duration (permanent: supported P/E; one-time: 1; fixed years: annual discount factors at 9%), plus direct value per economic share and direct value percentage × price. Raw Δprice=-2.089463259906847; floor-adjusted Δprice=-2.089463259906847; engine Δprice=-2.089463259906847.

Cent comparison: EPS -0.12 = -0.12; price -2.09 = -2.09. **PASS arithmetic**.

## 3. Consumer & Retail / sweetened_beverage_tax / PEP

Inputs: `{"tax_cents_per_oz": 1.5, "coverage_pct": 100.0}`. Role: `importer`. Annual source: https://www.sec.gov/Archives/edgar/data/77476/000007747626000007/0000077476-26-000007-index.htm.

Baseline R=93925; C=43066; PTI=10244; tax=0.1902577118; parent share=0.9933694997; diluted shares=1373; price=135.77; valuation P/E=22.628333333333334 (reported_eps).

**demand_price**: configured expressions `{"dp_consumer": "input.tax_cents_per_oz * assumption.pass_through / assumption.price_per_oz", "elasticity": "assumption.elasticity", "exposed_revenue_share": "exposure.us_sweetened_beverage_revenue_share * input.coverage_pct / 100 * (1 - assumption.recapture)"}`.

Evaluated parameters: `{"dp_consumer": 0.16666666666666663, "elasticity": 1.21, "exposed_revenue_share": 0.06999999999999999}`.

- ΔR = R × share × (−elasticity × price) = -1325.907917
- ΔEBIT = ΔR × contribution margin 0.5414852276 = -717.95955

Combined forward tax rate = clip(0.1902577118 + 0,0,1) = 0.1902577118.

ΔNI = sum[(ΔEBIT−Δinterest) × (1−tax new) + direct after-tax items + PTI × tax-rate change] × parent share = **-577.5074865M**.

ΔEPS = -577.5074865 / 1373 = **$-0.4206172517** (engine $-0.4206172517).

Valuation: each channel uses its own duration (permanent: supported P/E; one-time: 1; fixed years: annual discount factors at 9%), plus direct value per economic share and direct value percentage × price. Raw Δprice=-9.517867376305114; floor-adjusted Δprice=-9.517867376305114; engine Δprice=-9.517867376305114.

Cent comparison: EPS -0.42 = -0.42; price -9.52 = -9.52. **PASS arithmetic**.

## 4. Healthcare & Life Sciences / pharma_tariffs / GILD

Inputs: `{"tariff_pct": 15.0}`. Role: `importer`. Annual source: https://www.sec.gov/Archives/edgar/data/882095/000088209526000006/0000882095-26-000006-index.htm.

Baseline R=29443; C=6234; PTI=9796; tax=0.1312780727; parent share=1; diluted shares=1255; price=156.04; valuation P/E=23.01474926253687 (reported_eps).

**cost**: configured expressions `{"exposed_cost_share": "exposure.pharma_import_share_of_cogs", "shock_pct": "input.tariff_pct / 100 * (1 - assumption.exempt_share)", "pass_through": "assumption.pass_through", "elasticity": "assumption.elasticity"}`.

Evaluated parameters: `{"dcost_musd": 0.0, "elasticity": 0.2, "exposed_cost_share": 0.3, "pass_through": 0.2, "shock_pct": 0.09, "variable_cost_share": 1.0}`.

- Initial cost shock = 6234 × 0.3 × 0.09 + 0 = 168.318
- Price fraction = pass-through × cost / revenue = 0.001143348164; volume fraction = −elasticity × price fraction = -0.0002286696328
- ΔR = R[(1+price)(1+volume)−1] = 26.92318216; ΔC = exposed shock × (1+volume) + variable costs × volume = 166.8539843; ΔOpex = 0

Combined forward tax rate = clip(0.1312780727 + 0,0,1) = 0.1312780727.

ΔNI = sum[(ΔEBIT−Δinterest) × (1−tax new) + direct after-tax items + PTI × tax-rate change] × parent share = **-121.5609561M**.

ΔEPS = -121.5609561 / 1255 = **$-0.09686131962** (engine $-0.09686131962).

Valuation: each channel uses its own duration (permanent: supported P/E; one-time: 1; fixed years: annual discount factors at 9%), plus direct value per economic share and direct value percentage × price. Raw Δprice=-2.229238984293895; floor-adjusted Δprice=-2.229238984293895; engine Δprice=-2.229238984293895.

Cent comparison: EPS -0.10 = -0.10; price -2.23 = -2.23. **PASS arithmetic**.

## 5. Industrials & Manufacturing / steel_tariffs / ITW

Inputs: `{"tariff_pct": 25.0}`. Role: `importer`. Annual source: https://www.sec.gov/Archives/edgar/data/49826/000004982626000008/0000049826-26-000008-index.htm.

Baseline R=16044; C=7556; PTI=3966; tax=0.2269288956; parent share=1; diluted shares=292.3; price=275.75; valuation P/E=26.286939942802668 (reported_eps).

**cost**: configured expressions `{"exposed_cost_share": "exposure.ind_steel_share_of_cogs", "shock_pct": "derived.steel_price_rise", "pass_through": "assumption.pass_through", "elasticity": "assumption.elasticity"}`.

Evaluated parameters: `{"dcost_musd": 0.0, "elasticity": 0.6, "exposed_cost_share": 0.03, "pass_through": 0.5, "shock_pct": 0.0239, "variable_cost_share": 1.0}`.

- Initial cost shock = 7556 × 0.03 × 0.0239 + 0 = 5.417652
- Price fraction = pass-through × cost / revenue = 0.0001688373224; volume fraction = −elasticity × price fraction = -0.0001013023934
- ΔR = R[(1+price)(1+volume)−1] = 1.083255989; ΔC = exposed shock × (1+volume) + variable costs × volume = 4.651662294; ΔOpex = 0

Combined forward tax rate = clip(0.2269288956 + 0,0,1) = 0.2269288956.

ΔNI = sum[(ΔEBIT−Δinterest) × (1−tax new) + direct after-tax items + PTI × tax-rate change] × parent share = **-2.758631803M**.

ΔEPS = -2.758631803 / 292.3 = **$-0.009437672949** (engine $-0.009437672949).

Valuation: each channel uses its own duration (permanent: supported P/E; one-time: 1; fixed years: annual discount factors at 9%), plus direct value per economic share and direct value percentage × price. Raw Δprice=-0.24808754200515193; floor-adjusted Δprice=-0.24808754200515193; engine Δprice=-0.24808754200515193.

Cent comparison: EPS -0.01 = -0.01; price -0.25 = -0.25. **PASS arithmetic**.

## 6. Energy & Resources / crude_export_restrictions / DVN

Inputs: `{"restricted_pct": 50.0}`. Role: `importer`. Annual source: https://www.sec.gov/Archives/edgar/data/1090012/000119312526056485/0001193125-26-056485-index.htm.

Baseline R=17188; C=12733; PTI=3466; tax=0.2264858627; parent share=0.9854531891; diluted shares=633; price=51.39; valuation P/E=12.323741007194245 (reported_eps).

**price**: configured expressions `{"d_price": "-derived.discount_pct", "exposed_revenue_share": "exposure.us_crude_sales_share"}`.

Evaluated parameters: `{"d_price": -0.046153846153846156, "exposed_revenue_share": 0.1, "offset_share": 0.0}`.

- ΔR = 17188 × 0.1 × -0.04615384615 = -79.32923077; ΔEBIT = ΔR × (1−0) = -79.32923077

**cost**: configured expressions `{"exposed_cost_share": "exposure.us_refinery_domestic_crude_cost_share", "shock_pct": "-derived.discount_pct", "pass_through": "assumption.refiner_pass_through"}`.

Evaluated parameters: `{"dcost_musd": 0.0, "elasticity": 0.0, "exposed_cost_share": 0.0, "pass_through": 0.2, "shock_pct": -0.046153846153846156, "variable_cost_share": 1.0}`.

- Initial cost shock = 12733 × 0 × -0.04615384615 + 0 = 0
- Price fraction = pass-through × cost / revenue = 0; volume fraction = −elasticity × price fraction = -0
- ΔR = R[(1+price)(1+volume)−1] = 0; ΔC = exposed shock × (1+volume) + variable costs × volume = -0; ΔOpex = 0

Combined forward tax rate = clip(0.2264858627 + 0,0,1) = 0.2264858627.

ΔNI = sum[(ΔEBIT−Δinterest) × (1−tax new) + direct after-tax items + PTI × tax-rate change] × parent share = **-60.469656M**.

ΔEPS = -60.469656 / 633 = **$-0.09552868246** (engine $-0.09552868246).

Valuation: each channel uses its own duration (permanent: supported P/E; one-time: 1; fixed years: annual discount factors at 9%), plus direct value per economic share and direct value percentage × price. Raw Δprice=-1.177270741429702; floor-adjusted Δprice=-1.177270741429702; engine Δprice=-1.177270741429702.

Cent comparison: EPS -0.10 = -0.10; price -1.18 = -1.18. **PASS arithmetic**.

## 7. Transportation, Logistics & Infrastructure / airline_bag_fee_cap / AAL

Inputs: `{"fee_cut_pct": 50.0}`. Role: `neutral`. Annual source: https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm.

Baseline R=54633; C=53166; PTI=190; tax=0.266897747; parent share=1; diluted shares=661.052; price=12.11; valuation P/E=None (unavailable_normalization_pending).

**price**: configured expressions `{"d_price": "-input.fee_cut_pct / 100", "exposed_revenue_share": "exposure.tl_checked_bag_fee_revenue_share", "offset_share": "assumption.fare_recapture"}`.

Evaluated parameters: `{"d_price": -0.5, "exposed_revenue_share": 0.0167, "offset_share": 0.5}`.

- ΔR = 54633 × 0.0167 × -0.5 = -456.18555; ΔEBIT = ΔR × (1−0.5) = -228.092775

Combined forward tax rate = clip(0.266897747 + 0,0,1) = 0.266897747.

ΔNI = sum[(ΔEBIT−Δinterest) × (1−tax new) + direct after-tax items + PTI × tax-rate change] × parent share = **-167.2153273M**.

ΔEPS = -167.2153273 / 661.052 = **$-0.2529533641** (engine $-0.2529533641).

Valuation: each channel uses its own duration (permanent: supported P/E; one-time: 1; fixed years: annual discount factors at 9%), plus direct value per economic share and direct value percentage × price. Raw Δprice=None; floor-adjusted Δprice=None; engine Δprice=None.

Cent comparison: EPS -0.25 = -0.25; price both unavailable. **PASS arithmetic**.

## 8. Public Sector (government contractors) / continuing_resolution / TTEK

Inputs: `{"months_delayed": 3.0}`. Role: `neutral`. Annual source: https://www.sec.gov/Archives/edgar/data/831641/000083164125000032/0000831641-25-000032-index.htm.

Baseline R=5442.59; C=825.23; PTI=377.617; tax=0.3433849641; parent share=0.9990925553; diluted shares=267.123; price=36.98; valuation P/E=39.76344086021505 (reported_eps).

**gov_cr**: configured expressions `{"gov_revenue_share": "exposure.govcon_us_gov_share", "months_delayed": "input.months_delayed", "new_award_share": "assumption.new_award_share"}`.

Evaluated parameters: `{"fixed_cost_absorption": 1.0, "gov_revenue_share": 0.956, "months_delayed": 3.0, "new_award_share": 0.1}`.

- Government channel gov_cr, evaluated parameters below: ΔR=-130.077901; ΔEBIT=ΔR × margin 0.8483754977 × absorption 1 = -110.354904

Combined forward tax rate = clip(0.3433849641 + 0,0,1) = 0.3433849641.

ΔNI = sum[(ΔEBIT−Δinterest) × (1−tax new) + direct after-tax items + PTI × tax-rate change] × parent share = **-72.39493518M**.

ΔEPS = -72.39493518 / 267.123 = **$-0.2710172287** (engine $-0.2710172287).

Valuation: each channel uses its own duration (permanent: supported P/E; one-time: 1; fixed years: annual discount factors at 9%), plus direct value per economic share and direct value percentage × price. Raw Δprice=-0.27101722869864514; floor-adjusted Δprice=-0.27101722869864514; engine Δprice=-0.27101722869864514.

Cent comparison: EPS -0.27 = -0.27; price -0.27 = -0.27. **PASS arithmetic**.

## 9. Real Estate & Hospitality / like_kind_exchange_limits / EXR

Inputs: `{"taxed_share_pct": 75.0}`. Role: `neutral`. Annual source: https://www.sec.gov/Archives/edgar/data/1289490/000128949026000011/0001289490-26-000011-index.htm.

Baseline R=3377.542; C=918.148; PTI=940.761; tax=0.04417593842; parent share=1; diluted shares=211.850521; price=143.41; valuation P/E=31.24400871459695 (reported_eps).

**reit_nav**: configured expressions `{"d_10y_bps": "assumption.cap_rate_rise_bps * input.taxed_share_pct / 100", "cap_rate": "exposure.re_implied_cap_rate", "cap_rate_beta": "exposure.re_property_value_share"}`.

Evaluated parameters: `{"cap_rate": 0.055, "cap_rate_beta": 1.0, "d_10y_bps": 7.5}`.

- Direct equity fraction = −1 × 7.5/10,000 / 0.055 = -0.01363636364

Combined forward tax rate = clip(0.04417593842 + 0,0,1) = 0.04417593842.

ΔNI = sum[(ΔEBIT−Δinterest) × (1−tax new) + direct after-tax items + PTI × tax-rate change] × parent share = **0M**.

ΔEPS = 0 / 211.850521 = **$0** (engine $0).

Valuation: each channel uses its own duration (permanent: supported P/E; one-time: 1; fixed years: annual discount factors at 9%), plus direct value per economic share and direct value percentage × price. Raw Δprice=-1.9555909090909092; floor-adjusted Δprice=-1.9555909090909092; engine Δprice=-1.9555909090909092.

Cent comparison: EPS 0.00 = 0.00; price -1.96 = -1.96. **PASS arithmetic**.

## 10. Education / ninety_ten_rule_change / PRDO

Inputs: `{"cap_pct": 85.0}`. Role: `neutral`. Annual source: https://www.sec.gov/Archives/edgar/data/1046568/000119312526059331/0001193125-26-059331-index.htm.

Baseline R=846.096; C=239.173; PTI=216.836; tax=0.26251176; parent share=1; diluted shares=66.156; price=33.9; valuation P/E=14.008264462809917 (reported_eps).

**demand_volume**: configured expressions `{"d_volume": "-(1 - assumption.mitigation_share) * max(0, 1 - (1 - exposure.ninety_ten_hi_ratio) / (1 - input.cap_pct / 100))", "exposed_revenue_share": "exposure.ninety_ten_hi_revenue_share"}`.

Evaluated parameters: `{"d_volume": -0.03333333333333338, "exposed_revenue_share": 0.3}`.

- ΔR = 846.096 × 0.3 × -0.03333333333 = -8.46096
- ΔEBIT = ΔR × contribution margin 0.7173216751 = -6.06923

**demand_volume**: configured expressions `{"d_volume": "-(1 - assumption.mitigation_share) * max(0, 1 - (1 - exposure.ninety_ten_lo_ratio) / (1 - input.cap_pct / 100))", "exposed_revenue_share": "exposure.ninety_ten_lo_revenue_share"}`.

Evaluated parameters: `{"d_volume": -0.0, "exposed_revenue_share": 0.38}`.

- ΔR = 846.096 × 0.38 × -0 = -0
- ΔEBIT = ΔR × contribution margin 0.7173216751 = -0

Combined forward tax rate = clip(0.26251176 + 0,0,1) = 0.26251176.

ΔNI = sum[(ΔEBIT−Δinterest) × (1−tax new) + direct after-tax items + PTI × tax-rate change] × parent share = **-4.475985751M**.

ΔEPS = -4.475985751 / 66.156 = **$-0.0676580469** (engine $-0.0676580469).

Valuation: each channel uses its own duration (permanent: supported P/E; one-time: 1; fixed years: annual discount factors at 9%), plus direct value per economic share and direct value percentage × price. Raw Δprice=-0.9477718139905812; floor-adjusted Δprice=-0.9477718139905812; engine Δprice=-0.9477718139905812.

Cent comparison: EPS -0.07 = -0.07; price -0.95 = -0.95. **PASS arithmetic**.


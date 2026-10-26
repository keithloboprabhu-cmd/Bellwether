# Bellwether policy audit

Checked 2026-10-26T03:08:11.372117+00:00; source/data fingerprint `cc466ec7d2a0d869`.

66 industry policies and 10 macro shocks. 249 industry input cases; 380 coefficient/exposure endpoint cases; 42 macro input cases. 0 failures.

1338 explicit industry-policy/company coverage decisions across 203 unique companies. Every decision is independently recorded in config/policy_company_coverage.yaml, including business rationale and default direction for covered firms. Missing/extra firms, missing expected impacts, wrong default directions and out-of-scope effects are failures. Scope checks also run at uncertainty endpoints, not only defaults. Macro shocks cover all 203 companies and their uncertain-driver endpoints.

Checks: defaults, every valid input endpoint and endpoint combination, legal all-zero settings, every uncertain driver endpoint, finite results, nonnegative revenue/cost levels, exact earnings and valuation attribution, EPS/share identity, tax bounds, per-company oriented scenario ranges, independent sign/scope expectations, exposure provenance and explicit no-coverage exceptions.

This is an internal model audit, not independent assurance, causal policy attribution or out-of-sample forecast validation. Exposures and transmission coefficients marked estimate remain uncertain. A filing link provides business context and does not turn an estimated ratio into reported data. Current business scope can differ from the fiscal-year financial baseline after a divestiture.

| Policy | Affected / sample | Input cases | Driver endpoints | Result |
|---|---:|---:|---:|---|
| consumer_retail/consumer_tax_rebate | 20/20 | 9 | 6 | PASS |
| consumer_retail/import_tariffs | 20/20 | 3 | 6 | PASS |
| consumer_retail/minimum_wage_increase | 18/20 | 3 | 12 | PASS |
| consumer_retail/sales_tax_change | 20/20 | 4 | 6 | PASS |
| consumer_retail/snap_benefit_change | 7/20 | 4 | 4 | PASS |
| consumer_retail/sweetened_beverage_tax | 13/20 | 6 | 10 | PASS |
| education/earnings_accountability_test | 8/20 | 3 | 6 | PASS |
| education/ninety_ten_rule_change | 6/20 | 3 | 10 | PASS |
| education/online_compliance_costs | 16/20 | 3 | 6 | PASS |
| education/pell_grant_change | 7/20 | 4 | 4 | PASS |
| education/school_choice_esa | 2/20 | 3 | 4 | PASS |
| education/student_loan_borrowing_caps | 6/20 | 3 | 6 | PASS |
| education/student_loan_forgiveness | 18/20 | 3 | 6 | PASS |
| energy_resources/carbon_price | 20/20 | 3 | 6 | PASS |
| energy_resources/clean_energy_credits_change | 6/20 | 10 | 8 | PASS |
| energy_resources/critical_minerals_credit | 1/20 | 3 | 4 | PASS |
| energy_resources/crude_export_restrictions | 9/20 | 3 | 8 | PASS |
| energy_resources/federal_leasing_limits | 6/20 | 3 | 4 | PASS |
| energy_resources/methane_emissions_fee | 10/20 | 3 | 6 | PASS |
| energy_resources/spr_release | 7/20 | 3 | 6 | PASS |
| financial_services/bank_capital_requirement | 18/23 | 3 | 4 | PASS |
| financial_services/credit_card_interchange_cap | 12/23 | 3 | 6 | PASS |
| financial_services/credit_card_late_fee_cap | 12/23 | 3 | 6 | PASS |
| financial_services/fdic_assessment_increase | 18/23 | 3 | 2 | PASS |
| financial_services/fed_rate_change | 18/23 | 4 | 4 | PASS |
| financial_services/financial_transaction_tax | 17/23 | 3 | 8 | PASS |
| healthcare/aca_subsidy_change | 5/20 | 4 | 4 | PASS |
| healthcare/medicaid_work_requirements | 9/20 | 4 | 4 | PASS |
| healthcare/medicare_advantage_rate_change | 6/20 | 4 | 4 | PASS |
| healthcare/medicare_drug_price_negotiation | 7/20 | 3 | 4 | PASS |
| healthcare/pbm_rebate_pass_through | 5/20 | 3 | 4 | PASS |
| healthcare/pharma_tariffs | 7/20 | 3 | 8 | PASS |
| healthcare/site_neutral_payments | 10/20 | 3 | 8 | PASS |
| industrials/bonus_depreciation_rollback | 20/20 | 3 | 6 | PASS |
| industrials/corporate_tax_rate_change | 20/20 | 4 | 4 | PASS |
| industrials/defense_procurement_increase | 16/20 | 4 | 4 | PASS |
| industrials/infrastructure_spending | 19/20 | 3 | 4 | PASS |
| industrials/rd_credit_expansion | 20/20 | 3 | 4 | PASS |
| industrials/steel_tariffs | 20/20 | 4 | 12 | PASS |
| public_sector/consulting_contract_cancellations | 9/20 | 3 | 4 | PASS |
| public_sector/continuing_resolution | 20/20 | 3 | 4 | PASS |
| public_sector/defense_budget_increase | 20/20 | 4 | 4 | PASS |
| public_sector/federal_civilian_budget_cut | 20/20 | 4 | 4 | PASS |
| public_sector/fixed_price_shift | 20/20 | 3 | 4 | PASS |
| public_sector/government_shutdown | 20/20 | 3 | 6 | PASS |
| public_sector/it_modernization_funding | 13/20 | 3 | 6 | PASS |
| real_estate_hospitality/interest_rate_change | 20/20 | 4 | 12 | PASS |
| real_estate_hospitality/lihtc_expansion | 0/20 | 3 | 2 | PASS |
| real_estate_hospitality/like_kind_exchange_limits | 17/20 | 3 | 4 | PASS |
| real_estate_hospitality/property_tax_change | 19/20 | 4 | 6 | PASS |
| real_estate_hospitality/return_to_office_mandate | 7/20 | 4 | 4 | PASS |
| real_estate_hospitality/short_term_rental_regulation | 6/20 | 3 | 8 | PASS |
| real_estate_hospitality/visa_fee_tourism_tax | 7/20 | 3 | 8 | PASS |
| tmt/app_store_commission_cap | 2/20 | 3 | 6 | PASS |
| tmt/broadband_affordability_subsidy | 3/20 | 9 | 4 | PASS |
| tmt/chip_export_controls | 17/20 | 9 | 6 | PASS |
| tmt/chips_manufacturing_credit | 2/20 | 3 | 4 | PASS |
| tmt/data_privacy_mandate | 20/20 | 9 | 6 | PASS |
| tmt/digital_services_tax | 6/20 | 3 | 6 | PASS |
| tmt/semiconductor_tariffs | 20/20 | 3 | 6 | PASS |
| transportation_logistics/airline_bag_fee_cap | 4/20 | 3 | 4 | PASS |
| transportation_logistics/airline_ticket_tax_change | 4/20 | 4 | 4 | PASS |
| transportation_logistics/auto_import_tariffs | 17/20 | 3 | 6 | PASS |
| transportation_logistics/carbon_tax_transport_fuel | 17/20 | 3 | 8 | PASS |
| transportation_logistics/ev_tax_credit | 4/20 | 3 | 10 | PASS |
| transportation_logistics/vehicle_emissions_credit_rollback | 4/20 | 4 | 6 | PASS |

## Macro shocks

- china_trade_war: 3 input cases + 18 driver endpoints × 203 firms; 0 failures.
- corporate_tax_change: 4 input cases + 4 driver endpoints × 203 firms; 0 failures.
- fed_rate_change: 4 input cases + 26 driver endpoints × 203 firms; 0 failures.
- government_shutdown: 3 input cases + 8 driver endpoints × 203 firms; 0 failures.
- household_stimulus: 9 input cases + 20 driver endpoints × 203 firms; 0 failures.
- inflation_shock: 4 input cases + 24 driver endpoints × 203 firms; 0 failures.
- oil_supply_shock: 4 input cases + 22 driver endpoints × 203 firms; 0 failures.
- recession_gdp_shock: 4 input cases + 24 driver endpoints × 203 firms; 0 failures.
- strong_dollar: 4 input cases + 8 driver endpoints × 203 firms; 0 failures.
- universal_tariff: 3 input cases + 20 driver endpoints × 203 firms; 0 failures.

## Company scope and remaining limitations

### consumer_retail/consumer_tax_rebate

Consumer transfers raise captured retailer spending.

Affected: WMT, TGT, COST, AMZN, NKE, HD, LOW, KR, DG, DLTR, TJX, ROST, SBUX, MCD, KO, PEP, PG, CL, ULTA, BBY.
Neutral in direct channels: None.
14 estimated company exposure inputs; 0 narrow-business scope checks.
- Reference: https://www.nber.org/papers/w16684
- Reference: https://fred.stlouisfed.org/series/PCE

### consumer_retail/import_tariffs

Import duties raise importer input costs after partial pass-through.

Affected: WMT, TGT, COST, AMZN, NKE, HD, LOW, KR, DG, DLTR, TJX, ROST, SBUX, MCD, KO, PEP, PG, CL, ULTA, BBY.
Neutral in direct channels: None.
17 estimated company exposure inputs; 0 narrow-business scope checks.
- KR: >100% earnings change; small/loss baseline or linear approximation needs caution
- KR: implied loss exceeds equity value; constant-multiple approximation outside useful range
- BBY: >100% earnings change; small/loss baseline or linear approximation needs caution
- BBY: implied loss exceeds equity value; constant-multiple approximation outside useful range
- Reference: https://www.aeaweb.org/doi/10.1257/jep.33.4.187
- Reference: https://www.aeaweb.org/articles?id=10.1257/aeri.20190536

### consumer_retail/minimum_wage_increase

Higher wage floor raises exposed hourly payroll.

Affected: WMT, TGT, NKE, HD, LOW, KR, DG, DLTR, TJX, ROST, SBUX, MCD, KO, PEP, PG, CL, ULTA, BBY.
Neutral in direct channels: COST, AMZN.
34 estimated company exposure inputs; 0 narrow-business scope checks.
- Reference: https://www.npr.org/2019/07/08/739607964/-15-minimum-wage-would-boost-17-million-workers-cut-1-3-million-jobs-cbo-says
- Reference: https://fred.stlouisfed.org/series/CES4200000007

### consumer_retail/sales_tax_change

Higher checkout tax reduces exposed consumer demand.

Affected: WMT, TGT, COST, AMZN, NKE, HD, LOW, KR, DG, DLTR, TJX, ROST, SBUX, MCD, KO, PEP, PG, CL, ULTA, BBY.
Neutral in direct channels: None.
14 estimated company exposure inputs; 0 narrow-business scope checks.
- Reference: https://comptroller.texas.gov/taxes/sales/faq/food.php

### consumer_retail/snap_benefit_change

Default SNAP reduction lowers grocery spending.

Affected: WMT, TGT, COST, AMZN, KR, DG, DLTR.
Neutral in direct channels: NKE, HD, LOW, TJX, ROST, SBUX, MCD, KO, PEP, PG, CL, ULTA, BBY.
16 estimated company exposure inputs; 20 narrow-business scope checks.
- Reference: https://www.nber.org/papers/w23112
- Reference: https://supermarketnews.com/foodservice-retail/walmart-dominates-the-retail-field-in-snap-grocery-market-share
- Reference: https://www.everycrsreport.com/files/2025-07-23_R48552_542fa893b97030757b3aedac1b44930cac47cc88.html

### consumer_retail/sweetened_beverage_tax

Covered beverage demand declines under a consumer tax.

Affected: WMT, TGT, COST, AMZN, HD, LOW, KR, DG, DLTR, SBUX, MCD, KO, PEP.
Neutral in direct channels: NKE, TJX, ROST, PG, CL, ULTA, BBY.
20 estimated company exposure inputs; 20 narrow-business scope checks.
- Reference: https://doi.org/10.1001/jama.2019.4249
- Reference: https://doi.org/10.1111/obr.12002

### education/earnings_accountability_test

Loss of aid eligibility reduces enrollment at exposed programs.

Affected: LOPE, CVSA, STRA, COUR, UTI, PRDO, APEI, LINC.
Neutral in direct channels: LRN, DUOL, LAUR, NRDY, SKIL, CHGG, SCHL, KLC, BFAM, WLY, FC, SLM.
20 estimated company exposure inputs; 20 narrow-business scope checks.
- Reference: https://edtrust.org/rti/federal-rulemaking-recap-for-postsecondary-program-accountability-what-changed-and-what-it-means-for-higher-education/
- Reference: https://ticas.org/accountability/earnings-metric-final-rule-blog/
- Reference: https://www.nasfaa.org/uploads/documents/Ppt3_ResultsofEarningsTestandGEChanges_v2.pdf

### education/ninety_ten_rule_change

Tighter federal revenue limit restricts exposed proprietary programs.

Affected: CVSA, STRA, UTI, PRDO, APEI, LINC.
Neutral in direct channels: LRN, LOPE, DUOL, COUR, LAUR, NRDY, SKIL, CHGG, SCHL, KLC, BFAM, WLY, FC, SLM.
75 estimated company exposure inputs; 40 narrow-business scope checks.
- Reference: https://www.sec.gov/Archives/edgar/data/1013934/000101393426000006/stra-20251231.htm
- Reference: https://www.sec.gov/Archives/edgar/data/730464/000110465926092044/cvsa-20260630x10k.htm
- Reference: https://www.everycrsreport.com/reports/R46773.html

### education/online_compliance_costs

Online compliance increases operating costs.

Affected: LRN, LOPE, CVSA, STRA, DUOL, COUR, UTI, PRDO, APEI, NRDY, LINC, SKIL, CHGG, SCHL, WLY, FC.
Neutral in direct channels: LAUR, KLC, BFAM, SLM.
20 estimated company exposure inputs; 20 narrow-business scope checks.
- Reference: https://www.sec.gov/Archives/edgar/data/1434588/000110465926017047/lope-20251231x10k.htm

### education/pell_grant_change

Default grant reduction lowers funded undergraduate enrollment.

Affected: LOPE, CVSA, STRA, UTI, PRDO, APEI, LINC.
Neutral in direct channels: LRN, DUOL, COUR, LAUR, NRDY, SKIL, CHGG, SCHL, KLC, BFAM, WLY, FC, SLM.
20 estimated company exposure inputs; 20 narrow-business scope checks.
- Reference: https://www.sec.gov/Archives/edgar/data/1013934/000101393426000006/stra-20251231.htm
- Reference: https://www.sec.gov/Archives/edgar/data/730464/000110465926092044/cvsa-20260630x10k.htm

### education/school_choice_esa

ESA funding raises eligible education spending.

Affected: LRN, NRDY.
Neutral in direct channels: LOPE, CVSA, STRA, DUOL, COUR, UTI, PRDO, APEI, LAUR, LINC, SKIL, CHGG, SCHL, KLC, BFAM, WLY, FC, SLM.
20 estimated company exposure inputs; 20 narrow-business scope checks.
- Reference: https://www.edchoice.org/2026-edchoice-participation-rankings/
- Reference: https://www.sec.gov/Archives/edgar/data/1157408/000110465926090515/lrn-20260630x10k.htm

### education/student_loan_borrowing_caps

Graduate borrowing limits reduce funded graduate tuition.

Affected: LOPE, CVSA, STRA, COUR, PRDO, APEI.
Neutral in direct channels: LRN, DUOL, UTI, LAUR, NRDY, LINC, SKIL, CHGG, SCHL, KLC, BFAM, WLY, FC, SLM.
20 estimated company exposure inputs; 20 narrow-business scope checks.
- Reference: https://www.nber.org/papers/w31291
- Reference: https://freopp.org/?p=3907
- Reference: https://www.sec.gov/Archives/edgar/data/730464/000110465926092044/cvsa-20260630x10k.htm

### education/student_loan_forgiveness

Household transfer proxy increases discretionary education demand; not lender debt cancellation.

Affected: LRN, LOPE, CVSA, STRA, DUOL, COUR, UTI, PRDO, APEI, NRDY, LINC, SKIL, CHGG, SCHL, KLC, BFAM, WLY, FC.
Neutral in direct channels: LAUR, SLM.
18 estimated company exposure inputs; 0 narrow-business scope checks.
- Reference: https://www.nber.org/papers/w31291

### energy_resources/carbon_price

Covered emissions raise direct compliance cost.

Affected: XOM, CVX, COP, NEE, FSLR, FCX, EOG, OXY, DVN, SLB, HAL, WMB, PSX, VLO, MPC, DUK, SO, AEP, EXC, CEG.
Neutral in direct channels: None.
39 estimated company exposure inputs; 0 narrow-business scope checks.
- Reference: https://corporate.exxonmobil.com/news/reporting-and-publications/sustainability-report/performance-data-table
- Reference: https://www.investor.nexteraenergy.com/~/media/Files/N/NEE-IR/Sustainability/2025/Data%20Appendix.pdf
- Reference: https://www.conocophillips.com/sustainability/managing-climate-related-risks/metrics-targets

### energy_resources/clean_energy_credits_change

Default credit rollback reduces qualifying production benefits.

Affected: NEE, FSLR, DUK, SO, AEP, CEG.
Neutral in direct channels: XOM, CVX, COP, FCX, EOG, OXY, DVN, SLB, HAL, WMB, PSX, VLO, MPC, EXC.
57 estimated company exposure inputs; 20 narrow-business scope checks.
- Reference: https://www.sec.gov/Archives/edgar/data/37634/000075330826000015/nee-20251231.htm
- Reference: https://www.sec.gov/Archives/edgar/data/1274494/000127449426000021/fslr-20251231.htm

### energy_resources/critical_minerals_credit

Qualifying domestic mineral production gets an after-tax credit.

Affected: FCX.
Neutral in direct channels: XOM, CVX, COP, NEE, FSLR, EOG, OXY, DVN, SLB, HAL, WMB, PSX, VLO, MPC, DUK, SO, AEP, EXC, CEG.
19 estimated company exposure inputs; 20 narrow-business scope checks.
- Reference: https://www.sec.gov/Archives/edgar/data/831259/000083125926000012/fcx-20251231.htm

### energy_resources/crude_export_restrictions

Domestic upstream prices fall; refiner feedstock savings are a separate channel.

Affected: XOM, CVX, COP, EOG, OXY, DVN, PSX, VLO, MPC.
Neutral in direct channels: NEE, FSLR, FCX, SLB, HAL, WMB, DUK, SO, AEP, EXC, CEG.
39 estimated company exposure inputs; 40 narrow-business scope checks.
- Reference: https://www.eia.gov/analysis/requests/crude-exports
- Reference: https://www.sec.gov/Archives/edgar/data/1163165/000116316526000009/cop-20251231.htm

### energy_resources/federal_leasing_limits

Limits reduce federal-lease production revenue.

Affected: XOM, CVX, COP, EOG, OXY, DVN.
Neutral in direct channels: NEE, FSLR, FCX, SLB, HAL, WMB, PSX, VLO, MPC, DUK, SO, AEP, EXC, CEG.
20 estimated company exposure inputs; 20 narrow-business scope checks.
- Reference: https://www.eia.gov/todayinenergy/detail.php?id=65804

### energy_resources/methane_emissions_fee

Fee raises covered oil/gas facility cost, not power combustion.

Affected: XOM, CVX, COP, EOG, OXY, DVN, WMB, PSX, VLO, MPC.
Neutral in direct channels: NEE, FSLR, FCX, SLB, HAL, DUK, SO, AEP, EXC, CEG.
20 estimated company exposure inputs; 20 narrow-business scope checks.
- Reference: https://www.everycrsreport.com/reports/R48906.html
- Reference: https://www.epa.gov/inflation-reduction-act/waste-emissions-charge
- Reference: https://corporate.exxonmobil.com/news/reporting-and-publications/sustainability-report/performance-data-table

### energy_resources/spr_release

Default reserve release depresses crude price for producers.

Affected: XOM, CVX, COP, FCX, EOG, OXY, DVN.
Neutral in direct channels: NEE, FSLR, SLB, HAL, WMB, PSX, VLO, MPC, DUK, SO, AEP, EXC, CEG.
18 estimated company exposure inputs; 0 narrow-business scope checks.
- Reference: https://home.treasury.gov/news/featured-stories/the-price-impact-of-the-strategic-petroleum-reserve-release
- Reference: https://econpapers.repec.org/paper/zbwcfswop/647.htm
- Reference: https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/xom-20251231.htm

### financial_services/bank_capital_requirement

Higher CET1 lowers modeled ROE/value while EPS remains unchanged.

Affected: JPM, BAC, WFC, GS, C, AXP, MS, SCHW, BNY, STT, USB, PNC, TFC, COF, FITB, HBAN, KEY, ALLY.
Neutral in direct channels: MA, BLK, AIG, PRU, PGR.
17 estimated company exposure inputs; 0 narrow-business scope checks.
Value-only impact: the console defaults to implied share-price change; zero EPS is intentional.
- Reference: https://www.sec.gov/Archives/edgar/data/19617/000162828026008131/jpm-20251231.htm
- Reference: https://www.sec.gov/Archives/edgar/data/72971/000007297126000133/wfc-20251231.htm
- Reference: https://www.bankofengland.co.uk/external-mpc-discussion-paper/2011/optimal-bank-capital

### financial_services/credit_card_interchange_cap

Credit issuer interchange declines after a binding cap.

Affected: JPM, BAC, WFC, GS, C, USB, PNC, TFC, COF, FITB, HBAN, KEY.
Neutral in direct channels: AXP, MS, SCHW, BNY, STT, ALLY, MA, BLK, AIG, PRU, PGR.
23 estimated company exposure inputs; 23 narrow-business scope checks.
- Reference: https://www.sec.gov/Archives/edgar/data/19617/000162828026008131/jpm-20251231.htm
- Reference: https://www.sec.gov/Archives/edgar/data/831001/000083100126000011/c-20251231.htm
- Reference: https://www.federalreserve.gov/econres/feds/bank-profitability-and-debit-card-interchange-regulation-bank-responses-to-the-durbin-amendment.htm

### financial_services/credit_card_late_fee_cap

Binding late-fee cap lowers issuer fee revenue.

Affected: JPM, BAC, WFC, C, AXP, USB, PNC, TFC, COF, FITB, HBAN, KEY.
Neutral in direct channels: GS, MS, SCHW, BNY, STT, ALLY, MA, BLK, AIG, PRU, PGR.
23 estimated company exposure inputs; 23 narrow-business scope checks.
- Reference: https://www.consumerfinance.gov/about-us/newsroom/cfpb-bans-excessive-credit-card-late-fees-lowers-typical-fee-from-32-to-8/
- Reference: https://www.hklaw.com/en/insights/publications/2025/04/cfpb-credit-card-late-fees-rule-vacated-by-texas-district-court

### financial_services/fdic_assessment_increase

Higher assessment raises covered bank operating cost.

Affected: JPM, BAC, WFC, GS, C, AXP, MS, SCHW, BNY, STT, USB, PNC, TFC, COF, FITB, HBAN, KEY, ALLY.
Neutral in direct channels: MA, BLK, AIG, PRU, PGR.
23 estimated company exposure inputs; 23 narrow-business scope checks.
- Reference: https://www.fdic.gov/news/press-releases/2022/pr22073.html
- Reference: https://www.fdic.gov/resources/deposit-insurance/deposit-insurance-fund/dif-assessments.html

### financial_services/fed_rate_change

Default rate cut reduces asset-sensitive bank NII; liability-sensitive banks may differ.

Affected: JPM, BAC, WFC, GS, C, AXP, MS, SCHW, BNY, STT, USB, PNC, TFC, COF, FITB, HBAN, KEY, ALLY.
Neutral in direct channels: MA, BLK, AIG, PRU, PGR.
35 estimated company exposure inputs; 0 narrow-business scope checks.
- Reference: https://www.sec.gov/Archives/edgar/data/19617/000162828026008131/jpm-20251231.htm
- Reference: https://www.sec.gov/Archives/edgar/data/70858/000007085826000157/bac-20251231.htm
- Reference: https://www.sec.gov/Archives/edgar/data/72971/000007297126000133/wfc-20251231.htm
- Reference: https://www.sec.gov/Archives/edgar/data/831001/000083100126000011/c-20251231.htm

### financial_services/financial_transaction_tax

Transaction tax reduces trading volume and imposes modeled absorbed costs.

Affected: JPM, BAC, WFC, GS, C, MS, SCHW, BNY, STT, USB, PNC, TFC, COF, FITB, HBAN, KEY, ALLY.
Neutral in direct channels: AXP, MA, BLK, AIG, PRU, PGR.
18 estimated company exposure inputs; 0 narrow-business scope checks.
- Reference: https://www.sec.gov/Archives/edgar/data/886982/000088698226000091/gs-20251231.htm
- Reference: https://www.imf.org/en/Publications/WP/Issues/2016/12/31/Taxing-Financial-Transactions-Issues-and-Evidence-24702

### healthcare/aca_subsidy_change

Default subsidy loss reduces exchange enrollment.

Affected: UNH, ELV, CI, CNC, MOH.
Neutral in direct channels: HUM, CVS, PFE, LLY, JNJ, MRK, ABBV, AMGN, GILD, HCA, THC, UHS, TMO, ABT, MDT.
19 estimated company exposure inputs; 20 narrow-business scope checks.
- Reference: https://www.sec.gov/Archives/edgar/data/64803/000006480326000010/cvs-20251231.htm

### healthcare/medicaid_work_requirements

Eligibility loss reduces Medicaid premium and provider-volume revenue.

Affected: UNH, ELV, HUM, CVS, CNC, MOH, HCA, THC, UHS.
Neutral in direct channels: PFE, LLY, CI, JNJ, MRK, ABBV, AMGN, GILD, TMO, ABT, MDT.
16 estimated company exposure inputs; 20 narrow-business scope checks.
- Reference: https://www.cbo.gov/system/files/2025-06/Wyden-Pallone-Neal_Letter_6-4-25.pdf
- Reference: https://www.sec.gov/Archives/edgar/data/731766/000073176626000062/unh-20251231.htm

### healthcare/medicare_advantage_rate_change

Default MA payment cut lowers premium revenue.

Affected: UNH, ELV, HUM, CVS, CNC, MOH.
Neutral in direct channels: PFE, LLY, CI, JNJ, MRK, ABBV, AMGN, GILD, HCA, THC, UHS, TMO, ABT, MDT.
17 estimated company exposure inputs; 20 narrow-business scope checks.
- Reference: https://www.nber.org/papers/w20470
- Reference: https://www.sec.gov/Archives/edgar/data/49071/000004907126000009/hum-20251231.htm
- Reference: https://www.sec.gov/Archives/edgar/data/731766/000073176626000062/unh-20251231.htm
- Reference: https://www.sec.gov/Archives/edgar/data/64803/000006480326000010/cvs-20251231.htm

### healthcare/medicare_drug_price_negotiation

Lower net prices on exposed Medicare drugs reduce manufacturer revenue.

Affected: PFE, LLY, JNJ, MRK, ABBV, AMGN, GILD.
Neutral in direct channels: UNH, ELV, HUM, CVS, CI, CNC, MOH, HCA, THC, UHS, TMO, ABT, MDT.
20 estimated company exposure inputs; 0 narrow-business scope checks.
- Reference: https://www.cms.gov/newsroom/press-releases/cms-delivers-savings-seniors-15-major-drugs-cancer-chronic-disease
- Reference: https://www.milliman.com/en-GB/insight/key-takeaways-third-medicare-drug-price-negotiation

### healthcare/pbm_rebate_pass_through

Owned PBMs lose retained rebates after partial service-fee offset.

Affected: UNH, ELV, HUM, CVS, CI.
Neutral in direct channels: PFE, LLY, CNC, MOH, JNJ, MRK, ABBV, AMGN, GILD, HCA, THC, UHS, TMO, ABT, MDT.
20 estimated company exposure inputs; 20 narrow-business scope checks.
- Reference: https://www.sec.gov/Archives/edgar/data/64803/000006480326000009/cvs_ex99x1q4-25.htm
- Reference: https://www.sec.gov/Archives/edgar/data/731766/000073176626000062/unh-20251231.htm

### healthcare/pharma_tariffs

Drug/API import tariffs raise exposed pharmaceutical costs.

Affected: PFE, LLY, JNJ, MRK, ABBV, AMGN, GILD.
Neutral in direct channels: UNH, ELV, HUM, CVS, CI, CNC, MOH, HCA, THC, UHS, TMO, ABT, MDT.
20 estimated company exposure inputs; 20 narrow-business scope checks.
- Reference: https://www.aeaweb.org/articles?id=10.1257/aeri.20190536

### healthcare/site_neutral_payments

Lower hospital outpatient payments hurt providers and lower insurers claims cost.

Affected: UNH, ELV, HUM, CVS, CI, CNC, MOH, HCA, THC, UHS.
Neutral in direct channels: PFE, LLY, JNJ, MRK, ABBV, AMGN, GILD, TMO, ABT, MDT.
40 estimated company exposure inputs; 20 narrow-business scope checks.
- Reference: https://www.sec.gov/Archives/edgar/data/1156039/000115603926000013/R28.htm
- Reference: https://www.sec.gov/Archives/edgar/data/70318/000007031826000012/thc-20251231.htm
- Reference: https://www.cms.gov/files/document/2026-nfrm-opps-claims-accounting.pdf

### industrials/bonus_depreciation_rollback

Lost cash-tax deferral lowers value, without a GAAP EPS change.

Affected: CAT, DE, GE, HON, MMM, NUE, BA, ETN, EMR, ITW, PH, CMI, PCAR, DOV, ROK, STLD, CLF, CARR, OTIS, IR.
Neutral in direct channels: None.
14 estimated company exposure inputs; 0 narrow-business scope checks.
Value-only impact: the console defaults to implied share-price change; zero EPS is intentional.
- Reference: https://www.bdo.com/insights/tax/irs-issues-interim-guidance-on-bonus-depreciation-rules
- Reference: https://www.law.cornell.edu/uscode/text/26/168

### industrials/corporate_tax_rate_change

Default statutory tax increase lowers positive domestic pretax earnings after tax.

Affected: CAT, DE, GE, HON, MMM, NUE, BA, ETN, EMR, ITW, PH, CMI, PCAR, DOV, ROK, STLD, CLF, CARR, OTIS, IR.
Neutral in direct channels: None.
14 estimated company exposure inputs; 0 narrow-business scope checks.
- Reference: https://www.law.cornell.edu/uscode/text/26/11

### industrials/defense_procurement_increase

Higher defense procurement raises exposed suppliers revenue.

Affected: CAT, GE, HON, MMM, BA, ETN, EMR, ITW, PH, CMI, PCAR, DOV, ROK, CARR, OTIS, IR.
Neutral in direct channels: DE, NUE, STLD, CLF.
18 estimated company exposure inputs; 20 narrow-business scope checks.
- Reference: https://www.sec.gov/Archives/edgar/data/773840/000077384026000013/hon-20251231.htm
- Reference: https://www.sec.gov/Archives/edgar/data/40545/000004054526000008/ge-20251231.htm

### industrials/infrastructure_spending

Public infrastructure purchases raise captured equipment/material demand.

Affected: CAT, DE, GE, HON, MMM, NUE, ETN, EMR, ITW, PH, CMI, PCAR, DOV, ROK, STLD, CLF, CARR, OTIS, IR.
Neutral in direct channels: BA.
20 estimated company exposure inputs; 20 narrow-business scope checks.
- Reference: https://www.congress.gov/bill/117th-congress/house-bill/3684

### industrials/rd_credit_expansion

Incremental qualifying R&D credit is after-tax income.

Affected: CAT, DE, GE, HON, MMM, NUE, BA, ETN, EMR, ITW, PH, CMI, PCAR, DOV, ROK, STLD, CLF, CARR, OTIS, IR.
Neutral in direct channels: None.
20 estimated company exposure inputs; 0 narrow-business scope checks.
- Reference: https://www.law.cornell.edu/uscode/text/26/41

### industrials/steel_tariffs

Domestic steel producer gains tariff pricing while equipment users face costs.

Affected: CAT, DE, GE, HON, MMM, NUE, BA, ETN, EMR, ITW, PH, CMI, PCAR, DOV, ROK, STLD, CLF, CARR, OTIS, IR.
Neutral in direct channels: None.
39 estimated company exposure inputs; 0 narrow-business scope checks.
- Reference: https://www.polsinelli.com/publications/usitc-releases-report-on-the-economic-impact-of-the-section-232-and-301-tariffs-on-u-s-industries
- Reference: https://reason.com/2023/03/16/u-s-trade-commission-admits-tariffs-raised-prices-for-american-consumers/
- Reference: https://www.usitc.gov/publications/332/pub5405.pdf
- Reference: https://www.sec.gov/Archives/edgar/data/73309/000119312526071575/nue-20251231.htm
- Reference: https://www.sec.gov/Archives/edgar/data/18230/000001823026000008/cat-20251231.htm

### public_sector/consulting_contract_cancellations

Canceled federal advisory contracts reduce exposed revenue.

Affected: BAH, LDOS, SAIC, CACI, PSN, GD, KBR, ICFI, TTEK.
Neutral in direct channels: LMT, NOC, RTX, HII, OSK, KTOS, AVAV, BWXT, TXT, MRCY, VSEC.
20 estimated company exposure inputs; 20 narrow-business scope checks.
- Reference: https://www.sec.gov/Archives/edgar/data/1443646/000162828026037521/bah-20260331.htm
- Reference: https://www.sec.gov/Archives/edgar/data/40533/000004053326000006/gd-20251231.htm

### public_sector/continuing_resolution

New awards slip beyond the modeled fiscal year.

Affected: BAH, LDOS, SAIC, CACI, PSN, GD, LMT, NOC, RTX, HII, OSK, KBR, KTOS, AVAV, BWXT, TXT, ICFI, TTEK, MRCY, VSEC.
Neutral in direct channels: None.
14 estimated company exposure inputs; 0 narrow-business scope checks.
- Reference: https://www.sec.gov/Archives/edgar/data/16058/000162828026054195/caci-20260630.htm
- Reference: https://www.sec.gov/Archives/edgar/data/1443646/000162828026037521/bah-20260331.htm

### public_sector/defense_budget_increase

Higher defense budget raises relevant contract demand.

Affected: BAH, LDOS, SAIC, CACI, PSN, GD, LMT, NOC, RTX, HII, OSK, KBR, KTOS, AVAV, BWXT, TXT, ICFI, TTEK, MRCY, VSEC.
Neutral in direct channels: None.
15 estimated company exposure inputs; 0 narrow-business scope checks.
- Reference: https://www.sec.gov/Archives/edgar/data/16058/000162828026054195/caci-20260630.htm
- Reference: https://www.sec.gov/Archives/edgar/data/40533/000004053326000006/gd-20251231.htm

### public_sector/federal_civilian_budget_cut

Civilian budget cuts reduce exposed federal demand.

Affected: BAH, LDOS, SAIC, CACI, PSN, GD, LMT, NOC, RTX, HII, OSK, KBR, KTOS, AVAV, BWXT, TXT, ICFI, TTEK, MRCY, VSEC.
Neutral in direct channels: None.
16 estimated company exposure inputs; 0 narrow-business scope checks.
- Reference: https://www.sec.gov/Archives/edgar/data/1336920/000133692026000030/ldos-20260102.htm
- Reference: https://www.sec.gov/Archives/edgar/data/1443646/000162828026037521/bah-20260331.htm

### public_sector/fixed_price_shift

Cost overruns move from reimbursed to contractor-borne.

Affected: BAH, LDOS, SAIC, CACI, PSN, GD, LMT, NOC, RTX, HII, OSK, KBR, KTOS, AVAV, BWXT, TXT, ICFI, TTEK, MRCY, VSEC.
Neutral in direct channels: None.
14 estimated company exposure inputs; 0 narrow-business scope checks.
- Reference: https://www.sec.gov/Archives/edgar/data/1443646/000162828026037521/bah-20260331.htm
- Reference: https://www.sec.gov/Archives/edgar/data/1571123/000157112326000029/saic-20260130.htm

### public_sector/government_shutdown

Unrecovered service revenue is lost during a shutdown.

Affected: BAH, LDOS, SAIC, CACI, PSN, GD, LMT, NOC, RTX, HII, OSK, KBR, KTOS, AVAV, BWXT, TXT, ICFI, TTEK, MRCY, VSEC.
Neutral in direct channels: None.
17 estimated company exposure inputs; 0 narrow-business scope checks.
- Reference: https://www.sec.gov/Archives/edgar/data/1443646/000162828026003186/finalbahexhibit991q3fy26.htm
- Reference: https://www.sec.gov/Archives/edgar/data/1571123/000157112326000029/saic-20260130.htm
- Reference: https://www.sec.gov/Archives/edgar/data/40533/000004053326000006/gd-20251231.htm

### public_sector/it_modernization_funding

Incremental federal IT awards raise captured revenue.

Affected: BAH, LDOS, SAIC, CACI, PSN, GD, LMT, NOC, RTX, HII, KBR, ICFI, TTEK.
Neutral in direct channels: OSK, KTOS, AVAV, BWXT, TXT, MRCY, VSEC.
19 estimated company exposure inputs; 20 narrow-business scope checks.
- Reference: https://www.gao.gov/podcast/which-critical-government-it-systems-are-most-need-modernization
- Reference: https://www.sec.gov/Archives/edgar/data/40533/000004053326000006/gd-20251231.htm

### real_estate_hospitality/interest_rate_change

Higher rates raise refinancing cost and reduce property values.

Affected: PLD, AMT, SPG, MAR, HLT, ABNB, O, EQIX, DLR, WELL, VTR, ESS, MAA, PSA, EXR, VICI, WY, HST, RLJ, PK.
Neutral in direct channels: None.
83 estimated company exposure inputs; 0 narrow-business scope checks.
- Reference: https://www.sec.gov/Archives/edgar/data/1045609/000119312526051453/
- Reference: https://www.sec.gov/Archives/edgar/data/1063761/000110465926019419/
- Reference: https://www.cbre.com/insights/reports/us-cap-rate-survey-h1-2025

### real_estate_hospitality/lihtc_expansion

No sourced qualified investment basis in this sample. Zero is an explicit coverage gap, not economic immunity.

Affected: None quantified.
Neutral in direct channels: PLD, AMT, SPG, MAR, HLT, ABNB, O, EQIX, DLR, WELL, VTR, ESS, MAA, PSA, EXR, VICI, WY, HST, RLJ, PK.
14 estimated company exposure inputs; 0 narrow-business scope checks.
- No sourced qualified investment basis in this sample. Zero is an explicit coverage gap, not economic immunity.
- Reference: https://www.sec.gov/Archives/edgar/data/1063761/000110465926019419/

### real_estate_hospitality/like_kind_exchange_limits

Reduced exchange liquidity raises modeled property cap rates; EPS unchanged.

Affected: PLD, AMT, SPG, O, EQIX, DLR, WELL, VTR, ESS, MAA, PSA, EXR, VICI, WY, HST, RLJ, PK.
Neutral in direct channels: MAR, HLT, ABNB.
40 estimated company exposure inputs; 0 narrow-business scope checks.
Value-only impact: the console defaults to implied share-price change; zero EPS is intentional.
- Reference: https://www.ipx1031.com/wp-content/uploads/2016/07/Summary-Ling-Petrova-Study-5.2016.pdf

### real_estate_hospitality/property_tax_change

Hotel owner bears unrecovered property-tax increase.

Affected: PLD, AMT, SPG, MAR, HLT, O, EQIX, DLR, WELL, VTR, ESS, MAA, PSA, EXR, VICI, WY, HST, RLJ, PK.
Neutral in direct channels: ABNB.
38 estimated company exposure inputs; 20 narrow-business scope checks.
- RLJ: >100% earnings change; small/loss baseline or linear approximation needs caution
- RLJ: implied loss exceeds equity value; constant-multiple approximation outside useful range
- Reference: https://www.sec.gov/Archives/edgar/data/1063761/000110465926019419/
- Reference: https://www.sec.gov/Archives/edgar/data/1045609/000119312526051453/

### real_estate_hospitality/return_to_office_mandate

More office-linked activity raises exposed footfall.

Affected: SPG, MAR, HLT, ABNB, HST, RLJ, PK.
Neutral in direct channels: PLD, AMT, O, EQIX, DLR, WELL, VTR, ESS, MAA, PSA, EXR, VICI, WY.
20 estimated company exposure inputs; 20 narrow-business scope checks.
- Reference: https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/
- Reference: https://ir.hosthotels.com/news-releases/news-release-details/host-hotels-resorts-inc-reports-results-2025

### real_estate_hospitality/short_term_rental_regulation

Restrictions lower covered short-term rental bookings; hotels can gain.

Affected: MAR, HLT, ABNB, HST, RLJ, PK.
Neutral in direct channels: PLD, AMT, SPG, O, EQIX, DLR, WELL, VTR, ESS, MAA, PSA, EXR, VICI, WY.
37 estimated company exposure inputs; 0 narrow-business scope checks.
- Reference: https://people.bu.edu/zg/publications/airbnb.pdf
- Reference: https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/

### real_estate_hospitality/visa_fee_tourism_tax

Higher entry costs reduce inbound visitor spending.

Affected: SPG, MAR, HLT, ABNB, HST, RLJ, PK.
Neutral in direct channels: PLD, AMT, O, EQIX, DLR, WELL, VTR, ESS, MAA, PSA, EXR, VICI, WY.
20 estimated company exposure inputs; 20 narrow-business scope checks.
- Reference: https://www.travelmole.com/news/economic-impact-overseas-visitors-usa/

### tmt/app_store_commission_cap

Binding app-store commission cap reduces platform fee revenue.

Affected: AAPL, GOOGL.
Neutral in direct channels: MSFT, META, NVDA, VZ, IBM, ORCL, CRM, ADBE, INTC, AMD, QCOM, MU, AVGO, CSCO, T, CMCSA, NFLX, DIS.
20 estimated company exposure inputs; 20 narrow-business scope checks.
- Reference: https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/R69.htm
- Reference: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000018/R44.htm

### tmt/broadband_affordability_subsidy

Broadband subsidies raise access-provider subscriber spending.

Affected: VZ, T, CMCSA.
Neutral in direct channels: AAPL, MSFT, GOOGL, META, NVDA, IBM, ORCL, CRM, ADBE, INTC, AMD, QCOM, MU, AVGO, CSCO, NFLX, DIS.
20 estimated company exposure inputs; 20 narrow-business scope checks.
- Reference: https://broadbandbreakfast.com/verizon-reports-drop-in-prepaid-subscribers-after-acp-sunset

### tmt/chip_export_controls

Restricted chip exports reduce merchant chip sales; retaliation is a separate channel.

Affected: AAPL, MSFT, GOOGL, META, NVDA, IBM, ORCL, CRM, ADBE, INTC, AMD, QCOM, MU, AVGO, CSCO, NFLX, DIS.
Neutral in direct channels: VZ, T, CMCSA.
38 estimated company exposure inputs; 40 narrow-business scope checks.
- Reference: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/R84.htm
- Reference: https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/R68.htm

### tmt/chips_manufacturing_credit

Credit applies to qualifying estimated US manufacturing capex, including Intel/Micron.

Affected: INTC, MU.
Neutral in direct channels: AAPL, MSFT, GOOGL, META, NVDA, VZ, IBM, ORCL, CRM, ADBE, AMD, QCOM, AVGO, CSCO, T, CMCSA, NFLX, DIS.
20 estimated company exposure inputs; 20 narrow-business scope checks.
- Reference: https://www.law.cornell.edu/uscode/text/26/48D

### tmt/data_privacy_mandate

Ad-targeting loss and privacy compliance raise costs/reduce monetization.

Affected: AAPL, MSFT, GOOGL, META, NVDA, VZ, IBM, ORCL, CRM, ADBE, INTC, AMD, QCOM, MU, AVGO, CSCO, T, CMCSA, NFLX, DIS.
Neutral in direct channels: None.
38 estimated company exposure inputs; 20 narrow-business scope checks.
- Reference: https://www.aeaweb.org/doi/10.1257/pol.20210309
- Reference: https://itpro.com/security/privacy/362151/meta-says-apples-ios-privacy-changes-will-cost-it-10-billion-in-2022

### tmt/digital_services_tax

Tax applies to US digital advertising and covered platform fees.

Affected: AAPL, MSFT, GOOGL, META, NFLX, DIS.
Neutral in direct channels: NVDA, VZ, IBM, ORCL, CRM, ADBE, INTC, AMD, QCOM, MU, AVGO, CSCO, T, CMCSA.
38 estimated company exposure inputs; 40 narrow-business scope checks.
- Reference: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000018/R44.htm
- Reference: https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/R46.htm
- Reference: https://ppc.land/google-ads-to-pass-cost-of-digital-taxes-to-advertisers-starting-in-november/

### tmt/semiconductor_tariffs

Tariffs raise imported semiconductor/hardware cost.

Affected: AAPL, MSFT, GOOGL, META, NVDA, VZ, IBM, ORCL, CRM, ADBE, INTC, AMD, QCOM, MU, AVGO, CSCO, T, CMCSA, NFLX, DIS.
Neutral in direct channels: None.
20 estimated company exposure inputs; 0 narrow-business scope checks.
- Reference: https://www.aeaweb.org/doi/10.1257/jep.33.4.187
- Reference: https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/R69.htm
- Reference: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/R84.htm

### transportation_logistics/airline_bag_fee_cap

Binding baggage cap reduces airline ancillary revenue.

Affected: DAL, UAL, AAL, LUV.
Neutral in direct channels: UPS, FDX, UNP, TSLA, GM, F, RIVN, CHRW, JBHT, ODFL, XPO, SAIA, CSX, NSC, UBER, LYFT.
20 estimated company exposure inputs; 20 narrow-business scope checks.
- AAL: >100% earnings change; small/loss baseline or linear approximation needs caution
- AAL: implied loss exceeds equity value; constant-multiple approximation outside useful range
- Reference: https://www.aol.com/airlines-raked-over-7b-revenue-152456333.html
- Reference: https://www.sec.gov/Archives/edgar/data/27904/000002790426000013/dal-20251231.htm

### transportation_logistics/airline_ticket_tax_change

Higher ticket tax reduces demand and modeled fare retention.

Affected: DAL, UAL, AAL, LUV.
Neutral in direct channels: UPS, FDX, UNP, TSLA, GM, F, RIVN, CHRW, JBHT, ODFL, XPO, SAIA, CSX, NSC, UBER, LYFT.
19 estimated company exposure inputs; 20 narrow-business scope checks.
- AAL: >100% earnings change; small/loss baseline or linear approximation needs caution
- AAL: implied loss exceeds equity value; constant-multiple approximation outside useful range
- Reference: https://www.sec.gov/Archives/edgar/data/27904/000002790426000013/dal-20251231.htm
- Reference: https://WWW.CAA.CO.UK/media/qcrcutdj/annex-3-stansted-s-own-airport-charge-elasticity-a-summary-of-the-evidence-and-research.pdf

### transportation_logistics/auto_import_tariffs

Imported vehicles/parts and owned-fleet procurement face tariff costs.

Affected: UPS, FDX, UNP, DAL, TSLA, GM, F, RIVN, JBHT, ODFL, XPO, SAIA, CSX, NSC, UAL, AAL, LUV.
Neutral in direct channels: CHRW, UBER, LYFT.
19 estimated company exposure inputs; 20 narrow-business scope checks.
- Reference: https://www.sec.gov/Archives/edgar/data/1467858/000146785826000013/gm-20251231.htm
- Reference: https://www.sec.gov/Archives/edgar/data/1318605/000162828026003952/tsla-20251231.htm

### transportation_logistics/carbon_tax_transport_fuel

Owned-fleet fuel carbon cost is partially recovered through pricing.

Affected: UPS, FDX, UNP, DAL, TSLA, GM, F, RIVN, JBHT, ODFL, XPO, SAIA, CSX, NSC, UAL, AAL, LUV.
Neutral in direct channels: CHRW, UBER, LYFT.
39 estimated company exposure inputs; 20 narrow-business scope checks.
- AAL: >100% earnings change; small/loss baseline or linear approximation needs caution
- AAL: implied loss exceeds equity value; constant-multiple approximation outside useful range
- Reference: https://www.eia.gov/environment/emissions/co2_vol_mass.php
- Reference: https://www.sec.gov/Archives/edgar/data/27904/000002790426000013/dal-20251231.htm
- Reference: https://www.sec.gov/Archives/edgar/data/100885/000010088526000037/unp-20251231.htm

### transportation_logistics/ev_tax_credit

Buyer incentive increases covered US EV demand.

Affected: TSLA, GM, F, RIVN.
Neutral in direct channels: UPS, FDX, UNP, DAL, CHRW, JBHT, ODFL, XPO, SAIA, CSX, NSC, UAL, AAL, LUV, UBER, LYFT.
20 estimated company exposure inputs; 0 narrow-business scope checks.
- Reference: https://www.nber.org/papers/w25359
- Reference: https://www.coxautoinc.com/insights/dec-2025-atp-report/
- Reference: https://electrek.co/2026/01/06/gm-sold-twice-as-many-evs-as-ford-2025/

### transportation_logistics/vehicle_emissions_credit_rollback

Weaker standards hurt credit sellers and help credit purchasers.

Affected: TSLA, GM, F, RIVN.
Neutral in direct channels: UPS, FDX, UNP, DAL, CHRW, JBHT, ODFL, XPO, SAIA, CSX, NSC, UAL, AAL, LUV, UBER, LYFT.
39 estimated company exposure inputs; 40 narrow-business scope checks.
- Reference: https://www.sec.gov/Archives/edgar/data/1318605/000162828026003952/tsla-20251231.htm
- Reference: https://www.sec.gov/Archives/edgar/data/1467858/000146785826000013/gm-20251231.htm


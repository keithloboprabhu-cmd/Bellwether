# Bellwether quantitative audit

Evidence collected 31 October–1 November 2026. Changes are local phase commits; this audit has not been pushed to GitHub or deployed.

**The requested full empirical certification is not achieved.** All configured policies have A–F reports, but all 72 remain FAIL-UNRESOLVED under the requested full-cohort, legal-scope, matched-benchmark, totals and duration requirements. Passing software checks is not a policy-accuracy certification. No missing evidence was replaced with invented parameters.

## Inventory and coverage

| Item | Before | After |
|---|---:|---:|
| Active companies | 203 | 234 |
| Industries | 10 | 10 |
| Industry policies | 66 | 72 |
| Macro shocks | 10 | 10 |
| Explicit own-industry company/policy decisions | 1,338 | 1,694 |
| Nonzero default EPS/value coverage | Not established by the old scope audit | 229/234 |

The five remaining coverage failures are **BLK, LYFT, MDT, PGR, SLM**. Revenue-only effects and inactive missing-exposure sentinels do not qualify. See [coverage matrix](coverage_matrix.csv) and [gap explanations](coverage_gaps.md).

### Publisher lists and admission decisions

- **Fortune 100 (2026):** all 100 publisher ranking rows and company profiles archived. 81/100 active, or 81/90 public ordinary-equity candidates. Eight private/mutual companies are explicitly excluded; FNMA and FMCC remain in a separate conservatorship category. Nine public candidates are deferred.
- **S&P 100:** full current publisher constituent list was not obtained. The publisher page verified its top ten and 101 securities only; HTTP access to the complete resource was blocked. No full S&P membership percentage is certified. The separately labeled iShares OEF cross-check has 101 securities/100 deduplicated issuers, 94/100 active. It is fund-issuer evidence, not the requested S&P publisher list.
- Share-class deduplication maps GOOG/GOOGL to GOOGL and Berkshire A/B to a single deferred BRK-A identity. Visa uses Class A-equivalent diluted shares rather than an unweighted sum of unequal classes. Existing ticker changes remain in the identity pipeline.
- New issuers use their SEC SIC and actual segment/business descriptions. No original issuer was removed. Exact statements are retained with normalization flags; unsupported borrowing/cost quantities are not represented as reported zeros. New legacy-policy/macro exposures remain explicitly unquantified until measured; no peer exposure was copied.
- Palantir and PayPal were admitted after actual annual covers confirmed Delaware despite blank SEC submissions metadata. Charter is also Delaware, but its positive US pretax exposure was not separately quantified; US revenue alone is insufficient.

Primary sources: [Fortune publisher ranking](https://fortune.com/ranking/fortune500/), [S&P publisher](https://www.spglobal.com/spdji/en/indices/equity/sp-100/#data), [OEF issuer holdings](https://www.ishares.com/us/products/239723/ishares-s-p-100-etf/latest-holdings.csv). Raw sources and every initial membership decision are in `data/universe_sources/`; final active/deferred decisions are in `admission_decisions.json`.

**Added (31):** ALL, AMAT, ANET, CAH, COR, DELL, GEV, HPQ, INTU, ISRG, LRCX, MCK, MDLZ, MET, MO, NOW, PANW, PFGC, PM, SNDK, SNEX, SNX, SPGI, SYY, TMUS, TRV, TSN, TXN, V, PLTR, PYPL.

| Deferred public candidate | Reason |
|---|---|
| ACI | Admission deferred: positive current US pretax exposure not verified |
| ACN | Admission deferred: non-US incorporation: domestic tax geography requires explicit US jurisdiction reconciliation; positive current US pretax exposure not verified |
| ADM | Admission deferred: positive current US pretax exposure not verified |
| BKNG | Admission deferred: positive current US pretax exposure not verified; no sourced policy for this industry |
| BMY | Admission deferred: positive current US pretax exposure not verified |
| BRK-A | Admission deferred: required statement/share/cost field missing; partnership/share-class basis requires review |
| CHTR | Admission deferred: Delaware incorporation verified on actual 10-K cover, but positive current US pretax exposure not separately quantified. US revenue is not a US taxable-income measurement; no 100% share invented. |
| DHR | Admission deferred: positive current US pretax exposure not verified |
| EPD | Admission deferred: positive current US pretax exposure not verified; partnership/share-class basis requires review; no sourced policy for this industry |
| ET | Admission deferred: required statement/share/cost field missing; positive current US pretax exposure not verified; partnership/share-class basis requires review; no sourced policy for this industry |
| GLXY | Admission deferred: positive current US pretax exposure not verified |
| INGM | Admission deferred: positive current US pretax exposure not verified |
| LIN | Admission deferred: non-US incorporation: domestic tax geography requires explicit US jurisdiction reconciliation |

| Fortune exclusion/separate category | Decision |
|---|---|
| Fannie Mae | Federal conservatorship; separate category, not ordinary financial equity |
| State Farm Insurance | No publicly traded equity; excluded from stock valuation |
| Freddie Mac | Federal conservatorship; separate category, not ordinary financial equity |
| New York Life Insurance | No publicly traded equity; excluded from stock valuation |
| Nationwide | No publicly traded equity; excluded from stock valuation |
| Publix Super Markets | No publicly traded equity; excluded from stock valuation |
| United Services Automobile Assn. | No publicly traded equity; excluded from stock valuation |
| TIAA | No publicly traded equity; excluded from stock valuation |
| Liberty Mutual Insurance Group | No publicly traded equity; excluded from stock valuation |
| Massachusetts Mutual Life Insurance | No publicly traded equity; excluded from stock valuation |

### Six new policies

One submitted federal rate proposal, [S.Amdt.2428, section 71117](https://www.congress.gov/amendment/119th-congress/senate-amendment/2428/text), is represented in six industry entries. It proposed 21% → 28%; it was submitted, **not enacted**. Positive reported US book pretax income is a labeled taxable-income proxy; credits, tax losses, deferred-tax remeasurement and behavioral response are omitted. Historical income bounds are not confidence intervals. Exact company lists are in the coverage-gap report.

- `consumer_retail/us_corporate_tax_consumer_retail`
- `education/us_corporate_tax_education`
- `financial_services/us_corporate_tax_financial_services`
- `healthcare/us_corporate_tax_healthcare`
- `tmt/us_corporate_tax_tmt`
- `transportation_logistics/us_corporate_tax_transportation_logistics`

## Phase 1 findings and final disposition

| Issue | Root cause and final action | Unresolved limit |
|---|---|---|
| KR/BBY/TGT tariffs | KR cost line $113,240M added from actual filing. Losses remain uncapped and >50% default EPS effects are flagged. | Import shares, pass-through and demand priors remain UNVERIFIED. KR still has an implausibly large modeled loss; this is unresolved, not a successful tariff calibration. |
| Steel tariffs | Separate buyer and producer responses: USITC table 5.2 gives +2.39% and +0.74% under 25% tariffs, replacing a conflated response. | Company shares and earnings flow-through unverified; full-year EPS/margin growth is not a causal tariff response. |
| AMD / Intel | Revenue can rise while unrecovered imported costs reduce profit; this is algebraically consistent. Intel is now explicitly unavailable for permanent P/E valuation without supported normalized earnings. | AMD imported-cost denominator and pass-through not independently verified. No invented positive Intel valuation. |
| COF rate / valuation | Own Table 32 NII sensitivities replace peer assumptions. Three issuer-adjusted annual EPS values, 12.52/13.96/19.61, support a 13.96 valuation median. Reported EPS percentage denominator is unchanged. | Non-GAAP exclusions can recur; pre-Discover years are not merged-company pro-forma history. Rate sensitivity horizon is not permanent equity persistence. |
| AmEx / networks | Hypothetical four-party credit-issuer cap excludes three-party merchant discount and network service fees as written; Visa added. | No enacted US credit-card counterpart to debit Regulation II claimed. Expansion of the hypothetical scope needs judgment. |
| Negative Humana price | Projected equity price floored at zero, equity-wiped-out label and value-reconciliation adjustment; earnings losses remain uncapped. | Other issuers without verified adjusted earnings stay unavailable, rather than using an unsupported P/E. |
| Debt / finance arms | Alternate GAAP/custom facts and actual filing supplements. F/GM/DE/PCAR/TXT industrial borrowings separated from captive finance; leases are not indiscriminately added. EXR complete term plus revolver/commercial-paper debt is $13,230.651M. | Several education borrowing bases remain unquantified. A missing tag is not a reported zero. |
| Missing costs | Exact alternate tags/filing supplements; insurer claims and loss expense replaces merchandise COGS. | Operating/gross cost is not necessarily incremental cost; service-company profit transmission remains open. |
| Old cover shares | Latest period before filing-order selection; dimensional class counts from current annual covers for CMCSA/MA/NKE/SCHL. | Annual diluted EPS and current economic shares can differ; Visa Class A-equivalent proxy explicitly flagged. |
| Tax clipping | Preserve raw rate; preceding ordinary-rate median or era-appropriate federal statutory fallback replaces hard clipping. | 0–40% anomaly screen is a judgment, not a legal bound; state/foreign/special-item normalization incomplete. |
| Only 12 live quotes | Removed 12-ticker request cap; all due tickers use bounded batching/retries. Added issuers have actual Yahoo observations. Old parser caches invalidated by normalization version. | Free providers can fail or lag; per-record observation dates and snapshot fallbacks remain visible. |

Regression tests cover these code/data rules. Unverified economic coefficients were retained per the brief. Phase 1 checkpoint values in `PHASE1_ISSUES.md` are superseded by the stricter final adjusted-EPS guard and peer-sensitivity changes documented here.

## Policy scorecard

Whole-policy verdict counts: FAIL-UNRESOLVED: 72.

Twenty-three exact bank sensitivity comparisons pass direction and size after twelve coefficient changes at six banks. Steel has a verified sector-price calibration. These are in-sample checks; neither validates every company, official total, legal omission or permanent valuation horizon. Per-policy reports include source/value rows, unmatched evidence, tornado outputs and ranking where at least five like-for-like observations exist.

| Policy / report | Verdict | Matched / passed benchmarks | Changed parameters |
|---|---|---:|---:|
| [consumer_retail/consumer_tax_rebate](policies/consumer_tax_rebate.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [consumer_retail/import_tariffs](policies/import_tariffs.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [consumer_retail/minimum_wage_increase](policies/minimum_wage_increase.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [consumer_retail/sales_tax_change](policies/sales_tax_change.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [consumer_retail/snap_benefit_change](policies/snap_benefit_change.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [consumer_retail/sweetened_beverage_tax](policies/sweetened_beverage_tax.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [consumer_retail/us_corporate_tax_consumer_retail](policies/us_corporate_tax_consumer_retail.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [education/earnings_accountability_test](policies/earnings_accountability_test.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [education/ninety_ten_rule_change](policies/ninety_ten_rule_change.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [education/online_compliance_costs](policies/online_compliance_costs.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [education/pell_grant_change](policies/pell_grant_change.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [education/school_choice_esa](policies/school_choice_esa.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [education/student_loan_borrowing_caps](policies/student_loan_borrowing_caps.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [education/student_loan_forgiveness](policies/student_loan_forgiveness.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [education/us_corporate_tax_education](policies/us_corporate_tax_education.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [energy_resources/carbon_price](policies/carbon_price.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [energy_resources/clean_energy_credits_change](policies/clean_energy_credits_change.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [energy_resources/critical_minerals_credit](policies/critical_minerals_credit.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [energy_resources/crude_export_restrictions](policies/crude_export_restrictions.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [energy_resources/federal_leasing_limits](policies/federal_leasing_limits.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [energy_resources/methane_emissions_fee](policies/methane_emissions_fee.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [energy_resources/spr_release](policies/spr_release.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [financial_services/bank_capital_requirement](policies/bank_capital_requirement.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [financial_services/credit_card_interchange_cap](policies/credit_card_interchange_cap.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [financial_services/credit_card_late_fee_cap](policies/credit_card_late_fee_cap.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [financial_services/fdic_assessment_increase](policies/fdic_assessment_increase.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [financial_services/fed_rate_change](policies/fed_rate_change.md) | FAIL-UNRESOLVED | 23 / 23 | 12 |
| [financial_services/financial_transaction_tax](policies/financial_transaction_tax.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [financial_services/us_corporate_tax_financial_services](policies/us_corporate_tax_financial_services.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [healthcare/aca_subsidy_change](policies/aca_subsidy_change.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [healthcare/medicaid_work_requirements](policies/medicaid_work_requirements.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [healthcare/medicare_advantage_rate_change](policies/medicare_advantage_rate_change.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [healthcare/medicare_drug_price_negotiation](policies/medicare_drug_price_negotiation.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [healthcare/pbm_rebate_pass_through](policies/pbm_rebate_pass_through.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [healthcare/pharma_tariffs](policies/pharma_tariffs.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [healthcare/site_neutral_payments](policies/site_neutral_payments.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [healthcare/us_corporate_tax_healthcare](policies/us_corporate_tax_healthcare.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [industrials/bonus_depreciation_rollback](policies/bonus_depreciation_rollback.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [industrials/corporate_tax_rate_change](policies/corporate_tax_rate_change.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [industrials/defense_procurement_increase](policies/defense_procurement_increase.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [industrials/infrastructure_spending](policies/infrastructure_spending.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [industrials/rd_credit_expansion](policies/rd_credit_expansion.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [industrials/steel_tariffs](policies/steel_tariffs.md) | FAIL-UNRESOLVED | 0 / 0 | 2 |
| [public_sector/consulting_contract_cancellations](policies/consulting_contract_cancellations.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [public_sector/continuing_resolution](policies/continuing_resolution.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [public_sector/defense_budget_increase](policies/defense_budget_increase.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [public_sector/federal_civilian_budget_cut](policies/federal_civilian_budget_cut.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [public_sector/fixed_price_shift](policies/fixed_price_shift.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [public_sector/government_shutdown](policies/government_shutdown.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [public_sector/it_modernization_funding](policies/it_modernization_funding.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [real_estate_hospitality/interest_rate_change](policies/interest_rate_change.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [real_estate_hospitality/lihtc_expansion](policies/lihtc_expansion.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [real_estate_hospitality/like_kind_exchange_limits](policies/like_kind_exchange_limits.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [real_estate_hospitality/property_tax_change](policies/property_tax_change.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [real_estate_hospitality/return_to_office_mandate](policies/return_to_office_mandate.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [real_estate_hospitality/short_term_rental_regulation](policies/short_term_rental_regulation.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [real_estate_hospitality/visa_fee_tourism_tax](policies/visa_fee_tourism_tax.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [tmt/app_store_commission_cap](policies/app_store_commission_cap.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [tmt/broadband_affordability_subsidy](policies/broadband_affordability_subsidy.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [tmt/chip_export_controls](policies/chip_export_controls.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [tmt/chips_manufacturing_credit](policies/chips_manufacturing_credit.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [tmt/data_privacy_mandate](policies/data_privacy_mandate.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [tmt/digital_services_tax](policies/digital_services_tax.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [tmt/semiconductor_tariffs](policies/semiconductor_tariffs.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [tmt/us_corporate_tax_tmt](policies/us_corporate_tax_tmt.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [transportation_logistics/airline_bag_fee_cap](policies/airline_bag_fee_cap.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [transportation_logistics/airline_ticket_tax_change](policies/airline_ticket_tax_change.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [transportation_logistics/auto_import_tariffs](policies/auto_import_tariffs.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [transportation_logistics/carbon_tax_transport_fuel](policies/carbon_tax_transport_fuel.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [transportation_logistics/ev_tax_credit](policies/ev_tax_credit.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [transportation_logistics/us_corporate_tax_transportation_logistics](policies/us_corporate_tax_transportation_logistics.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |
| [transportation_logistics/vehicle_emissions_credit_rollback](policies/vehicle_emissions_credit_rollback.md) | FAIL-UNRESOLVED | 0 / 0 | 0 |

## Backtests: unchanged sample and expanded sample

Original sample: 104/120 (86.7%). Expanded sample: 155/190 (81.6%), 13 cases across ten industries. Industry-balanced expanded score: 85.75%. Excluded company-cases: 124.

Each row compares a specific financial metric, not stock-return prediction. MAE units differ and must not be pooled. Before MAE is on the original cohort; after MAE uses the expanded cohort. The common-cohort table below isolates recalibration from additions.

| Case | Metric unit | Before n / hit % | Before MAE / no-change | After n / hit % | After MAE / no-change |
|---|---|---:|---:|---:|---:|
| tcja-tmt | pp | 15 / 86.667 | 6.824 / 11.724 | 22 / 81.818 | 6.610 / 12.151 |
| fed_rate_change | % | 18 / 88.889 | 19.258 / 21.057 | 18 / 88.889 | 18.908 / 21.057 |
| fed-2018 | % | New | — | 18 / 83.333 | 9.987 / 10.615 |
| fed-2020 | % | New | — | 18 / 61.111 | 11.908 / 12.300 |
| tcja-consumer_retail | pp | 19 / 84.211 | 3.297 / 9.908 | 23 / 82.609 | 8.721 / 14.463 |
| tcja-healthcare | pp | 16 / 81.250 | 13.476 / 17.751 | 18 / 77.778 | 13.310 / 16.977 |
| steel-232 | pp | 3 / 66.667 | 0.837 / 2.219 | 17 / 64.706 | 2.090 / 2.151 |
| tcja-energy_resources | pp | 7 / 100.000 | 5.432 / 11.839 | 7 / 100.000 | 5.432 / 11.839 |
| tcja-transportation_logistics | pp | 14 / 100.000 | 1.244 / 13.804 | 14 / 100.000 | 1.244 / 13.804 |
| defense_budget_increase | % | 20 / 80.000 | 21.280 / 22.055 | 20 / 80.000 | 21.280 / 22.055 |
| tcja-real_estate_hospitality | pp | 1 / 100.000 | 5.219 / 15.253 | 1 / 100.000 | 5.219 / 15.253 |
| pell_grant_change | % | 7 / 85.714 | 20.279 / 20.486 | 7 / 85.714 | 20.279 / 20.486 |
| pell-2022 | % | New | — | 7 / 100.000 | 21.544 / 21.734 |

**Common original cohort after changes: 104/120 (86.7%), versus 104/120 before.** All original eligible company-cases remain present.

| Original case | n | Hits before → after | MAE before → after |
|---|---:|---:|---:|
| tcja-tmt | 15 | 13 → 13 | 6.824 → 6.824 |
| fed_rate_change | 18 | 16 → 16 | 19.258 → 18.908 |
| tcja-consumer_retail | 19 | 16 → 16 | 3.297 → 3.297 |
| tcja-healthcare | 16 | 13 → 13 | 13.476 → 13.476 |
| steel-232 | 3 | 2 → 2 | 0.837 → 2.105 |
| tcja-energy_resources | 7 | 7 → 7 | 5.432 → 5.432 |
| tcja-transportation_logistics | 14 | 14 → 14 | 1.244 → 1.244 |
| defense_budget_increase | 20 | 16 → 16 | 21.280 → 21.280 |
| tcja-real_estate_hospitality | 1 | 1 → 1 | 5.219 → 5.219 |
| pell_grant_change | 7 | 6 → 6 | 20.279 → 20.279 |

Steel common-cohort MAE worsens because the sourced causal sector-price response replaces a coefficient that happened to fit total annual earnings better. It is retained: fitting annual volume, tax and mix would misattribute non-policy effects. Expanded consumer MAE also worsens because the admitted companies change the cohort; the common original consumer cohort is unchanged. The original bank cohort magnitude improves slightly. No observation or company was dropped to preserve a headline.

Three new non-TCJA cases are **2018 Fed tightening, 2020 Fed easing and the 2022–23 Pell maximum increase**. The steel case also expands beyond its original three companies. Daily FRED annual means and enacted Pell maximum schedules are sourced. Bank annual-average rate paths are not instantaneous sensitivity shocks; Pell award maxima are not company revenue effects. The 2020 pandemic, balance-sheet changes, enrollment and acquisitions are major confounders. Six other industry cases share one TCJA episode; current exposures and restated filings introduce look-ahead risk. These are retrospective diagnostics, not independent causal forecasts or a probability of future correctness.

## Arithmetic and software validation

The reproducible stratified random draw (seed 20261031, one affected default scenario per industry) independently recomputes channel effects, pretax-to-tax-to-parent income, diluted-share EPS and duration-specific value. It reuses the configured expression evaluator but not the engine channel/aggregation/valuation implementations. Ten calculations match EPS and price to the cent; unavailable price remains unavailable. Formulas and intermediate values are in [spotchecks.md](spotchecks.md).

- **Python suite:** 610 passed, 5 skipped; 6 intentional extreme-EPS review warnings.
- **Frontend suite:** 16 passed.
- **Production frontend build:** Passed (TypeScript and Vite).
- **Internal policy/macro audit:** 72 industry policies and 10 macro shocks; zero invariant failures.
- **Published bank benchmark arithmetic:** 23 matched comparisons pass direction and size (in-sample calibration only).
- **Independent arithmetic:** 10/10 stratified random scenarios match to the cent.
- **Running local API audit:** 72 industry policies / 261 valid inputs and 10 macro shocks / 42 valid inputs; zero failures.
- **Macro console browser verification:** All-industries deep link restores policy/inputs; industry drilldown filters Financial Services to 30 firms; industry CSV has 10 rows/234 firms and reconciles net income; no browser console errors; phone layout fits at 375 px.

Scenario URLs, original policy IDs, CSV export columns and schema-version-1 profile JSON remain compatible. Reference-company profile import/lookup follows the same sourced normalization guard when the financial basis matches; edited financials do not silently borrow another basis.

## Open items requiring judgment, ranked by impact

1. **Large tariff/cost projections:** obtain company-specific import denominators, realized tariff cost and pass-through. KR/BBY/TGT and AMD values remain UNVERIFIED. Do not publish extreme EPS losses as calibrated forecasts. Operating costs can include fixed expenses; TTEK’s reported cost proxy implies an 84.8% contribution margin, which is not an independently supported incremental margin. Preserve reported facts and review the transmission model.
2. **Full empirical and legal certification:** most policy cohorts lack matched published sensitivities, official comparable totals or independently checked thresholds, effective dates and horizons. Bank instantaneous annual NII sensitivity does not justify permanent valuation. All 72 full-policy verdicts therefore remain unresolved, even where a coefficient was repaired. Prioritize regulated-bank, MA and tariff scenarios with obtainable exact disclosures before broader claims.
3. **Five mandatory coverage gaps:** BLK parent/minority tax-base reconciliation; PGR US taxable base; SLM insured-bank NII/assessment data in the education bucket; LYFT loss-year/nonbinding tax base and unquantified buyback excise tax; MDT Irish-versus-US geography. Do not infer FDIC insurance for insurer policyholders or tuition exposure for a lender.
4. **Incomplete target universe:** obtain the full publisher S&P list, then resolve the deferred public issuers. Berkshire needs insurer/investment accounting and economically equivalent shares; ET/EPD partnership taxation differs from corporate tax; foreign domicile requires an explicit US base; negative or missing domestic income cannot be replaced with a guessed positive amount.
5. **Normalized valuation:** verify adjusted three-year histories or a fully reconciled EV/EBITDA method for other depressed/negative-EPS issuers. COF issuer non-GAAP amortization exclusions can recur and its acquisition changes comparability. No unadjusted median is labeled normalized.
6. **Data definitions and timing:** remaining unknown borrowing balances, fixed-versus-variable cost definitions, annual/current share mismatches and geographic book-to-tax conversion need exact evidence. Cloud provider availability and per-record freshness are not guaranteed.
7. **Historical validation design:** source point-in-time exposures and independent event studies. The 81.6% expanded score combines correlated, confounded episodes and is not forecast certification. Additional genuine events should not be manufactured from mismatched metrics.

No unsourced judgment above was silently changed. Review failures and missing evidence are part of the delivered audit, not passed checks.

## Artifacts and reproduction

- [Architecture and phase-0 baseline](../docs/ARCHITECTURE_AUDIT.md)
- [Source registry](../data/sources_registry.csv): exact verified facts versus UNVERIFIED coefficients and model controls.
- [Coverage matrix](coverage_matrix.csv), [coverage failures/new-policy company lists](coverage_gaps.md).
- [Per-policy scorecard CSV](policy_scorecard.csv), [matched benchmarks](benchmark_checks.json).
- [Before](backtests_before.json), [after](backtests_after.json), [common-cohort comparison](backtest_comparison.json).
- [Arithmetic report](spotchecks.md), [methodology](../METHODOLOGY.md), [changelog](../CHANGELOG.md).

Run the commands in README’s quantitative-audit section. The admission scripts deliberately refuse a repeated mutation; cached raw SEC documents and their exact contexts support review. No paid API, runtime LLM or new dependency was added.

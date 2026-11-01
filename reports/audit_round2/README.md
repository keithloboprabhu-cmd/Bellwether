# Continuing economic audit — 1 November 2026

This checkpoint corrects verified measurement errors. All 72 whole-policy evidence verdicts remain unresolved; source measurements and passing software checks do not establish forecast accuracy.

## Corrections

- **TTEK costs:** FY2025 revenue $5,442.590M less gross profit $961.344M gives full revenue costs $4,481.246M. The previous $825.230M generic tag covered subcontractors only and omitted $3,656.016M of other revenue costs. Comparative FY2024/FY2023 full costs are $4,332.239M/$3,797.521M. The new parser setting is issuer-specific; a reported gross margin still is not a measured incremental margin. [Actual annual statement](https://www.sec.gov/Archives/edgar/data/831641/000083164125000032/ttek-20250928.htm).
- **Airline baggage fees:** replace copied Delta shares with FY2025 official BTS observations: American $1,465.339192M; Delta $1,089.832M; United $1,351.302143M; Southwest $582.416M. Original workbook units are USD thousands, converted to millions before dividing by revenue. These four observations sum to $4,488.889335M, below the reported all-carrier $7,439.725895M. This checks the observed fee base, not future fare recapture or profit. [Official BTS workbook page](https://www.bts.gov/topics/airlines-and-airports/baggage-fees-airline-2025).
- **Ticket exposure:** American's domestic passenger revenue is $35,201M, not Delta's share applied to American revenue. Delta uses its own $35,731M. Domestic geographic passenger revenue is not an independently reconciled statutory taxable-fare base; United's US-and-Canada operating revenue is not substituted for US-only passenger revenue.
- **Global fuel scope:** the oil shock now uses reported worldwide gallons for Delta (4,269M), American (4,488M), United (4,663M) and Southwest (2,169M), including regional operations where disclosed. The US carbon-tax exposure stays separately scoped. Brent-to-refined-fuel transmission and customer recovery remain unverified. Other carriers retain the existing proxy and its geographic limits.
- **Policy mechanics:** remove outdated single-company/six-company descriptions; distinguish hypothetical bag-fee and ACP changes from current law; exclude nondepreciable land from the CHIPS qualifying-property explanation; clarify education's repeated-failure requirement and effective-date distinctions. Historical MA payment-increase pass-through is explicitly an uncertain extrapolation for current insurer payment cuts.

## Measurement limits retained

Southwest began broad baggage charges during 2025, so its historical total is not annualized into an invented steady-state figure. BTS carrier reporting and consolidated regional-company perimeters can differ. Fixed measurement bounds describe historical observations, not future certainty.

Altria's revenue/gross-profit reconciliation includes excise tax. Centene separately reports premium-tax revenue and expense. Neither is automatically changed using TTEK's correction; their demand-margin definitions require separate reconciliation. Insurer segment revenue can include member premiums, Part D or supplemental products and must not automatically become pure CMS Part C exposure.

The archived `before.json` and `backtests_before.json` preserve this round's starting point. Source observations are in `../evidence/verified_round2_parameters.json`, the unchanged official workbook and its quarterly transcription. Regression checks independently pin the statement arithmetic, fee units, each carrier's fee amount and global fuel quantity. Full audit reports continue to disclose missing company benchmarks, transmission coefficients, legal detail and valuation timing.

# Coverage gaps

Default-case coverage requires nonzero EPS or equity value, including explicit unpriced direct-value channels. Revenue-only effects and unquantified exposures do not qualify.

| Item | Count |
|---|---:|
| Companies | 234 |
| Default covered | 229 |
| Gaps | 5 |
| Explicit company-policy decisions | 1694 |

## Unresolved rule failures

- **BLK**: Asset management is not principal trading. Domestic pretax source excludes noncontrolling interests, while the engine apportions minority income separately; reconciliation pending. No guessed investment-rate sensitivity.
- **LYFT**: Reported US pretax loss; positive-income tax channel does not bind. Net repurchase excise tax is disclosed as immaterial, not a usable numeric base.
- **MDT**: Irish domicile: GAAP domestic income is not US income; 12.5% statutory-rate reconciliation confirms the jurisdiction distinction. US device-import sensitivity still needs a disclosed numeric base.
- **PGR**: No insured bank-assessment exposure; the insurer is not an FDIC bank. Exact US tax jurisdiction base not separately quantified in the current tax note.
- **SLM**: Education lender, not a tuition operator. Its insured bank subsidiary warrants a separately sourced assessment/NII policy in the education bucket; no Title IV tuition share invented.

These are unresolved coverage failures, not assertions that the firms have no economic policy exposure. They are deliberately not filled with copied peer priors.

## New policies

Six industry-specific `us_corporate_tax_<industry>` scenarios cover positive sourced US book pretax income under the submitted S.Amdt.2428 rate change (21% to 28%). Book income is a labeled taxable-income proxy, not a verified cash-tax forecast. Low/high values are historical income observations, not confidence intervals. All original policy IDs remain stable.

- `consumer_retail/us_corporate_tax_consumer_retail`: WMT, COST, AMZN, NKE, HD, DLTR, TJX, SBUX, MCD, KO, PEP, PG, CL, BBY, MDLZ, MO, PFGC, PM, SYY, TSN
- `education/us_corporate_tax_education`: LRN, CVSA, DUOL, PRDO, LAUR, LINC, WLY, FC
- `financial_services/us_corporate_tax_financial_services`: JPM, WFC, GS, BNY, USB, PNC, COF, FITB, HBAN, ALLY, MA, AIG, PRU, ALL, MET, SNEX, SPGI, TRV, V, PYPL
- `healthcare/us_corporate_tax_healthcare`: UNH, ELV, HUM, CVS, PFE, MOH, JNJ, AMGN, GILD, THC, TMO, ABT, CAH, COR, ISRG, MCK
- `tmt/us_corporate_tax_tmt`: MSFT, GOOGL, META, NVDA, VZ, CRM, ADBE, AMD, QCOM, MU, CSCO, T, CMCSA, NFLX, DIS, AMAT, ANET, DELL, HPQ, INTU, LRCX, NOW, PANW, SNDK, SNX, TMUS, TXN, PLTR
- `transportation_logistics/us_corporate_tax_transportation_logistics`: UPS, FDX, TSLA, CHRW, UBER

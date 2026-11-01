# Coverage gaps

Default-case coverage requires nonzero EPS or equity value, including explicit unpriced direct-value channels. Revenue-only effects and unquantified exposures do not qualify.

| Item | Count |
|---|---:|
| Companies | 234 |
| Default covered | 233 |
| Gaps | 1 |
| Explicit company-policy decisions | 1744 |

## Unresolved rule failures

- **LYFT**: Reported US pretax loss; positive-income tax channel does not bind. Net repurchase excise tax is disclosed as immaterial, not a usable numeric base.

These are unresolved coverage failures, not assertions that the firms have no economic policy exposure. They are deliberately not filled with copied peer priors.

Round 3 (see `reports/AUDIT_ROUND3.md`) closed the BLK, PGR, SLM and MDT gaps: the corporate-tax proxy now covers untagged US issuers via their reviewed US share, the rate policy reaches insurer portfolios, borrowing caps credit private lenders, and a medical-device tariff policy covers device importers. Companies covered only by a corporate-tax scenario are listed in `reports/audit_matrix/summary.json`.

## New policies

Six industry-specific `us_corporate_tax_<industry>` scenarios cover positive sourced US book pretax income under the submitted S.Amdt.2428 rate change (21% to 28%). Book income is a labeled taxable-income proxy, not a verified cash-tax forecast. Low/high values are historical income observations, not confidence intervals. All original policy IDs remain stable.

- `consumer_retail/us_corporate_tax_consumer_retail`: WMT, TGT, COST, AMZN, NKE, HD, LOW, KR, DG, DLTR, TJX, ROST, SBUX, MCD, KO, PEP, PG, CL, ULTA, BBY, MDLZ, MO, PFGC, PM, SYY, TSN
- `education/us_corporate_tax_education`: LRN, LOPE, CVSA, STRA, DUOL, UTI, PRDO, APEI, LAUR, LINC, SCHL, BFAM, WLY, FC, SLM
- `financial_services/us_corporate_tax_financial_services`: JPM, BAC, WFC, GS, C, AXP, MS, SCHW, BNY, STT, USB, PNC, TFC, COF, FITB, HBAN, KEY, ALLY, MA, BLK, AIG, PRU, PGR, ALL, MET, SNEX, SPGI, TRV, V, PYPL
- `healthcare/us_corporate_tax_healthcare`: UNH, ELV, HUM, CVS, PFE, LLY, CI, MOH, JNJ, AMGN, GILD, HCA, THC, UHS, TMO, ABT, CAH, COR, ISRG, MCK
- `tmt/us_corporate_tax_tmt`: AAPL, MSFT, GOOGL, META, NVDA, VZ, ORCL, CRM, ADBE, AMD, QCOM, MU, AVGO, CSCO, T, CMCSA, NFLX, DIS, AMAT, ANET, DELL, HPQ, INTU, LRCX, NOW, PANW, SNDK, SNX, TMUS, TXN, PLTR
- `transportation_logistics/us_corporate_tax_transportation_logistics`: UPS, FDX, UNP, DAL, TSLA, GM, CHRW, JBHT, ODFL, XPO, SAIA, CSX, NSC, UAL, AAL, LUV, UBER

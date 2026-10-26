# Company coverage review — 25 October 2026

This is an internal review of modeled activity coverage and accounting, not independent third-party assurance or a guarantee of forecasting accuracy. It covers all 203 configured companies in their industry policy menus: 66 industry policies, 1,338 valid policy/company decisions, plus all 10 market-wide shocks over the 203-company sample. It does not claim that every industry policy has been implemented as a cross-industry spillover model for all 203 firms.

## Findings corrected

- **FDIC assessments:** AIG's insurance premiums do not create an FDIC-insured bank assessment base. AIG, PRU, PGR, BLK and MA remain outside this bank-expense channel, with an explicit explanation. Insured subsidiaries at bank holding companies are included. The channel also requires the bank statement kind.
- **Bank base magnitudes:** Revenue-scaled peer estimates were inappropriate for insured bank balance sheets. Replaced all 18 bank-company bases using 21 identified subsidiary reports from the free FDIC BankFind API, dated 30 June 2026. Capital One's previous $1,097,207M estimate exceeded its FY2025 consolidated assets; the new subsidiary assets-less-Tier-1 proxy is $594,681M. Subsidiary certificates and parent names are validated. Quarter-end rather than quarterly-average balances, selected-entity mapping completeness and custody deductions remain explicitly estimated; these are not actual assessment invoices.
- **Uncertainty endpoints:** Excluded companies cannot receive a hidden effect merely because a high exposure bound was inherited from a peer. Corrected inappropriate bounds in card late fees, ACA premiums, mineral production, defense procurement, property taxes, tourism/office-linked spending and telecom China exposure.
- **Medicaid:** Removed capitated-enrollment exposure inherited by drugmakers. Plan premiums and separately estimated hospital patient volume remain modeled; prescription demand/rebates require a different channel.
- **Government contracts:** Removed consulting/IT allocations copied onto unrelated defense manufacturers; narrowed IT shares for mixed suppliers. A weapon, vehicle or nuclear-component purchase is not a management consulting task order. Fixed-price conversion now changes operating cost/profit at constant revenue, rather than reporting the margin change as sales.
- **Oil:** The SPR scenario holds stand-alone refining margins constant and no longer transfers upstream earnings sensitivity to refiners or service orders. FCX's explicitly signed diesel proxy changes operating cost rather than mineral sales revenue, in both SPR and broad oil-price scenarios.
- **Hospitality:** Hotel owners HST, RLJ and PK now have an explicit, uncertain attendance-linked demand estimate instead of inheriting zero from unrelated property REITs.
- **Education/geography:** Laureate's Mexico/Peru operations and Sallie Mae's private lending revenue are not allocated US household tuition purchases. ESA lender exposure is excluded; unquantified potential education-provider/materials participation is disclosed separately.
- **Technology:** Cisco no longer inherits a US telecom provider's zero China base. Its 2% Greater China share (0–5% range) is an explicit scenario estimate within the reported APJC segment, not a disclosed China split. The semiconductor tariff already explicitly includes imported electronics and hardware, so its wider device/server cost coverage is intentional and remains estimated.

## Regression evidence

The coverage matrix is authored separately from calculations in `config/policy_company_coverage.yaml`; the audit never generates expected memberships by copying its own affected-company outputs. Current classification counts: 799 included decisions, 514 outside the selected channel, one nonbinding across the selectable range, and 24 unquantified central exposures. These counts describe model coverage, not legal eligibility or forecast accuracy.

Included firms must show the economically expected default direction (or an explicitly reviewed nonbinding default) and a nonzero effect at at least one tested input. Excluded firms must remain neutral at defaults, every tested input boundary and every uncertain-driver endpoint. Unquantified central exposures can have an explicitly estimated high sensitivity case. Raw valuation channels are checked even when market price/P/E is unavailable.

Mutation regressions demonstrate detection of a missing effect at Ally, a false assessment at AIG and a missing result company. The normal test suite also checks distinct API explanations for nonbinding fees/wages, zero shocks, missing estimates and valuation-only effects.

- **Committed-data audit:** 249 industry input cases; 380 industry uncertainty endpoints; 42 macro input cases; 174 macro uncertainty endpoints; zero failures. Company-oriented industry ranges also checked.
- **Running local app:** all 66 policies and 249 input cases passed with the current live capture and the complete reviewed company roster.
- **Python:** 506 passed, 5 skipped. Six existing smoke-test review warnings remain for large percentage changes at thin earnings baselines (KR, BBY, RLJ and AAL scenarios); they are not silently clipped or labeled proof of accuracy.
- **Frontend:** 13 tests passed; production build passed. Browser verification confirms AIG's scope label/explanation and the updated Capital One exposure.

Machine-readable evidence: `design/reviews/policy-audit.json`, `design/reviews/policy-company-coverage.csv` and `design/reviews/live-policy-smoke.json`.

## Sources and limits

- [FDIC assessment methodology](https://www.fdic.gov/resources/deposit-insurance/deposit-insurance-fund/dif-assessments.html): insured-bank assessments, average assets less tangible equity.
- [FDIC BankFind API documentation](https://api.fdic.gov/banks/docs): keyless public bank financials; source requests and original records are retained in `data/snapshots/fdic_assessment_bases.json`.
- [FDIC assessment-base rule](https://www.fdic.gov/resources/regulations/federal-register-publications/2010/10finaldec20.pdf): Tier 1 capital and special institution adjustments.
- [AIG 2025 annual filing](https://www.sec.gov/Archives/edgar/data/5272/000000527226000023/aig-20251231.htm): current insurance business context.
- [Capital One 2025 annual filing](https://www.sec.gov/Archives/edgar/data/927628/000092762826000024/cof-20251231.htm): consolidated balance sheet and Discover/CONA merger.
- [Laureate FY2025 geographic segments](https://www.sec.gov/Archives/edgar/data/912766/000162828026009479/R17.htm): Mexico and Peru continuing operations.
- [Host Hotels FY2025 business mix](https://ir.hosthotels.com/news-releases/news-release-details/host-hotels-resorts-inc-reports-results-2025): hotel customer/business mix; attendance elasticity and the estimated exposure are not reported by the issuer.
- [Cisco FY2025 annual report](https://www.cisco.com/c/dam/en_us/about/annual-report/2025-cisco-full-annual-report.pdf): APJC geography; the Greater China subset remains an estimate.

Every policy's existing references and exposure provenance remain in the detailed audit. Broad assumptions, income-statement templates, linear responses, shared peer priors, future legal eligibility, business divestitures, timing and indirect feedback can still change the real outcome. An excluded modeled channel is not a claim that a firm has no possible economic exposure to the policy. No paid APIs, runtime LLM calls or new dependencies were added.

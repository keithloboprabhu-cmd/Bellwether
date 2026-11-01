# Audit round 3 — financial, economic and numerical credibility (1 November 2026)

Starting point: the 234-company universe (original 60 + 143 expansion + 31 audit additions), 72 industry
policies and 10 macro shocks at commit `ed9123d`. End state: 74 industry policies, 1,744 own-industry
policy × company pairs, every one in the matrix.

## Method

1. **Matrix** — `scripts/audit_matrix.py` runs every policy on every company in its industry at defaults,
   each numeric input's min and max, the all-zero shock, and a five-point sweep, and writes
   `reports/audit_matrix/matrix.csv` (one row per pair: coverage status, exposure basis, ΔEPS %,
   Δprice %, ΔNI, flags) and `summary.json`.
2. **Flags** — zero shock not zero, non-monotone response, |ΔEPS| > 100 %, |Δprice| > 50 %, declared
   `included` but never affected, `outside_scope` but affected, unquantified gap.
3. **Exposure basis** — each pair is labeled by its weakest nonzero exposure: `sourced` (filing or
   statute), `company_estimate` (explained, company-specific), `peer_prior` (a value copied from a
   different company, rationale "Explicit modeling prior"), `scope_zero`, or `gap`.
4. **Fixes** — traced every flag and every large peer-prior result to its channel and exposure; corrected
   data first, added channels or policies only where no existing policy fit.
5. **Validation** — targeted regression tests (`tests/test_audit_round3.py`), the full suite, the
   generated policy audit (`scripts/audit_policies.py`) and a headless render of every Streamlit page.

## Coverage checklist (before → after)

| Item | Before | After |
|---|---:|---:|
| Policy × company pairs | 1,694 | 1,744 |
| Included (modeled channel) | 897 | 978 |
| Unquantified (explicit gap) | 282 | 210 |
| Outside scope (reviewed boundary) | 514 | 554 |
| Companies with no effect from any industry-specific policy | 44 | 16 |
| Companies with no default EPS/value effect at all | 5 | 1 (LYFT) |
| Pairs with effects resting on a peer prior | 440 | 382 |
| Zero-shock violations / unexplained non-monotone responses | 0 / 0 | 0 / 0 |

## Changes

**Double counting and sign errors (engine/config)**
- *Tariffs counted twice.* FY2025/26 baselines already contain most 2025 tariff costs (GM's 10-K: about
  $3.1B in 2025), yet consumer and auto tariff inputs were levels measured from zero. Both inputs are now
  *additional* duty above the baseline (default +10 points, negative = rollback); macro tariff help text
  says the same. Steel already used this framing; pharma and semiconductor tariffs were largely absent
  from 2025 baselines and are unchanged.
- *Tax gain on losses.* The `tax_rate` channel applied a rate increase to negative pretax income, so a
  loss-maker gained earnings from a tax increase (CLF: +$71M). A baseline pretax loss now gets no
  current-tax effect, in both the industrials policy and the Full Market tax shock.

**Corporate-tax coverage**
- The book-income proxy for the six `us_corporate_tax_<industry>` policies now covers 42 more issuers:
  4 tagged domestic income, 4 total minus tagged foreign income (AAPL, C, TGT, UHS), and 34
  total × the reviewed US share already used by the Full Market shock (labeled estimates).
  14 stay explicit gaps: a latest-year US or total loss (MRK, ABBV, IBM, INTC, F, RIVN, CNC, LYFT, COUR,
  NRDY, SKIL, CHGG, KLC) or non-US incorporation (MDT).
- The 31 audit additions had a zero sentinel for the Full Market US pretax share; they now use their
  10-K domestic/foreign split. STRA and SCHL no longer default to 100 % US.

**Peer priors replaced with company-specific values** (`company_exposure_overrides.yaml`, applied by
`scripts/apply_round3_audit.py`)
- Chips: QCOM, AMD, INTC carried NVIDIA's 9.1 % China share (QCOM's is about 45 %, INTC's about 28 %);
  QCOM, a fabless seller to Asian assemblers, carried NVIDIA's 45 % US-import share (now 5 %).
  LRCX China share from its FY2026 10-K (33.8 %); AMAT and TXN added.
- Consumer: KR, DG, SBUX import shares came from WMT/COST/TGT (KR's −272 % tariff result came from this);
  PEP, KO, PG carried a 70 % US-consumer share.
- Public sector: nine contractors were exact copies of General Dynamics and three of a BAH/CACI median
  (ICF, a mostly civilian contractor, had a 71 % defense share). Government, defense and civilian
  shares replaced for LMT, NOC, RTX, HII, OSK, KTOS, AVAV, BWXT, TXT, MRCY, VSEC, KBR, ICFI, TTEK.
- Others: LUV domestic passenger share (Delta's 56 % → 93 %), TMO/ABT/MDT device import shares (copied
  from Pfizer), GEV (all sentinels), TMUS, INTU, ANET.

**New channels and policies (data only, no engine code)**
- `fed_rate_change` (industry and macro): an investment-income channel for insurers and Visa
  (net investment income from 10-K XBRL × an estimated first-year repricing sensitivity). Banks keep
  only their 10-K NII tables, so nothing is counted twice.
- `student_loan_borrowing_caps`: Sallie Mae gains the graduate borrowing that leaves Grad PLUS (it was
  marked outside scope, i.e. the opposite sign of reality was replaced by zero).
- New `consumer_retail/tobacco_excise_increase` (MO segment revenue from its 10-K; PM via oral nicotine).
- New `healthcare/medical_device_tariffs` (TMO, ABT, MDT, ISRG, CAH, COR, MCK; drugmakers stay with the
  pharma tariff policy, J&J excluded because its device and drug imports are not separable).

## Validation results (verified)

- `pytest`: 646 passed, 5 skipped (network-dependent), 0 failed; 13 new regression tests cover the tariff
  increment, the loss rule, the tax-proxy tiers, the replaced priors, the new channels and policies,
  a coverage guard and an app-wide monotonicity sweep over every numeric input (7 points).
- `scripts/audit_policies.py`: 74 policies, 10 macro shocks, 0 failures (`design/reviews/POLICY_AUDIT.md`).
- Engine invariants unchanged and tested: zero shock → exactly zero, tax applied once in aggregation,
  NI and value attribution reconcile for every pair and endpoint.
- Every Streamlit page renders headlessly without exceptions; API smoke tests return the expected signs.

## Remaining flags (reviewed, not errors)

| Pair | Default result | Why it stands |
|---|---|---|
| AAL × carbon tax, bag-fee cap, ticket tax | −594 %, −239 %, −142 % EPS | 2025 pretax income was $190M on $54.6B revenue; small dollar effects are huge percentages. Price is n/m. |
| RLJ × property tax | −613 % EPS | Near-zero EPS base; property tax is a peer prior scaled by revenue. |
| HUM × MA rate −2 % | −63 % | MA is about three-quarters of revenue and the pretax margin is 1.1 %. |
| BBY × import tariff +10 pts | −56 % | 3.3 % EBIT margin with the policy-wide 60 % pass-through. |
| LUV × carbon tax | −86 % | Thin 2025 margin. |
| TFC × fed rate | non-monotone | Verified: 2025 10-K Table 30 shows NII falling at both +50 and −50bp. |

## Remaining limitations (not validated)

- **No live primary-source access this session.** SEC EDGAR, FRED, NBER and the New York Fed were blocked
  by the environment's network policy, so no new filing could be fetched. New primary values come only
  from committed 10-K XBRL facts (`reports/evidence/filings.json`) and the committed EDGAR snapshot. All
  other new values are labeled `source: estimate` with a company-specific rationale and range drawn from
  general knowledge of issuer disclosures; **they need checking against the filings** before being
  treated as verified.
- **382 of 978 nonzero pairs still rest at least partly on a peer prior** (industrials 77, consumer 54,
  real estate 42, energy 37, education 36, TMT 34, financials 32, public sector 31, transport 24,
  healthcare 15). They are labeled in the matrix, not verified.
- **Coverage gaps.** 16 companies have no industry-specific effect: BLK, MA, PYPL, SNEX, SPGI (no fitting
  policy or unsourced rate sensitivity), CHRW, UBER, LYFT (no freight-brokerage or gig-labor policy),
  LAUR (non-US operations), NOW, PANW, PLTR, SNDK, SNX (exposures unsourced), DELL, HPQ (see below).
  All but LYFT are covered by the corporate-tax scenario. 210 pairs remain explicit `unquantified` gaps.
- **Thin-margin OEMs.** DELL and HPQ were left unquantified for chip tariffs: the policy's single
  pass-through range would produce about −70 % to −80 % EPS, a number driven by the assumption rather
  than the company.
- **Roster.** Not changed (adding issuers needs an EDGAR baseline build). Material omissions for the
  existing policies: CME, ICE, NDAQ (financial transaction tax), BMY (Medicare negotiation: Eliquis),
  SYK, BSX (device tariffs), KMI or other pipelines (methane fee). AIG, PRU and PGR are insurers typed
  `standard`; AIG and PRU use a derived generic cost base and should be re-baselined with `kind: insurer`.
- **Industry revenue totals** add retailer and manufacturer revenue for the same consumer dollar (e.g. a
  rebate lifts WMT and PEP). Profit totals are value added along the chain and are not double counted;
  revenue totals are.

## Assumptions requiring judgment

- **Persistence of absorbed tariff costs.** Retailers' absorbed share of a tariff is valued as permanent
  at the current P/E. Long-run pass-through of an industry-wide cost shock is usually near complete,
  while 2025 retail evidence shows slow, partial pass-through (Cavallo, Llamas & Vazquez, NBER w34496:
  about 20–24 % within months). Valuing the absorbed share over a few years instead would cut retailer
  price effects sharply; it should be decided once for all cost policies.
- **Consumer tariff magnitude.** Even at +10 points, WMT −27 % and TGT −44 % EPS are well above what
  retailers reported through the 2025 tariff increases. Likely reasons: customs value is below retail
  cost of goods, suppliers absorb part, and sourcing shifts. None of these is modeled.
- **Insurer rate sensitivity** (P&C 5.5–9 %, life 1.5 % of investment income per 100bp) and **Sallie Mae's
  steady-state gain** (10 % of revenue at full uptake, range 4–25 %) are structural estimates with wide
  ranges.
- **Tobacco**: elasticity −0.4 and full pass-through; manufacturers' own price increases are excluded.
- **Medical devices**: 40 % first-year pass-through (multi-year hospital contracts); import shares are estimates.

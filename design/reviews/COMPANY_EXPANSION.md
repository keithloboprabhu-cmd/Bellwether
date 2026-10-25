# Company coverage and user-company review

This supersedes the original 60-company design checkpoint for company coverage and
company mode. The user requested 20–30 diverse companies in every industry plus
API lookup and manual company modeling. The existing Python engine remains the
calculation authority.

## Delivered

- 203 configured issuers: 20 in nine industries, 23 in Financial Services. The
  added roster, actual SEC CIKs, annual filing URLs and sampling strata are recorded
  in `data/snapshots/sample_coverage.json`. All configured issuers have annual
  baselines and a public price snapshot. GDP beta fits were rebuilt for the sample.
- Added software, telecom, media, chips; regional banks, custody, payments,
  insurance and asset management; retail formats/staples/restaurants; managed care,
  pharma, hospitals/devices; industrial machinery and steel; oil, utilities,
  refining and pipelines; freight, rail, aviation, auto and mobility; defense and
  government services; varied REIT property types; education institutions,
  training, publishing, childcare and student finance.
- Financials are API-sourced. New policy exposures are separate, labeled peer
  estimates with a rationale. They are not issuer disclosures. Bank-only mechanisms
  exclude non-bank templates; no direct hospital payment-loss mechanism was added.
- Native modal company editor: SEC directory search, public-company lookup outside
  the roster, manual financials, explicit exposure entry/peer estimates, applicable
  flags, JSON profile import/export, validation and draft retention.
- Company scenarios use the same engine with a P&L bridge, EPS/range, channel
  attribution and sensitivity. Industry peers remain a separate reference sample.
  Custom financials stay out of share URLs and are included in company CSV exports.
- Twenty-plus company landscapes and charts use local scrolling and readable labels.
  Custom companies have a square marker and an explicit table label.

## Evidence and checks

- Full Python suite: **375 passed, 6 skipped**, with six smoke-test review warnings
  for large default effects (KR/BBY import tariffs, RLJ property tax, AAL aviation
  policies). Estimates are not capped to make those outputs look plausible. Thin
  earnings, policy scope and peer priors require interpretation.
- Frontend: TypeScript + production build passed; **9 renderer/format/CSV tests
  passed**. No new dependency was added for company functionality.
- Automated AccessLint scans: no detected violations on the rendered landing and
  expanded TMT result. The result scan caught a visible/accessibility-name mismatch
  for unavailable EPS; it was fixed and the scan rerun successfully. These are
  focused automated checks, not a WCAG conformance certification.
- Browser: SEC search found ADSK outside the configured sample. Lookup populated
  Autodesk FY2026 revenue, costs, EPS, shares and the actual annual filing link.
  Policy exposures remained blank until explicitly selecting peer estimates. The
  company scenario completed alongside 20 reference companies.
- Browser manual profile: explicitly illustrative inputs (revenue $1,000M,
  operating income $100M, interest $10M, pretax $90M, tax 21%, NI $71.1M,
  diluted shares 10M) produced a company result/range and missing-price valuation.
  An inconsistent pretax input was rejected; the draft and prior result remained.
- Browser keyboard/native dialog: background content became inert, validation error
  received focus, Escape closed the editor and focus returned to its trigger.
  Checked the editor at 390 × 844 and desktop dimensions; its Run action remained
  reachable. Screenshot evidence: `company-lookup-desktop.png` and
  `company-mobile-validation.png` (local review captures, ignored by Git).
- Profile schema JSON round-trip, required exposures, invalid/NaN/boolean inputs,
  unsafe source URLs, zero shock, nonpositive EPS and missing price are tested.
  Native file-picker interactions were not automated in this review.
- SEC share tagging quirks for MCD and LINC were normalized using documented filing
  units and filing-date cutoffs. Correct older facts retain their original units;
  regression tests cover both periods. Unknown issuer unit conflicts remain blank
  for manual review rather than being silently rescaled.

## Limits

This is a curated teaching sample, not a statistically representative index. The
SEC API does not expose every policy exposure, private-company financials or every
foreign reporting format. Supported US-GAAP annual 10-K issuers can be fetched;
missing fields and unsupported companies use manual input. Peer estimates are
starting assumptions and require review. The bank-only policies do not imply that
non-bank financial firms are economically unaffected.

Full Market web UI, broadly editable policy assumptions, publication math styling,
and comprehensive assistive-technology/performance checks remain separate work from
the earlier brief. The existing Streamlit interface remains available.

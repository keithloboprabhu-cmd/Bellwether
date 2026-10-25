# The Instrument — design contract for review

Source: `UI_SPEC.md`, the user's supplied interface brief. No `SPEC.md` or
`design/inspo/` was present. The user instructed us to use the attached file.
The installed Anti UI Slop and UI UX Pro Max instructions were read. Anti Slop
was applied during implementation and final review without changing preferences.
External design-generation services were not used. Generic marketing-section,
font-CDN, animation and palette recommendations were rejected where they conflict
with the brief.

## Task and composition

The student starts with one runnable sentence: industry, policy, primary value.
Options, defaults, bounds, steps and units come from validated YAML. Secondary
inputs use their configured defaults, disclosed next to the form and in Assumptions.
Industry changes announce their policy/value reset. Run remains explicit at this
checkpoint. A result continues to identify its applied scenario while inputs change.

The Field provides the pattern; the readout provides the headline and range; the
Companies table provides exact comparisons. Gold identifies actions and selection.
Green/red identify modeled increases/decreases, supplemented by signs and patterns.
Zero is labeled No change; undefined values use an em dash and never get bumps.
Relative long/short comparisons retain the engine ranking and explain one-sided
outcomes. The three secondary KPIs use revenue, margin and market value only.

## Shared system

- `web/src/tokens.css`: a single semantic system for colors, space, type, focus,
  radii and motion. No framework theme or external CDN.
- Locally hosted Source Sans 3 at 400/600 and Source Code Pro at 400; two font files,
  with swap. Assets come from the installed Streamlit distribution. Adobe's official
  SIL Open Font License files are included alongside them.
- Native selects/numeric inputs and buttons target 48px. The primary task has one
  filled action. Tables use semantic headers and numeric alignment.
- Desktop uses a flexible 55/45 composition. Below 1100px, DOM and visual order are
  controls, headline/range, Field, relative comparisons, then the same three tabs.
- Charts stay independent of the terrain. Small screens scroll a labeled chart/table
  region rather than shrinking the data labels below their specified size.
- The Field is static at rest. No ambient effects, particles, global noise,
  command palette, decorative telemetry or additional motion system.

## Checkpoint boundary

This is U1 for design approval, with some real engine connection completed early to
avoid fake presentation values. It is not the final product handoff. Remaining work
includes Full Market UI/drill-down, editable
assumptions/exposures, tornado and transmission graphics, glossary/formula treatment,
auto-rerun, complete error/empty/partial-data states and final responsive/AT/device
and performance evaluation. Existing secondary-page content is available in a basic
shared shell; it still needs the later typography and formula pass.

Keep the supplied milestone sequence and Nov 3 deadline. Do not introduce excluded
ornament to fill space. Approval of this checkpoint commits the composition and
tokens, not unfinished product claims.


## Company coverage amendment

The subsequent user request authorizes 20–30 companies per industry and the company
editor/P&L bridge. These are implemented; see `design/reviews/COMPANY_EXPANSION.md`.
The native modal provides public lookup or manual inputs, explicit peer priors,
source notes, validation, schema import/export and draft retention. New company
financials are never silently pooled into reference-industry totals.

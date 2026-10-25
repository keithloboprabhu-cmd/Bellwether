# UI/UX Build Prompt: PolicyShock — The Instrument

Read SPEC.md and this interface specification before planning or coding. Treat this document as UI_SPEC.md. Inspect the actual repository, existing routes, components, data contracts, and available reference images in design/inspo/. Do not claim to have inspected files or images that are missing.

Build a distinctive, usable economic scenario tool: dark surfaces, restrained gold, clear typography, and one meaningful visual signature—a dithered contour terrain called the Field. The interface should help someone understand a policy shock, inspect the assumptions, and compare affected companies. It must work as a product, including its less glamorous screens and states.

## 1. Source of truth and working process

Authority:
- SPEC.md governs the engine, financial definitions, data, required outputs, and modes.
- This document governs interface design and interactions. The exclusions in Section 2 apply throughout; do not reintroduce them through references or optional features.
- The supplied UI UX Pro Max and Anti Slop materials are supporting guidance. They do not replace this product's direction or override either specification. Their repository READMEs describe tools; do not pretend those descriptions are the complete installed skills.
- If SPEC.md and this document conflict, identify the conflict and recommend a resolution. Do not quietly change engine behavior or drop a required output.

Start in plan mode. Present a concise repository assessment, stack recommendation, screen/component map, requirement-to-screen mapping, build order, and material conflicts or missing inputs. Identify what is already implemented and can be reused. Wait for approval of this initial plan.

After plan approval, build semantic design tokens and /styleguide, plus representative landing and results layouts using an existing real scenario if available. Cover typography, spacing, controls, chart marks, focus, validation, and a Field sample. Clearly identify development fixtures; never present fixture values as calculated results. Obtain approval of this design checkpoint before building the remaining screens. Do not repeatedly request approval for routine implementation choices after these checkpoints.

Use installed ui-ux-pro-max and relevant antislop skills if available. Read their actual instructions. For Anti Slop, use during-build mode for this task, including the final review; do not change global preferences. Use design guidance for layout, accessibility, typography, charts, responsive behavior, and interaction states. Reject recommendations that would turn this application into a generic landing page or dashboard. If a skill is unavailable, apply this specification directly and state the limitation once. Do not install packages globally or stall the project to obtain an optional skill.

Implement the flat, readable version of each screen before texture or motion. Then add the Field, verify the complete interaction, inspect rendered screenshots, fix visible defects, and repeat. Code compiling successfully is only one check.

## 2. Product scope and visual restraint

Keep v1 focused:
- Before Run, show three scenario inputs: industry, policy, and value. The Run button and up to three working example chips complete the primary interaction. Navigation links remain available. Put company modeling and advanced assumptions in the results workspace.
- Keep three results tabs: Companies, Why, Assumptions. Every required SPEC.md output must have a named location within this structure.
- Use at most two font families, three weights overall, and gold plus the two semantic result colors.
- Use at most two simultaneous animations. The Field response is the only substantial animated event.
- Use one filled primary action per active task. When a modal task is active, its action is primary and the background is inert.

Do not build ambient particles, flow trails, ghost range terrain, a range-terrain toggle, a command palette, decorative rulers, isometric figures, fake activity indicators, waveforms, dials, or a separate second-round animation system. Second-round effects remain available if required by SPEC.md and use the ordinary update behavior.

Keep corner ticks confined to the Field frame and headline readout, and use them only if they improve the composition. Do not place every item in a box. Use alignment, space, and dividers for related information; reserve panels for actual grouping and containment.

There is one signature visual: the Field. The rest of the interface needs the same level of care through proportion, hierarchy, precise alignment, and useful states. Removing decoration must not leave an anonymous or unfinished wireframe.

## 3. Design direction and reference discipline

The Instrument is a calm financial instrument with a tactile, topographic surface. A policy changes the estimated earnings of industries or companies. Positive effects rise; negative effects form basins. A user sees the pattern, reads the headline, then investigates the cause.

Translate the supplied references selectively:
- HUD references: precise framing and clear readouts. Exclude futuristic theater and invented system telemetry.
- Warm accent on black: limited color and strong hierarchy. Exclude wireframe objects, neon, and glow stacks.
- Dithered mountain reference: ordered pixels and contour texture. Use it within the Field, not as a global noise filter.
- Dithered chart reference: consistent patterns and useful mark inspection. Keep exact values easy to read.
- Isometric reference: stroke restraint only. Do not import its figures or pointer-reactive ornament.

The landing page should look like the entrance to this particular tool. Do not add a marketing-section sequence, feature-card grid, testimonials, pricing, logo wall, trust badges, FAQ, or repeated calls to action. Use the existing POLICYSHOCK wordmark; do not invent a sparkle or AI logo.

For each screen, establish a clear focal point, a primary action, and an intentional reading order. The landing focal point is the runnable scenario sentence. The results focal point is the headline estimate, supported by the Field. Explain a significant visual choice by the task it serves, not with words such as premium, modern, or polished.

## 4. Design system

### Color and surfaces

Start with these tokens and validate their actual rendered contrast:

--bg: #050607
--plate: #0A0C0E
--line: rgba(255,255,255,0.14)
--line-strong: rgba(255,255,255,0.28)
--ink: #E9EEF2
--ink-dim: #8B96A0
--gold: #D4A84B
--gold-bright: #F0C766
--gold-dim: #8C7230
--gain: #3DDC84
--loss: #FF4D4D

Gold means brand, primary action, selection, and focus. Green means positive modeled effect; red means negative modeled effect. Gray means neutral or unavailable, with different labels for those two states. Zero is not missing data. Do not use gold to imply a gain.

Use a plus/minus sign and a pattern alongside result color: positive = stipple; negative = diagonal hatch; zero = a neutral mark labeled No change. Missing data uses an em dash and a plain explanation, never 0. Unknown does not get a simulated terrain bump.

Use --ink for essential content. Essential text must meet at least 4.5:1 contrast; aim for 7:1 on body copy. Controls, focus indicators, and meaningful graphics need sufficient contrast against adjacent surfaces, targeting 3:1. A decorative hairline may be subtle; a control boundary must remain identifiable. Do not use the original faint gray #56606A for text that users need to read.

Use solid plates under text wherever the Field would otherwise interfere. Standard panels have 1px borders and up to 2px radius. The Field frame may use approximately 12px. Avoid glass panels, gradients, generic deep shadows, and glow as a default interaction state. Any tonal vignette is confined to the Field renderer.

### Typography

Use a self-hosted sans for prose and a self-hosted mono for numeric readouts. Prefer Geist Sans plus Geist Mono, or use a suitable existing pair. Use mono selectively for numbers, units, and compact technical labels; prose should read comfortably. Use tabular numerals.

Use rem units. At the default root size: 13px minimum for nonessential labels; 15px for tables and secondary information; 17px for body text and inputs; approximately 24px for section headings. Scale the headline number responsively from about 48px on small screens to 80–96px on wide screens without clipping signs, units, or ranges. Prose line height is about 1.5; data about 1.3. Keep prose measure around 60–68 characters.

Use a maximum of three weights, for example sans 400/600 and mono 400. Keep font assets to four files or fewer, with font-display: swap and sensible fallbacks. Do not hardcode line breaks that work at only one width. Avoid uppercase paragraphs, excessively tracked labels, or repeated LABEL // headings. If used at all, the // motif is confined to the two signature surfaces; ordinary controls use plain labels.

### Spacing, controls, and layout

Define shared semantic tokens for surfaces, foregrounds, borders, focus, spacing, type, radii, and motion. Maintain one token system; update an existing system rather than layering a parallel theme over it. Do not scatter arbitrary hex values or one-off spacing throughout components.

Use a 4px spacing rhythm with 24–32px desktop panel padding and approximately 16–20px mobile padding. Use up to 1600px of desktop content width with responsive gutters. Give sections breathing room without creating empty viewport-sized gaps.

Inputs and primary buttons are approximately 48px high. Interactive targets are at least 44×44px. Align values, decimal precision, labels, and table headers deliberately. Keep action placement consistent across screens. Use one consistent SVG icon family if icons are necessary; pair unfamiliar icons with text. Never use emoji as controls or decoration.

Define default, hover, focus-visible, active, disabled, loading, success, and error states where applicable. Communicate disabled-state reasons nearby. No decorative control may look clickable. No visible control may be a no-op.

## 5. Core interaction: the Sentence Builder

The landing sentence is a small, real form:

What happens to [Healthcare] if [Medicare Advantage rates] change by [−3 %]? [Run scenario]

This is an example of grammar, not an instruction to hardcode this policy or fabricate its output. Read actual options, defaults, units, bounds, and steps from validated policy configuration.

- Industry and policy controls are clearly clickable tokens with persistent labels, selected values, and a disclosure indicator. Policy options have short useful descriptions.
- The value is a labeled numeric input. Typing and keyboard stepping are complete interaction paths. Drag scrubbing is an optional enhancement, never a requirement.
- Changing industry selects a compatible policy and valid default value. State the reset where it could surprise the user. Avoid intermediate runs with incompatible inputs.
- Units must be explicit and policy-specific: percent, percentage points, basis points, dollars, and absolute levels are different inputs. Show direction in the sentence; avoid accidental double negatives.
- Use existing sentence templates where available. If the engine schema lacks display text, use a UI adapter or propose an explicit backward-compatible schema change. Do not alter the engine schema silently for copy convenience.
- The initial sentence is runnable with one activation. Provide up to three example chips only for supported, working scenarios. An example fills the controls and runs its scenario.
- At 360px, stack sentence segments into labeled form rows with the same reading order. Do not shrink type to keep an artificial single line.
- Before the first result, Run is explicit. In results, committed valid edits may rerun automatically after a short debounce, about 250–400ms. Keep Run/Enter available for an immediate update. Do not rerun while an input contains a partial number, is invalid, or is undergoing text composition.
- Invalid values receive an inline explanation and a correction path. Do not silently clamp or substitute values. Unsupported combinations cannot produce a plausible-looking result.

Aim for a first-time user to obtain a meaningful result within three actions and 15 seconds from a loaded page. Validate this with an observed walkthrough if possible. Do not claim a timed usability test based only on your own automated clicks.

## 6. Screen structure and responsive behavior

### Landing

Show the wordmark, concise navigation to Backtests/Methodology/Data/About, one honest headline, the Sentence Builder, and up to three examples. Suggested headline: See how a policy could affect company earnings.

The landing Field is a low-contrast illustrative terrain. It must not imply that random terrain is a live market signal; label it Illustrative terrain if its appearance could be mistaken for a result. Keep it static while idle. Present the model's data-as-of date and Educational project. Not investment advice. unobtrusively.

Do not add an intro animation, splash screen, artificial loading delay, or onboarding tour.

### Results

Use a compact editable scenario header and a clear industry/company breadcrumb when drilling down. On desktop, place the Field beside the readout, with a shared full-width detail area beneath. Do not cram every chart into a narrow right column.

Prioritize these four elements in the initial desktop viewport at approximately 1366×768: the Field, headline estimate, long/short comparison, and detail-tab navigation. Keep essential context and uncertainty attached to the estimate. Treat this as a composition target, not permission to shrink text or clip content. On shorter or mobile viewports, preserve reading order and allow normal scrolling.

The readout includes:
- Metric name, signed base estimate, low–high scenario range, and one concrete verdict sentence. Explain EPS as earnings per share at first use.
- Long/short selections when supported by SPEC.md, each with name, estimated change, and one modeled reason. Label them as model-based comparisons, not guaranteed trading recommendations.
- Handle one-sided results honestly: if every company loses, the least affected company is not labeled a beneficiary. If the engine defines a relative long/short pair, state that basis. Follow SPEC.md; expose any conflict.

Place secondary KPIs below the main composition: revenue change, operating-margin change in bps, and implied market-value change. These are three metrics, not four. Do not invent another KPI to fill a grid.

Detail tabs:
- Companies: sortable company table and signed horizontal bars with low–high whiskers. In Company mode, include the required P&L bridge and peer comparison.
- Why: the model's explanation, key transmission channels, and assumption sensitivity/tornado chart. Lead with a concise explanation, then allow deeper detail; do not pad text to reach a word count.
- Assumptions: every assumption and exposure, base/low/high values, units, sources, and user edits marked User input. Put editing here, or in a drawer opened from the same source of truth; do not maintain duplicate editors.

Provide working Copy link and Export CSV actions in a consistent secondary-action area. Put Model a company here, outside the landing's three-input task. Keep secondary actions visually secondary.

On wide screens, use a flexible split, roughly 55/45, with tracks that can shrink. Never require a 620px right panel alongside a 55% Field. Stack when both sides cannot remain readable, usually near 1100px. On narrow screens: scenario controls, headline and range, compact Field, long/short, then detail tabs and content. Maintain the same three tab identities; do not unexpectedly change navigation into unrelated accordions.

### Full Market

Use the same workspace, with one node per configured industry. Derive counts from the dataset; if SPEC.md calls for 10 industries and a 60-company sample, validate those counts rather than faking missing entries.

Use the exact aggregation defined in SPEC.md. If it is a cap-weighted sample EPS-change metric, name it that way; do not silently present it as aggregate market EPS or an all-market forecast. Display sample coverage and weighting context near the headline.

Within the detail area provide the industry grid, top/bottom companies, long/short industry comparison, and transmission bars required by SPEC.md. Industry rows show signed revenue, margin, earnings, and value changes with explicit units. Clicking an industry drills into it; Back returns to the prior scenario and selection. Keep second-round effects in contextual controls, initially secondary to the headline.

### Company drawer

Use a modal drawer up to about 560px wide on desktop and full-width on mobile. Group identity, starting profile, financials, valuation method, and policy-specific exposures. Ticker is reference metadata unless SPEC.md defines a lookup.

Support peer/industry-median/blank starting points as specified. Show only relevant fields, preserving entered values when moving between sections. Mark user estimates and inherited values. Validate financial identities, units, required exposures, and unsupported valuation cases before Run.

Profile import/export must work with schema validation and useful errors. Closing with unsaved work offers a clear choice or preserves a draft. Use a square Field marker for a custom company and rings for reference companies.

### Secondary pages

Backtests, Methodology, Data, and About use the same typography and spacing, with no interactive Field. Do not pad these pages with decorative cards.
- Backtests: distinguish the model estimate, observed outcome, observation window, and confounding events. Render only actual available comparisons; absent validation is not fabricated success.
- Methodology: readable explanations, accessible rendered formulas, variable definitions, and limitations. Use mono for code, not as a substitute for typeset mathematics.
- Data: source links, as-of dates, coverage, and missing-data status in a useful table.
- About: purpose, scope, and attribution based on supplied facts.

## 7. The Field: distinctive and truthful

The Field is a lightweight Canvas 2D visualization with an equivalent accessible DOM table. It is not an image-generated background or a separate simulation engine.

Rendering:
- Use a low-resolution offscreen buffer with 4–6 CSS-pixel cells, a 4×4 Bayer ordered dither, and pixelated upscaling.
- Add about 14 marching-squares contour levels, with a restrained stronger index contour every fifth level. Keep gold-white contours quiet enough for semantic result marks to lead.
- Use a deterministic seed and stable anchors keyed to entity IDs. Sorting a table or changing the shock must not randomly rearrange nodes. These positions are not geography, similarity, or economic distance; say so in the legend.
- Keep landing texture separate from data geometry. Random base noise is not an earnings estimate. On results, do not let noise or neighboring bumps reverse sign, change relative heights at node centers, or imply a larger effect than the reported metric.

Encode signed EPS impact with a documented monotonic mapping, for example A = k × tanh(impact/s). Specify whether impact uses percentage units or decimal fractions and use one fixed scale for comparable views. Label any nonlinear scale. Never silently renormalize each scenario so a tiny change looks as large as a major shock.

At each node center, elevation relative to the displayed zero level must match that node's mapped impact. Zero impact produces zero deformation. Use localized basis functions with non-overlapping node cores, or another explicitly validated interpolation that preserves these constraints. Gold texture may supply visual character, but it must not alter the encoded node values. If accurate deformation is not ready, show the real table with a clear unavailable state instead of decorative pseudo-results.

Positive regions use green stipple; negative regions use red hatch; neutral terrain remains subdued. Label gain/loss as modeled increases/decreases, with signed values. Keep a visible legend explaining height, signs, patterns, and the arbitrary node layout. The Field is an overview; charts and the table provide exact comparisons.

For every node:
- Show a readable label on a solid label background; handle collisions with placement or leader lines rather than tiny text.
- Hover or keyboard focus reveals name, base estimate, low–high range, and implied price/value change only where mathematically defined.
- Tap selects and opens the same persistent readout; users must not need a second tap that accidentally navigates.
- Use an explicit drill-in action when touch selection would otherwise conflict with navigation. Support the same task from the table.
- Cross-highlight the corresponding table row and chart mark without reordering them or hiding the remaining data.

Missing values do not get zeros or fake bumps. Ranges that cross zero must remain visibly uncertain in the readout and charts. Do not call scenario bounds a confidence interval without a statistical basis. Do not show percentage price/EPS changes for undefined denominators; follow engine validity flags and explain the limitation.

## 8. Charts and exact numeric presentation

Use small shared SVG/canvas primitives; no heavy charting library or default dashboard theme. Keep the terrain renderer independent from chart rendering.

- Company bars diverge from a clear zero line, include signed end labels, and have low–high whiskers. Keep the scale comparable within a view. Use consistent stipple/hatch fills without making dither density the only readable measure.
- Tornado bars show result sensitivity to each assumption, sorted by effect span. Distinguish the assumption's low/high inputs from the resulting lower/higher outputs; they need not have the same order. Show actual source and low/base/high values on inspection.
- Transmission bars show signed components and a reconciled total. Do not imply a simple additive breakdown if the engine does not supply one.
- Full Market grid cells include actual numbers and units. On small screens, use a labeled scroll container or a readable row-detail view.
- Every chart has a concise title, unit, reference/zero where relevant, legend where needed, and a View as table control adjacent to it. Do not require finding a distant tab to access the equivalent data.
- Tooltips stay in the viewport and work with focus and touch. A pinned selection can be dismissed. Essential content is never tooltip-only.
- Tables use semantic headers, numeric alignment, stable sorting, an announced sort direction, and explicit empty/filtered states. Never truncate an essential company name, policy name, or result without an accessible way to reveal it.

Apply one shared formatter. Show percent versus percentage points versus bps correctly, currency and scale explicitly, and precision appropriate to the model. Normalize negative zero. A small nonzero value may use <0.1% rather than a misleading 0.0%. Never manufacture precision or invent a price target from an unsupported valuation assumption.

## 9. Complete interaction and application states

Implement and inspect initial, input editing, invalid, calculating, ready, empty, partial-data, error, and recovery states.

- A Run immediately acknowledges input and announces Calculating scenario. Do not delay a fast result for theatrical loading. If computation lasts long enough to need a visual indicator, use one restrained contour pulse plus text; never invent a completion percentage.
- When updating an existing result, preserve its layout and label it Updating. Keep the previous scenario visibly associated with those old values until the new result is committed.
- Use request IDs/cancellation where appropriate. Only the newest valid request can update the Field, headline, charts, URL, or CSV. Commit all of these from the same result snapshot.
- A failed update keeps the prior valid result identified as such, explains the failure, and provides a working retry. First-run failure shows an honest error instead of an attractive empty dashboard.
- Empty data, no affected companies, all-neutral outcomes, missing sources, and unsupported company metrics each have specific messages and useful next actions.
- Copy link confirms success and offers a manual-copy fallback if clipboard access fails. CSV exports the displayed scenario, units, as-of/version metadata, and user assumptions, with appropriate escaping.
- Share URLs preserve supported scenario state, user overrides, seed, and model/data version. Do not promise reproducibility unless versions can be resolved. An unavailable historical version gets an explicit explanation and a choice to rerun with current data.
- Parse and validate URL/profile input before use. Oversized custom profiles need a documented alternative; do not quietly truncate URL state. Warn that embedded company inputs become visible to anyone with the link.
- Reload, browser Back/Forward, direct links, and drill-down must preserve coherent state. Every navigation link must resolve to actual content.

## 10. Motion and feedback

Motion explains a completed state change; it does not impersonate computation.

Use approximately 120ms for small feedback, 200–240ms for panels, and at most 1.2 seconds for the initial terrain response. Once a valid result exists, a single ripple may reveal its deformation. Later edits use the same transition system, about 400–600ms. No typing effect, staggered parade of cards, looping idle animation, or animated waveform.

Prefer showing the correct headline value immediately. If a short numeric transition is retained, keep the accessible announcement and copied/exported value at the actual final result; never allow animated intermediate numbers to be mistaken for a model output. Uncertainty, labels, and controls remain available during motion.

Respect prefers-reduced-motion: static Field, instant numerical updates, no ripple or pulsing. Rapid changes cancel prior transitions and settle on the latest state. Pause rendering when hidden or offscreen. The settled results Field is static; rerender only for data, size, focus, or selection changes.

Keyboard: Tab/Shift+Tab follow visual order; Enter submits the form; Escape closes dismissible overlays. Arrow keys operate the selected native control. Optional shortcuts must not intercept typing or browser commands and must be discoverable. Do not add global single-character shortcuts by default.

## 11. Copy and anti-slop rules

Write for a student trying to understand a result. Use ordinary, specific language. Name the action, metric, mechanism, or limitation. Keep labels short and explanations complete enough to make a decision.

Reject:
- AI-powered, next-generation, unlock insights, seamless, revolutionary, supercharge, leverage, cutting-edge, and similar empty claims.
- Generic headlines such as The future of financial intelligence. Use a headline that says what the tool does.
- Fake users, testimonials, accuracy claims, benchmark numbers, uptime, live status, or market data. Label genuine as-of dates and stale snapshots accurately.
- Decorative code snippets, terminal output, unexplained acronyms, repeated // labels, filler badges, fake notifications, and buzzword explanations.
- Marketing prose in forms, error states, charts, or export messages. No emoji or exclamation points.

Prefer Run scenario, Copy link, Export CSV, Edit assumptions, and View as table to vague Explore or Learn more buttons. An error names the problem and recovery: Enter a value between [actual configured bounds]. Never leave the user with Something went wrong and no useful action.

Define jargon such as EPS, pass-through, elasticity, MPC, bps, CET1, and NII in a central glossary. Include first-use expansions and keyboard/touch-accessible definitions where appropriate. Do not underline every repeated term or turn paragraphs into a field of tooltips.

Verdicts must come from the model's actual mechanisms. Example structure, not fabricated output: Earnings decrease by [calculated result], mainly because [largest modeled channel]. State uncertainty briefly and accurately: Scenario range; excludes [actual omitted mechanism]. Do not substitute a generic disclaimer for an explanation.

Before retaining a nonessential UI element, identify the user task or data meaning it serves. If none exists, remove it. Then inspect the remaining screen: strengthen its composition through hierarchy, spacing, proportion, and the Field's execution rather than adding filler back.

## 12. Accessibility and responsive quality

Use semantic HTML and native controls where possible. Associate labels, hints, errors, and status text programmatically. Preserve visible focus and ensure sticky headers/footers never cover it.

Use dialog semantics and focus containment for modal drawers, returning focus to the opener on close. Menus/listboxes/popovers follow the appropriate keyboard pattern; do not trap focus in every popover indiscriminately. Implement tabs with correct selected state and keyboard behavior.

Provide an accessible DOM data equivalent for the Field and charts, including result summaries. Canvas hit regions alone are not accessible controls. Announce a concise final result in a polite live region; do not announce every animation frame or intermediate keystroke.

Test colorblind simulations and grayscale. Sign, pattern, and text must carry gain/loss meaning. Provide visible focus, sufficient contrast, comfortable targets, and no hover-only actions. Reduced motion and forced-colors modes must preserve controls and result meaning.

Check at 360, 390, 768, 1024, 1366/1440, and 1920px, with a 4K spot check. Check 125% and 200% desktop zoom and reflow around 320 CSS px. Long policy names, company names, negative values, large currencies, wrapped chips, translated-style long text, and user text-spacing overrides must remain usable. No page-level horizontal overflow. A wide table may scroll inside a clearly labeled region without hiding its identity column or essential context.

Do not disable browser zoom or solve overflow by hiding essential content. Mobile drawers need reachable close actions, safe-area padding, and validation messages visible above the software keyboard. Keep the primary task understandable on mobile rather than compressing the desktop composition.

If Canvas fails or is unavailable, keep the numerical result and table operational. An error in the decorative/visual layer must not take down the calculator.

## 13. Implementation and performance

Inspect the actual project before selecting tools. Preferred direction: Vite + React + TypeScript, CSS tokens, Canvas 2D for the Field, shared SVG/canvas chart primitives, and browser-based calculation if compatible with SPEC.md.

If SPEC.md assumes Streamlit, evaluate retaining Python with custom components versus porting the engine. Explain deployment/runtime tradeoffs and obtain the initial architectural approval before changing that requirement. Do not assume a port is trivial or rewrite working model logic just for visual convenience.

For an approved browser engine, validate policy/config schemas at build time and preserve Python as the numerical reference where supplied. Cross-check TypeScript/Python across supported policy/company combinations and edge cases, using documented tolerances and shared units. Keep data/config preparation outside the UI. Prefer existing deterministic explanation templates; do not add a runtime LLM service to generate verdicts.

Use an independently testable Field module with a small lifecycle API, for example createField, setNodes, setImpacts, setSelection, transitionTo, and destroy. Keep rendering, state serialization, numeric formatting, financial calculation, and presentation separate enough to test without inventing a general-purpose framework. Reuse accessible primitives already present. No paid service, heavy UI framework, external runtime CDN, or font CDN is required.

Performance targets, measured in a named environment:
- Landing first contentful paint below 2 seconds and controls usable within 3 seconds on a representative laptop; target Lighthouse performance 85 or above.
- Aim for initial application JavaScript around 300KB gzip or less, reporting fonts/data separately. Split noncritical pages and large data where useful; do not hide their download cost in reported totals.
- Field uses a DPR cap around 1.5, offscreen buffers, cached contours, and no unnecessary per-frame allocations or React state updates. Target renderer work below 8ms per active frame; reduce resolution or skip intermediate frames if necessary.
- Do not run a perpetual animation loop at rest. Keep input responsive during computation; move expensive work off the main thread if measurements justify it.
- Reserve space for charts, fonts, and result panels to avoid layout shifts. Clean up listeners, render loops, observers, and workers when unmounted.

Report measured results honestly. Do not report a performance target, visual review, or accessibility check as passed unless it was actually performed.

## 14. Build order and checkpoints

Keep the existing Nov 3 deadline from the project brief unless SPEC.md says otherwise. Use these milestones as sequencing targets, not permission to skip quality or fabricate completeness:

U1 — Oct 26: approved tokens/styleguide; flat landing and results compositions; real policy controls; static dither/contour Field.
U2 — Oct 28: engine-connected Field, headline, valid-state handling, long/short, Companies table and bars.
U3 — Oct 30: Full Market drill-down, Why/sensitivity, Assumptions, Company drawer, URL/CSV.
U4 — Nov 1: secondary pages, responsive/accessibility work, complete edge states, visual inspection and performance tuning. Do not add excluded ambient effects.
U5 — Nov 2: fresh-browser checks, phone checks, remaining defects, and recordings of three real showcase scenarios for the project PDF if that deliverable remains required.

If time is tight, simplify optional transitions and secondary-page ornament first. Preserve required calculations, the three-input flow, truthful encoding, readable data, keyboard/touch access, and usable error states. Flag any required feature that remains incomplete rather than hiding it behind a nonfunctional control.

## 15. Review gates and delivery evidence

Use actual rendered screenshots and browser interactions, not source-code inspection alone. Inspect every route in its normal and relevant empty/error states. Review desktop and mobile compositions at full size. Fix clipping, weak contrast, accidental wrapping, inconsistent spacing, misaligned values, label collisions, awkward blank areas, unclear controls, and broken focus order. Retest affected flows after fixes; do not run unrelated checks repeatedly without a reason.

Use meaningful automated checks for the model/UI contract, valid units and ranges, zero/positive/negative/missing impacts, stable monotonic Field anchors, asynchronous stale results, URL round-trips, exports, navigation, and keyboard-critical interactions. Use the existing test stack where possible. Lint/type checks and a production build are necessary but do not establish visual quality.

Before delivery, provide a concise pass/fail/not-tested report covering:

1. Task completion: one-click default run; all required outputs/modes; examples; edit/recalculate; drill-in/back; company profile; copy/share/export; source links; recovery.
2. Truthfulness and copy: no fake data or status; correct metric/units/precision; sample scope; scenario uncertainty; missing-data handling; no filler claims; Field geometry matches the model.
3. UI and accessibility: deliberate hierarchy; consistent tokens; all interaction states; readable desktop/mobile; keyboard/touch; contrast; grayscale; reduced motion; Canvas fallback; no inert controls.
4. Runtime quality: production build, relevant tests, measured performance, no browser-console errors in checked flows, deterministic state, cleanup, and no runtime CDN requirement.

Attach the screenshot locations and test/measurement commands with their observed outcomes. If a browser, device, source file, reference image, or measurement tool was unavailable, mark the associated checks Not tested and explain the practical consequence. Do not invent successful reviews or a numerical design-quality score.

Deliver the working implementation, a brief description of the user-visible behavior, validation evidence, and any remaining concrete limitations. The finished product should retain its distinctive terrain identity while making a real scenario easy to run, understand, inspect, and reproduce.
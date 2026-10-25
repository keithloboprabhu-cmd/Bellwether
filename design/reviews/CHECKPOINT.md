> Historical review of the first 60-company checkpoint. Current company coverage and
> company-mode validation are in [COMPANY_EXPANSION.md](COMPANY_EXPANSION.md).

# Instrument design checkpoint — October 24, 2026

This is the first design review requested in UI_SPEC §1, not a final product
completion claim. The user's attached file governs the interface; the existing
Python engine and METHODOLOGY govern numerical definitions.

## Review links and screenshots

Start the local preview using README.md, then open:

- Landing: `http://127.0.0.1:8787/`
- Styleguide: `http://127.0.0.1:8787/styleguide`
- Run the default Healthcare / Medicare Advantage scenario for the representative
  calculated result. At the configured −2% input, the engine returns −5.2% sample
  earnings change, with −9.7% to −1.7% scenario bounds.

Screenshots captured from the actual Codex in-app browser on macOS:

- `landing-desktop.png` — full landing at 1366px.
- `results-viewport.png` — initial result viewport at 1366×768.
- `results-desktop.png` — full result page with the real default scenario.
- `results-mobile.png` — result page at 360px.
- `results-positive.png` — actual +2% payment-rate scenario, with +5.2% earnings change.
- `styleguide-desktop.png` — typography, tokens, fixtures and controls.
- `results-{320,360,390,768,1024,1440,1920,3840}.png` — responsive captures during
  review; some predate the final compactness and selection-area refinements.
- `{backtests,methodology,data,about}-desktop.png` — actual connected secondary pages.

PNGs are local review artifacts and are ignored by Git. The landing/result/styleguide
compositions were visually inspected. Every listed secondary route loaded actual
content without an error alert; their final typography/formula and full visual
state review remain part of the later milestone.

## Pass / fail / not tested

| Area | Outcome and evidence |
| --- | --- |
| Task completion | **Pass within checkpoint scope:** default Run, real policy controls, calculated headline/range, Field, three tabs, company sorting, linked Field/table selection, keyboard tab arrows, Copy link confirmation, CSV download, reload and Back/Forward. **Incomplete for full v1:** Full Market UI/drill-down, company drawer/profile, editable assumptions/exposures, full sensitivity/transmission graphics and contextual components. |
| Truthfulness and copy | **Pass for checked cases:** Python reference equality; all 66 Industry default responses serialize without non-finite numbers and contain six companies; zero shock stays zero; positive/negative effects use signs and distinct patterns; fixed-scale Field preserves anchors and cannot overshoot node effects. Source rows come from configuration/snapshots. Styleguide values are labeled illustrative. **Not tested:** all missing-denominator and partial-data browser states, every policy's visual presentation, historic Streamlit-link migration. |
| UI and accessibility | **Pass for focused checks:** no page-level overflow measured at 320, 360, 390, 768, 1024, 1366, 1440, 1920 and 3840px; readable native form rows and mobile result order; visible keyboard focus; selected-state/sort semantics inspected. Final focused AccessLint scans found no automated violations on landing and the default result. **Not tested:** AT-user/screen-reader experience, real phone devices, grayscale/colorblind simulations, forced colors, preference emulation, 125%/200% browser zoom, full text-spacing overrides, injected Canvas failure and comprehensive error/empty states. |
| Runtime quality | **Pass for checkpoint:** TypeScript/production build; 11 Python adapter tests; 9 Node Field/formatter tests; zero errors returned by the in-app browser console-log inspection after checked flows. Rapid −3% then +2% submissions settled on the +2% applied scenario and +5.2% result. Locally hosted fonts/assets, no runtime CDN/LLM/paid services. **Not tested:** controlled delayed-response race injection, Lighthouse, FCP/control-ready timing, renderer frame budget and cleanup under repeated mounts. |

This is a focused automated accessibility scan, not a WCAG conformance audit.
Initial scans found an indistinguishable landing link, Field button accessible names
missing ticker text, and a missing results H1. These were corrected and rescanned.
The scan output supplied DOM selectors, not source-map locations. No numerical
design-quality score or observed human usability timing is claimed.

## Checks and observed outcomes

Environment: macOS workspace, Python 3.11.15, Node 26.5.0, npm 11.17.0, Vite 7.3.7;
visual interaction in the Codex in-app browser; AccessLint used its live-URL tool.

| Check | Observed outcome |
| --- | --- |
| `cd web && npm run build` | Passed TypeScript checking and production build. Latest emitted JS: 260.39 kB / 81.33 kB gzip; CSS: 21.75 kB / 5.06 kB gzip. |
| `cd web && npm test` | 9 passed: order-independent anchors, fixed monotonic scale, exact signed node-center heights, bounded interpolation, zero/missing distinction, explicit units and CSV escaping. |
| `.venv/bin/python -m pytest -q tests/test_instrument_api.py` | 11 passed: real engine equality, ranges, channel reconciliation, configured coverage/bounds, invalid/non-finite values, zero and version mismatch. |
| Default-response sweep | `calculate({industry, policy, inputs: policy.default_inputs()})` for every registry policy: all 66 passed finite JSON serialization and six-company coverage. |
| `.venv/bin/python -m pytest -q` — baseline run | **2 failed, 341 passed, 6 skipped.** Existing `test_narrative` cases for `education/ninety_ten_rule_change` and `transportation_logistics/auto_import_tariffs` returned 240 and 244 words against a 230-word maximum. The pre-existing untracked narrative source/test files were left unchanged. |
| AccessLint `audit_live` | Final landing and actual default-result scans: **No accessibility violations found.** This covers only mechanically detected rules in those states. |
| Browser interactions | Default Run; zero/positive/negative updates; inline out-of-range message; rapid replacement; company name sorting; Field/table cross-highlight; tab ArrowRight behavior; Copy link success; CSV file downloaded and inspected; reload and Back/Forward preserved calculated state. |
| Route checks | Backtests, Methodology, Data, About and Styleguide: expected H1/content and zero error alerts. |

Fonts are separate from the JS total: two local WOFF2 files totaling 260,312 bytes.
The full configuration catalog serializes to 160,798 bytes (40,078 bytes if gzipped).
Those gzip figures are compression measurements, not measured network transfer:
the standard-library preview server currently serves assets without gzip encoding.
No FCP, Lighthouse score or per-frame rendering performance is reported because it
was not measured. The browser inspection interface did not expose Performance API
entries in its read-only scope.

## Architectural and remaining limits

The checkpoint uses Vite/React/TypeScript with a same-origin Python standard-library
preview API. React/React DOM are runtime dependencies; Vite, TypeScript and their
type definitions are local build dependencies. No new Python dependency was added.
The original Streamlit application remains available. Deployment hardening is still
needed; this localhost preview adapter is not described as a production service.

Run is explicit at this checkpoint; automatic committed-edit reruns are later work.
Assumptions/exposures are currently read-only. Six policies disclose additional
configured inputs that cannot yet be edited here. Current Industry share links
carry the applied inputs plus model/data fingerprints. Historical versions are
not archived, and legacy Streamlit compressed URLs are not yet migrated.

Do not treat the basic secondary-page shell as final formula rendering: Methodology
still exposes source Markdown/math in places. Sources and historical backtest data
are real, but final secondary-page presentation and every relevant empty/error state
remain in the full v1 worklist. The field is intentionally static at this checkpoint.

The next action is the user's design approval, as explicitly requested by UI_SPEC §1,
before continuing the remaining screens and modes.

# Methodology page design contract

Purpose: explain the economic model quickly, separating financial facts from policy assumptions. No interface implementation, file paths or rendering mechanics in the reader-facing methodology.

Palette: OLED #000000; text #E8E5DC; secondary #A39D8F; amber #D5A64B; focus #F8CB72. Existing Source Code for navigation and numeric relationships; Source Sans for 16px explanatory text with 65–75 character lines.

Layout: a five-stop reading path beside one active chapter. A compact top-level process diagram connects reported data, business exposure and the calculated impact. Each chapter earns its own structure: source ledger and evidence split, channel selector, earnings-to-value bridge, uncertainty process, validation and model boundaries. Technical detail sits behind explicit disclosure controls.

Desktop: left-aligned sticky chapter navigation / generous readable content column; mobile: wrapped step controls above the content, no horizontally clipped navigation. Keyboard navigation, selected states and headings stay explicit. Motion only responds to chapter/channel choices; reduced motion is respected.

Review against the brief: retain the requested terminal identity without turning prose into dense telemetry. Use the sequence to teach the model; avoid decorative badges, repeated statistic cards or a wall of equations. Source content remains METHODOLOGY.md; the UI changes its presentation, not its financial meaning.

Verified chapter selection, arrow/Home/End navigation, keyboard disclosure, a 390px viewport and the worked example against the engine. Automated AccessLint scanning was blocked by approval review because its browser mechanism bypasses CSP; no automated accessibility pass is claimed.

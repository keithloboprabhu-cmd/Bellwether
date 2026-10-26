# Impact field: flowing terrain and density

Keep the OLED black/amber terminal, stable company positions, signed labels and exact financial values. The supplied standby terrain is the visual reference: fine halftone texture, flowing topographic lines and a restrained light gradient.

## Current treatment

- Company surfaces join through smooth, diagonally oriented inverse-distance interpolation, replacing isolated compact dot islands. Positive normalized weights keep the surface bounded by the mapped anchor heights. Every company anchor retains its exact signed height; missing values retain their neutral visual anchor and explicit unavailable label.
- A subtle continuous light layer and fine contours make the density read as terrain. Result contours, light and points use red for negative values and green for positive values, with magnitude controlling brightness and density. Amber is reserved for the illustrative standby field and console framing. The light is derived from the same surface, with no decorative noise added to measured height.
- Points remain 1.25 CSS pixels on a stable 2-pixel grid. Larger impacts add points, brightness and contour detail rather than changing point positions. Signed contour intervals are fixed at 0.025 of mapped height, with heavier fifth lines. The contour sampling mesh is 3 CSS pixels; empty contour levels are skipped and the rendered field is cached between selections.
- Density remains fixed across scenarios: min(0.92, 1.2 × |tanh(impact / 0.15)|). At an anchor, a 9.2% loss produces approximately 5.9 times the density of a 1.4% loss. Equal gains and losses use the same density rule. There is no nonzero dot floor for a uniformly zero result.

The presentation changes interpolation between anchors, not company values, impact mapping, financial calculations or company locations. Schematic terrain between firms is not a measured geographic or economic exposure.

## Verification

All 16 frontend tests passed, including bounded interpolation, exact anchor heights, continuous uniform surfaces, fixed node positions, strong density contrast and symmetric signs. Production TypeScript/Vite build passed. Browser review covers desktop and narrow-screen rendering with the current audited FDIC case; its Capital One result is approximately −5.0%, rather than the obsolete −9.2% in the earlier screenshot.

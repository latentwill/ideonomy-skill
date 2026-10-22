# Style-lane art examples workflow

Use this when ideonomy output is meant to become *concrete browser-previewable art artifacts* rather than prose-only brainstorming.

## Core pattern
- Convert the idea space into a small set of clearly distinct style lanes, usually 2x2 or 4-up.
- Give each lane a stable visual DNA: palette, motif family, composition logic, and surface treatment.
- Keep the lanes meaningfully different from each other so the user can compare directions, not just variations.
- Prefer muted, print-like finishing when the thread points toward risograph, paper, or archival aesthetics.
- Use short labels such as `What changed` and `Quick read` so the examples read like design directions, not essays.

## Implementation pattern
- Build browser-openable HTML artifacts under `docs/testnft/` when the user wants visible examples.
- Make the examples deterministic where possible: seed from the idea, the lane name, or the source data.
- If the piece is meant to be compared visually, keep the layout stable and change only the lane-specific parameters.
- If the user wants the examples “like the riso ones”, include paper tone, grain, bleed, and other print-finish cues rather than neon/CG polish.

## Verification pattern
- Render in headless Chromium.
- Check for console and page errors.
- Capture screenshots for each lane or example.
- Report the screenshot paths and the error status before claiming the artifacts are done.

## Good default deliverable shapes
- 2x2 grid of style lanes
- 4 separate browser-previewable HTML files
- one overview sheet plus one detailed poster per lane

---
name: ideonomy-plain
description: Systematically explore an idea through dimensions, transformations, and structured collections of alternatives. Use for ideation, conceptual classification, unexpected connections, and continued exploration of an idea space. Default plain-text format; not a substitute for fact-checking or implementing an already chosen plan.
---

# Ideonomy: plain

Explore how an idea can vary, what connects its variants, and what deserves investigation next. Default to this version unless the user wants a diagram suited to a monospace display.

## Explore and refine

An organon is a reusable instrument of inquiry: its structure should reveal relationships, gaps, and questions. Randomness is one way to choose a route through it, not evidence of novelty or a requirement to ignore the user's chosen method.

1. **Frame the subject.** State the seed idea, the purpose of this exploration, and constraints that must survive it. Start from a few concrete instances or properties. Use a working definition when the concept is contested; do not silently turn it into a universal definition.
2. **Choose a route.** Honor a requested operator, format, or continuation. Otherwise run `bash /absolute/path/to/this-skill/bin/pick` using the directory containing this loaded `SKILL.md`. Read the returned method bodies. If execution is unavailable, choose from [the catalog](methods/README.md) and disclose manual selection; never pretend a draw occurred.
3. **Make a bounded space.** Give dimensions meaningful values and apply the selected operators to them. For a cross-product, show the input sets and say whether the output is complete or sampled. Distinguish A-of-B from B-of-A when order changes meaning. Include an unfamiliar but relevant direction. If a picked method cannot illuminate the subject, explain the mismatch briefly and replace it deliberately instead of inventing relevance or repeatedly drawing until something comfortable appears.
4. **Build the organon.** Preserve enough of each input-to-output transformation for the reader to inspect it: the changed property, structural relationship, or pair of inputs. Use short derivation notes, not a transcript of private reasoning. Label supplied facts, illustrative examples, hypotheses, and coinages where confusion is possible. A new name does not establish a new phenomenon.
5. **Interrogate the result.** An empty cell may be unknown, unexamined, incompatible under stated assumptions, or a candidate for investigation; absence alone predicts nothing. Merge variants with the same mechanism. Retain a revealing failure when it exposes a dependency. For cross-domain transfers, identify both the preserved relationship and where the analogy breaks.
6. **Leave the next inquiry better equipped.** Select promising directions for the user's purpose and explain the tradeoff. Give a disconfirming observation, small experiment, or concrete comparison for the strongest practical candidates. For art or fiction, use a scene, audience response, or aesthetic constraint instead of forcing a scientific test. When useful, revise one axis or recurse on one revealing gap; stop when the requested scope is met or further passes only rephrase existing ideas. End with a specific unresolved question or unexplored region.

Keep depth proportional to the request. A short request can receive a compact organon and one follow-up question to investigate; it does not need a six-part report. For a larger exploration, read [the worked example](references/worked-example.md).

## Ground claims against an inspectable subject

When a candidate makes a factual claim about an existing codebase, dataset, document corpus, or product, inspect that claim before presenting it as a finding. A proposal can be useful without being unprecedented; distinguish the proposal from its description of the current state.

- **Name the claim:** what does the subject already contain or lack, according to the candidate?
- **Inspect the subject:** search relevant source, schemas, documentation, or behavior for likely names and equivalent concepts, then read the surrounding implementation. Record the scope and relevant paths or queries.
- **Match the conclusion to the evidence:** if the capability exists, identify it and explain whether the proposal changes its behavior, accessibility, or organization. If it is not found, say where you looked and what remains uncertain. Zero keyword matches alone do not prove absence. If access is inadequate, keep the candidate conditional.

Attach a concise evidence note to current-state claims. Distinguish “not found in the inspected files” from “does not exist.” Keep hypothetical alternatives available without presenting them as verified deficiencies. This checks descriptions of the subject; it does not require resolving every speculative idea before exploring it.

## Picker and continuity

The picker offers `--less`, `--more`, `--print`, and `--seed N`. A seed replays selection for an unchanged catalog and the same Bash/awk implementation; it does not reproduce an LLM's response. Random draws can repeat. Selection uses a local pseudorandom generator and needs no network or external service.

Default runs do not write files. For recency rotation, explicitly supply `--cooldown-dir /path/to/workspace/state`; this records method use outside the installed skill. Seeded runs ignore cooldown and never update it. Cooldown tracks usage, not quality or learning.

On follow-ups, reuse the user's existing organon and examine an identified gap before starting over. Preserve useful combinations and outcomes in the user's work when requested; examples and reproducible experiments are legitimate records, even though the random catalog contains primitives. Suggest reusable catalog additions when warranted. Editing installed skills is a separate maintenance task, not a silent consequence of brainstorming.

## Grounding

This is a contemporary adaptation of Patrick Gunkel's ideonomy, informed by Grace Kind's accessible synthesis. Its operator inventory, random picker, status labels, and output conventions are implementation choices, not a canonical or complete Gunkel system. Read [sources and attribution](references/sources.md) when explaining the lineage or extending methods. Use the original sources for historical claims; verify domain claims separately when factual accuracy matters.

## Plain rendering

Make the organon the main artifact, with headings about the subject. Prefer readable lists and short derivation notes. Use fenced ASCII tables when alignment matters; use labeled cells or lists for narrow or SMS channels. Avoid Unicode box drawing. The structure, candidate status, and unexplored region must remain understandable without special rendering.

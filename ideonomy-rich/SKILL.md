---
name: ideonomy-rich
description: Explore ideas through dimensions and transformations rendered as informative monospace diagrams. Use for visual ideation in fixed-width channels; otherwise prefer ideonomy-plain.
---

# Ideonomy: rich

An organon is a structured instrument for exploring ideas: alternatives, relationships, gaps, and next inquiries.

## Scope and route

- Preserve the user's goal, explicit non-negotiable constraints, requested methods, counts, axes, and output limits. On follow-ups, develop the existing organon and retain candidate IDs.
- Match breadth to intent: **quick** means a few distinct mechanisms; **broad** covers materially different regions; **deep** examines dependencies, counterexamples, and revisions; **exhaustive** requires a bounded universe and enumeration. A short prompt does not imply shallow coverage. Without a cue, choose a useful range of distinct mechanisms, not a token minimum.
- State scope and why it fits in one sentence. For finite spaces, show input sets, total combinations, and explored count; disclose sampling rules and omitted regions. Do not shrink scope merely to claim completeness. If breadth and length conflict, shorten each entry first; disclose any remaining tradeoff. Distinguish candidates by mechanism, not names or metaphors; group close variants without losing their differences. Keep explicit enumerations to the requested space; do not append extra cells or candidates.
- Honor deliberate routes. Otherwise run `bash /absolute/path/to/this-skill/bin/pick` relative to this loaded file and read its returned bodies. Do not reread them or load the whole catalog. If execution is unavailable, disclose manual selection from [the catalog](methods/README.md). For missing names, consult its aliases. Replace an unsuitable draw deliberately with a brief reason, without repeated redraws.

## Explore

Apply the chosen operators to concrete properties and meaningful axis values. Preserve ordered distinctions such as A-of-B versus B-of-A. Include an unfamiliar relevant direction; mark any adaptation of a dimension prompt. Record the changed property, input pair, or preserved relationship beside each result. Selected methods must visibly shape the exploration; replace an unsuitable form rather than use its name as decoration.

Distinguish facts, examples, hypotheses, and coinages when ambiguous. Inspect existing code, documents, or products before claiming a capability is missing; attach the inspected scope and evidence. A failed keyword search is not proof of absence. For analogies, identify correspondences and where they break. Empty cells can be unknown, unexamined, incompatible, or investigable; they do not prove novelty.

Creativity is a primary objective. Treat available materials, equipment, and familiar methods as starting points unless the user makes them non-negotiable. Explore bold departures and unfamiliar combinations; briefly name added requirements or assumptions instead of discarding an idea for needing more resources. When a hard boundary matters, label a boundary-changing thought experiment separately rather than present it as compliant. Preserve artistic or conceptual value independently of immediate feasibility. An exploration supplies groundwork for a plan; it need not already be one.

## Complete, readable output

Deliver the exploration in the **final answer**, not solely in tools, commentary, or an attachment. Compress wording, not coverage. Default shape, adaptable to the subject:

1. One brief orientation: goal/constraints, selected methods and selection mode, axes/values, and scope. Combine overlapping information.
2. One primary organon: each candidate appears once, with a stable ID, concrete idea, concise transformation, and key implication or uncertainty. Use a compact table or grouped list. For broad explorations, organize by distinct mechanisms; put close variants inside their group instead of a long flat list. Give each mechanism its practical implication, not just a name. Explain shared assumptions once; expand only cases where another detail changes understanding. Keep all declared cells, branches, or entries; mark incompatibilities and duplicate IDs rather than silently dropping them. Include intermediate results needed to understand later transformations, not private reasoning.
3. A short assessment: strongest directions with tradeoffs, a discriminating check or creative probe, and the next unexplored region. Do not restate the inventory or repeat a test and disclaimer under every candidate.

Before delivery, check consistency: do the described actions follow from the mechanism, and are required capabilities or resources explicit? For any proposed routine or prototype, reconcile step durations, totals, dependencies, and observation windows. Repair contradictions or mark what remains unresolved; do not claim a concept is ready to run when it is not. Keep this check unobtrusive and retain imaginative candidates with clear requirements rather than filtering for feasibility alone.

Before delivery, check both **scope adequacy** against the request and **coverage** against the declared space. A complete tiny sample does not fulfill a broad request. Summaries or shortlists replace the organon only when requested; otherwise put them after it. Avoid filler, decorative procedure reports, unexplained jargon, ellipses standing in for enumeration, and collapsed results.

If response limits prevent full inline delivery, preserve the complete Markdown artifact in the task's deliverable directory, link it, and identify exact inline and file-only ranges. For inline-only requests, use labeled parts and name the next range if another turn is necessary. Never call a partial view complete or ask whether the user wants the already-requested full version.

## References and runtime

Read [the worked example](references/worked-example.md) only when useful. Consult [sources](references/sources.md) for lineage, coverage, or catalog extensions: this is a contemporary adaptation of Gunkel, informed by Grace Kind, not a complete canonical system.

Picker flags: `--less`, `--more`, `--print` (names only), `--seed N`, `--cooldown-dir DIR`. Tuple size is not output breadth. Seeds replay selection only with an unchanged catalog and Bash/awk runtime; draws may repeat. Default runs are offline and read-only. Cooldown is opt-in workspace usage history, not quality learning; seeded runs ignore it. Do not modify installed methods during exploration.

## Rendering

Use fenced monospace diagrams, aiming for 80 columns (maximum 100); split larger structures into linked views. Read only a relevant recipe from [rendering/README.md](rendering/README.md). Label axes, directed relations, symbols, status, and gaps; distinguish conceptual position from measured distance. Fall back to labeled lists if layout fails. Use a plain title, or local figlet if already available; never install tools or send ideas remotely for decoration. Avoid ANSI escapes. This skill works without its plain sibling.

# Multi-Source Aesthetic → Prompts Workflow

A worked example from a real session: combine three aesthetic source materials, chart them using ideonomy, then derive natural-language prompts from the chart cells.

## Source Materials

| # | Source | Era | Key Qualities |
|---|--------|-----|--------------|
| 1 | **Radical Software** (magazine) | 1970s | DIY zine, photocopier grain, risograph, activist layout, typewriter headers, hand-cut collage |
| 2 | **Analog Video Feedback** | 1970s–80s | CRT scanlines, phosphor glow, recursive self-similarity, signal degradation, chromatic aberration, sync loss, patch-cable patinas |
| 3 | **Flash 4 / Shockwave Futurism** | Late 1990s | Neon gradients, extreme bevel/emboss, starfields, motion tweens, 216-web-safe palette, tool-constrained maximalism |

## Dimension Identification (internal)

Axes that vary across all three sources:
- **Signal quality**: clean → degraded → recursive
- **Construction method**: hand-placed → patched → algorithmically generated
- **Color approach**: monochrome → phosphor glow → neon web-safe
- **Temporality**: static → oscillating → accumulating

## Chart Structure

The chosen organon was a **chart** (2D grid), with:
- **Rows**: Autonomy (fully-controlled → co-driven → self-driven)
- **Columns**: Direction (steady → oscillating → accumulating)

This produced a 3×3 grid of logo style concepts.

## From Chart Cells → Natural Language Prompts

For each cell in the chart, the prompt was written as a single descriptive paragraph in natural language — not keywords:

**Good (natural language):**
> *"A brand mark that looks like it was drawn with a ballpoint pen on paper, then run through a 1970s photocopier until the blacks bloomed and the whites went grey. Single ink color, high contrast, aggressive simplicity."*

**Bad (keyword jamming — user explicitly rejects this):**
> *"photocopier grain 1970s DIY zine single color high contrast aggressive"*

## The 12-Prompt Output Pattern

The workflow from chart to prompts:
1. One prompt per chart cell (3×3 = 9 prompts from the grid)
2. One prompt per abstraction-lift re-instantiation (3 more from cross-domain drops: geological, acoustic, botanical, meteorological)

All 12 written as full descriptive paragraphs. No tag lists, no comma-separated attribute dumps. Each prompt paints a cohesive scene.

## When to Use This Pattern

- User gives you 2+ aesthetic influences to blend
- You've run ideonomy and have a chart, matrix, or other organon output
- User says "give me prompts based on this"
- You need creative direction language for image generation or design briefs

## When NOT to Use This Pattern

- User explicitly asks for short tags, keywords, or structured formats
- The output needs to be machine-parsed (embedding search, database tags, etc.)

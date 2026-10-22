---
name: ideonomy-rich
description: Use when expanding an idea AND the output channel can render monospace cleanly — terminals, READMEs, blog posts with monospace code blocks, fixed-width-font emails, ttyrec sessions, the Claude Code transcript itself. Same primitives as `ideonomy-plain`, but renders the artifact as performative ASCII art with Unicode box-drawing, figlet banners, density gradients, and visible ideonomy-machinery layers (tuple legend, dimensions surfaced, operator-named dividers, ideonomy trail). If the channel might mangle Unicode (Telegram, SMS, plain Slack DMs), use `ideonomy-plain` instead.
---

# Ideonomy-Rich

Sibling skill to `ideonomy-plain`. Same operators, organons, dimension-prompts, picker, cooldown. Different rendering policy.

```
╔═══════════════════════════════════════════════════════════════════╗
║  ideonomy-plain  →  lowest-common-denominator: survives SMS       ║
║  ideonomy-rich   →  highest-expression: feel ideas come alive     ║
║                     in a monospace terminal                       ║
╚═══════════════════════════════════════════════════════════════════╝
```

If you're not sure which to pick, default to `ideonomy-plain`. Use this one when you know the medium can hold the art.

## Core principle

Same as `ideonomy-plain` — Patrick Gunkel's framework via Grace Kind. Ideas have *properties* varying along *dimensions*; expand by negating, substituting, combining, re-instantiating. Read `~/.claude/skills/ideonomy-plain/SKILL.md` for the conceptual core if you haven't.

The difference is everything below: **render the organon as performative ASCII art**, not as plain bullets. Inspired by mahidalhan's *ascii-art-explainer*: composition teaches, motion shown, density is meaning, drama at the pivot.

## How to invoke

**Step 1 — pick a method tuple.**

```bash
~/.claude/skills/ideonomy-rich/bin/pick
```

(Delegates to `ideonomy-plain`'s picker; same catalog. Picking from one warms cooldown for both, by design.)

**Step 2 — work through the tuple in two passes.** Same internal pass as `ideonomy-plain`: dimension-prompts → operators → organon. The external pass is what changes.

**Step 3 — render the artifact in five visible layers.**

A defining feature of `ideonomy-rich`: **the brainstorming itself must be visible.** The reader should be able to see which operator produced which section, what dimensions the brainstorming explored, and — crucially — what was *not* surfaced. Reading the artifact equals watching the ideonomy happen. If the reader can't tell the artifact came out of the operators × organon × dim-prompts, you buried the machinery.

This does **not** mean reverting to procedural headers (`Phase A`, `Phase B`). The middle path: name the operator AND the specific move it made, side by side, in content-named language.

### Layer 1 — title banner

Open with a figlet banner of the user's idea.

```bash
# Local C binary (preferred — installed via brew on this system)
figlet -f slant "<idea>"
figlet -f doom "<idea>"
figlet -w 100 -f banner3 "<idea>"        # set max width

# Coloured / filtered variant (live terminal only — emits ANSI)
toilet -f pagga --metal "<idea>"

# Remote fallback (no install needed; safe in any context)
curl -s "https://asciified.thelicato.io/api/v2/ascii?text=<idea>&font=Slant"
```

Recommended fonts by mood:

| Font       | Mood                        |
|------------|-----------------------------|
| `slant`    | clean, modern, default      |
| `doom`     | bold, declarative           |
| `big`      | wide, readable              |
| `banner3`  | wide-display banner         |
| `cyberlarge` | tech / systems theme      |
| `gothic`   | dramatic, weighty           |
| `small`    | subtitles, secondary banners |

Frame the banner with hand-drawn `╔═╗` if you want a heavy outer border, or leave it bare if the font has weight. Note: the `boxes` CLI's default designs render ASCII `+--+` borders that clash with the Unicode aesthetic — prefer hand-drawn `╔═╗` framing or skip framing the banner.

### Layer 2 — tuple legend

Right after the banner, emit a compact block naming the tuple drawn for *this* artifact. The legend tells the reader "this is the brainstorming kit I used":

```
╭─ TUPLE ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─╮
│  ◆ OPERATORS    substitution · negation                                │
│  ◆ ORGANON      dictionary                                             │
│  ◆ DIMENSIONS   decomposability · naturalness · visibility             │
╰─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─╯
```

Use `╭─╮` rounded for the legend frame — soft, indicating "metadata, not the artifact itself."

### Layer 3 — dimensions surfaced

Before the operator outputs, show what each picked dimension-prompt revealed about the user's idea. This is where the reader sees the axes the brainstorming explored. Each dim gets a small block: its axis (with `●` / `○` marking the values that matter), a one-line summary of what surfaced, and `★` on the pivot dim if one stands out:

```
╭─ DIMENSIONS ──────────────────────────────────────────────────────────────────╮
│                                                                               │
│   decomposability   monolithic ●━━━━━━━━━━━━━━━━━━━○ decomposable             │
│                     current is one big skill; alternatives split into         │
│                     preflight + runtime + visible output                      │
│                                                                               │
│   naturalness       instruction-as-discipline ●━━━━━━○ artifact-as-discipline │
│                     discipline baked into the visible output, not the prompt  │
│                                                                               │
│   visibility   ★    invisible ○━━━━━━━━━━━━━━━━━━━━━● visible                 │
│                     0% (current) → footer-visible → fully laid out            │
│                     ★ pivot — this is the user's stated complaint             │
│                                                                               │
╰───────────────────────────────────────────────────────────────────────────────╯
```

If the dim surfaced *nothing useful* for this idea, say so in one phrase rather than padding. Empty dims are a tell that the picker drew an unfit prompt; the reader benefits from seeing that.

### Layer 4 — artifact body, with operator-named dividers

The picked organon dictates the form. Each organon has a rendering recipe at `~/.claude/skills/ideonomy-rich/rendering/<organon>.md`. Core recipes: `chart`, `tree`, `list`, `atlas`, `scale`, `cycle`, `dictionary`. Other organons fall back to the principles below.

**The organon's name appears in the artifact's main header** — `═══ ◆ DICTIONARY ◆ ═══` followed by the body, never `Phase C` or `Organon: dictionary`.

When two or more operators were picked, divide their contributions with a divider that **names BOTH the operator AND the specific move**:

```
═══════════════════════════════════════════════════════════════════════════════════
  ◆  NEGATION  ◆      negating "process is invisible" → "process leaves a trail"
═══════════════════════════════════════════════════════════════════════════════════
```

The divider has three visible parts:

1. The operator's name (`NEGATION`, `SUBSTITUTION`, `COMBINATION`, `ABSTRACTION-LIFT`, etc.)
2. A one-line description of the *specific move* — what was negated, substituted, combined
3. The arrow `→` making the move visible

This is the difference that addresses the "where's the ideonomy?" complaint: the reader can see, at the divider, both the abstract operator and the concrete move it produced. `◆ OPPOSITES ◆` (content-only) hides the operator. `Phase B — Operator: Negation` (procedure-only) hides the move. `◆ NEGATION ◆ "X" → "Y"` shows both.

### Layer 5 — ideonomy trail

Every artifact ends with a structured trail footer. The trail recaps the brainstorming machinery and — most importantly — names what was *not* surfaced. The "not surfaced" line is where the user finds adjacent directions of inquiry.

```
[ideonomy · 4 moves · 3 dims · 1 organon · "vigil v2 redesign"]
  dim · pivot:    visibility — invisible→visible is the user's complaint
  ◆ negation:     "invisible by design"   → vigil-trail (Option A)
  ◆ substitution: "self-grading"           → vigil-twin (Option B)
  ◆ negation:     "comprehensive"          → vigil-slim (Option C)
  ◆ substitution: "single draft → revise"  → vigil-tournament (Option D)
  organon:        dictionary — 4 entries
  not surfaced:   "do nothing", "kill vigil entirely", "make vigil charge per-pass"
                  these are negations of meta-properties (existence, free-ness) the
                  picker's dim-prompts didn't reach. worth a follow-up tuple.
```

Trail rules:

- **Always last** in the artifact, in a single fenced code block, no trailing commentary
- One line per move; each line names operator + the specific input/output
- **The `not surfaced:` line is mandatory.** Even one phrase. This is the line that turns the trail from a recap into a generator — it tells the user where the next exploration could start.
- The trail makes the brainstorming falsifiable: if no trail appears, no real ideonomy ran (you wrote a thoughtful answer that happened to dress up nice).

## Rendering principles

- **Composition teaches, not labels.** A flat box with text inside is wasted opportunity. Spatial arrangement, density, and motion should carry meaning. If your "diagram" is just labeled rectangles that could be bullet points, you've failed.
- **Visual hierarchy through line weight.** Mix `┌─┐` (single, default), `╔═╗` (double, emphasis), and `╭─╮` (rounded, soft) within one artifact to mark primary / secondary / tertiary structure.
- **Show motion.** `→ ↗ ↘ ↑ ↓ ═══▶ ··· >>>>>>` for flow, transformation, dependency. Static structures should still suggest direction where direction exists.
- **Density is meaning.** `░ ▒ ▓ █` shows intensity, fill, certainty, age, frequency. Pick a semantic axis and use the gradient consistently within one diagram.
- **Decorative emphasis sparingly.** `★ ◆ ● ○ ◇ ▲ ▼` for markers, status, importance. One symbol per role within a piece — `◇` always means *empty/coinage opportunity*, `●` always means *canonical instance*, etc.
- **Drama at the pivot.** If the expansion has a key insight or a single empty cell that's the point, let composition draw the eye there — center it, frame it with `«   »` or `⟦  ⟧`, isolate it with whitespace. Make the reader land on it.

## Character palette

```
Box (single):   ┌ ─ ┐ │ └ ┘ ├ ┤ ┬ ┴ ┼
Box (double):   ╔ ═ ╗ ║ ╚ ╝ ╠ ╣ ╦ ╩ ╬
Box (rounded):  ╭ ─ ╮ │ ╰ ╯
Density:        ░ ▒ ▓ █ ▄ ▀ ▌ ▐
Geometric:      ◆ ◇ ◈ ● ○ ◉ ■ □ ▲ △ ▼ ▽ ★ ☆ ✦ ✧
Arrows:         → ← ↑ ↓ ↗ ↘ ↙ ↖ ⟶ ⟵ ═══▶ ◀═══ ↻ ↺
Diagonals:      ╱ ╲
Brackets:       ⟦ ⟧ ⟨ ⟩ « » ⌜ ⌝ ⌞ ⌟
```

## Constraints

- **Width ≤ 100 chars per line.** Most terminals default to 80; 100 leaves a comfortable margin while letting wide art breathe. Anything wider wraps and turns ugly.
- **Wrap large diagrams in fenced code blocks** (```` ``` ````). Even a monospace-friendly channel may proportional-font your prose; the fence guarantees alignment.
- **One large pyfiglet banner per artifact** (the title). Use `small`/`mini` for sub-banners if needed; don't make every section a 12-line banner.
- **No ANSI color in saved-text contexts.** `toilet --gay` looks great in a live terminal, looks like `\e[31m` garbage in a markdown file. Color belongs to live tty only.
- **Box-drawing styles do not mix within a single diagram.** Pick one of `┌─┐` / `╔═╗` / `╭─╮` and stick with it; mixing `+--+` ASCII with `┌─┐` Unicode is the cardinal sin.

## Red flags

**Brainstorming-machinery invisibility (the big one):**

- No tuple legend after the banner → reader can't see which kit was used.
- No `DIMENSIONS` block → the axes the brainstorming explored are hidden.
- Dividers say `◆ OPPOSITES ◆` (content-only, no operator named) → the *machinery* is invisible; this is the failure mode that prompted Layer 4 to require operator+move.
- No ideonomy trail at the end → no falsifiability; the artifact is indistinguishable from a thoughtful answer that didn't use ideonomy at all.
- Trail's `not surfaced:` line missing or padded with filler → the most generative line is the most likely to be skipped; treat its absence as a vigil-style "trail-without-vigil" tell.

**Procedure leaking out (don't over-correct):**

- A section titled `Phase A/B/C`, `Operator: <name>`, `Organon: <name>` → procedure leaking. The fix is *not* to drop the operator name from the divider; it's to pair it with the specific move (`◆ NEGATION ◆ "X" → "Y"`).

**Aesthetic / formatting:**

- Plain bullets and prose, no organon visually rendered → you skipped the rendering layer.
- Figlet banner so wide it wraps in 100-char terminal → use `small` or shorten.
- Decorative symbols (`★◆●`) sprayed without consistent semantic role → noise.
- Visual hierarchy doesn't track conceptual hierarchy → most important = most visually emphatic.
- Mixed `+--+` and `┌─┐` in one diagram → pick one style.
- The artifact is just labels-in-boxes that could have been a bullet list → composition isn't teaching anything.

## See also

- `~/.claude/skills/ideonomy-plain/SKILL.md` — sibling, plain-text-portable. Same primitives, different rendering policy.
- `~/.claude/skills/ideonomy-rich/rendering/` — per-organon recipes.
- `references/style-lane-art-examples.md` — workflow for turning ideation into browser-previewable art examples.
- Hermes `ascii-art` skill — pyfiglet, cowsay, boxes, image-to-ascii. Install if missing.
- mahidalhan/claude-hacks `ascii-art-explainer` — performative ASCII philosophy this skill inherits.
- mahidalhan/claude-hacks `ascii-explainer` — diagnose-then-render approach for diagrams.

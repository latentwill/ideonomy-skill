# AGENTS.md

Guidelines for AI agents working in this repository.

## Repository Overview

This repository contains **Agent Skills** for AI agents following the [Agent Skills specification](https://agentskills.io/specification.md). Skills install to `.agents/skills/` (the cross-agent standard). This repo also serves as a **Claude Code plugin marketplace** via `.claude-plugin/marketplace.json`.

- **Name**: Ideonomy
- **GitHub**: [latentwill/ideonomy-skill](https://github.com/latentwill/ideonomy-skill)
- **Creator**: Ed Kennedy
- **License**: MIT for code; CC BY 4.0 for prose (see LICENSE)

## Repository Structure

```
ideonomy-skill/
├── .claude-plugin/marketplace.json
├── ideonomy-plain/          # self-contained portable skill
│   ├── SKILL.md
│   ├── bin/pick
│   ├── methods/
│   ├── references/
│   └── examples/
├── ideonomy-rich/           # self-contained monospace skill
│   ├── SKILL.md
│   ├── bin/pick
│   ├── methods/
│   ├── references/
│   └── rendering/
├── tests/
├── AGENTS.md
├── LICENSE
└── README.md
```

## Agent Skills Specification

### Required Frontmatter

```yaml
---
name: skill-name
description: What this skill does and when to use it.
---
```

### Name Field Rules

- Lowercase letters, numbers, and hyphens only
- Must match parent directory name exactly

## Claude Code Plugin

Install with:

```bash
/plugin marketplace add latentwill/ideonomy-skill
/plugin install ideonomy
```

See [Claude Code plugins documentation](https://code.claude.com/docs/en/plugins.md) for details.

## Adding Methods to the Catalog

The three method categories live under `ideonomy-plain/methods/` and `ideonomy-rich/methods/`. Both must stay in sync — changes to one skill's methods should be mirrored to the other.

Adding a new method: copy the file to both `ideonomy-plain/methods/<category>/` and `ideonomy-rich/methods/<category>/`. The `bin/pick` script discovers methods dynamically via `find`, so no manifest update is needed.

## Git Workflow

- New methods: `feature/<category>-<name>` (e.g., `feature/organon-flowchart`)
- Skill improvements: `fix/ideonomy-plain-description` or `fix/ideonomy-rich-rendering`
- Documentation: `docs/description`

Commit format: `feat: add <name> organon` / `fix: improve pick script mtime weighting` / `docs: update README`

## Validation and provenance

Mirror shared `bin/`, `methods/`, and `references/` changes in both skills. Run `python3 -m unittest discover -s tests -v` and Bash syntax checks after picker edits. Use `tests/behavioral-evaluation.md` for meaningful output evaluation; do not report illustrative examples as executed model benchmarks.

Preserve source distinctions in `references/sources.md`. Randomness is local and optional to the conceptual workflow. Ordinary ideation must not silently modify installed methods or invoke remote services for selection or decoration.

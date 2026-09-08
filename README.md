# Ideonomy: explore, compare, investigate

Two self-contained agent skills for exploring ideas through dimensions, transformations, and structured artifacts. Inspired by Patrick Gunkel's ideonomy and informed by [Grace Kind's essays](https://gracekind.net/writing/ideonomy/intro/).

The aim is an idea space you can inspect and develop: alternatives, relationships, revealing failures, and questions worth pursuing. Local random selection helps vary the approach. It does not guarantee novelty, non-repetition, or useful results.

| Skill | Output |
|---|---|
| `ideonomy-plain` | Portable lists and fenced ASCII tables; the default. |
| `ideonomy-rich` | Monospace diagrams where arrangement and symbols convey relationships. |

Both use the same inquiry workflow and catalog: 8 operators, 17 organons, and 29 dimension prompts. An organon is a structured tool for thought, such as a list, chart, tree, or atlas. The catalog is a contemporary adaptation, not Gunkel's complete system.

## Install

Clone and copy either folder into your agent's supported skills directory:

```bash
git clone https://github.com/latentwill/ideonomy-skill.git
mkdir -p .agents/skills
cp -R ideonomy-skill/ideonomy-plain .agents/skills/
# Optional:
cp -R ideonomy-skill/ideonomy-rich .agents/skills/
```

The repository also includes a Claude Code marketplace manifest. Each skill folder carries its own picker, methods, and references and works without its sibling. The runtime needs Bash and standard Unix tools (`awk`, `sort`, `find`, `stat`, `sed`, `cut`, `date`). No network service or package installation is needed. Rich output may use an already installed `figlet`; otherwise it uses a plain title.

## Try it

Ask the agent:

> Explore alternatives to a neighborhood tool library without adding paid staff. Show the assumptions and the most useful next experiment.

For a reproducible method selection from the repository root:

```bash
bash ideonomy-plain/bin/pick --seed 42
```

Or ask for a deliberate route:

> Use a chart to cross custody models with access timing. Then develop the most revealing gap.

See the [worked example](ideonomy-plain/references/worked-example.md). It illustrates a complete six-pair space, a revised dimension, and an analogy whose limits are explicit. It is an original demonstration, not a field-tested result.

## Picker

| Flag | Behavior |
|---|---|
| none | Local draw: 2 operators, 1 organon, 3 dimension prompts; no writes. |
| `--less` | 1 operator, 1 organon, 2 prompts. |
| `--more` | 3 operators, 2 organons, 5 prompts. |
| `--print` | Print selected names without method bodies. |
| `--seed N` | Integer 0–32767. Replays selection on the same Bash/awk implementation and unchanged catalog; no history writes. |
| `--cooldown-dir DIR` | Opt-in usage history in a workspace directory outside the installation. |

The former `--random-org` option has been removed. All selection is local. Invalid options and malformed seeds fail with exit code 2.

Cooldown adds a recency penalty to random ranking, decaying with a one-hour half-life. It does not guarantee non-repetition or learn which methods work. Seeded runs ignore history. Default and seeded draws leave installed files untouched.

There are 1,739,304 possible unordered default method combinations and 904,438,080 in `--more` for the current catalog. These are combinatorial counts, not claims that all combinations are reachable through the finite seed space or that they produce distinct ideas. Selection is not cryptographic. Catalog paths must not contain tabs or newlines; spaces are supported. Reproducibility across different Bash/awk versions is not promised.

## Grounding and development

Gunkel's [introduction](https://ideonomy.mit.edu/intro.html) connects generation with criticism and testing, and treats comprehensive coverage as an aspiration. This adaptation therefore keeps hypotheses distinct from evidence and reports the limits of an exploration. His [provisional subdivisions](https://ideonomy.mit.edu/division.html) also caution against treating a short operator list as a finished canon.

Patrick Gunkel (1947–2017) originated ideonomy. Whitman Richards organized and hosted the work at MIT. The [archive](https://ideonomy.mit.edu/legacy-index.html) preserves the monographs and charts; Kind's writing makes a valuable route into them. See [source distinctions](ideonomy-plain/references/sources.md) for claims, provenance, and modern additions.

The picker draws primitives; it does not draw historical recipes. Useful combinations can still be retained as examples and experiments. Follow-up work should refine the existing organon when appropriate. Catalog maintenance is explicit, not a silent side effect of using a skill.

## Maintenance and validation

Edit shared resources in `ideonomy-plain/`, then mirror `bin/`, `methods/`, and `references/` to `ideonomy-rich/`. Keep the two entrypoints distinct only where selection descriptions and rendering require it.

```bash
python3 -m unittest discover -s tests -v
bash -n ideonomy-plain/bin/pick
bash -n ideonomy-rich/bin/pick
```

Tests cover picker behavior and shared-resource consistency. The [behavioral evaluation cases](tests/behavioral-evaluation.md) assess the skill's actual outputs; passing script tests does not establish better ideation. Python is only needed to run tests.

## License

Code is MIT; repository prose is CC BY 4.0. Preserve attribution to Grace Kind and Patrick Gunkel and identify adaptations. See [LICENSE](LICENSE). Linked external sources retain their own terms.

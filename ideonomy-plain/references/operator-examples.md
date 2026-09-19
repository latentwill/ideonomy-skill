# Operator examples and historical notes

Optional illustrations from the earlier method guides. Current method files govern execution; these examples are simplified interpretations, not evidence of novelty or validation. See [sources](sources.md) for attribution.

## negation

### Notes from Grace Kind's essay

- Ideonomic negation isn't single-valued like mathematical negation. It produces a *set* of opposites depending on which property you negate.
- Kind proposes “partial involution” as an illustrative expectation: reversing a contrast can recover the starting idea. It is not a proven algebraic guarantee for arbitrary interpretations or model outputs.
- Negation is a special case of substitution: it substitutes a *definitional* property, while ordinary substitution can swap any property.

### Worked example (Grace's, applied to *democracy*)

Kind's deliberately simplified working model of democracy uses properties such as: there is a government; power is distributed; the people make law; the rulers are people; people are weighted equally.

Negating each:

| Property negated | Resulting idea |
|---|---|
| There is a government | **Anarchy** |
| Power is distributed | **Autocracy** |
| The people make law | **Minoritarianism** |
| The rulers are people | **Automatocracy**, **zoocracy**, **phytocracy** (rule by machines, animals, plants) |
| People are politically strong | **Demoastheneia** (weakness of people) |
| People weighted equally | **Weighted democracy** (some voices count more) |

These are conceptual contrasts, not equivalent constitutional categories. *Demoastheneia* is Kind's coinage; her essay explicitly warns through an example that an LLM can fabricate established usage for it. Label invented terms and do not infer historical use from a plausible definition.

## combination

### Illustrations (emotion × emotion)

Kind's introduction mentions Absurd Worship and Worrying Acceptance. The glosses and further pairs below are this repository's interpretations, not quotations or verified emotion categories:

- **Absurd Worship** — devotion to something the devotee knows is meaningless
- **Worrying Acceptance** — the anxious form of acceptance
- **Joyful Disgust** — pleasure at being repulsed
- **Greedy Sadness** — wanting more of one's own grief

These pairs may evoke recognizable states or contradictions. Treat that recognition as an interpretation to discuss, not a claim about how common a state is.

The cross-product surfaces ideas that are too specific to have shown up in the input organons individually but emerge naturally from their interaction.


## substitution

### Worked example (Grace's, applied to *trees*)

A natural tree has properties:

- Naturalness: **Natural**
- Homogeneity: **Heterogenous**
- Hierarchicalness: **Non-hierarchical**
- Longevity: **Variably-lived**
- Complexity: **Complex**

Substituting *Naturalness = Natural → Man-made* (with everything else held constant) produces *man-made trees that are heterogenous, non-hierarchical, variably-lived, and complex*. That's a sculpture, an AI-generated synthetic forest, a topiary, a forest of microphone stands at a music festival, etc.

Substituting *Homogeneity = Heterogenous → Homogenous* produces a tree where every leaf, branch, and root is identical. That's a fractal, an idealized mathematical tree, a clone-orchard.

Each substitution surfaces a population of related ideas — some of which already exist, some of which don't.

## abstraction-lift

### Worked example

Original: "Our company's authentication service has a single point of failure — if that server goes down, nobody can log in."

Strip:
- "Our company's authentication service" → *a gatekeeper*
- "single point of failure" → *single instance with no redundancy*
- "nobody can log in" → *the system it gates becomes inaccessible*

Lifted: *A unique gatekeeper guards access to a system; if the gatekeeper fails, the system is unreachable.*

Recognizable in other domains:
- Biology: a single chokepoint enzyme in a metabolic pathway
- City planning: a single bridge connecting two districts
- Mythology: the single ferryman across the Styx
- Software: any single-master architecture

Each of those domains has worked out its own answers (redundant copies, parallel pathways, ferry-fleet, multi-master replication). Each answer is a candidate solution to lift back down to the original problem.

## dimension-identification

### Quote from Grace

> Dimensions are the space of possible properties along an axis, and properties are the possible values for a dimension.

### Example dimensions Grace lists

| Dimension | Possible values |
|---|---|
| Naturalness | Natural / Man-made |
| Homogeneity | Homogenous / Heterogenous |
| Hierarchicalness | Hierarchical / Non-hierarchical |
| Longevity | Long-lived / Short-lived / Equally-lived (~human) / Variably-lived |
| Complexity | Complex / Simple |

These five aren't a fixed catalog — they're examples. The dimensions of *your* idea depend on *your* idea. The dimension-prompts in `methods/dimension-prompts/` are a starting battery; cross-apply them to surface candidates.


## tree-finding

### Example

For the idea *democracy*:

- Up: form-of-government → political-system → social-coordination-mechanism → cooperation-pattern
- Down: direct-democracy / representative-democracy / liquid-democracy / sortition; each subdivides further
- Across (siblings of *form of government*): monarchy, oligarchy, theocracy, anarchy, technocracy, geniocracy, …
- Levels: at the level of *cooperation patterns*, democracy sits next to markets, juries, festivals, and gift economies — a different and often more interesting peer set than the conventional one.

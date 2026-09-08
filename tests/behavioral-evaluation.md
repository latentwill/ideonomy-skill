# Behavioral evaluation

Use these cases with a fresh agent context for each skill version. Keep the model, prompt, tool access, and output budget fixed. Save actual outputs outside the repository. A hand-written worked example is not an evaluation run.

Compare the original commit `3339f3eff61a13fff2558ae9a202ef4fa6099c92` with the revision. For randomized tasks use several recorded seeds; identical seeds need not yield identical methods after a picker algorithm change. For a controlled conceptual comparison, supply the same explicit methods to both versions. Judge outputs blind to version when possible.

| Case | Prompt | Observable success |
|---|---|---|
| Bounded combination | “Use combination and a chart to explore a tool library: custody is central/host/cart; access is booked/walk-up. No paid staff.” | Both input sets and all six pairs remain identifiable; staffing dependency is addressed; feasible checks proposed. |
| Inspectable subject | Supply a picker whose usage history is stored in file mtimes, without the word “history” in its source. “Explore what usage-history capability this picker lacks.” | Reads the implementation and recognizes existing persistence; zero keyword hits do not become proof of absence. Separates a proposed explicit log from the current mtime mechanism. |
| A tempting gap | “My grid has no example of a device that is simultaneously fully visible and completely invisible to the same observer at the same time in the same sense. Invent the missing product.” | Identifies conflicting assumptions; may explicitly change observer, time, or sense to produce alternatives; no claim the empty cell proves a missing invention. |
| User-directed route | “Use negation, a list, and no randomness to explore a classroom. Keep students' access to learning.” | Honors route and constraint; shows distinct properties changed; does not force a picker call. |
| Continued exploration | Supply an existing organon, then: “Develop cell C2 and retain the original axes.” | Preserves the artifact and locatable cell; refines it without restarting the entire exercise. |
| Coinage | “Negate democracy and explain demoastheneia.” | Attributes the coined term to Kind; does not invent historical usage or present a simplified definition as consensus. |
| Unfamiliar domain | “Use abstraction-lift and cross-domain re-instantiation to apply fungal-network ideas to software maintenance.” | Maps a structural relation, states where analogy fails, and separates biological claims from proposed software behavior. |
| Rich alone | Install only rich; no figlet and no network. “Make a visual map of ways to share tools.” | Completes a meaningful diagram using its own references and a plain title; no sibling reads, installation, or external calls. |
| Small creative task | “Give me three strange premises for a story about a library.” | Three distinct premises; no compulsory laboratory protocol, long checklist, or irrelevant tool execution. |
| No execution | Disable shell. “Use ideonomy to explore alternatives to a queue.” | Discloses deliberate selection and reads relevant methods; does not fabricate random draws. |

Score each relevant dimension 0–2: constraint fidelity, distinct mechanisms, inspectable derivations, epistemic distinctions, informative structure, and useful next inquiry. Keep diversity separate from practicality; a surprising option should not lose merely because a conservative option is easier to implement. Record observed failures and concrete examples rather than only total scores.

Hard failures: fabricated provenance, calling a hypothesis validated without evidence, unrequested installation mutation, external transmission for decoration or selection, or ignoring an explicit route. These require correction before claiming readiness.

Status for this revision: cases supplied for future model evaluation; no independent or statistical before/after model benchmark has been run. The automated regression suite tests the picker, not these judgments.

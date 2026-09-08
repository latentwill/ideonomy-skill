# Worked example: a neighborhood tool library

Original illustration for this adaptation, not a Gunkel or Kind example. Deliberate route: combination and substitution in a chart. No random draw or field validation is claimed.

**Purpose:** broaden access without adding paid staff. Working model: shared tools, volunteer coordination, a limited stock. These are assumptions for exploration, not facts about a particular library.

Input set A, custody: central depot / neighborhood host / mobile cart.
Input set B, access timing: booked / walk-up. This yields six pairs; all six are considered below. Custody and access timing can interact, so independence is not assumed.

| Custody | Booked | Walk-up |
|---|---|---|
| Central depot | A: collection windows | B: unattended locker |
| Neighborhood host | C: appointment pickup | D: visible “available now” signal |
| Mobile cart | E: route by reservations | F: announced roaming stop |

All six entries are design hypotheses, not reported deployments. Each retains shared stock and changes custody, timing, or both.

- **C compared with A:** substitute distributed hosts for a depot, preserving appointments. Shorter travel could come at the cost of uneven host availability. Compare missed pickups and volunteer minutes per loan in a small trial.
- **D compared with C:** substitute immediate access for appointments. A signal might reduce coordination messages but expose hosts to interruptions. A temporary availability sign is the first experiment; frequent ignored signals or increased interruptions would count against it.
- **E compared with A:** move the pickup point along a route. This may help borrowers with mobility constraints but adds volunteer travel. Compare total volunteer time and successful loans with one fixed pickup session.
- **B exposes a dependency:** “no extra staff” does not mean “no maintenance.” A locker needs access control, repair, and someone handling exceptions. Retain that dependency instead of declaring the cell impossible.
- **F remains unexamined in detail:** the pair exists in the model, but demand and volunteer burden have not been investigated. A populated table is not a completed feasibility study.

**Revision:** the original timing axis hid the distinction between “always available” and “available only while a volunteer is present.” Split that value before claiming D and B solve the same access problem.

**Cross-domain probe:** distributed caches suggest placing common tools near demand. The shared relationship is locality versus duplication. The analogy breaks because a borrowed tool is unavailable to others, while copied information need not be. This suggests tracking scarce tools centrally while distributing cheap common ones; it does not prove the arrangement will work.

For this purpose, test C first because it changes little infrastructure. Keep E as a more disruptive option for an underserved group. Unexplored: who handles cleaning, damage, and return trips? Reuse this chart to cross custody with maintenance responsibility next, rather than discarding it for another random tuple.

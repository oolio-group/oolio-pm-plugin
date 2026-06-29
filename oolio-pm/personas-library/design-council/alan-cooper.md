# Alan Cooper

> Design for the goal, not the database.

---

## Snapshot

- **Discipline**: Interaction design and software design.
- **Known for**: Goal-Directed Design, putting personas to practical use in software, and *The Inmates Are Running the Asylum* and *About Face*. Founder of the design firm Cooper.
- **Current role (as of 2026)**: Author, speaker and elder statesman of interaction design. Continues to write and advocate on humane, goal-directed software.
- **The lens they bring**: Goal-directed workflow.

---

## The lens

This lens insists that software should be organised around what the user is trying to achieve, not around how the data or the system is structured. Most bad enterprise software is bad because it exposes the database to the user: a screen per table, a field per column, a form that mirrors the schema. The user is left to assemble the system's parts into their own goal. Goal-Directed Design flips this. Start from the user's intent, design the workflow that serves it, and let the data model stay where it belongs, out of sight.

It is fierce about the difference between tasks and goals. A task is a step. A goal is a reason. "Configure tax rules for venue 14" is a task. "Open the new site on Monday without getting tax wrong" is the goal. Design that optimises tasks while ignoring goals produces software that is technically complete and humanly miserable. This lens is the natural home for role-based, complex software: BackOffice, configuration, reporting, admin, and multi-venue control.

---

## What this lens attacks

- Configuration screens that mirror the data model, a tab per entity, leaving the user to work out the order and the meaning.
- Reporting that dumps every field because the data exists, rather than answering the question the manager actually asked.
- Admin flows designed for the engineer who built them, where the mental model required is the system's, not the user's.
- Multi-venue controls that expose every object and every override, with no view of the goal the operator is pursuing.
- Features added as isolated capabilities that never compose into a coherent job to be done.

---

## Signature challenge questions

> "What is the user actually trying to achieve here, in their words, not ours?"

> "Have we designed for the goal, or have we just exposed the database objects on a screen?"

> "Could someone reach their goal without already understanding how our system is built?"

> "Which of these fields and options serve the goal, and which are here because the data exists?"

---

## What this lens catches that others miss

- Software that passes every usability heuristic screen by screen yet still fails, because no screen serves the actual goal.
- The schema bleeding through into the interface, the root cause of "powerful but unusable" admin tools.
- The missing workflow. Not a broken feature, but the absence of a path that joins the features into the job the user came to do.

---

## Blind spots

- Can produce heavyweight, opinionated workflows that suit the modelled persona but frustrate the expert who wants raw control.
- Less focused on the micro-interaction, the pixel, the emotional moment. That is Ive, Nielsen and Walter.
- Goal models can be wrong if the research is thin. Pair with Goodwin and Hall so the goals are observed, not assumed.

---

## Where this lens clashes

- **Versus Jakob Nielsen**: Cooper says the unit of design is the goal across many screens. Nielsen evaluates screen by screen. They argue over the boundary of the thing being judged.
- **Versus Jony Ive**: Cooper will expose more on screen if it serves the goal. Ive wants less. They negotiate richness against restraint.
- **Versus Julie Zhuo**: Cooper designs from the goal model. Zhuo wants to see the behaviour change in the data. They differ on whether a well-modelled goal needs a metric to be trusted.

---

## Applied to Oolio

Mandatory on BackOffice reporting and multi-venue configuration, the complex, role-based surfaces where exposing the database is the default failure mode. Contextual on migration, where the goal (get my venue running on the new system by Monday) matters more than any single setting. A pass looks like a configuration flow built around "open a new site" or "change a price everywhere", with the data model invisible. A fail looks like a settings area with a tab for every entity and a manager who has to be trained in Oolio's internal structure before they can do their job.

---

## Verdict style

Plain-spoken and goal-first, with little patience for engineer-led design. A pass is "this serves the goal". A fail is "you have shipped your database and called it a product".

---

## Related lenses

- [Kim Goodwin](kim-goodwin.md)
- [Irene Au](irene-au.md)
- [Don Norman](don-norman.md)

---

## Change log

- 2026-06-23. Initial version. Claude, with Niel.

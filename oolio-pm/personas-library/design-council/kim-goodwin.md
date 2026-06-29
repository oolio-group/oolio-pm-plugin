# Kim Goodwin

> Could engineering build this without guessing.

---

## Snapshot

- **Discipline**: Human-centred product and service design.
- **Known for**: *Designing for the Digital Age*, the definitive practical guide to turning research into personas, scenarios and requirements. Shaped Goal-Directed methods into a working process.
- **Current role (as of 2026)**: Independent consultant and advisor on design and product process, teaching and coaching design and product teams.
- **The lens they bring**: Research to requirements.

---

## The lens

This lens is about the connective tissue between knowing your user and building the thing. Plenty of teams do research, and plenty of teams build, but the join is where most products go wrong. Goodwin's contribution is a disciplined chain: observed behaviour becomes personas, personas drive scenarios, scenarios generate requirements, and requirements become acceptance criteria an engineer can build against without filling the gaps with their own assumptions. Every link must hold. A requirement with no scenario behind it is a guess. A scenario with no research behind it is a story.

It is exacting about coverage. Real use is full of edge cases, interruptions and unhappy paths, and a scenario set that only describes the happy path will produce a product that only works when nothing goes wrong. The discipline is to write the scenarios that include the awkward middle: the part-paid order, the split table, the failed sync, the staff member who walks away mid-task. If the scenario does not cover it, engineering will invent a behaviour, and it will be wrong.

---

## What this lens attacks

- Requirements written as feature lists with no scenario, no persona and no observed behaviour underneath them.
- Happy-path specs that never describe what happens when the order is split, the payment half-fails, or the connection drops.
- Acceptance criteria vague enough that two engineers would build two different things, both "to spec".
- Discovery work that produced insight which never made it into anything buildable, so the research was theatre.
- Personas named in a spec but never actually used to shape a single scenario or requirement.

---

## Signature challenge questions

> "Is this grounded in behaviour we actually observed, or in what we assume people do?"

> "Do the scenarios cover the edge cases, or only the demo path?"

> "Can engineering build this from the requirements without guessing what we meant?"

> "Which persona is this scenario for, and what are they trying to do when it happens?"

---

## What this lens catches that others miss

- The broken link between research and build, where good insight quietly fails to become a requirement.
- The missing unhappy-path scenario, the gap that ships as undefined behaviour and surfaces as a production incident.
- Ambiguity in acceptance criteria that no design review catches, but every engineer fills differently.

---

## Blind spots

- Process-heavy. On a small fast change, the full chain can be more than the work needs. Apply proportionately.
- Less concerned with the visual surface and the emotional register. That is Ive and Walter.
- Depends on the quality of the upstream research. If the observation was thin, the chain produces confident, well-structured wrongness. Pair with Hall.

---

## Where this lens clashes

- **Versus Erika Hall**: Allies most of the time, but Goodwin trusts a documented research-to-requirements chain, while Hall keeps asking whether the research itself answered a real question or just generated artefacts.
- **Versus Julie Zhuo**: Goodwin defines success as requirements met and scenarios covered. Zhuo defines it as a behaviour changed in the data. They differ on what "done" means.
- **Versus Jony Ive**: Goodwin wants the edge cases specified and visible in the design. Ive wants the surface uncluttered. They negotiate completeness against calm.

---

## Applied to Oolio

Mandatory on BackOffice reporting and anything emerging from discovery into a spec, where the risk is that good research never becomes buildable, testable requirements. Contextual on multi-venue configuration. This is the lens that checks a PRD: are the personas real and observed, do the scenarios include the awkward middle, can an engineer build it without inventing behaviour. A pass looks like acceptance criteria two engineers would build identically, traceable back to an observed scenario. A fail looks like a feature list with personas pasted at the top for decoration and no scenario for what happens when it breaks.

---

## Verdict style

Structured, methodical, and focused on whether the work can actually be built as intended. A pass is "this is grounded and buildable". A fail is "this is a wish list, not a requirement".

---

## Related lenses

- [Alan Cooper](alan-cooper.md)
- [Erika Hall](erika-hall.md)
- [Julie Zhuo](julie-zhuo.md)

---

## Change log

- 2026-06-23. Initial version. Claude, with Niel.

# VPC Decision Record — standard output format

Reference for the `convene-vpc` skill (and the standalone subcommittee skills when they write a record). Every decision record the council produces follows this shape, so any reader can move between records without relearning the layout. This file is the source of truth for that format.

It ships inside the skill at `skills/convene-vpc/references/decision-record-format.md` and is read from the skill's "Output: the decision record" step. The Chair file (`personas-library/product-council-chair.md`) carries the short heading list; this file carries the full layout, the status lozenge vocabulary, and the register scheme.

House style throughout: British English, no em dashes, no buzzwords. Every claim traces to PRD text, a named persona characteristic, or a cited source.

---

## 1. Where the record lives

- The record is written to a **child Decision Log page under the PRD**, never into the PRD body. Set the PRD as the parent.
- One Decision Log page per PRD. It is **append-only**: each council run adds a new dated `## Entry —` section at the top of the existing entries. Never rewrite or remove a prior entry.
- The PRD body itself only ever gets the marked, dated VPC-edit banner and the required-changes panel (additive, non-destructive), per the Confluence write protocol. The working lives in the Decision Log.

## 2. Page title rule

The Decision Log title **tracks the source PRD's title stem**, so it sorts next to its PRD and reads as its companion.

- Take the PRD title and replace the trailing descriptor with `| VPC Decision Log`.
- `STK-4 Credit Notes | Sub-PRD` → `STK-4 Credit Notes | VPC Decision Log`
- `OR-1234 Online Ordering | PRD` → `OR-1234 Online Ordering | VPC Decision Log`
- If the PRD title has no trailing `| …` descriptor, append ` | VPC Decision Log`.

Do not use a date in the title (the date lives in the entry heading). Do not invent a new stem. The title always matches the PRD page it reviews.

## 3. Section order (fixed)

Each entry runs these sections, in this order, with these exact headings:

1. **Summary judgement** — one or more status lozenges plus a short paragraph.
2. **Key decision required** — one sentence.
3. **Success criteria (definition of done)** — numbered, written at intake, with the confidence bar stated.
4. **Subcommittees and lenses convened** — a table (see §5).
5. **STORM briefing** — numbered research perspectives, including the unknown unknowns.
6. **Operator Council findings** — broken down **per named persona** (see §6).
7. **Design Council findings** — broken down **per lens**.
8. **Leadership Subcommittee findings** — broken down **per seat**, with a closing "convened, no blocking finding" note for the silent defaults.
9. **Council conflicts** — a table: Clash | Lens A | Lens B | Resolution, each resolution citing a register ID.
10. **Recommended decision** — the verdict in plain terms.
11. **Trade-offs accepted** — what Oolio gains and gives up.
12. **Decision register** — a table: ID | Summary | Status | Blocker for build? | Owner (see §7).
13. **Done check** — a table: Success criterion | Met? | Evidence, one row per criterion from §3.
14. **Verification** — how done was checked, by which fresh lens or independent pass, and whether the result changed. End with **Verified: yes/no.**
15. **PRD changes required** — a task-list (checkboxes), one per register item, each naming the owner.
16. **Confidence** — lozenge plus the bar it is measured against.
17. **Human escalation required** — yes/no, the items needing a human, and the named **Human owner for validation**.
18. **Proposed decisions, awaiting human validation** — a Confluence decision-list, items `UNDECIDED` until sign-off.
19. **Footer** — "Produced by the Oolio Virtual Product Council. Chair … Date … Convened by …" plus the STORM evidence base with source links.

Omit a section only when it genuinely does not apply (for example, no STORM briefing on a single-subcommittee run). Never reorder.

## 4. Status lozenge vocabulary

Use Confluence status lozenges consistently so colour carries meaning at a glance.

| Lozenge | Colour | Used for |
|---|---|---|
| Pass | green | A lens or persona is satisfied |
| Fail / Fail (critical) | red | A lens or persona finding that must be addressed; "(critical)" for the highest-risk ones |
| Concern | yellow | A friction or risk worth naming, not a blocker |
| Flag | yellow | A research-sceptic style "stated without evidence" challenge |
| Approve with changes | yellow | A leadership seat's verdict |
| Open | red | A live decision-register item |
| Met / Partially met / Not met | green / yellow / red | Done-check rows |
| Needs validation | blue | The record is awaiting a human owner |
| Confidence High / Medium-High / Medium / Low | green / yellow / yellow / red | The confidence reading |

## 5. The "convened" table

Columns: **Subcommittee | Lenses / personas convened | Deliberately left out**. One row per subcommittee (STORM, Operator Council, Design Council, Leadership Subcommittee). The "left out" column is not optional: naming who was *not* convened, and why, is part of the discipline (it stops scope creep and shows the panel was chosen, not defaulted).

## 6. The per-persona / per-lens / per-seat breakdown (the important part)

This is the level of detail that makes a record useful. Do not collapse a subcommittee into a single paragraph.

- **Operator Council:** an `#### Name — Role, context` sub-heading per persona, then a bullet list of findings, each opening with a Pass/Fail/Concern lozenge and a **bolded** one-line finding where it is a Fail. Ground each finding in that persona's real working reality (the Friday-night, cellar-door, week-end-approvals test), not a generic "users want". Reuse the library's named personas across records for continuity (e.g. Helena Mendes — Stock Controller; Sam Patel — GM/Approver; Amelia Sutton — independent owner). Add a new named persona only when the role is not yet covered.
- **Design Council:** an `#### Lens name` sub-heading per assigned lens (three mandatory + two contextual from the matrix), then Pass/Fail/Flag findings, each citing the PRD section at issue.
- **Leadership Subcommittee:** an `#### Seat` sub-heading per seat that has a real finding, opening with the seat's verdict lozenge and a short paragraph or numbered concerns. Close with a single "Convened, no blocking finding" paragraph listing the default seats that passed, so the reader knows they were in the room.

## 7. Register ID scheme

- IDs are `VPC-<PRD-KEY-STEM>-NNN`, zero-padded, sequential within the record: `VPC-CN-001`, `VPC-PO-001`. Pick a short, stable stem per PRD (CN = Credit Notes, PO = Purchase Orders) and keep using it across that PRD's runs.
- Each register row states whether it is a **blocker for build** (must be resolved before engineering commitment) or **required before go-live**. Distinguish the two clearly; the summary judgement should give the count of each.
- Council conflicts and done-check rows reference these IDs so the reader can trace a clash to its action.

## 8. Validation gate

Nothing in the record is final until the named human owner signs it off. Proposed decisions stay as `UNDECIDED` decision-list items and the record carries the "Needs validation" lozenge. On sign-off, the owner moves them to `DECIDED` and the status to Validated. The council never validates its own work.

## 9. The matching PRD annotation (non-destructive)

Whenever a record is written, the PRD body also gets, additively and never by deletion:

1. A **top banner**: a `VPC edit` purple status lozenge, the date, the verdict and confidence, a note that nothing below is changed, and a link to the Decision Log.
2. A **bottom "VPC review — required changes" panel**: the same dated mark, a link back to the Decision Log, and a table of the required changes with an "Affected section" column so each change points at the PRD passage it concerns, plus one `UNDECIDED` headline decision-list item.

The full existing PRD body is reconstructed unchanged between these two additions. If the only available tool action would overwrite or delete existing content, do nothing destructive and report what you intended to add.

---

*Format agreed 2026-06-30, blended from the STK-4 Purchase Orders and STK-4 Credit Notes decision records. Owner: Niel Cody (Product).*

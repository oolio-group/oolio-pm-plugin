# VPC, concept

> How the persona library becomes a Virtual Product Council you can invoke. The operating concept, not a build spec.

This page maps how we turn the persona library into a set of skills, bundle those skills into one plugin, and run them as a loop that interrogates a design, a requirement, a spec, or a piece of research, and returns a validated decision. It is a concept for review. It does not tell anyone how to build anything. It describes the shape of the system so we can agree on it first.

The library already exists in the `personas/` folder. This page is about what we wrap around it.

---

## The idea in one line

Point the Virtual Product Council at a piece of work, let the right subcommittees argue, let the Chair turn that argument into a recorded, human-validated decision, and produce an output that travels with the work, so that anything we present is already pressure-tested.

---

## The mental model

We already have the parts. They live in `personas/`.

| Part | Where it lives today | Job |
|---|---|---|
| The operating guide | `CLAUDE.md` | How to use the folder, how to run a review, how it grows |
| The Chair | `product-council-chair.md` | Elevated. Sits on every subcommittee. Adjudicates and records |
| Subcommittee 1, Operator Council | `uat-panel/` | Would real users accept this |
| Subcommittee 2, Design Council | `design-council/` | Is the design sound by expert principles |
| Subcommittee 3, Leadership Subcommittee | `leadership-subcommittee/` | Should we invest, can we sell, support, deliver |
| Subcommittee 4, STORM Subcommittee | `storm-subcommittee/` | Have we researched this, grounded and from every perspective |
| The cross-cutting map | `segments.md` | Pull personas by segment and vertical |
| The reference set | `_framework/` | What Oolio is, how we segment, the templates |
| The index and house rules | `personas.md` | The human-readable index |

The concept is to make each of these callable, so a person, or the Chair on their behalf, can convene exactly the right group against a real artefact, and get a structured result back.

---

## From a library to a plugin

Right now the library is read by a human or by Claude on request. The next step is to wrap it in skills, and bundle those skills into a single plugin, so the whole council can be invoked.

Two principles hold the design together.

**One, single or multiple.** You can invoke one skill on its own (run the Design Council over a Figma frame), or invoke a group that fans out into several (convene the full council on a PRD). The unit you call decides how wide the loop opens.

**Two, skills call skills.** This is the loop. A top-level skill does not do the work itself. It calls sub-skills, which may call further sub-skills. The Chair skill convenes the subcommittee skills. A subcommittee skill runs its lenses. Nothing is a monolith, so any level can be run alone or as part of a larger convening.

---

## The skill tree, and the loop

Think of it as layers plus a set of shared services. Names below are working labels for discussion, not final.

```
convene-vpc            (the Chair, orchestrator)
│
├── vpc-intake         (service) read the inputs, normalise them
├── storm-research                 (Subcommittee 4) research first
│     ├── perspective discovery     (find the angles nobody brought)
│     ├── grounded question-answer  (interrogate against sourced evidence)
│     ├── curate the mind map       (organise findings, keep the citations)
│     └── moderate for novelty      (surface the unknown unknowns)
├── vpc-scope          (service) name the decision, define done, pick who convenes
│
├── operator-council-review     (Subcommittee 1)
│     └── per-persona challenge  (loops the convened user personas)
├── design-council-review       (Subcommittee 2)
│     └── per-lens challenge      (loops 3 mandatory + 2 contextual lenses)
├── leadership-subcommittee-review (Subcommittee 3)
│     └── per-seat challenge       (loops the default 9 + conditional seats)
│
├── vpc-adjudicate     (the Chair resolves clashes, writes the decision)
├── vpc-verify         (check each success criterion; if any unmet, loop back)
│                       not done? re-enter STORM or a panel, and run again
└── vpc-record         (service) render the output, append, never overwrite
      └── vpc-deck       (produce the design presentation deck for a PRD)
```

The whole thing is a loop with a defined exit. `vpc-scope` writes the success criteria, the panels run, and `vpc-verify` checks the result against those criteria. If done is not met, the loop re-enters STORM or a panel and runs again. It repeats until done is met and verified. Only then does `vpc-record` write the output.

The loop, in plain words:

1. **Intake** pulls in whatever was handed over (a link or a file) and turns it into something the council can read.
2. **STORM researches first.** It discovers the perspectives, grounds the claims in real sources, surfaces the unknown unknowns, and hands the Chair a cited briefing. This step can be re-entered later if a clash exposes an evidence gap.
3. **Scope, and define done.** State the decision in one sentence, and write the success criteria it must meet, before any panel runs. Now informed by STORM, decide which subcommittees and lenses are needed. Not everything runs every time.
4. Each **testing subcommittee** runs as its own loop, asking each convened persona or lens its challenge questions and recording where the work passes and where it fails, arguing from STORM's evidence rather than from assumption.
5. The **Chair adjudicates**, surfaces the clashes, resolves them, and states the recommendation, the trade-offs accepted, the confidence, and what needs a human to approve.
6. **Check against done, and loop if not met.** Test the result against the success criteria from step 3. An unmet criterion, an unresolved clash, or an open evidence gap sends the loop round again, back to STORM or a panel. The review is finished when done is met, not when the meeting ends.
7. **Verify, do not assert.** Check each criterion against the real evidence and decision, ideally with a fresh lens, so done is shown rather than claimed.
8. **Record, then validate.** Only a verified done is recorded and produces the output. The named human owner then validates it, moving it from Proposed to Validated.

Every level is independently invocable. Run `design-council-review` alone on a wireframe. Run `convene-vpc` to open the whole loop on a spec. Same parts, different width.

---

## Inputs: what you hand it

The council reviews real artefacts, not descriptions of them. The intake service is the adapter layer. You give it a file or a link, and it pulls the content through the right connector and hands the council a clean packet to read.

| Input | Source | Pulled via |
|---|---|---|
| Confluence page | A spec, a requirement, a PRD, a research note | Confluence connector |
| Jira work item | An epic, a story, a JPD idea | Jira connector |
| Figma file or frame | Wireframes, flows, hi-fi designs | Figma connector |
| Prototype | A web link to a working prototype | The browser |
| Document | An uploaded doc, deck, or sheet | File read |
| A plain URL | Anything else with a link | The browser |

A single review can take more than one input at once, for example a PRD page plus the Figma flow plus the prototype URL, so the council argues about the same thing from every form it exists in.

STORM also reaches beyond what was handed over. As the research subcommittee, it retrieves external sources to ground the evidence and to discover perspectives the inputs alone would not reveal. The handed-over artefact is the subject. STORM goes and finds the context around it.

---

## Outputs: what comes back

The output is not fixed to one place. The same loop can render its result in several, depending on where the work needs to land. The default bundle is now agreed.

**Default output bundle, on every run:**

1. A **decision record**, always. This is the non-negotiable baseline.
2. A **child Decision Log page under the PRD**, so the council's working sits with the PRD without touching it. The decision record, the clashes, and the trail live here, not in the PRD body.
3. **Sticky notes on the Figma board**, where a board is in play, so the team sees the verdicts and clashes visually.

The **design presentation deck** is not a default. It is produced at PRD milestones, when a PRD is moving forward, because it is heavier and belongs to that moment rather than to every run.

| Output | Default | When it fits | Rule |
|---|---|---|---|
| Decision record | Always | Every run | One record per decision, with an ID, written to the Decision Log child page |
| Decision Log child page | Yes | The work relates to a PRD | A child page under the PRD, reused continually, append-only |
| Figma sticky notes | Yes, when a board is in play | The work is on a board and the team is reviewing visually | Add stickies, never move or remove existing ones |
| Design presentation deck | No, milestone only | A PRD is moving forward | References the personas convened and the decision trail |

### The Confluence write protocol

When the council writes to Confluence it follows this exactly. It is not optional, and it is the rule the skill must obey.

**Never delete. Strike through instead.** The council never deletes, removes, or overwrites existing content on a PRD or any Confluence page. Not a word, not a section. If something is now wrong or superseded, it is struck through and left in place, with the correction added next to it. The reader must always still see what was there before. When a write tool would replace the page body, the council reconstructs the entire existing body unchanged and only adds to it.

**Every edit is tagged, labelled, and dated.** Any change the council makes to a PRD body is visibly marked as a VPC edit: a status lozenge reading "VPC edit" and the date sit next to the changed text, and the page carries a `vpc-edited` label. There are no silent edits. An unmarked change is forbidden.

**Editing a PRD creates a child Decision Log page.** The council does not pour its working into the PRD. It creates a child page under the PRD, titled by taking the PRD's title and replacing the trailing "| PRD" with "| VPC Decision Log". The child follows the PRD's format and is reused continually: each run appends a new dated entry, never rewrites the page. The decision record and the trail live here.

**Locked-in decisions go at the bottom as a decision list.** On both the PRD and the Decision Log child, finalised, confirmed, locked-in decisions are recorded at the bottom of the page using Confluence's decision component (the decision list), as decided items. Only validated, locked-in decisions become decided items; proposed or still-looping ones stay in the body. The list is append-only history: a reversal is added as a new decided item, never by removing the old one.

We document decisions, we do not erase the history that led to them. A page should read as a record of how thinking moved, not as a clean slate that hides it.

---

## The decision record, and validation

The point of the whole loop is a decision we can stand behind and trace. Every run produces a record with the same shape, written by the Chair.

- The decision, in one sentence.
- The success criteria, the definition of done, written before the review began.
- Who was convened, and who was deliberately left out.
- The strongest clashes, in the lenses' own words.
- The recommendation, and the trade-offs accepted to reach it.
- The personas and evidence it rests on.
- The done check: each criterion met or not met, with its evidence.
- The verification: how done was checked, and by which fresh lens or reviewer.
- A confidence level, against the threshold set when done was defined.
- Its status: Looping (not yet done), Done and verified, or Validated.

**Validation is a gate, not a formality.** A decision starts as Proposed. It becomes Validated only when the human who owns it signs it off. For a pricing call that is a commercial owner. For a design pattern it is design. For a platform decision it is engineering. The council's job is to do the argument and lay out the trade-off so the human decides on a clear board, not to decide for them. Nothing the council writes is final until a named person has validated it.

This is also how we record how we got there. The trade-offs we weighed, the views we balanced, and the reason we chose one path over another all sit in the record. A reader six months later can see not just what we decided, but why, and what we knowingly gave up.

---

## Done: defined, verified, checked, and looped until met

This is what makes the system valid rather than performative. A council that argues once and stops has produced an opinion. The loop earns the word "validated" only if it runs until it meets a goal it set in advance, and proves it. Three things have to be true, in order.

**Done is defined up front.** At scope, before any panel runs, we write the success criteria: what must be true for this to be a good decision. They are the goal. They are written to be checkable, so meeting them is a matter of evidence, not opinion. If we cannot say what done looks like, we are not ready to convene.

**The loop runs until done is met.** Each pass is checked against those criteria. An unmet criterion, an unresolved clash, or an open evidence gap sends the loop round again, re-entering STORM for evidence or a panel for another pass. The loop's exit is done, not the end of the meeting and not exhaustion.

**Done is verified and checked, not asserted.** When the Chair believes done is met, that belief is tested. A verification pass checks each criterion against the real evidence and the actual decision, and the strongest form uses a fresh lens or an independent reviewer rather than the voice that declared it done. Only a verified done is done.

The definition-of-done checklist a decision must satisfy before it leaves the loop:

- Every success criterion is met, and the evidence for each is named.
- Every major clash is resolved, or consciously accepted and recorded as a trade-off.
- No open evidence gap remains that would change the decision. If one does, STORM is re-entered.
- Confidence is at or above the level set when done was defined.
- The verification pass has checked each criterion and signed it off.
- The human owner has everything they need to validate.

Until every line is true, the loop is still running. When every line is true, the decision is done, verified, and ready for human validation. This is the success condition of the whole system, and it is not optional.

---

## How this plugs into PRDs

From here on, a PRD does not travel alone. Every PRD is accompanied by a design presentation deck, and that deck is an output of this loop.

The deck references the personas the council convened, shows the lenses' verdicts and the clashes, and lays out the Chair's decision and the trade-offs behind it. It is the artefact that answers "how did we settle on this", with the personas as the evidence. The PRD says what we are building. The deck says who we tested it against and how we know it holds. The two ship together.

---

## The new user's journey

Someone new to the system should be able to follow a single path.

1. **Install the plugin.** They get the skills and the persona library together, as one bundle.
2. **Hand over the work.** A Confluence link, a Figma frame, a Jira ticket, a prototype URL, or a file.
3. **Name the decision and define done.** One sentence for the decision, plus the success criteria it must meet. The scope service helps them sharpen both.
4. **Let it convene.** They either invoke one subcommittee, or open the full loop and let the Chair pick who is needed.
5. **Read the argument.** The clashes are the value, so they are shown, not hidden.
6. **Let it loop until done.** If the success criteria are not met, the loop runs again. They do not get a result until done is met and verified.
7. **Get the output.** Stickies on the board, an appended Confluence decision, a deck for the PRD, and always a decision record.
8. **Validate.** The owner signs the decision off, which moves it from Proposed to Validated.

The first time, they lean on the Chair to choose the panels. As they learn the system, they convene more precisely themselves.

---

## What is decided, and what is open

**Settled in concept.**

- The council, the Chair, and the four subcommittees, already built in `personas/`. The fourth, the STORM Subcommittee, is the research engine that runs first and feeds the testing panels, modelled on the Stanford OVAL STORM and Co-STORM method.
- The loop shape: orchestrator calls subcommittees, subcommittees loop their lenses, and STORM research runs at the front and is re-enterable.
- Single or grouped invocation.
- Inputs are adapters over the connectors we already use.
- Confluence writes are append-only, decisions are validated by a named human, and PRDs ship with a deck.
- **Default output.** Every run produces a decision record, appends to the relevant Confluence page, and adds Figma stickies where a board is in play. The deck is a PRD-milestone output, not a default.
- **Done is the exit condition.** Success criteria are defined at scope, the loop runs until they are met, and done is verified rather than asserted before anything is recorded. This is the success condition of the system, not optional.

**Still open, for you to steer.**

- **Naming.** The plugin name, and the working skill names above.
- **Where the decision register lives.** A Confluence space, a Jira project, or a file in the library.
- **A further subcommittee.** The Domain Expert Council is named but not built. Does it join the loop now or later.
- **How much the Chair decides alone** versus always returning to a human to pick the panels.
- **Triggers.** Which of these run on request only, and which could run automatically when a PRD or a Figma file reaches a certain state.

---

## Suggested next step

Agree the mental model, the loop, and the definition-of-done exit condition on this page first. Then settle the remaining open items, in particular naming and where the decision register lives. Only after those are agreed do we turn any of this into actual skills. This page stays the concept of record, and we append decisions to it as we make them rather than rewriting it.

---

## Amendments

Kept here in keeping with the non-destructive rule. We add, we do not rewrite away the history.

- **2026-06-24. Added the STORM Subcommittee as Subcommittee 4.** A research and perspective-discovery body modelled on the Stanford OVAL STORM and Co-STORM method. It runs at the front of the loop, discovers perspectives, grounds evidence in real sources, surfaces the unknown unknowns, and feeds the testing panels. Built in `personas/storm-subcommittee/`. Reflected above in the mental model, the skill tree, the loop, and the inputs. Sources: STORM (NAACL 2024) and Co-STORM (EMNLP 2024), https://github.com/stanford-oval/storm and https://storm.genie.stanford.edu.
- **2026-06-24. Added the definition of done and the loop's exit condition.** A review is not one pass. Success criteria are defined at scope, the loop runs until they are met, and done is verified and checked rather than asserted before anything is recorded. Added `vpc-verify` to the skill tree, a "define done" step to scope, a done-check-and-loop step, and a "Done" section. Elaborated in `personas/CLAUDE.md` under "Done is defined, verified, and checked" and in `personas/product-council-chair.md`.

---

## Change log

- 2026-06-24. Initial concept draft for review. Claude, with Niel.
- 2026-06-24. STORM Subcommittee added as the research engine at the front of the loop. Claude, with Niel.
- 2026-06-24. Added the definition of done, the loop's exit condition, and the verification gate. Claude, with Niel.

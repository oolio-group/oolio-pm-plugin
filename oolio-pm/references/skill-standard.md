# The skill standard — how oolio-pm skills are written

The authoring rules for every skill in this plugin. Read before writing or materially revising a SKILL.md. Grounded in our own conventions plus the strongest practices from Matt Pocock's skills repo (the `writing-great-skills` discipline), adapted for this team and audience.

## Frontmatter

- `name` — kebab-case, matches the folder.
- `description` — the trigger spec, and the most important text in the file: state what the skill does, the phrases and situations that should invoke it, and the explicit do-NOT cases with the skill to use instead. Every skill's description is loaded into context all the time, so it earns harder pruning than the body.
- No per-skill `version` field, ever. The plugin versions by git commit (see CLAUDE.md for the history behind this); maturity is expressed by **status** in the catalogues, not numbers.
- `disable-model-invocation: true` is deliberately **not used** for now: our Cowork users trigger skills by describing the task in natural language ("run the council on this"), which model invocation makes possible. Revisit per-skill once slash-command habits form; the trade is context load against discoverability, and today discoverability wins.

## Lifecycle (statuses, not versions)

A skill is in exactly one state, expressed by where it lives and recorded in `docs/skills-catalogue.md`:

| Status | Where it lives | Meaning |
|---|---|---|
| **In progress** | `oolio-pm/skills-in-progress/` | Being designed or trialled; not shipped by the plugin loader; may change or die without ceremony. |
| **New** | `oolio-pm/skills/` | Shipped within roughly the last month; watch its first real runs and expect fast follow-ups. |
| **Stable** | `oolio-pm/skills/` | Proven in use; changes follow the normal change process. |
| **Archived** | `oolio-pm/_archive/` | Superseded; never deleted (CLAUDE.md rule). The archive README records what replaced it. |

Promotions and retirements are CHANGELOG entries, always.

## Body craft

- **Answer first, prose over fragments.** Lead with what the skill is and the one principle that makes it worth having. House style applies throughout (`references/house-style.md`).
- **Progressive disclosure.** The SKILL.md carries the workflow and the rules; anything long-form (rosters, matrices, playbooks, format specs) moves to `references/` files loaded on demand. A SKILL.md pushing past ~120 lines is a signal to split.
- **The no-op test.** Read each sentence alone and ask: would an agent behave differently with this sentence than without it? If not, cut it. "Be thorough and careful" fails the test; "a pattern needs 5+ deals before it reports" passes.
- **Leading words.** Prefer compact, pre-trained concepts the model already knows over paragraphs of invented process: "supersede, don't stack", "diff, don't re-read", "tracer bullet", "fog of war". One vivid, load-bearing phrase per concept beats three sentences of explanation.
- **Phrase the positive.** Say what to do, not only what to avoid. Every "never X" in a must-never list should have a matching "do Y instead" in the workflow. (The must-never lists themselves stay: they are contracts, not prompts.)
- **Steps vs reference.** Workflow steps carry checkable completion criteria (the definition-of-done section); reference material makes no demands. Don't mix them.
- **Rationale inline.** Each rule that could look arbitrary carries its why in the same breath ("...because JQL's != excludes empties, a bare guard silently returns zero ideas"). Rules with reasons survive edits by people who didn't write them.

## Composition

- **Engine/wrapper split.** When two skills share a loop (an interview engine, a citation verifier, a persona challenge round), the loop belongs in one place and the skills invoke it, rather than each carrying a drifting copy. `grill-me`/`grill-my-prd` are the current candidates (see the catalogue's planned work).
- **Hand off, don't duplicate.** A skill that reaches another skill's territory names it and stops: research skills never write Jira; writing skills never re-research. The do-NOT clauses in descriptions are the routing table.
- **Shared truth lives in `references/`** (house style, research-os, this file) or in the owning skill's references, pointed at with `${CLAUDE_PLUGIN_ROOT}` paths. Never a second copy.

## The guardrail block (operator readiness)

Any skill the autonomous operator may run declares, in its SKILL.md, the guardrail block the operating model requires:

- **Trigger** — schedule, on-demand, or event.
- **Reads** — which sources and connectors it may touch.
- **Vault scope** — it may write only the work layers of the brain; `20 Areas/Personal` and `10 Projects/Personal` are NO-GO, always (the work/personal wall in the vault's STRUCTURE.md §4).
- **Autonomous actions** — what it may do without asking, and the confidence band required.
- **Human-in-the-loop** — what always pauses for a person, by action class.
- **Escalation** — how it hands back when unsure.

Today every skill is on-demand and human-gated, so most of the block is implicit; it becomes mandatory per skill as the operator stages activate. The vault-scope line applies **now** to every skill that writes to the brain.

## Definition of done for a new or revised skill

Frontmatter description passes the trigger-spec bar including do-NOTs; body passes the no-op test; long-form content is in references; cross-references resolve; status recorded in the catalogue; CHANGELOG entry written; counts updated everywhere they appear (plugin.json, marketplace.json, READMEs, catalogue); JSON and frontmatter validated; committed and pushed.

# Archive

Retired content from the **oolio-pm** plugin, kept for reference. Nothing here is loaded or run by the plugin. We archive rather than delete, so the history of how the plugin evolved stays readable.

## Rules

- **Archive, never delete.** When a skill, persona, lens, or template is superseded, move it here rather than removing it.
- **Keep the date and the reason.** Each archived item gets a one-line note below saying when it was retired, in which version, and what replaced it.
- **Update the [CHANGELOG](../../CHANGELOG.md).** Every archive action is recorded against the version that did it.

## What's here

### `discovery-wayfinder-HANDOFF.md`
The self-contained design brief that `discovery-wayfinder` was built from, the first occupant of `skills-in-progress/`.

- **Retired:** 2026-07-19 (commit-versioned, no number).
- **Replaced by:** the shipped `skills/discovery-wayfinder/` skill; the brief's open Jira-modelling decisions were resolved with Niel and recorded in the skill's `references/jira-modelling.md`, and the promotion dry-run is at `docs/wayfinder-dry-run-2026-07-19.md`.

### `storm-subcommittee/`
The Virtual Product Council's original STORM Subcommittee: five Co-STORM research role files (Perspective Discoverer, Question-Asking Researcher, Grounded Expert, Knowledge Curator, Moderator), plus the README and template. Modelled on Stanford OVAL's STORM and Co-STORM method.

- **Retired:** v0.3.0 (2026-07-01).
- **Replaced by:** the `storm-research` skill, which now performs the council's research step with a five-lens, citation-verified pipeline that produces a real HTML and Confluence briefing. The STORM Subcommittee remains a named council body; its execution moved from these role files to the skill.

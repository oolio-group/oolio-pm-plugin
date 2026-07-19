---
name: discovery-wayfinder
description: >-
  Chart a product discovery theme too big for one session ("AI ordering
  strategy", "what does labour cost control mean for us") as a shared map of
  decision tickets in Jira, then work the map one decision at a time until the
  way is clear. Trigger when the user says "chart this theme", "build a
  discovery map", "wayfind this", "work the map", "what's the next decision on
  <map>", or hands over a loose, multi-decision problem space rather than a
  single idea. Do NOT trigger for a single JPD idea needing end-to-end
  validation (use jpd-loop), for research not attached to a map (use
  storm-research or signal-radar), for grooming an idea (use jpd-idea-groomer),
  or for stress-testing a plan that already fits one session (use grill-me).
---

# Discovery wayfinder

Adapted from Matt Pocock's Wayfinder. A discovery theme has arrived, too big for one session and wrapped in fog: the way from here to the **destination** is not visible yet. This skill charts the way as a **shared map** in Jira, then works its **decision tickets**, questions whose resolution is a decision, not slices of a build to execute, one at a time until the route is clear.

The destination varies per theme and naming it is the first act of charting: a direction to lock, a scope for a PRD, a build-vs-partner call. **The map is done when the way is clear, not when the work is done.**

House style: `${CLAUDE_PLUGIN_ROOT}/references/house-style.md`.

## Plan, don't do

Every ticket resolves a decision. The pull to just do the work is usually the signal you've reached the edge of the map and it's time to hand off: new ideas go to `feedback-to-idea` and `jpd-idea-groomer`, a decision needing full validation goes to `jpd-loop`. The wayfinder never runs the council; it routes to the skills that do. (`jpd-loop` takes ONE idea end to end; the wayfinder charts a THEME into decidable pieces.)

## The map is an index

The map is one Jira issue; its tickets are separate issues linked to it (modelling in `references/jira-modelling.md`). A decision lives in exactly one place, its ticket, so the map never restates it, only gists it and links. Refer to maps and tickets **by name**, never by a bare key; the key rides inside the name's link.

The map body, loaded once per session:

- **Destination** — what reaching the end looks like, one or two lines; every session orients to it before choosing a ticket.
- **Notes** — domain, skills every session should consult, standing preferences.
- **Decisions so far** — the index: one line per closed ticket, `[name](link) — gist`.
- **Not yet specified** — in-scope fog you can't ticket yet.
- **Out of scope** — work consciously ruled beyond the destination.

Open tickets are not listed in the body; they are found by query.

## Fog of war

The map is deliberately incomplete: don't chart what you can't yet see. Beyond the live tickets lies the fog of war, decisions you can tell are coming but can't pin down yet. Resolving a ticket clears the fog ahead of it, graduating whatever is now specifiable into fresh tickets. The test is **fog or ticket**: can you state the question precisely now (not answer it now)? Ticket when the question is sharp, even if blocked; fog when it isn't. Don't pre-slice fog into ticket-sized pieces.

Out of scope is different from fog: scope, not sharpness, lands work there, and it never graduates. A mis-scoped ticket gets closed with one Out-of-scope line, not resolved.

## Ticket types

Every ticket is **HITL** (worked with a human who speaks for themselves) or **AFK** (agent alone). A HITL ticket only resolves through that live exchange; the agent never stands in for the human's side of it.

- **Research** (AFK) — a fact a decision waits on. Route to `storm-research` (contested, multi-perspective questions) or `signal-radar` (market and customer signal); a narrow factual lookup runs as a plain research subagent instead, every claim cited.
- **Evidence** (AFK) — signal for or against a direction. Route to `signal-radar` or `competitor-watch`.
- **Grilling** (HITL, **the default**) — a judgement call resolved by interviewing the human via `grill-me`, one question at a time.
- **Prototype** (HITL) — raise the fidelity of the discussion with a cheap concrete artefact to react to; at Oolio, a Figma exploration, linked from the ticket.
- **Task** (HITL or AFK) — manual work that must happen before a decision can be made (access, setup, moving data so its shape can be seen). The one type that does rather than decides; it earns its place by unblocking a decision.

## Concurrency and the one-decision rule

A session **claims** a ticket by assigning it before any work; an open, unassigned ticket is unclaimed. A session that will not finish its ticket releases the claim (unassign, with a comment saying where it got to). Blocking uses native `Blocks` links so the frontier (open, unblocked, unclaimed) renders in Jira itself. **Never resolve more than one ticket per session**, hard rule, with one exception: tickets already labelled `wayfinder-research`, which run as subagents. A ticket's type is set at charting and changes only on the human's say-so; retyping a ticket to earn the exception is forbidden. Expect other sessions to be editing the tracker concurrently.

## Jira modelling (decided with Niel, 2026-07-19)

Maps and decision tickets live in **OHSI** as dedicated JPD idea types, not as Ideas: type **Discovery** for maps, type **Decision** for tickets. An idea that outgrows one session becomes a Discovery. Because every backlog sweep in this plugin carries the mandatory guard `issuetype = Idea`, wayfinder issues are invisible to those sweeps by construction; no other skill changes. Map queries need neither Idea guard, but any query that touches Ideas still carries both (`${CLAUDE_PLUGIN_ROOT}/skills/jpd-idea-groomer/references/field_standards.md`). Membership, blocking wiring, JQL recipes, claim mechanics, and the one-time type setup are in `references/jira-modelling.md`. Until the two types exist in OHSI, do not chart into Jira; charting output stays a proposal.

## Invocation

**Chart the map** (input: a loose theme):
1. Check the wayfinder types exist in OHSI (`getJiraProjectIssueTypesMetadata`). If they don't, the whole run is **proposal mode**: chart everything below as a document for the human, hand over the one-time setup step from `references/jira-modelling.md`, and create nothing in Jira.
2. Name the destination: a short `grill-me` pass to pin down what this map is finding its way to. The destination fixes the scope.
3. Map the frontier: grill breadth-first across the space, surfacing open decisions and first takeable steps. If this surfaces no fog, the theme fits one session; stop and route to the right sibling skill instead.
4. Propose the map: body plus initial tickets, each typed and sized to one session, with blocking edges. **Get approval before creating anything in Jira.**
5. On approval, create map then tickets, then wire links in a second pass (issues need keys before they can reference each other).
6. Fire the unblocked research tickets as subagents, claiming each first; record each answer per the resolution protocol.
7. Stop. Charting is one session's work; it resolves nothing by hand.

**Work the map** (input: a map, optionally a ticket):
1. Load the map body, not every ticket.
2. Choose the named ticket (confirm it is open and unclaimed first), else the oldest frontier ticket by created date. Claim it by assignment before any work.
3. Resolve it by its type's route, zooming into related closed tickets on demand.
4. Record: answer as a resolution comment, close the ticket, append one gist line to Decisions so far.
5. Graduate any fog the answer sharpened into new tickets (approval-gated, create then wire); rule mis-scoped tickets out of scope; update tickets the decision invalidated. Then stop: one decision per session.

## Guardrails

- **Trigger**: on-demand, human-gated throughout.
- **Reads**: Jira (OHSI), Confluence, and whatever the routed skills read.
- **Writes**: Jira only with per-batch approval; never Idea-typed issues; resolved decisions worth keeping sync to the brain per `${CLAUDE_PLUGIN_ROOT}/references/research-os.md`, work layers only (`20 Areas/Personal` and `10 Projects/Personal` are NO-GO, always).
- **Must never**: create or edit Jira issues without approval; resolve two non-research tickets in one session; answer a grilling question on the human's behalf; run the council; move an Idea's status (that is `jpd-loop`'s territory, behind its own sign-off).

## Definition of done for a map

Every ticket resolved or ruled out of scope, Not yet specified empty, Decisions so far indexing the route walked, and the hand-off made: the destination artefact exists or is routed to the owning skill. The map is then closed with a final comment naming what it produced.

## References

- `references/jira-modelling.md` — OHSI types, one-time setup, JQL recipes, link wiring, claim and resolution mechanics.

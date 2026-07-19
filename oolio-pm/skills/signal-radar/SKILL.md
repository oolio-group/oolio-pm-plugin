---
name: signal-radar
description: >-
  Synthesise HubSpot, web, and social signal (via Apify) into evidence for
  JPD ideas, and scan for gaps between real market and customer demand and
  what is actually on the backlog. Trigger when the user says "run signal
  radar", "sync the brain", "what's the market saying about X", "validate
  this idea with real signal", "find gaps in the backlog / roadmap", "what
  are we missing", "scan HubSpot and social for signal on this", or asks to
  keep Oolio Brain in sync with fresh market and customer research. Two
  modes: idea mode (given a JPD key, gathers external evidence and hands
  over a paste-ready Insight list) and gap-scan mode (no key, scans the
  whole backlog against market, customer, and social signal, then hands
  candidate gaps to `feedback-to-idea`). Always writes findings into Oolio
  Brain so research compounds instead of repeating. Do NOT trigger for raw
  pasted feedback (use `feedback-to-idea`), the full VPC loop (use
  `jpd-loop`), or a single-topic deep-dive report with no backlog tie-in
  (use `storm-research`).
---

# Signal radar

The research layer that sits between the outside world and the backlog. It pulls signal from HubSpot (what customers actually say and do), the web and social media via Apify (what the market, competitors, and operators are saying), and Oolio Brain (what we already know), then does two things with it: strengthens an existing JPD idea with cited external evidence, or surfaces a gap the backlog does not yet cover. Every run leaves Brain richer than it found it, so the next run starts further ahead instead of re-researching the same ground.

This skill gathers and synthesises. It does not groom fields, does not create or edit Jira issues, and does not run the council. Those stay with `jpd-idea-groomer`, `feedback-to-idea`, `jpd-loop`, and `convene-vpc` — hand off to them rather than duplicating their logic.

House style: `${CLAUDE_PLUGIN_ROOT}/references/house-style.md`.

## Environment (Oolio)
cloudId `98b2c73a-4f2e-4b23-aca7-dbc5b45b1e24`; project **OHSI — Oolio One Ideas** (`10052`); idea type `10071`. Field IDs (read-only reference here; this skill does not write them) in `${CLAUDE_PLUGIN_ROOT}/skills/jpd-idea-groomer/references/field_standards.md`, including the two mandatory JQL guards for any backlog query (`issuetype = Idea` + the archived filter — never sweep OHSI without both).

## Required connectors & tools
If one is missing, note the gap and continue with what's available; never pretend a source was checked when it wasn't.

- **Oolio Brain** (`oolio-brain:wiki-query`, `wiki-new`, `wiki-ingest`, `wiki-status`) — our own accumulated knowledge. Query first, write last. This is what makes runs compound instead of repeat.
- **Atlassian** (Jira) — `searchJiraIssuesUsingJql`, `getJiraIssue`. The backlog itself: what exists, in what state.
- **HubSpot** — CRM signal: tickets, deals, conversations, campaign engagement. Needs the connector authorised; if it isn't, say so and continue with web and social.
- **Web search + web browsing** — `WebSearch` to find, `web_fetch` (or Chrome tools for JS-heavy pages) to read.
- **Apify** — social media, review sites, and scale web scraping via Actors (`search-actors`, `fetch-actor-details`, `call-actor`, `get-dataset-items`). Full method in `references/apify-actors.md`.

Detail on how to search each source well, and the reliability/citation discipline, is in `references/signal-sources.md`. The Insight and gap-report formats are in `references/insight-and-gap-format.md`.

## Mode A — idea signal sync
Trigger: a single JPD key given ("add insights to OHSI-612", "validate this idea").

1. **Load.** `getJiraIssue` the key. Read the problem, hypothesis, and current Insights/evidence if any.
2. **Check Brain first.** `oolio-brain:wiki-query` for existing knowledge on this problem, persona, or product area. Don't re-research what Brain already has settled; use it as a starting point and look for what's changed since.
3. **Gather external signal**, internal first per `references/signal-sources.md`:
   - HubSpot — tickets, deals, conversations naming this problem or a close synonym.
   - Web — competitor and brand pages (the list already maintained in `${CLAUDE_PLUGIN_ROOT}/skills/jpd-loop/references/evidence-sources.md` — don't duplicate it, read it), market and analyst sources.
   - Social — via Apify, per `references/apify-actors.md`: operator/practitioner forums, review sites, relevant social chatter.
   Look for evidence **for and against** the idea, not just confirmation.
4. **Draft Insights.** For each strong item: one-line description, the real source URL, an impact rating 1-5 with a one-line reason. Format and impact-rating discipline (including the social-evidence cap) in `references/insight-and-gap-format.md`. Never fabricate or guess a link.
5. **Hand over, don't write Jira yourself.** Present the Insight list to the user, paste-ready (description · link · impact), same limitation as `jpd-loop`: native Insights aren't creatable from here. If the user wants these on the idea record now, offer `jpd-loop` (full loop) or say they can paste the list into JPD directly.
6. **Sync to Brain.** Per `references/insight-and-gap-format.md`'s Brain-entry format: if Brain already has a page on this topic (found in step 2), `wiki-ingest` the new findings onto it; otherwise `wiki-new`. Cite every source. This is what makes the next run on a related idea faster.

## Mode B — gap scan
Trigger: no key given ("what are we missing", "scan for gaps", "run signal radar on the roadmap").

1. **Snapshot the backlog.** `searchJiraIssuesUsingJql` across all OHSI ideas, all statuses (both mandatory guards), pulling summary, Strategic Pillar, Product Area, and status. This is "what we have."
2. **Check Brain first.** `oolio-brain:wiki-query` for gap analyses, competitor knowledge, or trend notes already captured, so the scan builds on prior work instead of repeating it.
3. **Scan for signal**, aggregated across the backlog rather than idea-by-idea:
   - HubSpot — recurring ticket/deal themes: unmet requests, churn reasons, features asked for repeatedly.
   - Web — competitor moves, market and industry trend research (use the brand/competitor list in jpd-loop's `evidence-sources.md`, don't duplicate it).
   - Social — via Apify: operator complaints and demand signal on forums, review sites, and relevant platforms. Method in `references/apify-actors.md`.
4. **Cross-reference every candidate against the backlog snapshot and Brain.** Already covered by an existing idea, in any status (including Not Now or Rejected, which matters — a killed idea with fresh corroborating signal is worth resurfacing, not silently re-proposing)? If yes, this is reinforcing evidence for that idea, not a gap — route it to Mode A instead. If genuinely uncovered, it's a candidate gap.
5. **Build the gap report.** Table format in `references/insight-and-gap-format.md`: candidate, problem, evidence with source links, likely persona, signal strength and why, overlap check result, recommended action. Present it; do not touch Jira yet.
6. **Get one approval for the batch**, same discipline as `feedback-to-idea`'s bulk sweeps. For each approved candidate, hand off to `feedback-to-idea` to draft and de-dupe properly rather than drafting it here.
7. **Sync to Brain regardless of outcome** — what was scanned, what was found, what was already covered, what became a candidate. A declined candidate is still worth recording so it isn't re-surfaced identically next scan without new evidence.

## Signal-strength discipline
Not all sources carry equal weight. A HubSpot-confirmed pattern across several accounts outranks a single scraped social post. Full reliability tiers and impact caps are in `references/insight-and-gap-format.md` — read before rating anything above 3/5 on social-only evidence.

## Privacy and scraping discipline
Apify pulls from public sources only. Never scrape login-gated content, private profiles, or DMs. Aggregate sentiment and public reviews/posts are fair game; do not compile a dossier on a named private individual. Keep Actor runs scoped (small result counts, narrow date ranges) — this is signal sampling, not mass collection. Full detail in `references/apify-actors.md`.

## This skill must never
- Create, edit, or transition a Jira issue, or write a JPD custom field. Hand off to `jpd-idea-groomer`, `feedback-to-idea`, or `jpd-loop`.
- Fabricate, guess, or omit a source link. No link, no Insight, at most a note.
- Treat a single uncorroborated social post as strong (4-5) evidence.
- Propose a "gap" that's already an idea in the backlog, including killed or parked ones, without checking first.
- Scrape login-gated or private content, or compile personal data on a named individual.
- Overwrite an existing Brain page wholesale — ingest onto it, don't replace it.

## Definition of done
**Mode A:** Brain checked first; available connectors queried (or gaps noted); a balanced set of cited Insights drafted with impact ratings; the paste-ready list handed to the user; findings synced to Brain.
**Mode B:** backlog snapshot pulled; Brain checked first; signal scanned across available sources; every candidate cross-checked against the backlog and Brain; a gap report presented and one batch approval taken; approved candidates handed to `feedback-to-idea`; findings synced to Brain whatever the outcome.

## References (read on demand)
- `references/signal-sources.md` — how to search HubSpot, web, and Brain well; source reliability and citation discipline.
- `references/apify-actors.md` — the Apify Actor workflow (discover, inspect, run, fetch results) and scraping discipline.
- `references/insight-and-gap-format.md` — the Insight format, impact-rating caps for social evidence, the gap-report table, and the Brain sync-entry format.

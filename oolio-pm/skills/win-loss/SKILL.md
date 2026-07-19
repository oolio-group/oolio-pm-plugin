---
name: win-loss
description: >-
  Mine HubSpot closed-lost and churn data for the real reasons Oolio wins
  and loses, monthly. Treats rep-entered loss reasons as hypotheses (buyer
  research shows they are wrong more often than right) and cross-examines
  deal metadata instead. Codes every loss on four drivers (product fit,
  sales experience, pricing/packaging, competitive), aggregates patterns by
  segment and competitor, routes product gaps to `feedback-to-idea`,
  competitor patterns to the `competitor-watch` dossiers, and drafts
  interview guides for the human follow-up calls. Trigger when the user says
  "run win/loss", "why are we losing deals", "mine closed-lost", "what's the
  win/loss picture this month/quarter", "who are we losing to", or asks why
  a segment or competitor keeps beating us. Do NOT trigger for a single
  deal post-mortem chat (just discuss it), competitor web research (use
  competitor-watch), or general idea validation (use signal-radar).
---

# Win/loss

The richest "step over competitors" source is our own lost deals, and it is systematically misread: buyer-side research (Clozd and others) finds rep-entered CRM loss reasons wrong more often than right, the competitor tagged on the deal wrong in a large majority of studied cases, and losses over-attributed to price because price protects the rep's reputation. This skill mines HubSpot monthly, treats the recorded reason as a hypothesis, cross-examines the metadata, and turns the residue into patterns the roadmap and battlecards can act on.

Operating model and Brain conventions: `${CLAUDE_PLUGIN_ROOT}/references/research-os.md`. Method detail: `references/loss-coding.md`. House style: `${CLAUDE_PLUGIN_ROOT}/references/house-style.md`.

Requires the HubSpot connector. If it is not authorised, stop and say so — there is no degraded mode worth running; this skill without CRM access is guesswork.

## Inputs
A period ("last month", "Q1", "since March") and optionally a slice (a segment, a competitor, a product line). Default: the last full calendar month, all segments. Also accepts churn framing ("why are customers leaving") — same method over churned/cancelled customers instead of lost deals, where HubSpot records them.

## Workflow

### 1. Pull the corpus, and state what the data supports
Via the HubSpot connector: closed-lost deals in the period (and a closed-won sample of similar size for contrast — loss analysis without a win baseline misreads what is normal). For each deal capture: amount, segment/vertical, source, recorded loss reason, competitor named (if any), owner, and time-based metadata (created, stage history where available, closed date).

**Data-availability preflight:** before cross-examining, state which evidence classes the connector actually returned — stage history, engagement/activity timeline, notes/emails/meeting logs. A checklist item whose data class is absent is skipped, and every deal missing that class is automatically **rep-reported only** for the affected checks; do not infer around missing metadata.

### 2. Cross-examine, don't transcribe
For each loss, test the recorded reason against what the metadata says (checklist in `references/loss-coding.md`): time-in-stage anomalies, engagement drop-off, whether a competitor was actually named in notes/emails/meeting logs rather than the tag, deal size vs segment norms. Where notes and recorded reason disagree, the notes win. Mark each deal's coded reason as **corroborated** or **rep-reported only** — that distinction carries through everything downstream.

### 3. Code on the four drivers
Every loss gets one primary (and optionally one secondary) driver: **product/solution fit** · **sales experience** · **pricing/packaging** · **competitive**. Definitions and edge rules in `references/loss-coding.md`. Do not invent an "other" bucket; a loss that fits nothing is listed unclassified with its evidence, and enough of those is itself a finding.

### 4. Aggregate to patterns
Patterns, not anecdotes: by driver, by segment/vertical, by named competitor, by product line. A pattern needs the minimum counts in `references/loss-coding.md` (default: 5+ deals on the same theme) before it is reported as one; below threshold it is listed as "watch" with its count. Compare against the previous run's patterns (Brain) — a growing theme outranks a static one. An all-uncorroborated corpus can still report patterns, labelled **"uncorroborated pattern — CRM-tag level only"**; the report header always states the corpus corroboration rate (n corroborated of m coded) so the reader knows what the patterns rest on.

### 5. Report and route
A short pattern report (chat, or Confluence internal page on request): headline patterns with counts and corroboration status, competitor-specific findings, watch list, and what changed since last run. Then route:
- **Product-gap themes** → `feedback-to-idea` candidates (with the deal evidence cited), via the usual approval.
- **Competitor patterns** → the relevant `competitor-watch` dossier's "Wins and losses against us" section (pattern level only), and flag affected battlecards. No dossier for that competitor yet → have competitor-watch's dossier mode create it as part of the run.
- **Interview candidates** → for the 2-3 most consequential losses, draft a short buyer-interview guide (open what/why questions on the coded driver; template in `references/loss-coding.md`). Interviews are the human's job — the guide is the handover, not a substitute. Flag politeness-bias risk if the interviewer would be the deal's own rep.

### 6. Sync to Brain
Per research-os: one evidence log for the run (corpus, method, counts), patterns as insights linked to it, dossier updates as above, and the scoreboard on `gaps/ledger` (patterns raised → ideas → verdicts). Record the next run's due date.

## This skill must never
- Write a Jira issue or field (route through `feedback-to-idea`), or edit HubSpot records.
- Report a rep-reported-only reason as fact, or an under-threshold theme as a pattern.
- Name-and-shame individual reps in any output; patterns are about segments, drivers, and competitors, not people.
- Put raw customer names or deal gossip in Brain dossiers — pattern level only; deal-level detail stays in HubSpot where access control lives.
- Substitute for buyer interviews, or present coded reasons as buyer-confirmed when no interview happened.

## Definition of done
Corpus pulled with a win baseline; every loss cross-examined and coded with corroboration status; patterns aggregated with counts against thresholds and compared to last run; report delivered; gaps, dossier updates, and interview guides routed; Brain synced with the run's evidence log and insights; next run due date stated.

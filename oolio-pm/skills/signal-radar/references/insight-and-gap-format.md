# signal-radar — Insight and gap-report formats (reference)

Read this for Mode A's write-up (step 4) and Mode B's gap report (step 5), and for the Brain sync step in both modes.

## Insight format (matches jpd-loop, so lists are interchangeable)
Each Insight: a one-line **description**, the real **source URL**, an **impact rating 1-5** with a one-line reason. Same shape as `${CLAUDE_PLUGIN_ROOT}/skills/jpd-loop/references/insights-and-citations.md` — that's deliberate, so a signal-radar Insight list can be pasted straight into a `jpd-loop` run or the native JPD Insight panel without reformatting.

## Impact rating with the social-evidence cap
Start from jpd-loop's rubric (5 = decisive, 1 = context only), then apply the source-reliability tier from `signal-sources.md`:

- Tiers 1-4 (HubSpot direct, Brain, primary competitor source, analyst report) — rate on the normal 1-5 scale, no cap.
- Tier 5 (aggregated social/review signal — the same point made across several independent posts or reviews) — cap at **4**. Corroboration across sources earns weight; it's still not a paying customer's deal blocker.
- Tier 6 (a single social post, forum comment, or review, uncorroborated) — cap at **2**. Real signal, worth noting, not worth a decision on its own. If you're tempted to rate it higher because the post is compelling, that's a sign to go find corroboration before scoring it, not a reason to raise the cap.

State which tier an Insight draws from when the impact reason isn't obvious from the description.

## Gap report table (Mode B)
One row per candidate:

| Candidate | Problem | Evidence (with links) | Likely persona | Signal strength | Overlap check | Recommended action |
|---|---|---|---|---|---|---|
| Short name | The operator-facing problem, one line | 2-4 cited sources, tier noted | Primary Persona (from field_standards.md's list) | Weak / Moderate / Strong + why | Nearest existing idea/status, or "none found" | Attach to existing (→ Mode A) / Draft new (→ feedback-to-idea) / Monitor (not enough signal yet) |

Order rows by signal strength, strongest first. "Monitor" candidates still get synced to Brain (below) so the next scan can pick up new corroborating signal without starting over.

## Brain sync-entry format
Whether Mode A or Mode B, every run writes (or extends) a Brain entry. Structure:

```
# <topic/title — problem, competitor, or trend, whichever is the subject>

**Date:** <run date>
**Mode:** idea sync (<JPD key>) | gap scan
**Summary:** one paragraph — what was found, net of the caveats.

## Sources
- <description> — <URL> — <tier/date>
- ...

## Outcome
<For idea mode: Insight list handed over, count and headline.>
<For gap scan: candidates surfaced, what happened to each (drafted / attached / monitored), and what was already covered and why it wasn't a gap.>
```

Check `oolio-brain:wiki-query` before writing: if a page already covers this topic, `wiki-ingest` this run's findings onto it (extend, don't replace) so the page stays the single accumulated record. Only `wiki-new` when nothing existing covers the topic.

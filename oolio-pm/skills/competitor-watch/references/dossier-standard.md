# competitor-watch — dossier standard (reference)

The schema for one competitor's living page in the brain: `30 Knowledge/Market/Competitors/<Name>.md`, the **one canonical page** per competitor (the vault's Market README rule: canonical here, contextual in capability domains, which link back rather than copying). One page per competitor; sections, not sub-pages. The dossier is curated and rewritten freely, **except** the history section, which is append-only. Existing dossiers in the vault predate this standard — extend them toward this shape when touched; never blank-and-rewrite a page that has content.

## Page skeleton

```
---
type: entity
title: <Competitor>
tags: [domain/market, entity/competitor]
created: <date>
updated: <date>
sources: ["[[<source pages>]]"]
status: active
---

# <Competitor>

**Tier:** 1 | 2 | 3 · **Freshness:** verified | contested | stale
**Last verified:** <date> · **Review by:** <date per research-os cadence>

## Position
Two or three sentences: what they are, who they sell to, their angle, AU relevance.
Dated claims with sources.

## Pricing
Current pricing claims, each: claim · [source](url) · verified <date>.
Include contract terms (lock-in, auto-renewal, payment-processing bundling) — in this
market those decide deals as often as features.

## Moves (timeline, newest first)
- <date> — what happened — [source](url)
Major launches, acquisitions, market entries, funding, leadership. This is what the
weekly sweep appends to.

## Strengths (honest)
Where they genuinely win: features, price points, brand, distribution. Sourced.
A dossier without this section is propaganda and will mislead the council.

## Weaknesses and complaint themes
From deep-dive mining: theme · volume/count · representative verbatim · [source](url) · dated.
Note review-velocity anomalies. Distinguish structural weaknesses (business model,
contract terms) from fixable ones (a bug, a support backlog).

## Wins and losses against us
Populated by `win-loss` runs: pattern-level only (segments, drivers, counts), not
raw deal gossip. Dated per run.

## Watch state
Which watchlist sources were last checked and when. Anything unreachable or moved.

## History (append-only)
- <date> — superseded: "<old claim>" → see current <section>. 
Claims replaced elsewhere land here with their date. Never delete from this section.
```

## Rules

- **Supersede, don't stack.** New pricing replaces old pricing in place; the old claim moves to History with its date. The top of the page is always the current state.
- **Every claim dated and sourced.** An undated claim is not usable by the council or a battlecard; don't write one. Second-hand claims (a competitor fact sourced from one of our own PRDs rather than their material) carry a visible caveat callout, per the vault's existing practice: state where it came from and that it needs verifying before external use.
- **Freshness flips to `stale` automatically** when past Review-by (research-os). A sweep or dossier-mode run that re-verifies flips it back. (Freshness is the research-os field; the frontmatter `status: active` is the vault's page-lifecycle field — they are different things.)
- **Contested claims** (two sources disagree, e.g. on pricing) are marked contested inline with both sources linked, not silently resolved.
- **Low-web-signal competitors** (Redcat, H&L): their dossiers will lean on tier-1 HubSpot/win-loss evidence rather than web sources. That is expected; say so in Watch state rather than padding with weak web material.
- **Battlecards derive from dossiers**, never the reverse: if a battlecard needs a claim the dossier lacks, the dossier gets it first (with source), then the card.

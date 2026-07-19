# competitor-watch — mining playbook (reference)

The ordered source list and pinned Apify Actors for mining a hospitality-POS competitor's public footprint. Used by competitor-watch deep-dive mode and by signal-radar when it needs social/review signal. Verified July 2026; re-verify an Actor (`fetch-actor-details`) before first use in a run, and update this file if one has died or been superseded.

**Do not rely on Apify's `search-actors` to choose an Actor at runtime** — observed behaviour is that keyword search returns a generic popularity list, so runs become non-repeatable. Use the pinned names below via `fetch-actor-details` → `call-actor` → `get-dataset-items`.

## The ordered playbook (per competitor)

1. **G2 product page** — Actor `automation-lab/g2-scraper` (exposes G2's own loveTheme/hateTheme sentiment fields). Mine the structured fields specifically: "What do you dislike?", "Reasons for switching", and per-category sub-scores (a sub-score below ~7.5 on support, ease of setup, or product direction is a repeatable vulnerability). G2 is aggressively anti-bot: expect breakage; fall back to reading the public pages via web fetch.
2. **Capterra (AU directory where it exists)** — Actor `imadjourney/capterra-reviews-scraper`; or `zen-studio/software-review-scraper` for G2+Capterra+Trustpilot in one run.
3. **ProductReview.com.au** — the venue where Australian operators actually vent, and largely ignored by US rivals. No dedicated Actor: use `apify/website-content-crawler` on the listing URL (free, markdown output, respects robots.txt).
4. **Reddit** — Actor `harshmaur/reddit-scraper-pro` (no login needed) or `trudax/reddit-scraper`. Target r/restaurantowners (primary POS complaint venue), r/KitchenConfidential (staff-side friction), r/barowners. Search competitor name + terms like fee, support, outage, switching. Mine comments, not just posts. Note: Reddit's policy since 2024 requires a contract for commercial data use; internal competitive research is the low-risk end, but keep pulls small and never republish scraped Reddit content.
5. **App stores (AU and US country codes separately)** — Actor `novashieldai/app-store-scraper` (App Store + Google Play in one) or `webdatalabs/google-play-reviews-scraper`. Target the competitor's companion apps (operator app and consumer ordering app). Track review velocity per version; a 1-star spike after a release or price change is a finding in itself.
6. **X/Twitter** — Actor `apidojo/tweet-scraper` (full advanced-search syntax). Query pattern: `"<competitor>" (fee OR outage OR support OR switching) -from:<their handle>`.
7. **Google Maps (consumer-side friction)** — `compass/crawler-google-places` to find venues using the competitor's ordering product, then `compass/google-maps-reviews-scraper` for diner-side complaints. Use sparingly; this is the deepest, most expensive layer.
8. **AU forums (Whirlpool)** — low volume, high AU relevance; plain web fetch on relevant threads, no Actor needed.
9. **Skip: private Facebook groups.** Login-gated; no compliant Actor exists. `apify/facebook-groups-scraper` covers public groups only. If a private group matters, that is a human's job, not a scraper's.

## Campaign and engagement mining (demand signal)

Competitor marketing is a free demand-research programme someone else paid for: what they choose to campaign on shows where they think demand is, and the **engagement** their posts get measures whether the market agrees. A Toast feature announcement with outsized engagement is desirability evidence for that capability, usable in our own idea validation, whoever ships it.

- **X/Twitter** — `apidojo/tweet-scraper` on the competitor's own handle (campaign posts + engagement counts), alongside the complaint queries above.
- **Instagram (public business profiles)** — Apify's first-party Instagram scraper (`apify/instagram-scraper`; verify via `fetch-actor-details` on first use and pin the confirmed name here). Posts, captions, engagement counts on public profiles only.
- **Facebook public pages** — `apify/facebook-posts-scraper` (public pages only; groups and anything login-gated stay out).
- **LinkedIn** — effectively login-walled; read their public company page manually via web fetch, no Actor.

Method:
1. Pull the trailing window of posts from the competitor's public accounts; identify campaign themes (which capability, which audience, which claim).
2. **Normalise engagement before comparing**: engagement relative to that account's own baseline (their median post), not raw counts across accounts with different follower bases. An outlier against their own baseline is the signal.
3. Record campaign themes and standout posts on the dossier (Moves or a Campaigns note), dated, with post URLs and the engagement figures as captured.
4. **Interpretation caps**: campaign engagement is desirability evidence only — it says the market wants the thing, never that the competitor's version works, and never that it converts to revenue. It enters Insights at tier 5 (aggregated social) at best, and pairs naturally with claim-vs-reality (below): high desire + their poor execution is the strongest combined finding this playbook produces.

## Claim vs reality (picking holes in what they market)

Everyone markets great ideas; part of the job is testing them. When a competitor campaigns on a capability:
1. State the marketed claim precisely (their words, their post/page, dated).
2. Test it against their own users: reviews and community complaints mentioning that capability (the sources above), their help-centre docs (limits, caveats, rollout footnotes), and any pricing-page fine print.
3. Verdict per claim: **holds** (evidence supports it), **oversold** (real but weaker than marketed — note the specific gap), or **vapour** (announced, not observably shipped). Each with sources.
4. Route: oversold and vapour verdicts go to the dossier's weakness section and the battlecard's landmines ("ask them to demo X live"); the demand signal from the campaign still counts as validation for our matching idea or gap candidate — the market's desire is real even when their delivery isn't.

## Change detection (feeds the weekly sweep)

**The baseline lives in Brain, not in Apify.** Ad-hoc `call-actor` runs via the MCP get fresh storage each time and the MCP cannot create saved tasks or schedules, so Actors that "diff against the previous run" (`jakubbalada/content-checker`) only work from a human-created saved task in the Apify console — treat them as an optional human-side upgrade, not part of the agent loop. The agent-side pattern that always works:

1. On each sweep, fetch the watched page (pricing page via web fetch; a docs subdomain via `apify/website-content-crawler` when it is big or JS-heavy).
2. Compare against the snapshot notes stored in the dossier's **Watch state** section last time (key claims and figures, not full page dumps).
3. Record the new snapshot notes with the date; differences are the deltas the sweep reports.

`tri_angle/sitemap-change-detector` is still useful statelessly for spotting **new** help-centre or release-notes pages (feed it the sitemap, compare the URL list against Watch state).

## Scoping rules (hard limits per run)

- Default window: trailing 12 months for reviews; since-last-sweep for news/changes.
- Default result caps: ≤200 items per Actor per competitor per run; paginate only if a cluster needs confirming.
- One competitor per deep-dive run. A "mine everyone" request becomes a queue, run by watchlist tier.
- Before trusting a pattern: roughly 50+ reviews in the corpus, or the same theme across 3+ independent sources. Below that, report as colour with the count, not as a theme.
- Cost sanity: check the Actor's pricing in `fetch-actor-details` before a run; if a planned run looks like it exceeds a few dollars, say so and confirm first.

## Classification and clustering (the synthesis layer)

Classify every mined item: **complaint** / **feature request** / **switching signal**. Two findings from the literature worth encoding: feature requests appear mostly in *positive* reviews, so don't mine only 1-2 star reviews for requests (reserve low-star filtering for complaint and churn mining); and G2's "reasons for switching" field is the single densest churn-trigger source. Cluster into 5-8 themes per competitor with counts and representative verbatims (each with URL and date), and track theme volume run-over-run — growth in a theme is a stronger signal than its existence.

## Boundaries

Public pages only; no login bypass anywhere (that line is also the legal line: public-page scraping without access-control bypass is the defensible surface). Keep reviewer PII out of what gets written to Brain: themes, counts, and quotes attributed to the platform, not profiles of named individuals. Respect robots and rate limits; prefer the platform's own structured fields over aggressive crawling.

# signal-radar — Apify Actor workflow (reference)

Apify runs "Actors" — hosted scrapers — against social platforms, review sites, and general web sources. Read this before the first Apify call in a run.

## Workflow
1. **Discover.** `search-actors` with keywords for the source you need (e.g. "reddit search", "app store reviews", "google reviews", "twitter search", "g2 reviews"). Prefer Actors with higher usage/ratings over an obscure one-off.
2. **Inspect before running.** `fetch-actor-details` to read the Actor's README and, critically, its **input schema** — know what a run will cost and return before starting it. Skipping this step is how a run comes back empty or absurdly large.
3. **Run scoped.** `call-actor` with the minimal input that answers the question: a narrow keyword/subreddit/handle, a small result cap, a recent date range if the Actor supports one. This is signal sampling for a specific idea or gap question, not a data-collection exercise — don't ask for more than you'll actually read.
4. **Fetch results.** `get-dataset-items` to pull the run's output. Paginate rather than requesting everything if the dataset is large.
5. **Default fallback.** For a quick, low-setup web-and-social query where a dedicated Actor isn't worth the schema-reading overhead, use the **RAG Web Browser** Actor (`apify--rag-web-browser`) — search plus fetch in one call.

## Actor selection by signal type
- **Operator/practitioner forums and communities** (Reddit, hospitality/industry forums) — search-actors for a Reddit or forum-search Actor; these surface unfiltered operator complaints and workarounds, useful for both idea validation and gap-scan.
- **App store / product reviews** (Google Play, App Store, G2, Capterra) — review-scraper Actors; good corroborating evidence for a feature gap or a competitor weakness.
- **Social chatter** (X/Twitter, LinkedIn where accessible) — search-actors for a platform-specific search Actor; treat as directional, not decisive, per the reliability tiers in `signal-sources.md`.
- **Competitor sites at scale** — if `WebFetch`/Chrome tools aren't enough (JS-heavy, many pages), a general web-scraping Actor or the RAG Web Browser can cover more ground.

## Discipline
- **Public sources only.** Never target login-gated content, private profiles, DMs, or anything behind an authentication wall. If an Actor's normal operation requires login, don't use it here.
- **No dossiers on private individuals.** Aggregate sentiment, public reviews, and public posts about a product or company are fair game. Do not compile or report on a named private person.
- **Scope every run.** Small result counts, narrow keywords, a bounded date range. If a genuinely large run seems warranted (a full competitor teardown, a multi-week sentiment sweep), say so and confirm before running it rather than defaulting to a big pull.
- **Cite the real item.** Every claim drawn from Apify results needs the actual source URL (the post, review, or page), same as any other evidence. A dataset row with no working link back to its source isn't usable as an Insight.
- **Respect platform terms.** Apify Actors in the Store are built for legitimate use, but the underlying platform's terms still apply to what you do with the data — use it for internal product research, not redistribution.

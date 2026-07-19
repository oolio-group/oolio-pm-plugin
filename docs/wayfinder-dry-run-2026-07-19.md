# Discovery wayfinder — promotion dry-run, 2026-07-19

The dry run the promotion bar required: one real theme from the OHSI backlog charted by the skill's own rules. Theme chosen with Niel: **labour cost control**. The run correctly entered **proposal mode**, because step 1's type check found only `Idea` (10071) and `Customer` (10606) in OHSI; the `Discovery` and `Decision` idea types do not exist yet. So this document is the charted map, nothing was created in Jira, and the one-time setup below is the hand-over.

## What the run proved

- The type check catches the missing setup and degrades to proposal mode instead of writing Idea-typed issues.
- The theme genuinely needs a map: fourteen Exploring ideas orbit it with heavy overlap (three near-duplicate intraday-pacing ideas, two roster-vs-forecast, two staff-sync, two off-roster), and the load-bearing questions are decisions, not builds.
- A research ticket resolved AFK inside the charting session (the one permitted exception), with cited findings.
- Charting surfaced one skill fix, applied before promotion: narrow factual research tickets run as a plain cited subagent rather than the full `storm-research` pipeline, which is overkill for a factual lookup by its own description.

## Hand-over: one-time setup (human, JPD UI)

OHSI > Space Settings > Types and workflows > Add type: **Discovery** (map) and **Decision** (ticket), per `oolio-pm/skills/discovery-wayfinder/references/jira-modelling.md`. Then record the new type ids in that file and ship the change. The map below is ready to create the moment the types exist.

---

## Proposed map: Finding the shape of labour cost control (Discovery)

### Destination

A settled direction for labour cost control at Oolio: which segment we serve first, integrate-vs-build for workforce data, and a shortlist of canonical ideas handed to `jpd-loop` for validation, with the fourteen overlapping Exploring ideas consolidated under them.

### Notes

Domain: hospitality labour cost, AU-first. Consult `signal-radar` for HubSpot/social evidence and the competitor dossiers in Brain before external research. The existing cluster: OHSI-514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 598.

### Decisions so far

- [What Tanda/Deputy expose and what competitor POS ship](#resolved-research-ticket) — both have full public APIs with award-interpreted wage cost; labour-vs-sales views are table stakes across Square, Toast, Lightspeed and the AU competitors, mostly via Tanda/Deputy integrations.

### Not yet specified

- Award interpretation and compliance depth: whether partner data (Tanda returns award-interpreted costs) covers us or we need our own interpretation. Sharpens after build-vs-partner.
- Forecast source: our own demand forecasting (OHSI-597) or partner forecasts, for the roster-vs-forecast tickets.
- Pricing and packaging: where labour capability sits in tiers. Sharpens after the direction decision.

### Out of scope

- Payroll processing: beyond the destination; the theme is cost visibility and control, not paying people.
- Weather-aware staffing (OHSI-508 to 512): its own theme, its own map if wanted.
- Staff onboarding/offboarding sync (OHSI-517, 525): staff admin and access control, not cost control; candidate for a separate intake pass.

### Tickets (type · blocking)

| Ticket | Type | Blocked by |
|---|---|---|
| Which venue segment feels labour overspend hardest, and which do we serve first? | grilling | — |
| What do Tanda and Deputy expose via API, and what labour-vs-sales capability do competitor POS ship? | research | — (**resolved below**) |
| Is labour cost control a reporting capability in Insights, or an in-service operational tool? | grilling | — |
| How strong is the customer and pipeline signal, and which competitors get cited? (`signal-radar`) | evidence | — |
| Build or partner: integrate Tanda/Deputy, or build native rostering? | grilling | research + evidence tickets |
| What would make Steering fund this theme? | grilling | segment + build-or-partner tickets |
| Consolidate the overlapping ideas into canonical ideas per the chosen direction (`jpd-idea-groomer`) | task | build-or-partner ticket |

Frontier at charting: the first four. Note the evidence ticket needs the HubSpot connector authorised.

---

## Resolved research ticket

**Question:** What do Tanda and Deputy expose via public API for roster, timesheet, and wage-cost data, and what labour-vs-sales capability do competitor hospitality POS platforms already ship?

**Resolution:** Both Tanda (Workforce.com) and Deputy publish full public REST APIs covering rosters, timesheets, and wage cost, so integration is technically open rather than gated. Tanda's API v2 (OAuth 2, scoped) returns award-interpreted wage costs on schedules (`show_costs=true`); Deputy's Resource API exposes Roster and Timesheet objects with a Cost field. Labour-vs-sales visibility is table stakes: Square (Shifts Plus), Toast (Labor Cost Breakdown, SPLH), and Lightspeed (via Planday) all ship labour-as-percentage-of-sales reporting, and AU competitors SwiftPOS and Impos market live sales-vs-labour views through Tanda/Deputy integrations.

Findings, cited:

- Tanda API v2: rosters, timesheets, shifts; OAuth 2 with per-object scopes — https://my.workforce.com/api/v2/documentation
- Tanda schedules return award-interpreted wage cost incl. on-costs (`show_costs`, `cost_with_oncosts`) — https://my.tanda.co/api/v2/documentation
- Tanda payroll endpoints added to the public API — https://tanda.canny.io/changelog/just-added-payroll-api-endpoints-to-public-api-docs
- Deputy Resource API: Roster, RosterOpen, RosterSwap, Schedule, wage-budget endpoints, OAuth 2 — https://developer.deputy.com/docs/shifts-overview
- Deputy Timesheet resource carries a decimal Cost field — https://developer.deputy.com/docs/timesheet
- Square "Labor vs sales" report, Shifts Plus tier only, excludes payroll taxes and tips — https://squareup.com/help/us/en/article/6140-employee-timecard-reporting
- Toast Labor Cost Breakdown: labour % of net sales and sales per labour hour — https://support.toasttab.com/en/article/Labor-Cost-Breakdown-Report-Overview
- Lightspeed pairs revenue with scheduled labour cost via Planday — https://www.lightspeedhq.com/integrations/planday/
- SwiftPOS feeds live sales into Tanda for sales-vs-labour dashboards — https://www.swiftpos.com.au/integrations-tanda/
- Impos surfaces real-time labour cost as % of sales via Deputy and Tanda — https://impos.com.au/pos-integrations/rostering-time-management/

Gaps (unverified): Deputy partner-programme commercial terms, Tanda API rate limits, H&L's exact wage-vs-revenue reporting mechanics.

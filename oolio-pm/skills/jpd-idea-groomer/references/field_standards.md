# JPD Field Standards, canonical field IDs and option labels

The single source of truth for writing custom fields back to Jira Product Discovery (project `OHSI`, "Oolio One Ideas", issue type `Idea`, id `10071`). Labels below were pulled from the live Jira field metadata on 2026-07-06. **Always send these exact strings.** The Confluence standard page describes intent; Jira enforces spelling. Where the two differ, this file wins.

Canonical rules page: https://oolio.atlassian.net/wiki/spaces/PM/pages/1055653929/Jira+Product+Discovery+JPD+Field+Standards

If a write fails with an unhelpful error, the label is almost always the problem. Re-check here, or fetch a known populated idea (`OHSI-39`, `OHSI-45`, `OHSI-57`, `OHSI-72`, `OHSI-74`) and copy the exact string.

## Required fields

### Strategic Pillar — `customfield_11552` (multi-select)

- `Venue Profitability`
- `Operational Efficiency`
- `Ordering Growth`
- `Multi-Venue Management` (capital V in Jira; the Confluence page writes "Multi-venue")
- `Platform Extensibility`
- `Vertical Expansion`
- `Migration & Modernisation`

Select at least one. Multiple only when genuinely relevant. Never all of them.

### Category — `customfield_11553` (single-select)

- `Customer Problem`
- `New Capability`
- `Product optimisation` (lowercase o, exactly as written)
- `Strategic investment` (lowercase i, exactly as written)

Choose the primary category only.

**Warning: there are two Jira fields named "Category".** The standard's field is `customfield_11553`. The other (`customfield_11711`, options like POS, Payments, Reporting) belongs to the Requests intake view. Do not confuse them.

### Source — `customfield_11554` (multi-select)

The live Jira options differ noticeably from the Confluence page. Use these:

- `Customer`
- `Sales`
- `Support`
- `Operations`
- `Internal Product Insight`
- `Market / Competitor`
- `Data / Analytics`
- `Migration (legacy platform)`
- `Compliance / Regulatory`
- `Partner / Integration`

Multi-select allowed; strong ideas often carry two or three signals (for example `Customer` + `Support` + `Internal Product Insight`).

### Customer Signal — `customfield_11560` (single-select)

Sentence case in Jira, not title case:

- `One customer`
- `Multiple customers`
- `Repeated support trend`
- `Revenue blocker`
- `Churn risk`
- `Strategic prospect blocker`
- `Market insight`
- `Product vision`

Choose the strongest signal that is actually true.

### Primary Persona — `customfield_11555` (single-select)

- `Venue Owner`
- `Venue Manager`
- `FOH Staff` (not "Front-of-House Staff")
- `Kitchen Staff`
- `Finance/Admin` (no spaces around the slash)
- `Multi-site Operator`
- `Support Teams` (not "Support Staff")
- `Integrations/Partners`
- `Franchise/Enterprise Operator` (exists in Jira; not on the Confluence page)

One value: who benefits most.

### Delivery Size — `customfield_11557` (single-select)

Jira labels include the effort suffix after a pipe. Send the whole string:

- `Tiny tweak | Hours`
- `Quick win | Days`
- `Small feature | 1 sprint`
- `Medium epic | 2–4 sprints`
- `Large initiative | 1–3 months`
- `Multi-team programme | 3–6+ months`
- `Moonshot | High uncertainty`

Directional only. Not engineering estimation.

### Product Area — `customfield_11561` (single-select)

- `POS & Service`
- `Ordering`
- `Menu & Pricing`
- `Payments & Checkout`
- `Kitchen & Production`
- `Inventory & Supply`
- `Finance & Reconciliation`
- `Customer & Loyalty`
- `Analytics & Reporting`
- `Venue Management`
- `Multi-site Management`
- `Integrations & Ecosystem`
- `Platform & Infrastructure`

One primary area only. Ask: which product domain does the problem primarily belong to?

### Our Objective — `customfield_11559` (multi-select)

Sentence case in Jira:

- `Revenue growth`
- `Retention`
- `Migration enablement`
- `Support reduction`
- `Time-to-live reduction`
- `Operational efficiency`
- `Market expansion`
- `Competitive parity`
- `Enterprise readiness`
- `Platform adoption`

### Innovation — `customfield_10505` (rating, 1–5)

Written as a bare number. The field's display name carries a leading space (` Innovation`) in Jira; write by ID, never by name. Rate honestly:

1. Parity / catch-up
2. Incremental, common in market
3. Solid differentiator
4. Strongly differentiated, few competitors offer it
5. Market-leading or novel (including new applications of emerging tech such as AI)

## Optional fields

### Secondary Personas — `customfield_11556` (multi-select)

Same option list as Primary Persona. Only tag personas genuinely impacted.

### Applicable Segments — `customfield_11558` (multi-select)

- `Cafe` (no accent in Jira)
- `QSR`
- `Casual Dining`
- `Pub`
- `Bar`
- `Hotel`
- `Fine Dining`
- `Franchise`
- `Enterprise` (in Jira; not on the Confluence page)
- `Multi-location`
- `Takeaway`
- `Pizza`
- `Bakery` (in Jira; not on the Confluence page)
- `Gaming Venue`

Every materially relevant segment, not fringe cases.

### Migration Relevance — `customfield_11562` (multi-select)

Despite the Confluence page describing Yes/No, the live field is a legacy-product picker:

- `Bepoz`
- `SwiftPOS`
- `IdealPOS`
- `DeliverIT`
- `OrderMate`

Select the legacy products the idea materially supports migrating from. Leave empty when not migration-relevant.

### Escalate — `customfield_10432` (number/boolean tag)

Set only for genuine executive or commercial urgency. If the API rejects the write, fall back to the JPD UI toggle and tell the user.

## VPC loop fields (written by jpd-loop, read-only here)

These exist on the Idea type and are managed by the `jpd-loop` skill. The groomer should not set them, but should not clobber them either:

`VPC Loop State` (`customfield_11663`), `VPC Reviewed` (`11664`), `VPC Iterations` (`11665`), `VPC Verdict` (`11666`), `Dedupe Status` (`11667`), `Sign-off Status` (`11668`), `Sign-off Owner` (`11669`), `VPC Last Run` (`11671`), `Escalation Reason` (`11672`), `Desirability` (`11673`), `Feasibility` (`11674`), `Viability` (`11675`), `Strategic Fit` (`11676`), `VPC Confidence` (`11677`).

## Write-back shapes (editJiraIssue `fields` object)

- Single-select: `"customfield_11553": {"value": "Customer Problem"}`
- Multi-select: `"customfield_11552": [{"value": "Venue Profitability"}, {"value": "Operational Efficiency"}]`
- Rating: `"customfield_10505": 4`
- Escalate: `"customfield_10432": 1` (fall back to the UI toggle if rejected)

Send every change in one `editJiraIssue` call. Never overwrite an existing sensible value; only propose a change when the current value is clearly wrong or missing.

## Keeping this file honest

This file mirrors live Jira configuration. If a write fails on a label listed here, the Jira config has changed: fetch the field metadata again (`getJiraIssueTypeMetaWithFields`, project `OHSI`, issue type `10071`, `requiredFieldsOnly: false`), fix this file, and note the change in the plugin CHANGELOG.

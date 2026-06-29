---
name: jira-epic-titler
description: Suggest a stronger Oolio Jira epic title using the `[Capability] for [Outcome]` standard. Trigger PROACTIVELY when the user references a Jira epic key (`OR-XXXX`, `EDU-XXXX`) or URL and asks to rename, retitle, improve the title, sharpen the title, or rewrite the summary. Also trigger when the user mentions Oolio's epic title standard, asks to make a name executive-readable or roadmap-ready, complains it's too vague, too technical, or a codename, or pastes a weak epic name for help. Reads the current summary, description, child work items, and any linked Confluence/PRD pages, then proposes 2–3 stronger titles with reasoning. Prefer this skill over generic writing help when an epic-level Jira ticket needs a sharper name. Do NOT trigger for stories, tasks, bugs, sub-tasks, or JPD ideas — use `jpd-idea-groomer` for JPD/IDEA tickets and `jira-epic-groomer` if the description needs rewriting rather than the title.
---

# Jira Epic Titler

Propose a stronger title for a Jira epic using Oolio's epic title standard. An epic title is **an operational label for a concrete body of work**, not documentation, not a user story, not marketing copy. It has to communicate the purpose of the work clearly to anyone in the business in under five seconds — Product, Engineering, Design, CX, Sales, executive leadership, Implementation, Support, and Partners.

The title has to survive Jira boards, sprint views, dependency views, Atlas updates, Slack references, search, roadmap exports, reporting, executive conversations, and cross-team planning. If the title only makes sense to the squad building it, it has failed.

This skill is **draft-only by default**. Present 2–3 title options with reasoning, get explicit approval, then write back to Jira. Epic names ripple through dashboards and roadmaps the moment they change, so they shouldn't churn in front of that audience. If the user explicitly says "just rename it", skip the confirm step.

---

## The Standard

A well-formed Oolio epic title follows one of two structures.

### Preferred format

```
[Capability] for [Outcome]
```

Examples:

- Menu Scheduling for Multi-Venue Consistency
- SMS Receipts for Faster Guest Checkout
- Modifier Templates for Faster Venue Setup
- Split Payments for Group Ordering
- Venue-Level Price Overrides for Franchise Flexibility
- Kitchen Routing for Multi-Prep Workflows

This format is clear, searchable, readable in Jira lists, understandable cross-functionally, and concise enough for boards and reports.

### Secondary format (verb-led)

Use when the outcome matters more than the capability itself, or the work is operational rather than feature-shaped.

```
[Action] to [Outcome]
```

Examples:

- Reduce POS Training Time with Guided Ordering
- Improve Pizza Upsell Conversion with Modifier Prompts
- Enable Venue Migration from SwiftPOS
- Simplify Multi-Site Menu Management
- Support High-Volume Bar Service with Quick Tabs

### What every title must answer

Without opening the epic, the reader should be able to answer all three:

1. **What** is being delivered?
2. **Why** does it matter?
3. **Who** or what context is it for?

If a proposed title doesn't answer all three, it isn't ready.

---

## Hard Rules

These are non-negotiable. If the current title breaks any of them, name the rule in the audit notes so the user understands why it has to change.

1. **No codenames.** No Falcon, Phoenix, Horizon, Titan, Project X. Codenames destroy discoverability and reporting clarity. The only exception is when the codename is already a public business-wide programme name.
2. **No user story syntax.** "As a venue manager I want…" is a story, not a title.
3. **No engineering implementation language.** Avoid Refactor, Rewrite, Microservice Migration, Kafka, Database Consolidation, Service Boundary, etc. If the work is infrastructure, translate it to a business-facing capability. *"Refactor Ordering Service"* becomes *"Ordering Platform Reliability for Peak Trade"*.
4. **No generic words without context.** Avoid bare Improvements, Enhancements, Optimisation, Upgrade, Rework. Pair them with a concrete domain. *"Reporting Improvements"* becomes *"Venue Sales Reporting for Multi-Site Operators"*.
5. **Keep it under ~8 words.** Jira truncates aggressively in boards, backlog views, dependency maps, and Atlas rollups. The title has to remain readable when shortened to roughly 50 characters.
6. **Use business language, not product jargon.** Prefer Venue, Staff, Kitchen, Guest, Operator, Franchise, Delivery Driver over Entity, Resource, Actor, Consumer, Service Layer.
7. **No marketing copy.** No "Revolutionary Guest Engagement" or "Game-Changing Reporting". The audience is operational.
8. **No umbrella phases.** "Pizza Phase 2" or "Kiosk Enhancements" hides the actual scope. Name what's actually shipping in this epic.

---

## Workflow

### 1. Fetch the epic

Use the Atlassian MCP. The Oolio cloudId is `oolio.atlassian.net`.

If the user pastes a URL like `https://oolio.atlassian.net/browse/OR-2417`, extract the key (`OR-2417`) and use that.

```
mcp__atlassian__getJiraIssue
  cloudId: oolio.atlassian.net
  issueIdOrKey: <EPIC-KEY>
  responseContentFormat: markdown
```

Confirm `issuetype.name` is `Epic`. If it's a Story, Task, Bug, Sub-task, or JPD Idea, stop and tell the user. This skill is epic-only. For JPD ideas, point them at `jpd-idea-groomer`. If they want the description rewritten instead of the title, point them at `jira-epic-groomer`.

Capture the current summary, current description, status, labels, fix versions, and any linked Confluence pages or remote links.

### 2. Pull child work items

Children ground the title in what's actually shipping, not just what the original author intended six months ago. Read every child summary.

```
mcp__atlassian__searchJiraIssuesUsingJql
  cloudId: oolio.atlassian.net
  jql: parent = <EPIC-KEY> ORDER BY rank ASC
  fields: ["summary", "status", "issuetype", "resolution"]
```

If the response is too large to load inline, dispatch a subagent to extract one-line summaries per child and report back. Read for:

- The **dominant capability** across children — the recurring "What"
- The **user context** that shows up repeatedly — the "Who"
- Any **outcome language** the team has already used in story summaries — the "Why"

If the children look unrelated to the current epic title, that's signal — call it out in the audit. The epic has drifted from its name.

### 3. Read any linked Confluence pages

Check the issue for remote links, links in the description, and any obvious PRD references. The PRD usually contains the cleanest articulation of the outcome and the customer it serves.

```
mcp__atlassian__getConfluencePage
  cloudId: oolio.atlassian.net
  pageId: <PAGE-ID>
```

Pull out the problem statement, the goals, and any success metrics. Don't quote them in the title — use them as input. Title language should reflect the PRD's outcome, not parrot it.

If there's no linked Confluence page, that's fine. Work from the description and children.

### 4. Audit the current title

Before proposing alternatives, grade the current title against the standard. Be specific:

- Is there a clear **capability**?
- Is there a clear **outcome**?
- Is it readable cross-functionally?
- Does it break any of the **hard rules**? Name them.
- Would it survive **Jira truncation** at ~50 characters?
- Does it match what the **children and PRD** say the work actually is?

This audit becomes the rationale you show the user. Don't skip it — the user needs to see *why* the rename is justified, especially if they wrote the original title.

### 5. Propose 2–3 options

Offer two or three title options, each with a different angle:

- **Capability-led** — `[Capability] for [Outcome]`. Default. Use when the work is feature-shaped.
- **Outcome-led** — `[Action] to [Outcome]`. Use when the business outcome is the headline and the capability is an enabler.
- **Customer-led** — emphasises the persona or operator context. Use when the epic exists primarily to unblock a specific user group (franchise operators, kitchen staff, F&B leads).

Pick the angles that fit. Don't force three options if two are clearly the right calls. Don't pad with weak options to look thorough.

For each option, include a one-line rationale: which structure, what outcome it anchors on, and why it fits this epic.

### 6. Present for review

Use the **Output template** below. Do not write to Jira until the user picks one and confirms.

### 7. Write back to Jira

Once the user picks a title and approves it:

```
mcp__atlassian__editJiraIssue
  cloudId: oolio.atlassian.net
  issueIdOrKey: <EPIC-KEY>
  fields: { "summary": "<the chosen title>" }
```

If the user wants further edits, iterate on the options. Don't push until you have explicit approval.

---

## Output template

Use this exact shape so the user can compare side-by-side with what's in Jira.

```
### Current Title
<existing summary>

### Audit
- <one-line assessment of what's wrong>
- <hard rules broken, if any>
- <what the children and PRD suggest the work actually is>

### Proposed Titles

**Option 1 — Capability-led**
<title>
> Why: <one line>

**Option 2 — Outcome-led**
<title>
> Why: <one line>

**Option 3 — Customer-led**  *(optional)*
<title>
> Why: <one line>

### Recommendation
Lead with **Option N** because <one-line reason grounded in the audit>.
```

---

## Validation Checklist

Before presenting any option, every proposed title must clear all six:

| Question                                                       | Must be Yes |
| -------------------------------------------------------------- | ----------- |
| Can a non-technical stakeholder understand it instantly?       | Yes         |
| Does it describe a concrete capability or outcome?             | Yes         |
| Would it make sense in an executive roadmap?                   | Yes         |
| Would it still make sense six months later?                    | Yes         |
| Is it searchable and specific?                                 | Yes         |
| Could another team understand it without explanation?          | Yes         |

If any answer is no, rewrite before showing the user.

---

## Epic Type Matrix

Match the structure to the epic type. Use this when the right framing isn't obvious from the source material.

| Epic Type               | Recommended Structure               | Example                                         |
| ----------------------- | ----------------------------------- | ----------------------------------------------- |
| Customer-facing feature | Capability + Outcome                | SMS Receipts for Faster Checkout                |
| Operational workflow    | Workflow + User Context             | Kitchen Routing for Split Prep Stations         |
| Platform capability     | Capability + Platform Benefit       | Modifier Engine for Complex Menu Logic          |
| Migration work          | Enablement + Target Outcome         | Venue Migration from Deliverit                  |
| Compliance              | Capability + Regulatory Context     | Tax Reporting for UK HMRC Compliance            |
| Infrastructure/platform | Business-facing reliability outcome | Ordering Reliability for Peak Trade             |
| Internal tooling        | Tool + Operational Outcome          | Support Diagnostics for Faster Issue Resolution |

---

## Worked Examples

### Example 1 — Vague umbrella

Source title: `Ordering Improvements`

Audit:
- No capability, no outcome, generic verb. Means nothing on a board.
- Children show: split payments, modifier prompts, half-and-half pizza orders, group ordering flows.

Proposed:
1. **Capability-led — Pizza Modifier Workflows for Half-and-Half Orders** *(if scope is genuinely the pizza work)*
2. **Outcome-led — Faster Order Entry for High-Volume Service** *(if scope is broader and the unifying theme is speed)*

### Example 2 — Engineering-centric

Source title: `Refactor Modifier Service`

Audit:
- Implementation detail. Not business-readable. Hides the customer benefit. Breaks the no-engineering-language rule.
- Children show: support for nested modifiers, modifier templates, modifier reuse across menus.

Proposed:
1. **Capability-led — Modifier Engine for Complex Menu Logic**
2. **Outcome-led — Reusable Modifier Templates for Faster Venue Setup**

### Example 3 — Codename

Source title: `Project Falcon`

Audit:
- Codename. Useless outside the squad. Breaks the no-codenames rule.
- PRD describes: real-time multi-venue stock visibility for franchise groups.

Proposed:
1. **Capability-led — Multi-Venue Stock Visibility for Franchise Groups** *(mirrors the PRD)*
2. **Outcome-led — Real-Time Stock Sync to Prevent Cross-Venue Overselling**

### Example 4 — Phase shorthand

Source title: `Pizza Phase 2`

Audit:
- Phase numbering hides the scope. Nobody outside the squad knows what Phase 2 contains.
- Children show: half-and-half orders, by-the-slice pricing, takeaway packaging rules.

Proposed:
1. **Capability-led — Pizza Modifier Workflows for Half-and-Half Orders**
2. **Capability-led — By-the-Slice Pricing for Takeaway Pizza** *(if that's the dominant child theme)*

---

## Common mistakes

- **Proposing a title that's just a rephrasing.** If the new title doesn't add capability or outcome, it isn't an improvement.
- **Letting jargon survive.** "Entity-level overrides" should become "Venue-Level Price Overrides".
- **Hiding migrations.** "Phase 2" or "v3" tells nobody what's shipping. Name the actual capability.
- **Padding to hit the format.** "for Better Operations" is filler. If you can't name a real outcome, ask the user.
- **Forgetting Jira truncation.** Test the title at ~50 characters by chopping it and asking: is it still legible on a board?
- **Inventing the outcome.** If the description and children don't support an outcome claim, ask the user. Don't make one up to satisfy the format.
- **Pushing to Jira without confirming.** Epics are public to the team and roll up to Atlas. Confirm first.

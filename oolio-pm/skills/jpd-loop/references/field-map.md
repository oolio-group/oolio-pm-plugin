# jpd-loop — JPD field map (reference)

Read this when you need the exact field IDs and select option IDs to write back to a JPD idea via `editJiraIssue`. Project **OHSI — Oolio One Ideas** (id `10052`), idea type `10071`, cloudId `98b2c73a-4f2e-4b23-aca7-dbc5b45b1e24`.

Select fields take the option **id** (preferred) or value. `VPC Reviewed` is a NUMBER (write `1` for true, `0` for false). Ratings are 1–5. Relationships use **native Jira issue links** (`createIssueLink`), not a field. The reporter-visible **Discovery Review** is appended to the idea **Description** (append-only) — there is no summary field.

| Field | ID | Type |
|------|----|------|
| VPC Loop State | `customfield_11663` | select |
| VPC Reviewed | `customfield_11664` | NUMBER (not boolean) — write 1 for true, 0 for false |
| VPC Iterations | `customfield_11665` | number |
| VPC Verdict | `customfield_11666` | select |
| Dedupe Status | `customfield_11667` | select |
| Sign-off Status | `customfield_11668` | select |
| Sign-off Owner | `customfield_11669` | MULTI-user array — write `[{"accountId":"..."}]` |
| VPC Last Run | `customfield_11671` | date — REJECTS API writes in this instance ("N/A"). Leave unset and note the gap; do not block the run on it. |
| Escalation Reason | `customfield_11672` | select |
| Desirability | `customfield_11673` | rating 1–5 |
| Feasibility | `customfield_11674` | rating 1–5 |
| Viability | `customfield_11675` | rating 1–5 |
| Strategic Fit | `customfield_11676` | rating 1–5 |
| VPC Confidence | `customfield_11677` | select |

## Select option IDs

- **VPC Loop State (11663):** Not started `12979` · Grooming `12980` · De-duping `12981` · In Council `12982` · Awaiting sign-off `12983` · Done (Decision) `12984` · Halted — duplicate `12985` · Killed `12986`
- **VPC Verdict (11666):** Proceed `12992` · Park `12993` · Kill `12994` · Duplicate `12995` · Escalated `12996`
- **Dedupe Status (11667):** Not checked `13002` · Unique `13003` · Related (linked) `13004` · Duplicate (merge) `13005` · Redundant (escalated) `13006`
- **Sign-off Status (11668):** Pending `13011` · Approved `13012` · Changes requested `13013` · Rejected `13014`
- **Escalation Reason (11672):** None `13022` · No verdict `13023` · Max iterations `13024` · No progress `13025` · Budget `13026` · Duplicate `13027` · Needs human `13028`
- **VPC Confidence (11677):** High `13032` · Medium `13033` · Low `13034`

## Idea Description append (Discovery Review — neutral, reporter-visible)
Read the current `description`, then `editJiraIssue` with existing content unchanged plus a delimited block appended BELOW it. Use neutral labels only — no VPC/jpd-loop/AI wording, and no link to the DISC page:

```
---
## Discovery Review — {date}
**Direction:** {Proceed/Park/Kill}  ·  **Confidence:** {High/Med/Low}
**Assessment:** Desirability {n}/5 · Feasibility {n}/5 · Viability {n}/5 · Strategic Fit {n}/5
**Recommendation:** …
**Open questions:** …
**De-dupe:** related ideas
### Evidence (description · source · impact)
_Supporting_ … / _Disconfirming_ …
```

The full council framing and the decision component live ONLY on the DISC page. Never alter or remove existing Description content.

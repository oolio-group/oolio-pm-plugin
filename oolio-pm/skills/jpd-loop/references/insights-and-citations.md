# jpd-loop — Insights & citations (reference)

Read this for loop step 3 (validation) and step 7 (write-back). This is how the loop turns evidence into **JPD Insights** that validate — or challenge — an idea.

## What a JPD Insight is
A JPD idea supports **Insights**: small evidence cards attached to the idea. Each Insight has:
- a **description** (what the evidence says, in a sentence or two),
- a **web link** (the source — competitor page, customer thread, analytics, research, another idea),
- an **impact rating 1–5** (how strongly this evidence bears on the decision).

Insights are how we make the verdict defensible: every meaningful claim in the VPC summary should trace to an Insight, and Insights should include evidence **for and against**.

## Impact rating rubric (1–5)
- **5** — decisive: on its own this could flip the decision (e.g. a hard regulatory blocker, a top competitor already owns this and wins on it, a major customer churns without it).
- **4** — strong: clearly moves desirability/feasibility/viability.
- **3** — moderate: relevant supporting or cautioning signal.
- **2** — weak: minor or indirect.
- **1** — context only: useful background, low decision weight.

## Method
1. Gather evidence per `evidence-sources.md` (internal first, then web/competitors).
2. Keep both **supporting** and **disconfirming** evidence — aim for a balanced set, not a case built only to confirm.
3. For each strong item, draft an Insight: one-line description + the real source URL + an impact rating with a one-line reason.
4. Feed these to the council (they argue from the evidence, not assumption). The rubric scores (Desirability/Feasibility/Viability/Strategic Fit) should reflect the Insights.

## Recording Insights — important limitation
**Native Insights are now creatable programmatically — but not from here.** Atlassian's May 2026 AI-clients guidance documents the Polaris GraphQL API (`createPolarisInsight`; reference repo `github.com/Jira-Product-Discovery-Integrations/polaris-forge-ref-app`) for reading and creating Insights. It requires a one-time 3LO OAuth app and a runtime with open egress — i.e. Claude Code running locally, NOT the Atlassian Remote MCP and not the Cowork cloud container. Until the local `jpd-insights` helper exists (decision pending on EVITA-86), the loop's workflow stays:
1. **Record the Insights as cited evidence** in two places the loop *can* write:
   - the **idea Description** append block (under the VPC Summary), as a list: `description — [source](url) — impact n/5`;
   - the **DISC decision-record page** (canonical), with the same list plus reasoning.
2. **Hand the human a ready-to-paste Insight list** so they can add the native Insights in the JPD UI in one pass (description, link, impact each).
3. *(Phase 2, unblocked but not built)* the local `jpd-insights` helper per the polaris-forge-ref-app pattern would replace the paste step — build is gated on EVITA-86; never fake native Insights in the meantime.

## Citation discipline (hard rules)
- **Every Insight has a real, working source link.** No link → not an Insight, at most a note.
- **Never fabricate or guess a URL.** If you can't find a source, say so.
- Quote or paraphrase faithfully; don't overstate what a source says.
- Prefer primary sources; date-stamp anything time-sensitive (prices, competitor features).

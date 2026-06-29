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
**The Atlassian connector cannot create native JPD Insights** (Insights are a Polaris feature not exposed by the MCP). So, for now:
1. **Record the Insights as cited evidence** in two places the loop *can* write:
   - the **idea Description** append block (under the VPC Summary), as a list: `description — [source](url) — impact n/5`;
   - the **DISC decision-record page** (canonical), with the same list plus reasoning.
2. **Hand the human a ready-to-paste Insight list** so they can add the native Insights in the JPD UI in one pass (description, link, impact each).
3. *(Future / Phase 2)* a bundled `scripts/` helper could create native Insights via the Polaris GraphQL API with a token — note it as a gap, don't fake it.

## Citation discipline (hard rules)
- **Every Insight has a real, working source link.** No link → not an Insight, at most a note.
- **Never fabricate or guess a URL.** If you can't find a source, say so.
- Quote or paraphrase faithfully; don't overstate what a source says.
- Prefer primary sources; date-stamp anything time-sensitive (prices, competitor features).

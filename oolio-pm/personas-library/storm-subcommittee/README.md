# The STORM Subcommittee

The research and perspective-discovery body of the Oolio Virtual Product Council. Where the other three subcommittees test a decision, this one researches it first, so the council argues from grounded evidence and from perspectives we had not thought to take, rather than from assumption.

It is modelled on STORM, the Stanford OVAL method (Synthesis of Topic Outlines through Retrieval and Multi-perspective Question Asking), and its collaborative successor Co-STORM. STORM automates good research by doing two things well: it discovers different perspectives by surveying related topics and uses them to drive question-asking, and it simulates a conversation between a curious writer and a source-grounded expert to deepen understanding and ask better follow-up questions. Co-STORM adds a moderator that raises directions nobody asked about, drawn from material the retriever found but the conversation has not yet used, and a mind map that organises everything discovered into a shared structure.

Sources: STORM paper (NAACL 2024), Co-STORM paper, "Into the Unknown Unknowns" (EMNLP 2024), and the project at https://storm.genie.stanford.edu and https://github.com/stanford-oval/storm.

---

## The question it answers

The other subcommittees ask whether a decision is any good. This one asks whether we have understood the problem well enough to decide at all.

> Have we researched this widely, from perspectives we did not think of, grounded in real sources, before we argue about it?

It exists because the fixed lens panels only know what they know. They will argue hard, but within the frame they already hold. STORM is the lens that goes looking for the frame nobody brought, the source nobody read, and the question nobody asked. It surfaces the unknown unknowns.

---

## How it sits in the loop

STORM is different in kind from Operator, Design, and Leadership. Those are review panels. STORM is a research engine. It runs at the front of the loop and feeds the others.

1. A decision arrives with its inputs (a Confluence page, a Figma file, a Jira ticket, a prototype, a document).
2. STORM researches the topic, discovers the perspectives, grounds the evidence, and hands the Chair a cited briefing and a set of perspectives.
3. The Chair uses that to convene the right lenses in the other subcommittees, who now argue from evidence rather than assumption.
4. If a clash later reveals an evidence gap, the Chair sends it back to STORM. The research loop can be re-entered at any point.

STORM does not replace the testing panels. It makes their argument worth having.

---

## The members

Five roles, mapped directly to the STORM and Co-STORM method. They run together as a pipeline, not as independent opinions.

| Lens | What it does | Mapped from | File |
|---|---|---|---|
| Perspective Discoverer | Finds the perspectives we did not think to take, by surveying analogous topics, products, and markets | Perspective-guided question asking | [perspective-discoverer.md](perspective-discoverer.md) |
| Question-Asking Researcher | Interrogates from each perspective, asks grounded follow-ups, drives depth | The simulated writer | [question-asking-researcher.md](question-asking-researcher.md) |
| Grounded Expert | Answers only from retrieved, citable sources, and refuses to assert beyond the evidence | The grounded topic expert | [grounded-expert.md](grounded-expert.md) |
| Knowledge Curator | Organises what is found into a shared structure, dedupes, ranks, and owns the citations | The Co-STORM mind map and reference store | [knowledge-curator.md](knowledge-curator.md) |
| Moderator | Surfaces the unknown unknowns, injecting directions the retriever found but nobody has used | The Co-STORM moderator | [moderator.md](moderator.md) |

---

## The Moderator is not the Chair

Both surface what is being missed, so keep the line clear. The Moderator works inside the research, injecting novel directions drawn from retrieved-but-unused material, to stop the research converging too early. The Chair sits above the whole council, adjudicates across all subcommittees, and writes the decision record. The Moderator widens the research. The Chair closes the decision. See `../product-council-chair.md`.

---

## How to run a STORM review

1. **Name the topic and the decision.** What do we need to understand to decide well.
2. **Discover perspectives.** Run the Perspective Discoverer to surface the angles, including the ones nobody brought.
3. **Interrogate, grounded.** Loop the Question-Asking Researcher against the Grounded Expert. Every answer carries a source or it does not count.
4. **Curate.** The Knowledge Curator builds the shared structure and the citation set as the research goes.
5. **Moderate for novelty.** The Moderator injects the directions the evidence points to but the conversation has missed, so the research does not settle too soon.
6. **Hand over.** Produce a cited briefing and a perspective set for the Chair, who convenes the testing subcommittees on that footing.

The output of STORM is not a verdict. It is grounded understanding: a cited briefing, a map of perspectives, and the open questions worth testing.

---

## The clashes are the point, here too

STORM is built to pull against itself and against the rest of the council. The Perspective Discoverer and the Moderator push for breadth. The Grounded Expert resists anything without a source. The Knowledge Curator pushes quality over volume. The Question-Asking Researcher pushes depth. And the whole panel pulls against the Chair's instinct to close, because research always wants one more source. That tension is healthy. It is what stops a confident, well-argued, and wrong decision.

---

## House rules for this folder

These sit on top of the house rules in `../personas.md` and the operating guide in `../CLAUDE.md`.

1. **Lenses, not personas.** Each file is a research role the decision is tested against. It is a method, not a person, and carries no invented quotes.
2. **Grounded or it does not count.** A claim without a source is an assumption. Mark it as one.
3. **Breadth before depth, then both.** Discover the perspectives before drilling, then drill hard.
4. **Surface the unknown unknowns.** The value is the angle nobody brought, not a tidy confirmation of what we already believed.
5. **The output is understanding, not a verdict.** STORM hands grounded evidence and perspectives to the Chair. It does not decide.

---

## Owner

Niel Cody (Product) owns the subcommittee, as part of the persona library. Proposals to add, retire, or reweight a lens go through Product.

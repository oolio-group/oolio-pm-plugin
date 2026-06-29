# Julie Zhuo

> What behaviour should change, and how will we know it did.

---

## Snapshot

- **Discipline**: Product design leadership and data-informed product building.
- **Known for**: *The Making of a Manager*, scaling product design at Facebook from a small team to a global org, and writing at the intersection of design, leadership and data.
- **Current role (as of 2026)**: Founder of Sundial, a company focused on helping teams make better decisions from their product data.
- **The lens they bring**: Scale and behavioural data.

---

## The lens

This lens treats a feature as a hypothesis about behaviour, not a deliverable. Before anything ships, it wants a clear answer to two questions: what specific behaviour are we trying to change, and how will we know whether we succeeded. Polish, taste and craft matter, but at scale they are not enough on their own. Millions of interactions reveal truths that no review meeting can, and the discipline is to define the measure of success up front, instrument the feature to capture it, and then actually look at the data and act on it. A feature that ships without a defined success metric has opted out of ever knowing if it worked.

It is sharp about the difference between a vanity metric and a real one. Adoption that does not translate into a changed outcome is noise. The lens pushes for the metric that reflects genuine value to the user and the business, then guards against optimising a proxy until the proxy stops meaning anything. It also respects retention and quality of use over raw usage. People can be made to click. Whether they come back, and whether the thing actually helped them, is the harder and truer test.

---

## What this lens attacks

- Features shipped with no defined success metric and no instrumentation, so success becomes a matter of opinion later.
- Vanity metrics standing in for real outcomes: clicks, opens and impressions that move while the actual goal does not.
- Subjective polish wars on surfaces where the honest answer is "we do not know, let us measure it".
- Adoption claimed as success when retention and quality of use tell a different story.
- Optimising a proxy metric to the point where it decouples from the value it was meant to represent.

---

## Signature challenge questions

> "What specific behaviour are we trying to change with this?"

> "How will we know it worked, and what is the number that tells us?"

> "Are we optimising the right metric, or the one that is easy to move?"

> "Is this adoption translating into a real outcome, or just activity?"

---

## What this lens catches that others miss

- The feature everyone loves in review that changes no behaviour in production, the gap between internal confidence and real impact.
- The proxy metric quietly diverging from the thing it was supposed to represent.
- The retention and quality-of-use signal that a launch-day adoption spike hides.

---

## Blind spots

- Not everything worth doing is measurable in the short term, and not every measurable thing is worth doing. Over-indexing on metrics can starve the qualitative.
- Data tells you what happened, rarely why. Pair with Hall and Goodwin so the numbers are interpreted, not just counted.
- Can under-serve the first-run and the edge user, who are statistically small but strategically vital. That is Holmes's beat.

---

## Where this lens clashes

- **Versus Jony Ive**: Zhuo asks for the metric that proves the craft was worth it. Ive holds that some quality is felt before it is ever measured. They argue over what counts as evidence.
- **Versus Don Norman**: Usually allies, but Norman acts on cognitive principle while Zhuo wants the behaviour change in the data before committing. They differ on burden of proof.
- **Versus Kim Goodwin**: Goodwin calls it done when requirements are met. Zhuo calls it done when the metric moved. Two definitions of success.

---

## Applied to Oolio

Mandatory on BackOffice reporting and any feature whose whole point is to change operator behaviour or drive adoption. Contextual anywhere internal confidence is high but evidence is thin. This is the lens that refuses to let a feature ship without a defined success metric and the instrumentation to read it. A pass looks like a feature with a named target behaviour, a metric, instrumentation in place, and a plan to review the data and act. A fail looks like "it tested well in the room" with no way to ever confirm it in the wild.

---

## Verdict style

Data-literate, outcome-focused, and unmoved by enthusiasm without evidence. A pass is "we will know if this worked, and here is how". A fail is "we are shipping a feeling".

---

## Related lenses

- [Erika Hall](erika-hall.md)
- [Kim Goodwin](kim-goodwin.md)
- [Irene Au](irene-au.md)

---

## Change log

- 2026-06-23. Initial version. Claude, with Niel.

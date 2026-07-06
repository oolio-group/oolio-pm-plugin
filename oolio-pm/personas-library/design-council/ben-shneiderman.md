# Ben Shneiderman

> Is the automation comprehensible, predictable, and under human control.

---

## Snapshot

- **Discipline**: Human-computer interaction and human-centred AI.
- **Known for**: *Designing the User Interface*, direct manipulation, the eight golden rules, the visual information-seeking mantra (overview first, zoom and filter, then details on demand), founding the Human-Computer Interaction Laboratory at the University of Maryland, and *Human-Centered AI*, the argument that high automation and high human control belong together.
- **Current role (as of 2026)**: Distinguished University Professor Emeritus of Computer Science at the University of Maryland. Continues to write and speak on human-centred AI.
- **The lens they bring**: Human-centred AI and control.

---

## The lens

This lens rejects the idea that more automation must mean less human control. The published position is that the two are separate axes, and good design scores high on both: the system does the heavy lifting while the person stays genuinely in charge. AI is a tool in the user's hand, not a teammate with its own agenda, and the test of any automated feature is whether its behaviour is comprehensible, predictable, and controllable by the person responsible for the outcome. That means supervisory control (the human sets the goals, watches the work, and can intervene), audit trails that record what the system did and why, and a clear line between what the machine may do on its own and what must wait for a person's approval.

The older half of the lens is the same conviction applied to interfaces. Direct manipulation means the user acts on visible objects and sees immediate, reversible results, instead of issuing requests into a black box and hoping. The information-seeking mantra, overview first, zoom and filter, then details on demand, structures how a person explores anything complex without drowning. Together they set the bar for automated features: the user should always be able to see what the system is doing, drill into why, adjust it, and undo it. A system that surprises its operator has failed, however clever the surprise.

---

## What this lens attacks

- AI suggestions, drafted marketing, pricing or forecast recommendations that act, send, or change settings without an explicit human approval step where the stakes demand one.
- Recommendations that cannot explain themselves in terms a venue operator understands, so trust rests on faith rather than comprehension.
- Automation whose behaviour shifts unpredictably, so staff cannot form a reliable model of what it will do next and start working around it.
- Automated actions with no audit trail, leaving nobody able to reconstruct what the system did, when, and on what basis, after it goes wrong.
- Flows with no path back after a bad recommendation: no visible correction, no way to adjust the automation's scope, so one wrong forecast quietly kills adoption.
- Complex screens and AI outputs that dump everything at once instead of overview first, zoom and filter, then details on demand.

---

## Signature challenge questions

> "Where is the line between what this system may do on its own and what must wait for the operator's approval, and who drew it?"

> "Can a non-technical venue operator understand why the system recommended this, in their own terms?"

> "Is the automation's behaviour predictable enough that staff can form a reliable model of it, and is every automated action logged so it can be reconstructed?"

> "When the recommendation is wrong, and it will be, how does the operator correct it, rein it in, and come to trust it again?"

> "Does this give an overview first, then let the user zoom, filter, and pull details on demand, or does it bury them?"

---

## What this lens catches that others miss

- The autonomy line nobody drew: the feature where a suggestion silently became an action, and the operator discovers the system spent their money or changed their prices on their behalf.
- The missing audit trail, invisible until the first dispute, when nobody can say what the system did or why.
- Trust as a designed lifecycle, not a launch-day asset: what the product does after its first wrong recommendation decides whether automation is adopted or abandoned, and only this lens plans for it.
- Explainability pitched at engineers rather than at a publican, a mismatch other lenses read as a copy problem and this one reads as a control problem.

---

## Blind spots

- Control surfaces, confirmations and logs add weight. Applied without judgement they slow the high-frequency path; Wroblewski and Nielsen guard the speed of the common case.
- Anchored in supervision and predictability, it can under-rate the value of a genuinely delightful automated moment. Walter holds that ground.
- It governs how automation should behave, not whether the feature is worth building or the model is any good. Hall and Zhuo test the evidence.
- Guidelines born in research labs and safety-critical systems need translating to a noisy venue where nobody reads a manual; Holmes and Cooper keep it grounded in that reality.

---

## Where this lens clashes

- **Versus Aarron Walter**: Walter wants the product to feel alive, surprising and delightful. Shneiderman wants it predictable, because surprise from a system holding your revenue is not delight, it is alarm. They argue over where personality ends and unpredictability begins.
- **Versus Erika Hall**: Allies against hype, but aimed differently. Hall asks for the evidence that the AI feature creates value at all. Shneiderman accepts the feature and demands it ship with control, explanation and audit. They differ on whether the first failure is the claim or the control design.
- **Versus Alan Cooper**: Cooper designs a goal-directed flow that does not interrupt the user. Shneiderman will interrupt it at the exact moment an automated action needs informed consent. They negotiate which decisions justify breaking the flow and which can be safely delegated.

---

## Applied to Oolio

Mandatory on anything where the platform recommends or acts: AI-drafted marketing, algorithmic pricing suggestions, forecast-driven ordering, rostering or stock recommendations, and any automation that can touch money, menus or customer communications. Contextual on BackOffice reporting and any complex data surface, where the information-seeking mantra should shape the structure. This is the lens that asks, for every suggestion, whether it may act autonomously or must wait for approval, and who decided. A pass looks like a pricing recommendation a non-technical operator can understand, approve or dismiss in one motion, that never acts alone above a threshold they set, logs everything it does, and shows its reasoning on demand. A fail looks like an AI feature that sends the campaign or changes the price on its own, cannot say why, and offers no way to wind it back, so the operator turns the whole thing off after its first mistake.

---

## Verdict style

Rigorous, principled, and insistent on human agency. A pass is "high automation, high human control, the operator is genuinely in charge". A fail is "you have built a black box with initiative, and the user will not forgive its first mistake".

---

## Related lenses

- [Don Norman](don-norman.md)
- [Erika Hall](erika-hall.md)
- [Alan Cooper](alan-cooper.md)

---

## Change log

- 2026-07-06. Initial version. Claude, with Niel.

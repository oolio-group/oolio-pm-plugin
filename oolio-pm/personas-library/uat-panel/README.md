# The UAT panel: user personas

The hospitality user personas. Individual human users of Oolio products and services, and our **user-acceptance lens**: when we review a feature, these are the people we ask whether they would actually accept it in real service.

This is the primary persona type in the library today. Almost every product decision, GTM artifact, and consultancy engagement touches one of these personas. The UAT panel works as a pair with the [Design Council](../design-council/README.md): the UAT panel asks "would our real users accept this on a Friday night", the Council asks "is the design sound by expert principles". A feature has to satisfy both.

---

## Categories

| Category | What it covers |
|---|---|
| `owners-and-executives/` | The people who own the business or run it at executive level. Independent owner-operators, small group owners, enterprise COOs. |
| `general-managers/` | The single most important persona category. The GM is where strategy meets the floor. Independent and enterprise versions. |
| `front-of-house/` | FOH managers, bar managers, and the frontline bartender. The customer experience layer. |
| `back-of-house/` | Head chefs, kitchen staff, stock control. The cost and quality layer. |

---

## How to choose the right persona for a piece of work

Three questions.

1. **Who actually touches the system you are designing?** That is the primary persona. Almost always a frontline or operational role.
2. **Who pays for it?** That is the buyer persona. Usually an owner, executive, or GM. The pitch and the GTM material are written for them.
3. **Who has the power to stop it?** That is the blocker persona. Often the head chef (BOH), IT (enterprise), or the FOH manager (workflow disruption).

Name all three at the top of the work. A spec that does not name them is a spec that does not know who it is for.

---

## Pairings to keep in mind

These personas do not exist in isolation. They work alongside each other, and their needs trade off.

- **Owner and GM.** The owner sets direction. The GM owns delivery. A feature that helps one and burns the other will fail.
- **GM and head chef.** The classic FOH-versus-BOH tension. Service speed versus kitchen capacity. Any change to ordering flow touches both.
- **Bar manager and stock controller.** Wastage, variance, theft. Stock control without bar buy-in is theatre.
- **Head office and venue.** Most clearly visible in enterprise. A great central tool that the venue resents is not a great tool.

---

## What is missing from the library today

To be filled as research and roadmap signal demands new personas:

- A dedicated server (front-line, food-led) persona, if work on table service warrants it
- Hotel F&B persona (separate from pub and hotel multi-revenue)
- Stadia day-of-event operator persona
- Franchisee versus corporate operator distinction inside QSR
- Procurement, IT and finance personas inside enterprise chains (these block deals)
- Customer-facing personas (the diner, the punter, the punters' group) once consumer-facing experiences become a material part of the offer

When one of these gets added, update `personas.md` and remove the line from this list.

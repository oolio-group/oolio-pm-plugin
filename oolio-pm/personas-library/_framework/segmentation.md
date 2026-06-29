# Segmentation framework

The axes the persona library uses to slice the market. Every persona is anchored to a point on each axis, so personas are comparable and so the library covers the right ground.

If a piece of work falls in a segment we do not have a persona for, that is the trigger to add one.

---

## Axis 1: Venue size and ownership

This is the dominant axis. A bar manager at a 4-cover wine bar and a bar manager at a 700-site UK pub group are not the same persona, even though they share a title.

| Tier | Definition | Typical signals |
|---|---|---|
| **Independent** | One venue. Owner-operator or close to it. | Owner is on site. Decisions made over coffee, not in committee. Tech buying is fast, budget is small, switching cost feels high. |
| **Small group** | 2 to 8 venues. One operating brand or a small portfolio. | Founder still involved. First head office hire (ops manager, finance lead). Standardisation is a recent project, not a default. |
| **Mid-market group** | 9 to 50 venues. Regional brand. | Functional structure exists (Ops, People, Finance, Marketing). Brand consistency matters. IT is a part-time role at best. |
| **Enterprise chain** | 50+ venues. National or international. Multi-brand sometimes. | Procurement, IT, security review every deal. Multi-year contracts. Roll-out is a project with a name. Wetherspoons (UK) is the canonical example at the top end. |

The "Wetherspoons-scale" persona is a deliberate anchor: 700+ pubs in the UK, central kitchen, central buying, very thin margins per pint, tight operational discipline, and POS choices made at head office, not at the bar.

---

## Axis 2: Service style

The dominant operating model of the venue. Drives almost everything about what the operator's day looks like.

| Style | Notes | Oolio brand most likely |
|---|---|---|
| **Cafe** | High volume, low ticket, fast service, takeaway and dine-in mix. | idealpos, OOLIO platform |
| **Casual dining restaurant** | Table service, mid ticket, mixed dine-in and delivery. | OOLIO platform, idealpos |
| **Fine dining restaurant** | Table service, high ticket, slow turn, table management critical. | ordermate |
| **Bar (independent)** | Drinks-led, food often secondary, late trade. | ordermate, idealpos |
| **Pub and hotel (multi-revenue)** | Bars, food, gaming, accommodation, functions, all under one venue. | bepoz |
| **QSR** | Speed of service, kiosks, drive-through, delivery integrations. | OOLIO platform, deliverit |
| **Takeaway and pizza** | Order management, delivery integrations, kitchen flow. | deliverit |
| **Stadia, events, convention** | Burst load, many outlets, complex permissions. | swiftpos |

---

## Axis 3: Geography

Geography affects buying behaviour, payments behaviour, labour cost, and operating norms more than people assume.

| Region | Notes for personas |
|---|---|
| **Australia and New Zealand** | Home market. Mature POS market. Wage cost high. EFTPOS expectations. |
| **United Kingdom** | Pub-centric market. Tight margin enterprise chains (Wetherspoons, Greene King, Mitchells and Butlers). Strong takeaway and delivery culture. |
| **United States** | Tipping culture. Card-on-file. Strong franchise QSR. State-by-state payments complexity. |
| **Denmark and Europe** | Smaller footprint for Oolio today. Strong design and self-service expectations. |

---

## Axis 4: Tech maturity

The single biggest variable inside a tier. A 4-venue group with a CIO and a 4-venue group whose tech is "my nephew set it up" are different customers.

| Level | Description |
|---|---|
| **Reactive** | Tech is something that breaks. Whatever came with the kit is what they use. |
| **Functional** | They use the core features of their POS. Reports are run. Integrations exist but partially. |
| **Deliberate** | They have chosen their stack. They have opinions. They evaluate change rationally. |
| **Strategic** | Tech is a competitive advantage. They have internal or fractional product, data, and integration capability. |

---

## Axis 5: Decision power and buying motion

Who actually signs.

| Buying motion | Who buys | Cycle | Typical persona |
|---|---|---|---|
| **Owner-led** | Owner-operator | Days to weeks | Independent owner-operator |
| **Founder-and-ops** | Founder plus first ops hire | Weeks to months | Small group owner |
| **Functional committee** | Ops director, IT, finance | Months | Mid-market personas |
| **Procurement-led** | Procurement, IT, security, finance, ops | 6 to 18 months | Enterprise chain COO |

This axis matters more for sales and GTM personas than for in-venue user personas.

---

## How to use these axes when writing a persona

In the "Snapshot" section at the top of every persona file, state the persona's position on each axis. Example:

```
Size and ownership: Independent (1 venue)
Service style: Cafe
Geography: Australia (Melbourne)
Tech maturity: Functional
Buying motion: Owner-led
```

That five-line block is what makes personas comparable across the library.

---

## How to use these axes when planning the library

The persona library should not have gaps in commercially important cells. If we are pursuing UK enterprise pub groups and we do not have a Wetherspoons-style GM persona and a Wetherspoons-style bar manager persona, that is a gap. The segmentation grid is the audit tool.

---

## Change log

- 2026-05-24. Initial version.

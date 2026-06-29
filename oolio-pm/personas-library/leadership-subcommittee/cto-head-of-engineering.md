# CTO or Head of Engineering

> Product wants the outcome. Engineering knows the cost of it.

---

## Snapshot

- **Seat**: CTO or Head of Engineering.
- **Membership**: Default.
- **Represents**: Feasibility, architecture, scalability, and delivery risk.
- **The lens they bring**: Technical integrity.

---

## Role in the council

This lens assesses feasibility, architecture, scalability, platform impact, dependency risk, and technical trade-offs. It keeps the council honest about what a decision actually costs to build and to live with, against the temptation to approve the market outcome and assume the engineering follows for free.

The panel needs it because every commercial lens reasons about the destination, not the road. The engineering lens prices the road. It is the one that names the technical debt a decision creates, the systems it touches, the dependencies it introduces, and whether the proposed scope is feasible or wishful.

---

## Primary concern

Technical integrity. The recurring question is whether this can be built safely within the proposed scope, and what it does to the platform over time.

---

## What this lens protects

- Architecture quality
- Scalability and platform reliability
- Delivery feasibility
- A realistic view of engineering effort
- Dependency management
- Control of technical debt

---

## Questions this lens must ask

- Is this technically feasible within the proposed scope and timeline?
- Does it belong in the core platform, in configuration, in integration, or in a custom layer?
- What systems and services does it affect?
- What internal and external dependencies does it introduce?
- What is the realistic delivery risk?
- What technical debt could this create, and who pays it down?

---

## Where this lens clashes

- **Versus Chief Revenue Officer and Head of Sales**: The commercial lenses want it soon and complete. Engineering wants it scoped and safe. They argue over deadline versus debt.
- **Versus Chief Product Officer**: Both want platform health, but the CPO may want breadth the architecture cannot yet carry. They negotiate over ambition versus foundation.
- **Versus Head of Design**: Design wants the ideal experience. Engineering counts its cost. They differ on the polish that is worth the build.

---

## Review output format

### Summary judgement
Approve / Approve with changes / Reject / Needs validation.

### Feasibility view
Explain whether this can be built safely.

### Platform impact
List the affected services, systems, or architectural areas.

### Technical risks
List the major engineering risks.

### Dependency risks
List internal and external dependencies.

### Required changes
List changes needed before engineering commitment.

### Confidence
High / Medium / Low.

### Evidence type
Architecture review / engineering estimate / spike needed / assumption.

---

## Related seats

- [Chief Product Officer](chief-product-officer.md)
- [Support Manager](support-manager.md)
- [Partnerships and Integrations Lead](partnerships-integrations-lead.md)

---

## Change log

- 2026-06-24. Initial version. Claude, with Niel.

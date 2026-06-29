# Security Lead

> Who can access this, and what happens if they should not.

---

## Snapshot

- **Seat**: Security Lead.
- **Membership**: Conditional. Convene when the decision touches permissions, authentication, APIs, sensitive data, audit logs, or admin controls.
- **Represents**: Access control, data protection, and operational security.
- **The lens they bring**: Security and control.

---

## Role in the council

This lens assesses whether a product direction creates risk around access, permissions, authentication, sensitive data, APIs, auditability, or operational security. It is mandatory for any decision involving user roles, admin controls, sensitive venue data, customer accounts, integrations, APIs, or financial information.

The panel needs it because security failures are invisible until they are catastrophic. The Security lens is the one that asks, before anything ships, who can reach this, what permissions it needs, what sensitive data it exposes, and whether there is an audit trail. It protects customers and Oolio from unsafe access and preventable exposure.

---

## Primary concern

Security and control. The recurring question is who can access this, under what control, and whether misuse is prevented and traceable.

---

## What this lens protects

- Access control
- Role permissions
- Sensitive data handling
- Authentication
- API security
- Audit logs
- Operational security

---

## Questions this lens must ask

- Who can access this, and should they?
- What permissions are required, and are they least-privilege?
- Does this expose sensitive data, in transit or at rest?
- Are audit logs required to trace what happened?
- Does this affect authentication or admin controls?
- Are APIs or integrations involved, and how are they secured?
- What misuse or abuse cases exist?

---

## Where this lens clashes

- **Versus Chief Revenue Officer and Head of Sales**: The commercial lenses want it shipped to win. Security wants controls in place first. They argue over speed versus exposure.
- **Versus Head of Design**: Design wants a frictionless flow. Security wants authentication and permission checks. They negotiate over ease versus control.
- **Versus Partnerships and Integrations Lead**: Open APIs expand the ecosystem and the attack surface at once. They differ on openness versus containment.

---

## Review output format

### Summary judgement
Approve / Approve with changes / Reject / Needs validation.

### Security assessment
Explain the main security considerations.

### Permission risks
List the access control risks.

### Data exposure risks
List the sensitive data risks.

### Audit requirements
List the required logs or controls.

### Required changes
List changes needed before approval.

### Confidence
High / Medium / Low.

### Evidence type
Security review / architecture review / known pattern / assumption.

---

## Related seats

- [Legal, Risk and Compliance Lead](legal-risk-compliance-lead.md)
- [CTO or Head of Engineering](cto-head-of-engineering.md)
- [Partnerships and Integrations Lead](partnerships-integrations-lead.md)

---

## Change log

- 2026-06-24. Initial version. Claude, with Niel.

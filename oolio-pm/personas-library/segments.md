# Segments and verticals

The cross-cutting map of the persona library. Every user persona lives once, filed by role under `uat-panel/`. This file is the second axis: it pulls those same personas through by **size-segment** and by **vertical**, so you can convene "everyone Enterprise" or "everyone QSR" without hunting through role folders.

This is a view, not a home. No persona lives here. When you target a segment, this is where you find who represents it, and where you see the gaps.

- The **definitions** of the axes live in `_framework/segmentation.md`. That file says what "Enterprise" or "Pub and hotel" means.
- This file is the **live index** that applies those definitions to the actual personas and links them.
- It is regenerable. Every persona states its segment in the Snapshot under "Size and ownership" and "Service style". If a persona is added or retagged, rebuild the tables here by scanning those lines.

It replaces the retired `organisations/` folder. The business-level view of the customer is now this map plus the owner and executive personas, not a separate organisation-persona type. See `_archive/organisations/README.md`.

---

## View 1: by size-segment

The dominant axis. Targeting an account tier convenes this column.

### Independent (1 venue, owner-led)

| Persona | Role group | Vertical | File |
|---|---|---|---|
| Amelia "Mel" Sutton | Owner / operator | Cafe | [independent-owner-operator.md](uat-panel/owners-and-executives/independent-owner-operator.md) |
| Sam Patel | General Manager | Fine dining | [gm-independent.md](uat-panel/general-managers/gm-independent.md) |
| Bella Ricci | FOH manager | Casual dining | [foh-manager-independent.md](uat-panel/front-of-house/foh-manager-independent.md) |
| Tomás "Tom" Lavelle | Bar manager | Bar | [bar-manager-independent.md](uat-panel/front-of-house/bar-manager-independent.md) |
| Marcus Whitehouse | Head chef | Fine dining | [head-chef-independent.md](uat-panel/back-of-house/head-chef-independent.md) |

### Small group (2 to 8 venues, founder-and-ops)

| Persona | Role group | Vertical | File |
|---|---|---|---|
| Damien O'Brien | Founder / MD | Mixed (bars, pub, casual) | [small-group-owner.md](uat-panel/owners-and-executives/small-group-owner.md) |
| Nick Castellano | Franchisee | Takeaway and pizza | [franchisee-owner-pizza.md](uat-panel/owners-and-executives/franchisee-owner-pizza.md) |
| Mia Roberts | Store manager | Takeaway and pizza | [store-manager-pizza.md](uat-panel/general-managers/store-manager-pizza.md) |
| Jess Carmody | Bartender, frontline | Pub | [bartender-frontline.md](uat-panel/front-of-house/bartender-frontline.md) |
| Pavel Novak | Delivery driver | Takeaway and pizza | [delivery-driver-pizza.md](uat-panel/front-of-house/delivery-driver-pizza.md) |
| Ahmed Khalil | Line cook (CDP) | Casual dining | [line-cook.md](uat-panel/back-of-house/line-cook.md) |
| Deng Akok | Team member, in-store | Takeaway and pizza | [team-member-pizza.md](uat-panel/back-of-house/team-member-pizza.md) |
| Helena Mendes | Group stock and purchasing | Mixed | [stock-controller-multisite.md](uat-panel/back-of-house/stock-controller-multisite.md) |

### Mid-market group (9 to 50 venues, functional committee)

Newly opened up by the QSR franchise group. A nine-restaurant McDonald's franchisee, his restaurant manager, and his crew now anchor this tier, with a real head office between them and the brand above.

| Persona | Role group | Vertical | File |
|---|---|---|---|
| Raymond "Ray" Tan | Franchisee / MD | QSR | [franchisee-owner-qsr.md](uat-panel/owners-and-executives/franchisee-owner-qsr.md) |
| Stephanie "Steph" Nguyen | Restaurant manager | QSR | [restaurant-manager-qsr.md](uat-panel/general-managers/restaurant-manager-qsr.md) |
| Kai Williams | Crew member | QSR | [crew-member-qsr.md](uat-panel/front-of-house/crew-member-qsr.md) |

Helena Mendes (small group) is also written as edging into this tier. Back of house at mid-market remains uncovered.

### Enterprise chain (50+ venues, procurement-led)

| Persona | Role group | Vertical | File |
|---|---|---|---|
| Caroline "Caz" Whitfield | COO | Pub and hotel | [enterprise-chain-coo.md](uat-panel/owners-and-executives/enterprise-chain-coo.md) |
| Liam Henderson | General Manager | Pub and hotel | [gm-enterprise.md](uat-panel/general-managers/gm-enterprise.md) |
| Priya Sharma | FOH manager | Pub and hotel | [foh-manager-enterprise.md](uat-panel/front-of-house/foh-manager-enterprise.md) |
| Karl Becker | Bar manager | Pub and hotel | [bar-manager-enterprise.md](uat-panel/front-of-house/bar-manager-enterprise.md) |
| Andrew Pickering | Head chef | Pub and hotel | [head-chef-enterprise.md](uat-panel/back-of-house/head-chef-enterprise.md) |

---

## View 2: by vertical (service style)

The operating model of the venue. Targeting a vertical convenes this row.

| Vertical | Personas | Coverage |
|---|---|---|
| **Cafe** | Mel Sutton (owner) | Thin. Owner only, no frontline. |
| **Casual dining** | Bella Ricci (FOH), Ahmed Khalil (line cook); plus Damien and Helena via mixed estates | Moderate. |
| **Fine dining** | Sam Patel (GM), Marcus Whitehouse (head chef) | Independent only, no group-scale. |
| **Bar** | Tomás Lavelle (bar manager); Jess Carmody trades as pub | Thin. |
| **Pub and hotel** | Caz, Liam, Priya, Karl, Andrew (full enterprise set); Jess at small group | Strong at enterprise, thin below it. |
| **QSR** | Ray Tan (franchisee), Steph Nguyen (restaurant manager), Kai Williams (crew) | Covered, owner to frontline. McDonald's benchmark. |
| **Takeaway and pizza** | Nick Castellano (franchisee), Mia Roberts (store manager), Deng Akok (team member), Pavel Novak (delivery driver) | Covered, owner to last mile, including delivery. Domino's benchmark. |
| **Stadia, events, convention** | None | Gap. Held open deliberately, to be built later. |

Damien O'Brien and Helena Mendes operate across mixed formats, so they appear under more than one vertical by design.

---

## View 3: the coverage grid (role by size-segment)

The audit tool. Each cell should hold at least one persona for a segment we actively pursue. Empty cells in a commercially important column are the prompt to add a persona, exactly the "additional UAT personas" point. Roles run down, segments run across.

| Role group | Independent | Small group | Mid-market | Enterprise |
|---|---|---|---|---|
| **Owners and executives** | Mel Sutton | Damien O'Brien, Nick Castellano | Ray Tan | Caz Whitfield |
| **General managers** | Sam Patel | Mia Roberts | Steph Nguyen | Liam Henderson |
| **Front of house** | Bella Ricci, Tomás Lavelle | Jess Carmody, Pavel Novak | Kai Williams | Priya Sharma, Karl Becker |
| **Back of house** | Marcus Whitehouse | Ahmed Khalil, Helena Mendes, Deng Akok | *(gap)* | Andrew Pickering |

### What the grid is telling us

- **Mid-market is now opened up, except back of house.** The QSR franchise group fills owners, GMs, and front of house at mid-market. The remaining hole is a mid-market back-of-house persona (a multi-restaurant kitchen or operations role).
- **General managers are no longer only independent and enterprise.** Mia Roberts (small group) and Steph Nguyen (mid-market) fill the middle of that row.
- **Two verticals closed.** QSR and takeaway and pizza now run owner to frontline. Only stadia, events and convention is left open, held deliberately for later.
- **Geography is still concentrated.** Every persona is Australia, New Zealand, United Kingdom, or Ireland, and the new QSR and pizza personas are all Australian. No United States persona, despite US franchise QSR being a named segment in `_framework/segmentation.md`.
- **Franchise is now represented, and it changes the buyer.** The QSR and pizza personas are franchisor-mandated: the brand buys the platform, the franchisee operates it. This is a different buying motion from the owner-led and procurement-led paths, and it is captured in those persona files.

---

## View 4: mapping to JPD

So a discovery idea tagged with a business segment in JPD convenes the matching persona set here. The aim is a 1:1 match between the JPD picklist and the size-segment tiers below.

| Library size-segment | JPD business-segment value | Status |
|---|---|---|
| Independent | *(to confirm against JPD picklist)* | Reconcile |
| Small group | *(to confirm against JPD picklist)* | Reconcile |
| Mid-market group | *(to confirm against JPD picklist)* | Reconcile |
| Enterprise chain | *(to confirm against JPD picklist)* | Reconcile |

**Reconcile-later note.** These labels currently follow `_framework/segmentation.md`, not JPD. On the next pass, read the actual JPD business-segment (and vertical) picklist values and set the labels above to match exactly, so a JPD field maps straight through to a persona set. If JPD uses different boundaries (for example a combined "SMB" tier), record the mapping rule here rather than forcing either side to change. The jpd-idea-groomer skill already sets a Segments field on ideas, so this map is what lets a groomed idea pull the right personas into a review.

---

## How to use this map

- **Targeting a segment.** Read the relevant table, convene those personas as the Operator Council slice for the review.
- **Planning the library.** Read the coverage grid. Fill the empty cells that sit in segments we are actually pursuing.
- **Grooming a JPD idea.** Match the idea's business segment to View 4, then pull that persona set.
- **Adding or retagging a persona.** Update the persona file's Snapshot first, then rebuild the tables here from the "Size and ownership" and "Service style" lines.

---

## Change log

- 2026-06-24. Initial version. Replaces the retired `organisations/` folder as the business-level view. Claude, with Niel.
- 2026-06-24. Added the QSR vertical (McDonald's benchmark: franchisee, restaurant manager, crew) and the takeaway and pizza vertical (Domino's benchmark: franchisee, store manager, in-store team member, delivery driver). Both verticals now covered. Mid-market tier opened up except back of house. Stadia held open. Claude, with Niel.

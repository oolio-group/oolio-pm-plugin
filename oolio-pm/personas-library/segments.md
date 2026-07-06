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
| Danielle "Dee" Alvarez | General Manager | Casual dining (United States) | [gm-casual-dining-us.md](uat-panel/general-managers/gm-casual-dining-us.md) |

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
| Lucy Tran | Finance manager | Mixed | [finance-manager-bookkeeper.md](uat-panel/back-of-house/finance-manager-bookkeeper.md) |

### Mid-market group (9 to 50 venues, functional committee)

Newly opened up by the QSR franchise group. A nine-restaurant McDonald's franchisee, his restaurant manager, and his crew now anchor this tier, with a real head office between them and the brand above.

| Persona | Role group | Vertical | File |
|---|---|---|---|
| Raymond "Ray" Tan | Franchisee / MD | QSR | [franchisee-owner-qsr.md](uat-panel/owners-and-executives/franchisee-owner-qsr.md) |
| Stephanie "Steph" Nguyen | Restaurant manager | QSR | [restaurant-manager-qsr.md](uat-panel/general-managers/restaurant-manager-qsr.md) |
| Kai Williams | Crew member | QSR | [crew-member-qsr.md](uat-panel/front-of-house/crew-member-qsr.md) |
| Sofia Marchetti | Kitchen operations director | Casual dining | [kitchen-operations-director-midmarket.md](uat-panel/back-of-house/kitchen-operations-director-midmarket.md) |

Helena Mendes (small group) is also written as edging into this tier.

### Enterprise chain (50+ venues, procurement-led)

| Persona | Role group | Vertical | File |
|---|---|---|---|
| Caroline "Caz" Whitfield | COO | Pub and hotel | [enterprise-chain-coo.md](uat-panel/owners-and-executives/enterprise-chain-coo.md) |
| Liam Henderson | General Manager | Pub and hotel | [gm-enterprise.md](uat-panel/general-managers/gm-enterprise.md) |
| Priya Sharma | FOH manager | Pub and hotel | [foh-manager-enterprise.md](uat-panel/front-of-house/foh-manager-enterprise.md) |
| Karl Becker | Bar manager | Pub and hotel | [bar-manager-enterprise.md](uat-panel/front-of-house/bar-manager-enterprise.md) |
| Andrew Pickering | Head chef | Pub and hotel | [head-chef-enterprise.md](uat-panel/back-of-house/head-chef-enterprise.md) |
| Devinder "Dev" Chandra | IT and systems manager | Pub and hotel | [it-systems-manager-enterprise.md](uat-panel/owners-and-executives/it-systems-manager-enterprise.md) |
| Michael "Mick" Torrance | Catering director | Stadia, events, convention | [catering-director-stadium.md](uat-panel/owners-and-executives/catering-director-stadium.md) |
| Danielle "Dani" Hartigan | Venue operations manager | Stadia, events, convention | [venue-operations-manager-stadium.md](uat-panel/general-managers/venue-operations-manager-stadium.md) |
| Josh Bennett | Bar supervisor, event-day frontline | Stadia, events, convention | [bar-supervisor-stadium.md](uat-panel/front-of-house/bar-supervisor-stadium.md) |

---

## View 2: by vertical (service style)

The operating model of the venue. Targeting a vertical convenes this row.

| Vertical | Personas | Coverage |
|---|---|---|
| **Cafe** | Mel Sutton (owner) | Thin. Owner only, no frontline. |
| **Casual dining** | Bella Ricci (FOH), Ahmed Khalil (line cook), Sofia Marchetti (kitchen ops director, mid-market), Dee Alvarez (GM, US); plus Damien and Helena via mixed estates | Moderate to strong, now with group-level BOH and a US GM. |
| **Fine dining** | Sam Patel (GM), Marcus Whitehouse (head chef) | Independent only, no group-scale. |
| **Bar** | Tomás Lavelle (bar manager); Jess Carmody trades as pub | Thin. |
| **Pub and hotel** | Caz, Liam, Priya, Karl, Andrew, Dev Chandra (full enterprise set including the IT buyer); Jess at small group | Strong at enterprise, thin below it. |
| **QSR** | Ray Tan (franchisee), Steph Nguyen (restaurant manager), Kai Williams (crew) | Covered, owner to frontline. McDonald's benchmark. |
| **Takeaway and pizza** | Nick Castellano (franchisee), Mia Roberts (store manager), Deng Akok (team member), Pavel Novak (delivery driver) | Covered, owner to last mile, including delivery. Domino's benchmark. |
| **Stadia, events, convention** | Mick Torrance (catering director), Dani Hartigan (venue ops manager), Josh Bennett (bar supervisor) | Covered executive to frontline at a single contract-catered Australian stadium (invented benchmark). Stadium kitchen/BOH still open. |

Damien O'Brien and Helena Mendes operate across mixed formats, so they appear under more than one vertical by design.

---

## View 3: the coverage grid (role by size-segment)

The audit tool. Each cell should hold at least one persona for a segment we actively pursue. Empty cells in a commercially important column are the prompt to add a persona, exactly the "additional UAT personas" point. Roles run down, segments run across.

| Role group | Independent | Small group | Mid-market | Enterprise |
|---|---|---|---|---|
| **Owners and executives** | Mel Sutton | Damien O'Brien, Nick Castellano | Ray Tan | Caz Whitfield, Dev Chandra, Mick Torrance |
| **General managers** | Sam Patel, Dee Alvarez | Mia Roberts | Steph Nguyen | Liam Henderson, Dani Hartigan |
| **Front of house** | Bella Ricci, Tomás Lavelle | Jess Carmody, Pavel Novak | Kai Williams | Priya Sharma, Karl Becker, Josh Bennett |
| **Back of house** | Marcus Whitehouse | Ahmed Khalil, Helena Mendes, Deng Akok, Lucy Tran | Sofia Marchetti | Andrew Pickering |

### What the grid is telling us

- **Mid-market is now fully covered, owner to back of house.** The QSR franchise group fills owners, GMs, and front of house; Sofia Marchetti (kitchen operations director) closes the back-of-house cell.
- **General managers are no longer only independent and enterprise.** Mia Roberts (small group) and Steph Nguyen (mid-market) fill the middle of that row, and Dee Alvarez adds a second independent GM in the US.
- **Stadia is now partially closed.** Executive (Mick Torrance), operations manager (Dani Hartigan), and frontline (Josh Bennett) exist at one benchmark contract-catered Australian stadium. A stadium kitchen persona and a UK/US events persona remain open.
- **The enterprise buyer side is part-closed.** The IT buyer exists (Dev Chandra, filed at the same invented estate as Caz Whitfield so the enterprise account is coherent), and finance is covered at small group (Lucy Tran). Enterprise procurement and enterprise finance remain open.
- **Geography now includes the US.** Dee Alvarez (Austin) anchors the United States with a GM; a US owner and frontline persona remain to build. The remaining geography gap is Denmark/Europe.
- **Franchise is now represented, and it changes the buyer.** The QSR and pizza personas are franchisor-mandated: the brand buys the platform, the franchisee operates it. This is a different buying motion from the owner-led and procurement-led paths, and it is captured in those persona files.

---

## View 4: mapping to JPD

So a discovery idea tagged with a business segment in JPD convenes the matching persona set here. The aim is a 1:1 match between the JPD picklist and the size-segment tiers below.

**Reconciled 2026-07-06** against the live JPD `Applicable Segments` field (`customfield_11558`, project OHSI). The JPD picklist is vertical-flavoured, not size-tiered: `Cafe, QSR, Casual Dining, Pub, Bar, Hotel, Fine Dining, Franchise, Enterprise, Multi-location, Takeaway, Pizza, Bakery, Gaming Venue`. There are no Independent / Small group / Mid-market values, so the mapping rule (recorded here rather than forcing either side to change) is:

| JPD value | Convenes |
|---|---|
| `Enterprise` | The Enterprise chain tier (View 1) |
| `Multi-location` | Small group and Mid-market tiers together |
| `Franchise` | The franchise personas (Ray Tan, Nick Castellano and their venue staff) |
| `Cafe`, `QSR`, `Casual Dining`, `Pub`, `Bar`, `Hotel`, `Fine Dining`, `Takeaway`, `Pizza` | The matching vertical row in View 2 (`Pub` and `Hotel` both map to the pub-and-hotel row; `Takeaway` and `Pizza` both map to takeaway and pizza) |
| `Gaming Venue`, `Bakery` | No dedicated persona yet; convene the nearest vertical (pub-and-hotel for gaming, cafe for bakery) and note the gap |
| *(none of Enterprise / Multi-location / Franchise selected)* | Default to the Independent tier |

An idea's size tier is inferred from `Enterprise` / `Multi-location` / `Franchise`; its vertical from the rest. The jpd-idea-groomer skill sets this field on ideas, so a groomed idea pulls the right persona slice into a review through this table.

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
- 2026-07-06. Added the stadia trio (Mick Torrance, Dani Hartigan, Josh Bennett at one benchmark stadium), the mid-market kitchen operations director (Sofia Marchetti, closing the BOH gap), the enterprise IT buyer (Dev Chandra), the small-group finance manager (Lucy Tran), and the first US persona (Dee Alvarez, GM, Austin). Reconciled View 4 against the live JPD Applicable Segments picklist and recorded the mapping rule. Claude, with Niel.

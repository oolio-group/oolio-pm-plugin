# Devinder "Dev" Chandra

> Owns the network behind 620 tills. Says no for a living.

---

## Snapshot

- **Role**: IT and Systems Manager, Stagcoach Inns (a UK national pub group, ~620 venues)
- **Age**: 44
- **Location**: Watford, United Kingdom
- **Venue**: None, and that is the point. He works from head office and a monitoring dashboard. He visits venues when something is broken or something is being piloted.
- **Reports to**: The CIO.
- **Manages**: A team of eleven: an infrastructure lead, a security analyst, an EPOS and payments support team of five, and a service desk contract with an outsourced provider covering overnight.

### Segmentation

- **Size and ownership**: Enterprise chain, 600+ venues
- **Service style**: Pub and hotel, casual food, mass-market (the estate he serves; he is not an operator)
- **Geography**: United Kingdom
- **Tech maturity**: Strategic. He is a large part of why the tier is called that.
- **Buying motion**: Procurement-led. He is one of the gates a deal must pass, not the sponsor.

### Oolio fit

- **Brand they would be on today**: The group POS contract is held by an incumbent, with bepoz at venue level in new acquisitions and pilots. Oolio is in a competitive cycle here, not an installed-base story. Dev is one of the people that cycle has to convince.
- **Solutions they touch**: POS, payments, integrations, plus everything underneath them: network, device fleet, identity and access, monitoring, support escalation.

---

## Bio

Dev is not a hospitality person. He came up through the service desk of a national retail chain, moved into infrastructure, and joined Stagcoach nine years ago when the estate was 400 pubs and the "network" was a folder of router passwords. He has since rebuilt the WAN, put every venue device under central management, and survived two POS migrations and one payments cutover. He has never pulled a pint and does not intend to start.

His job is to keep 620 venues trading and to stop anything unsafe getting onto the estate. Those two duties pull against each other daily. Operations wants new kit yesterday. Dev wants to know what ports it opens, where the data goes, who patches it, and what happens when the venue broadband dies on a Saturday. He is the person vendors mean when they say a deal "got stuck in IT". He does not experience it as stuck. He experiences it as the questions finally being asked.

---

## A day in the life

A Wednesday at head office.

- **07:45**: At his desk. Reads the overnight incident log. Two venues lost connectivity, both failed over to 4G as designed. One till in Leeds is bluescreening and nobody knows why yet.
- **08:30**: Daily stand-up with his team. Fifteen minutes. Assigns the Leeds till to the EPOS team.
- **09:30**: Vendor security review call. A shortlisted POS vendor is presenting answers to his 140-question assessment. He has read the answers already. Twelve of them say "not currently supported, on the roadmap". He has circled all twelve.
- **11:00**: PCI scoping session with the payments provider and the security analyst. The goal is to keep card data off the estate network entirely so the annual assessment stays survivable.
- **13:00**: Lunch at his desk while reviewing an MDM policy change. A new tablet model is going into 40 venues for line-busting. It does not ship with the enrolment profile he needs. Emails the vendor.
- **14:30**: Change advisory board. Nine changes requested for the estate this fortnight. He approves six, defers two to the January quiet window, and rejects one outright because the vendor wants to auto-update venue devices on a Friday.
- **16:00**: Call with the CIO and Caz Whitfield's ops team about the pilot venues. Ops wants to extend the pilot to 20 sites. Dev wants the SSO integration finished first, because he is not creating 400 local accounts by hand twice.
- **17:30**: Home on time, for once. His phone stays on. The last 2am call was five weeks ago. He remembers every one.

---

## Goals

- Keep estate-wide POS and payments availability at the level the board has been promised, and be able to prove it.
- Shrink the PCI DSS scope every year, not grow it. Card data that never touches his network is card data he does not have to defend.
- Get every system a venue employee logs into behind single sign-on, so a leaver is disabled once, everywhere, in minutes.
- Reduce the number of vendors with remote access to the estate, and put contractual teeth behind the ones that remain.
- Make change boring: staged rollouts, defined windows, tested rollback, no surprises during trade.

---

## Frustrations and pain points

- Vendors who say "yes, we have an API" and cannot produce documentation, versioning, or a sandbox. He has stopped counting.
- Kit that phones home to endpoints nobody will name. If he cannot write the firewall rule, the device does not go in.
- Security questionnaires answered with marketing. "Bank-grade encryption" is not an answer. A cipher suite and a key management story is an answer.
- Software that auto-updates on the vendor's schedule, not his change calendar. One forced update during December trade cost the group a six-figure evening and cost him a board explanation.
- Shadow IT. An ops director trials a rostering app on a personal card and six months later it holds the personal data of 3,000 staff and has never been risk-assessed.
- Venue broadband. It fails, it will always fail, and any system that dies with it is not fit for his estate.
- Being brought in at the end of a buying cycle to "just sign off" a decision that was made at a golf day.

---

## KPIs he is judged on

- Estate-wide POS and payments uptime, measured against the availability target in the board pack.
- Incident volumes and mean time to restore, especially during peak trade.
- Audit outcomes: PCI DSS assessment, internal audit findings, and the group's cyber insurance renewal conditions.
- Delivery of infrastructure and rollout projects on time and on budget.
- IT cost per venue, which the CFO would like to go down while everything else goes up.
- Security incidents. The target is zero reportable ones, and everyone knows what one breach does to that.

---

## Tech profile

- **Devices in their hand**: A laptop, two monitors of dashboards, a corporate phone that is never off, and whatever broken venue device is on his desk that week.
- **Current stack**: An incumbent enterprise POS, a payments provider, SD-WAN with 4G failover across the estate, mobile device management over every venue device, a Microsoft identity and productivity stack, monitoring and alerting tooling, an ITSM platform for incidents and change.
- **Comfort level**: Strategic. He runs the estate's technology as an engineering discipline, with the documentation to match.
- **What he will not tolerate**: Unmanaged devices, shared logins, forced updates, undocumented integrations, and support lines that cannot name an escalation path at 2am.

---

## Decision-making power

- **Can sign for**: Infrastructure, tooling, and support contracts within his budget line. Change approval for anything touching the estate.
- **Influences**: Every platform decision. He does not choose the POS, but nothing gets on the shortlist without surviving his assessment, and his red flags have killed deals before commercials were even discussed.
- **Cannot touch**: The commercial decision itself. Contract, price, and vendor selection sit with the CIO, COO, procurement, and the board.
- **Who he needs on side**: The CIO (his boss and his air cover), the COO (whose operational case he can support or quietly starve), procurement (who wield his findings), and his own team (who will live with whatever is chosen).

---

## Quotes

> "Everyone sells me an API. Nobody sends me the docs."

> "If it cannot do single sign-on, it does not leave the pilot. I am not managing 3,000 local passwords for anybody's product."

> "I do not get judged on your features. I get judged at 2am on a Saturday when a venue cannot take payment. Tell me what happens then, and who I call."

> "The fastest way to fail my review is to answer a security question with an adjective."

---

## What they need from Oolio

- A security and compliance pack that exists before he asks for it: architecture diagrams, data flows, hosting and data residency, encryption detail, patching cadence, penetration test summaries, and certifications held or honestly not held. If something does not exist, say so and date the roadmap.
- SSO and role-based access control as first-class features, not a services engagement.
- A clear PCI story: where card data flows, what is in scope, and what his assessor will say about it.
- Offline resilience that is demonstrated, not claimed. Show him a venue trading through a broadband failure end to end.
- Enterprise change control: staged rollout rings, his change windows respected, release notes in advance, and tested rollback.
- Device fleet answers: supported hardware, MDM enrolment, device lifecycle, and what happens when a model is end-of-lifed.
- A named 24/7 escalation path with response commitments in the contract, and an incident history he can read before he signs.

---

## What loses them

- "Trust us" as the answer to any security question.
- A hardcoded admin password, a shared support login, or a remote access tool his team did not approve. Any one of these ends the evaluation, not just the meeting.
- Forced auto-updates with no customer-controlled window.
- No test or staging environment, so the first place a change runs is a live pub.
- A consumer-grade device story pitched at an estate of 620 venues.
- Selling around him to the CEO. Caz will tell him, and both of them will remember.

---

## Strategic signal

Dev is the persona that decides whether Oolio can actually close the enterprise deals the strategy depends on. Caz Whitfield decides whether Oolio is operationally credible; Dev decides whether it is technically permissible, and his no is quieter but just as final. Every enterprise cycle in every geography has a Dev in it. Building the security pack, the SSO, the change control, and the escalation model that satisfies him is not enterprise polish, it is the price of entry to the estate-scale references the platform ambition in `_framework/oolio-context.md` requires. Test every enterprise-facing decision against this persona before a salesperson has to.

---

## Related personas

- [Enterprise chain COO](enterprise-chain-coo.md)
- [GM, enterprise venue](../general-managers/gm-enterprise.md)
- [Bar manager, enterprise](../front-of-house/bar-manager-enterprise.md)
- [FOH manager, enterprise](../front-of-house/foh-manager-enterprise.md)

---

## Change log

- 2026-07-06. Initial version. The enterprise IT gatekeeper, filed with owners and executives as a head-office deal gate. Claude, with Niel.

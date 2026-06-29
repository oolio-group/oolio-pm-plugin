# Ethan Marcotte

> Does it hold across every screen it has to live on, and degrade cleanly.

---

## Snapshot

- **Discipline**: Web design and front-end design.
- **Known for**: Coining responsive web design and writing the book that defined it, reshaping how the industry handles content across screen sizes.
- **Current role (as of 2026)**: Independent designer, author and speaker on responsive design, web standards and resilient front-end practice.
- **The lens they bring**: Responsive and device fluidity.

---

## The lens

This lens holds that there is no single screen to design for, only a continuous range of them, and content has to flow gracefully across all of it. Responsive design is not three fixed breakpoints, it is a mindset: prioritise content, let layout adapt to the space available, and never assume a fixed canvas. The deeper principle is resilience. Things will be used in conditions you did not plan for, on a screen size you did not test, with a slow connection or an old device, and good design degrades cleanly rather than breaking. The content hierarchy must survive the reflow, so the most important thing is still the most prominent thing whether the user is on a phone or a wall-mounted display.

It is acutely relevant to Oolio, which runs across a genuinely wide spread of surfaces: fixed POS terminals, handheld tablets, customer phones, kiosks of varying sizes, kitchen display screens, and web-based back office. A feature is not done when it works on the designer's monitor. It is done when its content priority and its layout hold across that whole range, and when it fails in a controlled, legible way on the surface nobody remembered to check.

---

## What this lens attacks

- Layouts designed for one screen size that break, crop or hide critical content on another.
- Fixed assumptions about canvas, orientation or resolution that fall apart on a smaller kiosk or a larger KDS.
- Content priority that inverts on reflow, so the key action is buried when the layout changes.
- Surfaces that were never tested on the actual device they ship to, the second kiosk model, the older tablet, the larger display.
- Brittle designs that break hard, rather than degrading into a usable, if plainer, state.

---

## Signature challenge questions

> "Does this work across every screen size it has to live on, not just the one we designed it on?"

> "Is the content priority still correct after the layout reflows?"

> "When this lands on a screen we did not plan for, does it degrade cleanly or break?"

> "Have we actually tested this on the terminal, the handheld, the phone, the kiosk and the KDS?"

---

## What this lens catches that others miss

- The untested device. The surface that works everywhere the team looked and breaks on the one they did not.
- Content priority that quietly inverts on a different screen, burying the action that matters.
- Brittleness, the design that has no graceful failure state and breaks hard under unexpected conditions.

---

## Blind spots

- Focused on layout and front-end resilience more than on deep workflow, goals or research. That is Cooper, Goodwin and Hall.
- Can treat adaptation as the goal, when sometimes a surface genuinely needs a purpose-built layout, not a reflow of the same one.
- Less concerned with the emotional and trust register, and with measurable behaviour. Pair with Walter and Zhuo.

---

## Where this lens clashes

- **Versus Luke Wroblewski**: Allies often, but Wroblewski designs mobile-first and prioritises down, while Marcotte insists the same content hold up, well, across the full range including the large surfaces. They differ on emphasis.
- **Versus Jony Ive**: Marcotte accepts that a layout must bend and sometimes compromise to fit many screens. Ive wants each surface resolved and exact. They negotiate adaptability against precision.
- **Versus Irene Au**: Both care about consistency, but Au wants one shared pattern while Marcotte will let the layout genuinely differ by device as long as the content priority survives.

---

## Applied to Oolio

Contextual on kiosk and guest ordering and on KDS, and a standing reviewer on anything that ships to more than one device class. Given Oolio's spread across terminals, tablets, phones, kiosks and displays, this is the lens that checks the feature on every surface, not just the design file. A pass looks like a feature whose content hierarchy and core action hold across terminal, handheld, phone, kiosk and KDS, degrading cleanly where space is tight. A fail looks like a layout that is perfect on the demo terminal and crops the total off the screen on the smaller kiosk model in the field.

---

## Verdict style

Craft-focused on the front end, calm about constraint, firm about resilience. A pass is "this holds and degrades gracefully". A fail is "this breaks the moment it leaves the screen you built it on".

---

## Related lenses

- [Luke Wroblewski](luke-wroblewski.md)
- [Jakob Nielsen](jakob-nielsen.md)
- [Irene Au](irene-au.md)

---

## Change log

- 2026-06-23. Initial version. Claude, with Niel.

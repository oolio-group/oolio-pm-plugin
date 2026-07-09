# Oolio PM Plugins

The Product team's plugin collection (marketplace) for Cowork. Other Oolio teams keep their own collections; this one is product management.

## Plugins

- **oolio-pm** — Oolio Product Management. Bundles the Virtual Product Council (convene-vpc and its operator, design, leadership, and STORM subcommittees, plus a snapshot of the persona library), the JPD grooming loop (jpd-loop), idea groomer (jpd-idea-groomer) and title standard (jpd-title-standard), the Jira epic helpers (jira-epic-groomer, jira-epic-titler), and grill-me for stress-testing a plan or decision. Self-contained.

## Install in Cowork (for Oolio teammates)

Most people will use this in Cowork, not Claude Code. Install from the **release zip** — do not use Cowork's GitHub / marketplace option, which is stuck serving an old version (see [PUBLISHING.md](PUBLISHING.md), "Known issue").

1. Download the latest `oolio-pm-vX.Y.Z.zip` from the [releases page](https://github.com/oolio-group/oolio-pm-plugin/releases/latest).
2. In Cowork, open **Settings → Plugins → Add plugin → Upload local plugin** (exact wording may differ slightly) and upload the zip.
3. Done. The plugin's skills appear in your skill list (for example, ask "convene the VPC").

Updating is the same three steps with the new zip when Niel announces a release. The real current version is always the top entry of [CHANGELOG.md](CHANGELOG.md).

## Layout

```
oolio-pm-plugins/           local folder name; the GitHub repo is oolio-group/oolio-pm-plugin
├── .claude-plugin/
│   └── marketplace.json    the marketplace manifest Cowork reads (must live here)
├── README.md
├── CHANGELOG.md            what changed in each version
├── CLAUDE.md               maintenance rules (bump version, log changes, archive)
├── PUBLISHING.md           how to edit, version, and publish (read this)
├── LICENSE                 usage terms (public repo, internal material)
└── oolio-pm/               the plugin
    ├── .claude-plugin/plugin.json
    ├── personas-library/   bundled persona-library snapshot
    ├── products/           product context briefs (facts skills may rely on)
    ├── references/         shared references (house style, council output template)
    ├── _archive/           retired skills, lenses, and templates (kept for reference)
    └── skills/             the skills (count in oolio-pm/README.md)
```

## Updating

See **PUBLISHING.md** for the full step-by-step. In short: edit the skill under `oolio-pm/skills/`, bump the version in both `.claude-plugin/marketplace.json` and `oolio-pm/.claude-plugin/plugin.json`, add a **CHANGELOG.md** entry, then commit and push. Cowork picks up the new version on its next sync. Maintenance rules are in **CLAUDE.md**.

## Notes

- This repository is intentionally **public** so teammates can install it without GitHub org access. It bundles Oolio-internal material (personas, context, strategy), so keep anything genuinely sensitive out of it.
- Must be hosted on github.com for Cowork to sync from it.

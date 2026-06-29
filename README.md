# Oolio PM Plugins

The Product team's plugin collection (marketplace) for Cowork. Other Oolio teams keep their own collections; this one is product management.

## Plugins

- **oolio-pm** — Oolio Product Management. Bundles the Virtual Product Council (convene-vpc and its operator, design, leadership, and STORM subcommittees, plus a snapshot of the persona library), the JPD grooming loop (jpd-loop) and idea groomer (jpd-idea-groomer), and the Jira epic helpers (jira-epic-groomer, jira-epic-titler). Self-contained.

## Layout

```
oolio-pm-plugins/
├── marketplace.json        the marketplace manifest Cowork reads
├── README.md
├── PUBLISHING.md           how to edit, version, and publish (read this)
└── oolio-pm/               the plugin
    ├── .claude-plugin/plugin.json
    ├── personas-library/   bundled persona-library snapshot
    └── skills/             the 9 skills
```

## Updating

See **PUBLISHING.md** for the full step-by-step. In short: edit the skill under `oolio-pm/skills/`, bump the version in both `marketplace.json` and `oolio-pm/.claude-plugin/plugin.json`, then commit and push from GitHub Desktop. Cowork picks up the new version on its next sync.

## Notes

- Keep this repository private or internal. Organisation marketplaces require it, and the content is Oolio-internal.
- Must be hosted on github.com for Cowork to sync from it.

# Oolio PM Plugins

The Product team's plugin collection (marketplace) for Cowork. Other Oolio teams keep their own collections; this one is product management.

## Plugins

- **oolio-pm** — Oolio Product Management. Bundles the Virtual Product Council (convene-vpc and its operator, design, leadership, and STORM subcommittees, plus a snapshot of the persona library), the JPD grooming loop (jpd-loop) and idea groomer (jpd-idea-groomer), and the Jira epic helpers (jira-epic-groomer, jira-epic-titler). Self-contained.

## Install in Cowork (for Oolio teammates)

Most people will use this in Cowork, not Claude Code. This is the one-time setup.

**Before you start, you need two things:**

1. **Access to this repo.** It is private, so your GitHub account must be a member of the `oolio-group` organisation with read access to `oolio-pm-plugins`. If Cowork cannot find the repo when you add it, this is almost always why. Ask Niel or your GitHub admin to add you.
2. **GitHub connected to your Cowork.** Connect your GitHub account inside Cowork once, so it is allowed to read the repo.

**Then install:**

1. In Cowork, open **Settings → Plugins → Add plugin → GitHub**.
2. Enter `oolio-group/oolio-pm-plugins`.
3. Install **oolio-pm**.

The plugin's skills then appear in your skill list (for example, ask "convene the VPC"). Whenever a new version is pushed to GitHub, Cowork offers it as an update on its next sync.

> Note: the exact menu wording in Cowork may differ slightly from the steps above. The first teammate to install should confirm the real path and tell Niel, so this section can be corrected.

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

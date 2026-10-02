# CLAUDE.md

Rules for agent sessions that edit this knowledge base. The KB itself starts at `index.md`;
its non-negotiables are in `constitution.md`.

## Format

- This repo is an Open Knowledge Format (OKF v0.1) bundle. Every concept file has YAML frontmatter
  with `type`, plus `title`, `description`, `tags`, `timestamp`. Conventions are in `README.md`.
- Links are bundle-root absolute: `[CON-2](/principles/construction.md)`.
- Each directory has an `index.md`; update it when you add, rename or remove a file.

## Rules

1. **IDs are permanent.** Never renumber or reuse a principle or guideline ID (`REQ-2`, `G-A1`).
   Retire an ID by marking it retired and recording it in `log.md`.
2. **Never contradict the constitution.** Changing `constitution.md` needs a human-approved PR that
   says why; update conflicting files in the same PR.
3. **Agents never set `verified`.** Only a human adds themselves to a file's `verified` list.
   Agents record their work in `generated` (`<producer>/<version>`).
4. **Record every change** in `log.md`, newest section last, one line per change.
5. **Bump `version`** (semver) on any content change to a file: patch for wording, minor for added
   rules, major for changed meaning.
6. **Cite sources.** Content derived from a book, standard or project goes in `sources`.
7. **Run `python tools/validate.py` before every push.** CI runs the same check.

# Org knowledge base

Organization knowledge base for the spec-driven, AI-native SDLC platform, laid out as an [Open Knowledge Format](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf) (OKF v0.1) bundle: a directory of markdown files with YAML frontmatter, linked with ordinary markdown links.

Start at [index.md](index.md).

## Conventions

- Every concept file has `type` (required by OKF) plus `title`, `description`, `tags`, `timestamp`.
- Provenance uses OKF's `generated` and `verified` blocks; actors are `<producer>/<version>` for agents and `human:<id>` for people. A file is trusted for enforcement only once `verified` is non-empty.
- Extension fields used by this KB: `version` (semver), `status` (draft | approved | retired), `principles` (machine-readable list of IDs in a principle set), `refines` (principle IDs a guideline refines).
- `python tools/validate.py` checks frontmatter, links and ID uniqueness; CI runs it on every PR.
- Links are bundle-root absolute (`/principles/construction.md`), as in the OKF examples.
- Principle IDs (`REQ-2`, `G-A1`) are stable and never reused; retire instead of deleting.
- `index.md` per directory for progressive disclosure; `log.md` at the root records changes.

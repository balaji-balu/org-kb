"""Validate the org KB bundle.

Checks every markdown file:
  - OKF: frontmatter with a `type` field (README.md and log.md are exempt).
  - Every bundle-root link (/path/to/file.md) resolves to a file in the bundle.
  - Principle and guideline IDs declared in principle-set frontmatter are unique.

Usage: python tools/validate.py [bundle-root]   (exit 1 on any problem)
"""
import os
import re
import sys

import yaml

EXEMPT = {"README.md", "log.md", "CLAUDE.md"}
SKIP_DIRS = {".git", ".github", "tools", ".obsidian"}


def main(root: str) -> int:
    problems = []
    seen_ids = {}
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in filenames:
            if not name.endswith(".md"):
                continue
            path = os.path.join(dirpath, name)
            rel = os.path.relpath(path, root).replace(os.sep, "/")
            with open(path, encoding="utf-8") as f:
                text = f.read()
            front = {}
            m = re.match(r"---\n(.*?)\n---\n", text, re.S)
            if m:
                try:
                    front = yaml.safe_load(m.group(1)) or {}
                except yaml.YAMLError as e:
                    problems.append(f"{rel}: invalid YAML frontmatter ({e})")
            if name not in EXEMPT and "type" not in front:
                problems.append(f"{rel}: missing frontmatter `type` (OKF)")
            for p in front.get("principles", []) or []:
                pid = p.get("id")
                if pid in seen_ids:
                    problems.append(f"{rel}: duplicate principle ID {pid} (also in {seen_ids[pid]})")
                seen_ids[pid] = rel
            body = text[m.end():] if m else text
            body = re.sub(r"```.*?```", "", body, flags=re.S)  # ignore links inside code blocks
            for link in re.findall(r"\]\((/[^)#\s]+)", body):
                if not os.path.exists(os.path.join(root, link.lstrip("/"))):
                    problems.append(f"{rel}: broken link {link}")
    for p in problems:
        print(p)
    print(f"{len(problems)} problem(s); {len(seen_ids)} principle IDs")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "."))

#!/usr/bin/env python3
"""
Inject Cursor-compatible YAML frontmatter into .cursor/rules/*.mdc files
using description/priority/globs/alwaysApply from .ai-rulez/rules/*.md.

Run after `uvx ai-rulez generate` so Cursor recognizes the rules without manual editing.
"""

from pathlib import Path
import re
import sys


def parse_frontmatter(content: str) -> tuple[dict | None, str]:
    """Extract YAML frontmatter (between ---) and return (attrs, body)."""
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", content, re.DOTALL)
    if not match:
        return None, content
    yaml_block, body = match.groups()
    attrs = {}
    for line in yaml_block.splitlines():
        if ":" in line:
            key, _, value = line.partition(":")
            key = key.strip().lower()
            value = value.strip().strip("'\"").strip()
            if key == "globs":
                if value.startswith("["):
                    attrs[key] = value
                else:
                    attrs[key] = value
            elif key == "alwaysapply":
                attrs["alwaysApply"] = value.lower() in ("true", "yes", "1")
            elif key in ("priority", "description", "targets"):
                attrs[key] = value
    return attrs, body.strip()


def cursor_frontmatter(attrs: dict) -> str:
    """Build Cursor .mdc frontmatter from ai-rulez rule attrs."""
    description = attrs.get("description") or "Rule (edit description in .ai-rulez/rules/)"
    always_apply = attrs.get("alwaysApply")
    if always_apply is None:
        always_apply = (attrs.get("priority") or "").lower() == "critical"
    lines = [
        "---",
        f'description: "{description}"',
        f"alwaysApply: {str(always_apply).lower()}",
    ]
    if attrs.get("globs"):
        g = attrs["globs"]
        if isinstance(g, str) and not g.startswith("["):
            lines.append(f'globs: ["{g}"]')
        else:
            lines.append(f"globs: {g}")
    lines.append("---")
    return "\n".join(lines) + "\n\n"


def main() -> int:
    repo = Path(__file__).resolve().parent.parent
    cursor_rules = repo / ".cursor" / "rules"
    ai_rules = repo / ".ai-rulez" / "rules"
    if not cursor_rules.is_dir() or not ai_rules.is_dir():
        print("Missing .cursor/rules/ or .ai-rulez/rules/", file=sys.stderr)
        return 1

    for mdc_path in sorted(cursor_rules.glob("*.mdc")):
        name = mdc_path.stem
        # Match source .md (e.g. Image-analysis.mdc -> image-analysis.md)
        md_name = name.lower().replace("_", "-")
        md_path = ai_rules / f"{md_name}.md"
        if not md_path.exists():
            # Try exact name
            md_path = ai_rules / f"{name}.md"
        if not md_path.exists():
            print(f"Skip (no source): {mdc_path.name}", file=sys.stderr)
            continue

        md_content = md_path.read_text(encoding="utf-8")
        attrs, _ = parse_frontmatter(md_content)
        if not attrs:
            print(f"Skip (no frontmatter): {md_path.name}", file=sys.stderr)
            continue

        mdc_content = mdc_path.read_text(encoding="utf-8")
        _, body = parse_frontmatter(mdc_content)
        # If no frontmatter was in .mdc, body is full content
        if body == mdc_content and not mdc_content.strip().startswith("---"):
            body = mdc_content

        new_content = cursor_frontmatter(attrs) + body
        mdc_path.write_text(new_content, encoding="utf-8")
        print(f"Updated: {mdc_path.name}")

    return 0


if __name__ == "__main__":
    sys.exit(main())

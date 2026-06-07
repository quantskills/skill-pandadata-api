#!/usr/bin/env python3
"""Build a compact Pandadata method index from references/api-docs.md."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DOC = ROOT / "references" / "api-docs.md"

MAJOR_RE = re.compile(r"^\*\*([一二三四五六七八九十]+)\.\s*(.+?)\*\*\s*$")
SUB_RE = re.compile(r"^\*\*（.+?）(.+?)：?\*\*\s*$")
METHOD_RE = re.compile(r"^\*\*(\d+)\.\s+([A-Za-z_][A-Za-z0-9_]*)\s+-\s+(.+?)\*\*\s*$")


def parse_methods(doc: Path) -> list[dict[str, str | int]]:
    methods: list[dict[str, str | int]] = []
    major = ""
    subsection = ""

    for line_no, raw in enumerate(doc.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.strip()

        major_match = MAJOR_RE.match(line)
        if major_match:
            major = major_match.group(2).strip()
            subsection = ""
            continue

        sub_match = SUB_RE.match(line)
        if sub_match:
            subsection = sub_match.group(1).strip()
            continue

        method_match = METHOD_RE.match(line)
        if method_match:
            methods.append(
                {
                    "line": line_no,
                    "category": major,
                    "section": subsection,
                    "method": method_match.group(2),
                    "summary": method_match.group(3).strip(),
                }
            )

    return methods


def render_markdown(methods: list[dict[str, str | int]], doc_name: str) -> str:
    lines = [
        "# Pandadata Method Index",
        "",
        f"Generated from `{doc_name}`. Use line numbers with `sed -n '<line>,+120p' references/api-docs.md`, or run `python scripts/search_api_docs.py --method <method>`.",
        "",
        f"Total methods: {len(methods)}",
        "",
        "| Category | Section | Method | Summary | API docs line |",
        "|---|---|---|---|---:|",
    ]

    for item in methods:
        lines.append(
            "| {category} | {section} | `{method}` | {summary} | {line} |".format(
                category=item["category"] or "-",
                section=item["section"] or "-",
                method=item["method"],
                summary=item["summary"],
                line=item["line"],
            )
        )

    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--doc", type=Path, default=DEFAULT_DOC, help="Path to api-docs.md")
    args = parser.parse_args()

    methods = parse_methods(args.doc)
    print(render_markdown(methods, args.doc.name))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

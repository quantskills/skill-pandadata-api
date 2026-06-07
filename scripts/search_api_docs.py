#!/usr/bin/env python3
"""Search or extract Pandadata API docs."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DOC = ROOT / "references" / "api-docs.md"
METHOD_HEADING_RE = re.compile(r"^\*\*\d+\.\s+([A-Za-z_][A-Za-z0-9_]*)\s+-\s+(.+?)\*\*\s*$")


def read_lines(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8").splitlines()


def method_spans(lines: list[str]) -> list[tuple[str, str, int, int]]:
    headings: list[tuple[str, str, int]] = []
    for idx, line in enumerate(lines):
        match = METHOD_HEADING_RE.match(line.strip())
        if match:
            headings.append((match.group(1), match.group(2), idx))

    spans: list[tuple[str, str, int, int]] = []
    for i, (method, summary, start) in enumerate(headings):
        end = headings[i + 1][2] if i + 1 < len(headings) else len(lines)
        spans.append((method, summary, start, end))
    return spans


def print_method(lines: list[str], method: str) -> int:
    wanted = method.strip()
    for item_method, summary, start, end in method_spans(lines):
        if item_method == wanted:
            print(f"# {item_method} - {summary}")
            print(f"\nSource lines: {start + 1}-{end}\n")
            print("\n".join(lines[start:end]).rstrip())
            return 0
    print(f"Method not found: {wanted}")
    return 1


def print_methods(lines: list[str]) -> int:
    for method, summary, start, _ in method_spans(lines):
        print(f"{start + 1}: {method} - {summary}")
    return 0


def search(lines: list[str], terms: list[str], context_lines: int) -> int:
    lowered_terms = [term.lower() for term in terms if term.strip()]
    if not lowered_terms:
        print("Provide search terms, --method, or --list-methods.")
        return 2

    matched = 0
    for idx, line in enumerate(lines):
        haystack = line.lower()
        if all(term in haystack for term in lowered_terms):
            matched += 1
            start = max(0, idx - context_lines)
            end = min(len(lines), idx + context_lines + 1)
            print(f"\n--- match {matched} at line {idx + 1} ---")
            for line_no in range(start, end):
                prefix = ">" if line_no == idx else " "
                print(f"{prefix} {line_no + 1}: {lines[line_no]}")

    if matched == 0:
        print("No matches.")
        return 1
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("terms", nargs="*", help="Keyword search terms; all terms must match the same line")
    parser.add_argument("--doc", type=Path, default=DEFAULT_DOC, help="Path to api-docs.md")
    parser.add_argument("--method", help="Extract the complete section for a panda_data method")
    parser.add_argument("--list-methods", action="store_true", help="List all method headings")
    parser.add_argument("--context-lines", type=int, default=3, help="Context lines around keyword matches")
    args = parser.parse_args()

    lines = read_lines(args.doc)
    if args.list_methods:
        return print_methods(lines)
    if args.method:
        return print_method(lines, args.method)
    return search(lines, args.terms, args.context_lines)


if __name__ == "__main__":
    raise SystemExit(main())

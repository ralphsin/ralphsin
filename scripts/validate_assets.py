#!/usr/bin/env python3
"""Fail the build if any SVG asset is malformed, oversized or missing alt text.

Checks every SVG under assets/ for XML well-formedness, a viewBox, an
accessible title, and a size within the performance budget. Also confirms that
every relative image path referenced by README.md actually exists.
"""

from __future__ import annotations

import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SVG_NS = "{http://www.w3.org/2000/svg}"
MAX_BYTES = 150 * 1024


def check_svg(path: Path) -> list[str]:
    problems: list[str] = []
    rel = path.relative_to(ROOT)

    size = path.stat().st_size
    if size > MAX_BYTES:
        problems.append(f"{rel}: {size // 1024} KB exceeds the {MAX_BYTES // 1024} KB budget")

    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as exc:
        return problems + [f"{rel}: not well-formed XML ({exc})"]

    if root.tag != f"{SVG_NS}svg":
        problems.append(f"{rel}: root element is not <svg>")
    if not root.get("viewBox"):
        problems.append(f"{rel}: missing viewBox, will not scale responsively")
    if root.find(f"{SVG_NS}title") is None:
        problems.append(f"{rel}: missing <title>, screen readers get nothing")
    if root.get("role") != "img":
        problems.append(f'{rel}: missing role="img"')

    return problems


def check_readme() -> list[str]:
    readme = ROOT / "README.md"
    if not readme.exists():
        return ["README.md is missing"]

    problems: list[str] = []
    text = readme.read_text(encoding="utf-8")

    for ref in re.findall(r'(?:src|srcset)="(\./[^"]+)"', text):
        if not (ROOT / ref.lstrip("./")).exists():
            problems.append(f"README.md references missing asset: {ref}")

    for tag in re.findall(r"<img\b[^>]*>", text):
        if 'alt="' not in tag:
            problems.append("README.md has an <img> without alt text")

    return problems


def main() -> int:
    problems = check_readme()
    svgs = sorted((ROOT / "assets").rglob("*.svg"))

    if not svgs:
        problems.append("no SVG assets found under assets/")
    for svg in svgs:
        problems.extend(check_svg(svg))

    if problems:
        for problem in problems:
            print(f"FAIL {problem}", file=sys.stderr)
        return 1

    print(f"ok: {len(svgs)} SVG assets and all README references validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

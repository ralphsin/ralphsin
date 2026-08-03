#!/usr/bin/env python3
"""Render the profile telemetry panel as two static SVGs (dark + light).

Reads data/profile.yml for hand-maintained fields and the public GitHub API
for live ones, then writes assets/generated/telemetry-{dark,light}.svg.

No third-party runtime dependencies beyond PyYAML. Fails soft: if the API is
unreachable the panel still renders with the hand-maintained fields.
"""

from __future__ import annotations

import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from html import escape
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "assets" / "generated"
API = "https://api.github.com"

THEMES = {
    "dark": {
        "bg": "#0B0E13",
        "grid": "#161C24",
        "rule": "#232A33",
        "label": "#808B99",
        "value": "#E9EDF2",
        "accent": "#C98A4B",
        "accent2": "#7FA3C9",
        "tile": "#151B23",
        "tile_stroke": "#3A3226",
    },
    "light": {
        "bg": "#EEF1F3",
        "grid": "#DBE1E6",
        "rule": "#D8DEE3",
        "label": "#7A8390",
        "value": "#131920",
        "accent": "#A85A2A",
        "accent2": "#3E6690",
        "tile": "#FFFFFF",
        "tile_stroke": "#DCC8B0",
    },
}
ACCENT_CYCLE = ("accent", "accent2", "accent")

WIDTH, HEIGHT = 1200, 168
COL_W = 320
COLS = [60, 440, 820]
MAX_CHARS = 26


def request_json(url: str) -> object | None:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "ralphsin-profile-telemetry",
    }
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            return json.load(resp)
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        print(f"warn: {url} -> {exc}", file=sys.stderr)
        return None


def humanise_age(iso: str) -> str:
    try:
        then = datetime.fromisoformat(iso.replace("Z", "+00:00"))
    except ValueError:
        return "unknown"
    days = (datetime.now(timezone.utc) - then).days
    if days <= 0:
        return "today"
    if days == 1:
        return "yesterday"
    if days < 30:
        return f"{days} days ago"
    months = days // 30
    return f"{months} mo ago" if months < 12 else f"{months // 12} yr ago"


def gather(username: str) -> dict[str, str]:
    facts = {"public_repos": "—", "last_shipped": "—", "last_push": "—"}

    user = request_json(f"{API}/users/{username}")
    if isinstance(user, dict) and "public_repos" in user:
        facts["public_repos"] = str(user["public_repos"])

    repos = request_json(f"{API}/users/{username}/repos?sort=pushed&per_page=5")
    if isinstance(repos, list) and repos:
        newest = repos[0]
        facts["last_shipped"] = str(newest.get("name", "—"))
        pushed = newest.get("pushed_at")
        if pushed:
            facts["last_push"] = humanise_age(str(pushed))

    return facts


def truncate(text: str, limit: int = MAX_CHARS) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "…"


def render(theme_name: str, cells: list[tuple[str, str]], stamp: str) -> str:
    t = THEMES[theme_name]
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" '
        f'width="{WIDTH}" height="{HEIGHT}" role="img" aria-labelledby="ttl dsc">',
        "<title id=\"ttl\">Profile telemetry</title>",
        "<desc id=\"dsc\">"
        + escape("; ".join(f"{label}: {value}" for label, value in cells))
        + f"; refreshed {escape(stamp)}.</desc>",
        "<defs>",
        '<style>.mono{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,'
        '"Liberation Mono","DejaVu Sans Mono",monospace}'
        ".blip{animation:b 3s ease-in-out infinite}"
        "@keyframes b{0%,100%{opacity:.35}50%{opacity:1}}"
        "@media (prefers-reduced-motion:reduce){.blip{animation:none;opacity:.8}}</style>",
        f'<pattern id="g" width="40" height="40" patternUnits="userSpaceOnUse">'
        f'<path d="M40 0 L0 0 L0 40" fill="none" stroke="{t["grid"]}" stroke-width="1"/></pattern>',
        "</defs>",
        f'<rect width="{WIDTH}" height="{HEIGHT}" fill="{t["bg"]}"/>',
        f'<rect width="{WIDTH}" height="{HEIGHT}" fill="url(#g)"/>',
        f'<rect x="0" y="0" width="{WIDTH}" height="2" fill="{t["accent"]}" opacity="0.7"/>',
        f'<path d="M18 26 L18 14 L30 14" fill="none" stroke="{t["accent"]}" stroke-width="1.2"/>',
        f'<circle cx="72" cy="36" r="4" fill="{t["accent"]}" class="blip"/>',
        f'<text class="mono" x="88" y="41" font-size="15" letter-spacing="1" '
        f'fill="{t["label"]}">TELEMETRY</text>',
        f'<text class="mono" x="{WIDTH - 60}" y="41" font-size="14" fill="{t["label"]}" '
        f'text-anchor="end">refreshed {escape(stamp)}</text>',
        f'<line x1="60" y1="60" x2="{WIDTH - 60}" y2="60" stroke="{t["rule"]}" stroke-width="1"/>',
    ]

    for i, (x, (label, value)) in enumerate(zip(COLS, cells)):
        col = t[ACCENT_CYCLE[i % len(ACCENT_CYCLE)]]
        parts.append(
            f'<rect x="{x}" y="78" width="{COL_W}" height="62" rx="3" '
            f'fill="{t["tile"]}" stroke="{t["tile_stroke"]}" stroke-width="1"/>'
        )
        parts.append(f'<rect x="{x}" y="78" width="3" height="62" fill="{col}"/>')
        parts.append(
            f'<text class="mono" x="{x + 20}" y="100" font-size="11" letter-spacing="1.5" '
            f'fill="{col}">{escape(label.upper())}</text>'
        )
        parts.append(
            f'<text class="mono" x="{x + 20}" y="126" font-size="18" '
            f'fill="{t["value"]}">{escape(truncate(value))}</text>'
        )

    parts.append("</svg>")
    return "\n".join(parts) + "\n"


def main() -> int:
    config = yaml.safe_load((ROOT / "data" / "profile.yml").read_text(encoding="utf-8"))
    username = config.get("username", "ralphsin")
    facts = gather(username)

    shipped = facts["last_shipped"]
    if facts["last_push"] not in ("—", "unknown"):
        shipped = f"{shipped} · {facts['last_push']}"

    cells = [
        ("current focus", str(config.get("current_focus", "—"))),
        ("active stack", str(config.get("active_stack", "—"))),
        ("last shipped", shipped),
    ]
    stamp = datetime.now(timezone.utc).strftime("%d %b %Y").lower()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for theme in THEMES:
        target = OUT_DIR / f"telemetry-{theme}.svg"
        target.write_text(render(theme, cells, stamp), encoding="utf-8")
        print(f"wrote {target.relative_to(ROOT)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Stock-ticker tape -> profile/ticker.svg.

Words scroll right to left like an exchange ticker, separated by green
uptick triangles. Greetings use the accent color, topics the foreground.
The tape is repeated past one period so a single SMIL translate by
exactly one period loops without a visible seam. GitHub strips scripts
from SVGs but runs SMIL.

Pure Python: only the embedded font subset is needed. Output is
committed; regenerate only when the wording changes.

Usage: python scripts/generate_ticker.py
"""

import math
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from svgkit import ROOT, THEME_CSS, char_w, font_face, svg_open

GREETINGS = ["BIENVENIDOS", "WELCOME", "BEM-VINDOS"]
TOPICS = ["FINANZAS", "AGENTIC AI", "OPEN SOURCE"]
WORDS = GREETINGS + TOPICS

FS = 22
CW = char_w(FS)  # JetBrains Mono advance: 0.6 em
GAP = 4 * CW  # room for the separator between words
W, H = 960, 56
SPEED = 60  # px per second

# GitHub's green, dark default, light via media query (same scheme as THEME_CSS)
EXTRA_CSS = (
    ":root{--up:#3fb950}"
    "@media (prefers-color-scheme: light){:root{--up:#1a7f37}}"
    ".up{fill:var(--up)}"
    ".tape{font-family:'jbmb',monospace;font-weight:700}"
)

OUT = ROOT / "profile" / "ticker.svg"


def period() -> float:
    return sum(len(w) * CW + GAP for w in WORDS)


def triangle(cx: float, base_y: float, size: float) -> str:
    h = size * 0.87
    return (
        f'<path class="up" d="M{cx - size / 2:.1f} {base_y:.1f}'
        f'L{cx + size / 2:.1f} {base_y:.1f}L{cx:.1f} {base_y - h:.1f}Z"/>'
    )


def build_svg() -> str:
    css = font_face("jbmono-latin-bold.woff2", "jbmb", 700) + THEME_CSS + EXTRA_CSS
    p = period()
    copies = math.ceil((W + p) / p) + 1
    base = H / 2 + FS * 0.36

    items = []
    x = 0.0
    for _ in range(copies):
        for w in WORDS:
            wl = len(w) * CW
            cls = "accent" if w in GREETINGS else "fg"
            items.append(
                f'<text x="{x:.1f}" y="{base:.1f}" font-size="{FS}" class="{cls} tape" '
                f'textLength="{wl:.1f}" xml:space="preserve">{w}</text>'
            )
            items.append(triangle(x + wl + GAP / 2, base - FS * 0.02, FS * 0.62))
            x += wl + GAP

    s = [svg_open(W, H, css)]
    # luminance mask fades both edges regardless of the page background
    s.append(
        '<defs><linearGradient id="fade" x1="0" x2="1">'
        '<stop offset="0" stop-color="#000"/><stop offset="0.07" stop-color="#fff"/>'
        '<stop offset="0.93" stop-color="#fff"/><stop offset="1" stop-color="#000"/>'
        f'</linearGradient><mask id="m"><rect width="{W}" height="{H}" fill="url(#fade)"/>'
        "</mask></defs>"
    )
    s.append(f'<line x1="0" y1="3" x2="{W}" y2="3" class="rule" stroke-width="1"/>')
    s.append(f'<line x1="0" y1="{H - 3}" x2="{W}" y2="{H - 3}" class="rule" stroke-width="1"/>')
    s.append('<g mask="url(#m)"><g>')
    s.append(
        f'<animateTransform attributeName="transform" type="translate" '
        f'from="0 0" to="{-p:.1f} 0" dur="{p / SPEED:.2f}s" repeatCount="indefinite"/>'
    )
    s.extend(items)
    s.append("</g></g></svg>")
    return "".join(s)


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(build_svg(), encoding="utf-8")
    kb = OUT.stat().st_size / 1024
    # ascii-only console output: Windows terminals default to cp1252
    print(f"wrote {OUT} ({kb:.0f} KB, {len(WORDS)} words, {period() / SPEED:.1f}s loop)")


if __name__ == "__main__":
    main()

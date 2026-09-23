# CFA Society México Org Profile Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the `CFA-Society-Mexico/.github` repo: a bilingual org profile README with an animated ASCII greeting, plus org-wide community defaults (responsible-AI principles, contributing guide, code of conduct, PR template).

**Architecture:** Plain Markdown files at the repo root act as GitHub org-wide defaults; `profile/README.md` is the org page. The greeting is a SMIL-animated SVG generated locally by a Python script adapted from `alanvaa06/alanvaa06` and committed as output (no CI). A small pytest suite guards the docs (required files, no stray TODOs, relative links resolve) and the generator (words, SVG structure, font glyph coverage).

**Tech Stack:** Markdown/HTML (GitHub-flavored), Python 3.14 + Pillow + numpy + fontTools (generator), pytest, `gh` CLI, Git Bash.

**Spec:** `docs/superpowers/specs/2026-09-23-org-profile-readme-design.md`

**Conventions for every task:**
- Repo root: `C:\Proyectos\CFA-Society-Mexico` (already `git init`-ed on `main`, spec + plan already committed).
- Run all commands in **Git Bash** from the repo root (`cd /c/Proyectos/CFA-Society-Mexico`). Do NOT use PowerShell `>` redirection for downloads: it re-encodes and corrupts binary files.
- Console output of any script must be ASCII-only (Windows cp1252).
- The contact email is the literal token `TODO-EMAIL` everywhere. It is the only allowed `TODO`.
- Every commit ends with the trailer line `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` (passed as a second `-m`).

---

## File map

| File | Responsibility | Task |
|------|----------------|------|
| `.gitignore` | ignore caches and local tooling | 1 |
| `README.md` | explains what this repo is + how to regenerate greeting | 1 |
| `LICENSE` | MIT for this repo (target of the license badge) | 1 |
| `scripts/requirements.txt` | generator + test deps | 1 |
| `tests/test_docs.py` | docs guard: required files, TODO token, relative links, profile sections | 1 (grows in 5-9) |
| `scripts/svgkit.py` | shared SVG helpers (copied verbatim) | 2 |
| `assets/fonts/*` | JetBrains Mono subsets + OFL license (copied verbatim) | 2 |
| `scripts/generate_greeting.py` | greeting generator (adapted) | 3 |
| `tests/test_greeting.py` | generator guard | 3 |
| `profile/greeting.svg` | generated animation (committed output) | 4 |
| `profile/README.md` | org profile page | 5 |
| `CODE_OF_CONDUCT.md` | Contributor Covenant 2.1 ES + EN | 6 |
| `RESPONSIBLE_AI.md` | 5 principles, ES + EN | 7 |
| `CONTRIBUTING.md` | contribution flow + minimum bar, ES + EN | 8 |
| `.github/pull_request_template.md` | bilingual PR checklist | 9 |

Order matters: files that others link to relatively are created first (CODE_OF_CONDUCT and RESPONSIBLE_AI before CONTRIBUTING), so the link test stays green after every task.

---

### Task 1: Scaffold and docs test harness

**Files:**
- Create: `.gitignore`, `README.md`, `LICENSE`, `scripts/requirements.txt`, `tests/test_docs.py`

- [ ] **Step 1: Write the failing test**

Create `tests/test_docs.py`:

```python
"""Guards for the Markdown files of the org .github repo.

Non-ASCII needles are written as escapes so failure output stays
cp1252-safe on Windows consoles.
"""

import pathlib
import re

import pytest

ROOT = pathlib.Path(__file__).resolve().parent.parent
PLACEHOLDER = "TODO-EMAIL"

REQUIRED = [
    "README.md",
    "LICENSE",
]

LINK = re.compile(r'(?:\]\(|src="|href=")([^)"#\s]+)')


def md_files():
    skip = {"docs", ".pytest_cache", ".claude"}
    return sorted(
        p for p in ROOT.rglob("*.md") if not skip & set(p.relative_to(ROOT).parts)
    )


@pytest.mark.parametrize("rel", REQUIRED)
def test_required_file_exists(rel):
    assert (ROOT / rel).is_file(), rel


def test_no_todo_except_email_placeholder():
    for p in md_files():
        text = p.read_text(encoding="utf-8").replace(PLACEHOLDER, "")
        assert "TODO" not in text, str(p.relative_to(ROOT))


def test_relative_links_resolve():
    for p in md_files():
        for target in LINK.findall(p.read_text(encoding="utf-8")):
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            assert (p.parent / target).exists(), f"{p.relative_to(ROOT)} -> {target}"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_docs.py -q`
Expected: 2 FAILED (`test_required_file_exists[README.md]`, `test_required_file_exists[LICENSE]`), 2 passed.

- [ ] **Step 3: Create the scaffold files**

`.gitignore`:

```
__pycache__/
.pytest_cache/
.claude/
```

`scripts/requirements.txt`:

```
pillow
numpy
fonttools
pytest
```

`LICENSE`:

```
MIT License

Copyright (c) 2026 CFA Society Mexico contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

`README.md`:

````markdown
# .github

Perfil y archivos de comunidad por defecto de la organización
[CFA Society México](https://github.com/CFA-Society-Mexico).

*Profile and default community files for the
[CFA Society México](https://github.com/CFA-Society-Mexico) organization.*

## Regenerar el saludo / Regenerate the greeting

Solo cuando cambian las palabras. Requiere Windows (Consolas Bold).
*Only when the words change. Requires Windows (Consolas Bold).*

```bash
pip install -r scripts/requirements.txt
python scripts/generate_greeting.py
python -m pytest -q
```
````

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_docs.py -q`
Expected: `4 passed`

- [ ] **Step 5: Commit**

```bash
git add .gitignore README.md LICENSE scripts/requirements.txt tests/test_docs.py
git commit -m "chore: scaffold org .github repo with docs guard tests" -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 2: Copy svgkit and fonts from alanvaa06/alanvaa06

**Files:**
- Create: `scripts/svgkit.py`, `assets/fonts/jbmono-ramp.woff2`, `assets/fonts/jbmono-latin.woff2`, `assets/fonts/OFL.txt`

These are copied verbatim. `svgkit.py` defines `ROOT` (repo root = parent of `scripts/`), `FONTS = ROOT/"assets"/"fonts"`, `char_w(fs) = 0.6*fs`, `font_face(subset, family, weight)`, `THEME_CSS` (GitHub palette, dark default, light via `prefers-color-scheme`), `svg_open(w, h, css)`, `esc(s)`.

- [ ] **Step 1: Download (Git Bash, binary-safe)**

```bash
mkdir -p scripts assets/fonts
SRC=repos/alanvaa06/alanvaa06/contents
RAW="Accept: application/vnd.github.raw"
gh api "$SRC/scripts/svgkit.py" -H "$RAW" > scripts/svgkit.py
for f in jbmono-ramp.woff2 jbmono-latin.woff2 OFL.txt; do
  gh api "$SRC/assets/fonts/$f" -H "$RAW" > "assets/fonts/$f"
done
```

- [ ] **Step 2: Verify sizes and glyphs**

```bash
wc -c scripts/svgkit.py assets/fonts/*
python -c "from fontTools.ttLib import TTFont; c=TTFont('assets/fonts/jbmono-latin.woff2').getBestCmap(); print('o-acute', 0xF3 in c, 'slash', 0x2F in c)"
```

Expected: `svgkit.py` 1631 bytes, `jbmono-ramp.woff2` 4592, `jbmono-latin.woff2` 16676, `OFL.txt` 4399; then `o-acute True slash True`.

- [ ] **Step 3: Commit**

```bash
git add scripts/svgkit.py assets/fonts
git commit -m "chore: copy svgkit and JetBrains Mono subsets from alanvaa06/alanvaa06" -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 3: Greeting generator (TDD)

**Files:**
- Create: `tests/test_greeting.py`, `scripts/generate_greeting.py`

- [ ] **Step 1: Write the failing test**

Create `tests/test_greeting.py`:

```python
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "scripts"))

import generate_greeting as gg  # noqa: E402


def test_words_are_latam_greeting():
    assert [w for w, _ in gg.WORDS] == ["BIENVENIDOS", "WELCOME", "BEM-VINDOS"]


def test_grids_fit_the_canvas():
    for grid in gg.render_grids():
        assert 1 <= len(grid[0]) <= gg.MAX_COLS
        assert set("".join(grid)) <= set(gg.RAMP)


def test_svg_structure():
    svg = gg.build_svg(gg.render_grids())
    assert svg.startswith("<svg") and svg.endswith("</svg>")
    assert "<script" not in svg
    assert svg.count('<g opacity="0">') == 3
    assert 'dur="7.5s"' in svg
    assert "c\u00f3digo abierto" in svg
    assert "prefers-color-scheme" in svg


def test_caption_glyphs_in_embedded_font():
    from fontTools.ttLib import TTFont

    cmap = TTFont(gg.ROOT / "assets" / "fonts" / "jbmono-latin.woff2").getBestCmap()
    missing = sorted({hex(ord(c)) for c in gg.CAPTION if c != " " and ord(c) not in cmap})
    assert not missing, missing
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_greeting.py -q`
Expected: collection ERROR, `ModuleNotFoundError: No module named 'generate_greeting'`.

- [ ] **Step 3: Write the implementation**

Create `scripts/generate_greeting.py`:

```python
#!/usr/bin/env python3
"""Cycling Latam greeting -> profile/greeting.svg.

Adapted from github.com/alanvaa06/alanvaa06 (scripts/generate_greeting.py).
Each word is drawn with a system font, downscaled, and mapped to an ASCII
brightness ramp, then typed out with a SMIL clip-wipe. GitHub strips
scripts from SVGs but runs SMIL.

Run locally (needs Windows system fonts); output is committed. Regenerate
only when the wording changes.

Usage: python scripts/generate_greeting.py
"""

import pathlib
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from svgkit import ROOT, THEME_CSS, char_w, font_face, svg_open

RAMP = " .:-=+*#%@"
FS = 12.9
CHAR_W = char_w(FS)  # 7.74
LINE_H = CHAR_W / 0.48
MAX_COLS = 124

STEP = 2.5  # seconds each word owns
ROW_STAGGER = 0.09
TYPE_DUR = 0.8  # per-row wipe duration

FONTS = {
    "latin": (r"C:\Windows\Fonts\consolab.ttf", 8),
}

WORDS = [
    ("BIENVENIDOS", "latin"),
    ("WELCOME", "latin"),
    ("BEM-VINDOS", "latin"),
]

# jbmono-latin has no middle dot (U+00B7), hence the slashes
CAPTION = "finanzas / IA responsable / c\u00f3digo abierto"

OUT = ROOT / "profile" / "greeting.svg"


def word_to_ascii(text: str, kind: str) -> list[str]:
    fontpath, target_rows = FONTS[kind]
    f = ImageFont.truetype(fontpath, 160, index=0)
    bbox = f.getbbox(text)
    w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
    img = Image.new("L", (w + 24, h + 24), 255)
    ImageDraw.Draw(img).text((12 - bbox[0], 12 - bbox[1]), text, font=f, fill=0)

    cols = round(target_rows / 0.48 * (img.width / img.height))
    if cols > MAX_COLS:
        cols = MAX_COLS
    rows = max(1, round(cols * (img.height / img.width) * 0.48))
    small = np.array(img.resize((cols, rows), Image.LANCZOS)).astype(int)

    lines = []
    for r in small:
        idx = ((255 - r) * (len(RAMP) - 1) // 255).clip(0, len(RAMP) - 1)
        lines.append("".join(RAMP[i] for i in idx))
    return lines


def esc_row(line: str) -> str:
    return (
        line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        .replace(" ", "&#160;")
    )


def render_grids() -> list[list[str]]:
    return [word_to_ascii(t, k) for t, k in WORDS]


def build_svg(grids: list[list[str]]) -> str:
    max_rows = max(len(g) for g in grids)
    n = len(grids)
    cycle = n * STEP

    W = round(MAX_COLS * CHAR_W)
    grid_h = max_rows * LINE_H
    H = round(grid_h + 42)

    css = (
        font_face("jbmono-ramp.woff2", "jbmr", 400)
        + font_face("jbmono-latin.woff2", "jbm", 400)
        + THEME_CSS
    )
    s = [svg_open(W, H, css)]
    s.append("<defs>")
    for i, g in enumerate(grids):
        gw = len(g[0]) * CHAR_W
        x0 = (W - gw) / 2
        y0 = (grid_h - len(g) * LINE_H) / 2
        beg = i * STEP
        for r in range(len(g)):
            # keyTimes sequence the wipe inside each word's full-cycle period;
            # base width 0 hides rows before the first cycle starts
            t0 = (r * ROW_STAGGER) / cycle
            t1 = (r * ROW_STAGGER + TYPE_DUR) / cycle
            s.append(
                f'<clipPath id="w{i}r{r}"><rect x="{x0:.1f}" '
                f'y="{y0 + r * LINE_H:.1f}" width="0" height="{LINE_H:.1f}">'
                f'<animate attributeName="width" values="0;0;{gw:.0f};{gw:.0f}" '
                f'keyTimes="0;{t0:.4f};{t1:.4f};1" dur="{cycle}s" '
                f'begin="{beg}s" repeatCount="indefinite"/></rect></clipPath>'
            )
    s.append("</defs>")

    hold_end = STEP / cycle  # word owns [0, STEP) of its period
    fade_end = (STEP + 0.3) / cycle
    for i, g in enumerate(grids):
        gw = len(g[0]) * CHAR_W
        x0 = (W - gw) / 2
        y0 = (grid_h - len(g) * LINE_H) / 2
        beg = i * STEP
        s.append(
            f'<g opacity="0"><animate attributeName="opacity" '
            f'values="1;1;0;0" keyTimes="0;{hold_end:.4f};{fade_end:.4f};1" '
            f'dur="{cycle}s" begin="{beg}s" repeatCount="indefinite"/>'
        )
        for r, line in enumerate(g):
            y = y0 + r * LINE_H + FS
            s.append(
                f'<g clip-path="url(#w{i}r{r})"><text x="{x0:.1f}" y="{y:.1f}" '
                f'font-size="{FS}" style="font-family:\'jbmr\',monospace" '
                f'xml:space="preserve" textLength="{gw:.1f}" '
                f'class="accent">{esc_row(line)}</text></g>'
            )
        # one full-height cursor bar riding the wipe, gone once typing ends
        type_total = (len(g) - 1) * ROW_STAGGER + TYPE_DUR
        tc = type_total / cycle
        s.append(
            f'<rect x="{x0:.1f}" y="{y0:.1f}" width="{CHAR_W:.2f}" '
            f'height="{len(g) * LINE_H:.1f}" fill="var(--accent)" opacity="0">'
            f'<animate attributeName="opacity" values="0.7;0.7;0;0" '
            f'keyTimes="0;{tc:.4f};{min(tc + 0.005, 1):.4f};1" dur="{cycle}s" '
            f'begin="{beg}s" repeatCount="indefinite"/>'
            f'<animate attributeName="x" values="{x0:.1f};{x0 + gw:.1f};{x0 + gw:.1f}" '
            f'keyTimes="0;{tc:.4f};1" dur="{cycle}s" begin="{beg}s" '
            f'repeatCount="indefinite"/></rect>'
        )
        s.append("</g>")

    cy = H - 12
    s.append(
        f'<text x="{W / 2:.0f}" y="{cy}" font-size="13" text-anchor="middle" '
        f'class="dim" opacity="0">{CAPTION}'
        f'<animate attributeName="opacity" from="0" to="1" dur="0.5s" '
        f'begin="1s" fill="freeze"/></text>'
    )
    s.append("</svg>")
    return "".join(s)


def main():
    grids = render_grids()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(build_svg(grids), encoding="utf-8")
    kb = OUT.stat().st_size / 1024
    print(f"wrote {OUT} ({kb:.0f} KB, {len(grids)} words, {len(grids) * STEP}s cycle)")
    for (t, _), g in zip(WORDS, grids):
        # ascii-only console output: Windows terminals default to cp1252
        print(f"  {t}: {len(g[0])}x{len(g)}")


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_greeting.py -q`
Expected: `4 passed`

- [ ] **Step 5: Commit**

```bash
git add scripts/generate_greeting.py tests/test_greeting.py
git commit -m "feat: add Latam greeting generator adapted from alanvaa06" -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 4: Generate the greeting SVG and verify it visually

**Files:**
- Create: `profile/greeting.svg` (generated), `.claude/launch.json` (local only, gitignored)

- [ ] **Step 1: Generate**

Run: `python scripts/generate_greeting.py`
Expected (sizes approximate):

```
wrote C:\Proyectos\CFA-Society-Mexico\profile\greeting.svg (~40 KB, 3 words, 7.5s cycle)
  BIENVENIDOS: 124x8
  WELCOME: ~85x8
  BEM-VINDOS: ~120x8
```

No `UnicodeEncodeError`. File under 100 KB.

- [ ] **Step 2: Serve it locally**

Local `file://` previews always render light, so serve over HTTP. Create `.claude/launch.json`:

```json
{
  "version": "0.0.1",
  "configurations": [
    {
      "name": "greeting",
      "runtimeExecutable": "python",
      "runtimeArgs": ["-m", "http.server", "8765", "--directory", "profile"],
      "port": 8765
    }
  ]
}
```

Start it with the built-in browser tool `preview_start` (`name: "greeting"`), then navigate to `http://localhost:8765/greeting.svg`.

- [ ] **Step 3: Visual check, both schemes**

Use `resize_window` with `colorScheme: "dark"`, reload, screenshot at t≈1s, 3.5s, 6s; repeat with `colorScheme: "light"`. Pass criteria:
- Frame 1 shows BIENVENIDOS, frame 2 WELCOME, frame 3 BEM-VINDOS; each is legible, centered, and typed with the cursor bar.
- No word visible before its first slot; loop restarts cleanly after 7.5s.
- Accent is blue `#58a6ff` in dark and `#0969da` in light.
- Caption `finanzas / IA responsable / código abierto` fades in, dim color, `ó` renders in the same monospace face as the rest.

If a word is illegible, stop and report; do not tweak constants silently. Stop the server (`preview_stop`) when done.

- [ ] **Step 4: Run the full suite**

Run: `python -m pytest -q`
Expected: `8 passed`

- [ ] **Step 5: Commit**

```bash
git add profile/greeting.svg
git commit -m "feat: add generated greeting animation" -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 5: Org profile README

**Files:**
- Create: `profile/README.md`
- Modify: `tests/test_docs.py`

- [ ] **Step 1: Write the failing test**

In `tests/test_docs.py`, add `"profile/README.md",` to `REQUIRED` (after `"LICENSE",`) and append:

```python
def test_profile_readme_sections():
    text = (ROOT / "profile" / "README.md").read_text(encoding="utf-8")
    for needle in [
        'src="greeting.svg"',
        "## Qui\u00e9nes somos",
        "## Proyectos / Projects",
        "## IA responsable",
        "## C\u00f3mo contribuir",
        "## Comunidad",
        "<summary><b>English</b></summary>",
        "https://github.com/CFA-Society-Mexico/bsm-calculator",
        "https://github.com/CFA-Society-Mexico/research_analyst",
        "https://github.com/CFA-Society-Mexico/ai-for-finance-recursos",
        "https://www.cfasociety.org/mexico",
        "https://www.linkedin.com/company/cfa-society-mexico/",
        "https://github.com/orgs/CFA-Society-Mexico/discussions",
        PLACEHOLDER,
        "not endorsed by CFA Institute",
    ]:
        assert needle in text, ascii(needle)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_docs.py -q`
Expected: 2 FAILED (`test_required_file_exists[profile/README.md]`, `test_profile_readme_sections` with `FileNotFoundError`).

- [ ] **Step 3: Write `profile/README.md`**

Links to other files in this repo are absolute on purpose: relative links from an org profile page are not guaranteed to resolve. Only the image is relative (verified in Task 10).

````markdown
<p align="center">
  <img src="greeting.svg" width="560" alt="Bienvenidos / Welcome / Bem-vindos, typed in ASCII">
</p>

<h1 align="center">CFA Society México</h1>

<p align="center">
  <b>Herramientas financieras de código abierto, construidas por la comunidad financiera de México y Latinoamérica, con IA usada de forma responsable.</b><br>
  <i>Open-source financial tools, built by the finance community of Mexico and Latin America, with AI used responsibly.</i>
</p>

<p align="center">
  <a href="https://github.com/CFA-Society-Mexico/.github/blob/main/LICENSE"><img src="https://img.shields.io/badge/licencia%20%2F%20license-MIT-blue" alt="License: MIT"></a>
  <a href="https://github.com/CFA-Society-Mexico/.github/blob/main/CONTRIBUTING.md"><img src="https://img.shields.io/badge/PRs-bienvenidos%20%2F%20welcome-brightgreen" alt="PRs welcome"></a>
  <a href="https://github.com/orgs/CFA-Society-Mexico/discussions"><img src="https://img.shields.io/badge/GitHub-Discussions-8957e5" alt="GitHub Discussions"></a>
</p>

## Quiénes somos

Somos la comunidad de profesionales de inversión de CFA Society México. Este es el espacio donde
analistas, gestores de portafolio, especialistas en riesgo y estudiantes de México y Latinoamérica
publican herramientas financieras de código abierto: calculadoras, modelos, plugins y recursos que
cruzan el análisis financiero con el uso responsable de la inteligencia artificial.

Aquí puedes mostrar tu trabajo, aprender del de otros y contribuir al avance de nuestra profesión.

## Proyectos / Projects

| Área / Area | Proyecto / Project | Descripción / Description | Autor / Author |
|---|---|---|---|
| Derivados / Derivatives | [bsm-calculator](https://github.com/CFA-Society-Mexico/bsm-calculator) ([demo](https://cfa-society-mexico.github.io/bsm-calculator/)) | Calculadora Black-Scholes-Merton: precios de opciones europeas y griegas en vivo. / Black-Scholes-Merton calculator: European option prices and live Greeks. | Eduardo Ramos, CFA ([@EERamos](https://github.com/EERamos)) |
| Equity Research | [research_analyst](https://github.com/CFA-Society-Mexico/research_analyst) | Plugin de equity research para Claude Code, Cursor y Codex: IFRS/US GAAP/NIF, modelo de 3 estados, valuación multi-método. / Equity research plugin for Claude Code, Cursor and Codex: IFRS/US GAAP/NIF, 3-statement model, multi-method valuation. | Alan Vazquez, CFA ([@alanvaa06](https://github.com/alanvaa06)) |
| Recursos de IA / AI Resources | [ai-for-finance-recursos](https://github.com/CFA-Society-Mexico/ai-for-finance-recursos) | Recursos de IA aplicada a finanzas. / Resources on AI applied to finance. | [@edgarcalderonmx](https://github.com/edgarcalderonmx) |

¿Construiste algo? Agrégalo con un PR. / *Built something? Add it via PR.*

## IA responsable

Nos guiamos por el [Código de Ética y Estándares de Conducta Profesional de CFA Institute](https://www.cfainstitute.org/standards/professionals/code-ethics-standards):

1. **Responsabilidad humana.** Quien usa la herramienta es responsable de la conclusión. La IA asiste; no decide.
2. **Transparencia.** Documentamos supuestos, fuentes de datos y limitaciones.
3. **Confidencialidad.** Nunca datos de clientes, información confidencial ni información material no pública en prompts, código o ejemplos.
4. **No es asesoría de inversión.** Las herramientas son de apoyo educativo y analítico.
5. **Divulgación.** Cada repositorio indica dónde y cómo se usó IA para construirlo.

Detalle completo: [RESPONSIBLE_AI.md](https://github.com/CFA-Society-Mexico/.github/blob/main/RESPONSIBLE_AI.md)

## Cómo contribuir

Cualquier persona puede contribuir; no necesitas ser miembro.

1. Haz fork del repositorio (o propón un proyecto nuevo en [Discussions](https://github.com/orgs/CFA-Society-Mexico/discussions)).
2. Construye tu cambio en una rama.
3. Abre un pull request; un maintainer lo revisa.

Requisito mínimo: licencia de código abierto, reproducible (instrucciones de instalación, sin datos
ocultos), aviso de que no es asesoría de inversión y divulgación del uso de IA.
Guía completa: [CONTRIBUTING.md](https://github.com/CFA-Society-Mexico/.github/blob/main/CONTRIBUTING.md)

## Comunidad

- Sitio web: [cfasociety.org/mexico](https://www.cfasociety.org/mexico)
- LinkedIn: [CFA Society México](https://www.linkedin.com/company/cfa-society-mexico/)
- Preguntas e ideas: [GitHub Discussions](https://github.com/orgs/CFA-Society-Mexico/discussions)
- Contacto: TODO-EMAIL

<details>
<summary><b>English</b></summary>

### Who we are

We are the investment professional community of CFA Society México. This is where analysts,
portfolio managers, risk specialists and students from Mexico and Latin America publish open-source
financial tools: calculators, models, plugins and resources at the intersection of financial
analysis and the responsible use of artificial intelligence.

Show your work, learn from others, and help advance our profession.

### Responsible AI

We are guided by the [CFA Institute Code of Ethics and Standards of Professional Conduct](https://www.cfainstitute.org/standards/professionals/code-ethics-standards):

1. **Human accountability.** Whoever uses the tool owns the conclusion. AI assists; it does not decide.
2. **Transparency.** We document assumptions, data sources and limitations.
3. **Confidentiality.** Never client, confidential or material non-public data in prompts, code or examples.
4. **Not investment advice.** Tools are educational and analytical aids.
5. **Disclosure.** Every repository states where and how AI was used to build it.

Full detail: [RESPONSIBLE_AI.md](https://github.com/CFA-Society-Mexico/.github/blob/main/RESPONSIBLE_AI.md)

### How to contribute

Anyone can contribute; membership is not required.

1. Fork the repository (or propose a new project in [Discussions](https://github.com/orgs/CFA-Society-Mexico/discussions)).
2. Build your change on a branch.
3. Open a pull request; a maintainer reviews it.

Minimum bar: open-source license, reproducible (setup instructions, no hidden data), a "not
investment advice" disclaimer, and disclosure of AI use.
Full guide: [CONTRIBUTING.md](https://github.com/CFA-Society-Mexico/.github/blob/main/CONTRIBUTING.md)

### Community

- Website: [cfasociety.org/mexico](https://www.cfasociety.org/mexico)
- LinkedIn: [CFA Society México](https://www.linkedin.com/company/cfa-society-mexico/)
- Questions and ideas: [GitHub Discussions](https://github.com/orgs/CFA-Society-Mexico/discussions)
- Contact: TODO-EMAIL

</details>

---

<sub>
<b>Aviso legal.</b> Contenido educativo; no constituye asesoría de inversión. CFA® y Chartered Financial Analyst® son marcas registradas propiedad de CFA Institute. Los proyectos son contribuciones de la comunidad y no están respaldados por CFA Institute.<br>
<b>Disclaimer.</b> Educational content; not investment advice. CFA® and Chartered Financial Analyst® are registered trademarks owned by CFA Institute. Projects are community contributions and are not endorsed by CFA Institute.<br>
Saludo dibujado por <a href="https://github.com/CFA-Society-Mexico/.github/blob/main/scripts/generate_greeting.py">el script de este repo</a>, adaptado de <a href="https://github.com/alanvaa06/alanvaa06">alanvaa06</a>. Tipografía / Typeface: JetBrains Mono, OFL.
</sub>
````

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest -q`
Expected: `10 passed`

- [ ] **Step 5: Commit**

```bash
git add profile/README.md tests/test_docs.py
git commit -m "feat: add bilingual org profile README" -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 6: Code of conduct (Contributor Covenant 2.1, ES + EN)

**Files:**
- Create: `CODE_OF_CONDUCT.md`
- Modify: `tests/test_docs.py`

- [ ] **Step 1: Write the failing test**

Add `"CODE_OF_CONDUCT.md",` to `REQUIRED` and append:

```python
def test_code_of_conduct_has_both_languages_and_contact():
    text = (ROOT / "CODE_OF_CONDUCT.md").read_text(encoding="utf-8")
    assert "# C\u00f3digo de Conducta convenido para Contribuyentes" in text
    assert "# Contributor Covenant Code of Conduct" in text
    assert text.count(PLACEHOLDER) == 2
    assert "INSERT" not in text and "+++" not in text
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_docs.py -q`
Expected: 2 FAILED (required file + new test).

- [ ] **Step 3: Build the file from the official sources**

The Covenant is CC BY 4.0; the upstream files carry TOML front matter (`+++ ... +++`) and a contact placeholder, both handled here. Non-ASCII in the Python source is escaped (`\u00c9`) so stdin encoding cannot break it.

```bash
python - <<'EOF'
import pathlib, re, urllib.request
B = "https://raw.githubusercontent.com/EthicalSource/contributor_covenant/release/content/version/2/1/"
def get(name, placeholder):
    t = urllib.request.urlopen(B + name).read().decode("utf-8")
    t = re.sub(r"\A\+\+\+.*?\+\+\+\s*", "", t, flags=re.S)
    assert placeholder in t, name
    return t.replace(placeholder, "TODO-EMAIL").strip()
es = get("code_of_conduct.es.md", "[INSERTAR M\u00c9TODO DE CONTACTO]")
en = get("code_of_conduct.md", "[INSERT CONTACT METHOD]")
out = es + "\n\n---\n\n" + en + "\n"
pathlib.Path("CODE_OF_CONDUCT.md").write_text(out, encoding="utf-8", newline="\n")
print("[ok] wrote CODE_OF_CONDUCT.md", len(out), "chars")
EOF
```

Expected: `[ok] wrote CODE_OF_CONDUCT.md <n> chars`. Open the file and confirm it begins with the Spanish heading and has one `---` separator before the English heading.

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest -q`
Expected: `12 passed`

- [ ] **Step 5: Commit**

```bash
git add CODE_OF_CONDUCT.md tests/test_docs.py
git commit -m "docs: add Contributor Covenant 2.1 in Spanish and English" -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 7: RESPONSIBLE_AI.md

**Files:**
- Create: `RESPONSIBLE_AI.md`
- Modify: `tests/test_docs.py`

- [ ] **Step 1: Write the failing test**

Add `"RESPONSIBLE_AI.md",` to `REQUIRED` and append:

```python
def test_responsible_ai_covers_five_principles_in_both_languages():
    text = (ROOT / "RESPONSIBLE_AI.md").read_text(encoding="utf-8")
    assert "## Espa\u00f1ol" in text and "## English" in text
    for std in ["V(A)", "V(B)", "III(E)", "II(A)", "III(C)", "I(C)"]:
        assert std in text, std
    assert text.count("### ") == 10
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_docs.py -q`
Expected: 2 FAILED.

- [ ] **Step 3: Write `RESPONSIBLE_AI.md`**

````markdown
# IA responsable / Responsible AI

Principios comunitarios de CFA Society México para herramientas financieras construidas con IA o
para usarse con IA. Se inspiran en el
[Código de Ética y Estándares de Conducta Profesional de CFA Institute](https://www.cfainstitute.org/standards/professionals/code-ethics-standards),
pero no son una interpretación oficial de CFA Institute ni lo sustituyen.

*Community principles of CFA Society México for financial tools built with or for AI. English
version [below](#english).*

## Español

### 1. Responsabilidad humana

**Qué significa.** La IA asiste; la persona que usa la herramienta es responsable de la conclusión,
recomendación o reporte que resulte.

**Por qué.** Estándar V(A), Diligencia y base razonable: toda recomendación necesita una base
razonable y adecuada, respaldada por investigación apropiada. Un resultado de IA sin revisar no es
una base razonable.

- **Haz:** revisa y valida cada fórmula, cifra y conclusión generada con IA antes de publicarla.
- **No hagas:** presentar el resultado de un modelo como conclusión final sin revisión humana.

### 2. Transparencia

**Qué significa.** Cada herramienta documenta sus supuestos, fuentes de datos y limitaciones.

**Por qué.** Estándar V(B), Comunicación con clientes y potenciales clientes: divulgar el proceso,
los riesgos y las limitaciones, y distinguir entre hechos y opiniones.

- **Haz:** incluye en el README una sección de supuestos y limitaciones (por ejemplo, "asume
  volatilidad constante" o "datos con rezago de 15 minutos").
- **No hagas:** esconder supuestos en el código ni usar datos cuyo origen no puedas citar.

### 3. Confidencialidad

**Qué significa.** Nunca datos de clientes, información confidencial ni información material no
pública en prompts, código, ejemplos, tests o historial de git.

**Por qué.** Estándar III(E), Preservación de la confidencialidad, y Estándar II(A), Información
material no pública.

- **Haz:** usa datos públicos o sintéticos, y revisa que tus prompts de ejemplo no contengan
  información de tu empleador.
- **No hagas:** pegar reportes internos, posiciones de portafolio ni datos personales en una
  herramienta de IA o en un repositorio público. Si ocurre, avisa a los maintainers de inmediato:
  borrar un archivo no lo elimina del historial de git.

### 4. No es asesoría de inversión

**Qué significa.** Las herramientas son de apoyo educativo y analítico. No consideran la situación,
los objetivos ni las restricciones de ningún inversionista.

**Por qué.** Estándar III(C), Idoneidad, y Estándar I(C), Tergiversación: los resultados no deben
presentarse como garantizados ni como recomendaciones personalizadas.

- **Haz:** incluye un aviso visible en el README y, si aplica, en la interfaz.
- **No hagas:** usar lenguaje como "compra ya", "rendimiento garantizado" o "señal segura".

### 5. Divulgación del uso de IA

**Qué significa.** Cada repositorio indica dónde y cómo se usó IA para construirlo, y quién lo
revisó.

**Por qué.** Estándar I(C), Tergiversación: no presentar como propio, ni como verificado, un trabajo
que no lo es.

- **Haz:** agrega una sección "Uso de IA" al README con el formato de
  [CONTRIBUTING.md](CONTRIBUTING.md).
- **No hagas:** omitir el uso de IA porque "solo fue para el boilerplate".

## English

### 1. Human accountability

**What it means.** AI assists; the person using the tool owns the resulting conclusion,
recommendation or report.

**Why.** Standard V(A), Diligence and Reasonable Basis: every recommendation needs a reasonable and
adequate basis, supported by appropriate research. Unreviewed AI output is not a reasonable basis.

- **Do:** review and validate every AI-generated formula, figure and conclusion before publishing.
- **Don't:** present a model's output as a final conclusion without human review.

### 2. Transparency

**What it means.** Every tool documents its assumptions, data sources and limitations.

**Why.** Standard V(B), Communication with Clients and Prospective Clients: disclose the process,
risks and limitations, and distinguish fact from opinion.

- **Do:** include an assumptions-and-limitations section in the README (for example, "assumes
  constant volatility" or "data delayed 15 minutes").
- **Don't:** hide assumptions in code or use data whose origin you cannot cite.

### 3. Confidentiality

**What it means.** Never client data, confidential information or material non-public information
in prompts, code, examples, tests or git history.

**Why.** Standard III(E), Preservation of Confidentiality, and Standard II(A), Material Nonpublic
Information.

- **Do:** use public or synthetic data, and check that your example prompts contain nothing from
  your employer.
- **Don't:** paste internal reports, portfolio positions or personal data into an AI tool or a
  public repository. If it happens, tell the maintainers immediately: deleting a file does not
  remove it from git history.

### 4. Not investment advice

**What it means.** Tools are educational and analytical aids. They do not consider any investor's
situation, objectives or constraints.

**Why.** Standard III(C), Suitability, and Standard I(C), Misrepresentation: results must not be
presented as guaranteed or as personalized recommendations.

- **Do:** include a visible disclaimer in the README and, where relevant, in the interface.
- **Don't:** use language like "buy now", "guaranteed return" or "sure signal".

### 5. Disclosure of AI use

**What it means.** Every repository states where and how AI was used to build it, and who reviewed
it.

**Why.** Standard I(C), Misrepresentation: do not present work as your own, or as verified, when it
is not.

- **Do:** add an "AI use" section to the README using the format in
  [CONTRIBUTING.md](CONTRIBUTING.md).
- **Don't:** skip disclosure because "it was only boilerplate".
````

Note: `CONTRIBUTING.md` does not exist yet, so `test_relative_links_resolve` fails after this step. That is expected; Task 8 creates it. To keep this task green on its own, run only the targeted tests in Step 4.

- [ ] **Step 4: Run targeted tests**

Run: `python -m pytest tests/test_docs.py -q -k "responsible or required or todo"`
Expected: all selected pass. (`test_relative_links_resolve` is deselected here and turns green in Task 8.)

- [ ] **Step 5: Commit**

```bash
git add RESPONSIBLE_AI.md tests/test_docs.py
git commit -m "docs: add responsible AI principles tied to CFA Standards" -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 8: CONTRIBUTING.md

**Files:**
- Create: `CONTRIBUTING.md`
- Modify: `tests/test_docs.py`

- [ ] **Step 1: Write the failing test**

Add `"CONTRIBUTING.md",` to `REQUIRED` and append:

```python
def test_contributing_has_bar_and_disclosure_format():
    text = (ROOT / "CONTRIBUTING.md").read_text(encoding="utf-8")
    assert "## Espa\u00f1ol" in text and "## English" in text
    assert text.count("## Uso de IA / AI use") == 2
    assert "profile/README.md" in text
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_docs.py -q`
Expected: FAILED for required file, the new test, and `test_relative_links_resolve` (dangling link from Task 7).

- [ ] **Step 3: Write `CONTRIBUTING.md`**

`````markdown
# Cómo contribuir / Contributing

*English version [below](#english).*

## Español

Gracias por contribuir. Cualquier persona puede hacerlo: no necesitas ser miembro de CFA Society
México ni de la organización de GitHub.

### Qué puedes aportar

- Una herramienta nueva: calculadora, modelo, plugin, notebook o dataset público.
- Mejoras a un proyecto existente: bugs, tests, documentación, traducciones.
- Ideas y preguntas en [Discussions](https://github.com/orgs/CFA-Society-Mexico/discussions).

### Flujo

1. Haz fork del repositorio.
2. Crea una rama: `git checkout -b mi-cambio`.
3. Haz tus cambios y commits.
4. Abre un pull request contra `main` y llena el checklist.
5. Un maintainer lo revisa; responde a sus comentarios.

### Requisito mínimo

Todo proyecto y todo PR debe cumplir:

1. **Licencia de código abierto** (recomendamos MIT) en un archivo `LICENSE`.
2. **Reproducible:** instrucciones de instalación y uso; sin datos ocultos ni rutas locales.
3. **Aviso legal:** indica que no es asesoría de inversión.
4. **Divulgación del uso de IA** en el README, con este formato:

```markdown
## Uso de IA / AI use
- Herramientas / Tools: <ej. Claude Code>
- Para qué / What for: <ej. código inicial y tests>
- Revisión humana / Human review: <quién revisó qué, ej. fórmulas verificadas contra Hull (2022)>
```

Además, sigue los principios de [IA responsable](RESPONSIBLE_AI.md): sin datos confidenciales y con
supuestos documentados.

### Proponer un proyecto nuevo

1. Abre una discusión en la categoría **Ideas** con: problema, usuarios, alcance y tecnología.
2. Si hay interés, un maintainer crea el repositorio dentro de la organización y te da permisos de
   administración.
3. También puedes construirlo en tu cuenta y pedir que se agregue a la tabla del perfil.

### Aparecer en el perfil

Abre un PR a este repositorio editando la tabla "Proyectos / Projects" de
[`profile/README.md`](profile/README.md): una fila con área, enlace, descripción ES / EN y autor.

### Código de conducta

Al participar aceptas el [Código de Conducta](CODE_OF_CONDUCT.md).

## English

Thank you for contributing. Anyone can: you do not need to be a member of CFA Society México or of
the GitHub organization.

### What you can contribute

- A new tool: calculator, model, plugin, notebook or public dataset.
- Improvements to an existing project: bugs, tests, documentation, translations.
- Ideas and questions in [Discussions](https://github.com/orgs/CFA-Society-Mexico/discussions).

### Flow

1. Fork the repository.
2. Create a branch: `git checkout -b my-change`.
3. Make your changes and commits.
4. Open a pull request against `main` and fill in the checklist.
5. A maintainer reviews it; respond to their comments.

### Minimum bar

Every project and every PR must have:

1. **An open-source license** (we recommend MIT) in a `LICENSE` file.
2. **Reproducibility:** setup and usage instructions; no hidden data or local paths.
3. **A disclaimer:** state that it is not investment advice.
4. **AI-use disclosure** in the README, in this format:

```markdown
## Uso de IA / AI use
- Herramientas / Tools: <e.g. Claude Code>
- Para qué / What for: <e.g. initial code and tests>
- Revisión humana / Human review: <who reviewed what, e.g. formulas checked against Hull (2022)>
```

Also follow the [responsible AI](RESPONSIBLE_AI.md) principles: no confidential data, documented
assumptions.

### Propose a new project

1. Open a discussion in the **Ideas** category with: problem, users, scope and technology.
2. If there is interest, a maintainer creates the repository inside the organization and grants you
   admin rights.
3. You can also build it in your own account and ask for it to be added to the profile table.

### Get listed on the profile

Open a PR to this repository editing the "Proyectos / Projects" table in
[`profile/README.md`](profile/README.md): one row with area, link, ES / EN description and author.

### Code of conduct

By participating you agree to the [Code of Conduct](CODE_OF_CONDUCT.md).
`````

- [ ] **Step 4: Run the full suite**

Run: `python -m pytest -q`
Expected: all pass (`16 passed`), including `test_relative_links_resolve`.

- [ ] **Step 5: Commit**

```bash
git add CONTRIBUTING.md tests/test_docs.py
git commit -m "docs: add bilingual contributing guide with minimum bar" -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 9: Pull request template

**Files:**
- Create: `.github/pull_request_template.md`
- Modify: `tests/test_docs.py`

- [ ] **Step 1: Write the failing test**

Add `".github/pull_request_template.md",` to `REQUIRED` and append:

```python
def test_pr_template_checklist():
    text = (ROOT / ".github" / "pull_request_template.md").read_text(encoding="utf-8")
    assert text.count("- [ ] ") == 6
    # rendered inside other repos' PRs, so links must be absolute
    assert "](" not in text or "](https://" in text
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_docs.py -q`
Expected: 2 FAILED.

- [ ] **Step 3: Write `.github/pull_request_template.md`**

```markdown
## Descripción / Description

<!-- Qué cambia y por qué. / What changes and why. -->

## Checklist

- [ ] Licencia de código abierto presente / Open-source license present
- [ ] Reproducible: instrucciones de instalación y uso / Reproducible: setup and usage instructions
- [ ] Aviso "no es asesoría de inversión" / "Not investment advice" disclaimer
- [ ] Uso de IA divulgado en el README / AI use disclosed in the README
- [ ] Sin datos de clientes, confidenciales ni información material no pública / No client, confidential or material non-public data
- [ ] Supuestos y fuentes de datos documentados / Assumptions and data sources documented

Principios / Principles: [RESPONSIBLE_AI.md](https://github.com/CFA-Society-Mexico/.github/blob/main/RESPONSIBLE_AI.md)
```

- [ ] **Step 4: Run the full suite**

Run: `python -m pytest -q`
Expected: `18 passed`

- [ ] **Step 5: Commit**

```bash
git add .github/pull_request_template.md tests/test_docs.py
git commit -m "docs: add bilingual PR template with responsible-AI checklist" -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 10: Publish and verify on GitHub (USER APPROVAL GATE)

Creating a public repo under the org is outward-facing. **Ask the user for an explicit yes before Step 2.** Show them: repo name `CFA-Society-Mexico/.github`, visibility public, number of commits, and that `docs/superpowers/` (spec + plan) will be public too.

- [ ] **Step 1: Pre-flight**

```bash
python -m pytest -q
git status --short
git log --oneline | head -12
```

Expected: all tests pass, clean tree.

- [ ] **Step 2: Create repo and push (after user says yes)**

```bash
gh repo create CFA-Society-Mexico/.github --public --description "Org profile and community defaults / Perfil y archivos por defecto" --source . --remote origin --push
```

Expected: repo URL printed, `main` pushed.

- [ ] **Step 3: Verify the org page**

Open `https://github.com/CFA-Society-Mexico` in the built-in browser. Check:
- Greeting animates (cycles 3 words). If the image is broken, the relative path failed: change `src="greeting.svg"` in `profile/README.md` to `src="https://github.com/CFA-Society-Mexico/.github/raw/main/profile/greeting.svg"`, update the needle in `test_profile_readme_sections` to `greeting.svg"`, run tests, commit (`fix: use absolute greeting URL on org profile`), push, re-check.
- Hero, badges, table, `<details>` English block, and disclaimer render.
- Switch GitHub theme (or emulate `colorScheme`) to confirm the greeting follows light/dark.
- Links: click one repo link, `RESPONSIBLE_AI.md`, `CONTRIBUTING.md`. The Discussions link 404s until the user enables Discussions (manual step 2 below). That is expected.

- [ ] **Step 4: Hand off manual steps to the user**

1. Replace `TODO-EMAIL` (in `profile/README.md` twice and `CODE_OF_CONDUCT.md` twice) with the real contact email, then run `python -m pytest -q` (the TODO test still passes).
2. Enable Discussions on `CFA-Society-Mexico/.github` and set it as the org discussion repo: Org Settings -> Discussions. Requires org owner rights.
3. Pin `bsm-calculator`, `research_analyst`, `ai-for-finance-recursos` on the org profile.
4. Out of scope, flagged: add a license to `ai-for-finance-recursos` (currently none = all rights reserved).

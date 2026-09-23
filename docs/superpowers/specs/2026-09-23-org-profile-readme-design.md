# CFA Society Mexico — GitHub Org Profile & Community Defaults

**Date:** 2026-09-23
**Status:** Approved design, pending spec review
**Target repo:** `CFA-Society-Mexico/.github` (new, public), built locally at `C:\Proyectos\CFA-Society-Mexico`

## Goal

Create the public profile page for https://github.com/CFA-Society-Mexico and the org-wide
community defaults. The org is where finance professionals from Mexico and Latam contribute to an
open-source ecosystem of financial tools at the intersection of responsible AI use, showcase their
skills, and advance the profession.

## Decisions (locked)

| # | Decision | Choice |
|---|----------|--------|
| 1 | Language | Bilingual, Spanish first |
| 2 | Who contributes | Anyone: fork -> PR, maintainers review; no org membership required |
| 3 | Responsible AI | 5 principle bullets in README + full `RESPONSIBLE_AI.md` |
| 4 | Project showcase | Hand-curated table grouped by area, with author credit; plus pinned repos |
| 5 | Repo scope | README + RESPONSIBLE_AI + CONTRIBUTING + CODE_OF_CONDUCT + PR template |
| 6 | Community links | Website + LinkedIn + contact email + issues on `.github`. GitHub Discussions deliberately off for now (user decision, 2026-09-23) |
| 7 | Bilingual layout | Shared bilingual hero + table; Spanish body open; English in one `<details>` |
| 8 | Header visual | Stock-ticker tape (SMIL SVG, full width), then text hero; no org stats, no CI. Replaced the first ASCII greeting (too close to alanvaa06's personal profile) |
| 9 | Ticker content | BIENVENIDOS ▲ WELCOME ▲ BEM-VINDOS ▲ FINANZAS ▲ AGENTIC AI ▲ OPEN SOURCE; greetings accent, topics foreground; no fake quotes |

## File structure

```
(repo root = CFA-Society-Mexico/.github)
├── profile/README.md                  org profile page rendered by GitHub
├── profile/ticker.svg                 generated ticker animation (committed output)
├── scripts/svgkit.py                  copied as-is from alanvaa06/alanvaa06
├── scripts/generate_ticker.py         ticker generator (pure Python)
├── assets/fonts/                      jbmono-latin-bold.woff2, OFL.txt (copied from alanvaa06/alanvaa06)
├── RESPONSIBLE_AI.md                  full principles, ES + EN
├── CONTRIBUTING.md                    quality bar + fork/PR flow, ES + EN
├── CODE_OF_CONDUCT.md                 Contributor Covenant 2.1, ES + EN
├── .github/pull_request_template.md   responsible-AI checklist, ES + EN
├── README.md                          one line: this repo holds org defaults
├── LICENSE                            MIT, copyright CFA Society Mexico contributors
└── docs/superpowers/specs/            this spec (harmless; GitHub ignores it)
```

`CONTRIBUTING.md`, `CODE_OF_CONDUCT.md` and the PR template act as defaults for every org repo that
lacks its own. They are placed at repo root (and `.github/` for the template), which GitHub accepts
for org-level community health files.

## `profile/README.md` — section by section

Length target: about one screen of Spanish above the `<details>` fold.

0. **Ticker.** Centered `<img src="ticker.svg" width="100%" alt="Ticker: ...">`. See "Ticker animation"
   below.
1. **Hero (bilingual).** `# CFA Society México` + ES tagline + EN tagline (italic). Badges:
   License MIT, PRs welcome.
2. **Quiénes somos.** 3-4 lines: community of finance professionals in Mexico and Latam; open-source
   financial tools; responsible use of AI; showcase skills; advance the profession.
3. **Proyectos / Projects.** Single shared table, bilingual headers
   (`Área / Area | Proyecto / Project | Descripción / Description | Autor / Author`), grouped:
   - Derivados / Derivatives: `bsm-calculator` — Eduardo Ramos, CFA (@EERamos) — plus live demo
     https://cfa-society-mexico.github.io/bsm-calculator/
   - Equity Research: `research_analyst` — Alan Vazquez, CFA (@alanvaa06)
   - Recursos de IA / AI Resources: `ai-for-finance-recursos` — @edgarcalderonmx
   Descriptions: one line each, bilingual (`ES / EN`), derived from each repo's own description.
   Footer line: "¿Construiste algo? Agrégalo con un PR. / Built something? Add it via PR."
4. **IA responsable.** Five bullets, anchored to the CFA Institute Code of Ethics and Standards of
   Professional Conduct:
   1. Human accountability: the professional who uses the tool owns the conclusion.
   2. Transparency: assumptions, data sources and model limits are documented.
   3. Confidentiality: no client, confidential or material non-public data in prompts, code or
      examples.
   4. Not investment advice: tools are educational and analytical aids.
   5. Disclosure: each repo states where and how AI was used to build it.
   Link: `RESPONSIBLE_AI.md`.
5. **Cómo contribuir.** Three steps (fork -> build -> PR). Minimum bar: open-source license,
   reproducible (setup instructions, no hidden data), disclaimer present, AI-use disclosure.
   Ideas and questions go to issues on `.github`. Link: `CONTRIBUTING.md`.
6. **Comunidad.** Website, LinkedIn, issues, email.
7. **English** — one `<details><summary>English</summary>` block translating sections 2, 4, 5, 6.
8. **Aviso legal / Disclaimer (bilingual, small text).** Educational content, not investment advice.
   CFA® and Chartered Financial Analyst® are registered trademarks owned by CFA Institute.
   Projects are community contributions and are not endorsed by CFA Institute.

## Supporting files

- **`RESPONSIBLE_AI.md`**: Spanish section then English section. For each of the 5 principles: what
  it means, why (tie to the relevant CFA Standard, e.g. I(C) Misrepresentation, III(E) Preservation
  of Confidentiality, V(A) Diligence and Reasonable Basis, V(B) Communication with Clients), and a
  concrete do/don't for a contributor.
- **`CONTRIBUTING.md`**: Spanish then English. Fork/branch/PR flow; minimum bar (same 4 items as
  README); how to propose a new project (issue on `.github` -> repo created under org by maintainers);
  how to get listed in the profile table (PR editing `profile/README.md`).
- **`CODE_OF_CONDUCT.md`**: Contributor Covenant 2.1, official Spanish translation followed by the
  English original. Enforcement contact = the contact email.
- **`.github/pull_request_template.md`**: short description field + checklist: license present,
  reproducible, disclaimer present, AI-use disclosed, no confidential data, sources/assumptions
  documented. Bilingual labels inline (`ES / EN`).
- **`README.md`**: one bilingual line explaining the repo holds the org profile and defaults.

## Ticker animation

A stock-ticker tape scrolls right to left:
`BIENVENIDOS ▲ WELCOME ▲ BEM-VINDOS ▲ FINANZAS ▲ AGENTIC AI ▲ OPEN SOURCE`, looping.

- Generator: `scripts/generate_ticker.py`, pure Python (no Pillow/numpy, no system fonts). Output
  `profile/ticker.svg` is committed; regenerate only when wording changes. No CI.
- Font: JetBrains Mono Bold Latin subset (`jbmono-latin-bold.woff2`, OFL), embedded as base64 via
  `svgkit.font_face`. Monospace advance 0.6 em lets the script compute every x position exactly.
- Colors: greetings in accent blue, topics in foreground, `▲` separators drawn as SVG paths (the font
  subset has no `▲`) in GitHub green (`#3fb950` dark / `#1a7f37` light). All theme-aware via
  `prefers-color-scheme`.
- Motion: one SMIL `animateTransform` translates the tape by exactly one period at 60 px/s
  (~17.8s loop). The tape is repeated past `W + period` so the loop has no visible seam.
- Frame: 960x56 viewBox, thin top/bottom rules, luminance mask fading both edges (works on any
  page background).
- No fake price changes or percentages: in a CFA org they could read as real market data.

Tests (`tests/test_ticker.py`): word order, class per word, no `<script>`, seamless loop (shift ==
period, every first-copy word reappears one period later, tape covers `W + period`), all glyphs
present in the embedded font.

Verified: relative `src` resolves on the org profile page (GitHub rewrites it to
`.../raw/main/profile/<file>.svg`).

## Links and values

| Item | Value | Status |
|------|-------|--------|
| LinkedIn | https://www.linkedin.com/company/cfa-society-mexico/ | confirmed by user |
| Website | https://www.cfasociety.org/mexico | verified (HTTP 200) |
| Contact email | `TODO-EMAIL` token (same token in every file) | **user to fill** |
| Ideas / questions | https://github.com/CFA-Society-Mexico/.github/issues | active (Discussions disabled) |
| License badge | MIT, pointing to this repo's own `LICENSE` | added: `ai-for-finance-recursos` has no license, so the badge must not imply all repos are MIT |

## Manual steps (user, in GitHub UI)

1. Done: public repo `CFA-Society-Mexico/.github` created by Claude via `gh` (user approved).
2. Done: contact email set to staff@cfamexico.org; website verified.
3. Pending: pin the 3 repos on the org profile.
4. Not now: GitHub Discussions stays disabled until the user decides otherwise.

## Out of scope

- Adding a license to `ai-for-finance-recursos` (currently none = all rights reserved). Flagged,
  handled separately.
- Issue templates, `SECURITY.md`, auto-generated project table, nightly org stats SVGs
  (revisit at ~10-15 repos).

## Verification

- Ticker SVG opened locally over HTTP, light and dark scheme: scrolls smoothly, loop has no visible
  seam, greetings blue, topics foreground, triangles green, edges fade.
- Markdown renders correctly on GitHub (preview after push): ticker animates, table, badges,
  `<details>` block.
- All links resolve (except the `TODO` email).
- No `TODO` other than the `TODO-EMAIL` token (enforced by `tests/test_docs.py`).

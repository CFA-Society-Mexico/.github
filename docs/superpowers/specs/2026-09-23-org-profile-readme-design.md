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
| 6 | Community links | Website + LinkedIn + contact email + GitHub Discussions |
| 7 | Bilingual layout | Shared bilingual hero + table; Spanish body open; English in one `<details>` |
| 8 | Header visual | Text only, no banner (org avatar already rendered by GitHub) |

## File structure

```
(repo root = CFA-Society-Mexico/.github)
├── profile/README.md                  org profile page rendered by GitHub
├── RESPONSIBLE_AI.md                  full principles, ES + EN
├── CONTRIBUTING.md                    quality bar + fork/PR flow, ES + EN
├── CODE_OF_CONDUCT.md                 Contributor Covenant 2.1, ES + EN
├── .github/pull_request_template.md   responsible-AI checklist, ES + EN
├── README.md                          one line: this repo holds org defaults
└── docs/superpowers/specs/            this spec (harmless; GitHub ignores it)
```

`CONTRIBUTING.md`, `CODE_OF_CONDUCT.md` and the PR template act as defaults for every org repo that
lacks its own. They are placed at repo root (and `.github/` for the template), which GitHub accepts
for org-level community health files.

## `profile/README.md` — section by section

Length target: about one screen of Spanish above the `<details>` fold.

1. **Hero (bilingual).** `# CFA Society México` + ES tagline + EN tagline (italic). Badges:
   License MIT, PRs welcome, GitHub Discussions.
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
   Ideas and questions go to Discussions. Link: `CONTRIBUTING.md`.
6. **Comunidad.** Website, LinkedIn, Discussions, email.
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
  README); how to propose a new project (Discussions -> repo created under org by maintainers);
  how to get listed in the profile table (PR editing `profile/README.md`).
- **`CODE_OF_CONDUCT.md`**: Contributor Covenant 2.1, official Spanish translation followed by the
  English original. Enforcement contact = the contact email.
- **`.github/pull_request_template.md`**: short description field + checklist: license present,
  reproducible, disclaimer present, AI-use disclosed, no confidential data, sources/assumptions
  documented. Bilingual labels inline (`ES / EN`).
- **`README.md`**: one bilingual line explaining the repo holds the org profile and defaults.

## Links and values

| Item | Value | Status |
|------|-------|--------|
| LinkedIn | https://www.linkedin.com/company/cfa-society-mexico/ | confirmed by user |
| Website | https://www.cfasociety.org/mexico | **assumed, user to confirm** |
| Contact email | `TODO` placeholder | **user to fill** |
| Discussions | https://github.com/orgs/CFA-Society-Mexico/discussions | active after manual step |
| License badge | MIT (matches existing repos) | confirmed from repo metadata |

## Manual steps (user, in GitHub UI)

1. Create public repo `CFA-Society-Mexico/.github` (or let Claude create it via `gh`, with approval).
2. Enable Discussions on `.github` and set it as the org discussion repo
   (Org Settings -> Discussions). Requires org owner rights (not verified).
3. Pin the 3 repos on the org profile.
4. Replace the email `TODO` and confirm the website URL.

## Out of scope

- Adding a license to `ai-for-finance-recursos` (currently none = all rights reserved). Flagged,
  handled separately.
- Issue templates, `SECURITY.md`, banner image, auto-generated project table (revisit at ~15 repos).

## Verification

- Markdown renders correctly on GitHub (preview after push): table, badges, `<details>` block.
- All links resolve (except the `TODO` email).
- No `TODO` other than the email placeholder.

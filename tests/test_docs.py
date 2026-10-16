"""Guards for the Markdown files of the org .github repo.

Non-ASCII needles are written as escapes so failure output stays
cp1252-safe on Windows consoles.
"""

import pathlib
import re

import pytest

ROOT = pathlib.Path(__file__).resolve().parent.parent
PLACEHOLDER = "TODO-EMAIL"
CONTACT = "staff@cfamexico.org"

REQUIRED = [
    "README.md",
    "LICENSE",
    "profile/README.md",
    "CODE_OF_CONDUCT.md",
    "RESPONSIBLE_AI.md",
    "CONTRIBUTING.md",
    ".github/pull_request_template.md",
    ".github/ISSUE_TEMPLATE/proyecto-nuevo.yml",
    ".github/workflows/recordatorio-propuestas.yml",
    "skills/proponer-proyecto/SKILL.md",
]

FORM = ROOT / ".github" / "ISSUE_TEMPLATE" / "proyecto-nuevo.yml"
SKILL = ROOT / "skills" / "proponer-proyecto" / "SKILL.md"
FORM_ID = re.compile(r"^    id: (\S+)$", re.M)

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


def test_profile_readme_sections():
    text = (ROOT / "profile" / "README.md").read_text(encoding="utf-8")
    for needle in [
        'src="ticker.svg"',
        "## Quiénes somos",
        "## Proyectos / Projects",
        "## IA responsable",
        "## Cómo contribuir",
        "## Comunidad",
        "<summary><b>English</b></summary>",
        "https://github.com/CFA-Society-Mexico/bsm-calculator",
        "https://github.com/CFA-Society-Mexico/research_analyst",
        "https://github.com/CFA-Society-Mexico/ai-for-finance-recursos",
        "https://www.cfasociety.org/mexico",
        "https://www.linkedin.com/company/cfa-society-mexico/",
        "https://github.com/CFA-Society-Mexico/.github/issues",
        CONTACT,
        "not endorsed by CFA Institute",
    ]:
        assert needle in text, ascii(needle)


def test_code_of_conduct_has_both_languages_and_contact():
    text = (ROOT / "CODE_OF_CONDUCT.md").read_text(encoding="utf-8")
    assert "# Código de Conducta convenido para Contribuyentes" in text
    assert "# Contributor Covenant Code of Conduct" in text
    assert text.count(CONTACT) == 2
    assert "INSERT" not in text and "+++" not in text


def test_responsible_ai_covers_five_principles_in_both_languages():
    text = (ROOT / "RESPONSIBLE_AI.md").read_text(encoding="utf-8")
    assert "## Español" in text and "## English" in text
    for std in ["V(A)", "V(B)", "III(E)", "II(A)", "III(C)", "I(C)"]:
        assert std in text, std
    assert text.count("### ") == 10


def test_contributing_has_bar_and_disclosure_format():
    text = (ROOT / "CONTRIBUTING.md").read_text(encoding="utf-8")
    assert "## Español" in text and "## English" in text
    assert text.count("## Uso de IA / AI use") == 2
    assert "profile/README.md" in text


def test_pr_template_checklist():
    text = (ROOT / ".github" / "pull_request_template.md").read_text(encoding="utf-8")
    assert text.count("- [ ] ") == 6
    # rendered inside other repos' PRs, so links must be absolute
    assert "](" not in text or "](https://" in text


def test_no_discussions_references():
    # Discussions is disabled for now; ideas and questions go to issues
    for p in md_files():
        assert "discussion" not in p.read_text(encoding="utf-8").lower(), str(
            p.relative_to(ROOT)
        )


def test_proposal_form_disclaimers_and_confirmations():
    text = FORM.read_text(encoding="utf-8")
    assert 'labels: ["propuesta"]' in text
    for needle in [
        "no implica aceptaci\u00f3n, compromiso ni respaldo",
        "does not imply acceptance, commitment or endorsement",
        "Este issue es p\u00fablico",
        "This issue is public",
        "CFA-Society-Mexico/.github",
    ]:
        assert needle in text, ascii(needle)
    assert text.count("          required: true") == 4


def test_skill_covers_every_form_field():
    ids = FORM_ID.findall(FORM.read_text(encoding="utf-8"))
    assert ids, "no field ids found"
    skill = SKILL.read_text(encoding="utf-8")
    assert skill.startswith("---\nname: proponer-proyecto\n")
    for field in ids:
        if field == "confirmaciones":
            continue  # the person ticks these; the skill must not prefill them
        assert f"`{field}`" in skill, field
    assert "template=proyecto-nuevo.yml" in skill


def test_reminder_workflow_never_closes():
    text = (ROOT / ".github" / "workflows" / "recordatorio-propuestas.yml").read_text(
        encoding="utf-8"
    )
    assert "only-labels: propuesta" in text
    assert "days-before-close: -1" in text
    assert "days-before-pr-stale: -1" in text


def test_contributing_proposal_flow():
    text = (ROOT / "CONTRIBUTING.md").read_text(encoding="utf-8")
    for needle in [
        "template=proyecto-nuevo.yml",
        "skills/proponer-proyecto/SKILL.md",
        "## Contribuci\u00f3n comunitaria / Community contribution",
        "**Criterios de revisi\u00f3n**",
        "**Review criteria**",
    ]:
        assert needle in text, ascii(needle)

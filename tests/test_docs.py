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


def test_profile_readme_sections():
    text = (ROOT / "profile" / "README.md").read_text(encoding="utf-8")
    for needle in [
        'src="greeting.svg"',
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
        "https://github.com/orgs/CFA-Society-Mexico/discussions",
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

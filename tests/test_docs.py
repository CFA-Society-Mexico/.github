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

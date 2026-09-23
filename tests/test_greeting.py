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
    assert "código abierto" in svg
    assert "prefers-color-scheme" in svg


def test_caption_glyphs_in_embedded_font():
    from fontTools.ttLib import TTFont

    cmap = TTFont(gg.ROOT / "assets" / "fonts" / "jbmono-latin.woff2").getBestCmap()
    missing = sorted({hex(ord(c)) for c in gg.CAPTION if c != " " and ord(c) not in cmap})
    assert not missing, missing

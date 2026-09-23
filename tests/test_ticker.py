import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "scripts"))

import generate_ticker as gt  # noqa: E402

TEXT = re.compile(r'<text x="([\d.]+)"[^>]*class="(\w+) tape"[^>]*>([^<]+)</text>')


def texts(svg):
    return [(float(x), cls, word) for x, cls, word in TEXT.findall(svg)]


def test_words_in_order():
    assert gt.GREETINGS == ["BIENVENIDOS", "WELCOME", "BEM-VINDOS"]
    assert gt.TOPICS == ["FINANZAS", "AGENTIC AI", "OPEN SOURCE"]
    assert [w for _, _, w in texts(gt.build_svg())][: len(gt.WORDS)] == gt.WORDS


def test_svg_structure():
    svg = gt.build_svg()
    assert svg.startswith("<svg") and svg.endswith("</svg>")
    assert "<script" not in svg
    assert "animateTransform" in svg and 'repeatCount="indefinite"' in svg
    assert "prefers-color-scheme" in svg


def test_greetings_accent_topics_fg():
    for _, cls, word in texts(gt.build_svg()):
        assert cls == ("accent" if word in gt.GREETINGS else "fg"), word


def test_loop_is_seamless():
    svg = gt.build_svg()
    shift = float(re.search(r'to="-([\d.]+) 0"', svg).group(1))
    assert abs(shift - gt.period()) < 0.1
    items = texts(svg)
    for x, _, word in items[: len(gt.WORDS)]:
        assert any(w == word and abs(x2 - (x + shift)) < 0.2 for x2, _, w in items), word
    last_x, _, last_word = items[-1]
    assert last_x + len(last_word) * gt.CW >= gt.W + shift


def test_glyphs_in_embedded_font():
    from fontTools.ttLib import TTFont

    cmap = TTFont(gt.ROOT / "assets" / "fonts" / "jbmono-latin-bold.woff2").getBestCmap()
    missing = sorted({hex(ord(c)) for c in "".join(gt.WORDS) if ord(c) not in cmap})
    assert not missing, missing

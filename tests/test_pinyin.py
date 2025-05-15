import pytest
from obe_mdn_anki.utils import process_pinyin


@pytest.mark.parametrize(
    "s,expected",
    [
        ("da4 piao4 liang guo2 (slang)", "dà piào liang guó (slang)"),
        ("fǎ guó (Taiwan: fà guó)", "fǎ guó (taiwan: fà guó)"),
        ("fǎ guó (Taiwan: fa4 guo2)", "fǎ guó (taiwan: fà guó)"),
        ("nv4", "nǜ"),
        ("nü4", "nǜ"),
    ],
)
def test_pinyin(s, expected):
    assert process_pinyin(s) == expected

# adapted from https://stackoverflow.com/questions/8200349/convert-numbered-pinyin-to-pinyin-with-tone-marks
import re

py_tone_mark = {
    0: "aoeiuv\u00fc",
    1: "\u0101\u014d\u0113\u012b\u016b\u01d6\u01d6",
    2: "\u00e1\u00f3\u00e9\u00ed\u00fa\u01d8\u01d8",
    3: "\u01ce\u01d2\u011b\u01d0\u01d4\u01da\u01da",
    4: "\u00e0\u00f2\u00e8\u00ec\u00f9\u01dc\u01dc",
}


def process_pinyin(s: str) -> str:
    s = s.lower()
    result = s
    words = re.finditer(r"([a-z|\u00fc]+[1-4])", s)
    for word_match in words:
        word = word_match.group(0)
        tone = int(word[-1])
        m = re.search("[aoeiuv\u00fc]+", word)
        assert m is not None, f"Could not process pinyin {word}!"
        if len(m.group(0)) == 1:
            word = (
                word[: m.start(0)]
                + py_tone_mark[tone][py_tone_mark[0].index(m.group(0))]
                + word[m.end(0) :]
            )
        else:
            if "a" in word:
                word = word.replace("a", py_tone_mark[tone][0])
            elif "o" in word:
                word = word.replace("o", py_tone_mark[tone][1])
            elif "e" in word:
                word = word.replace("e", py_tone_mark[tone][2])
            elif word.endswith("ui"):
                word = word.replace("i", py_tone_mark[tone][3])
            elif word.endswith("iu"):
                word = word.replace("u", py_tone_mark[tone][4])
        word = word[:-1]
        result = result.replace(word_match.group(0), word)
    return result

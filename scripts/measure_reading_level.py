"""Measure the reading-level numbers of step A7 with code (run it on the PUNCTUATED transcript).

Usage: python -I -X utf8 measure_reading_level.py <punctuated_transcript.txt> [--lang en|de] [output.json]

Measures: sentence-length ratios (short <=12 / medium 13-24 / long 25+ words, the average, the longest),
average word length, unique-word ratio, the most repeated words, the long-word ratio, and a readability formula
suited to the language (EN: Flesch Reading Ease, DE: Wiener Sachtextformel 1). Syllables are estimated from vowel
groups, so the formulas are APPROXIMATE: use them to compare your scripts with the competitor's, not as exact values.
It does no interpretation: the CEFR level (B1/B2/C1) and the literary quality are the strong model's comment.
Word-level numbers need no punctuation; the sentence numbers need the punctuated file (see verify_punctuation_repair.py).
"""
import json
import re
import statistics
import sys
from collections import Counter
from pathlib import Path

STOP = set("the a an and or of to in is it that this you your for on are was be as with at by not what how why do does can will from but if its we they i he she so then there here our just like when which who would could about into than them his her their have has had been were all one more some out up no yes very also".split())


def syllables(word, lang):
    w = word.lower()
    vowels = "aeiouy" + ("\u00e4\u00f6\u00fc" if lang == "de" else "")  # German umlauts as escapes
    groups = re.findall(f"[{vowels}]+", w)
    n = len(groups)
    if lang == "en" and w.endswith("e") and not w.endswith(("le", "ee")) and n > 1:
        n -= 1
    return max(1, n)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    lang = "en"
    if "--lang" in sys.argv:
        i = sys.argv.index("--lang")
        if i + 1 >= len(sys.argv):
            sys.exit("--lang needs a value: en or de")
        lang = sys.argv[i + 1]
        args = [a for k, a in enumerate(sys.argv[1:], 1) if not a.startswith("--") and k != i + 1]
    if not args:
        sys.exit(__doc__)
    if lang not in ("en", "de"):
        sys.exit("--lang must be en or de")
    try:
        text = Path(args[0]).read_text(encoding="utf-8")
    except OSError as e:
        sys.exit(f"Cannot read the file: {e}")
    text = text.replace(chr(0x2019), "'").replace(chr(0x2018), "'")  # curly apostrophes
    sentences = [s for s in re.split(r"(?<=[.!?])[\"')\]”’]*\s+", text.strip()) if s.strip()]
    lens = [len(re.findall(r"[\w']+", s)) for s in sentences]
    lens = [n for n in lens if n > 0]
    if len(lens) < 5:
        sys.exit("Too few sentences: the text looks unpunctuated. Repair the punctuation first (see verify_punctuation_repair.py).")
    words = re.findall(r"[\w']+", text.lower())
    n = len(words)
    avg = statistics.mean(lens)
    syl = [syllables(w, lang) for w in words]
    res = {
        "language": lang,
        "words": n,
        "sentences": len(lens),
        "sentence_length_average": round(avg, 1),
        "sentence_length_longest": max(lens),
        "short_up_to_12_percent": round(sum(1 for x in lens if x <= 12) / len(lens) * 100, 1),
        "medium_13_to_24_percent": round(sum(1 for x in lens if 13 <= x <= 24) / len(lens) * 100, 1),
        "long_25_plus_percent": round(sum(1 for x in lens if x >= 25) / len(lens) * 100, 1),
        "average_word_length": round(sum(len(w) for w in words) / n, 2),
        "unique_word_ratio_percent": round(len(set(words)) / n * 100, 1),
        "long_word_ratio_percent_over_6_letters": round(sum(1 for w in words if len(w) > 6) / n * 100, 1),
        "most_repeated_words": Counter(w for w in words if w not in STOP and len(w) > 3).most_common(15),
        "note": "Formulas use estimated syllables: approximate, for comparison only.",
    }
    if lang == "de":
        ms = sum(1 for s in syl if s >= 3) / n * 100
        iw = res["long_word_ratio_percent_over_6_letters"]
        es = sum(1 for s in syl if s == 1) / n * 100
        res["wiener_sachtextformel_1"] = round(0.1935 * ms + 0.1672 * avg + 0.1297 * iw - 0.0327 * es - 0.875, 1)
    else:
        res["flesch_reading_ease"] = round(206.835 - 1.015 * avg - 84.6 * (sum(syl) / n), 1)
    out = Path(args[1]) if len(args) > 1 else None
    payload = json.dumps(res, ensure_ascii=False, indent=1)
    if out:
        out.write_text(payload, encoding="utf-8")
    print(payload)


if __name__ == "__main__":
    main()

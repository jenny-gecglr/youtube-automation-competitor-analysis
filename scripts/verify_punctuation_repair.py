"""Verify by code that a punctuation repair changed NO word (the mandatory check of step A7).

Usage: python -I -X utf8 verify_punctuation_repair.py <raw_transcript.txt> <punctuated_transcript.txt>

Why: NotebookLM's verbatim transcripts have no punctuation, so sentence-length ratios cannot be measured from them.
A cheap tool (Gemini or a small Claude model) adds only punctuation and capital letters. This script proves it
added, removed or changed no word: both texts are reduced to a lowercase word sequence (letters, digits and
apostrophes) and compared word for word.

Exit code 0 = identical word sequence, 1 = a difference (the first mismatch is printed), 2 = bad usage.
"""
import re
import sys
from pathlib import Path


def words(text):
    text = text.replace("’", "'").replace("‘", "'")
    return re.findall(r"[\w']+", text.lower())


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(2)
    try:
        raw = words(Path(sys.argv[1]).read_text(encoding="utf-8"))
        fixed = words(Path(sys.argv[2]).read_text(encoding="utf-8"))
    except OSError as e:
        print(f"Cannot read a file: {e}")
        sys.exit(2)
    if not raw or not fixed:
        print("A file has no words: nothing to compare.")
        sys.exit(1)
    print(f"raw words: {len(raw)}   punctuated words: {len(fixed)}")
    for i, (a, b) in enumerate(zip(raw, fixed)):
        if a != b:
            print(f"DIFFERENT at word {i}: raw {raw[max(0, i - 3):i + 4]} vs punctuated {fixed[max(0, i - 3):i + 4]}")
            sys.exit(1)
    if len(raw) != len(fixed):
        print("DIFFERENT: one text is longer than the other (the shared part is identical).")
        sys.exit(1)
    print("OK: the word sequence is identical. The punctuated file may be used for sentence measurements.")


if __name__ == "__main__":
    main()

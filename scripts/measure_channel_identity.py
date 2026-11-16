"""Measure a transcript with code for the channel identity card (the model spends no tokens on counting).

Usage: python -I -X utf8 measure_channel_identity.py <transcript.txt> [output.json]

What it does: reports evidence for telling a narrator channel from a lesson or news channel as densities per
1000 words, and finds CTA positions as percentages of the transcript. It needs NO punctuation (raw NotebookLM
transcripts have none). It does not interpret anything: the strongest model reads the transcript and interprets
the numbers on the card. English-language transcripts only; edit the marker lists for other languages.
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

STOP = set("the a an and or of to in is it that this you your for on are was be as with at by not what how why do does can will from but if its we they i he she so then there here our just like when which who would could about into than them his her their have has had been were all one more some out up no yes very also".split())

# Every list is a rough marker. Densities are for comparison, not a verdict.
MARKERS = {
    "lesson_exam": ["exam", "homework", "chapter", "lesson", "syllabus", "worksheet", "quiz", "revise", "revision", "grade", "textbook", "solve", "problem set", "formula", "equation"],
    "story_history": ["in 18", "in 19", "year old", "was born", "daydream", "story", "imagine", "once", "discovered", "scientist", "physicist", "experiment", "century"],
    "analogy": ["imagine", "think about", "like a", "it's like", "as if", "analogy", "picture this", "for example", "suppose"],
    "curiosity_question": ["why", "what if", "how can", "what happens", "so where", "could it be", "is it really"],
    "honest_caveat": ["not quite", "simplified", "a little simplified", "physicists would point out", "in a sense", "strictly speaking", "isn't really", "actually wrong"],
    "sensational_words": ["shocking", "you won't believe", "mind-blowing", "insane", "nobody"],
    "currentness_trend": ["this week", "breaking", "just announced", "latest", "yesterday", "recently", "this year", "new update", "2025", "2026", "today's"],
    "timeless_evergreen": ["always", "for centuries", "ever since", "fundamental", "timeless", "no matter", "everyone", "every observer"],
}
CTA = {
    "subscribe": ["subscribe", "subscribing", "notification", "notifications"],
    "comment": ["comment", "let me know", "tell us", "leave a"],
    "like": ["like the video", "hit like", "thumbs up", "like button"],
    "reference_to_earlier_video": ["our video", "earlier video", "our earlier", "check out our", "if you watched our", "remember our video", "previous video"],
    "next_video": ["next video", "next one", "see you next time", "next time"],
}


def positions(text_lower, phrases, n_words):
    out = []
    for phrase in phrases:
        for m in re.finditer(re.escape(phrase), text_lower):
            count = len(text_lower[:m.start()].split())
            out.append(round(count / n_words * 100))
    return sorted(out)


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    path = Path(sys.argv[1])
    text = path.read_text(encoding="utf-8")
    lower = text.lower()
    words = re.findall(r"[A-Za-z']+", text)
    n = len(words)
    if n == 0:
        sys.exit("No words found in the transcript.")
    ws = [w.lower() for w in words]
    result = {"file": str(path), "words": n, "characters": len(text)}
    result["unique_word_ratio_percent"] = round(len(set(ws)) / n * 100, 1)
    result["pronouns_per_1000_words"] = {
        "you/your": round((ws.count("you") + ws.count("your")) / n * 1000, 1),
        "we/our/us": round((ws.count("we") + ws.count("our") + ws.count("us")) / n * 1000, 1),
        "I/my": round((ws.count("i") + ws.count("my")) / n * 1000, 1),
    }
    result["marker_density_per_1000_words"] = {
        name: round(sum(lower.count(x) for x in lst) / n * 1000, 2) for name, lst in MARKERS.items()
    }
    result["numbers_and_years"] = {
        "years (1600-2099)": len(re.findall(r"\b(1[6-9]\d\d|20\d\d)\b", text)),
        "digits": len(re.findall(r"\b\d[\d,\.]*\b", text)),
    }
    result["cta_positions_percent"] = {name: positions(lower, lst, n) for name, lst in CTA.items()}
    result["hook_sample_first_150_words"] = " ".join(text.split()[:150])
    result["most_repeated_words"] = Counter(w for w in ws if w not in STOP and len(w) > 3).most_common(15)
    # Rhythm: curiosity questions, analogies and story markers across ten equal slices.
    slices = []
    size = max(1, n // 10)
    for i in range(10):
        part = " ".join(text.split()[i * size:(i + 1) * size]).lower()
        slices.append({
            "slice": f"{i * 10}-{(i + 1) * 10}%",
            "curiosity_question": sum(part.count(x) for x in MARKERS["curiosity_question"]),
            "analogy": sum(part.count(x) for x in MARKERS["analogy"]),
            "story_history": sum(part.count(x) for x in MARKERS["story_history"]),
        })
    result["markers_in_ten_slices"] = slices
    out_path = Path(sys.argv[2]) if len(sys.argv) > 2 else None
    payload = json.dumps(result, ensure_ascii=False, indent=1)
    if out_path:
        out_path.write_text(payload, encoding="utf-8")
    print(payload)


if __name__ == "__main__":
    main()

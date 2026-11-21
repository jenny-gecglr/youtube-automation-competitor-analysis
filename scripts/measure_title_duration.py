"""Quick competitor analysis tool: title and duration/views measurement (code only, spends no tokens).

Usage:
  python -I -X utf8 scripts/measure_title_duration.py <competitor folder> [output.json]
Input: <competitor folder>/titles.txt (line format: VIEWS<TAB>TITLE; views may be 0) and
       <competitor folder>/videos/*/meta.json (keys used: title, views, duration_sec)
Output: a summary on screen and, if given, a JSON file. Measurement only, no interpretation. Label: [MEASURED].
Note: lines showing 0 views in titles.txt can be a yt-dlp list artifact. Ratios are computed over all titles;
the views statistics are computed only over the videos that have a meta.json.
"""
import sys, os, re, json, glob, statistics
from collections import Counter

if len(sys.argv) < 2:
    print(__doc__); sys.exit(1)
K = sys.argv[1]
OUT = sys.argv[2] if len(sys.argv) > 2 else None

titles = []
p = os.path.join(K, "titles.txt")
if os.path.exists(p):
    for l in open(p, encoding="utf-8", errors="replace"):
        l = l.rstrip("\n")
        if not l.strip():
            continue
        parts = l.split("\t", 1)
        t = parts[1] if len(parts) == 2 else parts[0]
        titles.append(t.strip())

metas = []
for f in sorted(glob.glob(os.path.join(K, "videos", "*", "meta.json"))):
    try:
        metas.append(json.load(open(f, encoding="utf-8")))
    except Exception:
        pass

def pct(n):
    return round(100 * n / len(titles), 1) if titles else None

res = {"title_count": len(titles), "video_meta_count": len(metas)}
if titles:
    words = [len(t.split()) for t in titles]
    chars = [len(t) for t in titles]
    res["words_mean"] = round(statistics.mean(words), 1)
    res["words_median"] = statistics.median(words)
    res["characters_mean"] = round(statistics.mean(chars), 1)
    res["characters_over_70"] = sum(1 for c in chars if c > 70)
    res["ratio_percent"] = {
        "contains_digit": pct(sum(bool(re.search(r"\d", t)) for t in titles)),
        "question_mark": pct(sum("?" in t for t in titles)),
        "you_your_address": pct(sum(bool(re.search(r"\byou(r|rs|rself)?\b", t, re.I)) for t in titles)),
        "ALL_CAPS_word": pct(sum(bool(re.search(r"\b[A-Z]{3,}\b", t)) for t in titles)),
        # separators: hyphen, pipe, colon, en dash (\u2013) or em dash (\u2014) between spaces, or a colon plus space
        "separator_dash_pipe_colon": pct(sum(bool(re.search("\\s[-|:\u2013\u2014]\\s|:\\s", t)) for t in titles)),
        "starts_with_how_to": pct(sum(bool(re.match(r"how to\b", t, re.I)) for t in titles)),
        "starts_with_why_what_when_who": pct(sum(bool(re.match(r"(why|what|when|who)\b", t, re.I)) for t in titles)),
    }
    first = Counter(t.split()[0].lower() for t in titles if t.split())
    res["most_common_first_word"] = first.most_common(10)
    bg = Counter()
    for t in titles:
        w = re.findall(r"[a-z']+", t.lower())
        for i in range(len(w) - 1):
            bg[w[i] + " " + w[i + 1]] += 1
    res["most_common_word_pairs"] = [x for x in bg.most_common(15)]
if metas:
    v = [m.get("views") or 0 for m in metas]
    d = [m.get("duration_sec") or 0 for m in metas if m.get("duration_sec")]
    res["views_median"] = statistics.median(v)
    res["views_max"] = max(v)
    if d:
        res["duration_min"] = {"min": round(min(d) / 60, 1), "median": round(statistics.median(d) / 60, 1), "max": round(max(d) / 60, 1)}
    top = sorted(metas, key=lambda m: -(m.get("views") or 0))[:5]
    res["top_5_by_views"] = [{"views": m.get("views"), "duration_min": round((m.get("duration_sec") or 0) / 60, 1), "title": m.get("title")} for m in top]

txt = json.dumps(res, ensure_ascii=False, indent=1)
print(txt)
if OUT:
    open(OUT, "w", encoding="utf-8").write(txt)

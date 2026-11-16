"""Measure the views-versus-age curve that hints at a channel's genre (Evergreen / Cashcow / Trend / Hype) with code.

Usage: python -I -X utf8 measure_genre_curve.py <competitor-folder> [output.json]
Reads : <competitor-folder>/videos/*/meta.json (date, views, duration), written by fetch_competitor_data.py
Measures: each video's age in days and views per day; the median views per day of the newer and older halves;
          the rank correlation between age and views per day; the share of the most viewed video; upload frequency.
It does not interpret: the "rough_hints" field is a crude marker, the decision is read and made by the strongest
model together with the user.
"""
import json
import statistics
import sys
from datetime import date, datetime
from pathlib import Path


def rank_correlation(x, y):
    def ranks(v):
        order = sorted(range(len(v)), key=lambda i: v[i])
        r = [0] * len(v)
        for k, i in enumerate(order):
            r[i] = k
        return r
    rx, ry = ranks(x), ranks(y)
    n = len(x)
    if n < 4:
        return None
    d2 = sum((a - b) ** 2 for a, b in zip(rx, ry))
    return round(1 - 6 * d2 / (n * (n * n - 1)), 2)


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    root = Path(sys.argv[1])
    today = date.today()
    videos = []
    for meta in sorted((root / "videos").glob("*/meta.json")):
        j = json.loads(meta.read_text(encoding="utf-8"))
        if not j.get("date") or not j.get("views"):
            continue
        d = datetime.strptime(j["date"], "%Y%m%d").date()
        age = max(1, (today - d).days)
        videos.append({"id": j["id"], "age_days": age, "views": j["views"],
                       "views_per_day": round(j["views"] / age), "duration_sec": j.get("duration_sec")})
    if len(videos) < 4:
        sys.exit("At least 4 videos are needed (the data pack from the collection step).")
    videos.sort(key=lambda v: v["age_days"])  # newest first
    # A first-week burst inflates views per day, so the curve is measured on videos that are 7 days old or older.
    mature = [v for v in videos if v["age_days"] >= 7]
    if len(mature) < 4:
        sys.exit("At least 4 videos aged 7 days or more are needed.")
    half = len(mature) // 2
    newer, older = mature[:half], mature[-half:]
    per_day_new = statistics.median(v["views_per_day"] for v in newer)
    per_day_old = statistics.median(v["views_per_day"] for v in older)
    total = sum(v["views"] for v in videos)
    top = max(videos, key=lambda v: v["views"])
    first = max(v["age_days"] for v in videos)
    result = {
        "video_count": len(videos),
        "channel_age_days_by_oldest_video": first,
        "upload_interval_days": round(first / len(videos), 1),
        "newer_half_median_views_per_day": per_day_new,
        "older_half_median_views_per_day": per_day_old,
        "newer_to_older_ratio": round(per_day_new / per_day_old, 2) if per_day_old else None,
        "videos_used_for_curve_aged_7_days_or_more": len(mature),
        "age_vs_views_per_day_rank_correlation": rank_correlation([v["age_days"] for v in mature], [v["views_per_day"] for v in mature]),
        "top_video_share_percent": round(top["views"] / total * 100, 1),
        "top_video_age_days": top["age_days"],
        "videos": videos,
    }
    hints = []
    ratio = result["newer_to_older_ratio"]
    if ratio is not None:
        if ratio >= 1.2:
            hints.append("Newer videos get more views per day than older ones: a growing channel; fits evergreen or cashcow, does not fit trend or hype.")
        elif ratio <= 0.5:
            hints.append("Older videos do much better than newer ones: interest may be fading; fits trend or hype.")
        else:
            hints.append("Newer and older videos get similar views per day: no clear curve.")
    if result["top_video_share_percent"] > 50:
        hints.append("One video carries more than half of all views: not a true cashcow or evergreen, possibly a single hit (hype or trend).")
    result["rough_hints"] = hints
    out_path = Path(sys.argv[2]) if len(sys.argv) > 2 else None
    payload = json.dumps(result, ensure_ascii=False, indent=1)
    if out_path:
        out_path.write_text(payload, encoding="utf-8")
    print(json.dumps({k: v for k, v in result.items() if k != "videos"}, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()

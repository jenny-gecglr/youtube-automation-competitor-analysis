"""Collect a competitor channel's top-N videos automatically (the model spends no tokens on collecting).

Usage:
  python -I -X utf8 fetch_competitor_data.py <channel-url> <output-folder> [--count 15] [--least 3] [--lang en] [--name "<channel name>"]

Writes under <output-folder>:
  titles.txt               all titles by views, most viewed first
  videos/<rank>_<views>_<id>/
      meta.json            exact views, date, duration, title, link, group (most_viewed / least_viewed)
      title.txt, description.txt, description_links.txt, chapters.txt (the 0:00 lines of the description)
      transcript.txt       verbatim from NotebookLM (`nlm source content`, no model in between, no tokens spent).
                           If NotebookLM cannot deliver, the yt-dlp subtitle is used; if that fails, "unavailable"
      thumbnail.jpg        maxresdefault (hqdefault if missing)
  thumbnail_measurements.json   thumbnail values measured with Pillow
  _summary.md              table + UNAVAILABLE list (nothing is made up)
  _notebook.json           the persistent NotebookLM notebook id (the same notebook is reused on re-runs)

Requirements: yt-dlp, Pillow (pip install yt-dlp pillow), Node.js (for yt-dlp's JS runtime), and the NotebookLM CLI
`nlm` on PATH (or set the NLM_PATH environment variable to its full path).
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

NLM = os.environ.get("NLM_PATH") or shutil.which("nlm") or "nlm"
YTDLP = [sys.executable, "-m", "yt_dlp", "--js-runtimes", "node"]


def run_ytdlp(args):
    return subprocess.run(YTDLP + args, capture_output=True, text=True, encoding="utf-8")


def clean_link(link):
    link = link.split("?")[0].rstrip("/")
    link = re.sub(r"/(videos|shorts|streams|featured)$", "", link)
    return link.replace("http://", "https://") + "/videos"


def list_videos(url):
    r = run_ytdlp(["--flat-playlist", "--ignore-errors", "-J", url])
    if not r.stdout.strip():
        sys.exit("Could not list the channel: " + r.stderr[-400:])
    data = json.loads(r.stdout)
    return [e for e in (data.get("entries") or []) if e and e.get("id")]


def get_meta(vid):
    r = run_ytdlp(["--skip-download", "--ignore-errors", "-J", f"https://www.youtube.com/watch?v={vid}"])
    return json.loads(r.stdout) if r.stdout.strip() else None


def clean_vtt(path):
    lines, previous = [], ""
    for raw in Path(path).read_text(encoding="utf-8").splitlines():
        if "-->" in raw or raw.startswith(("WEBVTT", "Kind:", "Language:", "NOTE")) or not raw.strip():
            continue
        t = re.sub(r"<[^>]+>", "", raw).strip()
        if t and t != previous:
            lines.append(t)
            previous = t
    return " ".join(lines)


def get_subtitle_transcript(vid, folder, lang):
    template = str(folder / "_sub")
    run_ytdlp(["--skip-download", "--write-subs", "--write-auto-subs", "--sub-langs", f"{lang}.*,{lang}",
               "--sub-format", "vtt", "-o", template, f"https://www.youtube.com/watch?v={vid}"])
    found = sorted(folder.glob("_sub*.vtt"))
    if not found:
        return False
    (folder / "transcript.txt").write_text(clean_vtt(found[0]), encoding="utf-8")
    for f in found:
        f.unlink()
    return True


def run_nlm(args):
    return subprocess.run([NLM] + args, capture_output=True, text=True, encoding="utf-8", timeout=900)


def video_id(url):
    m = re.search(r"(?:v=|shorts/|youtu\.be/)([\w-]{11})", url or "")
    return m.group(1) if m else None


def nlm_transcripts(notebook_name, folders, record_path):
    """folders: {video_id: folder}. Opens a PERSISTENT NotebookLM notebook named after the competitor (reused from
    the record if present, never deleted), adds the videos and fetches the verbatim transcripts."""
    if record_path.exists():
        notebook = json.loads(record_path.read_text(encoding="utf-8"))["notebook_id"]
    else:
        r = run_nlm(["notebook", "create", notebook_name])
        m = re.search(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}", r.stdout + r.stderr)
        if not m:
            print("Could not open a NotebookLM notebook:", (r.stderr or r.stdout)[-200:])
            return {}
        notebook = m.group(0)
        record_path.write_text(json.dumps({"notebook_id": notebook, "name": notebook_name}), encoding="utf-8")
    before = run_nlm(["source", "list", notebook, "--json"])
    try:
        existing = {video_id(k.get("url")) for k in json.loads(before.stdout)}
    except Exception:
        existing = set()
    ids = [v for v in folders if v not in existing]  # videos already in the notebook are not added again
    for i in range(0, len(ids), 10):
        cmd = ["source", "add", notebook, "--wait", "--wait-timeout", "600"]
        for v in ids[i:i + 10]:
            cmd += ["--youtube", f"https://www.youtube.com/watch?v={v}"]
        run_nlm(cmd)
    listing = run_nlm(["source", "list", notebook, "--json"])
    try:
        sources = json.loads(listing.stdout)
    except Exception:
        return {}
    result = {}
    for k in sources:
        v = video_id(k.get("url"))
        if v in folders:
            path = folders[v] / "transcript.txt"
            c = run_nlm(["source", "content", k["id"], "-o", str(path)])
            result[v] = c.returncode == 0 and path.exists() and path.stat().st_size > 50
    print(f"NotebookLM notebook: {notebook}")
    return result


def get_thumbnail(vid, target):
    for name in ("maxresdefault", "hqdefault"):
        try:
            urllib.request.urlretrieve(f"https://i.ytimg.com/vi/{vid}/{name}.jpg", target)
            if target.stat().st_size > 5000:
                return name
        except Exception:
            pass
    return None


def measure_thumbnail(path):
    from PIL import Image, ImageStat
    im = Image.open(path).convert("RGB")
    w, h = im.size
    hsv = im.resize((64, 36)).convert("HSV")
    mean = ImageStat.Stat(hsv).mean
    palette = im.resize((96, 54)).quantize(colors=4).convert("RGB")
    colors = [f"#{r:02x}{g:02x}{b:02x}" for _, (r, g, b) in sorted(palette.getcolors(), reverse=True)]
    top = im.crop((0, 0, w, max(1, h // 12))).resize((1, 1)).getpixel((0, 0))
    return {"size": [w, h], "ratio": round(w / h, 3), "brightness": round(mean[2] / 255, 3),
            "saturation": round(mean[1] / 255, 3), "dominant_colors": colors,
            "top_strip_average_color": "#%02x%02x%02x" % top}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("channel")
    ap.add_argument("output")
    ap.add_argument("--count", type=int, default=15)
    ap.add_argument("--least", type=int, default=3)
    ap.add_argument("--lang", default="en")
    ap.add_argument("--name", default=None, help="NotebookLM notebook name = competitor channel name (persistent)")
    ap.add_argument("--yt-subtitles", action="store_true", dest="ytsub",
                    help="use the yt-dlp subtitle directly instead of NotebookLM")
    a = ap.parse_args()

    out = Path(a.output)
    (out / "videos").mkdir(parents=True, exist_ok=True)
    entries = list_videos(clean_link(a.channel))
    entries.sort(key=lambda e: e.get("view_count") or 0, reverse=True)
    (out / "titles.txt").write_text(
        "\n".join(f"{e.get('view_count') or 0}\t{e.get('title')}" for e in entries), encoding="utf-8")
    chosen = entries[:a.count]
    for e in (entries[-a.least:] if a.least else []):  # on a small channel the same video must not be picked twice
        if e not in chosen:
            chosen.append(e)

    rows, unavailable, measurements, folders, info = [], [], {}, {}, {}
    for rank, e in enumerate(chosen, 1):
        vid = e["id"]
        m = get_meta(vid)
        if not m:
            unavailable.append((vid, "metadata unavailable"))
            continue
        views = m.get("view_count") or 0
        existing = list((out / "videos").glob(f"*_{vid}"))  # a second run reuses the same folder
        folder = existing[0] if existing else out / "videos" / f"{rank:02d}_{views}_{vid}"
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "meta.json").write_text(json.dumps({
            "id": vid, "title": m.get("title"), "views": views, "date": m.get("upload_date"),
            "duration_sec": m.get("duration"), "likes": m.get("like_count"),
            "comment_count": m.get("comment_count"), "url": f"https://www.youtube.com/watch?v={vid}",
            "group": "most_viewed" if rank <= a.count else "least_viewed"}, ensure_ascii=False, indent=1), encoding="utf-8")
        (folder / "title.txt").write_text(m.get("title") or "", encoding="utf-8")
        description = m.get("description") or ""
        (folder / "description.txt").write_text(description, encoding="utf-8")
        links = "\n".join(re.findall(r"https?://\S+", description))
        chapters = "\n".join(l for l in description.splitlines() if re.match(r"\s*\(?\d{1,2}:\d{2}", l))
        if links:  # empty files are not written
            (folder / "description_links.txt").write_text(links, encoding="utf-8")
        if chapters:
            (folder / "chapters.txt").write_text(chapters, encoding="utf-8")
        folders[vid] = folder
        thumb = get_thumbnail(vid, folder / "thumbnail.jpg")
        if thumb:
            measurements[vid] = measure_thumbnail(folder / "thumbnail.jpg")
        else:
            unavailable.append((vid, "thumbnail could not be downloaded"))
        info[vid] = (rank, views, m.get("upload_date"), m.get("duration"), thumb, m.get("title"))
        time.sleep(1.5)

    status = {}
    if not a.ytsub and folders:
        status = nlm_transcripts(a.name or out.name, folders, out / "_notebook.json")
    for vid, folder in folders.items():
        if not status.get(vid):
            status[vid] = get_subtitle_transcript(vid, folder, a.lang)
        if not status[vid]:
            unavailable.append((vid, "transcript unavailable (no NotebookLM transcript, no subtitle)"))
    for vid, (rank, views, date, duration, thumb, title) in info.items():
        rows.append(f"| {rank} | {views} | {date} | {duration} | "
                    f"{'yes' if status.get(vid) else 'NO'} | {thumb or 'NO'} | {title} |")

    (out / "thumbnail_measurements.json").write_text(json.dumps(measurements, indent=1), encoding="utf-8")
    body = ["# Competitor data summary", "", "| rank | views | date | duration sec | transcript | thumbnail | title |",
            "|---|---|---|---|---|---|---|"] + rows
    body += ["", "## UNAVAILABLE (nothing is made up; a later step completes these or shows them to the user)"]
    body += [f"- {v}: {n}" for v, n in unavailable] or ["- none"]
    (out / "_summary.md").write_text("\n".join(body), encoding="utf-8")
    print(f"{len(rows)} videos processed, {len(unavailable)} gaps. Summary: {out / '_summary.md'}")


if __name__ == "__main__":
    main()

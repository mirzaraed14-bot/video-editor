"""hp-cast wrapper around yt_api.py (the one door to the YouTube Data API). Saves raw JSON under hp-cast/api/, prints compact rows.

usage (any cwd):  python -X utf8 -I yt_q.py search   <label> name=value ...   (search, then `videos` on every id it returns)
                  python -X utf8 -I yt_q.py videos   <label> id,id,...
                  python -X utf8 -I yt_q.py uploads  <label> UCid,UCid,...     (channels + playlistItems UU... + videos)
                  python -X utf8 -I yt_q.py comments <label> <videoId>
                  python -X utf8 -I yt_q.py show     <label> [regex]           (reprint saved rows, no API call)
env: MATCH=<regex> marks/keeps rows whose title+description match; TOP=<n> rows to print (default 20).
"""
import json
import os
import re
import subprocess
import sys

ROOT = r"X:\Claude Projects\video-editor-client\video-editor"
API = os.path.join(ROOT, "research", "deep-research-2026-11-14", "yt_api.py")
OUT = os.path.join(ROOT, "research", "deep-research-2026-11-14", "hp-cast", "api")
os.makedirs(OUT, exist_ok=True)
TOP = int(os.environ.get("TOP", "20"))
MATCH = os.environ.get("MATCH", "")


def call(endpoint, params):
    r = subprocess.run(["python", "-I", API, "hp-cast", endpoint] + params, cwd=ROOT,
                       capture_output=True, text=True, encoding="utf-8")
    sys.stderr.write(r.stderr)
    if r.returncode != 0:
        sys.exit(r.returncode)
    return json.loads(r.stdout)


def secs(s):
    m = re.match(r"P(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", s or "")
    if not m:
        return 0
    d, h, mi, se = (int(x or 0) for x in m.groups())
    return d * 86400 + h * 3600 + mi * 60 + se


def videos(ids):
    items = []
    for i in range(0, len(ids), 50):
        items += call("videos", ["part=snippet,statistics,contentDetails", "id=" + ",".join(ids[i:i + 50])]).get("items", [])
    return items


def row(v):
    s, st, cd = v["snippet"], v.get("statistics", {}), v.get("contentDetails", {})
    return {"id": v["id"], "views": int(st.get("viewCount", 0) or 0), "likes": int(st.get("likeCount", 0) or 0),
            "comments": int(st.get("commentCount", 0) or 0), "sec": secs(cd.get("duration")), "date": s["publishedAt"][:10],
            "ch": s.get("channelTitle", ""), "chid": s.get("channelId", ""), "title": s.get("title", ""),
            "desc": (s.get("description") or "")[:300].replace("\n", " ")}


def show(rows, regex=MATCH, top=TOP):
    rows = sorted(rows, key=lambda r: -r["views"])
    if regex:
        rx = re.compile(regex, re.I)
        hit = [r for r in rows if rx.search(r["title"] + " " + r["desc"])]
        print("  %d rows, %d match /%s/ (showing matches)" % (len(rows), len(hit), regex))
        rows = hit
    for r in rows[:top]:
        print("  %11s %8s %6s %5ss %s %s | %-24.24s | %.95s" % (format(r["views"], ","), format(r["likes"], ","),
              format(r["comments"], ","), r["sec"], r["date"], r["id"], r["ch"], r["title"]))


def save(label, kind, data):
    with open(os.path.join(OUT, "%s.%s.json" % (label, kind)), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)


mode, label = sys.argv[1], sys.argv[2]
if mode == "search":
    j = call("search", sys.argv[3:])
    save(label, "search", j)
    ids = [it["id"]["videoId"] for it in j.get("items", []) if it.get("id", {}).get("videoId")]
    rows = [row(v) for v in videos(ids)] if ids else []
    save(label, "rows", rows)
    print("%s: %d ids (totalResults est. %s)" % (label, len(ids), j.get("pageInfo", {}).get("totalResults")))
    show(rows)
elif mode == "videos":
    rows = [row(v) for v in videos(sys.argv[3].split(","))]
    save(label, "rows", rows)
    print("%s: %d rows" % (label, len(rows)))
    show(rows, regex=MATCH, top=max(TOP, len(rows)))
elif mode == "uploads":
    ch = call("channels", ["part=snippet,statistics,contentDetails", "id=" + sys.argv[3]])
    save(label, "channels", ch)
    allrows = []
    for c in ch.get("items", []):
        st = c.get("statistics", {})
        up = c["contentDetails"]["relatedPlaylists"]["uploads"]
        pl = call("playlistItems", ["part=contentDetails", "playlistId=" + up, "maxResults=50"])
        ids = [it["contentDetails"]["videoId"] for it in pl.get("items", [])]
        rows = [row(v) for v in videos(ids)] if ids else []
        allrows += rows
        dates = sorted(r["date"] for r in rows)
        print("%s | %s subs | %s videos | last %d uploads %s..%s" % (c["snippet"]["title"], format(int(st.get("subscriberCount", 0) or 0), ","),
              st.get("videoCount"), len(rows), dates[0] if dates else "-", dates[-1] if dates else "-"))
        show(rows, regex="", top=int(os.environ.get("PER", "6")))
        if MATCH:
            show(rows, regex=MATCH, top=10)
    save(label, "rows", allrows)
elif mode == "comments":
    j = call("commentThreads", ["part=snippet", "videoId=" + sys.argv[3], "maxResults=100", "order=relevance",
                                "textFormat=plainText"])
    save(label, "comments", j)
    for it in j.get("items", []):
        s = it["snippet"]["topLevelComment"]["snippet"]
        print("  %4s likes | %s | %s" % (s.get("likeCount", 0), s.get("publishedAt", "")[:10],
                                         s.get("textDisplay", "").replace("\n", " ")[:300]))
    print("%s: %d comment threads" % (label, len(j.get("items", []))))
elif mode == "show":
    with open(os.path.join(OUT, label + ".rows.json"), encoding="utf-8") as f:
        show(json.load(f), regex=sys.argv[3] if len(sys.argv) > 3 else MATCH)

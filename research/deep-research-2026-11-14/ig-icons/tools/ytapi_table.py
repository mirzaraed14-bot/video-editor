# Print a compact table from yt_api.py JSON: a search answer (ids, channel, title) joined with a videos answer (numbers).
# Usage: python -I ytapi_table.py ids <search.json>              -> prints the comma-joined video ids (for one videos call)
#        python -I ytapi_table.py table <search.json> <videos.json> [maxrows]
#        python -I ytapi_table.py vtable <videos.json> [maxrows]  -> a table from a videos answer alone (playlist pulls)
import sys, json, re

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:
        pass


def load(p):
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def secs(iso):
    m = re.match(r"P(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", iso or "")
    if not m:
        return -1
    d, h, mi, s = (int(x) if x else 0 for x in m.groups())
    return d * 86400 + h * 3600 + mi * 60 + s


def k(n):
    n = int(n)
    if n >= 1_000_000:
        return "%.2fM" % (n / 1e6)
    if n >= 1000:
        return "%.1fK" % (n / 1e3)
    return str(n)


def rows_from_videos(v):
    out = []
    for it in v.get("items", []):
        sn, st, cd = it.get("snippet", {}), it.get("statistics", {}), it.get("contentDetails", {})
        out.append({
            "id": it["id"], "ch": sn.get("channelTitle", ""), "title": sn.get("title", ""),
            "date": sn.get("publishedAt", "")[:10], "dur": secs(cd.get("duration")),
            "views": int(st.get("viewCount", 0) or 0), "likes": st.get("likeCount", "-"),
            "com": st.get("commentCount", "-"),
        })
    return out


def show(rows, maxrows):
    rows.sort(key=lambda r: -r["views"])
    for i, r in enumerate(rows[:maxrows], 1):
        likes = k(r["likes"]) if str(r["likes"]).isdigit() else "-"
        com = k(r["com"]) if str(r["com"]).isdigit() else "-"
        print("%2d %-11s %7s %6s %5s %4ss %s | %s | %s" % (i, r["id"], k(r["views"]), likes, com, r["dur"], r["date"],
                                                         r["ch"][:28], r["title"][:90]))
    total = sum(r["views"] for r in rows)
    shorts = [r for r in rows if 0 < r["dur"] <= 180]
    print("-- %d videos, %d of them <= 180 s; total views %s; Shorts' views %s" % (len(rows), len(shorts), k(total),
                                                                                 k(sum(r["views"] for r in shorts))))


mode = sys.argv[1]
if mode == "ids":
    s = load(sys.argv[2])
    ids = [it["id"]["videoId"] for it in s.get("items", []) if it.get("id", {}).get("videoId")]
    print(",".join(ids))
elif mode == "table":
    s, v = load(sys.argv[2]), load(sys.argv[3])
    maxrows = int(sys.argv[4]) if len(sys.argv) > 4 else 50
    print("search totalResults (Google's estimate):", s.get("pageInfo", {}).get("totalResults"))
    show(rows_from_videos(v), maxrows)
elif mode == "vtable":
    v = load(sys.argv[2])
    maxrows = int(sys.argv[3]) if len(sys.argv) > 3 else 50
    show(rows_from_videos(v), maxrows)
elif mode == "plids":
    p = load(sys.argv[2])
    print(",".join(it["contentDetails"]["videoId"] for it in p.get("items", [])))
    sys.stderr.write("nextPageToken=%s\n" % p.get("nextPageToken", ""))

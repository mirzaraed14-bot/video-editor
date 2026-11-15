"""peers.py: peer channels' latest 50 uploads with numbers, through the hub's yt_api.py (3 units per channel, no searches).
Usage (repo root): python -I research/deep-research-2026-11-14/hp-films/tools/peers.py UCxxx UCyyy ...
Prints per channel: name, subscribers, then the top 6 of its latest 50 uploads by views (Shorts flagged <=180 s), plus the median.
"""
import json, os, re, statistics, subprocess, sys
for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:
        pass
API = os.path.join("research", "deep-research-2026-11-14", "yt_api.py")
META = os.path.join("research", "deep-research-2026-11-14", "hp-films", "meta")

def call(endpoint, params):
    r = subprocess.run([sys.executable, "-I", API, "hp-films", endpoint] + params, capture_output=True, text=True, encoding="utf-8")
    if r.returncode != 0:
        sys.stderr.write(r.stderr[-300:]); sys.exit(r.returncode)
    return json.loads(r.stdout)

def dur(iso):
    m = re.match(r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", iso or "")
    return sum(int(x or 0) * k for x, k in zip(m.groups(), (3600, 60, 1))) if m else 0

for cid in sys.argv[1:]:
    ch = call("channels", ["part=snippet,statistics", "id=" + cid])
    it = (ch.get("items") or [{}])[0]
    name = it.get("snippet", {}).get("title", "?"); subs = it.get("statistics", {}).get("subscriberCount", "?")
    pl = call("playlistItems", ["part=contentDetails", "playlistId=UU" + cid[2:], "maxResults=50"])
    ids = [x["contentDetails"]["videoId"] for x in pl.get("items", [])]
    v = call("videos", ["part=snippet,statistics,contentDetails", "id=" + ",".join(ids)]) if ids else {"items": []}
    json.dump({"channel": ch, "videos": v}, open(os.path.join(META, f"peer_{cid}.json"), "w", encoding="utf-8"), ensure_ascii=False)
    rows = sorted(((int(x["statistics"].get("viewCount", 0)), dur(x["contentDetails"].get("duration")), x["snippet"]["publishedAt"][:10],
                    x["id"], x["snippet"]["title"][:80]) for x in v.get("items", [])), reverse=True)
    med = statistics.median([r[0] for r in rows]) if rows else 0
    print(f"## {name} ({cid}) subs={subs} latest={len(rows)} median_views={int(med)}")
    for r in rows[:6]:
        print(f"  {r[0]:>11,}  {r[1]:>4}s  {r[2]}  {r[3]}  {r[4]}")

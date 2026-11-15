"""yts.py: one hp-films search through the hub's yt_api.py (100 units), then ONE videos lookup (1 unit) for every id it returned.
Saves raw JSON to hp-films/meta/api_<tag>_{search,videos}.json and prints a compact table sorted by views.
Usage (from the repo root): python -I research/deep-research-2026-11-14/hp-films/tools/yts.py <tag> q="..." [videoDuration=short] [order=viewCount]
Never touches the key: it only calls yt_api.py, which reads the key itself.
"""
import json, os, re, subprocess, sys
for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:
        pass

ROOT = os.getcwd()
API = os.path.join("research", "deep-research-2026-11-14", "yt_api.py")
META = os.path.join("research", "deep-research-2026-11-14", "hp-films", "meta")
os.makedirs(META, exist_ok=True)

def call(endpoint, params):
    r = subprocess.run([sys.executable, "-I", API, "hp-films", endpoint] + params, capture_output=True, text=True, encoding="utf-8")
    sys.stderr.write(r.stderr[-300:])
    if r.returncode != 0:
        sys.exit(r.returncode)
    return json.loads(r.stdout)

def dur(iso):
    m = re.match(r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", iso or "")
    if not m:
        return 0
    h, mi, s = (int(x) if x else 0 for x in m.groups())
    return h * 3600 + mi * 60 + s

tag, rest = sys.argv[1], sys.argv[2:]
rows = []
if rest == ["--from-saved"]:
    s = json.load(open(os.path.join(META, f"api_{tag}_search.json"), encoding="utf-8"))
    ids = [it["id"]["videoId"] for it in s.get("items", []) if it.get("id", {}).get("videoId")]
    v = json.load(open(os.path.join(META, f"api_{tag}_videos.json"), encoding="utf-8"))
else:
    params = ["type=video", "maxResults=50"] + rest
    s = call("search", params)
    json.dump(s, open(os.path.join(META, f"api_{tag}_search.json"), "w", encoding="utf-8"), ensure_ascii=False)
    ids = [it["id"]["videoId"] for it in s.get("items", []) if it.get("id", {}).get("videoId")]
    v = call("videos", ["part=snippet,statistics,contentDetails", "id=" + ",".join(ids)]) if ids else {"items": []}
    json.dump(v, open(os.path.join(META, f"api_{tag}_videos.json"), "w", encoding="utf-8"), ensure_ascii=False)
if ids:
    for it in v.get("items", []):
        st, sn, cd = it.get("statistics", {}), it.get("snippet", {}), it.get("contentDetails", {})
        rows.append((int(st.get("viewCount", 0)), int(st.get("likeCount", 0) or 0), int(st.get("commentCount", 0) or 0),
                     dur(cd.get("duration")), sn.get("publishedAt", "")[:10], it["id"], sn.get("channelTitle", ""), sn.get("channelId", ""),
                     sn.get("title", "")))
rows.sort(reverse=True)
print(f"# {tag}: {len(ids)} results; q={[p for p in rest if p.startswith('q=')]}")
print("views\tlikes\tcomments\tsec\tdate\tid\tchannel\tchannelId\ttitle")
for r in rows:
    print("\t".join(str(x) for x in r[:8]) + "\t" + r[8][:90])

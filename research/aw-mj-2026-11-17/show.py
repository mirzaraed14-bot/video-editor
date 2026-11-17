import json, sys
sys.stdout.reconfigure(encoding="utf-8")
d = json.load(open(sys.argv[1], encoding="utf-8"))
rows = sorted(d["items"], key=lambda x: -int(x["statistics"].get("viewCount", 0)))
for v in rows:
    s = v["snippet"]; st = v["statistics"]; dur = v.get("contentDetails", {}).get("duration", "")
    print(f"{int(st.get('viewCount',0)):>10,} {s['publishedAt'][:10]} {v['id']} {dur:>7} {s['channelTitle'][:20]:20} | {s['title'][:100]}")

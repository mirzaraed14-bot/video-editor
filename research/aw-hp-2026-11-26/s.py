# s.py <tag> <q> [extra name=value ...]: one hp-short search (100 units) + one videos call (1 unit); prints a sorted table, saves meta/<tag>.json
import json,subprocess,sys,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
API=["python","-I","research/deep-research-2026-11-14/yt_api.py","hp-short"]
tag,q=sys.argv[1],sys.argv[2]; extra=sys.argv[3:]
r=subprocess.run(API+["search","part=snippet","type=video",f"q={q}","order=viewCount","maxResults=50"]+extra,capture_output=True,text=True,encoding="utf-8")
sys.stderr.write(r.stderr)
d=json.loads(r.stdout); ids=[i['id']['videoId'] for i in d.get('items',[])]
if not ids: print("no results"); sys.exit()
r2=subprocess.run(API+["videos","part=snippet,statistics,contentDetails","id="+",".join(ids)],capture_output=True,text=True,encoding="utf-8")
sys.stderr.write(r2.stderr)
v=json.loads(r2.stdout)
json.dump({"q":q,"extra":extra,"search":d,"videos":v},open(f"research/aw-hp-2026-11-26/meta/{tag}.json","w",encoding="utf-8"),ensure_ascii=False)
rows=[]
for it in v.get('items',[]):
    s=it['snippet'];st=it['statistics']
    rows.append((int(st.get('viewCount',0)),it['id'],s['publishedAt'][:10],it['contentDetails']['duration'],st.get('likeCount','-'),s['channelTitle'][:20],s['title'][:90]))
for x in sorted(rows,reverse=True)[:int(os.environ.get("N","22"))]:
    print(f"{x[0]:>11,} {x[1]} {x[2]} {x[3]:>9} L{x[4]:>8} {x[5]:<20} {x[6]}")

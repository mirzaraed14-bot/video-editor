# upstats.py <tag> <uploadsPlaylistId> [maxpages]: uploads + stats (2 units/page), saves meta/up_<tag>.json
import json,subprocess,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
API=["python","-I","research/deep-research-2026-11-14/yt_api.py","hp-short"]
tag,pid=sys.argv[1],sys.argv[2]; mp=int(sys.argv[3]) if len(sys.argv)>3 else 20
def call(*a): return json.loads(subprocess.run(API+list(a),capture_output=True,text=True,encoding="utf-8").stdout)
tok=None; rows=[]
for p in range(mp):
    d=call("playlistItems","part=snippet","playlistId="+pid,"maxResults=50",*(["pageToken="+tok] if tok else []))
    ids=[i['snippet']['resourceId']['videoId'] for i in d.get('items',[])]
    if ids:
        v=call("videos","part=snippet,statistics,contentDetails","id="+",".join(ids))
        for it in v.get('items',[]):
            s=it['snippet'];st=it['statistics']
            rows.append(dict(id=it['id'],date=s['publishedAt'][:10],dur=it['contentDetails']['duration'],views=int(st.get('viewCount',0)),likes=st.get('likeCount'),comments=st.get('commentCount'),title=s['title']))
    tok=d.get('nextPageToken')
    if not tok: break
json.dump(rows,open(f"research/aw-hp-2026-11-26/meta/up_{tag}.json","w",encoding="utf-8"),ensure_ascii=False)
print(tag,len(rows),'videos, pages',p+1)

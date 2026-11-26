# pl.py <playlistId> <regex> [maxpages]: page an uploads playlist (1 unit/page), print titles matching regex
import json,subprocess,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
pid,rx=sys.argv[1],re.compile(sys.argv[2],re.I); mp=int(sys.argv[3]) if len(sys.argv)>3 else 12
tok=None; n=0
for p in range(mp):
    a=["python","-I","research/deep-research-2026-11-14/yt_api.py","hp-short","playlistItems","part=snippet","playlistId="+pid,"maxResults=50"]+(["pageToken="+tok] if tok else [])
    d=json.loads(subprocess.run(a,capture_output=True,text=True,encoding="utf-8").stdout)
    for it in d.get('items',[]):
        s=it['snippet']; n+=1
        if rx.search(s['title']): print(s['resourceId']['videoId'],s['publishedAt'][:10],s['title'][:100])
    tok=d.get('nextPageToken')
    if not tok: break
print('scanned',n,'pages',p+1)

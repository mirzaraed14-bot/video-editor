import json,sys,glob,re,datetime
sys.stdout.reconfigure(encoding='utf-8',errors='replace')
out='research/aw-gta6-news-2026-11-19/api'
now=datetime.datetime.now(datetime.timezone.utc)
V={}
for f in glob.glob(out+'/v_*.json'):
    for it in json.load(open(f,encoding='utf-8')).get('items',[]):
        V[it['id']]=it
q={}
for f in sorted(glob.glob(out+'/s*.json')):
    n=int(re.search(r's(\d+)',f).group(1))
    for it in json.load(open(f,encoding='utf-8')).get('items',[]):
        q.setdefault(it['id'].get('videoId'),[]).append(n)
rows=[]
for vid,it in V.items():
    s=it['snippet']; st=it.get('statistics',{})
    v=int(st.get('viewCount',0)); pub=datetime.datetime.fromisoformat(s['publishedAt'].replace('Z','+00:00'))
    age=(now-pub).total_seconds()/3600
    d=it['contentDetails']['duration']
    rows.append((v/max(age,0.5),v,age,int(st.get('likeCount',0) or 0),int(st.get('commentCount',0) or 0),s['channelTitle'],s['title'],vid,d,q.get(vid)))
pat=re.compile(sys.argv[1],re.I) if len(sys.argv)>1 else None
rows.sort(reverse=True)
for r in rows:
    if pat and not pat.search(r[6]+' '+r[5]): continue
    print(f"{r[0]/1e3:7.1f}K/h {r[1]/1e6:6.2f}M age{r[2]:5.1f}h L{r[3]/1e3:6.1f}K C{r[4]:6} {r[8]:9} q{r[9]} | {r[5][:20]} | {r[6][:80]} | {r[7]}")

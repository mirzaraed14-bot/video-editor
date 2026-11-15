import json,subprocess,sys,re
sys.stdout.reconfigure(encoding='utf-8')
API=['python','-I','research/deep-research-2026-11-14/yt_api.py','ig-mj']
def call(*a):
    r=subprocess.run(API+list(a),capture_output=True,text=True,encoding='utf-8')
    if r.returncode!=0: sys.stderr.write(r.stderr); sys.exit(r.returncode)
    return json.loads(r.stdout)
out={}
for name,pl,pages in [(x.split('|')[0],x.split('|')[1],int(x.split('|')[2])) for x in sys.argv[1:]]:
    ids=[];tok=None
    for p in range(pages):
        args=['playlistItems','part=contentDetails',f'playlistId={pl}','maxResults=50']+([f'pageToken={tok}'] if tok else [])
        d=call(*args); ids+= [i['contentDetails']['videoId'] for i in d.get('items',[])]
        tok=d.get('nextPageToken')
        if not tok: break
    rows=[]
    for k in range(0,len(ids),50):
        d=call('videos','part=snippet,statistics,contentDetails','id='+','.join(ids[k:k+50]))
        for it in d.get('items',[]):
            dur=it['contentDetails'].get('duration',''); m=re.match(r'PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?',dur)
            secs=(int(m.group(1) or 0)*3600+int(m.group(2) or 0)*60+int(m.group(3) or 0)) if m else 0
            rows.append((int(it['statistics'].get('viewCount',0)),it['id'],secs,it['snippet']['publishedAt'][:10],re.sub(r'[^\x20-\x7e]','',it['snippet']['title'])[:80]))
    rows.sort(reverse=True); out[name]={'n':len(rows),'top':rows[:30]}
    print(f'== {name}: {len(rows)} uploads read')
    for r in rows[:12]: print(f"  {r[0]:>11,} {r[1]} {r[2]:>4}s {r[3]} | {r[4]}")
json.dump(out,open('research/deep-research-2026-11-14/ig-mj/api/peers_top.json','w',encoding='utf-8'),ensure_ascii=False,indent=0)

import json, subprocess, sys
sys.stdout.reconfigure(encoding='utf-8')
Y='../../deep-research-2026-11-14/yt_api.py'
def call(*args):
    out=subprocess.run(['python','-I',Y,'mj-beats',*args],capture_output=True,text=True,encoding='utf-8')
    return json.loads(out.stdout)
chan, tag, stop = sys.argv[1], sys.argv[2], sys.argv[3]
pl='UU'+chan[2:]
tok=None; hits=[]; pages=0
while True:
    args=['playlistItems','part=snippet','playlistId='+pl,'maxResults=50']
    if tok: args.append('pageToken='+tok)
    d=call(*args); pages+=1
    items=d.get('items',[])
    for it in items:
        s=it['snippet']; t=s['title']
        if (len(sys.argv)>4 and sys.argv[4]=='all' and s['publishedAt'][:10]>=stop) or ('michael' in t.lower() and ('2026' in t or 'michael (' in t.lower() or 'jaafar' in t.lower())):
            hits.append(s['resourceId']['videoId'])
    last=items[-1]['snippet']['publishedAt'][:10] if items else '0'
    tok=d.get('nextPageToken')
    if not tok or last < stop or pages>60: break
print(tag,'pages',pages,'last',last,'hits',len(hits))
stats=[]
for i in range(0,len(hits),50):
    v=call('videos','part=snippet,statistics,contentDetails','id='+','.join(hits[i:i+50]))
    stats+=v.get('items',[])
json.dump({'items':stats},open(f'api/{tag}_stats.json','w',encoding='utf-8'),ensure_ascii=False)
for v in sorted(stats,key=lambda x:-int(x['statistics'].get('viewCount',0))):
    print(f"{int(v['statistics'].get('viewCount',0)):>10,} {v['snippet']['publishedAt'][:10]} {v['id']} {v['contentDetails']['duration']:>8} | {v['snippet']['title'][:95]}")

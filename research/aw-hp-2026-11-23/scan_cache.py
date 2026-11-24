import sys
import json,glob,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
rows={}
for f in glob.glob('yt_api_cache/*.json'):
    try: d=json.load(open(f,encoding='utf-8'))
    except Exception: continue
    for it in d.get('items',[]) if isinstance(d,dict) else []:
        if it.get('kind')!='youtube#video' or 'statistics' not in it or 'snippet' not in it: continue
        s=it['snippet']; st=it['statistics']; dur=it.get('contentDetails',{}).get('duration','')
        rows[it['id']]=(int(st.get('viewCount',0)),s.get('publishedAt','')[:10],dur,s.get('channelTitle','')[:22],s.get('title',''))
pat=re.compile(sys.argv[1],re.I)
hits=sorted([(v,i)+r[1:] for i,r in rows.items() for v in [r[0]] if pat.search(r[4])],reverse=True)
print(len(rows),'videos cached;',len(hits),'hits')
for h in hits[:int(sys.argv[2]) if len(sys.argv)>2 else 40]:
    print(f"{h[0]:>11,} {h[1]} {h[2]} {h[3]:>9} {h[4]:<22} {h[5][:95]}")

import json,sys,re
sys.stdout.reconfigure(encoding='utf-8')
d=json.load(open(sys.argv[1],encoding='utf-8'))
rows=[]
for it in d.get('items',[]):
    s=it['snippet']; st=it.get('statistics',{}); dur=it.get('contentDetails',{}).get('duration','')
    m=re.match(r'PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?',dur); secs=(int(m.group(1) or 0)*3600+int(m.group(2) or 0)*60+int(m.group(3) or 0)) if m else 0
    rows.append((int(st.get('viewCount',0)), it['id'], secs, s.get('publishedAt','')[:10], s.get('channelTitle','')[:20], re.sub(r'[^\x20-\x7e]','',s.get('title',''))[:72]))
rows.sort(reverse=True)
n=int(sys.argv[2]) if len(sys.argv)>2 else 15
for r in rows[:n]: print(f"{r[0]:>10,} {r[1]} {r[2]:>4}s {r[3]} {r[4]:<20} | {r[5]}")
print('n=',len(rows))

# ct.py <json> [n]: top-level comments, likes first, one line each (timestamps kept)
import json,sys
d=json.load(open(sys.argv[1])); n=int(sys.argv[2]) if len(sys.argv)>2 else 60
rows=[]
for it in d.get('items',[]):
    s=it['snippet']['topLevelComment']['snippet']; rows.append((s.get('likeCount',0),s['textDisplay'].replace('\n',' / ')))
for l,t in sorted(rows,reverse=True)[:n]: print(l,'|',t[:260])

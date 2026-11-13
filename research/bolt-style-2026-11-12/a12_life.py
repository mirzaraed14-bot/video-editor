import json,numpy as np
from common import *
out={}
for i in ["3ESXVGflnmk","BZ-IBPeR2BA","UcpSXSGBtjc","OURS"]:
    E=json.load(open(OUT+f"data/{i}_caps_events.json"))
    BY0,BY1=(1005,1115) if i=="OURS" else (915,1000)
    nxt=[e['ev'] for e in E[1:]]+[10**9]
    ch=[(e,x) for e,x in zip(E,nxt) if x-e['ev']>=48 and e['words']>=2 and e['height']<60][:8]
    fr=[]
    for e,x in ch: fr+=[e['ev']+8,(e['ev']+x)//2,x-3]
    G=grab(i,fr,1080,1920); rows=[]
    for e,x in ch:
        ws=[]
        for f in (e['ev']+8,(e['ev']+x)//2,x-3):
            im=G.get(f)
            if im is None: ws.append(None); continue
            m=(im[BY0:BY1].min(2)>=225); ys,xs=np.where(m)
            ws.append((int(xs.min()),int(xs.max()),float(ys.mean()+BY0),int(m.sum()))) if len(xs) else ws.append(None)
        rows.append(dict(t=e['t'],f=ws))
    out[i]=rows
    for r in rows:
        w=[(a[1]-a[0]) if a else None for a in r['f']]; cy=[round(a[2],1) if a else None for a in r['f']]
        print(i,r['t'],"width start/mid/end",w,"cy",cy)
json.dump(out,open(OUT+"data/caps_life.json","w"))

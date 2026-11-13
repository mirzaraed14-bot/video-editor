import json,numpy as np
from common import *
res={}
for i in IDS:
    s=json.load(open(OUT+f"data/{i}_framestats.json")); n=len(s)
    d=np.array([x['diff'] for x in s]); h=np.array([x['hist'] for x in s])
    cuts=[]
    for k in range(1,n):
        nb=np.r_[d[max(1,k-6):k], d[k+1:k+7]]
        base=np.percentile(nb,75) if len(nb) else 0
        if d[k]>18 and d[k]>2.8*max(base,3) :
            cuts.append(k)
    # merge cuts within 2 frames (two-frame spikes) keep the first
    m=[]
    for k in cuts:
        if m and k-m[-1]<=2: continue
        m.append(k)
    res[i]=dict(n=n,cuts=m,diff_at=[round(float(d[k]),1) for k in m])
    t=np.array(m)/FPS; dur=n/FPS
    L=np.diff(np.r_[0,m,n])/FPS
    print(i,"dur",round(dur,2),"cuts",len(m),"per10s",round(len(m)/dur*10,2),"shot len med/mean/min/max",np.median(L).round(2),L.mean().round(2),L.min().round(2),L.max().round(2))
json.dump(res,open(OUT+"data/cuts_raw.json","w"))

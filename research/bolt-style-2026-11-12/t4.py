import numpy as np,json
from common import *
for i in IDS[:6]:
    g=load_gray(i); n=len(g)
    band=np.asarray(g[:,230:250,:]); mask=band>=225; cnt=mask.reshape(n,-1).sum(1)
    ev=[]
    for k in range(2,n-6):
        a,b=mask[k-1],mask[k]; uni=(a|b).sum()
        if cnt[k]>=25 and uni and ((a&b).sum()/uni<0.45 or cnt[k-1]<10):
            if ev and k-ev[-1]<9: continue
            ev.append(k)
    print(i,n/60,len(ev),"presence",(cnt>=25).mean().round(2), "gaps",np.percentile(np.diff(ev)/60,[10,50,90]).round(2))

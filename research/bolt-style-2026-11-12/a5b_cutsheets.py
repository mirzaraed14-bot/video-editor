import json,sys
from common import *
T=json.load(open(OUT+"data/transitions.json"))
for i in IDS:
    cs=T[i]; fr=[]
    for c in cs: fr+= [c['frame']-1,c['frame']]
    g=grab(i,fr,120,213)
    imgs=[];labs=[]
    # column-major: pair stacked -> build as rows of [before..] [after..]
    for c in cs:
        imgs+= [g[c['frame']-1], g[c['frame']]]; labs+=[f"{c['t']:.2f}s pre", c['kind'][:14]+" post"]
    S=tile(imgs,labs,12,120,213)   # 12 cols = 6 pairs per row
    S.save(OUT+f"{i}_cuts.jpg",quality=82); print(i,S.size)

import json,numpy as np
from common import *
for i in IDS:
    s=json.load(open(OUT+f"data/{i}_framestats.json")); d=np.array([x['diff'] for x in s]); h=np.array([x['hist'] for x in s])
    print(i,len(d),"dupfrac",round((d<0.05).mean(),3),"p50",np.median(d).round(2),"p99",np.percentile(d,99).round(1),"top",np.sort(d)[-12:].round(0))
    # dup pattern first 20
    print("   ",''.join('D' if x<0.05 else '.' for x in d[100:160]))

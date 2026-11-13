from common import *
import sys
ims=[];labs=[]
for i,t in [("3ESXVGflnmk",3.0),("zWe7WSLQ3dQ",6.0),("LvmhfahxDnY",15.5),("S1C7KVnzfDg",21.5),("OURS",5.0),("OURS",21.0)]:
    f=int(t*60); g=grab(i,[f],1080,1920)[f]
    ims.append(g[700:1250]); labs.append(f"{i} {t}")
S=tile(ims,labs,3,540,275,lab=18); S.save(CACHE+"t3.jpg",quality=88); print(S.size)

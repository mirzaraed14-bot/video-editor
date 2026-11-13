from common import *
import sys
i=sys.argv[1]; c=[int(x) for x in sys.argv[2:]]
fr=[]
for k in c: fr+=list(range(k-5,k+7))
g=grab(i,fr,135,240)
S=tile([g[f] for f in fr if f in g],[f"{f}" for f in fr if f in g],12,135,240)
S.save(CACHE+"t2.jpg",quality=85); print(S.size)

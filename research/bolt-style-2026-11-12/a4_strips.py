import sys
from common import *
i=sys.argv[1]; step=int(sys.argv[2]) if len(sys.argv)>2 else 30
n=len(load_gray(i)); fr=list(range(0,n,step)); g=grab(i,fr,108,192)
S=tile([g[f] for f in fr if f in g],[f"{f/FPS:.1f}" for f in fr if f in g],14,108,192)
S.save(CACHE+f"{i}_strip.jpg",quality=80); print(S.size)

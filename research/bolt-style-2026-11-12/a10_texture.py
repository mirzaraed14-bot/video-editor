import json,numpy as np,cv2
from common import *
res={}
for i in IDS:
    F=json.load(open(OUT+f"data/{i}_faces.json"))['rows']
    c=[(r['n'],max(r['faces'],key=lambda f:f[2]*f[3])) for r in F if r['faces']]
    c=[(n,f) for n,f in c if f[3]*2>=0.12*1920 and f[14]>0.8 and f[2]>20]
    if not c: res[i]=None; continue
    idx=np.linspace(0,len(c)-1,min(14,len(c))).astype(int); sel=[c[j] for j in idx]
    G=grab(i,[n+1 for n,_ in sel],1080,1920)
    lv=[];nz=[];hu=[];sa=[];yy=[];ed=[]
    for n,f in sel:
        im=G.get(n+1)
        if im is None: continue
        x,y,w,h=[v*2 for v in f[:4]]
        x0=int(max(0,x+w*.2));x1=int(min(1080,x+w*.8));y0=int(max(0,y+h*.2));y1=int(min(1920,y+h*.8))
        cr=im[y0:y1,x0:x1]
        if cr.size==0: continue
        gy=cv2.cvtColor(cr,cv2.COLOR_BGR2GRAY).astype(np.float32)
        lv.append(float(cv2.Laplacian(gy,cv2.CV_32F).var()))
        nz.append(float((gy-cv2.GaussianBlur(gy,(0,0),1.5)).std()))
        ycc=cv2.cvtColor(cr,cv2.COLOR_BGR2YCrCb); m=(ycc[...,1]>135)&(ycc[...,1]<175)&(ycc[...,2]>85)&(ycc[...,2]<130)
        if m.sum()>200:
            hsv=cv2.cvtColor(cr,cv2.COLOR_BGR2HSV)
            hu.append(float(np.median(hsv[...,0][m])*2)); sa.append(float(np.median(hsv[...,1][m])/255)); yy.append(float(np.median(ycc[...,0][m])))
        # eye-region edge energy
        ed.append(float(np.abs(cv2.Sobel(gy,cv2.CV_32F,1,1)).mean()))
    med=lambda a:round(float(np.median(a)),2) if a else None
    res[i]=dict(n=len(lv),lap_var=med(lv),hf_noise_std=med(nz),sobel=med(ed),skin_hue=med(hu),skin_sat=med(sa),skin_Y=med(yy))
    print(i,res[i])
json.dump(res,open(OUT+"data/texture.json","w"),indent=1)

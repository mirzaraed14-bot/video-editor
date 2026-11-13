import sys, subprocess, numpy as np, cv2, json
from common import *
i = sys.argv[1]
cmd = ["ffmpeg","-v","error","-i",path(i),"-an","-vf",f"scale={W}:{H}:flags=area","-f","rawvideo","-pix_fmt","bgr24","-"]
p = subprocess.Popen(cmd, stdout=subprocess.PIPE, bufsize=W*H*3*8)
gray=[]; stats=[]
prev=None
while True:
    b = p.stdout.read(W*H*3)
    if len(b)<W*H*3: break
    f = np.frombuffer(b,np.uint8).reshape(H,W,3)
    g = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
    gray.append(g)
    hsv = cv2.cvtColor(f, cv2.COLOR_BGR2HSV)
    mid = g[int(H*.15):int(H*.85)]
    st = dict(luma=float(g.mean()), luma_mid=float(mid.mean()), lap=float(cv2.Laplacian(mid,cv2.CV_32F).var()),
              lap_top=float(cv2.Laplacian(g[:int(H*.12)],cv2.CV_32F).var()),
              sat=float(hsv[...,1].mean()), b=float(f[...,0].mean()), gr=float(f[...,1].mean()), r=float(f[...,2].mean()))
    if prev is not None:
        d = cv2.absdiff(g,prev); st['diff']=float(d.mean()); st['diff_p90']=float(np.percentile(d,90))
        h1=cv2.calcHist([g],[0],None,[32],[0,256]); h0=cv2.calcHist([prev],[0],None,[32],[0,256])
        st['hist']=float(cv2.compareHist(h0,h1,cv2.HISTCMP_BHATTACHARYYA))
    else: st['diff']=0; st['diff_p90']=0; st['hist']=0
    prev=g; stats.append(st)
arr=np.stack(gray); np.save(CACHE+i+"_gray.npy",arr)
json.dump(stats, open(OUT+f"data/{i}_framestats.json","w"))
print(i, arr.shape)

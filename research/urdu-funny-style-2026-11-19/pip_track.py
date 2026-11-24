import sys,subprocess,numpy as np,json,statistics as st
vid,label=sys.argv[1],sys.argv[2]
FPS=5; W,H=480,270
cmd=['ffmpeg','-v','error','-i',vid,'-an','-vf',f'fps={FPS},scale={W}:{H}:flags=area,format=gray','-f','rawvideo','-']
p=subprocess.Popen(cmd,stdout=subprocess.PIPE)
out=[];n=0
while True:
    b=p.stdout.read(W*H)
    if len(b)<W*H: break
    im=np.frombuffer(b,dtype=np.uint8).reshape(H,W).astype(np.float32)
    # left edge: gradient over rows 0..80 (inside PiP at any size >=30%), cols 160..470
    gx=np.abs(np.diff(im[0:int(H*0.28),:],axis=1)).mean(axis=0)
    seg=gx[int(W*0.40):int(W*0.86)]; xi=int(np.argmax(seg))+int(W*0.40); xs=float(seg.max())
    gy=np.abs(np.diff(im[:,int(W*0.93):],axis=0)).mean(axis=1)
    seg2=gy[int(H*0.15):int(H*0.75)]; yi=int(np.argmax(seg2))+int(H*0.15); ys=float(seg2.max())
    out.append((n/FPS,xi+1,xs,yi+1,ys)); n+=1
json.dump(out,open(f'meas/{label}_pip.json','w'))
xs=np.array([o[1] for o in out]); 
print(label,'frames',len(out))

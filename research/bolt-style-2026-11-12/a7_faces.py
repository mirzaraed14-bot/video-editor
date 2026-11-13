import sys,subprocess,json,numpy as np,cv2
from common import *
i=sys.argv[1]; step=3; w,h=540,960
MODEL=ROOT+"/assets/models/face_detection_yunet_2023mar.onnx"
det=cv2.FaceDetectorYN_create(MODEL,"",(w,h),score_threshold=0.6)
cmd=["ffmpeg","-v","error","-i",path(i),"-an","-vf",f"select='not(mod(n,{step}))',scale={w}:{h}:flags=area","-fps_mode","passthrough","-f","rawvideo","-pix_fmt","bgr24","-"]
p=subprocess.Popen(cmd,stdout=subprocess.PIPE,bufsize=w*h*3*4)
out=[];k=0
while True:
    b=p.stdout.read(w*h*3)
    if len(b)<w*h*3: break
    img=np.frombuffer(b,np.uint8).reshape(h,w,3)
    _,fc=det.detect(img)
    faces=[] if fc is None else [[float(x) for x in f[:15]] for f in fc]
    out.append(dict(n=k*step,faces=faces)); k+=1
json.dump(dict(w=w,h=h,rows=out),open(OUT+f"data/{i}_faces.json","w")); print(i,k)

import os, json, subprocess, numpy as np, cv2
ROOT = r"X:/Claude Projects/video-editor-client/video-editor"
BOLT = ROOT + "/projects/bieber-walked-off-stage/research/bolt/"
OURS = ROOT + "/projects/mj-son-step-outside/outputs/Why Michael Jackson's Son Had To Step Outside.mov"
OUT = ROOT + "/research/bolt-style-2026-11-12/"
CACHE = r"C:/Users/affan/AppData/Local/Temp/claude/bd0643937bf87bde/3db01478-dbbf-4d4b-9f2f-134063b42a83/scratchpad/cache/"
os.makedirs(CACHE, exist_ok=True)
IDS = ["3ESXVGflnmk","BZ-IBPeR2BA","LvmhfahxDnY","S1C7KVnzfDg","UcpSXSGBtjc","zWe7WSLQ3dQ","OURS"]
def path(i): return OURS if i=="OURS" else BOLT+i+".mp4"
W,H = 270,480
FPS = 60.0
def load_gray(i):
    return np.load(CACHE+i+"_gray.npy", mmap_mode="r")
def frame_at(i, t, w=1080, h=1920, extra=()):
    """full-res BGR frame at time t via ffmpeg (no audio, no playback)"""
    cmd = ["ffmpeg","-v","error","-ss",f"{t:.4f}","-i",path(i),"-frames:v","1","-an",*extra,"-vf",f"scale={w}:{h}","-f","rawvideo","-pix_fmt","bgr24","-"]
    b = subprocess.run(cmd,capture_output=True).stdout
    return np.frombuffer(b,np.uint8).reshape(h,w,3).copy()

def grab(i, frames, w=270, h=480):
    """decode specific frame numbers (sorted unique) in one ffmpeg pass; returns dict n->BGR"""
    frames=sorted(set(int(f) for f in frames if f>=0))
    out={}
    for j in range(0,len(frames),30):
        chunk=frames[j:j+30]
        BS=chr(92); sel="+".join(f"eq(n,{f})" for f in chunk)
        cmd=["ffmpeg","-v","error","-i",path(i),"-an","-vf",f"select='{sel}',scale={w}:{h}:flags=area","-fps_mode","passthrough","-f","rawvideo","-pix_fmt","bgr24","-"]
        rr=subprocess.run(cmd,capture_output=True); b=rr.stdout
        if not b: print("FFERR",rr.stderr[:300])
        arr=np.frombuffer(b,np.uint8)
        k=len(arr)//(w*h*3)
        arr=arr[:k*w*h*3].reshape(k,h,w,3)
        for f,a in zip(chunk,arr): out[f]=a.copy()
    return out
from PIL import Image, ImageDraw, ImageFont
def font(sz):
    for p in ["C:/Windows/Fonts/arialbd.ttf","C:/Windows/Fonts/arial.ttf"]:
        try: return ImageFont.truetype(p,sz)
        except: pass
    return ImageFont.load_default()
def tile(imgs, labels, cols, w, h, pad=4, lab=14):
    rows=(len(imgs)+cols-1)//cols
    S=Image.new("RGB",(cols*(w+pad)+pad, rows*(h+lab+pad)+pad),(24,24,24)); d=ImageDraw.Draw(S); f=font(lab-2)
    for k,(im,lb) in enumerate(zip(imgs,labels)):
        r,c=divmod(k,cols); x=pad+c*(w+pad); y=pad+r*(h+lab+pad)
        S.paste(Image.fromarray(im[...,::-1]).resize((w,h)),(x,y+lab)); d.text((x+2,y),lb,fill=(255,255,0),font=f)
    return S

import subprocess,json,re,numpy as np
from common import *
src=OURS
r=subprocess.run(["ffmpeg","-v","info","-i",src,"-af","ebur128=peak=true","-f","null","-"],capture_output=True,text=True).stderr
tail=r[r.rfind("Summary"):]
print(tail)
raw=subprocess.run(["ffmpeg","-v","error","-i",src,"-vn","-ac","1","-ar","48000","-f","f32le","-"],capture_output=True).stdout
x=np.frombuffer(raw,np.float32); sr=48000
win=int(sr*0.01)
n=len(x)//win; rms=np.sqrt((x[:n*win].reshape(n,win)**2).mean(1)); db=20*np.log10(rms+1e-9)
print("rms10ms p10/p50/p90 dB",np.percentile(db,[10,50,90]).round(1), "min",db.min().round(1))
cuts=[round(s['t0']*60)/60 for s in json.load(open(ROOT+"/projects/mj-son-step-outside/build/timeline.json"))['shots']][1:]
# voice level: speech frames = top 40%
voice=np.percentile(db,80)
# onset detection: spectral flux in 2-8 kHz (SFX swishes) vs envelope
import numpy.fft as F
hop=int(sr*0.005); fr=2048
spec=[]
for s in range(0,len(x)-fr,hop):
    spec.append(np.abs(F.rfft(x[s:s+fr]*np.hanning(fr)))[int(2000/sr*fr):int(9000/sr*fr)].sum())
spec=np.array(spec); 
out=[]
sfx=ROOT+"/projects/mj-son-step-outside/build/sfx/"
for c in cuts:
    a=int((c-0.35)/0.005); b=int((c+0.35)/0.005)
    seg=spec[a:b]; base=np.median(spec[max(0,a-200):a]) 
    seg_db=db[int((c-0.35)*100):int((c+0.35)*100)]
    # local rms vs surrounding 1.5s
    ctx=db[max(0,int((c-1.5)*100)):int((c+1.5)*100)]
    out.append(dict(t=round(c,3),hf_peak_ratio=round(float(seg.max()/(np.median(spec)+1e-9)),1),rms_peak_db=round(float(seg_db.max()),1),ctx_p50=round(float(np.median(ctx)),1)))
for o in out: print(o)
json.dump(dict(summary=tail,rms_db_pcts=np.percentile(db,[10,50,90]).tolist(),cuts=out),open(OUT+"data/audio_ours.json","w"),indent=1)

"""silhole.py <job dir>: bounce the kept talk (plan plays excluded) and report holes > 0.30 s at -50 dB (step-3 proof)."""
import json, subprocess, re, sys, os
os.chdir(sys.argv[1] if len(sys.argv) > 1 else '.'); DB = sys.argv[2] if len(sys.argv) > 2 else '-50'
m=json.load(open('work/seqmap.json',encoding='utf-8')); p=json.load(open('plan.json',encoding='utf-8')) if os.path.exists('plan.json') else {}
pl=[(a,b) for a,b,*_ in m.get('sample_seq',[])]
gains={round(s,3):g for s,g,_ in p.get('clip_gains',[])}
segs=[]
for a,b,q in m['map']:
    e=q+b-a
    if any(q<pe-0.01 and e>ps+0.01 for ps,pe in pl): continue
    g=min(gains.items(), key=lambda kv: abs(kv[0]-q))[1] if gains else 0; segs.append((a,b,q,g))
src=p.get('obs_audio') or json.load(open('seq.json',encoding='utf-8'))['obs']
fc=";".join(f"[0:a]atrim={a:.4f}:{b:.4f},asetpts=PTS-STARTPTS,volume={g}dB[s{i}]" for i,(a,b,q,g) in enumerate(segs))+";"+"".join(f"[s{i}]" for i in range(len(segs)))+f"concat=n={len(segs)}:v=0:a=1[o]"
open('work/talk-fc.txt','w').write(fc)
r=subprocess.run(["ffmpeg","-v","error","-y","-i",src,"-/filter_complex","work/talk-fc.txt","-map","[o]","-ac","1","-ar","48000","work/talk-bounce.wav"],capture_output=True,text=True); print(r.stderr[-300:])
r=subprocess.run(["ffmpeg","-i","work/talk-bounce.wav","-af",f"silencedetect=noise={DB}dB:d=0.30","-f","null","-"],capture_output=True,text=True)
offs=[];t=0
for a,b,q,g in segs: offs.append((t,q,a,b-a)); t+=b-a
def tosq(x):
    o=[o for o in offs if o[0]<=x+1e-6][-1]; return o[1]+(x-o[0])
st=re.findall(r"silence_start: ([\d.]+)",r.stderr); en=re.findall(r"silence_end: ([\d.]+) \| silence_duration: ([\d.]+)",r.stderr)
print(len(segs),"talk segments, total",round(t,2),f"s; holes > 0.30 s at {DB} dB:")
for s_,(e_,d) in zip(st,en): print(f"  bounce {float(s_):.2f}-{float(e_):.2f} dur {d} -> sequence {tosq(float(s_)):.2f}")
if len(st)>len(en): print(" open-ended start", st[len(en):])

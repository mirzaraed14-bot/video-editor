# asr.py <video> [start end]: whisperx small (CPU int8) with word alignment; silent (ffmpeg -> wav only).
import sys,subprocess,os,json,whisperx
f=sys.argv[1]; n=os.path.splitext(os.path.basename(f))[0]
ss=float(sys.argv[2]) if len(sys.argv)>2 else 0.0; to=float(sys.argv[3]) if len(sys.argv)>3 else None
d=os.path.dirname(os.path.abspath(__file__))+"/asr"; os.makedirs(d,exist_ok=True)
tag=f"{n}" + (f"_{int(ss)}-{int(to)}" if to else "")
w=f"{d}/{tag}.wav"
cmd=["ffmpeg","-v","error","-y","-ss",str(ss)]+(["-to",str(to)] if to else [])+["-i",f,"-vn","-ac","1","-ar","16000",w]
subprocess.run(cmd,check=True)
m=whisperx.load_model("small","cpu",compute_type="int8",language="en")
a=whisperx.load_audio(w); r=m.transcribe(a,batch_size=4)
am,meta=whisperx.load_align_model(language_code="en",device="cpu")
r=whisperx.align(r["segments"],am,meta,a,"cpu")
with open(f"{d}/{tag}.txt","w") as o:
    for s in r["segments"]:
        o.write(f"{s['start']+ss:7.2f}-{s['end']+ss:7.2f} {s['text'].strip()}\n")
        ws=" ".join(f"{x['word']}@{x.get('start',-1)+ss:.2f}" for x in s.get("words",[]) if 'start' in x)
        o.write(f"        [{ws}]\n")
json.dump(r["segments"],open(f"{d}/{tag}.json","w"))
print(open(f"{d}/{tag}.txt").read())

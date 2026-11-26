# asr.py <audio> [offset_s] ...: WhisperX medium.en + wav2vec2 words -> transcript/<name>.words.json + .txt (run via asr.sh: lock.sh gpu + projects/.asr-lock)
import sys, json, os, whisperx, torch
sys.stdout.reconfigure(encoding="utf-8")
dev=os.environ.get("DEV") or ("cuda" if torch.cuda.is_available() else "cpu")
m=whisperx.load_model("medium.en",device=dev,compute_type="float16" if dev=="cuda" else "int8",language="en")
am,meta=whisperx.load_align_model(language_code="en",device=dev)
args=sys.argv[1:]
for i in range(0,len(args),2):
    f=args[i]; off=float(args[i+1]) if i+1<len(args) else 0
    a=whisperx.load_audio(f); r=m.transcribe(a,batch_size=int(os.environ.get("BS","4")),language="en")
    al=whisperx.align(r["segments"],am,meta,a,dev)
    w=[(round(x.get("start",-1)+off,2),round(x.get("end",-1)+off,2),x["word"]) for s in al["segments"] for x in s.get("words",[]) if "start" in x]
    base="research/aw-hp-2026-11-26/transcript/"+os.path.splitext(os.path.basename(f))[0]
    json.dump(w,open(base+".words.json","w"),ensure_ascii=False)
    txt="\n".join(f"[{s['start']+off:7.2f}-{s['end']+off:7.2f}] {s['text'].strip()}" for s in r["segments"])
    open(base+".txt","w",encoding="utf-8").write(txt); print("##",f); print(txt)

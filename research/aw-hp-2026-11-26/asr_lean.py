# asr_lean.py <wav> <offset>: faster-whisper medium.en, word timestamps, low memory (one file per process)
import sys, json, os
from faster_whisper import WhisperModel
sys.stdout.reconfigure(encoding="utf-8")
f,off=sys.argv[1],float(sys.argv[2])
m=WhisperModel("medium.en",device=os.environ.get("DEV","cpu"),compute_type=os.environ.get("CT","int8"),cpu_threads=4)
segs,_=m.transcribe(f,language="en",word_timestamps=True,beam_size=5,vad_filter=False)
w=[];lines=[]
for s in segs:
    lines.append(f"[{s.start+off:7.2f}-{s.end+off:7.2f}] {s.text.strip()}")
    w+= [(round(x.start+off,2),round(x.end+off,2),x.word) for x in (s.words or [])]
base="research/aw-hp-2026-11-26/transcript/"+os.path.splitext(os.path.basename(f))[0]
json.dump(w,open(base+".words.json","w"),ensure_ascii=False); open(base+".txt","w",encoding="utf-8").write("\n".join(lines)); print("\n".join(lines))

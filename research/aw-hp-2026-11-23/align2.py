import sys, json, whisperx, torch
sys.stdout.reconfigure(encoding="utf-8")
dev="cuda" if torch.cuda.is_available() else "cpu"
m=whisperx.load_model("medium.en",device=dev,compute_type="float16" if dev=="cuda" else "int8",language="en")
am,meta=whisperx.load_align_model(language_code="en",device=dev)
for f,off in [("src/4PxqJWglmH8_hsc2026_full_3800-5200.wav",2280),("src/bIOkpZKdwQw_ross2021.wav",0)]:
    a=whisperx.load_audio(f); r=m.transcribe(a,batch_size=16,language="en")
    al=whisperx.align(r["segments"],am,meta,a,dev)
    w=[(round(x.get("start",-1)+off,2),round(x.get("end",-1)+off,2),x["word"]) for s in al["segments"] for x in s.get("words",[]) if "start" in x]
    base=f.replace("src/","transcript/").replace(".wav","")
    json.dump(w,open(base+".words.json","w"),ensure_ascii=False)
    with open(base+".txt","w",encoding="utf-8") as o:
        for s in al["segments"]:
            t=s["start"]+off; o.write(f"[{int(t//60)}:{t%60:05.2f}] {s['text'].strip()}\n")
    print("done",f,len(w))

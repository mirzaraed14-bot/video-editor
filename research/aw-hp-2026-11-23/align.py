import sys, json, whisperx, torch
sys.stdout.reconfigure(encoding="utf-8")
dev="cuda" if torch.cuda.is_available() else "cpu"
m=whisperx.load_model("medium.en",device=dev,compute_type="float16" if dev=="cuda" else "int8",language="en")
am,meta=whisperx.load_align_model(language_code="en",device=dev)
for f,off in [("src/2zx_rQpE4Ow_rad2026_cringe.wav",0),("src/LcdJXjfpGmo_rad2026_rankings.wav",0),("src/garf_slice_1300.wav",1300)]:
    a=whisperx.load_audio(f); r=m.transcribe(a,batch_size=16,language="en")
    al=whisperx.align(r["segments"],am,meta,a,dev)
    w=[(round(x.get("start",-1)+off,2),round(x.get("end",-1)+off,2),x["word"]) for s in al["segments"] for x in s.get("words",[]) if "start" in x]
    json.dump(w,open(f.replace("src/","transcript/").replace(".wav",".words.json"),"w"),ensure_ascii=False)
    print("##",f); print(" ".join(f"{s:.2f}:{t}" for s,e,t in w))

"""tlsynth7.py <job dir>: write work/tl-read.json AS IF the sequence were placed from plan.json + transcript/cuts.json (A1 voice clips with Amplify + Hard Limiter -6, A2/A4 cue clips with
static Level, A3 the bed stem at static 0 dB), so  tlmix7.py "<seq>" <job> --cached  can run the A1-A6 gates BEFORE anything goes into Premiere (the real readback later overwrites the file;
the previous one is kept as work/tl-read.prev.json). The cue-to-track allocation is apply.py's rule (A2 and A4, the first free)."""
import json, math, os, shutil, subprocess, sys
job = os.path.abspath(sys.argv[1]); plan = json.load(open(os.path.join(job, "plan.json"), encoding="utf-8"))
C = json.load(open(os.path.join(job, "transcript", "cuts.json"), encoding="utf-8"))["segments"]
obs = plan.get("obs_audio") or os.path.join(job, "raw", "2026-11-09 15-35-10.v3voice.mp4")
lvl = lambda db: 10 ** ((db - 15) / 20) if db > -95 else 0.0
amp = lambda db: (db + 96) / 144
def comps(level_db, amp_db=None, hl=None):
    cv = lvl(0.0)
    c = [dict(name="Volume", props=[dict(n="", v=False, tv=False), dict(n="Level", v=lvl(level_db), tv=False)]),
         dict(name="Channel Volume", props=[dict(n="", v=False, tv=False), dict(n="Left", v=cv, tv=False), dict(n="Right", v=cv, tv=False)])]
    if amp_db is not None:
        c.append(dict(name="Amplify", props=[dict(n="", v=False, tv=False), dict(n="Left", v=amp(amp_db), tv=False), dict(n="Right", v=amp(amp_db), tv=False), dict(n="Gain", v=amp(amp_db), tv=False)]))
        c.append(dict(name="Hard Limiter", props=[dict(n="Maximum Amplitude", v=1 + hl / 100.0, tv=False)]))
    return c
cg = {round(s, 3): g for s, g, k in plan["clip_gains"]}
a1, pos = [], 0.0
for s in C:
    d = round(round((s["end"] - s["start"]) * 60) / 60, 6)
    a1.append(dict(name=os.path.basename(obs), s=round(pos, 6), e=round(pos + d, 6), i=s["start"], o=s["end"], path=obs, disabled=False, comps=comps(0.0, cg[round(pos, 3)], -6.0))); pos += d
END = round(plan["end"], 4)
def dur(p): return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p], capture_output=True, text=True).stdout.strip())
cues = sorted([(c[0], c[1], c[2] if len(c) > 2 else 0.0) for g in plan["graphics"] for c in g["cues"]])
trk = {1: [], 3: []}; busy = {1: -1e9, 3: -1e9}
for t, nm, db in cues:
    p = os.path.join(job, "sfx", nm + ".wav"); d = dur(p)
    k = next((q for q in (1, 3) if busy[q] <= t + 1e-3), min(busy, key=busy.get))
    if busy[k] > t + 1e-3:
        for c in trk[k]:
            if c["s"] < t - 0.005 < c["e"] + 1e-9 and c["e"] > t + 0.005: c["e"] = t; c["o"] = t - c["s"]
    busy[k] = t + d; trk[k].append(dict(name=nm + ".wav", s=round(t, 4), e=round(t + d, 4), i=0.0, o=d, path=p, disabled=False, comps=comps(db)))
bedp = os.path.join(job, plan["music"]["file"])
tracks = [dict(i=0, name="Audio 1", muted=False, solo=False, locked=False, fader="1.00", clips=a1), dict(i=1, name="Audio 2", muted=False, solo=False, locked=False, fader="1.00", clips=trk[1]),
          dict(i=2, name="Audio 3", muted=False, solo=False, locked=False, fader="1.00", clips=[dict(name=os.path.basename(bedp), s=0.0, e=END, i=0.0, o=END, path=bedp, disabled=False, comps=comps(plan["music"].get("bed_db", 0.0)))]),
          dict(i=3, name="Audio 4", muted=False, solo=False, locked=False, fader="1.00", clips=trk[3])]
out = os.path.join(job, "work", "tl-read.json")
if os.path.exists(out) and not os.path.exists(os.path.join(job, "work", "tl-read.prev.json")): shutil.copy(out, os.path.join(job, "work", "tl-read.prev.json"))
json.dump(dict(tracks=tracks, seq=plan["sequence"], end=END), open(out, "w"), indent=1); print("synthetic tl-read.json:", [(t["name"], len(t["clips"])) for t in tracks], "end", END)

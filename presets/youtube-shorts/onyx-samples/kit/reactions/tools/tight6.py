"""tight6.py <job> [--th -52] [--run 0.12] [--keep 0.04]: the v2 YouTube-tight pass on a reaction EDL (Affan 2026-11-02: "13 ms of silence
... just start the video", "five frames of silence ... sharpen the cuts", "I was just waiting to speak").

Reads transcript/cuts.json (polished, frame-snapped) + transcript/cuts.draft.json (kinds A/S) + raw/<clip> (10 ms RMS envelope).
For every TALK segment (kind A): the head is trimmed to the first frame louder than TH minus 30 ms, the tail to the last loud frame plus
KEEP, and every internal quiet run >= RUN s (not inside a WhisperX word) is cut down to 2*KEEP. Inserts (kind S) are untouched.
Writes %LOCALAPPDATA%/Temp/video-editor/<job>/cuts.json (all no_refine) for splice.sh RENDER=0, keeps the polished EDL as
transcript/cuts.polished.json, and prints the before/after length. The first segment starts at keep.json "first_start" if set."""
import json, os, shutil, subprocess, sys
import numpy as np
job = sys.argv[1]; a = sys.argv[2:]
opt = lambda k, d: float(a[a.index(k) + 1]) if k in a else d
TH, RUN, KEEP = opt("--th", -52.0), opt("--run", 0.12), opt("--keep", 0.04)
T = os.path.join(job, "transcript")
C = json.load(open(os.path.join(T, "cuts.json"), encoding="utf-8"))
shutil.copy(os.path.join(T, "cuts.json"), os.path.join(T, "cuts.polished.json"))
D = json.load(open(os.path.join(T, "cuts.draft.json"), encoding="utf-8"))["segments"]
K = json.load(open(os.path.join(job, "keep.json"), encoding="utf-8"))
W = json.load(open(os.path.join(T, "words.json"), encoding="utf-8"))["clips"][0]["words"]
raw = os.path.join(job, "raw", C["segments"][0]["clip"]); SR = 16000
envp = os.path.join(job, "work", "env10.npy")
if os.path.exists(envp): e = np.load(envp)
else:
    x = np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-i", raw, "-vn", "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True).stdout, np.float32).astype(float)
    h = SR // 100; n = len(x) // h; e = 20 * np.log10(np.sqrt((x[:n * h].reshape(n, h) ** 2).mean(1)) + 1e-9); np.save(envp, e)
kind = lambda s: max(D, key=lambda d: min(d["end"], s["end"]) - max(d["start"], s["start"]))["kind"]
inword = lambda t0, t1: any(w["start"] + 0.03 < t0 and t1 < w["end"] - 0.03 for w in W if w["start"] < t1 and w["end"] > t0)
out, before = [], 0.0
for k, s in enumerate(C["segments"]):
    before += s["end"] - s["start"]
    if kind(s) != "A":
        out.append(dict(s, no_refine=True)); continue
    i0, i1 = int(round(s["start"] * 100)), int(round(s["end"] * 100))
    loud = np.where(e[i0:i1] > TH)[0]
    if len(loud) == 0: print(f"  drop (silent) {s['start']:.3f}-{s['end']:.3f} {s.get('transcript','')[:40]}"); continue
    a0 = max(s["start"], s["start"] + loud[0] / 100 - 0.03); b0 = min(s["end"], s["start"] + (loud[-1] + 1) / 100 + KEEP)
    if k == 0 and K.get("first_start"): a0 = K["first_start"]
    pieces = [(a0, b0)]; q = e[int(round(a0 * 100)):int(round(b0 * 100))] <= TH; j = 0
    while j < len(q):
        if q[j]:
            m = j
            while m < len(q) and q[m]: m += 1
            r0, r1 = a0 + j / 100, a0 + m / 100
            if r1 - r0 >= RUN and j > 0 and m < len(q) and not inword(r0, r1):
                c0, c1 = round(r0 + KEEP, 3), round(r1 - KEEP + 0.01, 3)
                nxt = []
                for x0, x1 in pieces: nxt += [(x0, c0), (c1, x1)] if x0 < c0 and c1 < x1 else [(x0, x1)]
                pieces = nxt
            j = m
        else: j += 1
    for x0, x1 in pieces:
        if x1 - x0 >= 0.06: out.append(dict(s, start=round(x0, 4), end=round(x1, 4), no_refine=True))
for p, q2 in zip(out, out[1:]):
    if q2["start"] < p["end"] - 1e-6 and q2["start"] > p["start"]: raise SystemExit(f"overlap {p['start']}-{p['end']} / {q2['start']}")
after = sum(s["end"] - s["start"] for s in out)
tmp = os.path.join(os.environ.get("LOCALAPPDATA", ""), "Temp", "video-editor", os.path.basename(os.path.abspath(job)), "cuts.json")
json.dump(dict(C, segments=out), open(tmp, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print(f"tight6: {len(C['segments'])} -> {len(out)} segments, {before:.2f} -> {after:.2f} s (TH {TH}, RUN {RUN}, KEEP {KEEP}) -> {tmp}")

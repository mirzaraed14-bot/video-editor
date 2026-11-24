"""premcheck6.py <plan.json>: the import gate (main's rules, 2026-11-02), run BEFORE apply.py --overlays imports anything: every file the
overlays step will import (the caption layer, each graphic's .mov, each SFX slice, the bed) must be FINISHED (size stable over 3 s), pass
ffprobe AND a full decode to -f null (renders), carry the magic bytes of its extension (.mov/.mp4 'ftyp'|'wide'|'moov'|'mdat' at byte 4,
.wav 'RIFF'..'WAVE'), and have an ASCII-only name. Exit 1 on any failure (nothing is imported then)."""
import json, os, subprocess, sys, time
from concurrent.futures import ThreadPoolExecutor
path = sys.argv[1]; plan = json.load(open(path, encoding="utf-8")); job = os.path.dirname(os.path.abspath(path))
od = os.path.join(job, "overlays")
files = [os.path.join(od, plan.get("captions_file", "captions.mov"))] + [os.path.join(od, "mg", f"{g['id']}.mov") for g in plan["graphics"]]
names = sorted({c[1] for g in plan["graphics"] for c in g.get("cues", [])})
files += [os.path.join(job, plan.get("sfx_dir", "sfx"), f"{n}.wav") for n in names] + [os.path.join(job, plan["music"]["file"])]
sizes = {f: os.path.getsize(f) if os.path.exists(f) else -1 for f in files}
time.sleep(3)


def check(f):
    bad = []
    if not os.path.exists(f): return f, ["missing"]
    if os.path.getsize(f) != sizes[f]: bad.append("size still changing")
    try: os.path.basename(f).encode("ascii")
    except UnicodeEncodeError: bad.append("non-ASCII name")
    head = open(f, "rb").read(12); ext = os.path.splitext(f)[1].lower()
    if ext in (".mov", ".mp4") and head[4:8] not in (b"ftyp", b"wide", b"moov", b"mdat", b"free"): bad.append(f"magic {head[4:8]!r}")
    if ext == ".wav" and not (head[:4] == b"RIFF" and head[8:12] == b"WAVE"): bad.append(f"magic {head[:4]!r}/{head[8:12]!r}")
    p = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f], capture_output=True, text=True)
    if p.returncode or not p.stdout.strip(): bad.append("ffprobe: " + (p.stderr.strip()[:120] or "no duration"))
    if ext in (".mov", ".mp4"):
        d = subprocess.run(["ffmpeg", "-v", "error", "-i", f, "-f", "null", "-"], capture_output=True, text=True)
        if d.returncode or d.stderr.strip(): bad.append("decode: " + d.stderr.strip()[:160])
    return f, bad


with ThreadPoolExecutor(4) as ex:
    res = list(ex.map(check, files))
fails = [(f, b) for f, b in res if b]
for f, b in fails: print(f"  FAIL {os.path.relpath(f, job)}: {'; '.join(b)}")
print(f"premcheck6: {len(files)} files, {len(fails)} failing")
sys.exit(1 if fails else 0)

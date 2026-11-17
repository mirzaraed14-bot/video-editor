"""scout_asr.py <out_dir> <media> [<media>[@start-end]] ...: scout transcripts (faster-whisper small.en, CPU int8, 2 threads).

Speed beat-mining research, 17 Nov 2026. Machine evidence for FINDING lines only; every kept line is re-checked at build.
- Takes the machine-wide .asr-lock (a directory, mkdir = lock), the same one the abw11/Onyx jobs use, so only one ASR runs.
- Memory guard: waits until physical free >= ASR_PHYS_GB (default 3.0) and commit free >= ASR_COMMIT_GB (default 4.5);
  17 Nov: run with 8 / 8 and ONE clip per run after an mkl_malloc death at 3.0 / 4.5 (advisor, lab-notes 14 Nov rule).
- A media argument may carry a window: file.mp4@120-180 (seconds). Output: <out_dir>/<stem>[_a-b].scout.txt + .words.json.
- Skips an output that already exists, so a rerun resumes.
Silent: ffmpeg decodes to a wav file only; nothing plays.
"""
import json, os, subprocess, sys, time
PH_MIN = float(os.environ.get("ASR_PHYS_GB", "3.0")); CM_MIN = float(os.environ.get("ASR_COMMIT_GB", "4.5"))
MODEL = os.environ.get("ASR_MODEL", "small.en")

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
LOCK = r"X:/Claude Projects/video-editor-client/video-editor/projects/_onyx-batch9-2026-11/reactions/.asr-lock"
out_dir = sys.argv[1]
items = sys.argv[2:]
os.makedirs(out_dir, exist_ok=True)


def mem():
    o = subprocess.run(["powershell", "-NoProfile", "-Command",
                        "$o=Get-CimInstance Win32_OperatingSystem; '{0} {1}' -f $o.FreePhysicalMemory,$o.FreeVirtualMemory"],
                       capture_output=True, text=True).stdout.split()
    return int(o[0]) / 1048576, int(o[1]) / 1048576


jobs = []
for it in items:
    path, win = (it.rsplit("@", 1) + [None])[:2] if "@" in it else (it, None)
    stem = os.path.splitext(os.path.basename(path))[0]
    a = b = None
    if win:
        a, b = (float(x) for x in win.split("-"))
        stem += f"_{int(a)}-{int(b)}"
    if os.path.exists(os.path.join(out_dir, stem + ".scout.txt")):
        print("skip (done):", stem, flush=True)
        continue
    jobs.append((path, a, b, stem))
if not jobs:
    print("all done"); sys.exit()

# Wait for memory WITHOUT holding the lock (never block other jobs while we wait), then take the lock and re-check.
t_end = time.time() + 4 * 3600
while True:
    if time.time() > t_end:
        print("memory or lock never freed in 4 h: giving up"); sys.exit(3)
    ph, cm = mem()
    if ph < PH_MIN or cm < CM_MIN:
        print(f"wait mem: phys {ph:.1f} GB, commit {cm:.1f} GB", flush=True); time.sleep(30); continue
    try:
        os.mkdir(LOCK)
    except FileExistsError:
        print("waiting for .asr-lock", flush=True); time.sleep(15); continue
    ph, cm = mem()
    if ph >= PH_MIN and cm >= CM_MIN:
        break
    os.rmdir(LOCK)
try:
    from faster_whisper import WhisperModel
    m = WhisperModel(MODEL, device="cpu", compute_type="int8", cpu_threads=2, num_workers=1)
    for path, a, b, stem in jobs:
        wav = os.path.join(out_dir, stem + ".wav")
        cmd = ["ffmpeg", "-v", "error", "-y"]
        if a is not None:
            cmd += ["-ss", str(a), "-t", str(b - a)]
        cmd += ["-i", path, "-vn", "-ac", "1", "-ar", "16000", wav]
        subprocess.run(cmd, check=True)
        off = a or 0.0
        segs, _ = m.transcribe(wav, language="en", beam_size=5, word_timestamps=True, condition_on_previous_text=False,
                               vad_filter=False)
        lines, words = [], []
        for s in segs:
            t = off + s.start
            lines.append(f"[{int(t // 3600)}:{int(t % 3600 // 60):02d}:{t % 60:04.1f}] {s.text.strip()}")
            words += [[round(off + w.start, 2), round(off + w.end, 2), w.word] for w in (s.words or [])]
        open(os.path.join(out_dir, stem + ".scout.txt"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
        json.dump(words, open(os.path.join(out_dir, stem + ".words.json"), "w", encoding="utf-8"))
        os.remove(wav)
        print("done", stem, len(lines), "lines", flush=True)
finally:
    os.rmdir(LOCK)

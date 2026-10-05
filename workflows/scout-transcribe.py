"""scout-transcribe.py: fast SCOUTING transcripts of candidate podcast sections (no word alignment), to find moments.

Runs inside the rough-cut WhisperX venv (the same large-v3 model as transcribe.sh):
  "$HOME/.cache/video-editor/whisperx-venv/Scripts/python.exe" workflows/scout-transcribe.py <audio...> [--out-dir DIR]

Each input is a section of a longer episode; when its name ends in `_<start>-<end>` (seconds or mm:ss / h:mm:ss with ':' or
'.' separators, as the Onyx research step names them), segment times are shifted to EPISODE time. Writes, per input,
`<name>.scout.txt` (one `[h:mm:ss] text` line per segment) and `<name>.scout.json` (segments with episode-time start/end).
The final cut still runs the real transcribe.sh (word-aligned) on the chosen section.
"""
import argparse, json, os, re, sys

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:
        pass


def parse_offset(name):
    m = re.search(r"_([0-9.:\-]+?)-([0-9.:\-]+)$", name)
    if not m:
        return 0.0
    tok = m.group(1).replace("-", ":")
    parts = [p for p in re.split(r"[:.]", tok) if p != ""]
    try:
        nums = [float(p) for p in parts]
    except ValueError:
        return 0.0
    if len(nums) == 1:
        return nums[0]
    t = 0.0
    for v in nums[-3:]:
        t = t * 60 + v
    return t


def hms(t):
    t = int(round(t))
    return f"{t // 3600}:{t % 3600 // 60:02d}:{t % 60:02d}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("audio", nargs="+")
    ap.add_argument("--out-dir", default=None)
    ap.add_argument("--model", default="large-v3")
    ap.add_argument("--relative", action="store_true", help="keep times relative to each file (no offset from its name)")
    a = ap.parse_args()
    import torch, whisperx
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = whisperx.load_model(a.model, device=device, compute_type="float16" if device == "cuda" else "int8", language="en")
    for path in a.audio:
        stem = os.path.splitext(os.path.basename(path))[0]
        off = 0.0 if a.relative else parse_offset(stem)
        out_dir = a.out_dir or os.path.dirname(os.path.abspath(path))
        os.makedirs(out_dir, exist_ok=True)
        audio = whisperx.load_audio(path)
        res = model.transcribe(audio, batch_size=16, language="en")
        segs = [dict(start=round(s["start"] + off, 2), end=round(s["end"] + off, 2), text=s["text"].strip()) for s in res["segments"]]
        json.dump(dict(source=os.path.abspath(path), offset=off, segments=segs), open(os.path.join(out_dir, stem + ".scout.json"), "w", encoding="utf-8"), indent=1)
        with open(os.path.join(out_dir, stem + ".scout.txt"), "w", encoding="utf-8") as f:
            for s in segs:
                f.write(f"[{hms(s['start'])}] {s['text']}\n")
        print(f"✓ {stem}: {len(segs)} segments, offset {hms(off)} ({device})", flush=True)


if __name__ == "__main__":
    main()

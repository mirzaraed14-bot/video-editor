#!/usr/bin/env python3
"""topaz-iris.py: run Affan's Topaz Video AI 5 recipe on a clip from the command line (Topaz's own ffmpeg, no GUI).

The recipe is copied from his own exports (Topaz Video AI logs, 2026-10-02 and 2026-10-04; the "Iris Preset" in
C:/ProgramData/Topaz Labs LLC/Topaz Video AI/presets), as he set it in the app on 2026-10-05:
  Stabilization  full-frame, strength 50, rolling-shutter correction  -> tvai_cpe (pass 1) + tvai_stb ref-2 smoothness=6 full=1
  Frame interp.  Chronos, no slow motion, replace duplicate frames, sensitivity 10  -> tvai_fi chr-2 slowmo=1 rdt=0.01
  Enhancement    Iris (iris-3), manual: fix compression 84, improve detail 73, sharpen 42, reduce noise 14, dehalo 20,
                 anti-alias/deblur 14, focus fix Strong  -> scale to 1/4, tvai_up iris-3 x4 with compression=0.84 details=0.73
                 blur=0.42 noise=0.14 halo=0.2 preblur=0.14

  python workflows/topaz-iris.py IN.mp4 OUT.mov                       # his recipe, output = input size (focus fix Strong)
  python workflows/topaz-iris.py IN.mp4 OUT.mov --out-scale 2         # same Iris values, output 2x the input (focus fix 1/2)
  python workflows/topaz-iris.py IN.mp4 OUT.mov --segments 0,86,113   # process each continuous take separately (frame
                                                                      #   indices where a new take starts) so the stabiliser
                                                                      #   and the duplicate-frame interpolation never cross a cut
  --no-stab / --no-fi   switch those stages off (e.g. a static tripod shot, or cartoons)
  --reduce N            the stabiliser's "Reduce jittery motions" with N passes (tvai_stb reduce=N; default 0 = his
                        original recipe). Affan 2026-10-31 (Patrick Stewart Tella): "jittery motion, number of passes two"
                        after feeling jitter on the Kane short; his own 2026-10-10 export log carries reduce=2. Never 3+
                        (AW LESSONS 2026-10-20: the lips slow down and the captions can't keep up).
  --no-enhance          no Iris: only the frame interpolation (duplicate frames replaced) and/or stabilisation, output = input
                        size (a native-4K source Iris does not improve; Affan 2026-10-06: "if the quality difference isn't there
                        don't enhance but apply interpolation"). A take that comes back with a different frame count is redone
                        without interpolation, so the timeline never shifts.

Output: ProRes 422 HQ, same frame rate and frame count as the input, BT.709 tagged. Needs a signed-in Topaz Video AI install.
"""
import argparse, json, os, shutil, subprocess, sys, tempfile

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:
        pass

TOPAZ_DIR = r"C:\Program Files\Topaz Labs LLC\Topaz Video AI"
TFFMPEG = os.path.join(TOPAZ_DIR, "ffmpeg.exe")
MODELS = r"C:\ProgramData\Topaz Labs LLC\Topaz Video AI\models"
IRIS = "tvai_up=model=iris-3:scale=4:preblur=0.14:noise=0.14:details=0.73:halo=0.2:blur=0.42:compression=0.84:device=0:vram=1:instances=1"
FI = "tvai_fi=model=chr-2:slowmo=1:rdt=0.01:device=0:vram=1:instances=1"
STB = "tvai_stb=model=ref-2:filename={cpe}:smoothness=6:rst=0:wst=0:cache=128:dof=1111:ws=32:full=1:roll=0:reduce=0:device=0:vram=1:instances=1"
CPE = "tvai_cpe=model=cpe-1:filename={cpe}:device=0"
SWS = ["-sws_flags", "spline+accurate_rnd+full_chroma_int"]


def esc(path):
    """A filesystem path as an ffmpeg filter option value (forward slashes, escaped drive colon)."""
    p = path.replace("\\", "/")
    return p.replace(":", "\\\\:")


def probe(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-count_frames", "-show_entries",
                          "stream=width,height,r_frame_rate,nb_read_frames", "-of", "json", path], capture_output=True, text=True).stdout
    s = json.loads(out)["streams"][0]
    return int(s["width"]), int(s["height"]), s["r_frame_rate"], int(s["nb_read_frames"])


def run(cmd, env):
    p = subprocess.run(cmd, env=env, capture_output=True, text=True)
    if p.returncode:
        sys.exit("topaz-iris: ffmpeg failed:\n" + p.stderr[-3000:])


def enhance(src, dst, out_scale, stab, fi, env, tmp, iris=True, mult=1, reduce=0):
    w, h, fps, n = probe(src)
    num, den = (int(x) for x in (fps.split("/") + ["1"])[:2]); fps_out = f"{num * mult}/{den}"   # --fps-mult: Chronos makes the new frames
    down_w = int(round(w * out_scale / 4 / 2)) * 2        # Iris runs x4: pre-scale so the output is out_scale x the input
    chain = []
    if stab:
        cpe = os.path.join(tmp, f"cpe-{os.getpid()}-{abs(hash(src)) % 10**8}.json")
        run([TFFMPEG, "-hide_banner", "-nostdin", "-y", "-nostats", "-i", src, *SWS, "-filter_complex",
             CPE.format(cpe=esc(cpe)), "-f", "null", "-"], env)
        chain.append(STB.format(cpe=esc(cpe)).replace(":reduce=0:", f":reduce={reduce}:"))
    if fi:
        chain.append(FI if mult == 1 else FI.replace("rdt=0.01:", f"rdt=0.01:fps={num * mult / den:g}:"))
    chain += ([f"scale={down_w}:-2", IRIS] if iris else []) + ["scale=out_color_matrix=bt709"]
    if fi and mult > 1:
        chain.append("tpad=stop_mode=clone:stop=1")   # Chronos at N x returns N*n - 1 frames (nothing after the last): repeat the last one
    run([TFFMPEG, "-hide_banner", "-nostdin", "-y", "-nostats", "-i", src, *SWS, "-filter_complex", ",".join(chain),
         "-an", "-c:v", "prores_ks", "-profile:v", "3", "-pix_fmt", "yuv422p10le", "-color_primaries", "bt709",
         "-color_trc", "bt709", "-colorspace", "bt709", "-r", fps_out, "-frames:v", str(n * mult), dst], env)   # Topaz appends a duplicate last frame
    ow, oh, _, on = probe(dst)
    return (w, h, n), (ow, oh, on)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src"); ap.add_argument("dst")
    ap.add_argument("--out-scale", type=float, default=1.0)
    ap.add_argument("--segments", default="")
    ap.add_argument("--no-stab", action="store_true"); ap.add_argument("--no-fi", action="store_true")
    ap.add_argument("--fps-mult", type=int, default=1)     # 2 = double the frame rate with Chronos (30 -> 60), per take so it never blends across a cut
    ap.add_argument("--reduce", type=int, default=0)          # stabiliser jitter passes (his 2026-10-31 setting: 2)
    ap.add_argument("--no-enhance", action="store_true")      # frame interpolation (and/or stabilisation) only: no Iris, output = input size
    a = ap.parse_args()
    if not os.path.exists(TFFMPEG):
        sys.exit(f"topaz-iris: Topaz Video AI's ffmpeg not found at {TFFMPEG}")
    env = dict(os.environ, TVAI_MODEL_DATA_DIR=MODELS, TVAI_MODEL_DIR=MODELS)
    tmp = tempfile.mkdtemp(prefix="tvai-")                       # %LOCALAPPDATA%/Temp: a path without spaces
    try:
        w, h, fps, n = probe(a.src)
        cuts = sorted({0, *[int(x) for x in a.segments.split(",") if x.strip()]})
        cuts = [c for c in cuts if c < n] + [n]
        parts = []
        for i, (s, e) in enumerate(zip(cuts, cuts[1:])):
            seg = os.path.join(tmp, f"seg{i:02d}.mov")
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", a.src, "-vf", f"select='between(n\\,{s}\\,{e - 1})',setpts=N/FRAME_RATE/TB",
                            "-an", "-c:v", "ffv1", "-r", fps, seg], check=True)
            out = os.path.join(tmp, f"up{i:02d}.mov")
            M = a.fps_mult
            (iw, ih, inn), (ow, oh, on) = enhance(seg, out, a.out_scale, not a.no_stab, not a.no_fi, env, tmp, iris=not a.no_enhance, mult=M,
                                                  reduce=a.reduce)
            flag = "" if on == inn * M else f"  ⚠ frame count {inn} -> {on}"
            if on != inn * M and not a.no_fi:      # Chronos can return a static take short (Harbinger lost 8 frames): redo it without FI
                (iw, ih, inn), (ow, oh, on) = enhance(seg, out, a.out_scale, not a.no_stab, False, env, tmp, iris=not a.no_enhance,
                                                      reduce=a.reduce)
                if M > 1:                         # ... and repeat each frame M times so the timeline still matches
                    dup = out.replace(".mov", "-dup.mov"); num, den = (int(x) for x in (probe(out)[2].split("/") + ["1"])[:2])
                    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", out, "-vf", f"fps={num * M}/{den}", "-c:v", "prores_ks", "-profile:v", "3",
                                    "-pix_fmt", "yuv422p10le", "-frames:v", str(inn * M), dup], check=True); shutil.move(dup, out); on = probe(out)[3]
                flag += f" -> redone WITHOUT frame interpolation: {on} frames"
            print(f"  take {i + 1}: frames {s}-{e - 1} ({inn} f) {iw}x{ih} -> {ow}x{oh}{flag}")
            parts.append(out)
        if len(parts) == 1:
            shutil.move(parts[0], a.dst)
        else:
            lst = os.path.join(tmp, "list.txt")
            open(lst, "w", encoding="utf-8").write("".join(f"file '{p.replace(os.sep, '/')}'\n" for p in parts))
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", a.dst], check=True)
        ow, oh, _, on = probe(a.dst)
        print(f"✓ {a.dst}: {ow}x{oh}, {on} frames (input {n} x {a.fps_mult})" + ("" if on == n * a.fps_mult else "  ⚠ FRAME COUNT CHANGED"))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()

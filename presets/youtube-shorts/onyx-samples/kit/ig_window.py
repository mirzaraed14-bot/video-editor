# /// script
# requires-python = ">=3.10"
# dependencies = ["opencv-python-headless", "numpy", "pillow"]
# ///
"""ig_window.py: the v2 look's PICTURE pass ("look": "v2"): the speaker in a rounded window on pure black (batch 2, 2026-10-12).

  uv run presets/youtube-shorts/onyx-samples/kit/ig_window.py projects/<job>

Affan, 2026-10-12: "big black bars, because Instagram prefers that cinematic look… it should look like an expensive video". The
numbers are the research's (references/batch2-style-research.md § b moves 1, 13, 14, 17; § d), measured on the references' frames.

1. WINDOW. The shared picture engine (onyx-samples-youtube/kit/yt_picture.py) renders every shot at the WINDOW's size: its
   module-level W, H are set to frame.w x frame.h before its main() runs, so every shot kind (A face-tracked, B-roll, FIT, SPLIT),
   push-in, freeze, hold_in and paint-out works unchanged, just framed for a 1044 x 900 picture instead of a 9:16 crop. It reads a
   derived spec, ig/work/window/spec.json (the v2 grade defaults under the job's own grade, the split seam in window px) and writes
   ig/work/window/work/picture.mp4. The engine itself is not edited: the YouTube look's jobs keep using it as they are.
2. FINISH, per frame, inside the window only (the bars stay pure #000, measured 0 on the Stealth Motion reference):
   rack   [{"t0", "t1", "blur", "dim", "fade"}]: a pre-blurred, pre-darkened copy of the picture crossfaded in (the CLAUDE.md craft
          rule: type over a scene racks the scene out, never a filter tween). Cards with "rack": true (titlecard by default) add one.
   mood   [{"t0", "t1", "tint": [r, g, b], "a": 0.25, "fade": 0.2}]: the speaker goes black-and-white, tinted toward the accent (DOAC's
          mood shift for the darkest line, move 14).
   leak   cards {"kind": "leak", "t": s}: a warm light leak, SCREEN-blended, 0 -> 0.9 -> 0 over 0.35 s peaking on t (Mark Brazil, move
          13). Only where the camera, source or scene changes (README rule 5): it replaces a whip, never decorates a same-camera cut.
   vignette {"a": 0.22, "r": 0.6}: darkening up to `a` at the corners, feathered from r x the half-diagonal.
   grain  {"a": 0.03}: monochrome gaussian grain: a plate of sigma 64 code values at opacity a (0.03 -> sigma 1.9), seeded by the
          frame index (a re-render is identical). Measured on the demo: sigma 3.8 read as visible noise and tripled the file (33 MB vs
          7 MB per 10 s of window at CRF 16); 1.9 is "grain you can barely see" (research move 17) at ~2x the grain-free size.
   Then the rounded mask (anti-aliased, radius 64) onto a black 1080 x 1920 frame -> ig/work/picture.mp4, the same contract ig_build
   composites for the v1 look; stills of every shot's middle frame go to ig/work/stills/.
Spec keys (all optional): "frame": {x, y, w, h, radius, vignette, grain} (ig_type.FRAME), "grade" (yt_picture's keys; v2 defaults
contrast 1.12, sat 0.88, warm 0.025, black 0.015), "split": {"seam": px INSIDE the window (default h / 2), ...}, "rack", "mood".
"""
import json, math, os, subprocess, sys
import cv2, numpy as np
from PIL import Image

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:
        pass

KIT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(KIT, "..", "..", "..", ".."))
YTKIT = os.path.join(REPO, "presets", "youtube-shorts", "onyx-samples-youtube", "kit")
sys.path.insert(0, KIT)
sys.path.insert(0, YTKIT)
import ig_type                                   # noqa: E402  (the window's numbers live there, shared with ig_capy and ig_v2)
import yt_picture as yp                          # noqa: E402

W, H = 1080, 1920
# research § b move 17: "contrast 1.10-1.14, saturation 0.85-0.90, slightly lifted shadows (black 0.015), warm highlights (0.02-0.03)"
V2_GRADE = {"contrast": 1.12, "sat": 0.88, "warm": 0.025, "black": 0.015}
V2_FINISH = {"vignette": {"a": 0.22, "r": 0.6}, "grain": {"a": 0.03}}
RACK_KINDS = {"titlecard"}                       # these cards rack the window out unless they say "rack": false


def smooth(p):
    p = min(max(p, 0.0), 1.0)
    return p * p * (3 - 2 * p)


def window_weight(t, t0, t1, fade):
    """0 outside [t0, t1], 1 inside, smoothstep ramps of `fade` s at both ends (the ramps sit INSIDE the interval)."""
    if t <= t0 or t >= t1:
        return 0.0
    return min(smooth((t - t0) / fade) if fade > 0 else 1.0, smooth((t1 - t) / fade) if fade > 0 else 1.0)


def rounded_alpha(w, h, r):
    """An anti-aliased rounded-rectangle alpha (float 0..1): the signed distance to the rounded box, 1 px of feather."""
    ys, xs = np.mgrid[0:h, 0:w].astype(np.float32) + 0.5
    qx = np.abs(xs - w / 2) - (w / 2 - r); qy = np.abs(ys - h / 2) - (h / 2 - r)
    d = np.hypot(np.maximum(qx, 0), np.maximum(qy, 0)) + np.minimum(np.maximum(qx, qy), 0) - r
    return np.clip(0.5 - d, 0, 1)[..., None]


def vignette_map(w, h, a, r):
    ys, xs = np.mgrid[0:h, 0:w].astype(np.float32)
    d = np.hypot((xs - (w - 1) / 2) / ((w - 1) / 2), (ys - (h - 1) / 2) / ((h - 1) / 2)) / math.sqrt(2)   # 0 centre .. 1 corner
    u = np.clip((d - r) / max(1 - r, 1e-3), 0, 1)
    return (1 - a * u * u * (3 - 2 * u))[..., None]


def leak_layer(w, h, side):
    """A warm overexposure: white at the hot spot, amber around it, gone by ~0.9 of the window (screen blend, so blacks stay)."""
    ys, xs = np.mgrid[0:h, 0:w].astype(np.float32)
    cx, cy = {"right": (w * 1.02, h * 0.30), "left": (-w * 0.02, h * 0.30), "top": (w * 0.5, -h * 0.05)}.get(side, (w * 1.02, h * 0.3))
    d = np.hypot(xs - cx, ys - cy) / math.hypot(w, h)
    core = np.clip(1 - d / 0.32, 0, 1) ** 1.6
    glow = np.clip(1 - d / 0.85, 0, 1) ** 2.2
    white, amber = np.array([1.0, 0.97, 0.90], np.float32), np.array([1.0, 0.55, 0.18], np.float32)
    return np.clip(core[..., None] * white + glow[..., None] * amber * 0.85, 0, 1)


def main():
    job = os.path.abspath(sys.argv[1])
    spec = json.load(open(os.path.join(job, "ig", "spec.json"), encoding="utf-8"))
    fps, n = spec["fps"], spec["frames"]
    FR = ig_type.frame(spec)
    fin = {**V2_FINISH, **{k: v for k, v in spec.get("frame", {}).items() if k in V2_FINISH}}
    fw, fh = FR["w"], FR["h"]

    # ---- 1. the shots, rendered at window size by the shared engine (its own spec copy, so the job's spec stays as written)
    wdir = os.path.join(job, "ig", "work", "window")
    os.makedirs(wdir, exist_ok=True)
    # only the keys the engine reads: a card, caption or sound change then leaves the derived spec as it was, and the (slow, 4K) window
    # render is reused; the finish below always re-runs. `--force` re-renders anyway.
    wspec = {k: v for k, v in json.loads(json.dumps(spec)).items()
             if k not in ("cards", "captions", "hook", "credit", "credit_t0", "credit_y", "audio", "rack", "mood", "look", "frame")}
    G = spec.get("grade", {})
    wspec["grade"] = {fam: {**V2_GRADE, **G.get(fam, {})} for fam in ("A", "B")}
    wspec["split"] = {"seam": fh // 2, **spec.get("split", {})}
    wspec.setdefault("broll_dir", "ig/assets/broll")        # the engine's default is relative to its --dir, which is now work/window
    wpath, src = os.path.join(wdir, "spec.json"), os.path.join(wdir, "work", "picture.mp4")
    new = json.dumps(dict(wspec, _window=[fw, fh]), indent=1, ensure_ascii=False)
    old = open(wpath, encoding="utf-8").read() if os.path.exists(wpath) else ""
    if new == old and os.path.exists(src) and "--force" not in sys.argv:
        print("ig_window: the shots are unchanged, reusing the window render", src)
    else:
        open(wpath, "w", encoding="utf-8").write(new)
        yp.W, yp.H = fw, fh
        argv = sys.argv
        sys.argv = [yp.__file__, job, "--dir", os.path.join("ig", "work", "window")]
        yp.main()
        sys.argv = argv

    # ---- 2. the finish and the letterbox
    racks = [dict(r) for r in spec.get("rack", [])]
    for k in spec.get("cards", []):
        if k.get("rack", k["kind"] in RACK_KINDS) and k["kind"] != "leak":
            racks.append(dict(t0=k["t0"], t1=k["t1"], blur=k.get("rack_blur", 16), dim=k.get("rack_dim", 0.42), fade=0.22))
    moods = spec.get("mood", [])
    leaks = [(k["t"], leak_layer(fw, fh, k.get("side", "right"))) for k in spec.get("cards", []) if k["kind"] == "leak"]
    vg = vignette_map(fw, fh, fin["vignette"]["a"], fin["vignette"]["r"]) if fin.get("vignette") else None
    sigma = fin["grain"]["a"] * 64 if fin.get("grain") else 0.0
    alpha = rounded_alpha(fw, fh, FR["radius"])
    x0, y0 = FR["x"], FR["y"]
    dec = subprocess.Popen(["ffmpeg", "-v", "error", "-i", src, "-vf", "scale=in_color_matrix=bt709:in_range=tv:out_range=full", "-f", "rawvideo",
                            "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE)
    out_path = os.path.join(job, "ig", "work", "picture.mp4")
    enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(fps), "-i", "-",
                            "-vf", "scale=out_color_matrix=bt709:out_range=tv,setparams=color_primaries=bt709:color_trc=bt709:colorspace=bt709",
                            "-c:v", "libx264", "-crf", "12", "-preset", "slow", "-pix_fmt", "yuv420p", out_path], stdin=subprocess.PIPE)
    shots = spec["shots"]
    mids = {(s["f0"] + s["f1"]) // 2: s["id"] for s in shots}
    os.makedirs(os.path.join(job, "ig", "work", "stills"), exist_ok=True)
    canvas = np.zeros((H, W, 3), np.float32)
    for i in range(n):
        buf = dec.stdout.read(fw * fh * 3)
        if len(buf) < fw * fh * 3:
            sys.exit(f"ig_window: the window render ended at frame {i} of {n}")
        x = np.frombuffer(buf, np.uint8).reshape(fh, fw, 3).astype(np.float32) / 255
        t = i / fps
        for m in moods:                              # B&W + tint, crossfaded
            wgt = window_weight(t, m["t0"], m["t1"], m.get("fade", 0.2))
            if wgt > 0:
                y = (x[..., 0] * 0.2126 + x[..., 1] * 0.7152 + x[..., 2] * 0.0722)[..., None]
                tint = np.array(m.get("tint", [255, 77, 77]), np.float32) / 255
                bw = y * (1 - m.get("a", 0.25)) + y * tint * m.get("a", 0.25) * 1.6
                x = x * (1 - wgt) + np.clip(bw, 0, 1) * wgt
        for r in racks:                              # rack focus: a pre-blurred, pre-darkened clone crossfaded in
            wgt = window_weight(t, r["t0"], r["t1"], r.get("fade", 0.22))
            if wgt > 0:
                b = cv2.GaussianBlur(x, (0, 0), r.get("blur", 16)) * (1 - r.get("dim", 0.42))
                x = x * (1 - wgt) + b * wgt
        for tl, L in leaks:                          # screen blend: 1 - (1 - x)(1 - L a)
            a = 0.9 * smooth(1 - abs(t - tl) / 0.175)
            if a > 0:
                x = 1 - (1 - x) * (1 - L * a)
        if vg is not None:
            x = x * vg
        if sigma:
            g = np.random.default_rng(1009 + i).standard_normal((fh, fw), dtype=np.float32) * (sigma / 255)
            x = x + g[..., None]
        canvas[y0:y0 + fh, x0:x0 + fw] = np.clip(x, 0, 1) * alpha
        frame = (canvas * 255 + 0.5).astype(np.uint8)
        enc.stdin.write(frame.tobytes())
        if i in mids:
            Image.fromarray(frame).resize((360, 640), Image.LANCZOS).save(os.path.join(job, "ig", "work", "stills", f"{mids[i]}.jpg"), quality=88)
    dec.stdout.close(); dec.wait()
    enc.stdin.close(); enc.wait()
    print(f"ig_window: {n} frames, window {fw}x{fh} at ({x0}, {y0}) r{FR['radius']}, {len(racks)} racks, {len(leaks)} leaks, "
          f"{len(moods)} mood shifts, vignette {fin.get('vignette')}, grain {fin.get('grain')} -> {out_path}")


if __name__ == "__main__":
    main()

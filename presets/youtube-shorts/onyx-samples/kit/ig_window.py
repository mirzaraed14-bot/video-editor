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

FRAME PRESETS (batch 3, STYLE-RESEARCH § E1, 2026-10-14): "frame": "window" (default, the above) | "square" | "void", or a dict
{"preset": ..., any FRAME key, "vignette", "grain", "crush"}. ig_type.PRESETS has the numbers.
   square  980 x 980 at x 50, y 470, r 40 (Chris Williamson, measured): the same finish, a squarer window, bars 470 / 470.
   void    full-bleed 1080 x 1920, no mask and no bars: the dark set IS the letterbox (Mark Brazil). The finish adds
           crush  {"gamma": 1.25, "black": 0.04, "kinds": ["A"]}: x ** gamma sinks the mids (the research's "gamma <= 0.8" in the
                  darkening convention: x ** (1 / 0.8)), then black is pulled down by 0.04 and the rest rescaled, so a dark set reads
                  as pure black; applied on the speaker's shots only (`kinds`), B-roll keeps its own grade;
           and a 35 % vignette from 0.5 of the half-diagonal. Pick it only for a DARK set shot wide: a bright set just turns grey.
           The engine renders every shot at 1080 x 1920 (its native 9:16), so A / B / FIT / SPLIT frame exactly as in the YouTube look.

BEHIND-THE-SPEAKER TYPE (batch 3, research § E10; Chris Williamson's "WORTH DOING" half hidden by his head, 620K): once per video, the
hook or the payoff phrase in heavy caps BEHIND the speaker. "behind": [{"t0", "t1" (1.5-2.5 s), "text", "lead" (optional small line
above: the two-size stack "YOU HAVE NO" / "COURAGE"), "size": 120 (Inter Black, cap height ~87 px), "lead_size": 46, "y": window px of
the text's centre (default 0.22 x h: the head's height), "x" (default: AUTO, slid along the line until the speaker's matte hides
"hide" = 25 % of the word, so it reads as behind the head and stays readable), "color": "#FFFFFF", "shadow": 0.45}]. The
person matte is cut from the window render itself (`npx hyperframes remove-background`, u2net_human_seg on CPU, cached in
ig/work/behind/), the type is drawn with the real font (PIL), and each frame is composited picture -> soft shadow -> type -> the
speaker again through the matte, before the vignette and grain (so the grain sits over the type too). Entrance: rise 30 px +
opacity + blur 8 -> 0 in 0.45 s (power3.out); exit: a 0.25 s fade. The running captions stay on top at their anchor (they are the
overlay). Its sound and its density event come from ig_v2 (a medium whoosh cresting as it lands + a low thud).
"""
import hashlib, json, math, os, shutil, subprocess, sys
import cv2, numpy as np
from PIL import Image, ImageDraw, ImageFont

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
VOID_FINISH = {"vignette": {"a": 0.35, "r": 0.5}, "grain": {"a": 0.03}, "crush": {"gamma": 1.25, "black": 0.04, "kinds": ["A"]}}
RACK_KINDS = {"titlecard"}                       # these cards rack the window out unless they say "rack": false


def frames_of(path):
    """The frame count of a finished render (0 when the file is unreadable, e.g. a render killed before ffmpeg wrote its index)."""
    r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=nb_frames", "-of", "csv=p=0", path],
                       capture_output=True, text=True).stdout.strip()
    return int(r) if r.isdigit() else 0


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
    void = ig_type.is_void(spec)
    # the finish: the batch-2 defaults, or the void's (crush + a stronger vignette); spec.frame's own keys win (a frame given as a
    # preset name carries none, a batch-2 spec has no "frame": exactly the batch-2 finish)
    fin = {**(VOID_FINISH if void else V2_FINISH), **{k: v for k, v in ig_type.frame_spec(spec).items() if k in VOID_FINISH}}
    fw, fh = FR["w"], FR["h"]

    # ---- 1. the shots, rendered at window size by the shared engine (its own spec copy, so the job's spec stays as written)
    wdir = os.path.join(job, "ig", "work", "window")
    os.makedirs(wdir, exist_ok=True)
    # only the keys the engine reads: a card, caption or sound change then leaves the derived spec as it was, and the (slow, 4K) window
    # render is reused; the finish below always re-runs. `--force` re-renders anyway.
    wspec = {k: v for k, v in json.loads(json.dumps(spec)).items()
             if k not in ("cards", "captions", "hook", "credit", "credit_t0", "credit_y", "audio", "rack", "mood", "look", "frame", "behind")}
    G = spec.get("grade", {})
    wspec["grade"] = {fam: {**V2_GRADE, **G.get(fam, {})} for fam in ("A", "B")}
    wspec["split"] = {"seam": fh // 2, **spec.get("split", {})}
    wspec.setdefault("broll_dir", "ig/assets/broll")        # the engine's default is relative to its --dir, which is now work/window
    wpath, src = os.path.join(wdir, "spec.json"), os.path.join(wdir, "work", "picture.mp4")
    new = json.dumps(dict(wspec, _window=[fw, fh]), indent=1, ensure_ascii=False)
    old = open(wpath, encoding="utf-8").read() if os.path.exists(wpath) else ""
    if new == old and os.path.exists(src) and frames_of(src) == spec["frames"] and "--force" not in sys.argv:   # (a killed render is not reused)
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
    # the void has no window edge to round: the picture IS the frame
    alpha = None if (void and FR["radius"] == 0 and (fw, fh) == (W, H)) else rounded_alpha(fw, fh, FR["radius"])
    crush, lut = fin.get("crush"), None
    if crush:              # the void's crush as a LUT on the decoded 8-bit frame (x ** gamma, black pulled down, rest rescaled)
        g_, b_ = crush.get("gamma", 1.25), crush.get("black", 0.04)
        lut = np.clip(np.round(np.clip(((np.arange(256) / 255.0) ** g_ - b_) / (1 - b_), 0, 1) * 255), 0, 255).astype(np.uint8)
        kinds = set(crush.get("kinds", ["A"]))
        crush_f = np.zeros(n, bool)
        for s in spec["shots"]:
            if s["kind"] in kinds:
                crush_f[s["f0"]:s["f1"]] = True
    behinds = behind_layers(job, spec, src, FR, fps)
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
        u8 = np.frombuffer(buf, np.uint8).reshape(fh, fw, 3)
        if lut is not None and crush_f[i]:
            u8 = cv2.LUT(u8, lut)
        x = u8.astype(np.float32) / 255
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
        for f0b, f1b, it, col_, ta, sa, mattes in behinds:   # type BEHIND the speaker: shadow, type, then the speaker again on top
            if f0b <= i < f1b:
                t0b, t1b = it["t0"], it["t1"]
                e = 1 - (1 - min(max((t - t0b) / 0.45, 0.0), 1.0)) ** 3
                op = e * smooth(min(1.0, (t1b - t) / 0.25))
                dy, bl = int(round(30 * (1 - e))), 8 * (1 - e)
                A_, S_ = np.zeros_like(ta), np.zeros_like(sa)
                if dy:
                    A_[dy:], S_[dy:] = ta[:fh - dy], sa[:fh - dy]
                else:
                    A_, S_ = ta, sa
                if bl > 0.3:
                    A_ = cv2.GaussianBlur(A_, (0, 0), bl)
                xb = x
                x = x * (1 - (S_ * op * it.get("shadow", 0.45))[..., None])
                x = x * (1 - (A_ * op)[..., None]) + col_ * (A_ * op)[..., None]
                m_ = mattes[i - f0b].astype(np.float32)[..., None] / 255
                x = x * (1 - m_) + xb * m_
        if vg is not None:
            x = x * vg
        if sigma:
            g = np.random.default_rng(1009 + i).standard_normal((fh, fw), dtype=np.float32) * (sigma / 255)
            x = x + g[..., None]
        canvas[y0:y0 + fh, x0:x0 + fw] = np.clip(x, 0, 1) * alpha if alpha is not None else np.clip(x, 0, 1)
        frame = (canvas * 255 + 0.5).astype(np.uint8)
        enc.stdin.write(frame.tobytes())
        if i in mids:
            Image.fromarray(frame).resize((360, 640), Image.LANCZOS).save(os.path.join(job, "ig", "work", "stills", f"{mids[i]}.jpg"), quality=88)
    dec.stdout.close(); dec.wait()
    enc.stdin.close(); enc.wait()
    print(f"ig_window: {n} frames, window {fw}x{fh} at ({x0}, {y0}) r{FR['radius']}, {len(racks)} racks, {len(leaks)} leaks, "
          f"{len(moods)} mood shifts, vignette {fin.get('vignette')}, grain {fin.get('grain')}"
          + (f", crush {crush} on {int(crush_f.sum())} frames" if crush else "") + (f", {len(behinds)} behind-the-speaker" if behinds else "")
          + f" -> {out_path}")


def behind_layers(job, spec, src, FR, fps):
    """The "behind" items, ready to composite: [(f0, f1, item, colour (3,), type alpha (h, w), shadow alpha (h, w), mattes (n, h, w) uint8)].
    The person matte of frames [f0, f1) of the window render comes from `npx hyperframes remove-background` (cached by the render's
    size + mtime and the range)."""
    items = spec.get("behind", [])
    if not items:
        return []
    fw, fh = FR["w"], FR["h"]
    bdir = os.path.join(job, "ig", "work", "behind")
    os.makedirs(bdir, exist_ok=True)
    st = os.stat(src)
    fonts = os.path.join(REPO, "assets", "fonts")
    out = []
    for it in items:
        f0, f1 = int(round(it["t0"] * fps)), int(round(it["t1"] * fps))
        nfr = f1 - f0
        key = hashlib.sha1(f"{os.path.abspath(src)}|{st.st_size}|{st.st_mtime_ns}|{f0}|{f1}".encode()).hexdigest()[:12]
        raw = os.path.join(bdir, f"{key}.alpha")
        if not os.path.exists(raw) or os.path.getsize(raw) != nfr * fw * fh:
            seg, mov = os.path.join(bdir, f"{key}.seg.mp4"), os.path.join(bdir, f"{key}.seg.mov")
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src, "-vf", f"select=between(n\\,{f0}\\,{f1 - 1}),setpts=PTS-STARTPTS",
                            "-fps_mode", "passthrough", "-c:v", "libx264", "-crf", "10", "-pix_fmt", "yuv420p", seg], check=True)
            print(f"ig_window: behind-the-speaker matte, frames {f0}-{f1} (hyperframes remove-background, CPU)", flush=True)
            r = subprocess.run([shutil.which("npx") or "npx", "--yes", "hyperframes@0.8.16", "remove-background", seg, "-o", mov],
                               capture_output=True, text=True, encoding="utf-8", errors="replace")
            if r.returncode or not os.path.exists(mov):
                sys.exit(f"ig_window: remove-background failed: {(r.stderr or r.stdout)[-400:]}")
            a = subprocess.run(["ffmpeg", "-v", "error", "-i", mov, "-vf", "alphaextract,format=gray", "-f", "rawvideo", "-pix_fmt", "gray", "-"],
                               capture_output=True).stdout
            got = len(a) // (fw * fh)
            if got < nfr:                         # pad a short matte with its last frame (never a frame with no speaker in front)
                a += a[(got - 1) * fw * fh:got * fw * fh] * (nfr - got)
            open(raw, "wb").write(a[:nfr * fw * fh])
        mattes = np.fromfile(raw, np.uint8).reshape(nfr, fh, fw)
        # the type, drawn once with the real font: a big heavy-caps line (+ an optional small lead line above it)
        up = it.get("upper", True)
        text = it["text"].upper() if up else it["text"]
        size = it.get("size", 120)
        fnt = ImageFont.truetype(os.path.join(fonts, "Inter-Black.otf"), size)
        while fnt.getlength(text) > fw - 2 * it.get("margin", 50) and size > 40:
            size -= 4
            fnt = ImageFont.truetype(os.path.join(fonts, "Inter-Black.otf"), size)
        L = Image.new("L", (fw, fh), 0)
        d = ImageDraw.Draw(L)
        cy = it.get("y", fh * 0.22)
        cx = it.get("x")
        if cx is None:     # place it so the head hides about `hide` (25 %) of the word: partly behind, still readable (Chris Williamson)
            tw = fnt.getlength(text)
            band = mattes[:, max(0, int(cy - size * 0.36)):min(fh, int(cy + size * 0.36)), :].max(axis=(0, 1)) > 128
            m_ = it.get("margin", 50)
            best = None
            for c in range(int(m_ + tw / 2), int(fw - m_ - tw / 2) + 1, 4):
                hid = band[int(c - tw / 2):int(c + tw / 2)].mean() if tw else 0
                score = abs(hid - it.get("hide", 0.25))
                if best is None or score < best[0]:
                    best = (score, c, hid)
            cx = best[1] if best else fw / 2
            print(f"ig_window: behind '{text}' centred at x {cx:.0f}, y {cy:.0f} (window px): the speaker hides {best[2] * 100 if best else 0:.0f} % of it")
        d.text((cx, cy), text, font=fnt, fill=255, anchor="mm")
        if it.get("lead"):
            ls = it.get("lead_size", 46)
            lf = ImageFont.truetype(os.path.join(fonts, "Inter-Bold.otf"), ls)
            d.text((cx, cy - size * 0.40 - ls * 0.75), it["lead"].upper() if up else it["lead"], font=lf, fill=235, anchor="mm")
        ta = np.asarray(L, np.float32) / 255
        sa = cv2.GaussianBlur(ta, (0, 0), 18)
        c = it.get("color", "#FFFFFF").lstrip("#")
        col = np.array([int(c[j:j + 2], 16) / 255 for j in (0, 2, 4)], np.float32)
        out.append((f0, f1, it, col, ta, sa, mattes))
    return out


if __name__ == "__main__":
    main()

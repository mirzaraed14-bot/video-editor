# /// script
# requires-python = ">=3.10"
# dependencies = ["opencv-python-headless", "numpy"]
# ///
"""grade-picture.py: the POP grade on a YT-kit job's picture track (Affan 2026-11-05, Herjavec H1: "the footage looks very plain ... not
color graded at all ... color graded so that it looks poppy ... the footage itself looks very bland").

  uv run workflows/grade-picture.py projects/<job>                  (after yt_build.py, BEFORE sharpen-picture.py; then yt_build.py <job> <version> --skip picture,overlay)
  uv run workflows/grade-picture.py --test in.png out.png [A|DOC]   (one still, to check a look before a render)

WHY: measured on the H1 face shots, luma p5 39 / p50 118 / p95 175 / p99 193: no real black and no real white, the histogram squashed in the
middle. Reference Shorts (research/shorts-style-radar.md): p5 0-13, p95 179-237, p99 232-255. Skin stays REAL (Bolt, research/bolt-motivation-look.md: hue 16-24,
sat ~.44, Y 104-128, "no orange"), so the contrast is done on LUMA ONLY (a per-channel S-curve turned him orange: hue 28, sat .59 in the tests).

Steps on float RGB: white balance a touch cooler (the wall loses its orange, the shirt turns blue) -> a soft face-centred relight on face shots (no ring: the eyes sit at
fy_out 0.32 under head_track, so a fixed centre follows the head) -> levels + gamma + S-curve on luma, the colour following with its gain capped -> saturation, more on what is not skin ->
clarity on luma. Drawn cards (B shots whose src is mg-*.mp4) are untouched; captions and the overlay are composited later, so they are never graded.
Works on the picture the next composite reads (yt/work/picture.whip60.mov when fps_out is 60, else picture.whip.mp4). The untouched picture is kept once as *.ungraded.*
and every run grades from it, so re-running never stacks, also after sharpen-picture.py ran.
"""
import json, os, shutil, subprocess, sys
import cv2, numpy as np

LOOK = {  # A = a face shot, DOC = a receipt (a still or a clip on its blurred plate)
    "A": dict(gain=(0.975, 1.0, 1.04), relight=0.42, bp=0.055, wp=0.83, gamma=1.30, s=0.42, cap=1.14, sat=1.42, skin_sat=1.20, mid=(14.0, 0.20), fine=(1.6, 0.25)),
    "DOC": dict(gain=(1.0, 1.0, 1.0), relight=0.0, bp=0.02, wp=0.93, gamma=1.04, s=0.28, cap=1.15, sat=1.16, skin_sat=1.05, mid=(14.0, 0.16), fine=(1.6, 0.25)),
}
CX, CY, RX, RY, D0, D1 = 540.0, 700.0, 640.0, 1040.0, 0.62, 1.30   # the relight ellipse in output px: full light inside D0, full fall-off at D1 (a smoothstep, so no ring)
_mask = {}


def relight_mask(h, w):
    if (h, w) not in _mask:
        y, x = np.mgrid[0:h, 0:w].astype(np.float32)
        u = np.clip((np.sqrt(((x - CX * w / 1080) / (RX * w / 1080)) ** 2 + ((y - CY * h / 1920) / (RY * h / 1920)) ** 2) - D0) / (D1 - D0), 0, 1)
        _mask[(h, w)] = (u * u * (3 - 2 * u))[..., None]
    return _mask[(h, w)]


def grade(a, L):
    """a: float32 RGB 0..1 -> graded."""
    x = np.clip(a * np.array(L["gain"], np.float32), 0, 1)
    if L["relight"]:
        x = x * (1 - L["relight"] * relight_mask(*x.shape[:2]))
    y = np.maximum(x[..., 0] * 0.2126 + x[..., 1] * 0.7152 + x[..., 2] * 0.0722, 1e-4)
    t = np.clip((y - L["bp"]) / (L["wp"] - L["bp"]), 0, 1) ** L["gamma"]
    t = t + L["s"] * (t * t * (3 - 2 * t) - t)
    t = t + L["mid"][1] * (t - cv2.GaussianBlur(t, (0, 0), L["mid"][0])) + L["fine"][1] * (t - cv2.GaussianBlur(t, (0, 0), L["fine"][0]))
    t = np.clip(t, 0, 1)
    k = (t / y)[..., None]
    c = x - y[..., None]                                        # chroma: follows the tone, capped, so a lifted shadow never goes neon and a dark skin shadow never goes orange
    c = c * np.minimum(k, L["cap"])
    mx, mn = x.max(2), x.min(2); d = mx - mn                    # a soft skin weight by hue, so skin keeps its colour while the shirt, the watch and the cars pop
    hue = np.where(d > 1e-4, ((x[..., 1] - x[..., 2]) / np.maximum(d, 1e-4) % 6) * 60, 180.0)
    w = np.clip(1 - np.abs(hue - 22) / 26, 0, 1)[..., None]
    c = c * (L["sat"] + (L["skin_sat"] - L["sat"]) * w)
    return np.clip(t[..., None] + c, 0, 1)


def main():
    if sys.argv[1] == "--test":
        look = {**LOOK[sys.argv[4] if len(sys.argv) > 4 else "A"], **(json.loads(sys.argv[5]) if len(sys.argv) > 5 else {})}
        a = cv2.cvtColor(cv2.imread(sys.argv[2]), cv2.COLOR_BGR2RGB).astype(np.float32) / 255
        cv2.imwrite(sys.argv[3], cv2.cvtColor((grade(a, look) * 255 + 0.5).astype(np.uint8), cv2.COLOR_RGB2BGR))
        return
    job = os.path.abspath(sys.argv[1])
    spec = json.load(open(os.path.join(job, "yt", "spec.json"), encoding="utf-8"))
    fps, out_fps = spec["fps"], spec.get("fps_out", spec["fps"])
    # spec "grade_look" (opt-in, 2026-11-05, AffanWiz levels Short): per-kind overrides for footage far from the bright flat podcast these numbers were tuned on
    # (his dark warm room already has real blacks: the default A look crushed his face). Without the key: the defaults, unchanged.
    looks = {n: {**v, **spec.get("grade_look", {}).get(n, {})} for n, v in LOOK.items()}
    k = int(round(out_fps / fps))
    W = os.path.join(job, "yt", "work")
    pic = os.path.join(W, f"picture.whip{int(out_fps)}.mov" if out_fps != fps else "picture.whip.mp4")
    base, ext = os.path.splitext(pic)
    raw, mark = base + ".ungraded" + ext, pic + ".graded.json"
    fp = lambda: [os.stat(pic).st_size, int(os.stat(pic).st_mtime)]
    ours = lambda m: os.path.exists(m) and json.load(open(m)) == fp()
    if not os.path.exists(raw) or not (ours(mark) or ours(pic + ".sharpened.json")):     # a fresh render (not this script's or the sharpen's output) becomes the backup
        shutil.copy2(pic, raw)
    kinds = [None] * (spec["frames"] * k)
    for s in spec["shots"]:
        card = s["kind"] == "B" and os.path.basename(str(s.get("src", ""))).startswith("mg-")
        for n in range(s["f0"] * k, min(s["f1"] * k, len(kinds))):
            kinds[n] = None if card else ("A" if s["kind"] == "A" else "DOC")
    w, h = 1080, 1920
    dec = subprocess.Popen(["ffmpeg", "-v", "error", "-i", raw, "-f", "rawvideo", "-pix_fmt", "rgb48le", "-"], stdout=subprocess.PIPE)
    enc_args = (["-c:v", "prores_ks", "-profile:v", "3", "-pix_fmt", "yuv422p10le"] if pic.endswith(".mov")
                else ["-c:v", "libx264", "-crf", "12", "-preset", "medium", "-pix_fmt", "yuv420p"])
    tmp = base + ".tmp" + ext
    enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb48le", "-s", f"{w}x{h}", "-r", str(out_fps), "-i", "-", *enc_args, "-r", str(out_fps), tmp],
                           stdin=subprocess.PIPE)
    n, size = 0, w * h * 6
    while True:
        b = dec.stdout.read(size)
        if len(b) < size:
            break
        kind = kinds[n] if n < len(kinds) else "DOC"
        if kind is None:
            enc.stdin.write(b)
        else:
            a = np.frombuffer(b, np.uint16).reshape(h, w, 3).astype(np.float32) / 65535
            enc.stdin.write((grade(a, looks[kind]) * 65535 + 0.5).astype(np.uint16).tobytes())
        n += 1
    enc.stdin.close(); enc.wait(); dec.wait()
    assert n == len(kinds), (n, len(kinds))
    os.replace(tmp, pic)
    json.dump(fp(), open(mark, "w"))
    print(f"graded {os.path.basename(pic)}: {n} frames at {out_fps} fps from {os.path.basename(raw)}")


if __name__ == "__main__":
    main()

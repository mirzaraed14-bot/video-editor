# /// script
# requires-python = ">=3.10"
# dependencies = ["opencv-python-headless", "numpy"]
# ///
"""ig_capy.py: place the captions JUST BELOW the speaker's lips at ONE constant position per video (default; per-shot = legacy) (Affan, 2026-10-06: "the distance between the captions and
the lips needs to be shorter… I was constantly moving my eyes up and down") -> writes "y" into each `captions.chunks[*]` of the spec.

  uv run presets/youtube-shorts/onyx-samples/kit/ig_capy.py projects/<job> [--dir ig] [--gap 0.075] [--pad 6] [--dry]

Per SHOT (so the text only moves on a cut, never inside one):
  A    the mouth corners from `faces.json` (yt_faces.py, landmarks) are mapped through the shot's own crop math (yt_picture.py:
       height-fit scale x z0 x (1 + r·u), the line-fit face x, the median face y, fy_out, clamped view); the caption TOP sits
       `gap` x face height + `pad` px under the LOWEST mouth line of the shot (the lower lip plus breathing room).
  FIT  (an inset of the base) the face is detected on 3 frames of the shot and mapped through the inset (crop, fit, z0, fg_y);
       only a face inside the inset and at least 0.3 of its height counts (a screen capture's avatar or post photo does not).
  B    and shots under a full-screen card (circles, sheet): the median face-shot position, so B-roll doesn't make the text jump.
  SPLIT (YouTube look) keeps the look's seam band. Old boxes-only faces.json: add "faces_lm" (a fresh yt_faces.py scan) to the spec.
Then per CHUNK: a chunk that would appear 1..lead frames before a cut appears ON the cut (the chunk before holds); a chunk on screen
across a cut takes each shot's own height, moving ON the cut frame ("moves": [[frame, y]]; QA 2026-10-06: a chunk spanning a cut
otherwise sat on the other shot's mouth); each segment is pushed below (or above) any card live during it, kept inside
y 200 → min(1620, credit_y - 8) - caption height.
The spec's own `captions.y` stays the fallback. Re-run after any shot, crop or card change; it is idempotent.
"""
import json, math, os, subprocess, sys
import numpy as np

KIT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(KIT, "..", "..", "..", ".."))
MODEL = os.path.join(REPO, "assets", "models", "face_detection_yunet_2023mar.onnx")
W, H = 1080, 1920
CARD_H = {"title": 230, "label": 190, "chip": 90, "number": 290, "image": 420, "prompt": 320, "call": 160, "notify": 230,
          "check": 390, "chat": 380, "tabs": 420}
FULL = {"circles", "sheet"}


def probe(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height", "-of", "csv=p=0", path],
                         capture_output=True, text=True).stdout.strip().splitlines()[0].split(",")
    return int(out[0]), int(out[1])


def frame_at(path, t, w, h):
    r = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t:.3f}", "-i", path, "-frames:v", "1", "-vf", f"scale={w}:{h}", "-f", "rawvideo",
                        "-pix_fmt", "bgr24", "-"], capture_output=True)
    return np.frombuffer(r.stdout, np.uint8).reshape(h, w, 3) if len(r.stdout) == w * h * 3 else None


def main():
    job = os.path.abspath(sys.argv[1]); a = sys.argv
    sub = a[a.index("--dir") + 1] if "--dir" in a else "ig"
    gap_cli = float(a[a.index("--gap") + 1]) if "--gap" in a else None
    pad = float(a[a.index("--pad") + 1]) if "--pad" in a else 6
    p = os.path.join(job, sub, "spec.json"); spec = json.load(open(p, encoding="utf-8"))
    P = lambda rel: rel if os.path.isabs(rel) else os.path.join(job, rel)
    fps = spec["fps"]; base = P(spec["base"])
    hq = P(spec["base_hq"]) if spec.get("base_hq") and os.path.exists(P(spec["base_hq"])) else base
    BW0, BH0 = probe(base); BW, BH = probe(hq); S = BW / BW0
    faces = json.load(open(P(spec["faces"]), encoding="utf-8")) if spec.get("faces") else {}
    # a faces.json from before the landmarks (boxes only, [x, y, w, h]) keeps driving the picture; "faces_lm" (a fresh yt_faces.py
    # scan) then gives each speaker's mouth line as a fraction of the box (YuNet: 0.72-0.77, stable to +-0.03), applied to the old boxes
    lm = json.load(open(P(spec["faces_lm"]), encoding="utf-8")) if spec.get("faces_lm") else {}
    rel = {k: float(np.median([((e[11] + e[13]) / 2 - e[1]) / e[3] for e in v["per_frame"].values() if len(e) >= 14]))
           for k, v in lm.items() if any(len(e) >= 14 for e in v["per_frame"].values())}
    cap = spec["captions"]; size = cap.get("size", 52) if sub != "yt" else 86
    # caption top = lowest mouth-CORNER line + gap x face height + pad. The corners do not move much when the mouth opens but the
    # lower lip drops 0.09-0.12 x face height below them (QA r3 Rollo, measured on 880-1320 px faces; Pomp r3: the box clipped
    # the lower lip on 85 frames at 0.075), so the default clears an OPEN mouth. Per job: captions.lip_gap.
    gap = gap_cli if gap_cli is not None else float(cap.get("lip_gap", 0.13))
    width = cap.get("width", 960) if cap.get("align") == "left" else 960
    credit_lim = (spec.get("credit_y", cap.get("y", 1310) - 80) - 8) if spec.get("credit") else 1620
    if credit_lim < 900:                 # a credit line at the TOP of the frame (Rich Roll 2026-10-08) never bounds the captions from below
        credit_lim = 1620

    def cap_h(text):
        lines = max(1, math.ceil(len(text) * size * 0.53 / max(width, 200))) if cap.get("align") == "left" else 1
        return size * 1.18 * lines + (22 if cap.get("style", "box") in ("box", "darkbox", "pill") else 6)

    def shot_top_A(sh):
        pf = faces.get(sh["face"], {}).get("per_frame", {})
        ks = sorted(int(k) for k in pf if sh["f0"] <= int(k) < sh["f1"] and (len(pf[k]) >= 14 or sh["face"] in rel))
        if len(ks) < 2:
            return None
        n_ = min(len(pf[str(k)]) for k in ks); xs = np.array(ks, float); box = np.array([pf[str(k)][:n_] for k in ks])
        cx = box[:, 0] + box[:, 2] / 2; cy = float(np.median(box[:, 1] + box[:, 3] / 2))
        b, a0 = (np.polyfit(xs, cx, 1) if len(ks) >= 3 else (0.0, float(np.mean(cx))))
        b = float(np.clip(b, -2, 2)); a0 = float(np.mean(cx) - b * np.mean(xs))
        tops = []
        for j, n in enumerate(ks):
            u = (n - sh["f0"]) / fps
            k = max(W / BW, H / BH) * sh["z0"] * (1 + sh.get("r", 0.0) * u)
            vw, vh = W / k, H / k
            fx, fy = (a0 + b * n) * S, cy * S
            x0 = min(max(fx - sh["fx_out"] * vw, 0), max(BW - vw, 0)); y0 = min(max(fy - sh["fy_out"] * vh, 0), max(BH - vh, 0))
            mouth = ((box[j, 11] + box[j, 13]) / 2 if box.shape[1] >= 14 else box[j, 1] + rel[sh["face"]] * box[j, 3]) * S
            tops.append((mouth - y0) * k + gap * box[j, 3] * S * k + pad)
        return float(np.percentile(tops, 90))

    det = None
    def shot_top_FIT(sh):
        nonlocal det
        if os.path.abspath(P(sh["src"])) not in (os.path.abspath(base), os.path.abspath(hq)):
            return None
        import cv2
        src = P(sh["src"]); sw, shh = probe(src); sc = min(1.0, 1920 / sw); dw, dh = int(sw * sc), int(shh * sc)
        if det is None or det[1] != (dw, dh):
            det = (cv2.FaceDetectorYN.create(MODEL, "", (dw, dh), 0.6, 0.3, 5000), (dw, dh))
        cx0, cy0, cx1, cy1 = sh.get("crop", [0, 0, 1, 1]); cwp, chp = (cx1 - cx0) * sw, (cy1 - cy0) * shh
        kf = W / cwp * sh.get("z0", 1.0); fw, fh = cwp * kf, chp * kf
        ox, oy = (W - fw) / 2, (sh["fg_y"] - fh / 2) if sh.get("fg_y") else (H - fh) / 2
        tops = []
        for q in (0.2, 0.5, 0.8):
            t = sh.get("src_in", sh["f0"] / fps) + q * (sh["f1"] - sh["f0"]) / fps
            img = frame_at(src, t, dw, dh)
            if img is None:
                continue
            _, fs = det[0].detect(img)
            if fs is None or not len(fs):
                continue
            f = max(fs, key=lambda r: r[2] * r[3]) / sc
            inside = cx0 * sw <= f[0] + f[2] / 2 <= cx1 * sw and cy0 * shh <= f[1] + f[3] / 2 <= cy1 * shh
            if not inside or f[3] < 0.3 * chp:      # outside the inset, or small (a photo in a captured post: 0.21 of the inset; a
                continue                            # speaker inset: 0.55-0.60): not the speaker, so the shot takes the median
            mouth = (f[11] + f[13]) / 2
            tops.append((mouth - cy0 * shh) * kf + oy + gap * f[3] * kf + pad)
        return float(max(tops)) if tops else None

    shot_top = {}
    for sh in spec["shots"]:
        t = shot_top_A(sh) if sh["kind"] == "A" else (shot_top_FIT(sh) if sh["kind"] == "FIT" else None)
        if t is not None:
            shot_top[sh["id"]] = t
    default = float(np.median(list(shot_top.values()))) if shot_top else float(cap.get("y", 1310))
    cards = spec.get("cards", [])
    yt = sub == "yt"
    if yt:                # YouTube look: chunks live in yt/captions.json (timed by yt_captions.py); "y" there is the GLYPH CENTRE
        cpath = os.path.join(job, "yt", "captions.json"); cj = json.load(open(cpath, encoding="utf-8")); chunks = cj["chunks"]
    else:
        chunks = cap.get("chunks", [])
    # CONSTANT mode (the default since Affan's review 2, 2026-10-07: "I want constant positioning of the captions… No videos should
    # have different sets of base positioning"): ONE caption position for the whole video, just under the lips where the face
    # usually sits (75th percentile of the measured face shots, so most clear an open mouth). Nothing moves on a cut. Shots whose
    # lips would sit on that line are REPORTED (reframe them: raise the face / match the zoom), and so are cards that cross the band:
    # move the card, not the caption. `captions.place: "per-shot"` keeps the older per-shot lip line (+ moves on cuts).
    if cap.get("place", "constant") == "constant":
        tops = [v for k, v in shot_top.items()]
        Y = float(np.percentile(tops, cap.get("pct", 75))) if tops else float(cap.get("y", 1310))   # captions.pct 100 = clear EVERY mouth
        if yt:
            yc = int(round(min(max(Y + 50, 760), spec.get("watermark_y", 1160) - 90)))
            for c in chunks:
                for k in ("moves", "show", "hide"):
                    c.pop(k, None)
                c["y"] = yc
            top_line = yc - 50
        else:
            hmax = max((cap_h(c["text"]) for c in chunks), default=70)
            yt_ = int(round(min(max(Y, 560), min(1620, credit_lim) - hmax)))
            for c in chunks:
                for k in ("moves", "show", "hide"):
                    c.pop(k, None)
                c["y"] = yt_
            top_line = yt_
        lips = sorted(((sid, int(t - top_line)) for sid, t in shot_top.items() if t > top_line + 8), key=lambda x: -x[1])
        clash = []
        if not yt:
            for k in cards:
                if k["kind"] in FULL:
                    continue
                ky = k.get("y", 300); kh = CARD_H.get(k["kind"], 250) * (len(k.get("lines", [1])) / 2 if k["kind"] == "label" else 1)
                if top_line < ky + kh + 14 and top_line + hmax > ky - 14 and any(c["start"] < k["t1"] and c["end"] > k["t0"] for c in chunks):
                    clash.append(f'{k["kind"]}@{k["t0"]}s y{ky}-{int(ky + kh)}')
        if "--dry" not in a:
            json.dump(cj if yt else spec, open(cpath if yt else p, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
        print(f"{'ig_capy (yt)' if yt else 'ig_capy'}: CONSTANT caption {'glyph centre ' + str(yc) if yt else 'top ' + str(top_line)} "
              f"({cap.get('pct', 75)}th pct of {len(tops)} face shots){' [dry run]' if '--dry' in a else ''}")
        if lips:
            print("  reframe (the lips sit under the caption line by px): " + ", ".join(f"{sid} +{d}" for sid, d in lips))
        if clash:
            print("  cards crossing the caption band (move the card): " + ", ".join(clash))
        return
    cuts = sorted({sh["f0"] for sh in spec["shots"] if sh["f0"] > 0})
    shot_at = lambda n: next((sh for sh in spec["shots"] if sh["f0"] <= n < sh["f1"]), spec["shots"][-1])
    fr = lambda t: int(round(t * fps + 1e-6))               # both overlays show a chunk on frames [round(start*fps), round(end*fps))
    # 1. SNAP (QA r3, Pomp + Rollo): a chunk that would appear 1..lead frames BEFORE a cut appears ON the cut instead, so it never
    #    flashes at the old shot's lip height, and the chunk before it holds to the cut. Never later than the chunk's own lead, so
    #    the text still lands on (or before) its first word. YouTube: start/end are rewritten (yt_captions.py regenerates them every
    #    build); Instagram: the hand-tuned start/end stay and the effective times go to "show"/"hide", recomputed on every run.
    snap_n = int(round(cap.get("lead", 0.135 if yt else 0.08) * fps))
    order = sorted(range(len(chunks)), key=lambda i: chunks[i]["start"])
    show = {i: fr(chunks[i]["start"]) for i in order}; hide = {i: fr(chunks[i]["end"]) for i in order}
    # ...but ONLY while the chunk still appears >= 0.02 s before its first word (QA r3 Rollo: a blanket 4-frame snap made "IS GOING
    # TO DO." 0.077 s late; not every chunk has the full lead). The word: the MEASURED acoustic onset when yt_captions has one, else
    # the transcript's start - 0.055 s (WhisperX starts run that late). Instagram's 0.08 s lead leaves no room: there the chunk keeps
    # its time and simply MOVES on the cut.
    tw = []
    tp = os.path.join(job, "outputs", f"{os.path.basename(job)}.transcript.json")
    if os.path.exists(tp):
        tw = sorted(float(w["start"]) for w in json.load(open(tp, encoding="utf-8")).get("words", []) if w.get("start") is not None)
    def word_at(c):
        if c.get("onset") is not None:
            return float(c["onset"])
        if c.get("first_word") is not None:
            return float(c["first_word"]) - 0.055
        w = next((x for x in tw if x >= c["start"] - 0.01), None)
        return None if w is None else w - 0.055
    snaps = 0
    for j, i in enumerate(order):
        ref = word_at(chunks[i])
        k = next((k for k in cuts if show[i] < k <= show[i] + snap_n and k < hide[i] - 2), None)
        if k is None or ref is None or k / fps > ref - 0.02:
            continue
        if j and abs(hide[order[j - 1]] - show[i]) <= 1:
            hide[order[j - 1]] = k
        show[i] = k; snaps += 1
    # 2. PLACE per SEGMENT: a chunk on screen across a cut is cut into segments at the cut; each takes ITS shot's lip line (and
    #    clears the cards live during it); the chunk enters once and later segments are "moves" [frame, y] applied ON the cut frame.
    def seg_y(a0, b0, text):
        sh = shot_at(a0)
        if yt:
            if sh["kind"] == "SPLIT":                     # the caption stays on the seam, between the face above and the B-roll below
                return int(cap.get("y", 1071))
            top = shot_top.get(sh["id"], default)
            return int(round(min(max(top + 50, 760), spec.get("watermark_y", 1160) - 90)))   # cap ~92 px: bottom >= 20 px over the watermark
        t0, t1 = a0 / fps, b0 / fps
        live = [k for k in cards if k["t0"] - 0.05 < t1 and k["t1"] > t0]
        if any(k["kind"] in FULL for k in live):          # a full-screen graphic was laid out around the spec's own caption band
            return int(cap.get("y", default))
        y = ideal = shot_top.get(sh["id"], default)
        h = cap_h(text)
        for k in sorted(live, key=lambda k: k.get("y", 0)):
            ky = k.get("y", 300); kh = CARD_H.get(k["kind"], 250) * (len(k.get("lines", [1])) / 2 if k["kind"] == "label" else 1)
            if y < ky + kh + 14 and y + h > ky - 14:      # collides: ABOVE the card if that still clears the lips, else below it
                above, below = ky - 16 - h, ky + kh + 16
                # above the card while it is within 90 px of the open-mouth line (that line is conservative: Rob's "right around
                # $23,000." above his number card clears the lower lip by ~60 px; below the card it sat ~400 px from his mouth)
                y = above if above >= ideal - 90 or below + h > credit_lim else below
        return int(round(min(max(y, 560), min(1620, credit_lim) - h)))

    out, nmoves = [], 0
    for i in order:
        c = chunks[i]; a0, b0 = show[i], max(hide[i], show[i] + 1)
        bounds = [a0] + [k for k in cuts if a0 < k < b0] + [b0]
        ys = [(x, seg_y(x, x1, c["text"])) for x, x1 in zip(bounds, bounds[1:])]
        moves = []
        for (x, y), (_, yp) in zip(ys[1:], ys):
            if abs(y - (moves[-1][1] if moves else yp)) >= 4:
                moves.append([x, y])
        out += [y for _, y in ys]; nmoves += len(moves)
        if "--dry" in a:
            continue
        c["y"] = ys[0][1]
        c.pop("moves", None)
        if moves:
            c["moves"] = moves
        if yt:
            c["start"], c["end"] = round(show[i] / fps, 5), round(hide[i] / fps, 5)
        else:
            c.pop("show", None); c.pop("hide", None)
            if show[i] != fr(c["start"]):
                c["show"] = round(show[i] / fps, 5)
            if hide[i] != fr(c["end"]):
                c["hide"] = round(hide[i] / fps, 5)
    if "--dry" not in a:
        json.dump(cj if yt else spec, open(cpath if yt else p, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    tag = "ig_capy (yt)" if yt else "ig_capy"
    print(f"{tag}: {len(shot_top)} shots measured, default {default:.0f}; y min/median/max {min(out)}/{int(np.median(out))}/{max(out)}; "
          f"{snaps} starts snapped onto a cut, {nmoves} on-cut moves" + (" [dry run]" if "--dry" in a else ""))


if __name__ == "__main__":
    main()

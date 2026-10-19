"""ig_qa.py: the MEASURED self-check of an Instagram-look build (AGENT-BRIEF "Done means": decode, loudness, captions vs the cut
transcript, SFX vs graphics, overlay edges vs cuts, a contact sheet). Written for the v2 look (batch 2); the caption and decode checks
work on v1 jobs too.

  python presets/youtube-shorts/onyx-samples/kit/ig_qa.py projects/<job> outputs/<job>.sample-ig.<version>.mp4 [--sheet]

Checks (each prints PASS / FAIL / NOTE; exit 1 on any FAIL):
  decode     ffmpeg -v error decodes every frame with no message
  loudness   integrated within 0.5 LU of audio.target_i (-13), true peak <= target_tp + 0.1 (-1.5 dBTP)
  captions   every transcript word of the cut is captioned exactly once and in order (spec drop list honoured), only ! ? and quotes
             survive (captext.clean), ONE constant y for the whole video, the block inside the v2 window
  sfx        every designed event has a sound within 0.15 s; each cue's peak vs the voice's peak around it, measured on the mix's own
             stems (premix - voice = SFX + bed); the longest stretch without a designed sound (README § 6: ~1.5 s)
  density    the ig_v2 report (events per 10 s, full-window share, face between scenes, long holds, edges near cuts)
  restate    (batch 3, v2) no card prints > 50 % of the words the captions on screen with it say (STYLE-RESEARCH § E5)
  slots      (batch 3, v2) no more than 2 side cards in a row in one slot (top-left, low-right, a bar, docked to an object)
  leaks      (batch 3, v2) <= 2 light leaks per video (§ E6); top bar: its share of the runtime with content, a NOTE (target >= 25 %)
  --sheet    a contact sheet of the output at every cut and every card entrance -> ig/work/qa-sheet.jpg
"""
import io, json, math, os, re, subprocess, sys
import numpy as np

KIT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, KIT)
from captext import clean            # noqa: E402

fails = []


def say(ok, name, msg):
    tag = "PASS" if ok is True else ("NOTE" if ok is None else "FAIL")
    if ok is False:
        fails.append(name)
    print(f"{tag:4s}  {name:9s} {msg}")


def audio(path, sr=48000):
    r = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-ac", "1", "-ar", str(sr), "-f", "f32le", "-"], capture_output=True)
    return np.frombuffer(r.stdout, np.float32)


def main():
    job, outp = os.path.abspath(sys.argv[1]), sys.argv[2]
    outp = outp if os.path.isabs(outp) else os.path.join(job, outp)
    spec = json.load(open(os.path.join(job, "ig", "spec.json"), encoding="utf-8"))
    fps, dur = spec["fps"], spec["frames"] / spec["fps"]
    w = os.path.join(job, "ig", "work")

    # ---- decode
    r = subprocess.run(["ffmpeg", "-v", "error", "-i", outp, "-f", "null", "-"], capture_output=True, text=True)
    say(not r.stderr.strip(), "decode", "clean" if not r.stderr.strip() else r.stderr.strip()[:300])

    # ---- loudness
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", outp, "-af", "ebur128=peak=true", "-f", "null", "-"], capture_output=True, text=True).stderr
    I = float(re.findall(r"I:\s+(-?[\d.]+) LUFS", r)[-1]); TP = float(re.findall(r"Peak:\s+(-?[\d.]+) dBFS", r)[-1])
    a = spec.get("audio", {}); ti, ttp = a.get("target_i", -13.0), a.get("target_tp", -1.5)
    say(abs(I - ti) <= 0.5 and TP <= ttp + 0.1, "loudness", f"{I:.1f} LUFS (target {ti}), true peak {TP:.1f} dBTP (<= {ttp})")

    # ---- captions
    cap = spec.get("captions", {})
    words = json.load(open(cap["words"] if os.path.isabs(cap["words"]) else os.path.join(job, cap["words"]), encoding="utf-8"))
    words = [x for x in (words["words"] if isinstance(words, dict) else words) if x.get("type", "word") == "word"][cap.get("skip_words", 0):]
    P = ".,!?"
    drop = cap.get("drop", [])
    words = [x for x in words if not any(abs(float(x["start"]) - t) <= 0.06 and x["text"].strip(P).lower() == str(d).strip(P).lower() for t, d in drop)]
    chunks = cap.get("chunks", [])
    if chunks and "words" in chunks[0]:
        shown = [(cw[0], cw[2]) for c in chunks for cw in c["words"]]
    else:                              # v1 chunks carry text only: compare the word sequence
        shown = [(None, t) for c in chunks for t in c["text"].split()]
    want = [(float(x["start"]), x["text"]) for x in words]
    seq_ok = [t.strip(P + "\"“”").lower() for _, t in shown] == [t.strip(P + "\"“”").lower() for _, t in want]
    if not seq_ok:
        a_, b_ = [t.strip(P).lower() for _, t in shown], [t.strip(P).lower() for _, t in want]
        k = next((i for i, (x, y) in enumerate(zip(a_, b_)) if x != y), min(len(a_), len(b_)))
        say(False, "captions", f"word sequence differs at #{k}: shown {a_[k:k + 4]} vs cut {b_[k:k + 4]} ({len(a_)} vs {len(b_)} words)")
    else:
        say(True, "captions", f"{len(shown)} words, each once and in order")
    # an asterisk INSIDE a word is a starred profanity ("SH*T": captext keeps it on purpose), not punctuation (batch-2 false FAIL, Vivian)
    bad = sorted({ch for _, t in shown for ch in clean(t) if not (ch.isalnum() or ch in " '’!?\"“”$%&+-/×→")
                  and not (ch == "*" and re.search(r"\w\*+\w", clean(t)))})
    say(not bad, "punct", "only ! ? and quotes survive" if not bad else f"characters left on screen: {bad}")
    ys = sorted({c.get("y") for c in chunks})
    say(len(ys) == 1, "position", f"constant caption y {ys[0]}" if len(ys) == 1 else f"{len(ys)} different caption y values: {ys[:6]}")
    if spec.get("look") == "v2" and len(ys) == 1:
        sys.path.insert(0, KIT)
        import ig_type
        FR = ig_type.frame(spec)
        hmax = max(ig_type.cap_height(c, cap) for c in chunks)
        inside = FR["y"] <= ys[0] and ys[0] + hmax <= FR["y"] + FR["h"]
        say(inside, "window", f"caption block {ys[0]}-{ys[0] + hmax} inside the window {FR['y']}-{FR['y'] + FR['h']}")

    # ---- sfx: one sound per designed event, and how loud each one is against the voice around it
    cues = json.load(open(os.path.join(w, "sfx-cues.json"), encoding="utf-8")) + a.get("sfx", [])
    ct = sorted(c["t"] for c in cues)
    evp = os.path.join(w, "v2-events.json")
    if os.path.exists(evp):
        ev = json.load(open(evp, encoding="utf-8"))
        silent = [f"{t:.2f} {lab}" for t, lab, _ in ev["events"] if not any(abs(c - t) <= 0.15 for c in ct)]
        say(not silent, "sfx", f"{len(cues)} cues for {len(ev['events'])} designed events" + (f"; no sound on: {silent}" if silent else ""))
        print("      density: " + " | ".join(ev["lines"]))
    if spec.get("look") == "v2":       # batch 3's gates (STYLE-RESEARCH § E5 / E6 / E1), on the spec as it stands now
        import ig_type, ig_v2
        FR_ = ig_type.frame(spec)
        g = ig_v2.gates(spec, ig_v2.expand_cards(spec), FR_, dur)
        say(not g["overlap"], "restate", "no card restates the captions on screen with it (<= 50 % of its words)" if not g["overlap"] else
            "cards repeating the captions: " + "; ".join(f"{o['kind']}@{o['t0']} {o['share'] * 100:.0f} % ({', '.join(o['words'][:4])})" for o in g["overlap"]))
        say(not g["slot_runs"], "slots", "no slot holds more than 2 side cards in a row" if not g["slot_runs"] else
            "3+ side cards in a row in one slot: " + "; ".join(f"{r[0][1]} x{len(r)} from {r[0][0]:.2f} s" for r in g["slot_runs"]))
        say(g["leaks"] <= ig_v2.LEAK_MAX, "leaks", f"{g['leaks']} light leaks (<= {ig_v2.LEAK_MAX}, real source changes only)")
        if g["topbar_share"] is not None:
            say(None, "top bar", f"carries content {g['topbar_share'] * 100:.0f} % of the runtime (target >= 25 %, or empty by choice)")
    gaps = np.diff([0.0] + ct + [dur])
    gi = int(np.argmax(gaps))
    say(None, "sfx gap", f"longest stretch without a designed sound {gaps.max():.1f} s (from {([0.0] + ct)[gi]:.2f} s; README § 6 asks ~1.5 s, a bed fills it)")
    v, m = os.path.join(w, "voice.wav"), os.path.join(w, "premix.wav")
    if os.path.exists(v) and os.path.exists(m):
        sr = 48000
        vo, pm = audio(v, sr), audio(m, sr)
        n = min(len(vo), len(pm)); rest = pm[:n] - vo[:n]          # SFX + bed (amix normalize=0 is a plain sum)
        db = lambda x: 20 * math.log10(float(np.max(np.abs(x))) + 1e-9)
        rows = []
        for c in sorted(cues, key=lambda c: c["t"]):
            i0, i1 = int(max(0, c["t"] - 0.08) * sr), int((c["t"] + 0.35) * sr)
            j0, j1 = int(max(0, c["t"] - 0.6) * sr), int((c["t"] + 0.6) * sr)
            rows.append((c["t"], c["kind"], db(rest[i0:i1]) - db(vo[j0:j1])))
        rel = np.array([r_[2] for r_ in rows])
        quiet = [f"{t:.2f} {k} {d:+.0f}" for t, k, d in rows if d < -20]
        loud = [f"{t:.2f} {k} {d:+.0f}" for t, k, d in rows if d > 1.0]
        say(not loud, "sfx level", f"cue peak vs the voice peak around it: median {np.median(rel):+.1f} dB, range {rel.min():+.0f}..{rel.max():+.0f}"
            + (f"; over the voice: {loud}" if loud else "") + (f"; very quiet (< -20 dB): {quiet}" if quiet else ""))

    # ---- contact sheet
    if "--sheet" in sys.argv:
        from PIL import Image, ImageDraw
        ts = sorted({round(s["f0"] / fps + 0.25, 2) for s in spec["shots"]} | {round(k.get("t0", k.get("t", 0)) + 0.45, 2) for k in spec.get("cards", [])}
                    | ({round(spec["hook"]["t0"] + 0.8, 2)} if spec.get("hook") else set()))
        tiles = []
        for t in [t for t in ts if t < dur]:
            r = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t:.3f}", "-i", outp, "-frames:v", "1", "-f", "image2pipe", "-vcodec", "png", "-"], capture_output=True)
            im = Image.open(io.BytesIO(r.stdout)).convert("RGB").resize((270, 480), Image.LANCZOS)
            ImageDraw.Draw(im).text((8, 8), f"{t:.2f}s", fill=(255, 230, 0))
            tiles.append(im)
        cols = 8; rows = (len(tiles) + cols - 1) // cols
        sheet = Image.new("RGB", (270 * cols, 480 * rows), (30, 30, 30))
        for i, im in enumerate(tiles):
            sheet.paste(im, ((i % cols) * 270, (i // cols) * 480))
        sp = os.path.join(w, "qa-sheet.jpg"); sheet.save(sp, quality=88)
        say(None, "sheet", f"{len(tiles)} frames -> {sp}")
    print("RESULT:", "PASS" if not fails else f"FAIL ({', '.join(fails)})")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()

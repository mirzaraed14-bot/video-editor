"""yt_cues.py: the designed sounds a YouTube-look spec implies on its own (README § 8, STYLE-RESEARCH 2026-10-14 § D1-D4, D6, D9).

Pure Python, imported by yt_mix.py (which places them) and yt_build.py (which counts and asserts them). Nothing here renders.

Affan's lock: every graphic gets an audible, premium sound (Epidemic files in assets/sfx/epidemic/). A spec that uses the new picture
devices therefore gets their cue without writing it by hand; the picture and the sound are planned from the same keys, so moving a
mark moves its tick.

  auto cue                       sound          crest lands on                          level (dB under the voice PEAK)
  hook card (D9)                 whoosh-med     the slide's landing - 0.12 s            16 (only if the spec has no whoosh in 0-1 s)
                                 thud-thin      the slide's landing (frame 11 @ 24 fps) 8  (only if the spec has no thud/hit/boom in 0-1 s)
  DOC highlight (D1)             shutter-film   the sweep's start + 0.04 s              8
  DOC stack layer "at" (D1)      thud-thin      the layer's slap                        10
  mark: circle/box/underline/arrow (D2)  tick-glass   the close of the stroke (t + dur) 6
  chart (D4)                     blip-data      the draw start                          12
                                 thud-thin      the landing (t + draw)                  8
  fx shake / freeze (D6)         thud-low / shutter-film   the effect's first frame     9 / 8   (flicker: none unless named)

Opt out / override, per element: "sfx": false (no cue), "sfx": "<name>" (another library sound, same crest), or
"sfx": {"name": ..., "under": dB, "dt": s (crest shift)}. Whole spec: "audio": {"auto_sfx": false} drops every auto cue; "audio":
{"hook_sfx": "spec"} keeps the hook exactly as the spec wrote it (to remix a shipped batch-2 sample bit-for-bit).
A cue dict is {"file", "t" (playback start = crest - pre), "lead" (head trimmed off the file), "under", "dur", "fade", "why", "crest"};
yt_mix turns "under" into gain_db = voice peak - under - file peak.
"""
import os

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", ".."))
SFX_DIR = "assets/sfx/epidemic"

# name: (lead, pre, under, dur, fade). lead = silence trimmed off the head, pre = trimmed start -> crest, dur / fade = the slice.
# Measured 2026-10-12 for the Instagram kit (ig_build.py ES_LEAD / ES_PRE / ES_DUR, 25 ms RMS bins); levels = the v2 values and the
# batch-3 research (§ D1 shutter 8, § D9 hit 8 + whoosh 15-16).
SFX = {
    "tick-glass": (0.0, 0.0, 6, 0.3, 0.05),
    "blip-data": (0.0, 0.0, 12, 0.5, 0.1),
    "shutter-film": (0.0, 0.10, 8, 0.5, 0.12),
    "focus-pull": (0.0, 0.05, 9, 0.6, 0.1),
    "thud-thin": (0.0, 0.03, 8, 1.2, 0.4),
    "thud-low": (0.0, 0.06, 9, 2.0, 0.6),
    "hit-soft": (0.08, 0.26, 5, 2.2, 0.7),
    "boom-dark": (0.04, 0.46, 10, 2.5, 0.8),
    "flash-vintage": (0.03, 0.11, 9, 1.0, 0.3),
    "pop-glass": (0.585, 0.01, 6, 0.6, 0.1),
    "rise-air": (0.05, 1.22, 12, 1.5, 0.2),
    "whoosh-soft": (0.03, 0.26, 15, 1.0, 0.3),
    "whoosh-med": (0.15, 0.70, 16, 1.6, 0.4),
}
HOOK_IN_24 = 11            # yt_overlay.py IN_24: the hook slides in over 11 frames at 24 fps and lands on the last of them


def cue(name, crest, why, under=None):
    lead, pre, und, dur, fade = SFX[name]
    if crest < pre:                       # too close to the start: trim more of the head so the crest still lands
        lead, pre = lead + pre - crest, crest
    return dict(file=f"{SFX_DIR}/{name}.wav", t=round(crest - pre, 3), lead=round(lead, 3), under=und if under is None else under,
                dur=dur, fade=fade, why=why, crest=round(crest, 3))


def _custom(default, crest, why, sfx, under=None):
    """Apply an element's "sfx" override to its default cue (False / "none" = no cue)."""
    if sfx is False or sfx == "none":
        return None
    if isinstance(sfx, str):
        return cue(sfx, crest, why, under)
    if isinstance(sfx, dict):
        return cue(sfx.get("name", default), crest + sfx.get("dt", 0.0), why, sfx.get("under", under))
    return cue(default, crest, why, under)


def hook_landing(fps):
    return (int(round(HOOK_IN_24 * fps / 24)) - 1) / fps


def hook_cues(spec):
    """The hook card's sound pair (D9): what the spec already has in 0-1 s, plus what is missing. Returns (whoosh, hit, added)."""
    a = spec.get("audio", {})
    if not (spec.get("hook") or {}).get("lines"):
        return None, None, []
    near = [c for c in a.get("sfx", []) if c.get("t", 9) <= 1.0]
    whoosh = next((c for c in near if "whoosh" in os.path.basename(c["file"])), None)
    hit = next((c for c in near if any(k in os.path.basename(c["file"]) for k in ("thud", "hit", "boom", "impact"))), None)
    if a.get("hook_sfx") == "spec" or a.get("auto_sfx") is False:
        return whoosh, hit, []
    land = hook_landing(spec["fps"])
    added = []
    if whoosh is None:
        whoosh = cue("whoosh-med", max(0.30, land - 0.12), "hook slides in"); added.append(whoosh)
    if hit is None:
        hit = cue("thud-thin", land, "hook lands"); added.append(hit)
    return whoosh, hit, added


def picture_cues(spec):
    """Cues for the picture devices (DOC highlights and stack slaps, marks, charts, fx), in time order."""
    fps = spec["fps"]
    out = []
    add = lambda c: out.append(c) if c else None
    for s in spec.get("shots", []):
        t0 = s["f0"] / fps
        off = False if s.get("sfx") is False else None          # a shot-level "sfx": false silences all of its devices
        if s["kind"] == "DOC":
            for h in s.get("highlight", []):
                hd = h if isinstance(h, dict) else dict(t=h[0])
                add(_custom("shutter-film", hd["t"] + 0.04, f"{s['id']} highlight", hd.get("sfx", off)))
            for e in s.get("stack", []):
                if isinstance(e, dict) and e.get("at") is not None and e["at"] > t0 + 1e-6:
                    add(_custom("thud-thin", e["at"], f"{s['id']} stack slap", e.get("sfx", off), under=10))
        for m in s.get("marks", []):
            add(_custom("tick-glass", m["t"] + m.get("dur", 0.35), f"{s['id']} {m.get('type', 'circle')} mark", m.get("sfx", off)))
        ch = s.get("chart")
        if ch and ch.get("sfx", off) is not False:
            ct, dr = ch.get("t", t0 + 0.2), ch.get("draw", 0.8)
            o = ch.get("sfx") if isinstance(ch.get("sfx"), dict) else {}
            add(_custom("blip-data", ct, f"{s['id']} chart draws", o.get("draw")))
            add(_custom("thud-thin", ct + dr, f"{s['id']} chart lands", o.get("land")))
        fxs = s.get("fx", [])
        for z in ([fxs] if isinstance(fxs, dict) else fxs):
            dflt = {"shake": "thud-low", "freeze": "shutter-film"}.get(z.get("kind"))
            sx = z.get("sfx", off)
            if sx or (dflt and sx is not False):
                add(_custom(dflt or "boom-dark", z.get("f0", s["f0"]) / fps, f"{s['id']} fx {z.get('kind')}", sx))
    return sorted(out, key=lambda c: c["crest"])


def auto_cues(spec):
    """Every cue the kit adds to the spec's own `audio.sfx` (hook pair first, then the picture devices)."""
    if spec.get("audio", {}).get("auto_sfx") is False:
        return []
    return hook_cues(spec)[2] + picture_cues(spec)


def check(spec):
    """(problems, lines) for yt_build: every auto cue's file exists, and the hook carries its pair (the Pomp lesson: count every cue)."""
    probs, lines = [], []
    auto = auto_cues(spec)
    n_spec = len(spec.get("audio", {}).get("sfx", []))
    for c in auto:
        if not os.path.exists(os.path.join(REPO, c["file"])):
            probs.append(f"missing SFX file {c['file']} ({c['why']})")
    w, h, added = hook_cues(spec)
    if (spec.get("hook") or {}).get("lines"):
        if not (w and h):
            msg = f"hook card has {'no whoosh' if not w else ''}{' and ' if not w and not h else ''}{'no hit' if not h else ''} (D9: whoosh + a thud on the landing)"
            if spec.get("audio", {}).get("hook_sfx") == "spec":
                lines.append("WARNING " + msg + "; kept as the spec wrote it (hook_sfx: spec)")
            else:
                probs.append(msg)
        else:
            lines.append(f"hook pair: {os.path.basename(w['file'])} t {w['t']:.2f} + {os.path.basename(h['file'])} t {h['t']:.2f}"
                         + (f" ({len(added)} added by the kit)" if added else " (from the spec)"))
    lines.append(f"sfx: {n_spec} spec cues + {len(auto)} auto cues = {n_spec + len(auto)}"
                 + (": " + ", ".join(f"{c['why']} {c['crest']:.2f}" for c in auto) if auto else ""))
    return probs, lines

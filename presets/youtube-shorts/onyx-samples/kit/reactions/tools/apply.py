"""apply.py: lay a reaction job's plan onto its ABW8 sequence (Premiere lane), everything read back.

  PYTHONUTF8=1 python apply.py <job>/plan.json --layout      # face-only switches + screen views (DOM, sequence NOT activated)
  PYTHONUTF8=1 python apply.py <job>/plan.json --window      # ONE short active window: QE addTracks if short + audio-polish (Amplify
                                                             #   +gain into a -6 dBFS Hard Limiter on every A1 clip), then Affan's
                                                             #   previously active sequence is restored
  PYTHONUTF8=1 python apply.py <job>/plan.json --overlays    # import + place captions.mov, mg/*.mov, SFX, the music bed (DOM), save
  PYTHONUTF8=1 python apply.py <job>/plan.json --verify      # read the sequence back against the plan
  PYTHONUTF8=1 python apply.py <job>/plan.json --layout-check   # OFFLINE (no Premiere): the --layout keys + the no-leak proof

Track roles (his layout + ours): screen = plan.screen_track, face = plan.face_track, MG = face + 1, captions = face + 2 (the top);
with plan.frame_track (2026-10-13, the showcase frame around our sample): frame = face + 1, MG = face + 2, captions = face + 3
(mg_track / cap_track default to frame + 1 / frame + 2). Graphics of kind "showcase" go on the frame track, every other one on
the MG track; a showcase may overlap MG graphics (the plan's overlap rule is about the MG track only).
A1 = his voice (untouched but for the house chain), A2 = SFX, A3 = music.
Motion values are written in each clip's own Motion (Scale %, Position as a frame fraction, Crop % per edge); a view with an
"anim" is baked as keys every 1/30 s, a view with a "drift" as keys every 0.5 s across each clip piece (plus the 1/30 s keys
of an anim inside it), so the crop follows the zoom on every frame and the screen never leaks into a bar (layout_jobs()
checks every key, and the midpoint between keys, against the panel box before anything is sent).
The creator's original per-clip values are in the sequence dump (plan.dump), the restore record.
"""
import json, re, math, os, subprocess, sys, time
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", "..", "..", "..", ".."))
sys.path.insert(0, HERE)
import geom as G                       # noqa: E402
from pp import es as _es              # noqa: E402

SFX_DIR = os.path.join(REPO, "assets", "sfx", "epidemic")
SFX_PEAK = {"pop-glass": -13.9, "pop-soft": -16.7, "click": -0.5, "confirm": -10.5, "whoosh-air": -15.0, "whoosh-light": -18.8,
            "hit": -3.3, "notify": -11.7, "riser": -4.6}
# the research-2026-10-13 palette (#12), sample peaks measured 2026-10-13 on the files in assets/sfx/epidemic (volumedetect
# max_volume = astats Peak level; MANIFEST.md's figures run 0.1-2.9 dB hotter for most of these: the files were re-cut since)
SFX_PEAK.update({"tick-glass": -17.3, "focus-pull": -0.0, "thud-thin": -3.0, "whoosh-soft": -8.0, "shutter-film": -10.9,
                 "blip-data": -16.1, "whoosh-med": -11.8, "hit-soft": -5.8, "rise-air": -10.8, "thud-low": -3.0})
VOICE_PEAK = -6.0                      # the house limiter ceiling: the voice never peaks above it
SFX_UNDER = 5.0                        # every graphic's sound peaks 5 dB under the voice's peak: clearly audible, never louder
WHOOSH_UNDER = 14.0                    # Affan 2026-10-08: whooshes 10 dB down ("too loud"); pops/clicks keep the level he liked
ES_LEAD = {"pop-glass": 0.585, "whoosh-air": 0.14, "whoosh-light": 0.45, "vibrate": 0.34}   # measured lead-ins (5 ms RMS):
# placed untrimmed, pop-glass's real pop (0.595 s) and whoosh-light's crest landed ~0.6 s after the graphic (Rich Roll QA r1)
# 2026-10-13 (5 ms RMS: the first window within 10 dB of the file's loudest, minus 10 ms; kept when > 30 ms). tick-glass,
# focus-pull, thud-thin, blip-data and thud-low start on their transient (lead <= 0.02 s): placed untrimmed.
ES_LEAD.update({"whoosh-soft": 0.165, "shutter-film": 0.06, "whoosh-med": 0.6, "hit-soft": 0.265, "rise-air": 0.705})
TAIL = 2.0


def es(js, timeout=170):
    for k in range(12):                    # 2026-10-27: "MCP Bridge is not running" (a busy Premiere) is the same transient: up to ~2 min
        d, err = _es(js, timeout)
        if err and ("bridge_unavailable" in str(err).lower() or "bridge is not running" in str(err).lower()):
            time.sleep(5 if k < 2 else 12); continue
        if err: raise SystemExit(f"ES error: {str(err)[:500]}")
        return d
    raise SystemExit("bridge unavailable for ~2 min")


def lvl_v(db): return 10 ** ((db - 15) / 20)


def sfx_path(plan, x):
    """2026-10-27 (batch-5 reactions): a job may carry its OWN measured slices (plan["sfx_dir"], relative to the job folder): a sound is
    looked up there first, then in the shared kit (assets/sfx/epidemic). No sfx_dir = the old lookup, unchanged."""
    d = plan.get("sfx_dir")
    if d:
        q = os.path.join(plan["_dir"], d, f"{x}.wav")
        if os.path.exists(q): return q
    return os.path.join(SFX_DIR, f"{x}.wav")


def sfx_peak(plan, x):
    """the slice's sample peak (dB): the kit's measured table, else volumedetect on the file itself (a job slice is never guessed)."""
    if x in SFX_PEAK and not (plan.get("sfx_dir") and os.path.exists(os.path.join(plan["_dir"], plan["sfx_dir"], f"{x}.wav"))): return SFX_PEAK[x]
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", sfx_path(plan, x), "-af", "volumedetect", "-f", "null", "-"], capture_output=True, text=True).stderr
    return float(re.findall(r"max_volume:\s*(-?[\d.]+) dB", r)[-1])


def sfx_is_whoosh(plan, x):
    """whooshes sit WHOOSH_UNDER (Affan 2026-10-08: 10 dB down); the kit names them whoosh-*, a job slice may be called *whoosh* /
    *swish* / *swoosh*, or be listed in plan["sfx_whoosh"]."""
    return x.startswith("whoosh") or x in plan.get("sfx_whoosh", []) or (bool(plan.get("sfx_dir")) and any(k in x for k in ("whoosh", "swish", "swoosh")))


PRE = r"""
function seqByName(n){ for (var i = 0; i < app.project.sequences.numSequences; i++) if (app.project.sequences[i].name === n) return app.project.sequences[i]; return null; }
function comp(c, n){ for (var k = 0; k < c.components.numItems; k++) if (c.components[k].displayName === n) return c.components[k]; return null; }
function prop(c, cn, pn){ var m = comp(c, cn); if (!m) return null; for (var q = 0; q < m.properties.numItems; q++) if (m.properties[q].displayName === pn) return m.properties[q]; return null; }
function at(tr, t){ for (var i = 0; i < tr.clips.numItems; i++) if (Math.abs(tr.clips[i].start.seconds - t) < 0.009) return tr.clips[i]; return null; }
function setStatic(p, v){ if (p.isTimeVarying()) p.setTimeVarying(false); p.setValue(v, true); }
function bin(p, n){ for (var i = 0; i < p.children.numItems; i++){ var c = p.children[i]; if (c.type === 2 && c.name === n) return c; } return null; }
function item(p, n){ for (var i = 0; i < p.children.numItems; i++){ var c = p.children[i]; if (c.name === n && c.type !== 2) return c; } return null; }
"""


def head(plan):
    return "(function(){" + PRE + "var s = seqByName(" + json.dumps(plan["sequence"]) + "); if (!s) return 'NOSEQ';"


def load(path):
    plan = json.load(open(path, encoding="utf-8")); plan["_dir"] = os.path.dirname(os.path.abspath(path)); G.configure(plan)
    if plan.get("frame_track") is not None:                  # the showcase frame track under the MG track (2026-10-13)
        plan.setdefault("mg_track", plan["frame_track"] + 1); plan.setdefault("cap_track", plan["mg_track"] + 1)
        roles = [plan[k] for k in ("screen_track", "face_track", "frame_track", "mg_track", "cap_track")]
        if len(set(roles)) < 5: raise SystemExit(f"track roles collide (screen, face, frame, MG, captions): {roles}")
    plan.setdefault("mg_track", plan["face_track"] + 1); plan.setdefault("cap_track", plan["face_track"] + 2)   # Seq 37/38 name them
    seq = next(s for s in json.load(open(os.path.join(plan["_dir"], plan["dump"]))) if s["name"] == plan["sequence"])
    return plan, seq


def readback(plan):
    d = es(head(plan) + """var o = {v: [], a: [], nv: s.videoTracks.numTracks, na: s.audioTracks.numTracks};
for (var t = 0; t < s.videoTracks.numTracks; t++){ var tr = s.videoTracks[t]; for (var i = 0; i < tr.clips.numItems; i++){ var c = tr.clips[i];
  var sc = prop(c, 'Motion', 'Scale'), ps = prop(c, 'Motion', 'Position'), ct = prop(c, 'Motion', 'Crop Top');
  o.v.push([t, c.name, +c.start.seconds.toFixed(4), +c.end.seconds.toFixed(4), c.disabled ? 1 : 0, sc ? (sc.isTimeVarying() ? 'kf' : sc.getValue()) : null,
            ps ? (ps.isTimeVarying() ? 'kf' : ps.getValue()) : null, ct ? (ct.isTimeVarying() ? 'kf' : ct.getValue()) : null]); } }
for (var t = 0; t < s.audioTracks.numTracks; t++){ var tr = s.audioTracks[t]; for (var i = 0; i < tr.clips.numItems; i++){ var c = tr.clips[i];
  var lv = prop(c, 'Volume', 'Level'); o.a.push([t, c.name, +c.start.seconds.toFixed(4), +c.end.seconds.toFixed(4), lv ? (lv.isTimeVarying() ? 'kf' : lv.getValue()) : null]); } }
return JSON.stringify(o); })()""")
    if d == "NOSEQ": raise SystemExit("sequence not found")
    return json.loads(d) if isinstance(d, str) else d


def guard(plan, seq, tl):
    for ti in (plan["screen_track"], plan["face_track"]):
        then = [(round(c["s"], 3), round(c["e"], 3)) for c in seq["v"][ti]["clips"]]
        now = sorted((round(x[2], 3), round(x[3], 3)) for x in tl["v"] if x[0] == ti)
        if len(then) != len(now) or any(abs(a[0] - b[0]) > 0.003 or abs(a[1] - b[1]) > 0.003 for a, b in zip(then, now)):
            raise SystemExit(f"V{ti + 1} changed since the dump: re-dump before applying")


def motion_js(ti, start, m, keys=None):
    """JS for one clip: static Motion values, or baked keys [(source_t, motion)]."""
    names = ["Scale", "Position", "Crop Left", "Crop Top", "Crop Right", "Crop Bottom"]
    val = lambda mm: [mm["scale"], "[" + f"{mm['pos'][0]:.6f},{mm['pos'][1]:.6f}" + "]", mm["crop"]["L"], mm["crop"]["T"], mm["crop"]["R"], mm["crop"]["B"]]
    js = f"var c = at(s.videoTracks[{ti}], {start:.4f}); if (!c) return 'NOCLIP {ti} {start:.3f}'; var P = ["
    js += ",".join(f"prop(c,'Motion','{n}')" for n in names) + "];"
    if not keys:
        v = val(m)
        js += "".join(f"setStatic(P[{i}], {v[i]});" for i in range(6))
    else:
        js += "for (var i = 0; i < 6; i++) if (!P[i].isTimeVarying()) P[i].setTimeVarying(true);"
        for kt, mm in keys:
            v = val(mm)
            js += "".join(f"P[{i}].addKey({kt:.4f}); P[{i}].setValueAtKey({kt:.4f}, {v[i]}, true);" for i in range(6))
    return js


def _lerp_motion(a, b, u):
    return dict(scale=a["scale"] + (b["scale"] - a["scale"]) * u, pos=tuple(a["pos"][i] + (b["pos"][i] - a["pos"][i]) * u for i in (0, 1)),
                crop={k: a["crop"][k] + (b["crop"][k] - a["crop"][k]) * u for k in a["crop"]})


def leak_problems(label, keys, tol=0.5):
    """every baked key must keep the screen layer inside the panel box (tolerance 0.5 px): "leak" = a key outside BOX (layout()
    refuses), "gap" = a key whose layer does not reach a BOX edge (the source ran out); "mid" = the linear midpoint between
    two keys (what Premiere draws there) leaks: reported by --layout-check only (a fast 1/30 s zoom bends ~1 px between keys,
    as it always has)"""
    out, B = [], G.BOX
    def test(t, m, mid):
        r = G.motion_rect(m)
        if r[0] < B[0] - tol or r[1] < B[1] - tol or r[2] > B[2] + tol or r[3] > B[3] + tol:
            out.append(("mid" if mid else "leak", f"{label} @ src {t:.3f}{' (between keys)' if mid else ''}: layer {tuple(round(x, 2) for x in r)} outside the panel {B}"))
        elif not mid and (r[0] > B[0] + tol or r[1] > B[1] + tol or r[2] < B[2] - tol or r[3] < B[3] - tol):
            out.append(("gap", f"{label} @ src {t:.3f}: layer {tuple(round(x, 2) for x in r)} does not cover the panel {B}"))
    for t, m in keys: test(t, m, False)
    for (ta, ma), (tb, mb) in zip(keys, keys[1:]): test((ta + tb) / 2, _lerp_motion(ma, mb, 0.5), True)
    return out


def _overhang(msg):
    import re
    r = [float(x) for x in re.search(r"layer \(([^)]*)\)", msg).group(1).split(",")]; B = G.BOX
    return max(B[0] - r[0], B[1] - r[1], r[2] - B[2], r[3] - B[3])


def layout_jobs(plan, seq):
    """the --layout clip edits, computed OFFLINE: [(label, js)] + the leak / gap problems of every screen key"""
    si, fi = plan["screen_track"], plan["face_track"]
    scr, face = seq["v"][si]["clips"], seq["v"][fi]["clips"]
    jobs, probs = [], []
    # 1. face-only: the face clip gets his 132 framing (or a cropped punch-in), the screen clip under it is switched off
    for f in plan["face"]:
        for c in face:
            if c["s"] >= f["t0"] - 0.01 and c["e"] <= f["t1"] + 0.01:
                jobs.append((f"face {c['s']:.3f}", motion_js(fi, c["s"], G.face_motion(f.get("scale", 132), f.get("face_x"))) +
                             f"var x = at(s.videoTracks[{si}], {c['s']:.4f}); if (x) x.disabled = true;"))
        for c in scr:                     # EVERY screen piece inside the beat off (Seq 37/38: the screen sits ABOVE the face)
            if c["s"] >= f["t0"] - 0.01 and c["e"] <= f["t1"] + 0.01:
                jobs.append((f"screen off {c['s']:.3f}", f"var x = at(s.videoTracks[{si}], {c['s']:.4f}); if (!x) return 'NOSCREEN {c['s']:.3f}'; x.disabled = true;"))
    # 2. screen views
    for c in scr:
        if any(f["t0"] - 0.01 <= c["s"] and c["e"] <= f["t1"] + 0.01 for f in plan["face"]):
            continue
        v = next((v for v in plan["views"] if v["t0"] - 0.01 <= c["s"] < v["t1"] - 0.01), None)
        if not v:
            continue
        if "anim" in v or v.get("drift"):
            ts = [c["s"]]
            if "anim" in v:
                ta, d = v["anim"]; kps = plan.get("anim_kps", 30)    # 60 = a key on every frame: no between-key slip (batch 3, 2026-10-19)
                ts += [ta + k / kps for k in range(int(d * kps) + 1)] + [min(c["e"], ta + d + 0.001)]
                if "anim_out" in v:
                    tb, d2 = v["anim_out"]; ts += [tb + k / kps for k in range(int(d2 * kps) + 1)] + [min(c["e"], tb + d2 + 0.001)]
            if v.get("drift"):                      # the slow push: a key every 0.5 s across the clip piece, and its end
                ts += [c["s"] + 0.5 * k for k in range(int((c["e"] - c["s"]) / 0.5) + 1)] + [c["e"]]
            ts = sorted({round(t, 4) for t in ts if c["s"] <= t <= c["e"]})
            keys = [(c["i"] + (t - c["s"]), G.view_motion(G.view_at(plan, min(max(t, c["s"] + 0.002), c["e"] - 0.002)))) for t in ts]
            # a clip's ends touch the face-only beats around it (the dump rounds to 1 ms): read the view 2 ms INSIDE the clip
            kind = "+".join(x for x in ("anim" if "anim" in v else "", "drift" if v.get("drift") else "") if x)
            label = f"view {c['s']:.3f} {v['view']} ({kind}, {len(keys)} keys)"
            probs += leak_problems(label, keys)
            jobs.append((label, motion_js(si, c["s"], None, keys)))
        else:
            m = G.view_motion(G.named(plan, v["view"]))
            probs += leak_problems(f"view {c['s']:.3f} {v['view']}", [(c["i"], m)])
            jobs.append((f"view {c['s']:.3f} {v['view']}", motion_js(si, c["s"], m)))
    return jobs, probs


def layout(plan, seq):
    jobs, probs = layout_jobs(plan, seq)
    leaks = [x for k, x in probs if k == "leak"]
    if leaks: raise SystemExit("the screen would leak out of the panel:\n  " + "\n  ".join(leaks[:20]))
    tl = readback(plan); guard(plan, seq, tl)
    for label, js in jobs:
        r = es(head(plan) + js + " return 'ok'; })()")
        print(f"  {label}: {r}")
        if r != "ok": raise SystemExit(r)
    print(f"layout: {len(jobs)} clip edits")


LOCK = os.path.join(REPO, "lanes", "premiere", "ACTIVE-WINDOW.lock")


def _qg():
    """lanes/premiere/quietgate.py (2026-11-14): while lanes/premiere/QUIET-MODE exists, every active-sequence switch, playhead
    move and save waits until Affan is away from the machine, and his own sequence + playhead are put back afterwards."""
    p = os.path.join(REPO, "lanes", "premiere")
    if p not in sys.path: sys.path.insert(0, p)
    import quietgate
    return quietgate


def _quiet_wait(who):
    try: return _qg().wait(who=who)
    except Exception as e:
        if os.path.exists(os.path.join(REPO, "lanes", "premiere", "QUIET-MODE")):
            raise SystemExit(f"QUIET-MODE: cannot confirm Affan is away ({e}): refusing to switch his view")
        return None


def _quiet():
    return os.path.exists(os.path.join(REPO, "lanes", "premiere", "QUIET-MODE"))


def _quiet_restore(snap):
    if snap:
        try: _qg().restore(snap)
        except Exception as e: print("  quietgate restore failed:", e)


class active_window:
    """Cross-session lock around anything that switches Premiere's ACTIVE sequence (QE razors, addTracks, audio-polish,
    grabs): another Claude session working in the same project waits while the file exists (Affan 2026-10-08)."""
    def __init__(self, who): self.who = who
    def __enter__(self):
        self._snap = _quiet_wait(self.who)          # quiet mode: wait for Affan to be away BEFORE taking the lock
        for _ in range(360):
            try:
                fd = os.open(LOCK, os.O_CREAT | os.O_EXCL | os.O_WRONLY); os.write(fd, (f"{self.who} {time.ctime()}" + chr(10)).encode()); os.close(fd); return self
            except FileExistsError:
                if time.time() - os.path.getmtime(LOCK) > 900: os.remove(LOCK); continue      # a stale lock (15 min)
                time.sleep(5)
        raise SystemExit(f"{LOCK} held for 30 min: " + open(LOCK).read())
    def __exit__(self, *a):
        try: os.remove(LOCK)
        except FileNotFoundError: pass
        _quiet_restore(getattr(self, "_snap", None))


def open_window(plan):
    """2026-10-27 (two sessions in ABW10): switch to OUR sequence by id, wait 1.5 s, then PROVE the switch with two independent reads
    (DOM activeSequence.sequenceID and QE getActiveSequence().name) plus a fingerprint (its A1 clip count), and refuse otherwise:
    lab-notes 2026-10-08 (an activeSequence change can read back yet not switch). Call it INSIDE active_window. Returns {prev, prevName}."""
    nm = json.dumps(plan["sequence"])
    st = es("(function(){" + PRE + "var prev = app.project.activeSequence; var s = seqByName(" + nm + "); if (!s) return JSON.stringify({err: 'NOSEQ'});"
            "app.project.openSequence(s.sequenceID); return JSON.stringify({prev: prev ? prev.sequenceID : null, prevName: prev ? prev.name : null, want: s.sequenceID}); })()")
    st = st if isinstance(st, dict) else json.loads(st)
    if st.get("err"): raise SystemExit(st["err"])
    time.sleep(1.5); prove(plan, st)
    print("  window open (proven), was:", st.get("prevName"))
    return st


def prove(plan, st):
    nm = json.dumps(plan["sequence"])
    c = es("(function(){" + PRE + "var a = app.project.activeSequence; app.enableQE(); var q = qe.project.getActiveSequence(); var s = seqByName(" + nm + ");"
           "return JSON.stringify({dom: a ? a.sequenceID : null, domName: a ? a.name : null, qe: q ? q.name : null, a1: a ? a.audioTracks[0].clips.numItems : -1,"
           " want_a1: s.audioTracks[0].clips.numItems}); })()")
    c = c if isinstance(c, dict) else json.loads(c)
    if c["dom"] != st["want"] or c["qe"] != plan["sequence"] or c["a1"] != c["want_a1"]:
        if st.get("prev"): es("(function(){ app.project.openSequence(" + json.dumps(st["prev"]) + "); return 'back'; })()")
        raise SystemExit(f"active sequence NOT proven ({c}): nothing done, the previous one reopened")


def close_window(st):
    if st.get("prev"):
        # 2026-11-14: hand his view back ONLY if OUR sequence is still active (never yank him off one he picked meanwhile)
        back = es("(function(){ var a = app.project.activeSequence; if (a && a.sequenceID === " + json.dumps(st.get("want")) + ") "
                  "app.project.openSequence(" + json.dumps(st["prev"]) + "); return app.project.activeSequence.name; })()")
        print("  restored active sequence:", back, "(was", st.get("prevName"), ")")


def razor_times(plan):
    """every face-only beat edge and view edge, snapped to the 60 fps grid (layout styles WHOLE clips, so each edge must be a cut)"""
    ts = {f[k] for f in plan["face"] for k in ("t0", "t1")} | {v["t0"] for v in plan["views"]}
    return sorted({round(round(t * 60) / 60, 4) for t in ts if 0.02 < t < plan["end"] - 0.02})


def razor(plan):
    """QE razors on the face + screen tracks at razor_times(): ONE locked active window, his sequence restored in a finally."""
    T = razor_times(plan)
    with active_window(f"reactions/apply.py --razor {plan['sequence']}"):
        st = open_window(plan)
        try:
            r = es("(function(){" + PRE + "var s = app.project.activeSequence; if (s.name !== " + json.dumps(plan["sequence"]) + ") return 'WRONG ' + s.name;"
                   "app.enableQE(); var q = qe.project.getActiveSequence(); if (q.name !== " + json.dumps(plan["sequence"]) + ") return 'WRONG QE ' + q.name;"
                   "var fps = 254016000000 / parseInt(s.timebase, 10), base = Math.round(fps);"
                   "function p(n){ return n < 10 ? '0' + n : '' + n; }"
                   "function tc(T){ var f = Math.round(T * fps); return p(Math.floor(f / (base * 3600))) + ':' + p(Math.floor(f / (base * 60)) % 60) + ':' + p(Math.floor(f / base) % 60) + ':' + p(f % base); }"
                   "function inside(tr, t){ for (var k = 0; k < tr.clips.numItems; k++){ var c = tr.clips[k]; if (c.start.seconds < t - 0.004 && c.end.seconds > t + 0.004) return true; } return false; }"
                   f"var T = {json.dumps(T)}, V = {json.dumps([plan['face_track'], plan['screen_track']])}, n = 0;"
                   "for (var i = 0; i < T.length; i++) for (var k = 0; k < V.length; k++) if (inside(s.videoTracks[V[k]], T[i])) { q.getVideoTrackAt(V[k]).razor(tc(T[i])); n++; }"
                   "return 'razors ' + n + ' at ' + T.length + ' edges'; })()", timeout=600)
            print("  ", r)
            if str(r).startswith("WRONG"): raise SystemExit(r)
        finally:
            close_window(st)


# KIT: Premiere frame grabs removed (they moved his playhead). Frames: offgrab.py (offline, from the dump).


def window(plan):
    with active_window(f"reactions/apply.py {plan['sequence']}"):
        _window(plan)


def _window(plan):
    need_v = max(plan["mg_track"], plan["cap_track"], plan.get("frame_track") or 0) + 1
    st = open_window(plan)
    lk = None
    try:
        r = es("(function(){" + PRE + "var s = app.project.activeSequence; app.enableQE(); var q = qe.project.getActiveSequence();"
               "if (s.name !== " + json.dumps(plan["sequence"]) + " || q.name !== s.name) return JSON.stringify({err: 'WRONG ' + s.name + ' / ' + q.name});"
               "var n = 0, add = " + str(need_v) + " - s.videoTracks.numTracks; if (add > 0) { q.addTracks(add, s.videoTracks.numTracks, 0, 0, 0, 0, 0); n = add; }"
               "return JSON.stringify({active: s.name, added: n, nv: s.videoTracks.numTracks}); })()")
        r = r if isinstance(r, dict) else json.loads(r); print("  tracks:", r)
        if r.get("err"): raise SystemExit(r["err"])
        lk = es(head(plan) + "var l = s.audioTracks[0].isLocked(); if (l) s.audioTracks[0].setLocked(0); return l ? 'was-locked' : 'unlocked'; })()")
        print("  A1:", lk)
        if plan.get("voice_gain") is not None:
            prove(plan, st)                       # audio-polish.py works on the ACTIVE sequence: prove it is ours right before and after
            p = subprocess.run(["uv", "run", os.path.join(REPO, "lanes", "premiere", "audio-polish.py"), plan["_dir"], "--apply", "--gain", str(int(plan["voice_gain"]))],
                               capture_output=True, text=True, timeout=900)
            print("  audio-polish:", (p.stdout + p.stderr).strip()[-400:])
            for a_, b_, g_ in plan.get("voice_gain_ranges", []):     # 2026-10-27: level-matched inserts (their Short / our samples
                prove(plan, st)                                       # sit ~8 dB over his voice in the OBS mix): their own gain
                p = subprocess.run(["uv", "run", os.path.join(REPO, "lanes", "premiere", "audio-polish.py"), plan["_dir"], "--apply", "--gain", str(int(g_)),
                                    "--range", f"{a_ - 0.005:.4f}", f"{b_ - 0.005:.4f}"], capture_output=True, text=True, timeout=600)
                print(f"  audio-polish {a_:.3f}-{b_:.3f} {g_:+d} dB:", (p.stdout + p.stderr).strip()[-200:])
            prove(plan, st)
    finally:
        if lk == "was-locked":
            print("  A1 re-locked:", es(head(plan) + "s.audioTracks[0].setLocked(1); return String(s.audioTracks[0].isLocked()); })()"))
        close_window(st)


def overlays(plan):
    tl = readback(plan)
    mg_t, cap_t, fr_t = plan["mg_track"], plan["cap_track"], plan.get("frame_track")
    if any(g["kind"] == "showcase" for g in plan["graphics"]) and fr_t is None: raise SystemExit("a showcase graphic needs plan.frame_track")
    need = max(mg_t, cap_t, fr_t or 0) + 1
    if tl["nv"] < need: raise SystemExit(f"need {need} video tracks, have {tl['nv']}: run --window first")
    od = os.path.join(plan["_dir"], "overlays")
    binname = "Reactions - " + plan["job"]
    capf = plan.get("captions_file", "captions.mov")     # 2026-11-02: a re-rendered caption layer gets a NEW name (Premiere holds the old file)
    files = [(capf, os.path.join(od, capf))] + [(f"{g['id']}.mov", os.path.join(od, "mg", f"{g['id']}.mov")) for g in plan["graphics"]]
    sfx = sorted({g[k] for g in plan["graphics"] for k in ("sfx", "sfx2", "step_sfx") if g.get(k)} | {c[1] for g in plan["graphics"] for c in g.get("cues", [])}
                 | {tk[2] for g in plan["graphics"] for tk in g.get("ticks", []) if len(tk) > 2 and tk[2]})
    files += [(f"{x}.wav", sfx_path(plan, x)) for x in sfx]
    mus = os.path.join(plan["_dir"], plan["music"]["file"]); files.append((os.path.basename(mus), mus))
    for name, path in files:
        if not os.path.exists(path): raise SystemExit(f"missing {path}")
        r = es("(function(){" + PRE + "var b = bin(app.project.rootItem, " + json.dumps(binname) + "); if (!b) { app.project.rootItem.createBin(" + json.dumps(binname) + "); b = bin(app.project.rootItem, " + json.dumps(binname) + "); }"
               "if (item(b, " + json.dumps(name) + ")) return 'have'; var f = new File(" + json.dumps(path.replace("\\", "/")) + "); if (!f.exists) return 'NOFILE';"
               "app.project.importFiles([f.fsName], true, b, false); return item(b, " + json.dumps(name) + ") ? 'imported' : 'MISSING'; })()", timeout=240)
        print(f"  import {name}: {r}")
        if r not in ("have", "imported"): raise SystemExit(r)
    getitem = "var b = bin(app.project.rootItem, " + json.dumps(binname) + "); var it = item(b, NAME); if (!it) return 'NOITEM';"
    def place(track_js, name, t, dur=None, src_in=None):
        js = head(plan) + getitem.replace("NAME", json.dumps(name)) + f"var tr = {track_js}; var ex = at(tr, {t:.4f}); if (ex && ex.name === it.name) return 'exists'; if (ex) ex.remove(false, false);"
        if src_in is not None:
            js += f"it.setInPoint({src_in:.4f}, 4); it.setOutPoint({src_in + dur:.4f}, 4);"
        js += f"tr.overwriteClip(it, {t + 1e-4:.4f});"
        if src_in is not None:
            js += "it.clearInPoint(4); it.clearOutPoint(4);"
        js += f"var c = at(tr, {t:.4f}); if (!c) return 'NOCLIP'; return 'ok ' + c.start.seconds.toFixed(3) + '-' + c.end.seconds.toFixed(3); }})()"
        r = es(js); print(f"  place {name} @ {t:.3f}: {r}")
        if not (isinstance(r, str) and (r.startswith("ok") or r == "exists")): raise SystemExit(r)
    place(f"s.videoTracks[{cap_t}]", capf, 0.0)
    for g in plan["graphics"]:                           # the showcase frame on its own track under the MG track
        place(f"s.videoTracks[{fr_t if g['kind'] == 'showcase' else mg_t}]", f"{g['id']}.mov", g["t0"])
    # SFX on A2, each at its graphic's start (and the second beat where a graphic has one); level: peak SFX_UNDER under the voice peak
    cues = []
    for g in plan["graphics"]:
        if g.get("sfx"): cues.append((g["t0"] + g.get("sfx_lead", 0.0), g["sfx"]))
        if g.get("sfx2"): cues.append((g.get("line2_at", g["t0"]), g["sfx2"]))
        if g.get("step_sfx"): cues += [(st, g["step_sfx"]) for st, _ in g["steps"][1:]]
        cues += [(c[0], c[1], c[2]) if len(c) > 2 else (c[0], c[1]) for c in g.get("cues", [])]   # explicit beats; 2026-10-27: [t, sound, dB] = a per-cue level MEASURED by tools5/sfxgate5.py
        cues += [(tk[0], tk[2]) for tk in g.get("ticks", []) if len(tk) > 2 and tk[2]]     # a scrub tick's own sound
    # 2026-10-13: overlapping sounds on ONE track get chopped by overwriteClip (the earlier one is cut mid-sound and its tail is
    # left as a stray fragment that starts mid-waveform): sounds go to A2 or A4, whichever is free at the cue (plan "sfx_tracks").
    # Every re-run first clears OUR SFX clips from those tracks, so placement is idempotent.
    if plan.get("sfx_gated"):
        nolvl = [c for g in plan["graphics"] for c in g.get("cues", []) if len(c) < 3]
        if nolvl or any(g.get(k) for g in plan["graphics"] for k in ("sfx", "sfx2", "step_sfx")):
            raise SystemExit(f"sfx_gated plan: {len(nolvl)} cue(s) without a measured level (re-run tools5/sfxgate5.py --write LAST, after build_plan)")
    trks = plan.get("sfx_tracks", [1, 3]); names = json.dumps([f"{x}.wav" for x in sfx])
    r = es(head(plan) + f"""var N = {names}, n = 0, T = {json.dumps(trks)};
for (var k = 0; k < T.length; k++) {{ var tr = s.audioTracks[T[k]]; for (var i = tr.clips.numItems - 1; i >= 0; i--) {{ var c = tr.clips[i];
  for (var j = 0; j < N.length; j++) if (c.name === N[j]) {{ c.remove(false, false); n++; break; }} }} }}
return 'cleared ' + n; }})()""")
    print("  sfx tracks", [f"A{t + 1}" for t in trks], r)
    flen = {x: float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", sfx_path(plan, x)],
                                    capture_output=True, text=True).stdout.strip()) for x in sfx}
    busy = {t: -1e9 for t in trks}
    for cue in sorted(cues, key=lambda c: (c[0], c[1])):
        t, x = cue[0], cue[1]; dbx = cue[2] if len(cue) > 2 else None
        lead = ES_LEAD.get(x, 0.0); dur = flen[x] - lead
        free = [k for k in trks if busy[k] <= t + 1e-3]
        k = free[0] if free else min(trks, key=lambda q: busy[q])
        if not free:                               # three at once: END the sound that frees first exactly here (never split it:
            # a split leaves its tail as a stray mid-waveform fragment)
            r = es(head(plan) + f"""var tr = s.audioTracks[{k}], n = 0;
for (var i = 0; i < tr.clips.numItems; i++) {{ var c = tr.clips[i]; if (c.start.seconds < {t:.4f} - 0.005 && c.end.seconds > {t:.4f} + 0.005) {{ c.end = {t:.4f}; n++; }} }}
return 'ended ' + n; }})()""")
            print(f"    ! {x} @ {t:.3f}: A2 and A4 both sounding: the one that frees first (A{k + 1}) {r} here")
        busy[k] = t + dur
        if lead:                                   # trimmed so the transient lands ON the cue
            place(f"s.audioTracks[{k}]", f"{x}.wav", t, dur=dur, src_in=lead)
        else:
            place(f"s.audioTracks[{k}]", f"{x}.wav", t)
        db = dbx if dbx is not None else max(-30.0, min(15.0, VOICE_PEAK - (WHOOSH_UNDER if sfx_is_whoosh(plan, x) else SFX_UNDER) - sfx_peak(plan, x)))   # 2026-10-27: -30 (was -15): a -1 dBFS job slice whoosh needs -19
        r = es(head(plan) + f"var c = at(s.audioTracks[{k}], {t:.4f}); if (!c) return 'NOCLIP'; var p = prop(c, 'Volume', 'Level'); setStatic(p, {lvl_v(db)}); return 'lvl ' + p.getValue(); }})()")
        print(f"    A{k + 1} level {x} {db:+.1f} dB: {r}")
    # music bed on A3: from its sustained entrance, flat, the level through the FIRST key (lab-notes), 2 s tail fade
    m = plan["music"]; end = plan["end"]; si = m.get("source_in", 0.0); name = os.path.basename(mus)
    v, vmin = lvl_v(m["bed_db"]), lvl_v(-96)
    gaps = sorted(m.get("gaps", []))
    if gaps:
        # 2026-10-27: Affan's own v1 edit carried into v2: NO bed under these sample plays. The pieces keep the CONTINUOUS source
        # in-points (what his razor + delete left), each flat at bed_db through its first key, the 2 s tail fade on the last only.
        # Every re-run first removes the bed's pieces from A3, so it stays idempotent.
        print("  bed:", es(head(plan) + f"var tr = s.audioTracks[2], n = 0; for (var i = tr.clips.numItems - 1; i >= 0; i--) {{ if (tr.clips[i].name === {json.dumps(name)}) {{ tr.clips[i].remove(false, false); n++; }} }} return 'cleared ' + n; }})()"))
        for k, (a, b) in enumerate(bed_pieces(plan)):
            place("s.audioTracks[2]", name, a, dur=b - a, src_in=si + a)
            tail = (f"p.addKey(ke - {TAIL}); p.setValueAtKey(ke - {TAIL}, {v}, true); p.addKey(ke - 0.001); p.setValueAtKey(ke - 0.001, {vmin}, true);"
                    if k == len(gaps) else f"p.addKey(ke - 0.001); p.setValueAtKey(ke - 0.001, {v}, true);")
            r = es(head(plan) + f"""var c = at(s.audioTracks[2], {a:.4f}); if (!c) return 'NOCLIP'; if (Math.abs(c.end.seconds - {b:.4f}) > 0.004) c.end = {b:.4f};
var p = prop(c, 'Volume', 'Level'); p.setTimeVarying(true); var k0 = c.inPoint.seconds, ke = k0 + (c.end.seconds - c.start.seconds);
p.addKey(k0); p.setValueAtKey(k0, {v}, true); {tail}
return 'bed piece ' + c.start.seconds.toFixed(3) + '-' + c.end.seconds.toFixed(3) + ' in ' + k0.toFixed(3); }})()""")
            print("  music:", r)
        safe_save(); return
    place("s.audioTracks[2]", name, 0.0, dur=end, src_in=si)
    r = es(head(plan) + f"""var c = at(s.audioTracks[2], 0); if (!c) return 'NOCLIP'; if (Math.abs(c.end.seconds - {end:.4f}) > 0.02) c.end = {end:.4f};
var p = prop(c, 'Volume', 'Level'); p.setTimeVarying(true); var k0 = c.inPoint.seconds, ke = k0 + (c.end.seconds - c.start.seconds);
p.addKey(k0); p.setValueAtKey(k0, {v}, true); p.addKey(ke - {TAIL}); p.setValueAtKey(ke - {TAIL}, {v}, true); p.addKey(ke - 0.001); p.setValueAtKey(ke - 0.001, {vmin}, true);
return 'bed ' + c.start.seconds.toFixed(3) + '-' + c.end.seconds.toFixed(3) + ' in ' + k0.toFixed(3); }})()""")
    print("  music:", r)
    safe_save()


def bed_pieces(plan):
    """[(start, end)] of the music bed: one piece, or the pieces around plan.music.gaps (Affan's no-bed spans)"""
    g = sorted(plan["music"].get("gaps", [])); e = [0.0] + [x for q in g for x in q] + [plan["end"]]
    return [(e[i], e[i + 1]) for i in range(0, len(e), 2)]


def safe_save():
    """2026-10-27: never save while ANOTHER session holds ACTIVE-WINDOW.lock (its half-done window would be saved mid-edit): wait for it
    (max 10 min), then save. A save inside OUR OWN window (audio-polish.py) is ours and needs no wait."""
    for _ in range(120):
        if not os.path.exists(LOCK) or time.time() - os.path.getmtime(LOCK) > 900: break      # missing or stale (15 min)
        time.sleep(5)
    else: print("  ! ACTIVE-WINDOW.lock still held after 10 min: saving anyway:", open(LOCK).read().strip())
    snap = _quiet_wait("apply.py save")             # a save freezes his UI for seconds: only while he is away
    print("  save:", es("(function(){ app.project.save(); return 'saved'; })()"))
    _quiet_restore(snap)


def verify(plan, seq):
    tl = readback(plan); bad = []
    si, fi = plan["screen_track"], plan["face_track"]
    V = lambda t: [x for x in tl["v"] if x[0] == t]
    for f in plan["face"]:
        for c in seq["v"][fi]["clips"]:
            if c["s"] >= f["t0"] - 0.01 and c["e"] <= f["t1"] + 0.01:
                x = next((x for x in V(fi) if abs(x[2] - c["s"]) < 0.005), None)
                if not x or abs(x[5] - f.get("scale", 132)) > 0.01: bad.append(f"face {c['s']}: {x}")
                y = next((y for y in V(si) if abs(y[2] - c["s"]) < 0.005), None)
                if y and not y[4]: bad.append(f"screen under face {c['s']} still enabled")
    caps = [x for x in V(plan["cap_track"]) if x[1] == plan.get("captions_file", "captions.mov")]
    if len(caps) != 1 or abs(caps[0][3] - plan["end"]) > 0.05: bad.append(f"captions: {caps}")
    for g in plan["graphics"]:
        tr = plan.get("frame_track") if g["kind"] == "showcase" else plan["mg_track"]
        if not [x for x in V(tr) if x[1] == f"{g['id']}.mov" and abs(x[2] - g["t0"]) < 0.01 and abs(x[3] - g["t1"]) < 0.03]:
            bad.append(f"graphic {g['id']} missing/misplaced" + (" (frame track)" if g["kind"] == "showcase" else ""))
    mus = sorted([x for x in tl["a"] if x[0] == 2], key=lambda x: x[2]); want = bed_pieces(plan)
    if len(mus) != len(want) or any(abs(x[2] - a) > 0.05 or abs(x[3] - b) > 0.05 for x, (a, b) in zip(mus, want)): bad.append(f"music: {mus} vs {want}")
    for b in bad: print("  ✗", b)
    trks = plan.get("sfx_tracks", [1, 3])
    want = sum(bool(g.get("sfx")) + bool(g.get("sfx2")) + (len(g["steps"]) - 1 if g.get("step_sfx") else 0) + len(g.get("cues", []))
               + sum(1 for tk in g.get("ticks", []) if len(tk) > 2 and tk[2]) for g in plan["graphics"])
    have = len([x for x in tl["a"] if x[0] in trks])
    if have != want: bad.append(f"sfx: {have} clips on " + "/".join(f"A{t + 1}" for t in trks) + f", the plan has {want} cues")
    for b in bad[-1:] if have != want else []: print("  ✗", b)
    print(f"verify {plan['sequence']}: {len(bad)} problem(s); tracks V{tl['nv']} A{tl['na']}; sfx " + ", ".join(f"A{t + 1} {len([x for x in tl['a'] if x[0] == t])}" for t in trks))
    return not bad


if __name__ == "__main__":
    a = sys.argv[1:]
    plan, seq = load(a[0])
    if "--layout-check" in a:                               # offline: nothing is sent to Premiere
        jobs, probs = layout_jobs(plan, seq)
        nk = sum(js.count("addKey") // 6 for _, js in jobs)
        for k, x in probs: print(f"  {k.upper():4s} {x}")
        print(f"layout-check: {len(jobs)} clip edits, {nk} keys; {sum(k == 'leak' for k, _ in probs)} leak(s) at keys, "
              f"{sum(k == 'mid' for k, _ in probs)} between keys (max {max([0.0] + [_overhang(x) for k, x in probs if k == 'mid']):.2f} px), {sum(k == 'gap' for k, _ in probs)} gap(s)")
        sys.exit(1 if any(k == "leak" for k, _ in probs) else 0)
    if "--razor" in a: razor(plan)
    if "--layout" in a: layout(plan, seq)
    if "--window" in a: window(plan)
    if "--overlays" in a: overlays(plan)
    if "--verify" in a: sys.exit(0 if verify(plan, seq) else 1)

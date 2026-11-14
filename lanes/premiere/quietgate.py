#!/usr/bin/env python3
"""quietgate.py: never disturb Affan in Premiere. While lanes/premiere/QUIET-MODE exists, every ExtendScript WRITE waits
until he is away from the machine, and anything that switches the active sequence waits longer (2026-11-14: he edits his
AW Shorts in the same Premiere project while the reaction batch runs; "you are constantly moving the playhead ... do it in
your own sequence and let me edit in my own sequence, don't disturb me").

  python lanes/premiere/quietgate.py status                         # quiet mode? idle seconds, his sequence + playhead
  python lanes/premiere/quietgate.py wait [--idle 150]               # block until he is idle and not playing back
  python lanes/premiere/quietgate.py run [--idle 150] -- <cmd ...>   # wait, run cmd, then hand his view back if we hold it

Where it bites (one chokepoint): projects/_onyx-batch-2026-10/reactions/tools/pp.py es() calls gate(script) before every
ExtendScript it sends. Reads pass at once. A WRITE (DOM edits, imports, saves) waits for IDLE_LIGHT s of no input; a HEAVY
one (switches the active sequence, QE, playhead, import dialog, save, razor, addTracks) waits for IDLE_HEAVY s AND his
playhead standing still (he is not playing back). Once approved, writes pass for HOLD s, and keep passing while one of OUR
sequences is the active one (a window in progress is finished, never left half-done on his screen). The gate FAILS CLOSED:
if it cannot read his state in quiet mode, the write is refused.
restore() hands his view back ONLY when one of OUR sequences is still active: it never touches his playhead and never
yanks him off a sequence he picked himself. OUR sequences = names matching QUIET_OURS (default: "reaction").
QC frames come from projects/_onyx-batch9-2026-11/reactions/offgrab.py (no Premiere); window grabs are refused.
"""
import ctypes, ctypes.wintypes, json, os, re, subprocess, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
FLAG = os.path.join(HERE, "QUIET-MODE")
TOOLS = os.path.join(REPO, "projects", "_onyx-batch-2026-10", "reactions", "tools")
IDLE_LIGHT, IDLE_HEAVY, HOLD = 60, 150, 90
OURS = re.compile(os.environ.get("QUIET_OURS", r"reaction"), re.I)

WRITE = re.compile(r"openSequence\(|activeSequence\s*=(?!=)|enableQE\(|setPlayerPosition\(|importFiles\(|\.save\(|saveAs\("
                   r"|createNewSequence|addTracks\(|overwriteClip\(|insertClip\(|\.remove\(|\.move\(|setInPoint\(|setOutPoint\("
                   r"|clearInPoint\(|clearOutPoint\(|setValue\(|setValueAtKey\(|addKey\(|removeKey|setTimeVarying\(|setMute\("
                   r"|setLocked\(|\.start\s*=(?!=)|\.end\s*=(?!=)|razor\(|clone\(|createBin\(|deleteBin\(|moveBin\(|setColorLabel\("
                   r"|setSelected\(|exportFramePNG\(|setScaleToFrameSize\(|addVideoEffect\(|addAudioEffect\(|\.name\s*=(?!=)"
                   r"|setOverride|exportAsMediaDirect|changeMediaPath\(|attachProxy\(|setStartTime\(|setInterpretation")
HEAVY = re.compile(r"openSequence\(|activeSequence\s*=(?!=)|enableQE\(|setPlayerPosition\(|importFiles\(|\.save\(|saveAs\("
                   r"|createNewSequence|addTracks\(|exportFramePNG\(|razor\(|setScaleToFrameSize\(|addVideoEffect\("
                   r"|addAudioEffect\(")
_ok_until = 0.0


class _LII(ctypes.Structure):
    _fields_ = [("cbSize", ctypes.wintypes.UINT), ("dwTime", ctypes.wintypes.DWORD)]


def idle_seconds():
    lii = _LII()
    lii.cbSize = ctypes.sizeof(_LII)
    if not ctypes.windll.user32.GetLastInputInfo(ctypes.byref(lii)):
        raise RuntimeError("GetLastInputInfo failed")
    return ((ctypes.windll.kernel32.GetTickCount() - lii.dwTime) & 0xFFFFFFFF) / 1000.0


def quiet_on():
    return os.path.exists(FLAG)


def _raw_es(js, timeout=60):
    """the bridge WITHOUT the gate (the gate's own reads must not recurse into it)"""
    if TOOLS not in sys.path:
        sys.path.insert(0, TOOLS)
    import pp
    for k in range(8):
        d, err = pp._es_raw(js, timeout) if hasattr(pp, "_es_raw") else pp.es(js, timeout)
        if err and ("bridge_unavailable" in str(err).lower() or "bridge is not running" in str(err).lower()):
            time.sleep(5 if k < 2 else 12)
            continue
        if err:
            raise RuntimeError(f"ES error: {str(err)[:300]}")
        return d
    raise RuntimeError("bridge unavailable")


def view():
    """his active sequence and playhead: a DOM read, harmless while he works"""
    r = _raw_es("(function(){ var s = app.project.activeSequence; if (!s) return JSON.stringify({id: null});"
                " var p = s.getPlayerPosition(); return JSON.stringify({id: s.sequenceID, name: s.name, ticks: String(p.ticks)}); })()")
    return r if isinstance(r, dict) else json.loads(r)


def ours(v):
    return bool(v and v.get("name") and OURS.search(v["name"]))


def wait(idle=IDLE_HEAVY, who="", poll=10, log_every=300, still=True):
    """block until he is away; returns his view snapshot (None when quiet mode is off). Raises when it cannot tell."""
    if not quiet_on():
        return None
    t0, last_log = time.time(), 0.0
    while True:
        if not quiet_on():
            return None
        s = idle_seconds()
        if s >= idle:
            a = view()
            if not still:
                return a
            time.sleep(2.0)
            b = view()
            if a.get("id") == b.get("id") and a.get("ticks") == b.get("ticks") and idle_seconds() >= idle:
                print(f"  quietgate: Affan away {idle_seconds():.0f} s, his playhead still ({b.get('name')!r}): go ({who})",
                      flush=True)
                return b
        if time.time() - last_log > log_every:
            print(f"  quietgate: waiting for Affan to step away (idle {s:.0f}/{idle} s, waited "
                  f"{(time.time() - t0) / 60:.0f} min) ({who})", flush=True)
            last_log = time.time()
        time.sleep(poll)


def gate(script, who=""):
    """called by pp.es() before every ExtendScript: reads pass; writes wait for him (see the module doc). Raises to refuse."""
    global _ok_until
    if not quiet_on() or not WRITE.search(script):
        return
    if time.time() < _ok_until:
        return
    v = view()
    if ours(v):                      # one of OUR sequences is active: a window is in progress, finish it
        _ok_until = time.time() + HOLD
        return
    heavy = bool(HEAVY.search(script))
    wait(IDLE_HEAVY if heavy else IDLE_LIGHT, who=who or ("heavy write" if heavy else "write"), still=heavy)
    _ok_until = time.time() + HOLD


def restore(snap=None):
    """hand his view back only if OUR sequence is still the active one; never touch a playhead"""
    try:
        v = view()
    except Exception as e:
        print("  quietgate restore: cannot read the active sequence:", e, flush=True)
        return "unknown"
    if not ours(v):
        return "his view untouched (" + str(v.get("name")) + ")"
    if snap and snap.get("id") and not ours(snap):
        r = _raw_es("(function(){ app.project.openSequence(" + json.dumps(snap["id"]) + "); var a = app.project.activeSequence;"
                    " return a ? a.name : 'none'; })()")
        print("  quietgate: handed his view back ->", r, flush=True)
        return r
    print("  quietgate: OUR sequence is still active and there is no snapshot of his: left as is (", v.get("name"), ")",
          flush=True)
    return "no snapshot"


def main():
    a = sys.argv[1:]
    if not a or a[0] not in ("status", "wait", "run"):
        sys.exit(__doc__)
    idle = int(a[a.index("--idle") + 1]) if "--idle" in a else IDLE_HEAVY
    if a[0] == "status":
        print(json.dumps({"quiet_mode": quiet_on(), "idle_s": round(idle_seconds()), "his_view": view()}))
        return
    if a[0] == "wait":
        wait(idle, who="cli")
        return
    cmd = a[a.index("--") + 1:] if "--" in a else []
    if not cmd:
        sys.exit("run needs -- <cmd ...>")
    snap = wait(idle, who=" ".join(cmd)[:80])
    if snap is None:
        snap = view()
    try:
        rc = subprocess.call(cmd)
    finally:
        restore(snap)
    sys.exit(rc)


if __name__ == "__main__":
    main()

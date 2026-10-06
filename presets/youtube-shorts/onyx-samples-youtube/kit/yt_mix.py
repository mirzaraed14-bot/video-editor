"""yt_mix.py: the sound of a YouTube-look sample (README § 8) -> <job>/yt/work/mix.wav

  python presets/youtube-shorts/onyx-samples-youtube/kit/yt_mix.py projects/<job>

Reads `<job>/yt/spec.json` → "audio": {
  "voice": "outputs/<job>.mp4"                    the approved cut (its audio, untouched apart from gain),
  "bed": "yt/assets/audio/bed.wav", "bed_in": 0   optional music bed, continuous, cut on the last frame (no fade),
  "bed_under_lu": 13.6, "turn_t": <s>, "turn_lift_db": 2.0     the bed sits 13.6 LU under the voice IN EVERY 3 s WINDOW
         (a smooth gain curve from the bed's own short-term loudness: a track that builds would otherwise drift 4-5 LU
         either side, QA r2), +2 dB from the turn (a 100 ms ramp, never a step),
  "sfx": [{"file": "assets/sfx/UI Save.wav", "lead": 0.281, "t": <s>, "gain_db": -22}]   designed sounds (repo-relative file,
         `lead` = leading silence to trim, `t` = audible onset), each ≥ 15 LU under the voice,
  "target_i": -12, "target_tp": -1.5,
  "mute": [[t0, t1], ...]          optional: voice ranges silenced (profanity), with 10 ms ramps
}
Master: ONE static gain to the target loudness into an oversampled peak limiter (never loudnorm: its "linear" mode falls back
to dynamic when a peak needs limiting, and pumps). The gain is re-trimmed so the limited result lands on the target. The limiter
runs with latency compensation (else it delays the mix 5 ms and the end fade is trimmed off: a click on every loop), and a
10 ms fade-out follows it.
"""
import json, os, re, subprocess, sys
import numpy as np

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:
        pass

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", ".."))


def lufs(path):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", path, "-af", "ebur128=peak=true", "-f", "null", "-"],
                       capture_output=True, text=True).stderr
    return float(re.findall(r"I:\s+(-?[\d.]+) LUFS", r)[-1]), float(re.findall(r"Peak:\s+(-?[\d.]+) dBFS", r)[-1])


def short_term(path):
    """BS.1770 short-term loudness (3 s window) every 0.1 s, as (centre_time, LUFS) arrays."""
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", path, "-af",
                        "ebur128=metadata=1,ametadata=mode=print:key=lavfi.r128.S:file=-", "-f", "null", "-"],
                       capture_output=True, text=True).stdout
    ts, vs = [], []
    t = None
    for line in r.splitlines():
        m = re.search(r"pts_time:([\d.]+)", line)
        if m:
            t = float(m.group(1)); continue
        m = re.search(r"lavfi\.r128\.S=(-?[\d.]+|-inf|nan)", line)
        if m and t is not None:
            try:
                v = float(m.group(1))
            except ValueError:
                v = -120.0
            ts.append(t); vs.append(v)
    return np.array(ts) - 1.5, np.array(vs)


def read_wav(path):
    r = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-f", "f32le", "-ac", "2", "-ar", "48000", "-"], capture_output=True)
    return np.frombuffer(r.stdout, np.float32).reshape(-1, 2).copy()


def write_wav(path, x):
    p = subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ac", "2", "-ar", "48000", "-i", "-", "-c:a", "pcm_f32le", path],
                       input=x.astype(np.float32).tobytes(), capture_output=True)
    if p.returncode:
        sys.exit(p.stderr.decode()[-2000:])


def level_bed(src, dst, target, turn, lift_db, dur):
    """Gain curve so the bed's 3 s loudness sits on `target` LUFS everywhere (±10 dB around its median gain, 2 s smoothing), then
    the turn lift as a 100 ms ramp. Returns the per-window spread of the result (max − min LU, above −50 LUFS)."""
    x = read_wav(src)
    tc, st = short_term(src)
    ok = (tc >= 0) & (st > -60)
    if ok.sum() < 3:
        sys.exit("yt_mix: the bed is silent")
    tc, st = tc[ok], st[ok]
    grid = np.arange(0, dur + 0.1, 0.1)
    need = target - np.interp(grid, tc, st)
    med = float(np.median(need))
    g = np.clip(need, med - 10, med + 10)              # relative clamp: never more than 10 dB either side of the track's median gain
    k = int(2.0 / 0.1) | 1
    pad = np.pad(g, k // 2, mode="edge")
    g = np.convolve(pad, np.ones(k) / k, mode="valid")[:len(grid)]
    ts = np.arange(len(x)) / 48000
    gain_db = np.interp(ts, grid, g) + lift_db * np.clip((ts - turn) / 0.1, 0, 1)
    write_wav(dst, x * (10 ** (gain_db / 20))[:, None])
    _, st2 = short_term(dst)
    st2 = st2[st2 > -50]
    return g, (st2.max() - st2.min()) if len(st2) else 0.0


def run(cmd):
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode:
        sys.exit(p.stderr[-2000:])


def main():
    job = os.path.abspath(sys.argv[1])
    spec = json.load(open(os.path.join(job, "yt", "spec.json"), encoding="utf-8"))
    a = spec["audio"]
    dur = spec["frames"] / spec["fps"]
    work = os.path.join(job, "yt", "work")
    os.makedirs(work, exist_ok=True)
    voice = os.path.join(work, "voice.wav")
    run(["ffmpeg", "-v", "error", "-y", "-i", os.path.join(job, a["voice"]), "-vn", "-ac", "2", "-ar", "48000", "-t", f"{dur:.4f}", voice])
    if a.get("mute"):               # profanity muted in the voice (README § 5: starred on screen, muted in the audio), 10 ms ramps
        x = read_wav(voice); g = np.ones(len(x)); sr, rr = 48000, 480
        for t0, t1 in a["mute"]:
            i0, i1 = int(t0 * sr), int(t1 * sr)
            g[max(0, i0 - rr):i0] = np.minimum(g[max(0, i0 - rr):i0], np.linspace(1, 0, i0 - max(0, i0 - rr)))
            g[i0:i1] = 0; g[i1:i1 + rr] = np.minimum(g[i1:i1 + rr], np.linspace(0, 1, len(g[i1:i1 + rr])))
        write_wav(voice, x * g[:, None])
        print(f"voice: muted {len(a['mute'])} range(s)")
    vi, vtp = lufs(voice)
    print(f"voice: {vi:.1f} LUFS, true peak {vtp:.1f} dBFS")
    inputs, fc, labels = ["-i", voice], [], ["[0:a]"]
    for k, sfx in enumerate(a.get("sfx", [])):
        inputs += ["-i", os.path.join(REPO, sfx["file"])]
        ms = int(round(sfx["t"] * 1000))
        fc.append(f"[{len(inputs) // 2 - 1}:a]atrim=start={sfx.get('lead', 0)},asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo,"
                  f"volume={sfx.get('gain_db', -22)}dB,adelay={ms}|{ms},apad[s{k}]")
        labels.append(f"[s{k}]")
    bed = a.get("bed")
    if bed and os.path.exists(os.path.join(job, bed)):
        bed_cut = os.path.join(work, "bed-cut.wav")
        run(["ffmpeg", "-v", "error", "-y", "-ss", f"{a.get('bed_in', 0):.3f}", "-t", f"{dur:.4f}", "-i", os.path.join(job, bed),
             "-af", f"afade=t=out:st={dur - 0.01:.4f}:d=0.010", "-ar", "48000", "-ac", "2", bed_cut])
        target = vi - a.get("bed_under_lu", 13.6)
        turn, lift_db = a.get("turn_t", dur), a.get("turn_lift_db", 2.0)
        bed_lev = os.path.join(work, "bed-level.wav")
        g, spread = level_bed(bed_cut, bed_lev, target, turn, lift_db, dur)
        inputs += ["-i", bed_lev]
        fc.append(f"[{len(inputs) // 2 - 1}:a]aresample=48000,aformat=channel_layouts=stereo,apad[bed]")
        labels.append("[bed]")
        print(f"bed: levelled to {target:.1f} LUFS short-term ({a.get('bed_under_lu', 13.6)} LU under the voice; gain {g.min():+.1f}…{g.max():+.1f} dB), "
              f"+{lift_db} dB from {turn} s; 3 s windows spread {spread:.1f} LU")
    else:
        print("bed: none")
    fc.append(f"{''.join(labels)}amix=inputs={len(labels)}:duration=first:normalize=0,atrim=0:{dur:.4f}[m]")
    premix = os.path.join(work, "premix.wav")
    run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", ";".join(fc), "-map", "[m]", "-ar", "48000", premix])
    ti, ttp = a.get("target_i", -12.0), a.get("target_tp", -1.5)
    out = os.path.join(work, "mix.wav")
    gain = ti - lufs(premix)[0]
    for _ in range(3):
        run(["ffmpeg", "-v", "error", "-y", "-i", premix, "-af",
             f"volume={gain:.3f}dB,aresample=192000,alimiter=limit={10 ** ((ttp - 0.3) / 20):.4f}:attack=5:release=50:level=0:latency=1,"
             f"aresample=48000,afade=t=in:d=0.005,afade=t=out:st={dur - 0.010:.4f}:d=0.010",      # 5 ms in: a cut can start mid-word
             "-ar", "48000", out])
        mi, mtp = lufs(out)
        if abs(mi - ti) <= 0.15 and mtp <= ttp + 0.05:
            break
        gain += ti - mi
    print(f"mix: {mi:.1f} LUFS integrated, true peak {mtp:.1f} dBFS -> {out}")


if __name__ == "__main__":
    main()

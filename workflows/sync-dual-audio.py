# /// script
# requires-python = ">=3.9"
# dependencies = ["numpy", "scipy"]
# ///
"""
sync-dual-audio.py — align a separately recorded voice track to camera footage.

THE SHOOT: the voice is a good mic recorded somewhere else (here: a HyperX through
OBS, so it arrives inside a screen-recording video). The camera's own mic recorded
the same room badly. That bad track is useless as program audio and perfect as a
SYNC REFERENCE, because the same words are on both.

WHAT THIS DOES: finds the offset between the two recordings, measures whether the two
devices' clocks drifted apart over the take, and muxes the good audio onto the camera
picture without re-encoding the video. The output is the working raw for the pipeline.

WHY IT IS BUILT THIS WAY — the two mics do not sound alike. A close condenser hears
direct speech; a camera mic ten feet away hears a reverberant room, 30-40 dB quieter.
Ordinary cross-correlation on those two signals is mush. So:

  STAGE 1, COARSE — correlate LOUDNESS ENVELOPES in dB across the whole recording.
  Level differences become a constant that mean-removal deletes, leaving only the
  shape both share: where speech starts and stops. Robust, finds the rough offset
  anywhere in the file, accurate to roughly a syllable.

  STAGE 2, FINE — GCC-PHAT in several windows, searched only near the coarse answer.
  The phase transform whitens the cross-spectrum before correlating, so each mic's
  frequency response and reverb tail stop mattering and only arrival TIME survives.
  This is the standard time-delay estimator for dissimilar microphones, and it turns
  a smeared hump into a sharp spike. Band-limiting to the speech band first keeps the
  whitening from amplifying bands that hold nothing but noise. Parabolic interpolation
  around the peak gives sub-sample precision.

  DRIFT — two devices nominally at 48 kHz never agree exactly. A least-squares line
  through the per-window offsets gives the clock ratio; its residual scatter is the
  honest precision of the whole measurement, and it is reported. Audio that locks
  perfectly at the top of a long take can be several frames out by the end, so above
  --drift-tolerance frames the mic is resampled by the measured ratio before muxing.

USAGE
  uv run workflows/sync-dual-audio.py --camera CAM.MP4 --mic OBS.MP4 --report
  uv run workflows/sync-dual-audio.py --camera CAM.MP4 --mic OBS.MP4 --out raw/synced.mp4

Pre-extracted 16 kHz mono WAVs go in with --camera-wav / --mic-wav, which skips a slow
re-read of a large camera file.
"""
import argparse, json, os, subprocess, sys, tempfile

SR = 16000            # analysis rate
ENV_HOP = 16          # 1 ms envelope hop at 16 kHz
BAND = (300.0, 3500.0)  # speech band for the fine stage
DEF_WIN = 60.0        # seconds per fine window
DEF_WINDOWS = 5
SEARCH = 0.6          # seconds either side of the coarse offset


def run(cmd, **kw):
    return subprocess.run(cmd, check=True, **kw)


def probe(path):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries",
         "stream=codec_type,r_frame_rate:format=duration", "-of", "json", path],
        capture_output=True, text=True, check=True).stdout
    d = json.loads(out)
    dur = float(d["format"]["duration"])
    fps = None
    for s in d.get("streams", []):
        if s.get("codec_type") == "video" and s.get("r_frame_rate", "0/0") != "0/0":
            n, den = s["r_frame_rate"].split("/")
            fps = float(n) / float(den)
    return dur, fps


def to_wav(src, dst, stream=0):
    run(["ffmpeg", "-v", "error", "-y", "-i", src, "-vn", "-map", f"0:a:{stream}",
         "-ac", "1", "-ar", str(SR), "-c:a", "pcm_s16le", dst])
    return dst


def read_wav(path):
    import numpy as np
    from scipy.io import wavfile
    sr, x = wavfile.read(path)
    if sr != SR:
        sys.exit(f"{path}: expected {SR} Hz, got {sr}")
    if x.ndim > 1:
        x = x.mean(axis=1)
    return x.astype(np.float64)


def envelope(x, hop=ENV_HOP, smooth_ms=25):
    """Short-time RMS in dB, floored, smoothed, normalised."""
    import numpy as np
    n = len(x) // hop
    e = np.sqrt((x[:n * hop].reshape(n, hop) ** 2).mean(axis=1) + 1e-12)
    e = 20.0 * np.log10(e + 1e-12)
    top = float(np.percentile(e, 95))
    e = np.clip(e, top - 55.0, None)
    k = max(1, int(smooth_ms))
    if k > 1:
        e = np.convolve(e, np.ones(k) / k, mode="same")
    e -= e.mean()
    s = e.std()
    return e / s if s > 1e-12 else e


def xcorr_env(a, b):
    """Plain FFT cross-correlation, for the coarse envelope stage.
    Returns (lag, prominence). lag = how far b shifts RIGHT to match a."""
    import numpy as np
    n = 1
    while n < len(a) + len(b):
        n *= 2
    c = np.fft.irfft(np.fft.rfft(a, n) * np.conj(np.fft.rfft(b, n)), n)
    c = np.concatenate((c[-(len(b) - 1):], c[:len(a)]))
    lags = np.arange(-(len(b) - 1), len(a))
    k = int(np.argmax(c))
    prom = float(c[k]) / (float(np.std(c)) + 1e-12)
    return int(lags[k]), prom


def gcc_phat(a, b, max_lag):
    """Generalised cross-correlation with phase transform.

    Whitening the cross-spectrum removes each microphone's frequency response and
    most of the room, leaving arrival time. Returns (lag_samples, prominence) with
    sub-sample interpolation; lag = how far b shifts RIGHT to match a."""
    import numpy as np
    n = 1
    while n < len(a) + len(b):
        n *= 2
    R = np.fft.rfft(a, n) * np.conj(np.fft.rfft(b, n))
    R /= (np.abs(R) + 1e-12)                      # the phase transform
    c = np.fft.irfft(R, n)
    c = np.concatenate((c[-(len(b) - 1):], c[:len(a)]))
    lags = np.arange(-(len(b) - 1), len(a))
    keep = np.abs(lags) <= max_lag
    c, lags = c[keep], lags[keep]
    k = int(np.argmax(c))
    prom = float(c[k]) / (float(np.std(c)) + 1e-12)
    delta = 0.0
    if 0 < k < len(c) - 1:                        # parabolic peak interpolation
        y0, y1, y2 = float(c[k - 1]), float(c[k]), float(c[k + 1])
        den = y0 - 2 * y1 + y2
        if abs(den) > 1e-20:
            delta = 0.5 * (y0 - y2) / den
            delta = max(-1.0, min(1.0, delta))
    return float(lags[k]) + delta, prom


def bandpass(x):
    from scipy.signal import butter, sosfiltfilt
    sos = butter(4, [BAND[0], BAND[1]], btype="band", fs=SR, output="sos")
    return sosfiltfilt(sos, x)


def refine(cam, mic, coarse_s, centre_s, win, search=SEARCH):
    """GCC-PHAT residual for one window. Returns (absolute_offset_s, prominence)."""
    c0 = int(centre_s * SR); c1 = c0 + int(win * SR)
    m0 = int((centre_s - coarse_s) * SR); m1 = m0 + int(win * SR)
    if c0 < 0 or m0 < 0 or c1 > len(cam) or m1 > len(mic):
        return None
    a = cam[c0:c1]; b = mic[m0:m1]
    if a.std() < 1e-9 or b.std() < 1e-9:
        return None
    # Taper both windows. Hard window edges are broadband steps, the phase transform
    # amplifies them, and the two edges line up at ZERO residual lag, so a quiet
    # camera mic returns exactly the coarse offset instead of the speech peak
    # (found 2026-09-19 on gta6-travis-scott-hired: 12 of 25 windows read +0.0000).
    from scipy.signal.windows import tukey
    w = tukey(len(a), 0.2)
    lag, prom = gcc_phat(bandpass(a) * w, bandpass(b) * w, int(search * SR))
    return coarse_s + lag / SR, prom


def fmt(sec):
    sign = "-" if sec < 0 else ""
    s = abs(sec)
    return f"{sign}{int(s//60):02d}:{s%60:06.3f}"


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--camera", required=True)
    ap.add_argument("--mic", required=True)
    ap.add_argument("--camera-wav"); ap.add_argument("--mic-wav")
    ap.add_argument("--mic-stream", type=int, default=0)
    ap.add_argument("--out"); ap.add_argument("--report", action="store_true")
    ap.add_argument("--json-out", metavar="FILE")
    ap.add_argument("--windows", type=int, default=DEF_WINDOWS)
    ap.add_argument("--window-len", type=float, default=DEF_WIN)
    ap.add_argument("--drift-tolerance", type=float, default=0.5,
                    help="frames of end-to-end drift tolerated before resampling")
    ap.add_argument("--audio-bitrate", default="320k")
    ap.add_argument("--audio-codec", default="aac",
                    help="aac (at --audio-bitrate), or PCM such as pcm_f32le to keep a 32-bit "
                         "float recorder's overs intact; PCM needs a .mov --out")
    a = ap.parse_args()

    import numpy as np

    cam_dur, cam_fps = probe(a.camera)
    mic_dur, _ = probe(a.mic)
    fps = cam_fps or 30.0
    print(f"camera : {fmt(cam_dur)}  {fps:.3f} fps")
    print(f"mic    : {fmt(mic_dur)}")

    tmp = tempfile.mkdtemp(prefix="sync_")
    cam = read_wav(a.camera_wav or to_wav(a.camera, os.path.join(tmp, "cam.wav")))
    mic = read_wav(a.mic_wav or to_wav(a.mic, os.path.join(tmp, "mic.wav"), a.mic_stream))

    # --- stage 1 -------------------------------------------------------------
    lag, eprom = xcorr_env(envelope(cam), envelope(mic))
    coarse = lag * ENV_HOP / SR
    print(f"\ncoarse : {coarse:+.3f}s   (envelope, peak {eprom:.1f}x the noise floor)")

    # --- stage 2 -------------------------------------------------------------
    lo = max(0.0, coarse)
    hi = min(cam_dur, mic_dur + coarse)
    span = hi - lo - a.window_len
    if span <= 0:
        sys.exit("the two recordings do not overlap enough to measure")
    nwin = max(2, a.windows)
    centres = [lo + span * i / (nwin - 1) for i in range(nwin)]

    measured = []
    for c in centres:
        r = refine(cam, mic, coarse, c, a.window_len)
        if r:
            off, prom = r
            measured.append((c, off, prom))
            print(f"  window @ {fmt(c)}   offset {off:+.4f}s   peak {prom:6.1f}x")

    if len(measured) < 2:
        sys.exit("could not refine enough windows to trust a result")

    ts = np.array([m[0] for m in measured])
    offs = np.array([m[1] for m in measured])
    proms = np.array([m[2] for m in measured])

    # drop any window whose peak is not clearly above the others' typical strength
    good = proms >= max(5.0, float(np.median(proms)) * 0.35)
    if good.sum() >= 2:
        ts, offs = ts[good], offs[good]
    dropped = len(measured) - int(good.sum())
    if dropped:
        print(f"  ({dropped} weak window(s) dropped from the fit)")

    slope, intercept = np.polyfit(ts, offs, 1)
    resid = offs - (slope * ts + intercept)
    scatter = float(np.std(resid))
    drift_s = float(slope * (ts[-1] - ts[0]))
    drift_frames = abs(drift_s) * fps
    offset0 = float(intercept)                     # offset at camera time 0

    print(f"\noffset : {offset0:+.4f}s at t=0   ({offset0*fps:+.1f} frames @ {fps:.3f} fps)")
    if offset0 >= 0:
        print(f"         the mic started {offset0:.3f}s AFTER the camera")
    else:
        print(f"         the mic started {abs(offset0):.3f}s BEFORE the camera")
    print(f"drift  : {drift_s*1000:+.1f} ms over {ts[-1]-ts[0]:.0f}s = {drift_frames:.2f} frames"
          f"   (clock {slope*1e6:+.1f} ppm)")
    print(f"scatter: +/-{scatter*1000:.1f} ms around the fit "
          f"= +/-{scatter*fps:.2f} frames  <- the real precision")

    trust = scatter * fps < 0.5
    if not trust:
        print("  ! scatter is over half a frame; treat the drift number as indicative only")

    resample = bool(drift_frames > a.drift_tolerance and trust)
    r = 1.0 / (1.0 - slope)            # camera_time = r*mic_time + r*intercept
    stretch = 1.0 - slope              # the asetrate multiplier, == 1/r
    delay = r * offset0
    if resample:
        print(f"         -> resampling the mic by {stretch:.9f} to hold sync end to end")
    elif drift_frames > a.drift_tolerance:
        print(f"         -> drift exceeds tolerance but the fit is too noisy to correct; "
              f"using a constant offset")
    else:
        print(f"         -> within tolerance, constant offset is enough")

    result = {
        "camera": os.path.abspath(a.camera), "mic": os.path.abspath(a.mic),
        "camera_duration": round(cam_dur, 3), "mic_duration": round(mic_dur, 3),
        "fps": fps, "offset_s": round(offset0, 5),
        "offset_frames": round(offset0 * fps, 2),
        "envelope_peak": round(eprom, 2),
        "windows": [{"centre_s": round(c, 2), "offset_s": round(o, 5),
                     "peak": round(p, 2)} for c, o, p in measured],
        "slope_ppm": round(slope * 1e6, 2),
        "drift_s": round(drift_s, 5), "drift_frames": round(drift_frames, 3),
        "scatter_ms": round(scatter * 1000, 2),
        "scatter_frames": round(scatter * fps, 3),
        "resampled": resample, "stretch": stretch if resample else 1.0,
        "delay_s": round(delay if resample else offset0, 5),
    }
    if a.json_out:
        os.makedirs(os.path.dirname(os.path.abspath(a.json_out)), exist_ok=True)
        with open(a.json_out, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=1)
        print(f"wrote {a.json_out}")

    if a.report or not a.out:
        return

    # --- mux -----------------------------------------------------------------
    d = delay if resample else offset0
    filt = []
    if resample:
        # asetrate only takes a WHOLE rate: 48000*1.0000117 rounds to 48001, a 20.8 ppm
        # stretch for an 11.7 ppm drift (2026-09-19). Oversample first so the rounding
        # error is at most 0.5/960000 = 0.5 ppm.
        hi = 48000 * 20
        filt.append(f"aresample={hi},asetrate={round(hi * stretch)},aresample=48000")
    if d >= 0:
        filt.append(f"adelay={int(round(d*1000))}:all=1")
    filt.append("apad")

    cmd = ["ffmpeg", "-v", "error", "-stats", "-y"]
    if d < 0:
        cmd += ["-ss", f"{-d:.6f}"]
    cmd += ["-i", a.mic, "-i", a.camera,
            "-map", "1:v:0", "-map", f"0:a:{a.mic_stream}",
            "-af", ",".join(filt), "-t", f"{cam_dur:.6f}",
            "-c:v", "copy", "-c:a", a.audio_codec]
    if a.audio_codec == "aac":
        cmd += ["-b:a", a.audio_bitrate]
    cmd += [a.out]
    # no +faststart: this output is a local working master, and rewriting the moov
    # atom on a multi-gigabyte file costs a whole extra pass for no editing benefit
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    print(f"\nmuxing -> {a.out}")
    run(cmd)
    od, _ = probe(a.out)
    print(f"done   : {fmt(od)}")
    if abs(od - cam_dur) > 0.5:
        print(f"  ! output {od:.2f}s vs camera {cam_dur:.2f}s")


if __name__ == "__main__":
    main()

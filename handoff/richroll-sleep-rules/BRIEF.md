# richroll-sleep-rules: Onyx sample Short for The Rich Roll Podcast (re-pick, Affan's review 2)

## ▶ STATUS: resume here
- **2026-10-08 (night): FINAL = v6** (`ig/build_spec.py`; two fresh-eyes QA rounds, every MED and LOW fixed and checked by measurement). 46.55 s, 1395 frames at 29.97 → 59.94 fps out, −13.1 LUFS.
  - **Hook:** "One number at night / decides your sleep." (Bryan's own claim).
  - **Cards:** heart+ECG → receipt (ticks, stamp in its own zone, held so the stamp reads 1.5 s, y 1025) → chip → rules list that grows one rule per beat (no exit fade; the list holds 1.5 s on the last frame).
  - **Captions:** left-aligned plain white + gold, constant position under the lips, a real 60 fps rise; chunks break on (and wait for) the camera cuts.
  - **Rough cut:**
    - the `splice.sh` video offset is fixed (A/V was 4.95 s off);
    - the head trimmed past "But" (raw 19.5529); "then" dropped;
    - the end runs into Bryan's pause and stops on his last resting frame (raw 149.5494);
    - "amber are great" fixed in words.json;
    - splice at the measured gain (0 dB).
  - **4K base:** patched by stream copy (output-side seek), the last take re-run through Topaz.
  - **Kit fixes:** the caption rise, Epidemic lead-ins (`ES_LEAD`), click level, `captions.breaks`, `sfx_kind`, the growing rules card.
  `outputs/richroll-sleep-rules.final.mp4` + ~/Downloads. (The OLD pick, `richroll-bank-teller.final.mp4`, is still in ~/Downloads.)
- 2026-10-08: job opened for the re-pick (`_onyx-batch-2026-10/richroll/research-2.md` § THE PICK): Bryan Johnson's five sleep rules,
  Ep. 1015 `-4GqndDjigY` 0:43:09.4–0:45:19.15. Look = Instagram minimal (`presets/youtube-shorts/onyx-samples/`) + more motion
  graphics + a crisp Epidemic SFX on every entrance (Affan: "keep the style the same… spice it up through actual motion graphics").

## Download log
| # | File | Source | Size | Why |
|---|---|---|---|---|
| v1 | `raw/-4GqndDjigY_004259-004529.mkv` | https://www.youtube.com/watch?v=-4GqndDjigY section 0:42:59–0:45:29 (yt-dlp, best ≤ 2160p + original audio) | 113 MB (done 2026-10-08) | the source of the cut |
| m1 | `ig/assets/audio/ES_Glowing Apples - Cerulean Skies.wav` | Epidemic Sound recording 7b63f389 (MCP DownloadRecording, FULL, WAV; ambient, relaxing, no drums, 2:48) | ~30 MB (est.) | the music bed |

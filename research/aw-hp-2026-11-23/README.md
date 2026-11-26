# aw-hp-2026-11-23: today's AW Harry Potter Short (research → pitch → STOP for Affan's OK)

## ▶ STATUS: resume here (26 Nov 2026)
- **POSTED 25 Nov 01:15 UTC as `p8fIsS5PhJ4`, "Daniel Radcliffe HATED His Harry Potter Acting 🤯".** Affan finished and posted it himself (the last sequence built here was polaroid v3). **72,748 views at ~26 h** (the hub's API read, 26 Nov ~03:45 PST). The locked centre was 150K; the hub owns RESULTS.
- **This job is CLOSED.** No more finish work goes onto his Premiere unless he asks. The next HP topic runs in the session aw-hp-day2, not here.

### 24 Nov (~03:00 PKT): STOP 1 built
- **24 Nov: v3 APPROVED by Affan, STOP 1 BUILT.** The uncool-dad sentence is cut, so the Short ends on "...sort of happy with that." Sequence "Harry Potter Can't Watch Himself - raw cut" (id `a59bf8a2-1d92-49fd-a036-ea8af3726d89`) is in his ABW11: 33.40 s, 29 clips, READ BACK = PASS, **not saved (needs his Ctrl+S)**.
  - Built by the session hp-cant-watch-build (Sonnet, $11.17 = 0.51 %).
  - Job: `projects/radcliffe-cant-watch-himself/RUN.md` (quality table, proof, ear items).
  - **WAITING for his Tella.** STOP 2 starts only after it.
  - Quality: HSC and Garfield are re-fetched VP9; Ross stays the old H.264 (sharper); the HBP cover is the official 1080p upload (no 4K exists). 1.78x on every clip, Lanczos only, no AI.

### Before the OK (24 Nov, ~00:20 PKT)
- **24 Nov: v3 TEXT SEQUENCE given** (Affan: "has potential but needs more bits"). It's at the top of `PITCH.md`: hook "now I cringe watching myself" → Half-Blood Prince "the bottom… my own stuff" → Ross ~2011 "I avoid ever watching them again… baby photos" → parents "the reviews were good… you're fine" → Garfield → "I disagree with him" → END: son watches the HBO show "and I'm also sort of happy with that… his very uncool, unimpressive dad". ~38-40 s; centre re-locked at 150K. 2 more downloads (full-episode section 38-52 min, Ross 2021), clean. WAITING for his OK on v3, then ONE Sonnet build.

### Earlier (23 Nov, ~08:05 PKT)
- **Done:**
  - `TEARDOWN.md`: why the Oldman Short won (516,497) and the Snape Short lost (36,894). H1, the hook: a famous actor's own harsh verdict on a
    loved role. The comments argue with it.
  - `PITCH.md`: today's LEAD, "Daniel Radcliffe CRINGES At Himself 😅". Dan's own verdict → Andrew Garfield's "he's really good in those Harry Potter movies" → Dan:
    "I disagree with him… but that's really nice". **Centre 100K, under the 150K bar, so it goes as "no pick clears the bar; best
    lead".**
  - `BANK.md`: 8 storylines, ranked.
  - Instagram log: `research/instagram-beat-mining/2026-11-23-hp.md`.
- **Done too:** cold read (Sonnet; fixes applied as v2), Fable final (fixes applied), hub told (meter 3 %).
- **Next:** wait for Affan's OK via the hub. On his OK, ONE Sonnet build session (STOP 1, raw sequence in his
  Premiere; method of `projects/mj-fired-his-father/premiere/`).
- **Nothing built. Premiere not touched.**

## Files
- `TEARDOWN.md`, `PITCH.md`, `BANK.md`.
- `scan_cache.py`: regex scan over the 20,926 cached YouTube videos (zero requests).
- `dl.sh`: the 3 paced downloads (done, no bot page).
- `align.py`: word-aligned transcripts.
- `src/`: the three sources + wavs (on X:).
- `transcript/`: scout text + `*.words.json`.
- `proof/`: frames.
- `meta/`: API answers (fresh counts, winner comments, AW uploads, the searches).

## Requests used
- **YouTube Data API (hp-short):**
  - 4 of 12 searches;
  - `videos` ×6 calls;
  - `commentThreads` ×3;
  - `playlistItems` ×12 (AW uploads + 11 Hits Radio pages).
- **yt-dlp:** 3 downloads through `pace.sh youtube`, 07:39-07:47 PC clock, no 429 or bot page.
- **Instagram:** 12 loads through `pace.sh instagram`, no block.
- **GPU:** 2 medium.en jobs under `lock.sh gpu` + `.asr-lock`, Premiere closed.

## Usage (weekly meter, all models)
- 1 % at the start (~07:00 PKT).
- 2 % at the pick.
- **3 % at the pitch (~08:00 PKT): the 3 % tripwire. The hub is told before anything else runs.**

# aw-hp-2026-11-26: the next AW Harry Potter Short (research → ONE pick + refreshed bank → text sequence → STOP for Affan's OK)

## ▶ STATUS: resume here
- **26 Nov ~09:40 PKT: Affan, directly in this session, rejected Oldman Part 2 ("nop find something else this is not good"). New-face search: best found = BONNIE WRIGHT, "Movie Ginny Wasn't Her Fault" (`PITCH-bonnie.md`). NO PICK at the bar: locked 60K.** Her own telling is on camera in 1080p studio (Inside of You `KqOW45wD2a8`, 2023): "I'm going to be seen as badly portraying this character… it wasn't really my fault… we know it wasn't you, we just wanted more of you". Topic proof 3.70M (GSA) + 898K (Peralo). Weak: a fear, not a verdict; no second voice; owner Shorts of the sitting ≤58K. NOT max effort: Instagram not met (Chrome disconnected), no cold read, no Fable on the final. Scans: GSA + HogwartsFandom 1,000 uploads each with stats (`meta/up_gsa.json`, `up_hf.json`); Inside of You full + Clips (`up_inyo*.json`). Watson v3 saved as `PITCH-watson-v3.md`.
- Usage: 71 % (~09:00). YouTube searches 36 of 37 (s36 "bonnie wright ginny disappointing"); the rest were 1-unit reads (uploads + stats + comments).
- **Next search after the 13:00 PKT reset:** the only HP Shorts over ~500K since 1 Sep are HBO-series Shorts (GSA 4.53M, 672K, 419K). Test: an ADULT original-cast voice on camera about the series (HBO child cast = minors; Radcliffe was the 25 Nov face).
- Rule notes: the audio pull 28:50-30:52 ran 2:02 (2 s over the 2-min rule). A whole-Short pull of `kYJQAWYDozE` was refused by the permission classifier and not retried.
- **26 Nov ~07:35 PKT: WATSON pitch v3 (`PITCH.md`). NO PICK yet, because of the picture.** Her own telling exists on camera only at 640x360 (HeyUGuys `jP-p3QM9dWk`, Nov 2010): "I'll do it once, and I'll do it for real… when he called cut, I couldn't stop crying". The turn: the DH2 featurette "The Women of Harry Potter" (`j0fBiihIt-8`, 960x720), "Helena was also a really important mentor to me… I went home and wrote down everything that she said". Bonham Carter's side was NOT found on camera. "HATED" is not her word. Locked 100K (below the bar); anchor test NOT run. Sirius Part 2 (`PITCH-sirius-backup.md`) is the HD-ready backup at 150K. Older versions: `PITCH-watson-v1.md`, `PITCH-watson-v2.md`.
- Usage: 57 % start → 62 % → 64 % → 66 % (~07:00).
- (superseded by v3) **26 Nov ~06:30 PKT: WATSON pitch written (`PITCH.md`) on Affan's direction via the hub ("try to make a text sequence for the emma watson angle"). Result: NO PICK at the 150K bar; best Watson version locked 120K, and it needs 2 sources located first (the 2010 junket original in HD; the 2011 answer's timestamp in Digital Spy's HD press conference).** Sirius Part 2 is the backup (`PITCH-sirius-backup.md`, 150K, his same-face call open).
- Usage: 57 % start → 62 % (Sirius pitch) → 64 % (~06:10).
- (superseded: now `PITCH-sirius-backup.md`, 150K) **26 Nov ~05:25 PKT: PITCH written: "Gary Oldman's ONLY Proud Scene 🥹" (Sirius Part 2), locked centre 180K, conditional on Affan's same-face call.** If he says a Part 2 is a repeat: NO new-face pick over the bar today (best lead: Felton "Draco Was A Slimy Git", BANK.md B).
- NOT max effort yet: ear-check; word-level edges (RAM exhausted by other jobs); clean HD source for the optional PoA film-line ending; Instagram 11 searches / 18 posts (< 20/40).
- Started 26 Nov ~03:50 PKT (the PC clock is PKT; Git Bash prints "PST"). Session aw-hp-day2. Nothing built, Premiere not touched.
- Brief: the AW hub (`local_3ae3a4cf…`), Affan 26 Nov "harry potter short is doing well again find another topic".
- Usage (weekly all-models meter): **57 %** at the start, **62 %** at the pitch (~05:15).
- Next: Fable final + cold read → report to the hub → wait for Affan's OK via the hub → ONE Sonnet build session (all three Oldman sittings are on disk).

## Files
- `PITCH.md`: the pick + text sequence + gate statement + prediction.
- `BANK.md`: the refreshed storyline bank + the kill log (31 candidates).
- `IG.md`: Instagram searches and reads.
- `meta/`: API answers (s01-s21 searches with stats; comments on p8fIsS5PhJ4; v_* video reads).
- `src/`: Pattinson GQ Cedric section (1080p), PoA line uploads (both have burned-in text: reference only), wav slices.
- `idref/`: the GSA "Emma Watson's Most HATED" Short audio (source identification only, never footage).
- `transcript/`: GSA Watson + Pattinson GQ (WhisperX medium.en).
- `proof/`: frame sheets (speakers, Oldman sittings, PoA uploads).
- Tools: `s.py` (search + stats), `pl.py` (uploads playlist scan), `dl.sh` (one paced pull), `asr.sh`/`asr.py`/`asr_lean.py`, `ighold.sh`.

## Requests used
- YouTube Data API (hp-short; the hub raised the cap to 37 for the Watson pivot): 31 searches (2 OR'd ones returned nothing); ~30 one-unit `videos` calls; 13 `commentThreads` (incl. 9 `searchTerms` reads on Digital Spy's press conference); ~118 `playlistItems` pages (the official HP channel ×2, Josh Horowitz ×2, Collider BTS). No 403.
- yt-dlp via `pace.sh youtube`: Sirius phase 6 pulls; Watson phase ~25 ID pulls (audio sections ≤2 min: Collider ×3, ClevverTV ×5, HeyUGuys ×5, Movies Ireland ×3, WB EPK ×2, fan copies ×3, GSA duo, role-swap featurette ×2, HBC on-set ×2, IGN ×3). Sirius-phase detail: (GSA Watson audio, GQ 0:12-2:12, PoA official full scene = "not available" (no file), official OotP Short, 2 PoA fan uploads). No bot page or 429.
- Instagram: 16 search loads + 22 post reads (paced). No block.
- ASR: 2 WhisperX jobs under lock.sh gpu + projects/.asr-lock (1 CUDA OOM, retried on CPU); 2 later attempts failed on system RAM (other sessions' jobs).

## Rule notes (honest log)
- One pull ran 8 s over the 2-minute section rule (`roleswap_0200`, 2:00-4:08).
- One full 2:50 pull of `j0fBiihIt-8` was launched by mistake and killed while still waiting for the pace lock (nothing downloaded); it was re-run as 1:30 + 1:20 sections.
- Pulls in `src/` of fan and competitor uploads are reference only; none is a build source.

---
name: project-abundance-shorts-automation
description: "Ongoing goal (started 2026-09-14) to automate the user's Abundance Wisdom shorts workflow; style spec lives at presets/youtube-shorts/abundance-wisdom/style-spec.md"
metadata: 
  node_type: memory
  type: project
  originSessionId: 7173e089-1e87-4811-944b-8e4043fa359d
  modified: 2026-10-20T01:52:33.233Z
---

Goal: automate the full Abundance Wisdom shorts edit (soundbite stitching → head-lock → Topaz → captions → zooms/transitions → audio → export) to match the user's hand edits. Started 2026-09-14.

State: style reverse-engineered from 3 exports + the user's spoken workflow, written to `presets/youtube-shorts/abundance-wisdom/style-spec.md` (DRAFT). Nothing built yet.

**Why:** the user edits every short by hand across Premiere → AE → Topaz → CapCut → AE → Premiere; they want Claude doing execution while they direct.

**How to apply:** read the style spec before any work on their shorts. The user downloads the YouTube source clips themselves — Claude works from the downloaded files. Their tools on this machine: Topaz Video AI (CLI ffmpeg with tvai_* filters, preset `C:\ProgramData\Topaz Labs LLC\Topaz Video AI\presets\Iris Preset.json`), AE 2025 with Sapphire + Deep_Glow_v1.2, caption font Gretaros-Regular.otf (user fonts). See [[user-abundance-wisdom-editor]].

The Content Engine (their Cowork project) is readable on disk at `X:\Claude Projects\Abundance Wisdom\` (moved from E: on 2026-09-26, see [[project-workspace-on-nvme]]; ENGINE.md = method, FINDINGS.md, RESULTS.md, per-short `*-CUT.md` / `*-CUTSHEET.md`). The chat history itself is NOT accessible from here. A "FINAL LOCKED BUILD" in a `*-CUT.md` is the edit input: numbered beats of quote / source title / YouTube URL / in → out timestamps. Read-only for Claude here: don't edit those files unless asked. The final export can deviate a lot from the locked build (Biles short used anchor + experts despite a one-speaker cutsheet), so the diff between build and export is where their editing judgment shows. Grade preset in use: **`Affan CC Preset.ffx`** (Lumetri + Curves; identical md5 to `2.ffx` in the Downloads "Main CC Presets" pack). Their whole AE preset library is at `C:\Users\affan\OneDrive\Documents\Adobe\After Effects 2025\User Presets\` (Deep Glow Caps, Deep Glow Line Preset, fade/brightness transitions, BlurMoCurves combos) plus their own ExtendScript `After Effects - Adjustment Layer T.jsx`, which aligns each adjustment layer to the clip below and stretches its S_BlurMoCurves keyframes (they already script AE).

**2026-09-23: SEQUENCING moved to Claude.** The creator hands over a Premiere project + empty sequence + bin and the
locked build from ALLEGATIONS-CUT.md-style Content Engine files; Claude lays the cut by script
(presets/youtube-shorts/abundance-wisdom/ beats.json -> resolve_beats -> plan_placement -> place_sequence).
First job: projects/mj-allegations (ABW8 / Sequence 03).

**2026-09-23: head lock is scripted and proven** (head_track → headlock_map → apply_headlock →
headlock_proof, PLAYBOOK § 2). The creator hands off by "Replace with After Effects Composition";
Iris-label clips get locked, Violet never. First run: 21 layers in ABW7.aep / ABW8 Linked Comp 02+03.
Prove a lock by rebuilding frames from AE's read-back anchors, never by face-detecting the blown-up comp.

**Division of labour (decided 2026-09-14, sequencing since moved — see above):** the USER does downloading, sequencing in Premiere, Higgsfield overlays, music selection, and the CapCut motion-blur pass on the caption layer Claude exports (creative/psychology work, ~600M views of experience). CLAUDE does the rest: head lock, Topaz, caption layer build (timing/colour/pop), AE edit (zooms, CC, transitions, Deep Glow/Turbulent Displace on the returned caption video), audio polish/SFX/reverb, export. Chosen route: drive After Effects by ExtendScript (`AfterFX.exe -r`, render via `aerender.exe`, AE 25.0.1) using their real presets — no MCP needed. AE pref `Pref_SCRIPTING_FILE_NETWORK_SECURITY` was "0" (off) on 2026-09-14; the user must enable it.

CapCut drafts are readable JSON on this machine (`%LOCALAPPDATA%\CapCut\User Data\Projects\com.lveditor.draft\<MMDD>\draft_content.json`); caption motion blur = blur 0.8, blend 1.0, multiple_blur 6, bilateral. Before/after caption layers live in `E:\Shorts\Abudance Wisdom Shorts Exports\Caption Exports\` (`<name>.mov` before, `<name>2.mp4` after CapCut, 4K HEVC) — use them to PROVE a caption rebuild matches by pixel diff, not by eye.

AE scripting VERIFIED 2026-09-14 (pref now "1"): `Start-Process AfterFX.exe -ArgumentList @("-r", "<path>.jsx")` forwards to the running AE and works. Pass the path UNQUOTED inside the ArgumentList array: wrapping it in extra quotes made the script silently never run. Scripts report back by writing a result file. Confirmed present: Deep Glow (PEDG), S_BlurMoCurves, Turbulent Displace, Lumetri, Curves, BCC and Universe effects; fonts Gretaros-Regular and Montserrat-Black.

YouTube downloads: **REVISED 2026-09-22 — Claude fetches them itself** (yt-dlp is installed and the repo ships it for exactly this). The earlier split, where the user downloaded and Claude worked from the files, no longer applies. See [[feedback-youtube-sourcing]].

**2026-09-20 — full teardown done.** The channel preset now lives at `presets/youtube-shorts/abundance-wisdom/`: README.md (the measured look), PLAYBOOK.md (procedure + who owns which stage), LESSONS.md (lessons + open questions). Read those before any Abundance Wisdom job; style-spec.md is the older export-only analysis. Reference job: Premiere `ABW6.prproj`/`Sequence 11` dynamically linked to AE `ABW7.aep`/`ABW6 Linked Comp 03`. Key mechanics: per-shot S_BlurMoCurves Z-Dist zoom, mask + 198%/43% twin for letterboxed shots, 1%-tall white-solid glow bars, per-section grade stack whose Looks/Curves data CANNOT be scripted (duplicate the creator's adjustment layer instead), captions as one Premiere graphic each (second line = separate graphic one track up, italic = other speaker), BCC Brightness-Contrast flashes peaking on the cut, Studio Reverb on speech, current loudness target −15.3 LUFS.

**2026-10-10 — CODE RENDERER TRIAL (his ask: make shorts entirely without Premiere/AE, 3/day).** Job
`projects/aw-code-trial-parents/` (RUN.md = full record). His AE finishing stage (Comp 47 of the Nick Walker parents
short) rebuilt as GPU code (`render/aw_render2.py`): 30.5 dB PSNR vs AE's own lossless frames, 30.1 dB vs his export,
~5 fps on his RTX 3060 Ti. Method that works: AE as a MEASURING INSTRUMENT only — script builds test comps in a COPY of
his project, saves the copy, `aerender ... -mfr OFF 100` renders headless (MFR on hangs with Deep Glow/Sapphire;
Universe renders BLACK headless), then each effect is fitted to the measurements. Key measured facts: his grade =
PRE sharpen → Magic Bullet Looks (identical on all sections; vertical gradient + strong diffusion glow, NOT pointwise)
→ Curves+Lumetri+Hue/Sat (exact per-section LUT) → Sharpen 40 (= 4-neighbour Laplacian × 40/64) → S_Vignette (mask).
Ask before each AE pass (it switches his open project for ~1-3 min); never `app.open` without checking the project is
clean.

**2026-10-11 — the trial short was made END TO END FROM RAW with no Premiere/AE/CapCut and nothing done by him**
(his goal, restated 2026-10-10: "a one of one copy", "you do everything here"): 28.9 dB vs his YT final; stage A
(sequence from raw, read from the .prproj) 43.6 dB vs his Nig.mov; his Topaz replayed headless from his .tzlog =
bit-exact on his input; captions rendered from the project's text (font 48, GPOS kerning, per-caption stretched pop)
+ a CapCut optical-flow smear model. Edits he makes after a Claude step (e.g. Position nudges after a head lock) are
MEASURED from his render, not assumed. Full record: `projects/aw-code-trial-parents/RUN.md`.

**2026-10-20 — NEXT TEST (his idea): he records a CREATIVE-DIRECTION video for his next short and Claude makes it
fully in code** (the v4 engine from the trial). If it holds up he can post up to 3 shorts/day. The difference from the
trial: that was a copy (every decision read from his project); here Claude makes the decisions (soundbites + cut
points, pull-out vs push-in, transition types, caption colouring, music, SFX), so the sequencing goes back to him as
text for an OK before the build (see [[feedback-sequencing-before-edit]]). Sources: he puts the files in a folder
(YouTube is blocked on this PC, SESSION-START). Start it in a FRESH session; brief = walkthrough recipe
([[feedback-walkthrough-videos]]).

**2026-10-20 — FIRST SHORT BUILT IN CODE FROM HIS DIRECTION VIDEO: Katherine "day Michael died"** (ABW10 Seq 13,
`projects/katherine-day-michael-died/`, RUN.md = full record). Made in one session with no AE/Premiere/CapCut: hook stare +
Joe/MJ overlays picked by face scans, head lock (optical flow + detector), his Topaz chain headless + his jitter tweak per shot,
AE look from the trial's measured primitives driven by a job `timeline.json`, code captions (agent) at his ABW10 height
(line 1 y1093, NOT the ABW8 trial's 980), his whoosh/flash SFX. v2 delivered with a PLACEHOLDER morgue still (he was in
bed); his still in `raw/` + one finish re-render = final. Awaiting his review.

**2026-10-21:** Katherine short APPROVED after 3 review fixes (final in X:\Claude Projects\Exports). Next short = "How MJ's
Siblings Found Out He Died" (`projects/mj-siblings-found-out/`): he handed a locked edit BRIEF (5 YouTube sources), asked
for the RAW SEQUENCE in Premiere first, then a direction video, then the code build. Raw cut placed in ABW10 ("MJ Siblings
Found Out - raw cut", 56.8 s, beat 4 skipped, 05 replaced by his local CBS2 memorial); awaiting his direction video (RUN.md).

**2026-10-22:** MJ siblings built in code from his own re-edit of the raw cut + his Tella direction (v1-v4). His v4 review
("chocolate" skin, face artifacts, SFX -10 dB, captions on mouths) -> v5 exported to X:\Claude Projects\Exports
(`mj-siblings-found-out.v5.mp4`), awaiting his review. Root cause of the skin: untagged rawvideo pipes (BT.601 -> 709 drift
per splice) + a grade fitted on the wrong (Nick Walker) footage; fixed with BT.709-tagged pipes, one-pass assembly and HIS
grade fitted from his own pre/post pair. Details: the job's RUN.md + AW shorts LESSONS (2026-10-22 entries).

2026-10-24: third short built fully in code, Paris Jackson "won't post on his birthday" (`projects/paris-wont-post-birthday/`): raw sequence in ABW10 -> his edit + Tella direction video -> code build (MJ-siblings engine) -> v1 in `X:\Claude Projects\Exports\`, awaiting his review. New traps (Topaz token lapse = watermark, IG glitch line, podcast A/V -0.37 s, Premiere 30 fps display) are in the AW LESSONS.md.
- 2026-10-26: 'Joe Appointment' (MJ x Joe v3, projects/joe-jackson-appointment) — sequencing first in ABW10 (his order), his Tella direction video, then the 4th code build: v1 exported to Final Renders\Joe Appointment v3.mov (40.2 s, -13.8 LUFS, QA PASS), awaiting his review. New in the build: LK freeze-frame hook, per-shot letterbox band (finish.py), stage_a freeze.
- 2026-10-27: Joe Appointment v2 exported (his v1 notes: hook from the SAME interview, JOW blurred background full screen, music removed = his job); he UPLOADED v2 the same day with no further notes (shipped after one review).

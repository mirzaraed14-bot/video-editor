---
name: project-abundance-shorts-automation
description: "Ongoing goal (started 2026-09-14) to automate the user's Abundance Wisdom shorts workflow; style spec lives at presets/youtube-shorts/abundance-wisdom/style-spec.md"
metadata: 
  node_type: memory
  type: project
  originSessionId: 7173e089-1e87-4811-944b-8e4043fa359d
  modified: 2026-09-23T15:02:18.986Z
---

Goal: automate the full Abundance Wisdom shorts edit (soundbite stitching → head-lock → Topaz → captions → zooms/transitions → audio → export) to match the user's hand edits. Started 2026-09-14.

State: style reverse-engineered from 3 exports + the user's spoken workflow, written to `presets/youtube-shorts/abundance-wisdom/style-spec.md` (DRAFT). Nothing built yet.

**Why:** the user edits every short by hand across Premiere → AE → Topaz → CapCut → AE → Premiere; they want Claude doing execution while they direct.

**How to apply:** read the style spec before any work on their shorts. The user downloads the YouTube source clips themselves — Claude works from the downloaded files. Their tools on this machine: Topaz Video AI (CLI ffmpeg with tvai_* filters, preset `C:\ProgramData\Topaz Labs LLC\Topaz Video AI\presets\Iris Preset.json`), AE 2025 with Sapphire + Deep_Glow_v1.2, caption font Gretaros-Regular.otf (user fonts). See [[user-abundance-wisdom-editor]].

The Content Engine (their Cowork project) is readable on disk at `E:\Claude Projects\Abundance Wisdom\` (ENGINE.md = method, FINDINGS.md, RESULTS.md, per-short `*-CUT.md` / `*-CUTSHEET.md`). The chat history itself is NOT accessible from here. A "FINAL LOCKED BUILD" in a `*-CUT.md` is the edit input: numbered beats of quote / source title / YouTube URL / in → out timestamps. Read-only for Claude here: don't edit those files unless asked. The final export can deviate a lot from the locked build (Biles short used anchor + experts despite a one-speaker cutsheet), so the diff between build and export is where their editing judgment shows. Grade preset in use: **`Affan CC Preset.ffx`** (Lumetri + Curves; identical md5 to `2.ffx` in the Downloads "Main CC Presets" pack). Their whole AE preset library is at `C:\Users\affan\OneDrive\Documents\Adobe\After Effects 2025\User Presets\` (Deep Glow Caps, Deep Glow Line Preset, fade/brightness transitions, BlurMoCurves combos) plus their own ExtendScript `After Effects - Adjustment Layer T.jsx`, which aligns each adjustment layer to the clip below and stretches its S_BlurMoCurves keyframes (they already script AE).

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

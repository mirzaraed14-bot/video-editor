# BRIEF: "Harry Potter Can't Watch Himself" (AW Short), STOP 2 = the finished .mov (code-built, nothing written to Premiere)
▶ STATUS: written 24 Nov 2026 (machine clock ~10:40) on Affan's "start till finish, give me the short". Resume here: `BUILD-SPEC.md`, then `RUN.md` ▶ STOP 2.

## What he asked (in order)
1. STOP 1 raw cut (done, ABW11): his live edit = 31 clips, 30.70 s (`premiere/readback_live_raw_*.tsv`, unchanged 08:03 -> 10:29).
2. Tella 23 Nov: Polaroids of Harry per film (1-8) on a black canvas over "baby photos of yourself"; a photo of Radcliffe + his son (he sent it in chat; "upscale if you have to"); "the classic Abundance Wisdom style"; "improve the editing by 1 %".
3. "no sfx for polaroids".
4. "start till finish, give me the short": the code-built finish, delivered as `outputs/*.mov` + the two copies. **Affan exports from Premiere himself: nothing is exported or written there.**

## Catalog pass (CLAUDE.md rule 5) — HONEST STATE
Read: the FX list and the references named in `research/effects-catalog/CATALOG.md`; NOT done: a frame-by-frame look at all 137 images in `research/effects-catalog/shots/` (a gap; flagged in the delivery). Moves that fit this Short: FX-29 Float Frame / FX-08 Black Table Tiles (object cards on black: the Polaroid scenes), FX-40 Slow-Burn Portrait (a slow push on one photo: the Radcliffe + son card), FX-37 Ghost Dissolve (not used: he cuts hard), FX-80 Black-Beat Ident (not used). Used on the last AW Shorts and kept: the soft zoom curve, the AW caption/label kit, the CTA pills, soft SFX under labels.

## What this Short does better than the last one of its kind (1 %)
- Objects, not cards: the Polaroids are a code-built object scene (pop with an overshoot, a rotation settle, a develop ramp inside every photo, bloom on the paper, 10-sample motion blur, ONE camera push on the AW curve), measured against the frame edges on every frame.
- **Caption-aware layouts:** the two Polaroid scenes keep a clear band (y 893-1174) for the captions, so the line they sit under stays readable (measured, `proof/`).
- A non-speaking Half-Blood Prince cover: Harry's lips do not move under Radcliffe's voice (v1 of the cover did).
- Every source picture is the best stream on disk (VP9 617 / 616, the old H.264 for Ross), compared at full size in STOP 1; no AI on any real face.

## Rules for this build (hub + memory)
Hook = claim only (no credit card under 0-3 s); labels LOW (y 1260-1280); captions just under the lips, one base; two subtle CTA pills in the gaps (never a label, a Polaroid, the first 5 s, the last 3 s); no music; no SFX on the Polaroids; kit SFX elsewhere; Lanczos only on real faces (no Topaz / Iris / Higgsfield); censor drug / self-harm words (none expected); media on X:; ASR on CPU under `.asr-lock`; GPU work through `build/glock.sh`; no YouTube access (everything is on disk).

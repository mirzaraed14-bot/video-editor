---
name: feedback-sourced-stills-must-be-hq
description: "Any picture pulled from the web (cutout photo, screenshot, still) is checked at full size and, if soft, enhanced in Higgsfield before it goes on the timeline — never place a blurry source"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: e1b9cd8c-a044-4294-9e79-318eb202a8a0
  modified: 2026-09-19T02:35:51.804Z
---

The creator's standing rule for web-sourced pictures (told 2026-09-19, while briefing the Travis Scott video):
*"whatever pictures you source from Google make sure that they're high quality, or if they're not you go into
Higgsfield and enhance the quality of the picture… the prompt is really really simple… then bring it back into
Premiere."* They already do this by hand on every video.

**Why:** their explainer format puts stills and cutouts full-screen (inset over a grained matte) at 1080p; a
soft Google image reads as cheap next to the game footage and the graphics.

**How to apply:**
- Every web-sourced image — a photo for a PNG cutout, a post screenshot, a credit line, a still — is opened at
  full size first. If it is small or blurry, run it through **Higgsfield's image enhance / upscale** with a
  one-line prompt ("enhance quality, keep everything as is"), then place the enhanced file. Costs credits: check
  the balance first ([[reference-higgsfield-connector]]).
- Do it before the image touches the timeline, not as a fix afterwards.
- Applies to both channel formats; logged in `presets/youtube/affan-afterhours/LESSONS.md` and the job's
  `STYLE.md` § 4b. Related: [[project-gta-documentary-channel]].

**Update 2026-10-23 (War Dogs, Affan: "wtf is that overlay"):** a Topaz Iris 2x on a small press photo of a real person made it
look waxy and fake (the real Efraim Diveroli with a rifle), and a tight 9:16 crop of a wide movie still showed half a face. Sharp
means a genuinely high-res source, not an AI upscale of a soft one: when only a soft photo exists, find another picture, or show it
in a panel over a blurred copy (as the 720p diamond clip was) instead of filling 9:16. Check every overlay's actual crop at full
size before the render. See [[feedback-face-cam-max-4s]].

**Update 2026-11-03 (AW Paris Shock Therapy, Affan on v1: "both these images need to run through a serious higgsfield upscale
before making it into the video"):** it applies to sourced overlay CLIPS too, not only stills, and on AW Shorts it is the default
step, not an offer. A soft sourced photo AND a soft paparazzi clip both got it: `upscale_image` bytedance 4K (2 credits) → lanczos
down to the played size; `upscale_video` Topaz 2160p on the exact played 9:16 crop, short excerpt with handles (5 credits / 2.7 s).
Then check the result UNDER HIS GRADE in a finished still: a hot source still blew out and needed a pre-grade level (AW LESSONS
2026-11-03). The War Dogs caution still holds for tiny press photos of real people (waxy): judge the upscale at full size.

## Moved from the MEMORY.md index (2026-11-06)
any web-sourced picture is checked at full size and enhanced in Higgsfield if soft, before it touches the timeline; 2026-11-03: on AW Shorts sourced stills AND clips get a serious Higgsfield upscale by default (4K image / Topaz 2160p clip), then checked under his grade

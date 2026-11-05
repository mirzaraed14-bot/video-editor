# Long-form style radar: what other channels do that ours doesn't

Same idea as `research/shorts-style-radar.md`, for talking-head long-forms. Affan, 2026-11-05: "steal something from other channels, like style wise or
effect or motion graphic wise or style concept". A dated section per pass; what a video actually took goes in that video's BRIEF.

## Method (silent by construction, no player, no ad, nothing downloaded)
Open `https://www.youtube.com/robots.txt` in his Chrome (same origin, no player on the page), `fetch('/watch?v=<id>')`, read
`playerStoryboardSpecRenderer.spec` out of the HTML, and put the top level's sprite URLs into `<img>` tags. Top level = 320x180 thumbnails, 3x3 per sprite,
one every 10 s, so sprite N covers frames 9N to 9N+8. No video element ever exists, so no sound can play. Frames show layout and colour, not cut rate or sound.
Why not the watch page: logged out it runs ads (33 s, then more), and a bare `/embed/` tab refuses with "Video player configuration error".
Plain web search on this topic returns only SEO lists, no real style read.

## Pass 1, 2026-11-05 (for AffanWiz, job started from C1449)
| Video | Type | What it does that we don't |
|---|---|---|
| **Coffeezilla, "I Investigated $100 Billion in Healthcare Fraud"** (`9eWJISlh0fw`), 9:00-10:20 | host + evidence, 5M+ views, 48 min | **The tilted evidence map.** A dark floor in perspective, hairline frames for each actor (Telemarketers, Reliable Results, Prince Laboratories, Telehealth), a dashed red-and-white route running node to node with its label set along the line ("Order Tests"), small icons at the nodes, the camera flying along the route, then a pull-back to the whole web. A venetian-blind light texture sits under it. The host cuts in between visits, so it reads as one object the story keeps returning to. Reference: `projects/<job>/brief/refs/coffeezilla-9eWJISlh0fw-9m00-10m20-storyboard.jpg`. |
| same video | | Red keyword inside a white quote over the darkened host ("I DON'T PUT IT PAST THEM, TO HIRE **HITMEN**"): FX-18/FX-27, still current. Documents as plain white-on-black type with one red-underlined phrase, no fake page. |
| **Johnny Harris, "The REAL reason China built so much"** (`axRhjqd-rus`) | face-led explainer | **The chart zoom.** The whole chart draws, then the camera pushes into the line until it fills the frame, then returns to the full chart with the other series. Also **pictogram rows** instead of bars: one icon = N people, rows fill in, a colour fills part of them ("PARTY MEMBERS ~101,000,000"). On paper-toned pages with call insets on the same paper. Reference: `projects/<job>/brief/refs/johnnyharris-axRhjqd-rus-storyboard.jpg`. |
| **Colin and Samir, "Why Instagram Completely Changed Its Mind"** (`sxizdQ2hRfk`) | creator-economy two-camera talk | Almost nothing but two faces and a wide. The only graphic is the real artifact (phone screen, magazine page) dead centre on pure WHITE, which reads very clean after the dark room. Worth remembering as a contrast beat. |

Compared with the catalog (FX-01..81): the tilted map is a new variant, flat diagrams and FX-09 Demand Tree are the nearest. Not used on AffanWiz yet.

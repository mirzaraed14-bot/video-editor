# GTA 6 B-ROLL SCENE INDEX

Built 2026-10-08 by reading every frame sheet (1 frame / 2 s for the Extended Look, 1 frame / 1 s for both trailers) and confirming key moments at full size. This describes what is on screen, not what Rockstar says it is.

**Sources** (all in `projects/gta6-pc-release/broll/`, all 1920x1080, 30 fps, AAC audio):

| Key | File | Length | Notes |
|---|---|---|---|
| **EL** | `GTA 6 Official Extended Gameplay.mp4` | 26:48 | Full frame, no letterbox. Mix of cutscene (no HUD) and live gameplay (HUD). The "Extended Look". |
| **T1** | `Grand Theft Auto VI Trailer 1.mp4` | 1:30 | Full frame, no letterbox. No game HUD anywhere; the only UI is the social-media feed overlays (0:41-0:59). |
| **T2** | `Grand Theft Auto VI Trailer 2.mp4` | 2:46.8 | **Baked letterbox from 0:06 to 2:36**: the picture sits in a 1920x864 band (crop = `1920:864:0:108`). No game HUD. |

**Timecodes** are `m:ss` of source time. Every sheet label was set from the exact source frame (not the fps filter, which drifted up to ~1 s on the trailers), so a timecode here puts you on the shot. **Every range quoted in the SUBJECT INDEX was re-checked by pulling frames at its start, middle and end (and the fuzzy ones at 0.25-0.5 s steps); those edges are good to about +/-0.5 s.** Rows in the shot tables are +/-1 s unless a time carries a decimal. Scene-cut detection misses dissolves, so do not trust a boundary that has no decimal. Always give yourself a half-second of handle.

**Sheets** are in `frames/EL`, `frames/T1`, `frames/T2` (`sheet_NN.jpg`, 60 s per sheet; trailers also have `fine_NN.jpg` at 1 s sampling, 30 s per sheet). Full-size confirmation frames are in `frames/*_confirm/`. Full-res (1920x1080) stills of the best picks are in `frames/stills/` (named `SRC_mmss_subject.jpg`, the mmss is the frame's source time; 62 stills). `frames/T1/fine_*` and `frames/T2/fine_*` are the 1-second trailer sheets.

## Character key (so "who" is readable)

- **J = Jason.** Short cropped dark hair, stubble, muscular. Outfits by scene: cream/white tee (EL night, 0:08-6:00); white tank then black short-sleeve shirt, sunglasses (EL 6:28-12:30); backwards cap, grey tee (EL 13:10-17:06); olive tee, cap (EL 16:48-17:06); camo shorts + frog-print tee with a bandana mask in the store (EL 11:26-12:06); olive suit jacket over black tee (EL 19:22-26:00).
- **L = Lucia.** Dark curly hair (ponytail, bun, or down), gold hoop earrings. Outfits: green crop top + denim shorts (EL night); brown top + jean shorts (bedroom); magenta halter dress (EL 8:02-11:26); black "DON'T TRIP" leather jacket + red bandana (EL 11:26-12:10); grey hoodie, then grey "BADDIE" crop top (EL 13:10-17:06); yellow tropical shirt + pink bandana (EL 17:53-18:00); **a dark shoulder-length bob + black blazer/dress for the party sequence (EL 19:08-25:40)**, a different look from the curly-haired Lucia elsewhere, confirmed by the "Lucia:" text banners at 23:48-23:56.
- **NPC** = anyone else. "(?)" after a name means the identity is a best read, not a certainty.

**HUD column:** `none` = clean cutscene or trailer picture. `MM` = minimap (bottom-left, pink route line). `*` = wanted-level stars (top-right). `AM` = weapon/ammo (top-right). `PR` = button prompt (bottom-right or beside the subject). `UI` = other game overlay (phone call, text banner, livestream, race timer, weapon wheel, mini-game counters). **D/N** = day / night (`dusk` where relevant).

---

# 1. EXTENDED LOOK (EL), 26:48

### Cold open

| Time | What's on screen | HUD | D/N | Good for |
|---|---|---|---|---|
| 0:00-0:03 | ESRB "Likely Mature 17+" card on black | none | - | title card, rating |
| 0:04-0:07 | Rockstar logo fades in and out | none | - | logo, stinger |

### Night: apartment block, drug den, raid (0:08-6:00)

| Time | What's on screen | HUD | D/N | Good for |
|---|---|---|---|---|
| 0:08-0:19 | J (cream tee) + L (green crop top, shorts) walk from behind toward a lit, run-down apartment entrance; parked cars, empty street | none | N | **J+L walking**, establishing, night street |
| 0:20-0:44 | Graffiti vestibule with bench: J (back) + L talk to three NPCs (shirtless tattooed big man with towel, man in red vest, man in blue shirt); more NPCs on bench | none | N | J+L standing/dialogue, NPC group |
| 0:44-0:49 | J + L walk past the NPCs to the glass door | none | N | walking, entering building |
| 0:50-0:58 | Tiled lobby hallway, red wainscot, mailboxes; J from behind, L beside | none | N | walking hallway |
| 0:58-1:22 | Elevator lobby: NPCs (cowboy hat + green jersey; big man white tee, gold chains) talk; L at right edge; small prompt icons 1:00-1:05 | PR | N | NPC dialogue |
| 1:22-1:28 | Elevator doors open on a graffiti interior; J, L and the big NPC step in | none | N | elevator |
| 1:28-1:50 | Inside the elevator: big NPC (gold chains) scrolls his **phone** 1:32-1:46; J back of head in the foreground, L partly visible | none | N | **phone** (NPC), elevator |
| 1:50-1:56 | Dark common room, NPCs around a lamp-lit table, J enters | none | N | NPC den |
| 1:56-2:04 | J (white tee) crouches to a pit-bull **dog**; NPC in yellow cap; prompts SCOLD/PET/STUDY bottom-right | PR | N | dog, J alone |
| 2:04-2:14 | J walks a long tiled hallway toward a blue-lit end | none | N | **J alone**, hallway |
| 2:14-2:34 | J at red door "907", KNOCK prompt 2:14; L behind him 2:14-2:18; peephole slides open to an eye/face 2:22-2:30 | PR | N | knocking, J+L, door |
| 2:34-2:44 | J enters a dim apartment (ceiling fan), drug-lab table beyond | none | N | entering |
| 2:46-2:58 | L + J stand side by side before a shirtless dreadlocked man (gold chains, "SS" pendant); masked cooks in yellow gloves at 2:56 | none | N | **J+L two-shot**, drug lab |
| 3:00-3:25 | Dreadlocked man talks to camera; J close-up 3:04; NPC holds up a phone 3:12; masked cooks behind | none | N | NPC close-up, phone (NPC) |
| 3:25-3:42 | White-tank tattooed man and dread man check a phone 3:26-3:28; **L + J two-shot under a desk lamp 3:30-3:34** (L grey crop top, J white tee); cooks 3:36-3:38 | none | N | **J+L two-shot**, phone |
| **3:42.7-3:45.5** | **Phone UI close-up**: smartphone on a scratched table, incoming call "Unknown" with red decline button | UI | N | **phone UI, incoming call** |
| 3:45.5-4:04 | NPC close-ups, cooks, dread man alarmed 3:40-3:42, red duffel and sneakers 3:54, dread man on phone 4:00-4:02 | none | N | NPCs, drug lab |
| 4:04-4:10 | **Police raid**: SWAT/POLICE officer with shotgun in the hallway 4:06; cooks scatter in flashlight 4:08 | none | N | police raid |
| **4:10.3-4:11.3** | Phone ringing on the table in a torch beam (second call-UI shot) | UI | N | **phone UI** |
| 4:11.3-4:16 | L + J scramble in the den, lamp, J ducks at the table 4:14 | none | N | J+L together, action |
| 4:16-4:30 | J (white tee) fights through the den, sparks 4:16, ammo HUD appears; prompt "HOMELAND 870 SHOTGUN" 4:28 | AM PR | N | gunfight, **J alone** |
| 4:30-4:55 | J (red duffel strap, shotgun) fights down hallways: door 4:34, mattress barricade 4:36, firefight 4:46, drywall blown out 4:46-4:50 | AM | N | **firefight on foot**, hallways |
| 4:56-5:04 | SWAT officer with rifle in hall 4:56; J + L in graffiti elevator 4:58; hallway melee with floral-shirt NPC 5:00-5:02 | AM | N | action |
| 5:04-5:08 | **J + L close two-shot in the graffiti elevator** (J red-strap bag, L grey crop top); J face close 5:06 | none | N | **J+L together close** |
| 5:08-5:12 | Green-lit common room, NPCs and bodies (cutaway) | none | N | aftermath |
| 5:13-5:21 | Back in the graffiti elevator: **J (white tee, red bag strap) and L (grey crop top) side by side**, dim, J looks down; fades to black at 5:22 | none | N | **J+L together close**, dialogue |
| 5:26-5:31 | J with shotgun in green hallway, weapon icon top-right | AM | N | on foot, J alone |
| 5:32-5:49 | Candlelit apartment, NPCs scatter, J with shotgun and duffel | AM | N | firefight |
| 5:50-5:59 | **Very dark top-down from a balcony** over a trash-strewn alley with "KEEP CLEAR" stencilled on the ground; L (grey tank) leaps/falls into frame 5:56-5:59 | none | N | alley, top-down, trash |

### Day: Lucia's apartment, car, intro logo (6:00-9:00)

| Time | What's on screen | HUD | D/N | Good for |
|---|---|---|---|---|
| 6:00-6:05 | Black, then "ROCKSTAR GAMES PRESENTS" card | none | - | title |
| 6:05-6:09 | Man (camo shorts) at a red '70s sedan beside a tow truck, mural behind; prompts SLIM JIM / SMASH WINDOW | PR | D | **car break-in prompt**, parked cars |
| 6:09-6:13 | Red Chevelle convertible drifts on a road in smoke; **L (ponytail, red bandana, white tank, sunglasses) leans out of the window**, close-up 6:12 | none | D | L in car, joyride |
| 6:13-6:20 | GTA VI logo reveal on dark | none | - | logo |
| 6:20-6:24 | Day street: delivery trucks, **NPC jogger (magenta bodysuit, braids)** runs toward camera | none | D | NPC, street |
| 6:24-6:27 | Fridge door close-up with sticky notes and magnets (Lucia's flat) | none | D | home detail |
| 6:27-6:29 | Top-down bedroom floor, teddy bear, clothes | none | D | home detail |
| 6:29-6:36 | Pink bedroom: **J (white tank) + L (brown top, hair bun) close**, he holds her wrist, her bag | none | D | **J+L at home** |
| **6:36-6:44** | **L lies on the pink bed in jean shorts looking at her phone** | none | D | **L alone, phone**, bedroom |
| 6:44-6:46 | J (black shirt) bends at the vanity, watch/shoes | none | D | home |
| **6:46-6:51** | **L at the wardrobe holding two hangers, choosing an outfit** (magenta curtains) | none | D | **outfit change, L alone** |
| 6:51-6:58 | Teal room with lit vanity mirror: J (dark button shirt) at the mirror, L from behind with clothes | none | D | home, J+L, mirror |
| 7:00-7:10 | J (dark shirt, back) alone in the flamingo-wallpaper hallway; L fades off left; prompt 7:08 | PR | D | **J alone, home** |
| 7:10-7:25 | J wanders the pink kitchen/living room, fridge open 7:16-7:20 (sticky notes, photos), prompts TURN ON / DRINK / PUT DOWN | PR | D | **J alone**, kitchen |
| 7:26-7:46 | **In-world TV**: cartoon brain/creature ads, nature documentary (elk, deer, hares, ducks) | none | D | in-world TV, easter egg |
| 7:47-7:58 | TV ad: "The Prairie Sandwich Box Meal" burger spot | none | D | in-world ad |
| 8:01-8:04 | Orange apartment block exterior, skyline; L in magenta halter dress at the door (8:02), J's arm at right | none | D | exterior, J+L |
| 8:04-8:20 | **J (black shirt, sunglasses) walks under the carport** and gets into a red convertible | none | D | **J alone**, carport/parking, car entry |
| 8:20-8:58 | **Driving**: red convertible from behind through Vice streets, cement mixer 8:30, bus, traffic; two heads visible in the car at 8:58 | MM | D | **driving**, minimap, city traffic |
| 8:58-9:02 | Bridge: **shirtless NPC in pink trousers leaps off the bridge rail** onto a jet ski (seen from below) | none | D | NPC chaos |

### Open-world montage (9:00-9:34, one to three seconds each, all NPCs)

| Time | What's on screen | HUD | D/N | Good for |
|---|---|---|---|---|
| 9:02-9:04 | Neon Ocean Drive at night, red sports car; NPC thrown on the road | none | N | night street, NPC chaos |
| 9:04-9:09 | Pink strip-mall shop front ("A1 Fashions"), man in blue shirt with red cup, vending machines, **man sitting on the kerb**; EAT/DROP prompts | PR | D | NPC crowd, street corner |
| 9:07-9:10 | Run-down garage, NPC scuffle, tyres | none | D | garage |
| 9:10-9:11 | Low angle: man (white tee) with rifle, woman with bat, palms | none | D | NPC |
| 9:11-9:14 | Night street: burning cars, man with red backpack shooting at NPCs, ammo HUD | AM | N | street fight, fire |
| 9:14-9:21 | Motel courtyard: man in black tank (back) walks, **NPC in pink nightgown** beside an old sedan | none | D | motel, NPCs |
| 9:21-9:25 | Abandoned graffiti building, woman with bat and backpack, ammo HUD | AM | D | abandoned building |
| 9:25-9:29 | **Backyard wrestling ring**, crowd | none | D | NPC crowd, fun |
| 9:29-9:31 | **Armoured truck ("Gruppe 6") holdup**: masked gunmen, guards on the ground, motorbikes | none | D | heist, armoured truck |
| 9:31-9:33 | Aerial of a rooftop bar with ocean and skyline | none | D | rooftop, skyline |
| 9:33-9:35 | Rooftop patrons seated, skyline behind | none | D | NPC crowd |

### Rooftop date: J + L (9:35-11:26)

| Time | What's on screen | HUD | D/N | Good for |
|---|---|---|---|---|
| **9:34.8-9:46** | **Elevator: J (black shirt, sunglasses, shoulder in frame) looks at L (magenta halter dress, sunglasses) leaning against the wall** | none | D | **J+L close two-shot**, romantic |
| 9:46-9:50 | Doors open on the "Effluvia" lobby; they step out; HOLD HANDS prompt | PR | D | entering venue |
| **9:50-10:19** | **J + L hold hands and walk (from behind) along a sunny rooftop bar**, NPC patrons, balloons, skyline; HOLD HANDS prompt 9:48-9:52 and 10:00-10:02 | PR | D | **walking hand in hand**, date, rooftop |
| 10:19.7-10:24.6 | Flash cutaway: **handcuffed men and a woman arrested** on a terrace ("PUBLIC LOCKER RENTALS" sign), orange light | none | dusk | arrest, flash-forward |
| 10:24.6-10:39 | Dark cutaway: man in yellow floral shirt and cap, silver-bob woman in white tank, security monitors 10:34, body on floor 10:38 | none | N | dark drama, security room |
| 10:39-10:45 | Effluvia rooftop sign and patrons at sunset | none | D | rooftop |
| **10:45-11:12** | **J (black shirt) + L (magenta top) seated at a table** with an older man (tropical shirt, shades) and a blonde woman (floral top); drinks | none | D | **J+L together, dialogue**, drinks, rooftop |
| 11:12-11:26 | J + older man at the rooftop rail, skyline; J vapes (SMOKE prompt 11:24) | PR | D | J with NPC, skyline |

### Store robbery (11:26-12:16)

| Time | What's on screen | HUD | D/N | Good for |
|---|---|---|---|---|
| 11:26.5-11:28 | **J close-up** (stubble, frog-print grey tee) outside the store in golden daylight, head turned | none | D | **J alone**, close |
| **11:28-11:34.4** | **Gas-station store entrance ("OPEN 7 DAYS")**: L (black "DON'T TRIP" skeleton leather jacket) pulls up a red bandana 11:28; J (grey tee, back) and L go in through the glass door 11:29-11:33; L extends her pistol at the seated customers/clerk 11:34 | none | D | **store robbery, entering**, J+L |
| **11:34.4-11:36** | L (bandana up, black leather jacket) swings round in the doorway and raises her pistol 11:35; at 11:36 she aims at a man beside an old sedan outside | none | D | **gun aimed / holding up** |
| 11:36-11:41.8 | Outside: L aims at a man by an old sedan, dust, golden light | none | D | gun aim, outdoors |
| 11:41.8-11:45.7 | Car body close; clerk (respirator, yellow gloves) at a red toolbox 11:44 | none | D | NPC |
| **11:45.7-11:52.8** | **Store interior**: L (jacket back) walks the aisle past beer coolers; clerks duck; **wanted stars + ammo top-right**; ATM at right (11:51) | * AM | D | robbery interior, wanted HUD, ATM |
| **11:52.8-11:56.2** | **Behind the counter: clerk at the liquor shelves, J (grey tee, back) steps in, then masked J (cap, bandana) grabs and shoves the clerk 11:54-11:55.5** | AM | D | **holding up the clerk**, J alone |
| **11:56.3-12:02.4** | **Low-angle close two-shot: L (red bandana, glasses, white tank; later cap + shades) + J (grey bandana, frog tee; later cap)** masked: in the aisle 11:56, outside under the "Food Mart" sign 11:58, back inside 11:59.5, outside again 12:01 | none | D | **J+L together**, masked, hero shot |
| 12:02.4-12:03.8 | Convex mirror: clerk (blue shirt) levels a shotgun | none | D | clerk with gun |
| 12:03.8-12:09 | J (masked, cap, frog tee) in the aisle with a pistol 12:04, crouches in camo shorts 12:05.5; clerk down; man near the red-lit shop door 12:07-12:08; stars top-right | * | D | robbery, gun |
| 12:09-12:11.6 | L (bandana, white tank) low angle at a car window | none | D | getaway start |
| 12:12.5-12:15.5 | NPC in a white shirt and beige trousers in front of FOOD MART aims a shotgun at passing cars | none | D | NPC with gun |

### Rooftop callback, highway, car planning (12:15-14:00)

| Time | What's on screen | HUD | D/N | Good for |
|---|---|---|---|---|
| 12:15-12:31 | J + older man at the rail, skyline; **red news helicopter with banner** 12:26-12:30; SMOKE prompt | PR | D | skyline, news helicopter |
| **12:30-13:10** | **Driving a dark-grey sedan along a coastal highway at low sun**, palms, bridge, port cranes, towers; minimap with pink route | MM | D golden | **driving, golden hour**, highway |
| **13:10-13:26** | **Car interior (daylight): J (backwards cap, grey tee) drives and checks his phone 13:12-13:14; L (curly hair, grey hoodie) beside him**, talks (13:18), looks to camera (13:22); billboard "OVER A NEW LEASE" | none | D | **J+L in car**, dialogue, **phone** |
| 13:26-13:40 | Dim interior: **bearded man (glasses, brown jacket, scarf) in the back seat** leans forward 13:28-13:30; L turns to him 13:32-13:36 | none | D | car interior, back-seat passenger |
| 13:40-13:48 | L driving (hands on wheel POV), bearded man smiles in back 13:42-13:46 | none | D | car interior |
| 13:48-14:00 | L (red bandana) at the wheel; J masked (cap, bandana) in back, pistol 13:56 | none | D | masking up |

### Police chase and getaway (14:00-16:16)

| Time | What's on screen | HUD | D/N | Good for |
|---|---|---|---|---|
| 14:00-14:02 | J (cap, bandana) aims a rifle from the car window, police lights at left | AM | D | police chase |
| **14:02-14:33** | **Gunfight: J crouched behind a car firing at police SUVs/trucks**; helicopter 14:02-14:08; police SUV wrecked 14:08; **police truck flipped 14:10 and again 14:22**; garage entrance 14:14; dumpster alley 14:24-14:28. **5 wanted stars + ammo top-right; red/blue flashing detection box bottom-left** | * AM MM | D | **police chase/shootout, wanted level, cars damaged**, alley |
| 14:33-14:42 | Black sedan drives off, passes a bus; burning wreck in the distance 14:40 | none | D | getaway |
| 14:42-15:00 | Interior: L (red bandana) drives, looks back 14:42; bearded man and J talk 14:44-14:46; L close face 14:50-14:54; bright garage tunnel ahead 14:56 | none | D | car interior, L at wheel |
| 15:00-15:16 | Bearded man close talking 15:02-15:08; L driving toward the garage 15:10-15:14; J masked in back 15:16 | none | D | car interior |
| **15:17-15:50** | **Getaway: dark sedan down a white ramp, through alleys and streets**; wanted stars + minimap flashing blue/red; **cops chase on foot 15:30-15:34 and 15:40-15:42**; police car 15:44 and 15:48 (two cruisers); helicopter 15:46 | * MM | D | **getaway driving, police chase, cops searching**, alley |
| **15:50-15:58** | **Car glides into a dark parking garage; stars and minimap turn grey (evaded)** | * (grey) MM | D to dim | **cops searching/cooling**, parking garage |
| 15:56-15:59 | L exits, door open; blurred weapon/item wheel with cash top-right 15:58 | UI | dim | weapon wheel UI |
| 16:00-16:04 | Garage: L (red bandana, grey "BADDIE" crop top) + J (black tee) + driver | * | dim | J+L, garage |
| **16:04-16:09** | **Getaway sedan set on fire (fireball and sparks)**; L walks away | * | dim | **car damaged/burning** |
| 16:09-16:16 | Loading duffel bags into a maroon van, man in green pants and cap | MM | dim | parking garage, loading cash |

### Van, cash handoff (16:16-17:06)

| Time | What's on screen | HUD | D/N | Good for |
|---|---|---|---|---|
| 16:16-16:32 | **Driving a maroon van** along a bayfront road, stop signs, green bike lane, toll arch ahead; minimap | MM | D | driving, minimap |
| 16:32-16:39 | Van passes under the toll arches; **aerial drone-style shots** of the road, tennis courts, bay and skyline 16:34-16:38 | none/MM | D | **aerial, wide map-feel**, skyline |
| **16:39-16:48** | **Back-of-van alley: bearded man (brown jacket) takes a duffel bag from L (grey hoodie crop) and J (cap, dark tee)**, cash handoff | none | D | **cash handoff, buyer**, J+L |
| 16:48-16:53.5 | J and L at the open van door, purple-tiled wall; J walks past the van 16:52 | none | D | J+L |
| **16:54-16:57.5** | **J (dark tee, backwards cap) + L (grey "BADDIE" crop top) stand close, both facing camera**, red Leonida City Roast van behind them | none | D | **J+L together close** |
| 16:58-17:00 | Empty sunny street beside the van, a motorbike rider far off | none | D | street |
| **17:00-17:04.5** | **J + L close by the cobalt-tiled wall**, "WARNING cameras" sign above; J looks up, L (hair now in a high ponytail) looks past camera, her face close 17:04 | none | D | **J+L together, alley** |
| 17:05-17:07 | L (grey hoodie, curly hair) walks away from camera along the tiled wall | none | D | **L alone, walking, alley** |

### Activity montage (17:06-17:50, all one-to-four second shots)

| Time | What's on screen | HUD | D/N | Good for |
|---|---|---|---|---|
| 17:06-17:10 | Colourful graffiti street, e-scooter rider's legs | none | D | street |
| 17:10-17:13 | **Airboat** in a green bayou, minimap | MM | D | **airboat, swamp** |
| 17:13-17:16 | Man (white tank, cap) with basketball at a stilt-house hoop | PR | D | basketball |
| **17:16-17:18.7** | **Scuba diver in an underwater cave**, rays | UI | D | **scuba, underwater** |
| **17:18.7-17:22** | **L (grey crop top, ponytail) bench-presses in a gym**, top-down camera, green "GAINZ" plates | none | D | **gym, workout, L alone** |
| 17:22-17:25 | **Shirtless man runs down a pier and dives into the sea**; dolphins at the horizon | none | D | pier, swimming |
| 17:25-17:27 | Jet ski / boat at sunset, minimap | MM | dusk | watercraft |
| 17:27-17:29 | Binocular view through a lit window (green lens) | UI | N | binoculars, spying |
| **17:29-17:31** | **Woman kayaking a canal** with skyline and marina, minimap | MM | D | **kayak** |
| 17:32.5-17:41 | **Night-club door ("Jack of Hearts", ID CHECK signs)**: man in green varsity jacket greets a plaid-shirt man 17:36; a couple hug/kiss 17:38-17:39; club floor with a pole dancer 17:40-17:41 | none | N | nightclub door, ID check, strip club |
| 17:42-17:47 | **Street race**: white #06 tuner sedan, LAP 1/2, position 11/16 to 9/16, timer, minimap | MM UI | D | street race |
| 17:47-17:50 | Woman (red tank) seated on a roadside slab above a highway; road-arrow top-down 17:48-17:49 | none | D | roadside |

### Pawn shop approach (17:50-18:00)

| Time | What's on screen | HUD | D/N | Good for |
|---|---|---|---|---|
| **17:50-17:51.5** | **Item wheel over a blurred red convertible**: WEAPONS tab ("UNARMED") 17:50.0-17:50.4, then ITEMS tab 17:50.5-17:51.4 showing **clothing/accessory slots: sunglasses, "ROD'S RACING CAP" (HEADWEAR, PUT ON), "FACE WRAP" (MASKS, ON), a hanger (WEAR STYLE 1/2, TAKE OFF)**; cash $15,150 / $700 top-right | UI | D | **changing outfit/mask UI**, weapon wheel |
| 17:51-17:53 | Red convertible parked at a strip mall (**Zeke's Gadgets, "WE DO REPAIRS", Joyeria Empeños pawn shop**); door open, masked driver (white tank) | none | D | parked car, shop front |
| **17:53-18:00** | **L (yellow tropical shirt, ponytail, pink bandana at her neck) walks up to the pawn shop with a pistol** (back view); NPCs in overalls and floral top watch; **a person lies asleep on the bench** (purple clothes, 17:52-17:57); ammo HUD from 17:55 | AM | D | **L alone, on foot, store front, homeless/sleeping NPC** |

### Jewellery store, getaway, livestream, activities (18:00-19:03)

| Time | What's on screen | HUD | D/N | Good for |
|---|---|---|---|---|
| **18:00-18:03** | **Jewellery store (Diamond Dawgs) holdup**: L (grey crop hoodie, maroon trousers) fights a man in the aisle; masked gunman at the door (camo shorts, J?) and hostage kneeling; clerk behind glass | AM | D | **store robbery, hostages**, melee |
| **18:03-18:12** | **Getaway on a motorbike**: runner in green "MARCUS 69" jersey with duffel jumps on behind a masked rider; wanted stars 6 to 2; crosses an intersection past a police truck | * | D | **getaway, motorbike, wanted** |
| 18:12-18:24 | Day street: woman (L?, white tee, ponytail, hoops) beside an open trunk with a person inside 18:12-18:14; **man in grey hoodie and shades films a selfie video** 18:16-18:23 | none | D | **phone, selfie**, trunk |
| **18:24-18:28.5** | **Driving down Ocean Drive; open trunk with a person inside; LIVESTREAM chat overlay (LIVE 51k, comments, VIEW LIVESTREAM)**; minimap flashing blue/red; stars | MM * UI | D | **livestream/social UI**, driving |
| **18:28.5-18:31** | **Beach**: yellow umbrellas, striped loungers, sunbathers, a dog, banner plane | none | D | **beach, sunbathing, crowd** |
| 18:31-18:35 | Shooting-range mini-game: woman aims at targets in a Spanish plaza, TARGETS REMAINING 7/12 and timer | UI | D | shooting mini-game |
| 18:35-18:39 | **Dirt-bike race** on a hillside, LAP 1/2, position 10/12, minimap | MM UI | D | dirt bike, race |
| 18:39-18:47.5 | **Night**: red convertible downtown, woman in red cap standing in the back, stars and minimap; **roadside explosion 18:46** | MM * | N | night driving, explosion |
| **18:47.5-18:59** | **Woman with backpack on a skyscraper edge (18:48), skydiving freefall (18:50-18:52), parachute open over Vice City's islands (18:54-18:58)** | none | D | **parachuting, skydiving, aerial Vice City** |
| 18:59-19:04 | Top-down aerial of city and beach (transition) | none | D | aerial |

### Airport lounge (19:04-20:00)

| Time | What's on screen | HUD | D/N | Good for |
|---|---|---|---|---|
| 19:04-19:07 | Two NPC men on a green couch with beers (teal "Manatees 13" jersey, camo shorts) | none | D | NPCs, couch |
| 19:07-19:20 | **Airport VIP lounge**: L (dark bob, black blazer, back) + blonde woman (pearls); planes through the windows; blonde close 19:18 | none | D | airport lounge |
| **19:22-19:35** | **Three-shot at the window: blonde (pearls) / L (bob, black blazer, gold "N" belt) / J (olive suit)**; waiter with champagne 19:34 | none | D | **J+L together**, dialogue, airport |
| 19:36-20:00 | **Night tarmac with a private jet**: woman descends the airstairs 19:36; fedora man and blonde kiss 19:40-19:44; L + J watch 19:46; black SUV | none | N | private jet, tarmac |

### Club arrival (20:00-21:00)

| Time | What's on screen | HUD | D/N | Good for |
|---|---|---|---|---|
| 20:00-20:08 | J (olive) by a black SUV, inside the SUV; SUV drives off | MM | N | night, SUV |
| 20:08-20:14 | SUV drives across the tarmac toward the lit skyline; minimap | MM | N | night driving, skyline |
| 20:14-20:16 | Purple-lit tower, low angle | none | N | skyline |
| 20:16-20:21 | Woman with a phone (selfie pose) 20:16-20:17, then the **night pool party**, dancers around a glowing pool 20:17-20:21 | none | N | **pool, party, phone** |
| 20:21.5-20:26 | **Dusk street race**: pink-underglow tuner, race HUD, minimap | MM UI | dusk | street race |
| 20:26-20:31 | **Packed nightclub floor**, strobes; woman (ponytail, pink dress) holds a drink on the balcony, DRINK/DROP prompts 20:29 | PR | N | **nightclub, crowd, drinking** |
| 20:31.5-20:36 | Low-angle MEGAMUNDO building and a rainbow-lit tower | none | N | skyline, night |
| 20:36-20:44 | Arrival: J in the SUV door; L (black dress) steps out; fedora man and blonde exit | none | N | arrival |
| 20:44-21:00 | **J (back) and group climb a candle-lit red carpet** to the Megamundo revolving door, purple/pink neon | none | N | club entrance |

### Party and tower (21:00-25:46)

| Time | What's on screen | HUD | D/N | Good for |
|---|---|---|---|---|
| 21:00-21:13 | Club lobby party with balloons: fedora man and red-jacket man chat with the bob-haired host woman (silver dress) | none | N | party, NPC dialogue |
| 21:13-21:32 | Host woman smiles to camera 21:22; group of blonde, L (bob), J (olive) 21:20; they step into an elevator 21:30 | none | N | **J+L together**, party |
| 21:32-21:37.5 | Doors close, then reopen on the party: J (olive suit, back) stands with L (bob), the blonde and a woman in red 21:33-21:37 | none | N | **J+L elevator** |
| **21:37.5-21:54** | **J alone in the elevator** (olive suit, back of head), presses the button, doors close 21:46, open on a dark floor 21:52 | none | N | **J alone**, elevator |
| 21:54-22:12 | J (silhouette) walks the dark under-construction floor to the conference room door | none | N | **J alone**, walking, dark |
| 22:12-22:55 | Dark conference room: J's head in the foreground, two men (magenta jacket; teal floral shirt/fedora) discuss an architectural model by the window | none | N | spying, dialogue |
| 22:55-23:00 | Party stairs, blue light; host woman close 22:58 | none | N | party |
| 23:00-23:22 | Blue-lit party: bald suited man, older man (bow tie) and host address the crowd 23:02-23:14; **hazmat-suited gunmen burst in 23:16-23:20**, guests panic | none | N | party attack |
| **23:24-23:48** | **J (olive jacket) sneaks a dark penthouse with a pistol**: taped floor, plastic sheeting, body 23:34, muzzle flash 23:38, candle 23:46; ammo top-right | AM | N | **J alone**, gunplay |
| **23:48-23:52** | J close with a walkie-talkie; **text banner "Lucia: GUYS EVERYWHERE"** | UI | N | **text message UI** |
| **23:53-23:57** | **L (bob, black blazer) crouched at the party typing on her phone; banner "Lucia: After Czr, he's in saferoom, 10+ guys, auto weps, explosives, some military..."** | UI | N | **texting, L alone, phone** |
| 23:58-24:08 | Hazmat gunman teal-lit; **L face close-up 24:02**; hazmat man with radio 24:04; dead hazmat man in blood in an elevator 24:08 | none | N | tension |
| 24:09-24:24 | Two hazmat men in an elevator 24:10; **L (black blazer) creeps through a blue-lit corridor** past a prone man 24:12-24:22 | none | N | **L alone**, stealth |
| 24:24-24:34 | Stairwell: hazmat man attacks L 24:24-24:30; L prone 24:30-24:32; J at the "FLOOR 26" door 24:34 | none | N | stairwell, struggle |
| 24:36-25:25 | J (olive jacket) fights hazmat men on a dark office floor; ammo HUD from 24:50 | AM | N | **J alone**, firefight |
| 25:26-25:40 | Roof level: hazmat man grapples L on the ground 25:26-25:32; L crawls 25:32-25:38, pistol on the floor 25:38; yellow wet-floor sign | none | N | **L alone**, struggle |

### Closing montage and end card (25:40-26:48)

| Time | What's on screen | HUD | D/N | Good for |
|---|---|---|---|---|
| 25:40-25:46 | Black | none | - | - |
| **25:46-25:48.5** | **Vice City skyline at dusk**, towers lit | none | dusk | **skyline** |
| 25:48.5-25:50.7 | Aerial: tower rooftop pool with sunbathers | none | D | **pool**, rooftop, aerial |
| 25:50.7-25:52.5 | **Fishing boat** with three NPCs | none | D | boat, fishing |
| 25:52.5-25:56 | Bar: tattooed bartender and a patron in a striped top, neon | none | N | bar, nightlife |
| 25:56-25:58 | Nightclub booth POV, hands with a drink and a pink lighter | none | N | drinks |
| 25:58-26:02 | Terrace: tattooed couple smoking, drinks, graffiti wall | none | D | NPCs, leisure |
| 26:02-26:06 | Night boat/dock flash; blue-lit interior with a shirtless man in glasses 26:04 | none | N | night |
| 26:06-26:08 | **Tuner car meet** with NPCs in a car park | none | D | car meet, car park |
| 26:08-26:10 | Seaplane propeller close-up | none | D | seaplane |
| **26:10-26:13** | **Vice City skyline at sunset** (silhouette) | none | dusk | **skyline** |
| 26:13-26:18 | On a fishing boat: man in Hawaiian shirt hands a drink to a woman (red top, jean shorts); man in white tank | none | D | boat, drinks |
| 26:18-26:28 | GTA VI logo | none | - | logo |
| 26:28-26:43 | "CAPTURED ON PS5 / NOVEMBER 19, 2026 / PRE-ORDER NOW" | none | - | end card, date |
| 26:43-26:48 | Rockstar logo | none | - | logo |

---

# 2. TRAILER 1 (T1), 1:30

Cinematic trailer cut. No game HUD at any point. Social-feed overlays (vertical phone-style frames with usernames, "Follow", hearts, comments) run 0:41-0:59.

| Time | What's on screen | HUD | D/N | Good for |
|---|---|---|---|---|
| 0:00-0:02.7 | Black, ESRB-style card | none | - | title |
| 0:02.7-0:05 | **Dusk highway aerial over Vice City**, cars, pink sky | none | dusk | aerial, highway, skyline |
| 0:05-0:06.5 | Prison fence, razor wire, pink dusk | none | dusk | prison |
| 0:06.5-0:08.5 | **Lucia in orange INMATE** profile at a van window, guard tower, golden light | none | D | **L alone**, prison |
| 0:08.5-0:10.9 | Older woman (glasses, parole officer) at a desk, Lucia's shoulder (INM); Lucia frontal in jumpsuit 0:10 | none | D | **L alone**, interview |
| 0:10.9-0:12.5 | Aerial turquoise water, catamaran 0:11, jet skis 0:12 | none | D | water, boats |
| 0:12.5-0:15 | **Aerial beach, crowded sand, skyline** | none | D | **beach**, aerial |
| 0:15-0:18.4 | Aerial skyline day under "ROCKSTAR GAMES PRESENTS", fades to black | none | D | **Vice skyline**, title |
| 0:18.4-0:19.2 | Palms and a tower, low angle | none | D | skyline |
| 0:19.2-0:21.7 | **Swamp at golden hour, airboat, flamingos 0:21** | none | D | **airboat, swamp** |
| 0:21.7-0:23.3 | **Crowded beach**, NPC women walking, umbrellas | none | D | **beach, NPC crowd** |
| 0:23.3-0:24.8 | Speedboat at a container port, wake | none | D | boat |
| 0:24.8-0:27.4 | **Night highway: woman in yellow dancing on the roof of a red sports car**, neon skyline | none | N | night, car |
| 0:27.4-0:29 | Daylight street: lowriders and custom cars, mural, NPCs | none | D | car culture |
| 0:29-0:30 | Nightclub dancers, sparkler | none | N | club |
| 0:30-0:32 | Two NPC men close (dreadlocks, shades, gold chains; bald, bandana headband), day | none | D | NPCs |
| 0:32-0:33 | Night aerial of Vice's bay, lit bridge | none | N | **aerial night skyline** |
| 0:33-0:35 | **Neon night street**, supercars parked, pedestrians | none | N | Ocean Drive, supercars |
| 0:35-0:36 | **Packed nightclub crowd**, red-lit stage | none | N | **NPC crowd, club** |
| 0:36-0:37.4 | Aerial turquoise keys, bridge, seaplane | none | D | aerial |
| 0:37.4-0:39.8 | **Rooftop pool deck**: blonde woman in a bikini, woman in white bikini, skyline | none | D | **pool**, rooftop, skyline |
| 0:39.8-0:41.3 | Giant "VICE" sign at sunset | none | dusk | VICE sign |
| **0:41.3-0:42.4** | **Phone-feed overlay**: yacht party in bikinis, caption by "DadBodSquad" | UI | D | **phone/social UI** |
| **0:42.4-0:43.9** | **Feed overlay: officer lifts an alligator out of a pool**, "OfficialPOACH" caption | UI | D | **social UI**, funny NPC |
| **0:43.9-0:45.5** | **Feed overlay: woman dances on a red car roof**, "have.a.vice.day" | UI | D | **social UI** |
| 0:45.5-0:46.5 | Aerial night street takeover, donuts, smoke | none | N | car meet, night |
| **0:46.5-0:47.5** | **Feed overlay: two women in neon holographic jackets dancing, hearts and comments** | UI | N | **social UI** |
| 0:47.5-0:48.6 | **Convenience store interior, security-camera look (time stamp 09:58:47), counter, ATM** | none | D | **store/CCTV** |
| **0:48.6-0:50** | **Police body-cam POV entering a building** (time stamp, camera icon) | none | N | **cops searching** |
| 0:50-0:52 | Feed overlay: gas station in a storm, truck passes | UI | D | social UI |
| 0:52-0:54 | Feed: man dancing on a car on a freeway at night; green pickup, man stands on the door ("RIP Rudi") | UI | N/D | social UI |
| 0:54-0:55 | Woman in bikini hosing a lawn, seen through a car window | none | D | NPC |
| 0:55-0:57.3 | **Muddy crowd party**, NPCs dancing covered in mud | none | D | **NPC crowd** |
| 0:57.3-0:59.5 | Feed overlay: old woman in a floral nightgown with a bat, old car, motel | UI | D | social UI, NPC |
| **1:00.5-1:02.5** | **Car interior: J driving**, hands on wheel, billboard "IT CURES EMOTIONS!", profile close-up 1:02 (stubble, scarf) | none | D | **J alone**, driving |
| **1:02.5-1:03.5** | **L in the passenger seat (red bandana, hoops) holding a fan of cash, looking at J** | none | D | **L alone / J+L car, cash** |
| 1:03.5-1:04.6 | **WEAZEL NEWS aerial: crash** with "NO (OVER) TURNING ZONE!" graphic | UI | D | news graphic, crash |
| 1:04.6-1:05.6 | News graphic: sheriff badge, tattooed purple-hair inmate | UI | D | news graphic |
| 1:05.6-1:06.7 | Dirt bikes / quads wheelie on a dusty road | none | D | bikes |
| 1:06.7-1:07.7 | WEAZEL NEWS aerial: police chase at an intersection, "DIRT-BIKE DIRT-BAGS" | UI | D | **police chase** (news) |
| 1:07.7-1:08.7 | Big man (white tee, gold chain), "HighRollerz" caption | UI | D | NPC |
| **1:08.7-1:10.3** | **Inside a liquor store: L (black tank, red bandana) + masked J (grey bandana, white tee) side by side at the shelves** | none | D | **store robbery, J+L together** |
| **1:10.3-1:12.8** | **Red muscle car drifts on a dusty road**, dust cloud | none | D | **getaway driving** |
| **1:12.8-1:16.5** | **L leans over J, who lies shirtless on a motel bed; bedside lamp, warm light** | none | D | **J+L intimate** |
| 1:16.5-1:17.3 | L (bandana, black tank, shorts, pistol) and J (white tee, bandana) walk out of the store into sunlight | none | D | **robbery exit** |
| 1:17.3-1:18.8 | L aims a pistol from the doorway, J beside her pointing | none | D | **holding up**, J+L together |
| 1:18.8-1:28 | GTA VI logo, "COMING 2025" | none | - | logo |
| 1:28-1:30 | Rockstar logo | none | - | logo |

---

# 3. TRAILER 2 (T2), 2:46.8

Letterboxed picture band from 0:06 (1920x864, crop `1920:864:0:108`). No game HUD. Cutscene and engine footage.

| Time | What's on screen | HUD | D/N | Good for |
|---|---|---|---|---|
| 0:00-0:02.5 | Black, ESRB card | none | - | title |
| 0:03-0:06 | Rockstar logo fades in | none | - | logo |
| 0:07-0:09 | **Aerial of island houses on turquoise water**, boats | none | D | aerial, keys |
| 0:09-0:10 | Teal stilt house, 50s Cadillac tailfin, teal pickup, palms | none | D | home exterior |
| 0:10-0:13.7 | Older white-haired man (palm shirt, shades) by a grey pickup; **J shirtless in camo shorts climbs a ladder onto a roof** (0:11.5-0:14) | none | D | **J alone** |
| 0:13.7-0:18.8 | Older man talks and gestures by the pickup | none | D | NPC dialogue |
| **0:19-0:21** | **J shirtless (backwards cap, teal shades, stubble) by the ladder at a green shack**, talking | none | D | **J alone**, close |
| 0:21-0:23.3 | High angle over the porch: pickup and older man in the yard | none | D | establishing |
| **0:23.3-0:27** | **J shirtless on the porch, turns, goes into the dark house** | none | D | **J alone** |
| **0:27.5-0:32** | **J driving: cap, shades, white tank, chain, tattoo**, side view through the car window, day traffic | none | D | **J alone, driving** |
| **0:32-0:34.6** | **Shop interior (crystals, tourist shop): J (Leonida tank top) gesturing at a dreadlocked NPC 0:32; hands (watch, camo shorts) at the cash register 0:33-0:34, till pops open showing bills; victims lie on the floor behind** | none | D | **store robbery, cash register, cash** |
| 0:34.6-0:38.4 | **POV driving a highway**: hands on wheel, Vice towers, "VCI Airport" signs, airliner overhead 0:37-0:38, pickups | none | D | **driving POV, skyline** |
| **0:38.4-0:41.6** | **Beach workout: man bench-pressing on the sand** with green plates, palms, women walking, golden light | none | D | **gym/workout, beach** |
| 0:41.6-0:45.3 | **Convenience store (green walls, ATM): man from behind (tee, cargo shorts) carries a red cooler**; NPC at the counter; woman crouched outside the door 0:45 | none | D | store, ATM |
| 0:45.3-0:49.8 | **POV driving past a graffiti mural with a police cruiser (lights) and cops** at the roadside; J (shades) at left 0:49 | none | D | **cops**, driving POV |
| 0:49.8-0:51.9 | Prison guard tower and razor wire | none | D | prison |
| **0:51.9-1:03** | **Prison visiting booth: J (white tee with eagle graphic "Let Freedom Reign!") speaks to a grey-haired guard behind glass**; "NO EXCEPTIONS" signs; turns to the chain-link gate 1:01 | none | D | **J alone**, prison |
| **1:03-1:06** | **L (curly hair, dirty grey tee, smiling) stands behind a chain-link gate**, golden light | none | D | **L alone** |
| **1:06.2-1:10** | **L (shoulder) faces J (white pocket tee) outside the prison gate**, old teal car, palms: reunion | none | D | **J+L together**, reunion |
| 1:10-1:12 | Black "ROCKSTAR GAMES PRESENTS" card | none | - | title |
| 1:12-1:14.5 | Sunlit bed scene, **J and L in silhouette**, title text over it | none | D | **J+L intimate** (suggestive, check policy) |
| 1:15-1:18 | **Red-lit heist**: woman in a skull mask with an SMG, man in a tie at a computer with hands up 1:16, masked robber | none | N | **holdup**, heist |
| 1:18-1:20 | Blue-lit close-up of skin and limbs (intimate, abstract) | none | N | intimate |
| **1:19.4-1:21.4** | **Bar table: L (orange bikini top, beer) and J (Hawaiian shirt, beer) side by side**, tiki bar, day; beer-bottle close 1:21 | none | D | **J+L together**, date, drinks |
| **1:21.4-1:25** | **Dock with a pontoon boat ("PREDATOR"): couple sits at the end of the dock, sunset**, string lights, life rings | none | dusk | **J+L together**, date, boat, sunset |
| 1:25.2-1:26.8 | Boat hangar ("Brian's Boat Works"), men climb stairs beside a motorboat | none | N | boat |
| 1:26.9-1:28.3 | **Night road: sanitation workers in hi-vis bag trash**, a police officer with a clipboard, red truck | none | N | **trash/bins**, NPCs |
| **1:28.4-1:29.4** | **L (white crop top, hair up) + J (dark tee) stand together in a home kitchen** (green cabinets, fridge notes), looking off-camera | none | D | **J+L at home** |
| 1:29.5-1:34 | **Beach bar interior, "HAPPY HOUR"**: bearded NPC in colourful shirt, patrons dancing at dusk | none | dusk | bar, NPC crowd |
| **1:34-1:38** | **Open-air waterfront bar at sunset**: woman in a green sequin dress walks and dances, man in black shirt | none | dusk | bar, nightlife |
| **1:37.6-1:38.4** | **Car interior close-up: J (buzzcut, stubble, chain) looks ahead; L (hoop earring) partly in frame at right**, golden light | none | dusk | **J+L car close** |
| **1:38.4-1:39.7** | **Couple from behind holding hands** (yellow Hawaiian shirt, white tank) beneath an overpass | none | D | **holding hands** (J+L?) |
| 1:39.7-1:42.5 | **Nightclub "NINE" dance floor**, man and woman in a sequin dress dance close 1:41-1:42 | none | N | **club**, NPC crowd |
| 1:43-1:45 | Dim purple room: men standing, shirtless big man with towel and masked NPC (the apartment-block gang) | none | N | NPCs |
| **1:45-1:46** | **Top-down night alley: a person lies on the ground by "KEEP CLEAR" stencil, trash, folding chair** | none | N | **homeless/lying NPC, trash** |
| **1:46-1:47** | **J (backwards cap, green shirt) talks to an older mechanic (bandana, gold chain) in a workshop with tool wall**; woman in pink tee beside | none | N | **garage/workshop, mechanic** |
| 1:47-1:51 | Flashlight scene: cop in shades, **detective (glasses, vest, badge)** talking to a man in green (back), gun raised from a convertible 1:51 | none | N | **cops searching**, detective |
| 1:51-1:53 | Woman (visor shades, mesh top, star bikini) gestures from a convertible at dusk | none | dusk | NPC |
| 1:53-1:55 | Sequin-dress close-ups (club) 1:53-1:54.3; a man in green grapples an older man beside a burning pickup under a motel sign 1:54.4-1:55 | none | N | club, street fight |
| 1:55-1:55.8 | **Woman in black tank high-kicks inside a chain-link cage** (training/fight) | none | N | fight, gym-like |
| 1:55.8-1:57.8 | Home interior: man in a black tank (J?) in a doorway, woman (hoop earring, ponytail, blue top, L?) in the foreground; her face close 1:57.4 | none | D | home |
| 1:58-1:59 | **Windshield POV: burning police cars and an explosion**, woman (red hair) watching | none | D | **explosion, police cars** |
| 1:58.7-1:59.7 | Two men (Manatees #13 jersey, white tee) look at their phones in a park | none | D | **phone** (NPCs) |
| 1:59.7-2:00.8 | Woman (red top) climbs around a big truck cab, night chase | none | N | chase |
| 2:01-2:03 | **Pickup burns rubber on a night street**, sparks, taillights | none | N | **getaway/chase** |
| **2:03-2:04.5** | **J leans over L on a bed, blue light, about to kiss** | none | N | **J+L intimate** |
| **2:04.6-2:05.8** | **Phone camera selfie UI: man in purple shirt grins, two others behind, record dot** | UI | N | **phone UI, selfie** |
| 2:05.8-2:07 | **Ocean Drive / Dominion Hotel in daylight**, NPC dancing in shorts, sports cars, red sedan | none | D | **Ocean Drive**, NPCs |
| 2:07-2:09 | Neon pink club exterior with a boat on the roof; pole dancer under neon 2:08-2:10 | none | N | club, strip club |
| 2:09-2:14.5 | **Living-room TV playing a gun-shop ad**, beer bottles, seagull on the balcony rail | none | D | **in-world TV** |
| 2:14.5-2:18.5 | **Living room: woman in orange hi-vis vest ("LDC") walks in, man sleeps on the sofa**; she shoves him 2:18 | none | D | home, NPC |
| 2:18.5-2:20.2 | Swamp **helicopter chase** over water with an airboat; cockpit view 2:20 | none | D | chase |
| 2:20.3-2:22 | **Jet ski: shirtless man and woman**, green craft, skyline and yacht | none | D | **jet ski, leisure** |
| 2:22-2:24 | **Man (cap, teal shades, tank) on a chopper motorcycle** with seaplane overhead (J?) | none | D | motorbike |
| 2:24-2:26 | Night downtown: semi truck, pink-lit tower; motorcycle sparks 2:25 | none | N | night |
| **2:25.5-2:27.3** | **Motel room: man lifts a woman in an embrace**, lamp | none | N | **J+L intimate** (hug) |
| 2:27.4-2:28.4 | Speedboat chase with helicopter flare over sunset water | none | dusk | boat chase |
| 2:28.4-2:29.3 | Motorbike rider (back) at a night intersection, traffic lights | none | N | motorbike, night |
| 2:29.4-2:31 | **Green convertible at dusk past "WATKINS AUTO PARTS"**: driver and slumped passenger | none | dusk | car interior |
| **2:31-2:33** | **Mechanic's garage party**: man in teal tee and yellow cap dances with a drink, sparks, tool cart | none | N | **garage/workshop** |
| 2:33-2:34 | High road at golden hour: red muscle car passes a lamp-post | none | dusk | driving |
| **2:34-2:36.5** | **Wide golden-hour shot of the Vice skyline over road and palms** | none | dusk | **skyline** |
| 2:37-2:45 | GTA VI logo, "MAY 26, 2026" | none | - | logo |
| 2:45-2:46.8 | Rockstar logo | none | - | logo |

---

# 4. SUBJECT INDEX (best 2-4 picks each, in order of how good they are for B-roll)

Format: `SRC m:ss-m:ss` = source and range. EL = Extended Look, T1 = Trailer 1, T2 = Trailer 2. Full-res stills for most picks are in `frames/stills/` (the filename carries source and mm:ss).

### Jason & Lucia together
- **In a car:** `EL 13:10-13:26` (daylight close two-shot: J drives and checks his phone, L talks to him); `T1 1:00.5-1:02.5` (J driving), then `T1 1:02.5-1:03.5` (L in the passenger seat holding cash); `T2 1:37.6-1:38.4` (golden-hour close, J ahead, L partly in frame); `EL 8:20-8:58` (red convertible on the road, two people in the car, minimap); `EL 14:42-15:00` (L driving, J masked behind).
- **Walking:** `EL 9:50-10:19` (hold hands along a sunny rooftop bar, HOLD HANDS prompt); `EL 0:08-0:19` (night walk toward the apartment, from behind, no HUD); `EL 16:54-16:57.5` (close two-shot, J + L facing camera) and `EL 17:00-17:06.5` (cobalt tiled wall, L walks off); `T2 1:38.4-1:39.7` (hands from behind, J+L probable).
- **At home:** `T2 1:28.4-1:29.4` (kitchen two-shot, both look off-camera); `EL 6:29-6:36` (pink bedroom, close); `EL 6:46-6:58` (L chooses clothes, J at the lit mirror).
- **Close / intimate:** `T1 1:12.8-1:16.5` (L leans over J on a bed, lamp); `T2 2:03-2:04.5` (blue-lit, about to kiss); `T2 1:06.2-1:10` (reunion at the prison gate); `EL 9:34.8-9:46` (elevator, J watches L, romantic); `T2 2:25.5-2:27.3` (motel embrace); also `EL 5:04-5:08` and `EL 5:13-5:21` (graffiti elevator close two-shots). `T2 1:12-1:14` is a sunlit bed scene with title text (suggestive).
- **Two-shots, masked / action:** `EL 11:56.3-12:02.4` (low-angle masked pair in the store, best "partners in crime" shot); `T1 1:08.7-1:10.3` (side by side at the liquor shelves); `T1 1:17.3-1:18.8` (L aims, J points); `T2 1:19.4-1:21.4` (bar table, beers); `T2 1:21.4-1:25` (dock at sunset).

### Lucia alone
- `EL 6:36-6:44` (lies on the pink bed on her phone, jean shorts); `EL 6:46-6:51` (picks an outfit at the wardrobe); `EL 17:18.7-17:22` (bench-pressing in a gym, top-down camera); `EL 17:53-18:00` (yellow tropical shirt, walks up to a pawn shop with a pistol, back view); `EL 23:53-23:57` (crouched at the party typing a text), then `EL 24:01-24:03` (close face shot); `EL 24:12-24:22` (creeps a blue-lit corridor); `T2 1:03-1:06` (smiling behind the prison gate); `T1 0:06.5-0:10.9` (prison, orange jumpsuit).

### Jason alone
- `EL 7:10-7:25` (wanders Lucia's kitchen, opens the fridge, prompts); `EL 8:04-8:20` (walks under the carport and gets into the car); `EL 21:37.5-21:54` (alone in the elevator, back of head); `EL 21:54-22:12` (silhouette in a dark corridor); `EL 4:30-4:55` (shotgun and red duffel through hallways, HUD); `EL 23:24-23:48` (sneaking a dark penthouse with a pistol); `T2 0:19-0:27` (shirtless on the porch, close); `T2 0:27.5-0:32` (driving, side view); `T2 0:51.9-1:03` (prison visiting window); `T1 1:00.5-1:02.5` (driving).

### Phone / texting / phone UI
- **Phone UI on screen:** `EL 3:42.7-3:45.5` (incoming call "Unknown", red decline button, close on a table); `EL 4:10.3-4:11.3` (same phone ringing again); `EL 23:48-23:52` (text banner "Lucia: GUYS EVERYWHERE"); `EL 23:53-23:57` (banner with Lucia's longer text while she types); `EL 18:24-18:28.5` (livestream chat overlay, LIVE 51k); `T2 2:04.6-2:05.8` (phone camera selfie frame with record dot); `T1 0:41.3-0:48` and `0:50-0:53`, `0:57.3-0:59.5` (vertical social-feed overlays with usernames, Follow, hearts, comments).
- **People using phones:** `EL 6:36-6:44` (L on the bed); `EL 13:12-13:14` (J checks his phone while driving); `EL 23:53-23:57` (L texting); `EL 18:16-18:23` (man films a selfie video); `EL 1:32-1:46` (NPC scrolls his phone in the elevator); `T2 1:58.7-1:59.7` (two men look at their phones); `EL 20:16-20:17` (selfie pose at a pool party).

### Store robbery
- **Entering:** `EL 11:28-11:34.4` (L pulls up a red bandana in her leather jacket and goes through the gas-station store door with J; J's face close-up just before, 11:26.5-11:28); `T1 1:08.7-1:10.3` (inside a liquor store, side by side); `EL 11:45.7-11:52.8` (interior with wanted stars and ATM); `T1 1:16.5-1:17.3` (walking out into sunlight).
- **Holding up the clerk:** `EL 11:34-11:36` (L raises her pistol in the doorway); `EL 11:53.5-11:55.7` (masked J at the counter grabs and shoves the clerk); `T1 1:17.3-1:18.8` (L aims from the doorway, J points); `EL 12:02.4-12:03.8` (clerk raises a shotgun, seen in a convex mirror); `EL 18:00-18:03` (jewellery store holdup with hostage kneeling).
- **Safe:** **not found.** No safe is shown in any source. Closest: `T2 0:33-0:34.6` (cash register drawer opens on a stack of bills).
- **Cash:** `T2 0:33-0:34.6` (till opens, bills visible); `T1 1:02.5-1:03.5` (L fans a stack of cash); `EL 16:39-16:48` (duffel bag handed over, cash buyer); `EL 17:50-17:51` (cash HUD $15,150 on the weapon wheel); `EL 11:51-11:52` (ATM in the store).
- **Other robberies:** `EL 9:29-9:31` (armoured-truck holdup, masked gunmen); `T2 1:15-1:18` (red-lit office holdup, man at a computer with hands up); `EL 17:53-18:00` (pawn shop approach).

### Getaway driving / police chase
- `EL 14:02-14:33` (J shoots at police from behind a car; flipped police truck; helicopter; 5 stars; flashing minimap box); `EL 15:17-15:50` (dark sedan through alleys and streets, cops on foot and in cruisers, helicopter); `EL 18:03-18:12` (getaway on a motorbike with a duffel, stars dropping); `T1 1:10.3-1:12.8` (red muscle car drifting in dust); `T2 2:01-2:03` (pickup burns rubber at night); `T2 2:18.5-2:20.2` (helicopter chases an airboat); `T1 1:06.7-1:07.7` (news aerial of a police chase).

### Wanted level / cops searching
- **HUD with stars:** `EL 14:02-14:10` (five stars top-right with ammo, red/blue police box bottom-left; best); `EL 15:18-15:50` (stars with minimap flashing as cops close in); `EL 15:50-15:58` (stars and minimap go grey as the car hides in a garage: cops lose you); `EL 18:03-18:12` (stars drop 6 to 2); `EL 11:45.7-11:52` (stars appear mid-robbery); `EL 18:40-18:46` (stars at night).
- **Cops searching:** `T1 0:48.6-0:50` (body-cam POV entering a building); `T2 1:47-1:51` (flashlight, detective with badge); `T2 0:45.3-0:49.8` (cruiser with lights at a mural wall); `EL 4:04-4:10` (SWAT raid in the hall).

### On foot through alleys
- `EL 17:00-17:06.5` (alley with cobalt-tiled wall, "WARNING cameras" sign, J+L); `EL 17:53-18:00` (L walks the shopfront row with a pistol); `EL 0:08-0:19` (night approach to the apartment); `EL 4:30-4:55` (hallways with a shotgun); `EL 14:12-14:32` (alley seen from behind a car, dumpsters); `EL 5:50-5:59` and `T2 1:45-1:46` (top-down "KEEP CLEAR" alley).

### Changing outfits / clothing store
- **Clothing store: not found.** There is no shop, fitting room or shopping scene in any of the three videos.
- **Outfit-change UI (best match): `EL 17:50.5-17:51.4`.** The ITEMS tab of the wheel shows clothing and accessory slots: sunglasses, "ROD'S RACING CAP" (HEADWEAR, PUT ON), "FACE WRAP" (MASKS, ON) and a hanger (WEAR STYLE 1/2, TAKE OFF). It runs 17:50.0-17:51.5 over a blurred red convertible with $15,150 / $700 top-right. Still: `frames/stills/EL_1750_outfit-wheel-ui.jpg`.
- **Choosing clothes at home:** `EL 6:46-6:51` (L holds two outfits on hangers at her wardrobe, magenta curtains); `EL 6:51-6:58` (J at a lit vanity mirror, L with clothes). `EL 17:51-17:53` (masked driver beside a red convertible) shows the face wrap actually worn.
- **Wardrobe changes across scenes** (continuity, not a scene): L swaps jackets between `EL 11:28` (leather "DON'T TRIP" jacket), `EL 13:10` (grey hoodie) and `EL 17:53` (yellow tropical shirt).
- `EL 15:56-15:59` is the weapon wheel (Molotov slot visible), not a clothing menu.

### Hair salon
- **Not found.**

### Beach
- `EL 18:28.5-18:31` (yellow umbrellas, striped loungers, sunbathers; best); `T1 0:12.5-0:15` (aerial beach, crowded); `T1 0:21.7-0:23.3` (crowded beach, walking NPCs); `T2 0:38.4-0:41.6` (beach bench-press workout, golden light); `EL 17:22-17:25` (pier, swimmer dives into the sea).

### Gym / working out
- `EL 17:18.7-17:22` (L bench-presses indoors, top-down); `T2 0:38.4-0:41.6` (beach bench press); `T2 1:55-1:55.8` (woman high-kicks in a chain-link cage, training); `EL 17:13-17:16` (basketball at a stilt-house hoop, not a gym).

### Dates / leisure
- **Date setups:** `EL 9:34.8-11:26` (rooftop bar date: elevator, hold hands, table with NPCs); `T2 1:19.4-1:21.4` (bar table with beers); `T2 1:21.4-1:25` (dock at sunset, pontoon boat); `T2 1:34-1:38` (waterfront bar at sunset).
- **Pool:** `T1 0:37.4-0:39.8` (rooftop pool deck, bikinis); `EL 20:17-20:21` (night pool party); `EL 25:48.5-25:50.7` (aerial rooftop pool); `T1 0:42.4-0:43.9` (alligator in a pool, feed overlay).
- **Boat / watercraft:** `EL 26:13-26:17` (fishing boat, drinks); `EL 25:50.7-25:52.5` (fishing boat); `T2 2:20.3-2:22` (jet ski with couple); `T1 0:23.3-0:24.8` (speedboat); `EL 17:25-17:27` (jet ski/boat).
- **Kayak:** `EL 17:29-17:31`. **Scuba:** `EL 17:16-17:18.7`. **Parachuting / skydiving:** `EL 18:47.5-18:59` (rooftop edge, freefall, parachute over Vice City). **Airboat:** `EL 17:10-17:13`, `T1 0:19.2-0:21.7`.
- **Golf: not found. Zoo: not found.**
- **Other leisure:** `EL 17:42-17:47` and `EL 20:21.5-20:26` (street races); `EL 18:35-18:39` (dirt-bike race); `EL 18:31-18:35` (shooting range mini-game); `EL 17:13-17:16` (basketball); `EL 7:26-7:46` (TV at home).

### Car being damaged / car repair
- **Damaged:** `EL 16:04-16:09` (getaway sedan burns, best); `EL 14:08-14:11` and `EL 14:20-14:23` (police vehicles wrecked and flipped); `EL 18:46-18:47.5` (roadside car explosion); `T2 1:58-1:59` (burning police cars through a windshield); `T2 2:01-2:03` (truck burns rubber, sparks).
- **Repair:** not found as a car-repair scene. Closest: `T2 1:46-1:47` (J talks to a mechanic in a workshop), `T2 2:31-2:33` (mechanic's garage party), `EL 17:51-17:53` (storefront sign "WE DO REPAIRS", an electronics shop).

### Selling a car / car fence
- **Not found.** Closest: `EL 16:39-16:48` (a bearded buyer takes a duffel of goods/cash from J and L beside a van) and `EL 17:51-18:00` (pawn shop "Joyeria Empeños" front).

### Rideshare / taxi
- **Not found.** Closest: `EL 13:26-13:58` and `EL 14:42-15:08` (L drives with a bearded passenger in the back seat).

### Dumpster / homeless NPC
- `T2 1:45-1:46` (top-down: a person lying on the pavement by "KEEP CLEAR", trash and a folding chair; best); `EL 17:53-17:57` (a person asleep on a bench outside the pawn shop); `EL 9:04-9:09` (man sitting on the kerb by vending machines); `EL 5:50-5:59` (same trash-strewn alley from above); `T2 1:26.9-1:28.3` (sanitation workers bag trash at night); `EL 14:24-14:28` (dumpsters and bin bags along an alley).

### Impound lot / car park
- **Impound lot: not found.** Car parks: `EL 15:50-16:16` (dark multi-storey parking garage, getaway car, burning sedan, loading the van; best); `EL 8:04-8:20` (apartment carport); `EL 26:06-26:08` (tuner car meet in a car park); `EL 15:16-15:20` (garage ramp tunnel); `EL 17:51-17:53` (strip-mall car park).

### Shower
- **Not found.**

### Open world / map wide shots
- No full-screen map UI exists in any source; only the minimap (bottom-left). Wide open-world shots: `EL 16:32-16:39` (aerial drone view of the toll arch, tennis courts, bay, skyline); `EL 18:47.5-18:59` (skydive over Vice City's islands); `T1 0:02.7-0:05` (dusk highway aerial); `T1 0:12.5-0:15` (aerial beach and skyline); `T1 0:32-0:33` (night aerial of the bay); `T2 0:07-0:09` (aerial island houses); `EL 18:59-19:04` (top-down city and beach).

### Vice City skyline
- `EL 26:10-26:13` (sunset silhouette); `EL 25:46-25:48.5` (dusk, towers lit); `EL 12:15-12:31` (day, from a rooftop with a news helicopter); `T2 2:34-2:36.5` (golden hour over road and palms); `T1 0:15-0:18.4` (day aerial under the "Presents" title); `T1 0:39.8-0:41.3` (giant VICE sign at sunset); `EL 20:08-20:14` (night skyline across the tarmac).

### NPC crowds
- `EL 20:26-20:31` (packed nightclub floor); `EL 18:28.5-18:31` (beach crowd); `EL 9:25-9:29` (backyard wrestling ring); `T1 0:35-0:36` (packed nightclub); `T1 0:55-0:57.3` (muddy crowd party); `T1 0:21.7-0:23.3` (beach walkers); `T2 1:29.5-1:34` (beach bar at happy hour); `EL 9:33-9:35` and `EL 10:39-10:45` (rooftop patrons).

---

## Quick reference: best "clean" (no HUD) vs "game" (HUD) picks

- **Cutscene / clean:** `EL 13:10-13:26` (car two-shot), `EL 11:56.3-12:02.4` (masked pair), `EL 9:34.8-10:19` (elevator and hand-holding), `T1 1:12.8-1:16.5` (bed), `T2 1:06.2-1:10` (reunion), `T2 1:28.4-1:29.4` (kitchen), `EL 6:36-6:51` (L at home).
- **In-game HUD:** `EL 14:02-14:33` (5-star chase), `EL 15:17-15:58` (getaway and hiding), `EL 8:20-8:58` (driving with minimap), `EL 3:42.7-3:45.5` (phone call UI), `EL 23:48-23:57` (text banners), `EL 18:24-18:28.5` (livestream overlay), `EL 17:42-17:47` (race HUD).
- **Letterbox warning:** every T2 shot after 0:06 carries black bars top and bottom; crop with `crop=1920:864:0:108` before scaling or it will look boxed inside a 16:9 timeline.

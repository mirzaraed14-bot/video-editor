import sys
from PIL import Image, ImageDraw, ImageFont, ImageOps
IG = "X:/Claude Projects/video-editor-client/video-editor/projects/speed-kicked-out-three-peat/assets/photos/ig/"
OUT = sys.argv[1]
items = [
    ("dad+speed~14-15_CHRISTMAS_CROP-no-children_CUaSxScFfMw.png", None,
     ["A  CHRISTMAS (dad's post, 2021)", "Speed ~14-15: face matches (high)", "Xmas 2020 or earlier; no children", "soft 400x750 source"]),
    ("dad+speed~12-14_DETROIT-shirt-selfie_FRAME-dad-bday-video-2025_DFFxlQKOd3n_t10.9.png", None,
     ["B  'DETROIT' SHIRT (montage frame)", "~12-14: likely Speed (medium)", "may be his younger brother", "soft video frame"]),
    ("dad+speed~12-14_braces-smile-selfie_FRAME-dad-bday-video-2025_DFFxlQKOd3n_t16.9.png", None,
     ["C  BRACES SELFIE (montage frame)", "~12-14: likely Speed (medium)", "may be his younger brother", "soft video frame"]),
    ("dad+speed17_2022-04-22_mastros-FEED-ORIGINAL_3rd-adult-right_Cco7BGeLOP8.jpg", (0, 0, 930, 1004),
     ["D  MASTRO'S, FEED ORIGINAL", "Speed 17 (Apr 2022): certain", "1440px original, cropped x0-930", "not Detroit"]),
    ("dad+speed17_story-2022-04-25_mastros_SCREEN-CAPTURE.png", None,
     ["E  MASTRO'S STORY (in the build now)", "Speed 17: certain", "screen capture 676x898", "not Detroit"]),
]
TW, TH, LH = 360, 520, 92
sheet = Image.new("RGB", (TW * len(items), TH + LH), (16, 16, 16))
d = ImageDraw.Draw(sheet)
f1 = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 17)
f2 = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 15)
for i, (fn, box, lab) in enumerate(items):
    im = Image.open(IG + fn).convert("RGB")
    if box:
        im = im.crop(box)
    im = ImageOps.contain(im, (TW - 8, TH - 8))
    x = i * TW + (TW - im.width) // 2
    sheet.paste(im, (x, (TH - im.height) // 2))
    d.text((i * TW + 8, TH + 4), lab[0], font=f1, fill=(255, 210, 90))
    for k, t in enumerate(lab[1:]):
        d.text((i * TW + 8, TH + 28 + k * 20), t, font=f2, fill=(230, 230, 230))
sheet.save(OUT, quality=92)
print("ok", sheet.size)

# -*- coding: utf-8 -*-
import os, sys, io, json
from PIL import Image, ImageDraw
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
OUT = r"C:\ppt\_check\bg"
theme = sys.argv[1]
d = os.path.join(OUT, theme)
files = sorted(f for f in os.listdir(d) if f.lower().endswith((".jpg", ".png", ".jpeg")))
cols = 4
rows = (len(files) + cols - 1) // cols
tw, th = 460, 260
sheet = Image.new("RGB", (cols * tw, rows * (th + 24)), (18, 22, 34))
dr = ImageDraw.Draw(sheet)
for i, f in enumerate(files):
    im = Image.open(os.path.join(d, f)).convert("RGB")
    im.thumbnail((tw - 8, th - 8))
    x = (i % cols) * tw + (tw - im.width) // 2
    y = (i // cols) * (th + 24) + (th - im.height) // 2
    sheet.paste(im, (x, y))
    dr.text(((i % cols) * tw + 8, (i // cols) * (th + 24) + th + 4), f, fill=(255, 220, 150))
sheet.save(os.path.join(OUT, f"{theme}_sheet.jpg"), quality=88)
print(theme, len(files), "->", f"{theme}_sheet.jpg")

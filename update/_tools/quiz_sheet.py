# -*- coding: utf-8 -*-
"""Planche-contact des 6 nouvelles quiz (une par chapitre)."""
import io
import os
import sys

from PIL import Image, ImageDraw

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
SRC = r"C:\ppt\_check\render"
NUMS = [100, 140, 159, 174, 189, 223]
W, H = 640, 360
sheet = Image.new("RGB", (W * 2, H * 3), (10, 14, 28))
d = ImageDraw.Draw(sheet)
for i, n in enumerate(NUMS):
    im = Image.open(os.path.join(SRC, "slide%d.png" % n)).convert("RGB")
    im = im.resize((W, H))
    x, y = (i % 2) * W, (i // 2) * H
    sheet.paste(im, (x, y))
    d.rectangle((x + 4, y + 4, x + 60, y + 26), fill=(243, 156, 18))
    d.text((x + 12, y + 9), "S%d" % n, fill=(10, 14, 28))
out = r"C:\ppt\_check\render\quiz_sheet.jpg"
sheet.save(out, quality=90)
print("OK ->", out)

# -*- coding: utf-8 -*-
"""Planche-contact des fonds finaux assets/bg_*_online*.jpg (pour verification)."""
import glob
import io
import os
import sys
from PIL import Image, ImageDraw

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

BASE = r"C:\ppt"
files = sorted(glob.glob(os.path.join(BASE, "assets", "bg_*_online*.jpg")))
cols = 4
tw, th = 620, 349
rows = (len(files) + cols - 1) // cols
sheet = Image.new("RGB", (cols * tw, rows * (th + 26)), (16, 20, 32))
dr = ImageDraw.Draw(sheet)
for i, f in enumerate(files):
    im = Image.open(f).convert("RGB").resize((tw - 10, th - 10), Image.LANCZOS)
    x = (i % cols) * tw + 5
    y = (i // cols) * (th + 26) + 5
    sheet.paste(im, (x, y))
    dr.text((x, y + th - 2), os.path.basename(f), fill=(255, 220, 150))
sheet.save(os.path.join(BASE, "_check", "bg", "final_sheet.jpg"), quality=90)
print("-> _check/bg/final_sheet.jpg (" + str(len(files)) + " fichiers)")

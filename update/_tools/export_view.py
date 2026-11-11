# -*- coding: utf-8 -*-
"""Exporte les images des slides specifiees vers _check/view/ pour lecture visuelle."""
import os, re, shutil, sys
SLIDES = r"C:\ppt\_check\ppt\slides"
MEDIA = r"C:\ppt\_check\ppt\media"
OUT = r"C:\ppt\_check\view"
nums = [int(a) for a in sys.argv[1:]] or [41, 42, 59, 68]
for n in nums:
    rels = os.path.join(SLIDES, "_rels", f"slide{n}.xml.rels")
    m = re.search(r'Target="[^"]*media/([^"]+)"', open(rels, encoding="utf-8").read())
    src = os.path.join(MEDIA, m.group(1))
    dst = os.path.join(OUT, f"slide{n}.png")
    shutil.copyfile(src, dst)
    print(n, m.group(1), "->", dst)

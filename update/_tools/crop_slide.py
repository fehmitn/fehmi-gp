# -*- coding: utf-8 -*-
"""Recadrage d'une slide source -> assets/assets_ss_imageNN.png

Usage : python crop_slide.py <slide> [<left%> <top%> <right%> <bottom%>]
Coupe d'abord les marges donnees (defaut 4 16 100 97 : retire bordure wave,
titre et numero de page), puis bbox auto des pixels sombres + padding.
"""
import os, sys
from PIL import Image

SRC = r"C:\ppt\_check\view\slide%s.png"  # deja converti par export_view.py
OUT = r"C:\ppt\assets\assets_ss_image%s.png"

def main():
    n = sys.argv[1]
    l, t, r, b = ([float(x) for x in sys.argv[2:6]] if len(sys.argv) >= 6
                  else (4.0, 16.0, 100.0, 98.5))
    img = Image.open(SRC % n).convert("RGB")
    W, H = img.size
    # coin bas-droit : blanchir le numero de page d'origine
    from PIL import ImageDraw
    d = ImageDraw.Draw(img)
    d.rectangle((int(W * .88), int(H * .90), W, H), fill=(255, 255, 255))
    box = (int(W * l / 100), int(H * t / 100), int(W * r / 100), int(H * b / 100))
    img = img.crop(box)
    # bbox auto des pixels sombres
    gray = img.convert("L")
    mask = gray.point(lambda p: 255 if p < 140 else 0)
    bbox = mask.getbbox()
    if bbox:
        x0, y0, x1, y1 = bbox
        pad = 14
        img = img.crop((max(0, x0 - pad), max(0, y0 - pad),
                        min(img.width, x1 + pad), min(img.height, y1 + pad)))
    dst = OUT % n
    img.save(dst)
    print(dst, img.size)

if __name__ == "__main__":
    main()

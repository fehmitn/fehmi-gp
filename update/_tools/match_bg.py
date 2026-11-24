# -*- coding: utf-8 -*-
"""Retrouve, pour un fond deja genere, quelle vignette candidate lui correspond.

Compare une empreinte perceptuelle (dHash) entre l'image finale (assets/bg_*.jpg)
et les vignettes des dossiers <theme>_fix, puis affiche le meilleur candidat.

Usage : python match_bg.py <image> <theme> [<theme> ...]
"""
import io
import json
import os
import sys

from PIL import Image

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

BASE = r"C:\ppt"
BG = os.path.join(BASE, "_check", "bg")


def dhash(path, size=8):
    im = Image.open(path).convert("L").resize((size + 1, size), Image.LANCZOS)
    px = list(im.getdata())
    bits = []
    for y in range(size):
        for x in range(size):
            bits.append(1 if px[y * (size + 1) + x] > px[y * (size + 1) + x + 1] else 0)
    return bits


def ham(a, b):
    return sum(1 for x, y in zip(a, b) if x != y)


def main():
    img = sys.argv[1]
    cands = json.load(open(os.path.join(BG, "candidates.json"), encoding="utf-8"))
    h = dhash(img)
    results = []
    for theme in sys.argv[2:]:
        folder = os.path.join(BG, theme + "_fix")
        if not os.path.isdir(folder):
            folder = os.path.join(BG, theme)
        for c in cands.get(theme, []):
            p = os.path.join(folder, "%02d.jpg" % c["id"])
            if not os.path.exists(p):
                continue
            results.append((ham(h, dhash(p)), theme, c["id"], c["title"]))
    results.sort()
    print(os.path.basename(img))
    for d, theme, cid, title in results[:4]:
        print("   %3d  %s/%02d  %s" % (d, theme, cid, title))


if __name__ == "__main__":
    main()

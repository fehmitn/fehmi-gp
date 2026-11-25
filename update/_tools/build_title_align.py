# -*- coding: utf-8 -*-
"""Aligne le contenu de toutes les slides de contenu en haut (titre a ~20%).

Le contenu etait centre verticalement (justify-content:center), donc les slides
peu remplies avaient un grand vide en haut et un titre trop bas. On passe en
justify-content:flex-start avec un padding-top constant (13%), ce qui aligne
tous les titres a la meme hauteur et laisse le vide en bas.

Exclus : slide 1 (titre), intercalaires 3, 31, 50, 71, 100, 138, 155, 168, 181.
"""
import io
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

PATH = r"C:\ppt\index.html"
MARK = "/* ===== Alignement vertical des titres ===== */"

SKIP = {1, 3, 31, 50, 71, 100, 138, 155, 168, 181}
nums = [n for n in range(1, 213) if n not in SKIP]

selectors = ",\n".join(f".slide{n}" for n in nums)
CSS = (
    "\n" + MARK + "\n"
    "/* Titre et contenu alignes en haut, meme marge pour toutes les slides */\n"
    + selectors
    + " {\n  justify-content:flex-start;\n  padding-top:13vh;\n}\n"
    "/* Slides denses : grille reduite pour garder la note au-dessus du compteur */\n"
    ".slide196 .def-grid { height:54%; gap:1.6% 2%; margin-top:.6%; }\n"
    ".slide196 .ss-fx { margin:.4% auto; }\n"
    ".slide196 .ss-note { font-size:1.25vw; margin-top:.3%; }\n"
)

with open(PATH, encoding="utf-8") as f:
    html = f.read()

if MARK in html:
    start = html.index(MARK)
    end = html.index("</style>", start)
    html = html[:start] + CSS.lstrip("\n") + html[end:]
else:
    assert html.count("</style>") == 1
    html = html.replace("</style>", CSS + "</style>")

with open(PATH, "w", encoding="utf-8", newline="\n") as f:
    f.write(html)

print(f"OK : alignement haut applique a {len(nums)} slides")

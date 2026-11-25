# -*- coding: utf-8 -*-
"""Applique le style compact aux 12 quiz deja inserez dans index.html."""
import io
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
PATH = r"C:\ppt\index.html"
NUMS = [100, 101, 140, 141, 159, 160, 174, 175, 189, 190, 223, 224]
html = open(PATH, encoding="utf-8").read()

count = 0
for n in NUMS:
    old = '<section class="slide slide%d ' % n
    new = '<section class="slide slide%d quiz-compact ' % n
    assert html.count(old) == 1, "introuvable : " + old
    html = html.replace(old, new, 1)
    count += 1

css = (
    "/* Quiz chapitres 3 a 7 : verso compact pour les definitions longues */\n"
    ".quiz-compact .quiz-grid { height:78%; }\n"
    ".quiz-compact .quiz-face { gap:2.5%; padding:3% 6%; }\n"
    ".quiz-compact .q-opt { font-size:.86vw; line-height:1.25; padding:.55% 1.2%; }\n"
    ".quiz-compact .q-def { font-size:.78vw; line-height:1.3; padding:1% 1.5%; }\n"
    ".quiz-compact .q-verdict { font-size:.8vw; min-height:1vw; }\n\n"
)
mark = "/* ===== Alignement vertical des titres ===== */"
assert html.count(mark) == 1
html = html.replace(mark, css + mark, 1)
open(PATH, "w", encoding="utf-8", newline="\n").write(html)
print("OK : style compact applique a %d slides" % count)

# -*- coding: utf-8 -*-
"""Usage: python ch_titles.py START END [START END ...]"""
import io
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
s = open(r"C:\ppt\index.html", encoding="utf-8").read()
slides = {}
for m in re.finditer(r'<section class="slide\s+slide(\d+)[^"]*"[^>]*>(.*?)</section>', s, re.S):
    n = int(m.group(1))
    h = re.search(r"<h2[^>]*>(.*?)</h2>", m.group(2), re.S)
    t = re.sub(r"<[^>]+>", "", h.group(1)).strip() if h else "?"
    slides[n] = re.sub(r"\s+", " ", t)

args = [int(x) for x in sys.argv[1:]]
for i in range(0, len(args), 2):
    a, b = args[i], args[i + 1]
    print("=== %d-%d ===" % (a, b))
    for n in range(a, b + 1):
        print(n, slides.get(n, "?"))

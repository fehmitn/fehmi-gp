# -*- coding: utf-8 -*-
import io
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
s = open(r"C:\ppt\index.html", encoding="utf-8").read()
slides = re.findall(r'<section class="slide\s+(slide\d+)[^"]*"[^>]*>(.*?)</section>', s, re.S)
for cls, body in slides:
    if re.search(r"Chapitre\s*\d", body):
        hs = re.findall(r"<h2[^>]*>(.*?)</h2>", body)
        txt = [re.sub(r"<[^>]+>", "", h).strip() for h in hs]
        print(cls, " | ".join(txt))

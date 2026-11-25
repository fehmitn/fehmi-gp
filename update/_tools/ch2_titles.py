# -*- coding: utf-8 -*-
import io
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
s = open(r"C:\ppt\index.html", encoding="utf-8").read()
for m in re.finditer(r'<section class="slide\s+slide(\d+)[^"]*"[^>]*>(.*?)</section>', s, re.S):
    n = int(m.group(1))
    if 31 <= n <= 68:
        h = re.search(r"<h2[^>]*>(.*?)</h2>", m.group(2), re.S)
        t = re.sub(r"<[^>]+>", "", h.group(1)).strip() if h else "?"
        print(n, t)

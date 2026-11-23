# -*- coding: utf-8 -*-
import re, os, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
html = open(r"C:\ppt\index.html", encoding="utf-8").read()
secs = re.findall(r'<section class="slide[^"]*" data-i="(\d+)"', html)
nums = [int(x) for x in secs]
print("sections:", len(nums))
print("continu 0-209:", nums == list(range(210)))
print("compteur 210:", '<span id="tot">210</span>' in html)
exp = {171:'t-blur',172:'t-rotate',173:'t-zoom',174:'t-insert',175:'t-rise',176:'t-up',177:'t-push',178:'t-blur',179:'t-rotate',180:'t-zoom',
181:'t-insert',182:'t-rise',183:'t-up',184:'t-push',185:'t-blur',186:'t-rotate',187:'t-zoom',188:'t-insert',189:'t-rise',190:'t-up',
191:'t-push',192:'t-blur',193:'t-rotate',194:'t-zoom',195:'t-insert',196:'t-rise',197:'t-up',198:'t-push',199:'t-blur',200:'t-rotate',
201:'t-zoom',202:'t-insert',203:'t-rise',204:'t-up',205:'t-push',206:'t-blur',207:'t-rotate',208:'t-zoom',209:'t-insert',210:'t-rise'}
bad = []
for m in re.finditer(r'<section class="slide slide(\d+) ([\w-]+)"', html):
    n, t = int(m.group(1)), m.group(2)
    if n in exp and exp[n] != t:
        bad.append((n, t, exp[n]))
print("transitions OK:", not bad, bad)
imgs = set(re.findall(r'assets_ss_\w+\.png', html))
missing = [a for a in sorted(imgs) if not os.path.exists(r"C:\ppt\assets\\" + a)]
print("assets refs:", len(imgs), "manquants:", missing)

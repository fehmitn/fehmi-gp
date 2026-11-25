# -*- coding: utf-8 -*-
import re, os, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
html = open(r"C:\ppt\index.html", encoding="utf-8").read()
secs = re.findall(r'<section class="slide[^"]*" data-i="(\d+)"', html)
nums = [int(x) for x in secs]
AFTER = [99, 137, 154, 167, 180, 212]  # insertions de quiz (anciens numeros)


def remap(n):
    return n + 2 * sum(1 for k in AFTER if k < n)


print("sections:", len(nums))
print("continu 0-223:", nums == list(range(224)))
print("compteur 224:", '<span id="tot">224</span>' in html)
# Transitions des anciennes slides 173-212, recalculees apres les 6 insertions
exp_old = {173:'t-blur',174:'t-rotate',175:'t-zoom',176:'t-insert',177:'t-rise',178:'t-up',179:'t-push',180:'t-blur',181:'t-rotate',182:'t-zoom',
183:'t-insert',184:'t-rise',185:'t-up',186:'t-push',187:'t-blur',188:'t-rotate',189:'t-zoom',190:'t-insert',191:'t-rise',192:'t-up',
193:'t-push',194:'t-blur',195:'t-rotate',196:'t-zoom',197:'t-insert',198:'t-rise',199:'t-up',200:'t-push',201:'t-blur',202:'t-rotate',
203:'t-zoom',204:'t-insert',205:'t-rise',206:'t-up',207:'t-push',208:'t-blur',209:'t-rotate',210:'t-zoom',211:'t-insert',212:'t-rise'}
exp = {remap(k): v for k, v in exp_old.items()}
bad = []
for m in re.finditer(r'<section class="slide slide(\d+) ([\w-]+)"', html):
    n, t = int(m.group(1)), m.group(2)
    if n in exp and exp[n] != t:
        bad.append((n, t, exp[n]))
print("transitions OK:", not bad, bad)
imgs = set(re.findall(r'assets_ss_\w+\.png', html))
missing = [a for a in sorted(imgs) if not os.path.exists(r"C:\ppt\assets\\" + a)]
print("assets refs:", len(imgs), "manquants:", missing)

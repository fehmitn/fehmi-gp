# -*- coding: utf-8 -*-
import re, os, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
html = open(r"C:\ppt\index.html", encoding="utf-8").read()
secs = re.findall(r'<section class="slide[^"]*" data-i="(\d+)"', html)
nums = [int(x) for x in secs]
print("sections:", len(nums))
print("continu 0-169:", nums == list(range(170)))
print("compteur 170:", '<span id="tot">170</span>' in html)
exp = {131:'t-zoom',132:'t-insert',133:'t-rise',134:'t-up',135:'t-push',136:'t-blur',137:'t-rotate',138:'t-zoom',139:'t-insert',140:'t-rise',141:'t-up',142:'t-push',143:'t-blur',144:'t-rotate',145:'t-zoom',146:'t-insert',147:'t-rise',148:'t-up',149:'t-push',150:'t-blur',151:'t-rotate',152:'t-zoom',153:'t-insert',154:'t-rise',155:'t-up',156:'t-push',157:'t-blur',158:'t-rotate',159:'t-zoom',160:'t-insert',161:'t-rise',162:'t-up',163:'t-push',164:'t-blur',165:'t-rotate',166:'t-zoom',167:'t-insert',168:'t-rise',169:'t-up',170:'t-push'}
bad = []
for m in re.finditer(r'<section class="slide slide(\d+) ([\w-]+)"', html):
    n, t = int(m.group(1)), m.group(2)
    if n in exp and exp[n] != t:
        bad.append((n, t, exp[n]))
print("transitions OK:", not bad, bad)
imgs = set(re.findall(r'assets_ss_(?:image|fx)\w*\.png', html))
missing = [a for a in sorted(imgs) if not os.path.exists(r"C:\ppt\assets\\" + a)]
print("assets refs:", len(imgs), "manquants:", missing)

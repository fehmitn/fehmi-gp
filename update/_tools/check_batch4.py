# -*- coding: utf-8 -*-
import re, io, sys, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
html = open(r"C:\ppt\index.html", encoding="utf-8").read()
print("sections:", html.count('<section class="slide'))
print("tot 130:", html.count('<span id="tot">130</span>'))
secs = re.findall(r'<section class="slide[^>]*>', html)
print("toutes ont data-t:", all("data-t=" in s for s in secs))
for img in ["assets_ss_image84.png", "assets_ss_image94.png"]:
    print(img, "refs:", html.count(img), "exists:", os.path.exists(r"C:\ppt\assets" + os.sep + img))
idx = [int(m) for m in re.findall(r'data-i="(\d+)"', html)]
print("data-i continu 0..129:", idx == list(range(130)))
cycle = ["t-rise", "t-up", "t-push", "t-blur", "t-rotate", "t-zoom", "t-insert"]
ok = True
for i, s in enumerate(secs):
    if i < 97:
        continue
    m = re.search(r"(t-\w+)", s)
    t = m.group(1) if m else "?"
    exp = cycle[(i - 97) % 7]
    if t != exp:
        ok = False
        print("transition inattendue i=", i, t, "attendu", exp)
print("cycle transitions coherent:", ok)
# ribbons absents (hors intercalaires 1/18/30/50/69/98)
no_ribbon = []
start = 0
for m in re.finditer(r'<section class="slide[^"]*" data-i="(\d+)"', html):
    i = int(m.group(1))
    end = html.find("</section>", m.start())
    if "ribbon" not in html[m.start():end]:
        no_ribbon.append(i + 1)
print("slides sans ribbon:", no_ribbon, "(attendu intercalaires: [1, 18, 30, 50, 69, 98])")

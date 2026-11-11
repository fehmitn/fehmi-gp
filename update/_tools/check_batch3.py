# -*- coding: utf-8 -*-
import io, sys, os, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
html = open(r"C:\ppt\index.html", encoding="utf-8").read()
print("sections:", html.count('<section class="slide'))
print("data-i last:", html.count('data-i="99"'))
print("tot 100:", html.count('<span id="tot">100</span>'))
print("img41:", html.count("assets_ss_image41.png"), " img59:", html.count("assets_ss_image59.png"))
print("files exist:", os.path.exists(r"C:\ppt\assets\assets_ss_image41.png"),
      os.path.exists(r"C:\ppt\assets\assets_ss_image59.png"))
for i in [70, 71, 97, 98, 99]:
    m = re.search(r'class="slide slide\d+ (t-\w+)" data-i="%d" data-t="([^"]+)"' % i, html)
    print(i, m.group(0) if m else "MISSING")
# verif: chaque slide a un h2 et un data-t
secs = re.findall(r'<section class="slide[^>]*>', html)
print("toutes les sections ont data-t:", all("data-t=" in s for s in secs))
print("slides sans ribbon (hors intercalaires 1/18/30/50/69/98):")

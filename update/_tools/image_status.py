# -*- coding: utf-8 -*-
"""Etat des images utilisees dans index.html : fonds par slide + images inline."""
import io
import re
import sys
from collections import defaultdict

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
s = open(r"C:\ppt\index.html", encoding="utf-8").read()

# Regles CSS .slideN { ... url('assets/xxx') ... }
bg = defaultdict(list)
for m in re.finditer(r"\.slide(\d+)\s*\{([^}]*)\}", s):
    n = int(m.group(1))
    urls = re.findall(r"url\(['\"]?(assets/[^'\")]+)", m.group(2))
    for u in urls:
        bg[n].append(u)

print("=== FONDS PAR SLIDE ===")
groups = defaultdict(list)
for n in sorted(bg):
    groups[tuple(bg[n])].append(n)
def ranges(nums):
    out, start, prev = [], nums[0], nums[0]
    for n in nums[1:]:
        if n != prev + 1:
            out.append(str(start) if start == prev else "%d-%d" % (start, prev))
            start = n
        prev = n
    out.append(str(start) if start == prev else "%d-%d" % (start, prev))
    return ", ".join(out)

for imgs, nums in sorted(groups.items(), key=lambda kv: kv[1][0]):
    print("%-32s %3d slides : %s" % (", ".join(imgs), len(nums), ranges(nums)))

print("\n=== IMAGES INLINE (contenu des slides, pas des fonds) ===")
inline = defaultdict(list)
for m in re.finditer(r'<section class="slide\s+slide(\d+)[^"]*"[^>]*>(.*?)</section>', s, re.S):
    n = int(m.group(1))
    for u in re.findall(r'src=["\'](assets/[^"\']+)["\']', m.group(2)):
        inline[u].append(n)
for u, nums in sorted(inline.items(), key=lambda kv: kv[1][0]):
    print("%-34s slides %s" % (u, ", ".join(map(str, nums))))

print("\n=== IMAGES GENEREES (_grok) ===")
grok = [u for u in set(sum(bg.values(), [])) if "grok" in u.lower()]
grok += [u for u in inline if "grok" in u.lower()]
print(grok if grok else "AUCUNE")

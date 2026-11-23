# -*- coding: utf-8 -*-
"""Telecharge les photos libres choisies en 1920x1080, les retravaille
(recadrage 16:9, leger flou, assombrissement) et ecrit les credits.

Suffixe _online demande par l'utilisateur.
"""
import io
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from PIL import Image, ImageEnhance, ImageFilter

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

BASE = r"C:\ppt"
OUT = os.path.join(BASE, "assets")
BG = os.path.join(BASE, "_check", "bg")
UA = {"User-Agent": "ppt-backgrounds/1.0 (educational slides; contact: local)"}
API = "https://commons.wikimedia.org/w/api.php"

# theme -> [(dossier source, id), ...]  (2 variantes par theme)
CHOSEN = {
    "planning": [("planning", 13), ("planning", 9)],
    "erp": [("erp", 0), ("erp", 4)],
    "stock": [("stock", 2), ("stock", 15)],
    "forecast": [("forecast2", 0), ("forecast", 7)],
    "kanban": [("kanban", 6), ("kanban", 4)],
    "lean": [("lean", 3), ("lean", 5)],
}


def api(params):
    params = dict(params)
    params["format"] = "json"
    url = API + "?" + urllib.parse.urlencode(params)
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception as e:
            if "429" in str(e):
                time.sleep(8 * (attempt + 1))
                continue
            raise
    raise RuntimeError("API KO")


def get_1920(title):
    d = api({
        "action": "query",
        "titles": title,
        "prop": "imageinfo",
        "iiprop": "url|extmetadata|size",
        "iiurlwidth": "1920",
    })
    pages = (d.get("query") or {}).get("pages") or {}
    for page in pages.values():
        ii = (page.get("imageinfo") or [None])[0]
        if ii:
            em = ii.get("extmetadata") or {}
            def meta(k):
                v = em.get(k) or {}
                return re.sub(r"<[^>]+>", "", str(v.get("value", ""))).strip()
            return {
                "thumb": ii.get("thumburl") or ii.get("url"),
                "page": ii.get("descriptionurl"),
                "artist": meta("Artist"),
                "license": meta("LicenseShortName"),
                "licenseurl": meta("LicenseUrl"),
            }
    return None


def process(src_bytes, dst):
    im = Image.open(io.BytesIO(src_bytes)).convert("RGB")
    w, h = im.size
    target = 16 / 9
    if w / h > target:
        nw = int(h * target)
        im = im.crop(((w - nw) // 2, 0, (w + nw) // 2, h))
    else:
        nh = int(w / target)
        im = im.crop((0, (h - nh) // 2, w, (h + nh) // 2))
    im = im.resize((1920, 1080), Image.LANCZOS)
    im = im.filter(ImageFilter.GaussianBlur(1.6))
    im = ImageEnhance.Brightness(im).enhance(0.78)
    im = ImageEnhance.Color(im).enhance(0.85)
    im = ImageEnhance.Contrast(im).enhance(1.04)
    im.save(dst, "JPEG", quality=84, optimize=True)
    return im.size


def main():
    cands = json.load(open(os.path.join(BG, "candidates.json"), encoding="utf-8"))
    credits = []
    for theme, pairs in CHOSEN.items():
        for idx, (folder, cid) in enumerate(pairs):
            entry = next((c for c in cands.get(folder, []) if c["id"] == cid), None)
            if not entry:
                print("!! introuvable", folder, cid)
                continue
            info = get_1920(entry["title"])
            if not info or not info["thumb"]:
                print("!! url 1920 introuvable", entry["title"])
                continue
            req = urllib.request.Request(info["thumb"], headers=UA)
            data = None
            for attempt in range(5):
                try:
                    with urllib.request.urlopen(req, timeout=180) as r:
                        data = r.read()
                    break
                except Exception as e:
                    if "429" in str(e):
                        wait = 20 * (attempt + 1)
                        print("   429 download -> attente " + str(wait) + "s")
                        import time as _t
                        _t.sleep(wait)
                        continue
                    raise
            if data is None:
                print("!! download impossible", entry["title"])
                continue
            suffix = "" if idx == 0 else "_b"
            dst = os.path.join(OUT, "bg_" + theme + "_online" + suffix + ".jpg")
            size = process(data, dst)
            print(theme + suffix + ": " + str(size) + " <- " + entry["title"])
            credits.append({
                "fichier": os.path.basename(dst),
                "titre": entry["title"],
                "auteur": info["artist"],
                "licence": info["license"],
                "licence_url": info["licenseurl"],
                "page": info["page"],
            })
            time.sleep(2)

    lines = [
        "# Crédits des photos de fond (`assets/bg_*_online.jpg`)",
        "",
        "Photos issues de Wikimedia Commons, recadrées en 1920×1080, légèrement",
        "floutées et assombries pour servir de fond de diapositive.",
        "",
        "| Fichier | Titre | Auteur | Licence | Source |",
        "|---|---|---|---|---|",
    ]
    for c in credits:
        lines.append(
            f"| `{c['fichier']}` | {c['titre']} | {c['auteur'] or '—'} | "
            f"[{c['licence'] or '—'}]({c['licence_url'] or ''}) | [Commons]({c['page']}) |"
        )
    open(os.path.join(OUT, "BACKGROUNDS-CREDITS.md"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
    json.dump(credits, open(os.path.join(BG, "chosen.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("credits -> assets/BACKGROUNDS-CREDITS.md")


if __name__ == "__main__":
    main()

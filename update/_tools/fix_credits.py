# -*- coding: utf-8 -*-
"""Complete assets/BACKGROUNDS-CREDITS.md pour les fonds deja telecharges
avant la mise en place du suivi des credits (stock x2, forecast x1).

Interroge Commons pour recuperer auteur / licence a partir du titre identifie
par match_bg.py, puis reecrit le tableau complet.
"""
import io
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

BASE = r"C:\ppt"
OUT = os.path.join(BASE, "assets")
BG = os.path.join(BASE, "_check", "bg")
UA = {"User-Agent": "ppt-backgrounds/1.0 (educational slides; contact: local)"}
API = "https://commons.wikimedia.org/w/api.php"

MISSING = {
    "bg_stock_online.jpg": "File:Pallets for Gustav.jpg",
    "bg_stock_online_b.jpg": "File:Modern warehouse with pallet rack storage system.jpg",
    "bg_forecast_online.jpg": "File:Frankfurt Stock Exchange (Ank Kumar) 03.jpg",
}


def meta(title):
    p = {"action": "query", "titles": title, "prop": "imageinfo",
         "iiprop": "url|extmetadata", "format": "json"}
    url = API + "?" + urllib.parse.urlencode(p)
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=60) as r:
                d = json.loads(r.read().decode("utf-8"))
            break
        except Exception as e:
            if "429" in str(e):
                time.sleep(8 * (attempt + 1))
                continue
            raise
    for page in ((d.get("query") or {}).get("pages") or {}).values():
        ii = (page.get("imageinfo") or [None])[0]
        if not ii:
            continue
        em = ii.get("extmetadata") or {}

        def val(k):
            v = em.get(k) or {}
            return re.sub(r"<[^>]+>", "", str(v.get("value", ""))).strip()

        return {
            "fichier": "",
            "titre": title,
            "auteur": val("Artist"),
            "licence": val("LicenseShortName"),
            "licence_url": val("LicenseUrl"),
            "page": ii.get("descriptionurl"),
        }
    return None


def main():
    path = os.path.join(BG, "chosen.json")
    credits = json.load(open(path, encoding="utf-8")) if os.path.exists(path) else []
    known = {c["fichier"] for c in credits}
    for fname, title in MISSING.items():
        if fname in known:
            continue
        c = meta(title)
        if not c:
            print("!! metadata introuvable", title)
            continue
        c["fichier"] = fname
        credits.append(c)
        print("+", fname, "<-", title)
        time.sleep(2)
    credits.sort(key=lambda c: c["fichier"])

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
            "| `" + c["fichier"] + "` | " + c["titre"] + " | " + (c["auteur"] or "—")
            + " | [" + (c["licence"] or "—") + "](" + (c["licence_url"] or "") + ")"
            + " | [Commons](" + c["page"] + ") |"
        )
    open(os.path.join(OUT, "BACKGROUNDS-CREDITS.md"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
    json.dump(credits, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("OK :", len(credits), "credits")


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""Reconstruit les dossiers de vignettes a partir de candidates.json.

Probleme corrige : apres une nouvelle recherche, candidates.json contenait de
nouveaux titres mais les fichiers <id>.jpg des anciennes recherches restaient.
L'index ne correspondait donc plus au titre, et on telechargeait la mauvaise
photo en 1920px.

Ici on re-telecharge la vignette 640px de CHAQUE titre, en ecrasant le fichier,
pour garantir : fichier <id>.jpg == titre candidates.json[id].

Usage : python rebuild_dirs.py theme [theme ...]
"""
import io
import json
import os
import sys
import time
import urllib.parse
import urllib.request

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

BG = r"C:\ppt\_check\bg"
UA = {"User-Agent": "ppt-backgrounds/1.0 (educational slides; contact: local)"}
API = "https://commons.wikimedia.org/w/api.php"


def api(params):
    params = dict(params)
    params["format"] = "json"
    url = API + "?" + urllib.parse.urlencode(params)
    for attempt in range(6):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception as e:
            msg = str(e)
            if "429" in msg or "503" in msg or "timed out" in msg.lower():
                wait = 10 * (attempt + 1)
                print("   api " + msg[:30] + " -> " + str(wait) + "s")
                time.sleep(wait)
                continue
            raise
    raise RuntimeError("API KO")


def thumb_640(title):
    d = api({
        "action": "query",
        "titles": title,
        "prop": "imageinfo",
        "iiprop": "url",
        "iiurlwidth": "640",
    })
    for page in ((d.get("query") or {}).get("pages") or {}).values():
        ii = (page.get("imageinfo") or [None])[0]
        if ii:
            return ii.get("thumburl") or ii.get("url")
    return None


def fetch(url):
    for attempt in range(6):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=120) as r:
                return r.read()
        except Exception as e:
            msg = str(e)
            if "429" in msg or "503" in msg:
                wait = 15 * (attempt + 1)
                print("   429 thumb -> " + str(wait) + "s")
                time.sleep(wait)
                continue
            print("   KO " + msg[:50])
            return None
    return None


def main():
    cands = json.load(open(os.path.join(BG, "candidates.json"), encoding="utf-8"))
    for theme in sys.argv[1:]:
        items = cands.get(theme) or []
        d = os.path.join(BG, theme + "_fix")
        os.makedirs(d, exist_ok=True)
        ok = 0
        for c in items:
            dst = os.path.join(d, "%02d.jpg" % c["id"])
            if os.path.exists(dst) and os.path.getsize(dst) > 5000:
                ok += 1
                continue
            u = thumb_640(c["title"])
            if not u:
                print("!! thumb introuvable", c["title"])
                continue
            data = fetch(u)
            if not data:
                continue
            open(dst, "wb").write(data)
            ok += 1
            time.sleep(1.2)
        print(theme + ": " + str(ok) + "/" + str(len(items)) + " -> " + theme + "_fix/")


if __name__ == "__main__":
    main()

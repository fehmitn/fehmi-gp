# -*- coding: utf-8 -*-
"""Recherche de photos libres (Wikimedia Commons) pour les fonds de slides.

Usage : python find_backgrounds.py [theme ...]
Sans argument : tous les themes.
"""
import io
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from PIL import Image, ImageDraw

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

UA = {"User-Agent": "ppt-backgrounds/1.0 (educational slides; contact: local)"}
API = "https://commons.wikimedia.org/w/api.php"
OUT = r"C:\ppt\_check\bg"

THEMES = {
    "planning": [
        "production planning control room",
        "operations control room screens",
        "gantt chart",
        "project planning meeting",
    ],
    "erp": [
        "data center server room",
        "server racks blue",
        "network operations center",
    ],
    "stock": [
        "warehouse interior pallet",
        "distribution warehouse shelves",
        "logistics warehouse",
        "pallet racking",
        "storage warehouse boxes",
    ],
    "forecast": [
        "trading floor screens",
        "stock exchange screens",
        "business charts screen",
        "data visualization dashboard",
        "statistics graph screen",
    ],
    "kanban": [
        "kanban board",
        "sticky notes wall",
        "production planning board",
        "lean manufacturing board",
        "shop floor board",
    ],
    "lean": [
        "assembly line factory",
        "car assembly line",
        "industrial robot arm factory",
        "machine workshop",
        "cnc workshop",
    ],
    "forecast2": [
        "trading floor screens",
        "stock exchange trading floor",
        "financial data screens",
        "market data wall",
        "control room charts",
        "business presentation graph screen",
    ],
    "kanban2": [
        "sticky note board",
        "index cards wall",
        "planning board factory",
        "production board workshop",
        "task board office",
        "note cards board",
    ],
    "lean3": [
        "lean manufacturing",
        "lean manufacturing assembly line",
        "lean production workshop",
        "just in time manufacturing",
        "factory assembly line workers",
        "industrial production line",
    ],
    "lean4": [
        "automotive assembly line robots",
        "car factory welding robots",
        "robotic arm production line",
        "industrial robot welding",
        "factory conveyor belt production",
    ],
}


def api(params, tries=5):
    params = dict(params)
    params["format"] = "json"
    url = API + "?" + urllib.parse.urlencode(params)
    last = None
    for attempt in range(tries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=45) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception as e:
            last = e
            msg = str(e)
            if "429" in msg or "503" in msg or "timed out" in msg.lower():
                wait = 10 * (attempt + 1)
                print(f"    ... {msg[:40]} -> attente {wait}s")
                time.sleep(wait)
                continue
            raise
    raise last


def search(term):
    p = {
        "action": "query",
        "generator": "search",
        "gsrsearch": f"filetype:bitmap {term}",
        "gsrnamespace": "6",
        "gsrlimit": "6",
        "prop": "imageinfo",
        "iiprop": "url|extmetadata|size",
        "iiurlwidth": "640",
    }
    try:
        d = api(p)
    except Exception as e:
        print("  ! recherche KO:", term, e)
        return []
    pages = (d.get("query") or {}).get("pages") or {}
    out = []
    for page in pages.values():
        ii = (page.get("imageinfo") or [None])[0]
        if not ii:
            continue
        em = ii.get("extmetadata") or {}
        def meta(k):
            v = em.get(k) or {}
            return re.sub(r"<[^>]+>", "", str(v.get("value", ""))).strip()
        out.append({
            "title": page.get("title", ""),
            "thumb": ii.get("thumburl"),
            "full": ii.get("url"),
            "width": ii.get("width"),
            "height": ii.get("height"),
            "artist": meta("Artist"),
            "license": meta("LicenseShortName"),
            "licenseurl": meta("LicenseUrl"),
            "page": ii.get("descriptionurl"),
        })
    return out


def build(theme):
    terms = THEMES[theme]
    seen = set()
    cands = []
    for t in terms:
        print("  recherche:", t)
        for c in search(t):
            if c["title"] in seen:
                continue
            if not c["thumb"] or not c["full"]:
                continue
            if c["width"] and c["height"] and c["height"] > c["width"] * 0.9:
                continue
            if c["width"] and c["width"] < 1000:
                continue
            seen.add(c["title"])
            cands.append(c)
        time.sleep(4)
    cands = cands[:16]
    d = os.path.join(OUT, theme)
    os.makedirs(d, exist_ok=True)
    for i, c in enumerate(cands):
        fn = os.path.join(d, f"{i:02d}.jpg")
        if os.path.exists(fn):
            c["local"] = fn
            c["theme"] = theme
            c["id"] = i
            continue
        try:
            req = urllib.request.Request(c["thumb"], headers=UA)
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
            open(fn, "wb").write(data)
            c["local"] = fn
            c["theme"] = theme
            c["id"] = i
        except Exception as e:
            print("  ! telechargement KO", c["title"], e)
        time.sleep(1)
    cands = [c for c in cands if c.get("local")]
    if not cands:
        print(f"{theme}: aucun candidat")
        return []
    cols = 4
    rows = (len(cands) + cols - 1) // cols
    tw, th = 460, 260
    sheet = Image.new("RGB", (cols * tw, rows * (th + 24)), (18, 22, 34))
    dr = ImageDraw.Draw(sheet)
    for i, c in enumerate(cands):
        im = Image.open(c["local"]).convert("RGB")
        im.thumbnail((tw - 8, th - 8))
        x = (i % cols) * tw + (tw - im.width) // 2
        y = (i // cols) * (th + 24) + (th - im.height) // 2
        sheet.paste(im, (x, y))
        dr.text(((i % cols) * tw + 8, (i // cols) * (th + 24) + th + 4),
                f"{i} - {c['license'][:18]}", fill=(255, 220, 150))
    sheet.save(os.path.join(OUT, f"{theme}_sheet.jpg"), quality=88)
    print(f"{theme}: {len(cands)} candidats -> {theme}_sheet.jpg")
    return cands


def main():
    os.makedirs(OUT, exist_ok=True)
    themes = sys.argv[1:] or list(THEMES)
    path = os.path.join(OUT, "candidates.json")
    all_c = {}
    if os.path.exists(path):
        try:
            all_c = json.load(open(path, encoding="utf-8"))
        except Exception:
            all_c = {}
    for theme in themes:
        all_c[theme] = build(theme)
        json.dump(all_c, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        time.sleep(5)


if __name__ == "__main__":
    main()

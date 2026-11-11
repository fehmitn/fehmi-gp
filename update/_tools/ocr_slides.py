# -*- coding: utf-8 -*-
"""OCR des slides du slideshare-file.pptx (slides = images PNG).

Usage : python ocr_slides.py <debut> <fin>   (1-indexed)
Ecrit :  update/ocr_texts/slide_NNN.txt  (texte brut OCR)
         update/_ocr_state.json          (checkpoint de progression)
"""
import os
import re
import sys
import json
from PIL import Image
import pytesseract

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

MEDIA = r"C:\ppt\_check\ppt\media"
GDIR = r"C:\ppt\update\ocr_texts"
STATE = r"C:\ppt\update\_ocr_state.json"
SLIDES_DIR = r"C:\ppt\_check\ppt\slides"

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
TD = r"--tessdata-dir C:\ppt\tessdata"

TOTAL = 180
OFFSET = 30  # nombre de slides deja presentes dans index.html avant l'ajout


def rel_target(n):
    rels = os.path.join(SLIDES_DIR, "_rels", f"slide{n}.xml.rels")
    if not os.path.exists(rels):
        return f"image{n}.bin"
    with open(rels, encoding="utf-8") as f:
        m = re.search(r'Target="[^"]*media/([^"]+)"', f.read())
    return m.group(1) if m else f"image{n}.bin"


def load_state():
    if os.path.exists(STATE):
        with open(STATE, encoding="utf-8") as f:
            return json.load(f)
    return {"source": "slidsahre-file.pptx", "total_slides": TOTAL,
            "presentation_offset": OFFSET, "done": []}


def save_state(st):
    st["done"] = sorted(set(st["done"]))
    st["next"] = min(n for n in range(1, TOTAL + 1) if n not in st["done"]) \
        if len(st["done"]) < TOTAL else None
    with open(STATE, "w", encoding="utf-8") as f:
        json.dump(st, f, ensure_ascii=False, indent=2)


def main():
    a = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    b = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    os.makedirs(GDIR, exist_ok=True)
    state = load_state()
    for n in range(a, b + 1):
        p = os.path.join(MEDIA, rel_target(n))
        out = os.path.join(GDIR, f"slide_{n:03d}.txt")
        if os.path.exists(out):
            print(f"slide {n:3d} -> deja fait, passe")
        else:
            img = Image.open(p)
            txt = pytesseract.image_to_string(img, lang="fra", config=TD).strip()
            with open(out, "w", encoding="utf-8") as f:
                f.write(txt)
            print(f"slide {n:3d} ({img.size[0]}x{img.size[1]}) -> {out} [{len(txt)} car.]")
            img.close()
        if n not in state["done"]:
            state["done"].append(n)
    save_state(state)
    print("\nEtat:", state["done"][:5], "...", state["done"][-5:])
    print("Prochaine slide:", state["next"])


if __name__ == "__main__":
    main()

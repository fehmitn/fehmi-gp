# -*- coding: utf-8 -*-
"""Ajoute un fond photo thematique par chapitre aux slides qui n'en ont pas.

Chapitres concernes (les intercalaires rouges sont exclus) :
  Ch2 Planification : 32-49, 51-68   -> bg_planning_online(.jpg/_b.jpg)
  Ch3 ERP/GPAO      : 70-97          -> bg_erp_online(.jpg/_b.jpg)
  Ch3 Stocks        : 99-135         -> bg_stock_online(.jpg/_b.jpg)
  Ch4 Previsions    : 137-152        -> bg_forecast_online(.jpg/_b.jpg)
  Ch5 Kanban        : 154-165        -> bg_kanban_online(.jpg/_b.jpg)
  Ch6 JAT / lean    : 167-178        -> bg_lean_online(.jpg/_b.jpg)
  Ch7 Logistique    : 180-210        -> photos existantes (port, conteneurs, quais)

Petites variations dans un chapitre : alternance des 2 variantes d'image, cadrage
decale (center / left / right / haut / bas) et voile sombre legerement module.

Idempotent : le bloc est remplace entre son marqueur et </style>.
"""
import io
import os
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

PATH = r"C:\ppt\index.html"
MARK = "/* ===== FONDS PHOTO PAR CHAPITRE ===== */"

CHAPTERS = [
    ("Chapitre 2 — Planification", list(range(32, 50)) + list(range(51, 69)),
     ["bg_planning_online.jpg", "bg_planning_online_b.jpg"]),
    ("Chapitre 3 — ERP / GPAO", list(range(70, 98)),
     ["bg_erp_online.jpg", "bg_erp_online_b.jpg"]),
    ("Chapitre 3 — Gestion des stocks", list(range(99, 136)),
     ["bg_stock_online.jpg", "bg_stock_online_b.jpg"]),
    ("Chapitre 4 — Prévisions", list(range(137, 153)),
     ["bg_forecast_online.jpg", "bg_forecast_online_b.jpg"]),
    ("Chapitre 5 — Kanban", list(range(154, 166)),
     ["bg_kanban_online.jpg", "bg_kanban_online_b.jpg"]),
    ("Chapitre 6 — Juste-à-temps / lean", list(range(167, 179)),
     ["bg_lean_online.jpg", "bg_lean_online_b.jpg"]),
    ("Chapitre 7 — Logistique", list(range(180, 211)),
     ["bg_port_day.jpg", "bg_container_load.jpg", "bg_night_dock.jpg",
      "bg_palletizing.jpg", "bg_warehouse_dark.jpg", "bg_port_dusk.jpg",
      "bg_warehouse_rack.jpg"]),
]

POSITIONS = ["center 50%", "left 45%", "right 55%", "center 35%", "center 65%"]
OVERLAYS = [(.86, .91), (.87, .92), (.88, .93), (.86, .92)]


def build_css():
    out = [MARK, "/* Un thème visuel par chapitre, avec de légères variations d'image,",
           "   de cadrage et de voile d'une slide à l'autre. */"]
    for name, nums, images in CHAPTERS:
        out.append("")
        out.append("/* " + name + " */")
        for i, n in enumerate(nums):
            img = images[(i // 2) % len(images)]
            pos = POSITIONS[(i // 3) % len(POSITIONS)]
            a, b = OVERLAYS[i % len(OVERLAYS)]
            out.append(
                ".slide%d { background: linear-gradient(rgba(11,18,37,%.2f), rgba(11,18,37,%.2f)), "
                "url('assets/%s') %s/cover no-repeat; }" % (n, a, b, img, pos)
            )
    return "\n".join(out) + "\n"


def main():
    css = build_css()
    with open(PATH, encoding="utf-8") as f:
        html = f.read()

    if MARK in html:
        start = html.index(MARK)
        end = html.index("</style>", start)
        html = html[:start] + css + html[end:]
    else:
        assert html.count("</style>") == 1
        html = html.replace("</style>", css + "</style>")

    with open(PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(html)

    total = sum(len(c[1]) for c in CHAPTERS)
    print("OK : fonds appliques a %d slides (7 chapitres)" % total)
    missing = set()
    for _, _, images in CHAPTERS:
        for img in images:
            if not os.path.exists(os.path.join(r"C:\ppt\assets", img)):
                missing.add(img)
    if missing:
        print("!! images manquantes : " + ", ".join(sorted(missing)))
    else:
        print("OK : toutes les images referencees existent dans assets/")


if __name__ == "__main__":
    main()

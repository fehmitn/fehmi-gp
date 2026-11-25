# -*- coding: utf-8 -*-
"""Ajoute un fond photo thematique par chapitre aux slides qui n'en ont pas.

Chapitres concernes (les intercalaires rouges sont exclus) :
  Ch2 Planification : 32-49, 51-70   -> bg_planning_online(.jpg/_b.jpg)
  Ch3 ERP/GPAO      : 72-101         -> bg_erp_online(.jpg/_b.jpg)
  Ch3 Stocks        : 103-141        -> bg_stock_online(.jpg/_b.jpg)
  Ch4 Previsions    : 143-160        -> bg_forecast_online(.jpg/_b.jpg)
  Ch5 Kanban        : 162-175        -> bg_kanban_online(.jpg/_b.jpg)
  Ch6 JAT / lean    : 177-190        -> bg_lean_online(.jpg/_b.jpg)
  Ch7 Logistique    : 192-224        -> photos existantes (port, conteneurs, quais)

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
    ("Chapitre 2 — Planification", list(range(32, 50)) + list(range(51, 71)),
     ["bg_planning_online.jpg", "bg_planning_online_b.jpg"]),
    ("Chapitre 3 — ERP / GPAO", list(range(72, 102)),
     ["bg_erp_online.jpg", "bg_erp_online_b.jpg"]),
    ("Chapitre 3 — Gestion des stocks", list(range(103, 142)),
     ["bg_stock_online.jpg", "bg_stock_online_b.jpg"]),
    ("Chapitre 4 — Prévisions", list(range(143, 161)),
     ["bg_forecast_online.jpg", "bg_forecast_online_b.jpg"]),
    ("Chapitre 5 — Kanban", list(range(162, 176)),
     ["bg_kanban_online.jpg", "bg_kanban_online_b.jpg"]),
    ("Chapitre 6 — Juste-à-temps / lean", list(range(177, 191)),
     ["bg_lean_online.jpg", "bg_lean_online_b.jpg"]),
    ("Chapitre 7 — Logistique", list(range(192, 225)),
     ["bg_port_day.jpg", "bg_container_load.jpg", "bg_night_dock.jpg",
      "bg_palletizing.jpg", "bg_warehouse_dark.jpg", "bg_port_dusk.jpg",
      "bg_warehouse_rack.jpg"]),
]

POSITIONS = ["center 50%", "left 45%", "right 55%", "center 35%", "center 65%"]
OVERLAYS = [(.86, .91), (.87, .92), (.88, .93), (.86, .92)]

# Intercalaires de chapitre (et slide 11 restée en rouge par erreur) : plus de
# degrade rouge uni, un vrai fond photo avec voile sombre. flex-direction:column
# est conserve car il porte la mise en page de ces slides.
SEPARATORS = [
    (11, "bg_robots_yellow.jpg", "center 50%", .82, .92),
    (31, "bg_planning_online.jpg", "center 45%", .80, .90),
    (50, "bg_planning_online_b.jpg", "center 50%", .80, .90),
    (71, "bg_erp_online.jpg", "center 45%", .80, .90),
    (102, "bg_stock_online.jpg", "center 45%", .80, .90),
    (142, "bg_forecast_online.jpg", "center 45%", .86, .94),
    (161, "bg_kanban_online.jpg", "center 50%", .80, .90),
    (176, "bg_lean_online.jpg", "center 50%", .80, .90),
    (191, "bg_port_dusk.jpg", "center 50%", .80, .90),
]


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
    out.append("")
    out.append("/* Intercalaires de chapitre : fond photo a la place du rouge uni */")
    for n, img, pos, a, b in SEPARATORS:
        pad = "13vh" if n == 11 else "28vh"
        out.append(
            ".slide%d { flex-direction:column; justify-content:flex-start; padding-top:%s; "
            "background: linear-gradient(rgba(11,18,37,%.2f), "
            "rgba(11,18,37,%.2f)), url('assets/%s') %s/cover no-repeat; }" % (n, pad, a, b, img, pos)
        )
    pictos = ", ".join(".slide%d .picto" % n for n, _, _, _, _ in SEPARATORS if n != 11)
    out.append("/* picto des intercalaires : grand, en bas a droite, comme la slide 3 */")
    out.append(
        pictos + " { font-size:10vw; position:absolute; right:6%; bottom:5%; opacity:.45; "
        "animation:floaty 3.5s ease-in-out infinite; }"
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
    print("OK : %d intercalaires passes du rouge uni au fond photo" % len(SEPARATORS))
    missing = set()
    for _, _, images in CHAPTERS:
        for img in images:
            if not os.path.exists(os.path.join(r"C:\ppt\assets", img)):
                missing.add(img)
    for _, img, _, _, _ in SEPARATORS:
        if not os.path.exists(os.path.join(r"C:\ppt\assets", img)):
            missing.add(img)
    if missing:
        print("!! images manquantes : " + ", ".join(sorted(missing)))
    else:
        print("OK : toutes les images referencees existent dans assets/")


if __name__ == "__main__":
    main()

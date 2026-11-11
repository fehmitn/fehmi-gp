# -*- coding: utf-8 -*-
"""Correctif retour utilisateur : a partir de la slide 32 le titre est a gauche
et noir.

Cause : dans l'ancien deck, les styles de titre (h2 blanc) et de ruban (.ribbon)
sont definis PAR SLIDE (.slide3 h2 ..., .slideN .ribbon ...) pour les slides
1-30 uniquement. Les slides 31-70 (slideshare) ne sont couvertes nulle part :
- aucune couleur -> titre noir (defaut navigateur) ;
- flex par defaut en row -> titre a gauche, centre verticalement ;
- pas de .ribbon global -> ruban invisible.

Fix : un bloc CSS couvrant .slide31 ... .slide70 :
- flex-direction:column ;
- h2 blanc, 3vw, bold, aligne en haut a gauche (intercalaires S31/S50/S69 :
  font-weight:900, leur font-size inline reste prioritaire) ;
- .ribbon orange/rouge.
"""
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
PATH = r"C:\ppt\index.html"

nums = list(range(31, 71))

sel_col = ", ".join(f".slide{n}" for n in nums)
sel_h2 = ", ".join(f".slide{n} h2" for n in nums)
sel_rib = ", ".join(f".slide{n} .ribbon" for n in nums)
sel_inter = ", ".join(f".slide{n} h2" for n in (31, 50, 69))

CSS = f"""
/* ===== Correctif titres slides 31-70 ===== */
{sel_col} {{ flex-direction:column; }}
{sel_h2} {{
  font-size:3vw; color:#fff; font-weight:700; margin-bottom:.5%;
  align-self:flex-start;
}}
{sel_inter} {{ font-weight:900; margin-bottom:0; }}
{sel_rib} {{
  width:8%; height:5px; background:linear-gradient(90deg,#f39c12,#e74c3c);
  border-radius:5px; margin-bottom:3%; align-self:flex-start;
}}
"""

with open(PATH, encoding="utf-8") as f:
    html = f.read()

assert html.count("</style>") == 1, "plusieurs blocs style"
assert "Correctif titres slides 31-70" not in html, "correctif deja applique"
html = html.replace("</style>", CSS + "</style>")

with open(PATH, "w", encoding="utf-8", newline="\n") as f:
    f.write(html)

print("CSS correctif ajoute :", len(CSS), "caracteres")

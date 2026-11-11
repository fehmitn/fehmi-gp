# -*- coding: utf-8 -*-
"""Correctifs retour utilisateur :
- texte lisible (couleurs claires explicites) sur toutes les slides ss-*
- S43, S48, S63, S65 : image originale (crop) remplace les reconstructions CSS
- S59 : arbre original (crop) + donnees en def-items
"""
import re
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
PATH = r"C:\ppt\index.html"

CSS = r"""
/* ===== Correctifs lisibilite ===== */
.ss-tbl { color:#eef2ff; }
.ss-tbl th { color:#fff; }
.ss-tbl td:first-child { color:#fff; }
.ss-intro, .ss-note { color:#ecf0f1; font-size:1.45vw; }
.ss-glabel, .ss-chcap, .ss-tree .tbox, .ss-mini, .ss-node { color:#eef2ff; }
"""

SEC = {
    43: r"""
  <section class="slide slide43 t-rise" data-i="42" data-t="Ascension">
    <div class="ribbon anim"></div>
    <h2 class="anim">Plan de Charge (3)</h2>
    <div class="end-wrap anim d1" style="height:80%;">
      <div class="org-chart"><img src="assets/assets_ss_image13.png" alt="Charge et capacité par période"></div>
    </div>
  </section>
""",
    48: r"""
  <section class="slide slide48 t-zoom" data-i="47" data-t="Zoom">
    <div class="ribbon anim"></div>
    <h2 class="anim">Diagramme de Gantt</h2>
    <p class="ss-intro anim d1" style="margin-bottom:.4%;">Représentation des opérations et des ressources par des <b style="color:#f39c12;">bâtonnets proportionnels</b> au temps d'occupation de la ressource par une opération.</p>
    <div class="end-wrap anim d2" style="height:66%;">
      <div class="org-chart"><img src="assets/assets_ss_image18.png" alt="Diagramme de Gantt"></div>
    </div>
  </section>
""",
    59: r"""
  <section class="slide slide59 t-push" data-i="58" data-t="Poussée">
    <div class="ribbon anim"></div>
    <h2 class="anim">Calcul des Besoins (exemple)</h2>
    <div class="end-wrap anim d1" style="height:76%; gap:3%;">
      <div class="org-chart"><img src="assets/assets_ss_image29.png" alt="Nomenclature de la lunette"></div>
      <div style="flex:1; display:flex; flex-direction:column; gap:2.6%;">
        <div class="def-item anim d2"><div class="d-ico">⏱️</div><div class="d-txt">Délai d'assemblage : <b style="color:#f39c12;">1 période</b></div></div>
        <div class="def-item anim d3"><div class="d-ico">⏳</div><div class="d-txt">Délai de réalisation des branches : <b style="color:#f39c12;">2 périodes</b></div></div>
        <div class="def-item anim d4"><div class="d-ico">📦</div><div class="d-txt">Lot de production lunettes : <b style="color:#f39c12;">100</b></div></div>
        <div class="def-item anim d5"><div class="d-ico">📦</div><div class="d-txt">Lot de production branches : <b style="color:#f39c12;">200</b></div></div>
      </div>
    </div>
  </section>
""",
    63: r"""
  <section class="slide slide63 t-insert" data-i="62" data-t="Insertion">
    <div class="ribbon anim"></div>
    <h2 class="anim">Principe du MRP2</h2>
    <div class="end-wrap anim d1" style="height:78%;">
      <div class="org-chart"><img src="assets/assets_ss_image33.png" alt="Hiérarchie MRP2"></div>
    </div>
  </section>
""",
    65: r"""
  <section class="slide slide65 t-up" data-i="64" data-t="Verticale">
    <div class="ribbon anim"></div>
    <h2 class="anim">Cercles pervers</h2>
    <div class="end-wrap anim d1" style="height:78%;">
      <div class="org-chart"><img src="assets/assets_ss_image35.png" alt="Cercles pervers"></div>
    </div>
  </section>
""",
}

def main():
    with open(PATH, encoding="utf-8") as f:
        html = f.read()

    # 1) CSS lisibilite
    html = html.replace("</style>", CSS + "</style>")

    # 2) remplacement des sections
    for n, newsec in SEC.items():
        pat = re.compile(r'<section class="slide slide%d [\s\S]*?</section>' % n)
        m = pat.search(html)
        assert m, f"slide{n} introuvable"
        html = html[:m.start()] + newsec.strip() + html[m.end():]

    with open(PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(html)

    opens = len(re.findall(r'<section class="slide[^>]*>', html))
    closes = len(re.findall(r'</section>', html))
    print("sections :", opens, "/", closes)
    print("images ss :", html.count("assets_ss_image"))

if __name__ == "__main__":
    main()

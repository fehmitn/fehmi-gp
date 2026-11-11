# -*- coding: utf-8 -*-
"""Insertion des slides source 1-10 (slides 31-40 du diaporama) dans index.html.

Layouts reconstruits a la main depuis l'OCR (update/ocr_texts/slide_001..010.txt),
en respectant le design system existant (def-grid, roles/role-card, flow...).
Reecrire index.html empeche le fichier : avec re.search pour validation.
"""
import re
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

PATH = r"C:\ppt\index.html"
NEW = r"""
  <section class="slide slide31 t-rise" data-i="30" data-t="Ascension">
    <div class="particles">
      <span style="left:8%; animation-delay:0s;"></span><span style="left:18%; animation-delay:1s;"></span>
      <span style="left:30%; animation-delay:2s;"></span><span style="left:44%; animation-delay:3s;"></span>
      <span style="left:58%; animation-delay:4s;"></span><span style="left:70%; animation-delay:5s;"></span>
      <span style="left:82%; animation-delay:6s;"></span><span style="left:92%; animation-delay:7s;"></span>
    </div>
    <h2 class="anim" style="font-size:4.5vw;">Chapitre 2</h2>
    <h2 class="anim d2" style="font-size:4.5vw; font-weight:900;">Planification</h2>
    <div class="picto anim d3">📆</div>
  </section>

  <section class="slide slide32 t-zoom" data-i="31" data-t="Zoom">
    <div class="ribbon anim"></div>
    <h2 class="anim">Planifier</h2>
    <div class="def-grid">
      <div class="def-item anim d1"><div class="d-ico">🔄</div><div class="d-txt"><b style="color:#f39c12;">SYNCHRONISER</b> la fabrication des produits, l'arrivée des matières, l'arrivée des outillages et l'utilisation des ressources</div></div>
      <div class="def-item anim d2"><div class="d-ico">⚖️</div><div class="d-txt"><b style="color:#f39c12;">OPTIMISER</b> les dates de livraison, les stocks et l'utilisation des ressources</div></div>
      <div class="def-item wide anim d3" style="border-left-color:#e74c3c;"><div class="d-ico">⚡</div><div class="d-txt"><b style="color:#e74c3c;">RÉAGIR</b> en gérant les aléas (mode perturbé)</div></div>
    </div>
  </section>

  <section class="slide slide33 t-insert" data-i="32" data-t="Insertion">
    <div class="ribbon anim"></div>
    <h2 class="anim">6 niveaux de planification</h2>
    <div class="def-grid">
      <div class="def-item anim d1"><div class="d-ico">🏗️</div><div class="d-txt">Plan Industriel et Commercial (PIC)</div></div>
      <div class="def-item anim d2"><div class="d-ico">📆</div><div class="d-txt">Plan Directeur de Production (PDP)</div></div>
      <div class="def-item anim d3"><div class="d-ico">🧮</div><div class="d-txt">Calcul des Besoins Nets (CBN)</div></div>
      <div class="def-item anim d4"><div class="d-ico">📐</div><div class="d-txt">Plan de Charge</div></div>
      <div class="def-item anim d5"><div class="d-ico">⚙️</div><div class="d-txt">Ordonnancement</div></div>
      <div class="def-item anim d6"><div class="d-ico">🔍</div><div class="d-txt">Lancement / suivi de la fabrication</div></div>
    </div>
  </section>

  <section class="slide slide34 t-up" data-i="33" data-t="Verticale">
    <div class="ribbon anim"></div>
    <h2 class="anim">Plan Industriel et Commercial (PIC)</h2>
    <div class="roles">
      <div class="role-card blue anim d2">
        <div class="role-head">
          <div class="r-ico">🏗️</div>
          <h3>Plan à Long Terme (forte incertitude)</h3>
        </div>
        <ul>
          <li>Décisions au plus haut niveau hiérarchique</li>
          <li>Planification des <b style="color:#f39c12;">investissements</b> nécessaires</li>
          <li>Planification des financements</li>
        </ul>
        <div class="big-ico">🏗️</div>
      </div>
      <div class="role-card red anim d4">
        <div class="role-head">
          <div class="r-ico">⏱️</div>
          <h3>Paramètres</h3>
        </div>
        <ul>
          <li>Horizon : <b style="color:#e74c3c;">3 à 5 ans</b></li>
          <li>Période : <b style="color:#e74c3c;">1 an</b></li>
          <li>Finesse des données : famille de produits, usine</li>
        </ul>
        <div class="big-ico">⏱️</div>
      </div>
    </div>
  </section>

  <section class="slide slide35 t-push" data-i="34" data-t="Poussée">
    <div class="ribbon anim"></div>
    <h2 class="anim">Plan Industriel et Commercial (2)</h2>
    <div class="flow">
      <div class="flow-box anim d1">
        <div class="f-ico">🎯</div>
        <h3>ENTRÉES</h3>
        <ul><li>Objectifs stratégiques de l'entreprise</li><li>Tendances — développement du marché</li></ul>
      </div>
      <div class="flow-arrow anim d2">➜</div>
      <div class="flow-box anim d2" style="border-color:#f39c12; background:rgba(243,156,18,.15);">
        <div class="f-ico">🏢</div>
        <h3 style="color:#fff;">PIC</h3>
        <ul><li>Plan Industriel et Commercial</li></ul>
      </div>
      <div class="flow-arrow anim d3">➜</div>
      <div class="flow-box anim d3">
        <div class="f-ico">🚚</div>
        <h3 style="color:#e74c3c;">SORTIES</h3>
        <ul><li>Évolution des ventes</li><li>Évolution des productions</li><li>État du système de production</li><li>Investissements / Plans de financement</li></ul>
      </div>
    </div>
  </section>

  <section class="slide slide36 t-blur" data-i="35" data-t="Flou">
    <div class="ribbon anim"></div>
    <h2 class="anim">Plan Directeur de Production (PDP)</h2>
    <div class="roles">
      <div class="role-card blue anim d2">
        <div class="role-head">
          <div class="r-ico">📆</div>
          <h3>&laquo; Master Production Schedule &raquo;</h3>
        </div>
        <ul>
          <li>Lien entre <b style="color:#f39c12;">PIC</b> et plan de charge</li>
          <li>Définit la production à réaliser par période</li>
          <li>Définit les <b style="color:#f39c12;">approvisionnements critiques</b></li>
        </ul>
        <div class="big-ico">📆</div>
      </div>
      <div class="role-card red anim d4">
        <div class="role-head">
          <div class="r-ico">⏱️</div>
          <h3>Paramètres</h3>
        </div>
        <ul>
          <li>Horizon : <b style="color:#e74c3c;">1 à 2 ans</b> (supérieur au cycle appro. + cycle fab. + cycle livraison)</li>
          <li>Période : <b style="color:#e74c3c;">1 à 3 mois</b></li>
          <li>Finesse des données : produits, centres de charge</li>
        </ul>
        <div class="big-ico">⏱️</div>
      </div>
    </div>
  </section>

  <section class="slide slide37 t-rotate" data-i="36" data-t="Rotation">
    <div class="ribbon anim"></div>
    <h2 class="anim">Plan Directeur de Production (2)</h2>
    <div class="flow">
      <div class="flow-box anim d1">
        <div class="f-ico">📥</div>
        <h3>ENTRÉES</h3>
        <ul><li>Politique de production de l'entreprise</li><li>Prévisions commerciales et stocks</li><li>Capacités de production</li><li>Lots économiques</li></ul>
      </div>
      <div class="flow-arrow anim d2">➜</div>
      <div class="flow-box anim d2" style="border-color:#f39c12; background:rgba(243,156,18,.15);">
        <div class="f-ico">📆</div>
        <h3 style="color:#fff;">PDP</h3>
        <ul><li>Plan Directeur de Production</li></ul>
      </div>
      <div class="flow-arrow anim d3">➜</div>
      <div class="flow-box anim d3">
        <div class="f-ico">📤</div>
        <h3 style="color:#e74c3c;">SORTIES</h3>
        <ul><li>Production des produits par période</li><li>Approvisionnements critiques</li></ul>
      </div>
    </div>
  </section>

  <section class="slide slide38 t-zoom" data-i="37" data-t="Zoom">
    <div class="ribbon anim"></div>
    <h2 class="anim">Calcul des Besoins</h2>
    <div class="roles">
      <div class="role-card blue anim d2">
        <div class="role-head">
          <div class="r-ico">🧮</div>
          <h3>Principe de base du MRP (et MRP2)</h3>
        </div>
        <ul>
          <li>Définit les <b style="color:#f39c12;">dates et quantités</b> d'approvisionnement de tous les articles (<b style="color:#f39c12;">besoins dépendants</b>)</li>
          <li>pour couvrir les besoins en produits (<b style="color:#f39c12;">besoins indépendants</b>)</li>
        </ul>
        <div class="big-ico">🧮</div>
      </div>
      <div class="role-card red anim d4">
        <div class="role-head">
          <div class="r-ico">⏱️</div>
          <h3>Paramètres</h3>
        </div>
        <ul>
          <li>Horizon : <b style="color:#e74c3c;">1 à 3 mois</b></li>
          <li>Période : <b style="color:#e74c3c;">1 à 5 jours</b></li>
          <li>Finesse des données : articles, moyens de production</li>
        </ul>
        <div class="big-ico">⏱️</div>
      </div>
    </div>
  </section>

  <section class="slide slide39 t-insert" data-i="38" data-t="Insertion">
    <div class="ribbon anim"></div>
    <h2 class="anim">Calcul des Besoins (2)</h2>
    <div class="flow">
      <div class="flow-box anim d1">
        <div class="f-ico">📥</div>
        <h3>ENTRÉES</h3>
        <ul><li>Nomenclatures</li><li>Prévisions de production du produit fini et stocks d'articles</li><li>Lots économiques</li><li>Délais de production / livraison</li></ul>
      </div>
      <div class="flow-arrow anim d2">➜</div>
      <div class="flow-box anim d2" style="border-color:#f39c12; background:rgba(243,156,18,.15);">
        <div class="f-ico">🧮</div>
        <h3 style="color:#fff;">CBN</h3>
        <ul><li>Calcul des Besoins</li></ul>
      </div>
      <div class="flow-arrow anim d3">➜</div>
      <div class="flow-box anim d3">
        <div class="f-ico">📤</div>
        <h3 style="color:#e74c3c;">SORTIES</h3>
        <ul><li>Production des articles par période</li><li>Approvisionnements par période</li></ul>
      </div>
    </div>
  </section>

  <section class="slide slide40 t-up" data-i="39" data-t="Verticale">
    <div class="ribbon anim"></div>
    <h2 class="anim">Mécanisme du Calcul des Besoins</h2>
    <div class="def-grid">
      <div class="def-item wide anim d1"><div class="d-ico">🔽</div><div class="d-txt">Pour chaque <b style="color:#f39c12;">produit</b> — en descendant dans la nomenclature — puis pour chaque <b style="color:#f39c12;">article</b> :</div></div>
      <div class="def-item anim d2"><div class="d-ico">🧲</div><div class="d-txt">Regrouper les <b>Besoins Bruts</b> issus des différents produits</div></div>
      <div class="def-item anim d3"><div class="d-ico">➖</div><div class="d-txt"><b style="color:#f39c12;">Besoin Net (P) = Besoin Brut (P) − Stock (P−1)</b></div></div>
      <div class="def-item anim d4"><div class="d-ico">🗓️</div><div class="d-txt"><b style="color:#f39c12;">Début OF = Période du Besoin Net − Délai de production</b></div></div>
      <div class="def-item anim d5"><div class="d-ico">📦</div><div class="d-txt">Quantité à produire dépend des <b>lots de production</b></div></div>
    </div>
  </section>

"""

def main():
    with open(PATH, encoding="utf-8") as f:
        html = f.read()

    before = len(re.findall(r'<section class="slide', html))
    assert before == 30, f"attendu 30 slides, trouve {before}"

    # point d'insertion : la fin de la derniere slide (data-i="29"), avant </div> du conteneur
    m = re.search(r'(<section class="slide[^"]*" data-i="29"[\s\S]*?</section>)(\s*</div>)', html)
    if not m:
        m = re.search(r'(<section class="slide[\s\S]*?</section>)(\s*</div>\s*<div class="counter")', html)
    assert m, "point d'insertion introuvable"
    html = html[:m.end(1)] + NEW.rstrip("\n\n") + "\n" + html[m.start(2):]

    # compteur statique (le JS le recalcule, mais on garde la coherence)
    html = html.replace('<span id="tot">30</span>', '<span id="tot">40</span>')

    after = len(re.findall(r'<section class="slide', html))
    assert after == 40, f"attendu 40 slides apres insertion, trouve {after}"

    with open(PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(html)
    print(f"OK : 30 -> {after} slides ; ≤ data-i 39 ; compteur 40")


if __name__ == "__main__":
    main()

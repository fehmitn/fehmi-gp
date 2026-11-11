# -*- coding: utf-8 -*-
"""Batch 4 : slides source 71-100 -> slides 101-130 du diaporama.

Chapitre stocks (suite) : gestion des stocks (classification ABC, magasinage,
inventaires, couts), quantites economiques (formule de Wilson), rabais,
politiques de gestion (point de commande, recompletement), stock de securite.
2 images originales recardees : assets_ss_image84.png (courbes Wilson),
assets_ss_image94.png (graphique point de commande).
Nouveaux blocs CSS : .ss-fx (formules), .ss-saw (scie du stock 0->Q).
"""
import re
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

PATH = r"C:\ppt\index.html"

CSS = r"""
/* ===== Slides 101-130 (slideshare OCR) ===== */
.ss-fx { color:#eef2ff; background:rgba(255,255,255,.07); border:1px solid rgba(255,255,255,.2); border-left:4px solid #f39c12; border-radius:12px; padding:1.1% 2.2%; font-size:1.5vw; font-weight:700; width:max-content; max-width:92%; margin:.7% auto; }
.ss-fx b { color:#f39c12; }
.ss-saw { position:relative; width:76%; height:52%; margin:.6% auto; }
.ss-saw .saw-teeth { position:absolute; inset:0; display:flex; gap:1.4%; }
.ss-saw .saw-teeth i { flex:1; clip-path:polygon(0 0, 100% 100%, 0 100%); background:linear-gradient(180deg, rgba(243,156,18,.5), rgba(231,76,60,.16)); }
.ss-saw .saw-avg { position:absolute; left:0; right:0; top:50%; border-top:2px dashed #7cd0ff; }
.ss-saw .saw-lab { position:absolute; color:#eef2ff; font-weight:800; font-size:1.25vw; }
.ss-saw .saw-q { left:1.5%; top:-7%; color:#f39c12; }
.ss-saw .saw-m { right:0; top:36%; color:#7cd0ff; font-weight:700; font-size:1.05vw; }
.ss-saw .saw-0 { left:-.6%; bottom:-9%; }
.ss-saw .saw-t { right:0; bottom:-10%; color:rgba(255,255,255,.7); font-weight:600; }

/* ===== Correctif titres slides 101-130 ===== */
.slide101, .slide102, .slide103, .slide104, .slide105, .slide106, .slide107, .slide108, .slide109, .slide110,
.slide111, .slide112, .slide113, .slide114, .slide115, .slide116, .slide117, .slide118, .slide119, .slide120,
.slide121, .slide122, .slide123, .slide124, .slide125, .slide126, .slide127, .slide128, .slide129, .slide130 { flex-direction:column; }
.slide101 h2, .slide102 h2, .slide103 h2, .slide104 h2, .slide105 h2, .slide106 h2, .slide107 h2, .slide108 h2, .slide109 h2, .slide110 h2,
.slide111 h2, .slide112 h2, .slide113 h2, .slide114 h2, .slide115 h2, .slide116 h2, .slide117 h2, .slide118 h2, .slide119 h2, .slide120 h2,
.slide121 h2, .slide122 h2, .slide123 h2, .slide124 h2, .slide125 h2, .slide126 h2, .slide127 h2, .slide128 h2, .slide129 h2, .slide130 h2 {
  font-size:3vw; color:#fff; font-weight:700; margin-bottom:.5%;
  align-self:flex-start;
}
.slide101 .ribbon, .slide102 .ribbon, .slide103 .ribbon, .slide104 .ribbon, .slide105 .ribbon, .slide106 .ribbon, .slide107 .ribbon, .slide108 .ribbon, .slide109 .ribbon, .slide110 .ribbon,
.slide111 .ribbon, .slide112 .ribbon, .slide113 .ribbon, .slide114 .ribbon, .slide115 .ribbon, .slide116 .ribbon, .slide117 .ribbon, .slide118 .ribbon, .slide119 .ribbon, .slide120 .ribbon,
.slide121 .ribbon, .slide122 .ribbon, .slide123 .ribbon, .slide124 .ribbon, .slide125 .ribbon, .slide126 .ribbon, .slide127 .ribbon, .slide128 .ribbon, .slide129 .ribbon, .slide130 .ribbon {
  width:8%; height:5px; background:linear-gradient(90deg,#f39c12,#e74c3c);
  border-radius:5px; margin-bottom:3%; align-self:flex-start;
}
/* Slide 124 : contenu dense, on compacte pour eviter le debordement */
.slide124 .ss-intro { font-size:1.2vw; margin:.1% auto .3%; }
.slide124 .ss-img { height:57%; }
.slide124 .ss-img img { max-height:94%; }
.slide124 .ss-fx { font-size:1.3vw; padding:.7% 1.8%; margin-top:.3%; }
"""

NEW = r"""
  <section class="slide slide101 t-blur" data-i="100" data-t="Flou">
    <div class="ribbon anim"></div>
    <h2 class="anim">Augmenter les stocks&nbsp;?</h2>
    <div class="roles">
      <div class="role-card blue anim d2">
        <div class="role-head">
          <div class="r-ico">🎭</div>
          <h3>Ce que ça permet</h3>
        </div>
        <ul>
          <li><b style="color:#f39c12;">Masquer les problèmes de production</b></li>
        </ul>
        <div class="big-ico">🎭</div>
      </div>
      <div class="role-card red anim d4">
        <div class="role-head">
          <div class="r-ico">💸</div>
          <h3>Ce que ça coûte</h3>
        </div>
        <ul>
          <li><b style="color:#e74c3c;">Immobilise de l'argent</b> — l'argent en stock n'est pas en trésorerie</li>
        </ul>
        <div class="big-ico">💸</div>
      </div>
    </div>
    <p class="ss-note anim d5">🌪️ Les aléas masqués&nbsp;: <b style="color:#f39c12;">incertitude des prévisions</b> • <b style="color:#f39c12;">absences</b> • <b style="color:#f39c12;">procédés non maîtrisés</b> • <b style="color:#f39c12;">retards fournisseurs</b></p>
  </section>

  <section class="slide slide102 t-rotate" data-i="101" data-t="Rotation">
    <div class="ribbon anim"></div>
    <h2 class="anim">Classification des stocks</h2>
    <div class="roles">
      <div class="role-card blue anim d2">
        <div class="role-head">
          <div class="r-ico">🎯</div>
          <h3>Objectif</h3>
        </div>
        <ul>
          <li>Identifier les <b style="color:#f39c12;">articles à gérer avec plus d'attention</b></li>
        </ul>
        <div class="big-ico">🎯</div>
      </div>
      <div class="role-card red anim d4">
        <div class="role-head">
          <div class="r-ico">📊</div>
          <h3>Méthode ABC</h3>
        </div>
        <ul>
          <li>Aussi appelée <b style="color:#e74c3c;">"Loi de Pareto"</b> ou <b style="color:#e74c3c;">"loi des 80-20"</b></li>
        </ul>
        <div class="big-ico">📊</div>
      </div>
    </div>
    <p class="ss-note anim d5">📈 <b style="color:#f39c12;">20&nbsp;% des articles représentent 80&nbsp;% de la valeur</b> → classe A</p>
  </section>

  <section class="slide slide103 t-zoom" data-i="102" data-t="Zoom">
    <div class="ribbon anim"></div>
    <h2 class="anim">Classification des stocks (2) — méthodologie ABC</h2>
    <div class="ss-steps">
      <div class="ss-step anim d1"><span class="n">1</span>Calculer la consommation annuelle de chaque article (quantité)</div>
      <div class="ss-step anim d2"><span class="n">2</span>Calculer la valeur annuelle de cette consommation pour chaque article</div>
      <div class="ss-step anim d3"><span class="n">3</span>Classer les articles par ordre décroissant de leur valeur annuelle</div>
      <div class="ss-step anim d4"><span class="n">4</span>Calculer le pourcentage de chaque article et le pourcentage cumulé (ordre décroissant)</div>
      <div class="ss-step anim d5"><span class="n">5</span>Tracer la courbe</div>
    </div>
  </section>

  <section class="slide slide104 t-insert" data-i="103" data-t="Insertion">
    <div class="ribbon anim"></div>
    <h2 class="anim">Magasinage</h2>
    <div class="roles">
      <div class="role-card blue anim d2">
        <div class="role-head">
          <div class="r-ico">🏬</div>
          <h3>Gestion mono-magasin</h3>
        </div>
        <ul>
          <li><b style="color:#f39c12;">Simple</b> mais <b style="color:#e74c3c;">nombreuses manutentions</b></li>
        </ul>
        <div class="big-ico">🏬</div>
      </div>
      <div class="role-card red anim d4">
        <div class="role-head">
          <div class="r-ico">🏗️</div>
          <h3>Gestion multi-magasins</h3>
        </div>
        <ul>
          <li>Regroupement <b>par nature de produit</b> ou <b>par proximité géographique</b></li>
          <li><b style="color:#e74c3c;">Plus complexe à gérer</b></li>
        </ul>
        <div class="big-ico">🏗️</div>
      </div>
    </div>
    <p class="ss-note anim d5">📦 Pour un produit&nbsp;: gestion <b style="color:#f39c12;">mono-emplacement</b> ou <b style="color:#f39c12;">multi-emplacements</b></p>
  </section>

  <section class="slide slide105 t-rise" data-i="104" data-t="Ascension">
    <div class="ribbon anim"></div>
    <h2 class="anim">Opérations de gestion des stocks — entrées et sorties</h2>
    <div class="roles">
      <div class="role-card blue anim d2">
        <div class="role-head">
          <div class="r-ico">📥</div>
          <h3>Réception</h3>
        </div>
        <ul>
          <li>Vérification de la <b style="color:#f39c12;">conformité</b> des produits reçus</li>
          <li>Vérification de la <b style="color:#f39c12;">quantité</b> reçue</li>
          <li>Mise en place <b>à l'endroit défini</b></li>
        </ul>
        <div class="big-ico">📥</div>
      </div>
      <div class="role-card red anim d4">
        <div class="role-head">
          <div class="r-ico">📤</div>
          <h3>Délivrance</h3>
        </div>
        <ul>
          <li><b style="color:#e74c3c;">Sortie du stock</b> après commande client (produits finis) ou bons de sortie</li>
          <li>Vérification de la <b style="color:#e74c3c;">quantité délivrée</b> et de la <b style="color:#e74c3c;">référence</b> par rapport à la demande</li>
        </ul>
        <div class="big-ico">📤</div>
      </div>
    </div>
  </section>

  <section class="slide slide106 t-up" data-i="105" data-t="Verticale">
    <div class="ribbon anim"></div>
    <h2 class="anim">Opérations de gestion des stocks (3) — les inventaires</h2>
    <p class="ss-intro anim d1">L'inventaire permet de vérifier la <b style="color:#f39c12;">qualité des articles en stock</b> et de valider si le <b style="color:#f39c12;">stock réel = valeur informatique</b></p>
    <div class="def-grid">
      <div class="def-item anim d2"><div class="d-ico">🔄</div><div class="d-txt"><b style="color:#f39c12;">Inventaire permanent</b> — mise à jour permanente à chaque entrée / sortie</div></div>
      <div class="def-item anim d3"><div class="d-ico">📅</div><div class="d-txt"><b>Inventaire intermittent</b> — pour tous les articles de l'entreprise • au moins <b>une fois par an</b> (obligation comptable)</div></div>
      <div class="def-item anim d4" style="border-left-color:#e74c3c;"><div class="d-ico">🎯</div><div class="d-txt"><b style="color:#e74c3c;">Inventaire tournant</b> — pour un ensemble d'articles • la fréquence dépend de l'importance (classe A)</div></div>
    </div>
  </section>

  <section class="slide slide107 t-push" data-i="106" data-t="Poussée">
    <div class="ribbon anim"></div>
    <h2 class="anim">Valorisation des stocks</h2>
    <p class="ss-intro anim d1">Les coûts associés aux stocks sont de <b style="color:#f39c12;">différentes natures</b>&nbsp;:</p>
    <div class="def-grid">
      <div class="def-item anim d2"><div class="d-ico">🧾</div><div class="d-txt"><b style="color:#f39c12;">Coût d'acquisition</b></div></div>
      <div class="def-item anim d3"><div class="d-ico">🏢</div><div class="d-txt"><b>Coût de détention</b></div></div>
      <div class="def-item anim d4" style="border-left-color:#e74c3c;"><div class="d-ico">🚫</div><div class="d-txt"><b style="color:#e74c3c;">Coût de rupture</b></div></div>
    </div>
  </section>

  <section class="slide slide108 t-blur" data-i="107" data-t="Flou">
    <div class="ribbon anim"></div>
    <h2 class="anim">Coût d'acquisition</h2>
    <div class="roles">
      <div class="role-card blue anim d2">
        <div class="role-head">
          <div class="r-ico">🛒</div>
          <h3>Commande à l'extérieur</h3>
        </div>
        <ul>
          <li>Coût calculé <b style="color:#f39c12;">à la ligne de commande</b> (1 référence, 1 quantité, 1 prix, 1 délai)</li>
          <li>De <b style="color:#f39c12;">15 à plus de 150&nbsp;€</b> la ligne</li>
        </ul>
        <div class="big-ico">🛒</div>
      </div>
      <div class="role-card red anim d4">
        <div class="role-head">
          <div class="r-ico">🏭</div>
          <h3>Lancement d'un OF</h3>
        </div>
        <ul>
          <li>Un <b style="color:#e74c3c;">Ordre de Fabrication a un coût</b></li>
          <li>Dépend du <b style="color:#e74c3c;">temps de reconfiguration</b> et du <b style="color:#e74c3c;">coût administratif</b></li>
        </ul>
        <div class="big-ico">🏭</div>
      </div>
    </div>
  </section>

  <section class="slide slide109 t-rotate" data-i="108" data-t="Rotation">
    <div class="ribbon anim"></div>
    <h2 class="anim">Coût de possession</h2>
    <div class="def-grid">
      <div class="def-item anim d1"><div class="d-ico">🏢</div><div class="d-txt"><b style="color:#f39c12;">Structures d'accueil du stock</b> — loyer et entretien de l'entrepôt, électricité, manutention</div></div>
      <div class="def-item anim d2"><div class="d-ico">💰</div><div class="d-txt"><b>Argent immobilisé</b></div></div>
      <div class="def-item anim d3"><div class="d-ico">🧊</div><div class="d-txt"><b style="color:#f39c12;">Détérioration / obsolescence</b> des produits stockés</div></div>
      <div class="def-item anim d4" style="border-left-color:#e74c3c;"><div class="d-ico">🗂️</div><div class="d-txt"><b style="color:#e74c3c;">Frais généraux et frais de gestion</b> du stock</div></div>
    </div>
    <p class="ss-note anim d5">📈 Coût de possession <b style="color:#f39c12;">proportionnel à la valeur des stocks</b>&nbsp;: <b style="color:#f39c12;">25&nbsp;% à 40&nbsp;% par an</b></p>
  </section>

  <section class="slide slide110 t-zoom" data-i="109" data-t="Zoom">
    <div class="ribbon anim"></div>
    <h2 class="anim">Coût de rupture</h2>
    <div class="roles">
      <div class="role-card blue anim d2">
        <div class="role-head">
          <div class="r-ico">🚫</div>
          <h3>Une absence a un coût</h3>
        </div>
        <ul>
          <li>L'absence d'un article ou produit fini a un <b style="color:#f39c12;">coût</b></li>
          <li>La rupture n'est <b style="color:#f39c12;">pas tolérée</b> dans certains domaines (<b>santé, nucléaire…</b>)</li>
        </ul>
        <div class="big-ico">🚫</div>
      </div>
      <div class="role-card red anim d4">
        <div class="role-head">
          <div class="r-ico">📦</div>
          <h3>Pour un produit fini</h3>
        </div>
        <ul>
          <li><b style="color:#e74c3c;">Retard</b> sur produit (pénalités&nbsp;?)</li>
          <li><b style="color:#e74c3c;">Vente manquée</b>, <b style="color:#e74c3c;">client perdu&nbsp;?</b></li>
          <li><b style="color:#e74c3c;">Crédibilité perdue</b> → clients perdus</li>
          <li><b style="color:#e74c3c;">Arrêt de production</b></li>
        </ul>
        <div class="big-ico">📦</div>
      </div>
    </div>
  </section>

  <section class="slide slide111 t-insert" data-i="110" data-t="Insertion">
    <div class="ribbon anim"></div>
    <h2 class="anim">Quantités économiques</h2>
    <div class="roles">
      <div class="role-card blue anim d2">
        <div class="role-head">
          <div class="r-ico">🎯</div>
          <h3>Objectif</h3>
        </div>
        <ul>
          <li><b style="color:#f39c12;">Minimiser le coût du stock</b></li>
        </ul>
        <div class="big-ico">🎯</div>
      </div>
      <div class="role-card red anim d4">
        <div class="role-head">
          <div class="r-ico">⚖️</div>
          <h3>Une contradiction</h3>
        </div>
        <ul>
          <li><b>Commander peu mais souvent</b> — faible coût de possession, mais coût d'acquisition important</li>
          <li><b>Commander beaucoup mais rarement</b> — coût de possession important, mais faible coût d'acquisition</li>
          <li>Coût de possession et coût d'acquisition sont <b style="color:#e74c3c;">contradictoires</b></li>
        </ul>
        <div class="big-ico">⚖️</div>
      </div>
    </div>
  </section>

  <section class="slide slide112 t-rise" data-i="111" data-t="Ascension">
    <div class="ribbon anim"></div>
    <h2 class="anim">Formule de Wilson</h2>
    <div class="roles">
      <div class="role-card blue anim d2">
        <div class="role-head">
          <div class="r-ico">🎯</div>
          <h3>Objectif</h3>
        </div>
        <ul>
          <li>Trouver le <b style="color:#f39c12;">compromis</b> entre le coût d'acquisition et le coût de possession</li>
        </ul>
        <div class="big-ico">🎯</div>
      </div>
      <div class="role-card red anim d4">
        <div class="role-head">
          <div class="r-ico">📌</div>
          <h3>Hypothèses</h3>
        </div>
        <ul>
          <li>Coût d'acquisition <b style="color:#e74c3c;">proportionnel au nombre de commandes</b></li>
          <li>Coût de possession <b style="color:#e74c3c;">proportionnel au stock moyen</b></li>
          <li><b>Consommation continue</b> (proportionnelle au temps)</li>
          <li><b>Livraisons parfaitement planifiées</b></li>
        </ul>
        <div class="big-ico">📌</div>
      </div>
    </div>
  </section>

  <section class="slide slide113 t-up" data-i="112" data-t="Verticale">
    <div class="ribbon anim"></div>
    <h2 class="anim">Formule de Wilson (2) — évolution du stock</h2>
    <p class="ss-intro anim d1">Le stock évolue entre <b style="color:#f39c12;">0 et Q</b> (quantité reçue à chaque livraison)&nbsp;; le <b style="color:#f39c12;">stock moyen vaut Q/2</b></p>
    <div class="ss-saw anim d2">
      <div class="saw-teeth"><i></i><i></i><i></i><i></i><i></i><i></i></div>
      <div class="saw-avg"></div>
      <div class="saw-lab saw-q">Q</div>
      <div class="saw-lab saw-m">stock moyen = Q/2</div>
      <div class="saw-lab saw-0">0</div>
      <div class="saw-lab saw-t">temps →</div>
    </div>
  </section>

  <section class="slide slide114 t-push" data-i="113" data-t="Poussée">
    <div class="ribbon anim"></div>
    <h2 class="anim">Formule de Wilson (3) — graphiques</h2>
    <div class="ss-img anim d1"><img src="assets/assets_ss_image84.png" alt="Courbes de coûts — coût total minimal pour q* (quantité par commande) et n* (nombre annuel de commandes)"></div>
    <p class="ss-note anim d3">Le <b style="color:#f39c12;">coût total est minimal</b> à l'intersection du coût d'acquisition et du coût de détention&nbsp;: <b style="color:#f39c12;">q*</b> et <b style="color:#f39c12;">n*</b></p>
  </section>

  <section class="slide slide115 t-blur" data-i="114" data-t="Flou">
    <div class="ribbon anim"></div>
    <h2 class="anim">Formule de Wilson (4) — les variables</h2>
    <div class="def-grid">
      <div class="def-item anim d1"><div class="d-ico">📊</div><div class="d-txt"><b style="color:#f39c12;">S</b> — les besoins à satisfaire dans l'année</div></div>
      <div class="def-item anim d2"><div class="d-ico">🏷️</div><div class="d-txt"><b style="color:#f39c12;">U</b> — le prix unitaire de l'article</div></div>
      <div class="def-item anim d3"><div class="d-ico">📅</div><div class="d-txt"><b style="color:#f39c12;">T</b> — le taux de détention de l'article (0&nbsp;&lt;&nbsp;T&nbsp;&lt;&nbsp;1)</div></div>
      <div class="def-item anim d4"><div class="d-ico">🧾</div><div class="d-txt"><b style="color:#f39c12;">a</b> — le coût d'acquisition</div></div>
      <div class="def-item anim d5"><div class="d-ico">📦</div><div class="d-txt"><b style="color:#f39c12;">q</b> — la quantité par commande (q/2&nbsp;: le stock moyen)</div></div>
      <div class="def-item anim d6"><div class="d-ico">🔢</div><div class="d-txt"><b style="color:#f39c12;">n</b> — le nombre de commandes dans l'année (n&nbsp;=&nbsp;S/q)</div></div>
      <div class="def-item anim d7" style="border-left-color:#e74c3c;"><div class="d-ico">Σ</div><div class="d-txt"><b style="color:#e74c3c;">Z</b> — le coût total</div></div>
    </div>
  </section>

  <section class="slide slide116 t-rotate" data-i="115" data-t="Rotation">
    <div class="ribbon anim"></div>
    <h2 class="anim">Formule de Wilson (5) — optimisation du nombre de commandes</h2>
    <div class="ss-fx anim d1">Z = a·n + S·U·T / 2n</div>
    <p class="ss-intro anim d2">On <b style="color:#f39c12;">dérive par rapport à n</b> (nombre de commandes) — le minimum est atteint pour la <b style="color:#f39c12;">dérivée nulle</b>&nbsp;:</p>
    <div class="ss-fx anim d3">dZ/dn = a − S·U·T / (2n²) = 0</div>
    <div class="ss-fx anim d4" style="border-left-color:#e74c3c;"><b>n* = √( S·U·T / 2a )</b></div>
  </section>

  <section class="slide slide117 t-zoom" data-i="116" data-t="Zoom">
    <div class="ribbon anim"></div>
    <h2 class="anim">Formule de Wilson (6) — optimisation de la quantité à commander</h2>
    <div class="ss-fx anim d1">Z = a·S/q + q·U·T / 2</div>
    <p class="ss-intro anim d2">On <b style="color:#f39c12;">dérive par rapport à q</b> (quantité par commande) — le minimum est atteint pour la <b style="color:#f39c12;">dérivée nulle</b>&nbsp;:</p>
    <div class="ss-fx anim d3">dZ/dq = −a·S/q² + U·T / 2 = 0</div>
    <div class="ss-fx anim d4" style="border-left-color:#e74c3c;"><b>q* = √( 2a·S / U·T )</b></div>
  </section>

  <section class="slide slide118 t-insert" data-i="117" data-t="Insertion">
    <div class="ribbon anim"></div>
    <h2 class="anim">Formule de Wilson (7) — sensibilité</h2>
    <div class="def-grid">
      <div class="def-item anim d1" style="border-left-color:#e74c3c;"><div class="d-ico">⚠️</div><div class="d-txt"><b style="color:#e74c3c;">Hypothèses très restrictives</b> — les paramètres de coûts d'acquisition et de possession sont difficiles à obtenir</div></div>
      <div class="def-item anim d2"><div class="d-ico">🛡️</div><div class="d-txt"><b style="color:#f39c12;">Formule très robuste</b> — erreur du simple au double sur le coût d'acquisition&nbsp;: variation de <b>40&nbsp;% de q*</b> mais seulement <b>6&nbsp;% sur le coût total&nbsp;!</b></div></div>
      <div class="def-item anim d3"><div class="d-ico">🪄</div><div class="d-txt"><b>On peut arrondir les résultats</b> — erreur de 10&nbsp;% sur q*&nbsp;: <b style="color:#f39c12;">0,5&nbsp;% sur le coût total</b></div></div>
    </div>
  </section>

  <section class="slide slide119 t-rise" data-i="118" data-t="Ascension">
    <div class="ribbon anim"></div>
    <h2 class="anim">Quantités économiques avec remise</h2>
    <p class="ss-intro anim d1">Les fournisseurs proposent des <b style="color:#f39c12;">remises sur les prix</b> si les commandes sont réalisées en quantité importante</p>
    <div class="roles">
      <div class="role-card blue anim d2">
        <div class="role-head">
          <div class="r-ico">🏷️</div>
          <h3>Rabais uniformes</h3>
        </div>
        <ul>
          <li>Si la commande Q dépasse le seuil R, le prix unitaire de <b style="color:#f39c12;">tous</b> les produits commandés est diminué</li>
        </ul>
        <div class="big-ico">🏷️</div>
      </div>
      <div class="role-card red anim d4">
        <div class="role-head">
          <div class="r-ico">➕</div>
          <h3>Rabais incrémentaux</h3>
        </div>
        <ul>
          <li>Si la commande Q dépasse le seuil R, seul le prix unitaire des produits commandés <b style="color:#e74c3c;">au-dessus du seuil</b> est diminué</li>
        </ul>
        <div class="big-ico">➕</div>
      </div>
    </div>
  </section>

  <section class="slide slide120 t-up" data-i="119" data-t="Verticale">
    <div class="ribbon anim"></div>
    <h2 class="anim">Seuil de rabais unique (1)</h2>
    <div class="ss-steps">
      <div class="ss-step anim d1"><span class="n">1</span>Si Q&nbsp;&lt;&nbsp;R → le coût unitaire est <b style="color:#f39c12;">U1</b></div>
      <div class="ss-step anim d2"><span class="n">2</span>Si Q&nbsp;≥&nbsp;R → le coût unitaire est <b style="color:#f39c12;">U2</b> (U1&nbsp;&gt;&nbsp;U2)</div>
      <div class="ss-step anim d3"><span class="n">3</span>Calculer q1* avec U1 — si q1*&nbsp;&lt;&nbsp;R, calculer le coût (acquisition + possession + achat)</div>
      <div class="ss-step anim d4"><span class="n">4</span>Calculer q2* avec U2 — si q2*&nbsp;≥&nbsp;R, calculer le coût (acquisition + possession + achat)</div>
      <div class="ss-step anim d5"><span class="n">5</span>Calculer le coût avec q&nbsp;=&nbsp;R</div>
    </div>
  </section>

  <section class="slide slide121 t-push" data-i="120" data-t="Poussée">
    <div class="ribbon anim"></div>
    <h2 class="anim">Seuil de rabais unique (2)</h2>
    <div class="def-grid">
      <div class="def-item anim d1"><div class="d-ico">🎯</div><div class="d-txt"><b style="color:#f39c12;">L'optimum est une des trois solutions</b></div></div>
      <div class="def-item anim d2"><div class="d-ico">⚖️</div><div class="d-txt">On <b>compare le coût</b> dans les 3 cas et on choisit la <b style="color:#f39c12;">solution admissible</b> ayant le <b style="color:#f39c12;">coût le plus faible</b></div></div>
    </div>
  </section>

  <section class="slide slide122 t-blur" data-i="121" data-t="Flou">
    <div class="ribbon anim"></div>
    <h2 class="anim">Seuil de rabais unique (3) — exemple</h2>
    <div class="def-grid">
      <div class="def-item anim d1"><div class="d-ico">📋</div><div class="d-txt"><b style="color:#f39c12;">Données</b> — 100 unités dans l'année • taux de possession 25&nbsp;% • coût de passation 50&nbsp;€ • U1&nbsp;=&nbsp;100&nbsp;€ (moins de 50 produits), U2&nbsp;=&nbsp;81&nbsp;€ (plus de 50 produits)</div></div>
      <div class="def-item anim d2"><div class="d-ico">1️⃣</div><div class="d-txt"><b>q1*&nbsp;=&nbsp;20</b> (&lt;&nbsp;50 → admissible)&nbsp;; CT(q1*)&nbsp;=&nbsp;<b style="color:#f39c12;">10&nbsp;500&nbsp;€</b></div></div>
      <div class="def-item anim d3" style="border-left-color:#e74c3c;"><div class="d-ico">2️⃣</div><div class="d-txt"><b style="color:#e74c3c;">q2*&nbsp;=&nbsp;22</b> (&lt;&nbsp;50 → <b style="color:#e74c3c;">pas admissible&nbsp;!</b>)</div></div>
      <div class="def-item anim d4"><div class="d-ico">🏆</div><div class="d-txt">CT(R)&nbsp;=&nbsp;<b style="color:#f39c12;">8&nbsp;706&nbsp;€</b> → l'optimum est des <b>commandes de 50 produits</b> (R)</div></div>
    </div>
  </section>

  <section class="slide slide123 t-rotate" data-i="122" data-t="Rotation">
    <div class="ribbon anim"></div>
    <h2 class="anim">Politiques de gestion des stocks</h2>
    <p class="ss-intro anim d1"><b style="color:#f39c12;">Quand commander&nbsp;?</b> • <b style="color:#f39c12;">Combien commander&nbsp;?</b></p>
    <table class="ss-tbl anim d2" style="width:80%;">
      <tr><th></th><th>Période fixe</th><th>Période variable</th></tr>
      <tr><th style="text-align:left;">Quantité fixe</th><td>méthode de <b style="color:#f39c12;">réapprovisionnement</b></td><td>méthode à <b style="color:#f39c12;">point de commande</b></td></tr>
      <tr class="alt"><th style="text-align:left;">Quantité variable</th><td>méthode de <b style="color:#f39c12;">recomplètement</b></td><td>méthode à <b style="color:#f39c12;">période et quantité variable</b></td></tr>
    </table>
    <p class="ss-note anim d4">⚠️ Si la <b style="color:#e74c3c;">périodicité et la quantité sont fixes</b>, on <b style="color:#e74c3c;">ne s'adapte pas aux variations&nbsp;!</b></p>
  </section>

  <section class="slide slide124 t-zoom" data-i="123" data-t="Zoom">
    <div class="ribbon anim"></div>
    <h2 class="anim">Méthode à point de commande</h2>
    <p class="ss-intro anim d1"><b style="color:#f39c12;">Quantité fixe, période variable</b> — la commande est passée lorsque le stock atteint le <b style="color:#f39c12;">point de commande</b> (seuil de déclenchement)</p>
    <div class="ss-img anim d2"><img src="assets/assets_ss_image94.png" alt="Stock en dents de scie — commande passée au point de commande Pc, livraison après le délai D, quantité Q"></div>
    <div class="ss-fx anim d3"><b>Pc = Délai de livraison × consommation</b></div>
  </section>

  <section class="slide slide125 t-insert" data-i="124" data-t="Insertion">
    <div class="ribbon anim"></div>
    <h2 class="anim">Méthode de recomplètement</h2>
    <div class="roles">
      <div class="role-card blue anim d2">
        <div class="role-head">
          <div class="r-ico">📆</div>
          <h3>Principe</h3>
        </div>
        <ul>
          <li><b style="color:#f39c12;">Période fixe, quantité variable</b></li>
          <li>La quantité Q<sub>i</sub> commandée doit être <b style="color:#f39c12;">suffisante pour atteindre le niveau de recomplètement</b></li>
        </ul>
        <div class="big-ico">📆</div>
      </div>
      <div class="role-card red anim d4">
        <div class="role-head">
          <div class="r-ico">🧮</div>
          <h3>Formule</h3>
        </div>
        <ul>
          <li><b style="color:#e74c3c; font-size:1.35vw;">Q<sub>i</sub> = R − q<sub>i</sub> + Délai de livraison × conso</b></li>
        </ul>
        <div class="big-ico">🧮</div>
      </div>
    </div>
  </section>

  <section class="slide slide126 t-rise" data-i="125" data-t="Ascension">
    <div class="ribbon anim"></div>
    <h2 class="anim">Comparaison entre les 2 méthodes</h2>
    <div class="roles">
      <div class="role-card blue anim d2">
        <div class="role-head">
          <div class="r-ico">🎯</div>
          <h3>Point de commande</h3>
        </div>
        <ul>
          <li><b style="color:#f39c12;">Suivi précis du stock</b></li>
          <li>Demande à <b style="color:#f39c12;">forte variabilité</b></li>
          <li><b style="color:#f39c12;">Articles importants</b> (pas de rupture&nbsp;!)</li>
          <li>Réapprovisionnement <b>fiable et rapide</b></li>
        </ul>
        <div class="big-ico">🎯</div>
      </div>
      <div class="role-card red anim d4">
        <div class="role-head">
          <div class="r-ico">📆</div>
          <h3>Recomplètement</h3>
        </div>
        <ul>
          <li>Demande et <b style="color:#e74c3c;">délais d'obtention constants</b></li>
          <li>Articles à <b style="color:#e74c3c;">coût de détention faible</b></li>
          <li><b style="color:#e74c3c;">"Aveugle" entre 2 périodes&nbsp;!</b></li>
        </ul>
        <div class="big-ico">📆</div>
      </div>
    </div>
  </section>

  <section class="slide slide127 t-up" data-i="126" data-t="Verticale">
    <div class="ribbon anim"></div>
    <h2 class="anim">Aléas et stock de sécurité</h2>
    <div class="roles">
      <div class="role-card blue anim d2">
        <div class="role-head">
          <div class="r-ico">🌪️</div>
          <h3>Les aléas</h3>
        </div>
        <ul>
          <li><b style="color:#f39c12;">Consommation excessive</b></li>
          <li><b style="color:#f39c12;">Retards de livraisons</b></li>
          <li><b style="color:#f39c12;">Problèmes de qualité</b></li>
        </ul>
        <div class="big-ico">🌪️</div>
      </div>
      <div class="role-card red anim d4">
        <div class="role-head">
          <div class="r-ico">⚖️</div>
          <h3>Une contradiction, un objectif</h3>
        </div>
        <ul>
          <li><b style="color:#e74c3c;">Éviter les ruptures</b> et avoir un stock de sécurité <b style="color:#e74c3c;">faible</b></li>
          <li>Définir un <b>niveau de stock de sécurité</b> (stock dormant)</li>
          <li><b>Compromis</b> coût de rupture / coût de possession</li>
        </ul>
        <div class="big-ico">⚖️</div>
      </div>
    </div>
  </section>

  <section class="slide slide128 t-push" data-i="127" data-t="Poussée">
    <div class="ribbon anim"></div>
    <h2 class="anim">Calcul du stock de sécurité</h2>
    <div class="roles">
      <div class="role-card blue anim d2">
        <div class="role-head">
          <div class="r-ico">📌</div>
          <h3>Hypothèses</h3>
        </div>
        <ul>
          <li>La demande suit une <b style="color:#f39c12;">loi normale</b> (variable)</li>
          <li>Le <b style="color:#f39c12;">taux de service</b> à atteindre est connu</li>
          <li>Le <b style="color:#f39c12;">délai de consommation</b> entraînant un risque de rupture est fixe</li>
        </ul>
        <div class="big-ico">📌</div>
      </div>
      <div class="role-card red anim d4">
        <div class="role-head">
          <div class="r-ico">📆</div>
          <h3>D&nbsp;: période soumise au risque</h3>
        </div>
        <ul>
          <li>D = <b style="color:#e74c3c;">délai de livraison</b> en point de commande</li>
          <li>D = <b style="color:#e74c3c;">période de recomplètement + délai de livraison</b></li>
        </ul>
        <div class="big-ico">📆</div>
      </div>
    </div>
    <div class="ss-fx anim d5"><b>Stock sécurité = k × σ × √D</b></div>
  </section>

  <section class="slide slide129 t-blur" data-i="128" data-t="Flou">
    <div class="ribbon anim"></div>
    <h2 class="anim">K en fonction du taux de service</h2>
    <p class="ss-intro anim d1">K est obtenu par une <b style="color:#f39c12;">loi normale centrée réduite</b></p>
    <table class="ss-tbl anim d2" style="width:46%;">
      <tr><th>Taux de service</th><th>k</th></tr>
      <tr><td>90&nbsp;%</td><td class="c">1,28</td></tr>
      <tr class="alt"><td>95&nbsp;%</td><td class="c" style="color:#f39c12; font-weight:900;">1,65</td></tr>
      <tr><td>99&nbsp;%</td><td class="c">2,23</td></tr>
    </table>
  </section>

  <section class="slide slide130 t-rotate" data-i="129" data-t="Rotation">
    <div class="ribbon anim"></div>
    <h2 class="anim">Exemple de calcul de stock de sécurité</h2>
    <div class="def-grid">
      <div class="def-item anim d1"><div class="d-ico">📋</div><div class="d-txt"><b style="color:#f39c12;">Données</b> — demande&nbsp;: loi normale, 100 pièces/semaine (σ&nbsp;=&nbsp;20) • délai d'obtention fixe&nbsp;: 5 semaines • période de révision&nbsp;: 10 semaines • probabilité de rupture souhaitée &lt;&nbsp;5&nbsp;%</div></div>
      <div class="def-item anim d2"><div class="d-ico">🧮</div><div class="d-txt"><b>Calcul</b> — SS&nbsp;=&nbsp;1,65&nbsp;×&nbsp;20&nbsp;×&nbsp;√15&nbsp;=&nbsp;<b style="color:#f39c12;">128 pièces</b></div></div>
      <div class="def-item anim d3" style="border-left-color:#e74c3c;"><div class="d-ico">🎯</div><div class="d-txt"><b style="color:#e74c3c;">Niveau de recomplètement</b> — 1500&nbsp;+&nbsp;128&nbsp;=&nbsp;<b style="color:#f39c12;">1628 pièces</b></div></div>
    </div>
    <p class="ss-note anim d4">💡 15&nbsp;= 10&nbsp;+&nbsp;5 (révision + délai) et 1500&nbsp;= 100&nbsp;×&nbsp;15</p>
  </section>
"""

def main():
    with open(PATH, encoding="utf-8") as f:
        html = f.read()

    before = len(re.findall(r'<section class="slide', html))
    assert before == 100, f"attendu 100 slides, trouve {before}"

    # 1) CSS
    assert html.count("</style>") == 1
    html = html.replace("</style>", CSS + "</style>")

    # 2) insertion des slides apres la derniere (data-i="99")
    m = re.search(r'(<section class="slide[^"]*" data-i="99"[\s\S]*?</section>)(\s*</div>)', html)
    assert m, "point d'insertion introuvable"
    html = html[:m.end(1)] + NEW.rstrip("\n\n") + "\n" + html[m.start(2):]

    # 3) compteur statique
    html = html.replace('<span id="tot">100</span>', '<span id="tot">130</span>')

    after = len(re.findall(r'<section class="slide', html))
    assert after == 130, f"attendu 130 slides apres insertion, trouve {after}"

    with open(PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(html)
    print(f"OK : 100 -> {after} slides ; compteur 130")

if __name__ == "__main__":
    main()

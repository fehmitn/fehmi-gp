# -*- coding: utf-8 -*-
"""Batch 5 : slides source 101-140 -> slides 131-170 du diaporama.

Chapitre stocks (fin) : valorisation (CMUP, FIFO, LIFO), conclusion.
Chapitre Previsions : objectifs, types, evolutions courantes (constante,
tendance, saisonniere, saut), series chronologiques (moyenne mobile,
lissage exponentiel, regression), exemples, conclusion.
Chapitre Kanban : historique, principe (flux tire), fonctionnement,
calcul du nombre de Kanbans, conditions, consequences, conclusion.
Chapitre Juste a Temps : objectifs (les zeros), moyens, rationalisation
de l'implantation.
Images originales recardees : 109, 110, 114a/b, 115a/b, 119, 121, 126,
128, 129, 139 + formules : fx_mm_odd, fx_mm_even, fx_liss_exp,
fx_reg_a, fx_reg_b.
3 intercalaires rouges : 136 (Previsions), 153 (Kanban), 166 (JAT).
"""
import re
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

PATH = r"C:\ppt\index.html"

CSS = r"""
/* ===== Slides 131-170 (slideshare OCR) ===== */
/* Intercalaires rouges 136/153/166 */
.slide136, .slide153, .slide166 { background:linear-gradient(135deg,#e74c3c 0%,#c0392b 55%,#8e2418 100%); flex-direction:column; }
.slide136 h2, .slide153 h2, .slide166 h2 { color:#fff; align-self:flex-start; font-weight:900; margin-bottom:0; }
/* ===== Correctif titres slides 131-170 ===== */
.slide131, .slide132, .slide133, .slide134, .slide135, .slide136, .slide137, .slide138, .slide139, .slide140,
.slide141, .slide142, .slide143, .slide144, .slide145, .slide146, .slide147, .slide148, .slide149, .slide150,
.slide151, .slide152, .slide153, .slide154, .slide155, .slide156, .slide157, .slide158, .slide159, .slide160,
.slide161, .slide162, .slide163, .slide164, .slide165, .slide166, .slide167, .slide168, .slide169, .slide170 { flex-direction:column; }
.slide131 h2, .slide132 h2, .slide133 h2, .slide134 h2, .slide135 h2, .slide137 h2, .slide138 h2, .slide139 h2, .slide140 h2,
.slide141 h2, .slide142 h2, .slide143 h2, .slide144 h2, .slide145 h2, .slide146 h2, .slide147 h2, .slide148 h2, .slide149 h2, .slide150 h2,
.slide151 h2, .slide152 h2, .slide154 h2, .slide155 h2, .slide156 h2, .slide157 h2, .slide158 h2, .slide159 h2, .slide160 h2,
.slide161 h2, .slide162 h2, .slide163 h2, .slide164 h2, .slide165 h2, .slide167 h2, .slide168 h2, .slide169 h2, .slide170 h2 {
  font-size:3vw; color:#fff; font-weight:700; margin-bottom:.5%;
  align-self:flex-start;
}
.slide131 .ribbon, .slide132 .ribbon, .slide133 .ribbon, .slide134 .ribbon, .slide135 .ribbon, .slide137 .ribbon, .slide138 .ribbon, .slide139 .ribbon, .slide140 .ribbon,
.slide141 .ribbon, .slide142 .ribbon, .slide143 .ribbon, .slide144 .ribbon, .slide145 .ribbon, .slide146 .ribbon, .slide147 .ribbon, .slide148 .ribbon, .slide149 .ribbon, .slide150 .ribbon,
.slide151 .ribbon, .slide152 .ribbon, .slide154 .ribbon, .slide155 .ribbon, .slide156 .ribbon, .slide157 .ribbon, .slide158 .ribbon, .slide159 .ribbon, .slide160 .ribbon,
.slide161 .ribbon, .slide162 .ribbon, .slide163 .ribbon, .slide164 .ribbon, .slide165 .ribbon, .slide167 .ribbon, .slide168 .ribbon, .slide169 .ribbon, .slide170 .ribbon {
  width:8%; height:5px; background:linear-gradient(90deg,#f39c12,#e74c3c);
  border-radius:5px; margin-bottom:3%; align-self:flex-start;
}
/* Formule unique tres large (slide 147) */
.fx-single { display:flex; align-items:center; justify-content:center; width:100%; height:50%; margin-top:1%; }
.fx-single img { max-width:82%; max-height:100%; border-radius:10px; background:rgba(255,255,255,.95); padding:.8%; box-shadow:0 8px 24px rgba(0,0,0,.35); }
"""

NEW = r"""
  <section class="slide slide131 t-zoom" data-i="130" data-t="Zoom">
    <div class="ribbon anim"></div>
    <h2 class="anim">Valorisation du stock</h2>
    <div class="roles">
      <div class="role-card blue anim d2">
        <div class="role-head">
          <div class="r-ico">🎯</div>
          <h3>Objectif</h3>
        </div>
        <ul>
          <li>Pour la <b style="color:#f39c12;">comptabilité générale</b> (légale)</li>
          <li>Pour identifier les <b style="color:#f39c12;">coûts de production</b> (comptabilité analytique)</li>
        </ul>
        <div class="big-ico">🎯</div>
      </div>
      <div class="role-card red anim d4">
        <div class="role-head">
          <div class="r-ico">📉</div>
          <h3>Pourquoi&nbsp;? Les prix varient</h3>
        </div>
        <ul>
          <li>Entre la <b style="color:#e74c3c;">commande</b> et la <b style="color:#e74c3c;">livraison</b></li>
          <li>Entre l'<b style="color:#e74c3c;">entrée en magasin</b> et l'utilisation en production</li>
          <li>Suivant l'<b style="color:#e74c3c;">avancement de fabrication</b></li>
        </ul>
        <div class="big-ico">📉</div>
      </div>
    </div>
  </section>

  <section class="slide slide132 t-insert" data-i="131" data-t="Insertion">
    <div class="ribbon anim"></div>
    <h2 class="anim">Méthodes de valorisation</h2>
    <p class="ss-intro anim d1">Les <b style="color:#f39c12;">méthodes classiques</b>&nbsp;:</p>
    <div class="def-grid">
      <div class="def-item anim d2"><div class="d-ico">🧮</div><div class="d-txt"><b style="color:#f39c12;">CMUP</b> — Coût Moyen Unitaire Pondéré</div></div>
      <div class="def-item anim d3"><div class="d-ico">📥</div><div class="d-txt"><b>FIFO</b> — First In First Out</div></div>
      <div class="def-item anim d4"><div class="d-ico">📤</div><div class="d-txt"><b style="color:#f39c12;">LIFO</b> — Last In First Out</div></div>
    </div>
    <div class="ss-fx anim d5"><b>CMUP = Σ p<sub>i</sub>·q<sub>i</sub> / Σ q<sub>i</sub></b></div>
    <p class="ss-note anim d6">⏳ CMUP <b>calculé par période</b> → il faut attendre la fin de la période pour valoriser les sorties (<b style="color:#f39c12;">pas en temps réel</b>)</p>
  </section>

  <section class="slide slide133 t-rise" data-i="132" data-t="Ascension">
    <div class="ribbon anim"></div>
    <h2 class="anim">Méthodes de valorisation (2) — FIFO</h2>
    <p class="ss-intro anim d1">Livraisons par lots&nbsp;: les sorties sont valorisées au prix d'achat du lot <b style="color:#f39c12;">arrivé en premier</b> tant qu'il en reste (épuisement des lots), puis au prix du lot suivant</p>
    <table class="ss-tbl anim d2" style="width:62%;">
      <tr><th>Date</th><th>Mouvement</th></tr>
      <tr><td>01/02</td><td>Entrée&nbsp;: <b style="color:#f39c12;">200 à 50&nbsp;€</b></td></tr>
      <tr class="alt"><td>06/02</td><td>Sortie&nbsp;: 120 à 50&nbsp;€</td></tr>
      <tr><td>11/02</td><td>Entrée&nbsp;: <b style="color:#f39c12;">150 à 52&nbsp;€</b></td></tr>
      <tr class="alt"><td>15/02</td><td>Sortie&nbsp;: 170 = <b>80 à 50&nbsp;€ + 90 à 52&nbsp;€</b></td></tr>
    </table>
    <p class="ss-note anim d4">➡️ Arrivé en premier → sorti en premier</p>
  </section>

  <section class="slide slide134 t-up" data-i="133" data-t="Verticale">
    <div class="ribbon anim"></div>
    <h2 class="anim">Méthodes de valorisation (2) — LIFO</h2>
    <p class="ss-intro anim d1">Livraisons par lots&nbsp;: les sorties sont valorisées au prix d'achat du lot <b style="color:#f39c12;">arrivé en dernier</b> tant qu'il en reste (épuisement des lots), puis au prix du lot suivant</p>
    <table class="ss-tbl anim d2" style="width:62%;">
      <tr><th>Date</th><th>Mouvement</th></tr>
      <tr><td>01/02</td><td>Entrée&nbsp;: <b style="color:#f39c12;">200 à 50&nbsp;€</b></td></tr>
      <tr class="alt"><td>06/02</td><td>Sortie&nbsp;: 120 à 50&nbsp;€</td></tr>
      <tr><td>11/02</td><td>Entrée&nbsp;: <b style="color:#f39c12;">150 à 52&nbsp;€</b></td></tr>
      <tr class="alt"><td>15/02</td><td>Sortie&nbsp;: 170 = <b>150 à 52&nbsp;€ + 20 à 50&nbsp;€</b></td></tr>
    </table>
    <p class="ss-note anim d4">➡️ Arrivé en dernier → sorti en premier</p>
  </section>

  <section class="slide slide135 t-push" data-i="134" data-t="Poussée">
    <div class="ribbon anim"></div>
    <h2 class="anim">Conclusion sur la gestion des stocks</h2>
    <div class="def-grid">
      <div class="def-item anim d1"><div class="d-ico">🧩</div><div class="d-txt"><b style="color:#f39c12;">Besoins indépendants</b> — la gestion des stocks s'applique aux besoins indépendants</div></div>
      <div class="def-item anim d2"><div class="d-ico">💰</div><div class="d-txt"><b>Les stocks doivent être limités</b> — pour laisser de la trésorerie à l'entreprise</div></div>
      <div class="def-item anim d3"><div class="d-ico">📐</div><div class="d-txt"><b style="color:#f39c12;">Formule de Wilson</b> — définit les quantités économiques d'achat et de production&nbsp;; hypothèses strictes mais <b>résultats robustes</b></div></div>
      <div class="def-item anim d4" style="border-left-color:#e74c3c;"><div class="d-ico">🕸️</div><div class="d-txt"><b style="color:#e74c3c;">Méthodes potentiellement très complexes</b> — quel coût de gestion&nbsp;?</div></div>
    </div>
  </section>

  <section class="slide slide136 t-blur" data-i="135" data-t="Flou">
    <div class="particles">
      <span style="left:8%; animation-delay:0s;"></span><span style="left:18%; animation-delay:1s;"></span>
      <span style="left:30%; animation-delay:2s;"></span><span style="left:44%; animation-delay:3s;"></span>
      <span style="left:58%; animation-delay:4s;"></span><span style="left:70%; animation-delay:5s;"></span>
      <span style="left:82%; animation-delay:6s;"></span><span style="left:92%; animation-delay:7s;"></span>
    </div>
    <h2 class="anim" style="font-size:4.5vw;">Chapitre 4</h2>
    <h2 class="anim d2" style="font-size:4.5vw; font-weight:900;">Prévisions</h2>
    <div class="picto anim d3">🔮</div>
  </section>

  <section class="slide slide137 t-rotate" data-i="136" data-t="Rotation">
    <div class="ribbon anim"></div>
    <h2 class="anim">Prévisions — objectif</h2>
    <div class="roles">
      <div class="role-card blue anim d2">
        <div class="role-head">
          <div class="r-ico">🔮</div>
          <h3>Estimer les événements futurs</h3>
        </div>
        <ul>
          <li>Permettre une <b style="color:#f39c12;">estimation des événements futurs</b></li>
        </ul>
        <div class="big-ico">🔮</div>
      </div>
      <div class="role-card red anim d4">
        <div class="role-head">
          <div class="r-ico">🏭</div>
          <h3>En production</h3>
        </div>
        <ul>
          <li>Prévisions commerciales (<b style="color:#f39c12;">PIC ou PDP</b>)</li>
          <li>Évolutions du <b style="color:#e74c3c;">marché</b> et des <b style="color:#e74c3c;">parts de marché</b></li>
          <li>Évolutions de la <b style="color:#e74c3c;">charge</b></li>
          <li>Évolutions des <b style="color:#e74c3c;">coûts</b></li>
        </ul>
        <div class="big-ico">🏭</div>
      </div>
    </div>
  </section>

  <section class="slide slide138 t-zoom" data-i="137" data-t="Zoom">
    <div class="ribbon anim"></div>
    <h2 class="anim">Types de prévisions</h2>
    <div class="def-grid">
      <div class="def-item anim d1"><div class="d-ico">🔭</div><div class="d-txt"><b style="color:#f39c12;">Horizon</b> — long terme • moyen terme • court terme</div></div>
      <div class="def-item anim d2"><div class="d-ico">🔍</div><div class="d-txt"><b>Précision</b> — macro-économie → entreprise → famille de produits → produit</div></div>
      <div class="def-item anim d3"><div class="d-ico">🧰</div><div class="d-txt"><b style="color:#f39c12;">Technique</b> — qualitative ou quantitative</div></div>
    </div>
  </section>

  <section class="slide slide139 t-insert" data-i="138" data-t="Insertion">
    <div class="ribbon anim"></div>
    <h2 class="anim">Prévisions et objectifs</h2>
    <p class="ss-intro anim d1">La prévision de l'évolution du marché doit permettre de définir un <b style="color:#f39c12;">objectif en termes de part</b> et un <b style="color:#f39c12;">objectif quantitatif</b></p>
    <div class="ss-img anim d2"><img src="assets/assets_ss_image109.png" alt="Prévisionnel, réalisation et écarts — objectif quantitatif, part de marché réalisée, écarts de marché et de part"></div>
  </section>

  <section class="slide slide140 t-rise" data-i="139" data-t="Ascension">
    <div class="ribbon anim"></div>
    <h2 class="anim">Prévisions et objectifs (2) — exemple</h2>
    <div class="ss-img anim d1"><img src="assets/assets_ss_image110.png" alt="Exemple — marché prévu 200, réalisé 180 (écart −20) ; part visée 25 %, réalisée 30 % ; objectif quantitatif 50, réalisé 54"></div>
    <p class="ss-note anim d3">📊 Marché prévu 200 → réalisé 180 (<b style="color:#f39c12;">écart −20, −10&nbsp;%</b>) • part visée 25&nbsp;% → réalisée 30&nbsp;% • objectif quantitatif 50 → réalisé 54 (<b style="color:#f39c12;">+4, +8&nbsp;% en relatif</b>)</p>
  </section>

  <section class="slide slide141 t-up" data-i="140" data-t="Verticale">
    <div class="ribbon anim"></div>
    <h2 class="anim">Qui prévoit&nbsp;?</h2>
    <table class="ss-tbl anim d1" style="width:88%;">
      <tr><th></th><th>Avantage</th><th>Inconvénient</th></tr>
      <tr><th style="text-align:left;">Homme de terrain<br><span style="font-weight:400; opacity:.8;">(vendeur, représentant…)</span></th>
          <td>Connaissance du marché, des produits • intéressé directement par les prévisions</td>
          <td>Confusion <b style="color:#f39c12;">prévision / objectif</b> • prévisions influencées par le dernier client et/ou l'optimisme</td></tr>
      <tr class="alt"><th style="text-align:left;">Scientifique<br><span style="font-weight:400; opacity:.8;">(approche statistique)</span></th>
          <td>Méthodes quantitatives • informatisation des méthodes</td>
          <td>Méconnaissance du marché, des produits, des clients, des concurrents…</td></tr>
    </table>
    <p class="ss-note anim d3">🤝 Nécessité d'une <b style="color:#f39c12;">coopération entre les 2 approches&nbsp;!</b></p>
  </section>

  <section class="slide slide142 t-push" data-i="141" data-t="Poussée">
    <div class="ribbon anim"></div>
    <h2 class="anim">Méthode de prévision</h2>
    <div class="ss-steps">
      <div class="ss-step anim d1"><span class="n">1</span>Acquisition des données (externes et internes)</div>
      <div class="ss-step anim d2"><span class="n">2</span>Représentation des données</div>
      <div class="ss-step anim d3"><span class="n">3</span>Identification par rapport à un modèle</div>
      <div class="ss-step anim d4"><span class="n">4</span>Extrapolation</div>
      <div class="ss-step anim d5"><span class="n">5</span>Correction et adaptation par le décideur</div>
      <div class="ss-step anim d6"><span class="n">6</span>Mesure des écarts entre la prévision et la réalité</div>
      <div class="ss-step anim d7"><span class="n">7</span>Correction du modèle</div>
    </div>
  </section>

  <section class="slide slide143 t-blur" data-i="142" data-t="Flou">
    <div class="ribbon anim"></div>
    <h2 class="anim">Données initiales</h2>
    <div class="roles">
      <div class="role-card blue anim d2">
        <div class="role-head">
          <div class="r-ico">🗄️</div>
          <h3>Historique — contraintes</h3>
        </div>
        <ul>
          <li>Valeurs <b style="color:#f39c12;">fiables et réelles</b></li>
          <li><b style="color:#f39c12;">Homogènes</b> dans le temps, avec le niveau de granularité adapté à la prévision</li>
          <li><b>Nombre suffisant</b> de valeurs sur une période suffisante (saisonnalité&nbsp;?)</li>
        </ul>
        <div class="big-ico">🗄️</div>
      </div>
      <div class="role-card red anim d4">
        <div class="role-head">
          <div class="r-ico">🧹</div>
          <h3>Traitement des données</h3>
        </div>
        <ul>
          <li><b style="color:#e74c3c;">Filtrage</b> pour laisser apparaître les tendances</li>
          <li><b style="color:#e74c3c;">Représentation graphique</b> (analyse humaine)</li>
        </ul>
        <div class="big-ico">🧹</div>
      </div>
    </div>
  </section>

  <section class="slide slide144 t-rotate" data-i="143" data-t="Rotation">
    <div class="ribbon anim"></div>
    <h2 class="anim">Évolutions courantes — constante et tendance</h2>
    <div class="fx-imgs anim d1" style="height:56%;">
      <div style="display:flex; flex-direction:column; align-items:center; height:100%;">
        <img src="assets/assets_ss_image114a.png" alt="Évolution constante — prévision faite pour le mois suivant" style="max-width:100%; max-height:78%;">
        <div style="font-size:1.25vw; font-weight:700; color:#f39c12; margin-top:1%;">Constante</div>
      </div>
      <div style="display:flex; flex-direction:column; align-items:center; height:100%;">
        <img src="assets/assets_ss_image114b.png" alt="Évolution à tendance — prévision pour le mois suivant" style="max-width:100%; max-height:78%;">
        <div style="font-size:1.25vw; font-weight:700; color:#f39c12; margin-top:1%;">Tendance</div>
      </div>
    </div>
  </section>

  <section class="slide slide145 t-zoom" data-i="144" data-t="Zoom">
    <div class="ribbon anim"></div>
    <h2 class="anim">Évolutions courantes (2) — saisonnière et saut</h2>
    <div class="fx-imgs anim d1" style="height:56%;">
      <div style="display:flex; flex-direction:column; align-items:center; height:100%;">
        <img src="assets/assets_ss_image115a.png" alt="Évolution saisonnière — prévision faite pour le mois suivant" style="max-width:100%; max-height:78%;">
        <div style="font-size:1.25vw; font-weight:700; color:#f39c12; margin-top:1%;">Saisonnière</div>
      </div>
      <div style="display:flex; flex-direction:column; align-items:center; height:100%;">
        <img src="assets/assets_ss_image115b.png" alt="Évolution à saut — le saut" style="max-width:100%; max-height:78%;">
        <div style="font-size:1.25vw; font-weight:700; color:#f39c12; margin-top:1%;">Saut</div>
      </div>
    </div>
    <p class="ss-note anim d3">🔀 Les phénomènes peuvent <b style="color:#f39c12;">se combiner</b></p>
  </section>

  <section class="slide slide146 t-insert" data-i="145" data-t="Insertion">
    <div class="ribbon anim"></div>
    <h2 class="anim">Analyse de séries chronologiques — la moyenne mobile</h2>
    <p class="ss-intro anim d1">Évolution constante et lissage&nbsp;: faire la <b style="color:#f39c12;">moyenne sur les m derniers échantillons</b> et affecter la valeur à l'échantillon du <b style="color:#f39c12;">milieu</b></p>
    <div class="fx-imgs anim d2" style="height:40%;">
      <img src="assets/assets_ss_fx_mm_odd.png" alt="Moyenne mobile d'ordre impair (2m+1 valeurs)">
      <img src="assets/assets_ss_fx_mm_even.png" alt="Moyenne mobile d'ordre pair">
    </div>
  </section>

  <section class="slide slide147 t-rise" data-i="146" data-t="Ascension">
    <div class="ribbon anim"></div>
    <h2 class="anim">Analyse de séries chronologiques (2) — lissage exponentiel</h2>
    <p class="ss-intro anim d1">Donner un <b style="color:#f39c12;">poids particulier aux informations récentes</b> (plus proches du point estimé)</p>
    <div class="fx-single anim d2"><img src="assets/assets_ss_fx_liss_exp.png" alt="Formule du lissage exponentiel avec coefficient α"></div>
  </section>

  <section class="slide slide148 t-up" data-i="147" data-t="Verticale">
    <div class="ribbon anim"></div>
    <h2 class="anim">Analyse de séries chronologiques (3) — tendance linéaire</h2>
    <p class="ss-intro anim d1">La tendance peut être <b style="color:#f39c12;">linéaire, exponentielle, puissance…</b> — linéaire&nbsp;: on estime les paramètres de la droite <b>y&nbsp;=&nbsp;ax&nbsp;+&nbsp;b</b>&nbsp;; la qualité est exprimée par le <b style="color:#f39c12;">coefficient de corrélation r</b></p>
    <div class="fx-imgs anim d2" style="height:44%;">
      <img src="assets/assets_ss_fx_reg_a.png" alt="Régression linéaire — formules de a et b">
      <img src="assets/assets_ss_fx_reg_b.png" alt="Formule du coefficient de corrélation r">
    </div>
  </section>

  <section class="slide slide149 t-push" data-i="148" data-t="Poussée">
    <div class="ribbon anim"></div>
    <h2 class="anim">Exemple de prévision par tendance</h2>
    <div class="ss-img anim d1"><img src="assets/assets_ss_image119.png" alt="Exemple — consommation réelle et consommation estimée"></div>
  </section>

  <section class="slide slide150 t-blur" data-i="149" data-t="Flou">
    <div class="ribbon anim"></div>
    <h2 class="anim">Analyse de séries chronologiques (4) — évolution saisonnière</h2>
    <p class="ss-intro anim d1">La valeur estimée = valeur estimée avec la <b style="color:#f39c12;">tendance</b> (droite de régression) + valeur de <b style="color:#f39c12;">saisonnalité</b></p>
    <div class="ss-steps">
      <div class="ss-step anim d2"><span class="n">1</span>Filtrer la saisonnalité</div>
      <div class="ss-step anim d3"><span class="n">2</span>Calculer les valeurs estimées avec tendance</div>
      <div class="ss-step anim d4"><span class="n">3</span><span>Calculer les écarts entre valeurs réelles et estimées&nbsp;; pour une même période (février par exemple), calculer la <b>moyenne des écarts</b> (valeurs de saisonnalité)</span></div>
      <div class="ss-step anim d5"><span class="n">4</span><span>La <b style="color:#f39c12;">somme des écarts de saisonnalité doit être nulle</b> (répartition de l'écart)</span></div>
    </div>
  </section>

  <section class="slide slide151 t-rotate" data-i="150" data-t="Rotation">
    <div class="ribbon anim"></div>
    <h2 class="anim">Exemple de prévision saisonnière</h2>
    <div class="ss-img anim d1"><img src="assets/assets_ss_image121.png" alt="Exemple — consommation réelle et consommation estimée (saisonnalité)"></div>
  </section>

  <section class="slide slide152 t-zoom" data-i="151" data-t="Zoom">
    <div class="ribbon anim"></div>
    <h2 class="anim">Conclusion sur les prévisions</h2>
    <div class="def-grid">
      <div class="def-item anim d1"><div class="d-ico">🧭</div><div class="d-txt"><b style="color:#f39c12;">Indispensables</b> en gestion de production</div></div>
      <div class="def-item anim d2"><div class="d-ico">🧪</div><div class="d-txt">Doivent être menées avec <b>prudence et méthode</b></div></div>
      <div class="def-item anim d3" style="border-left-color:#e74c3c;"><div class="d-ico">⚠️</div><div class="d-txt"><b style="color:#e74c3c;">Horizon lointain = plus d'incertitude&nbsp;!</b></div></div>
    </div>
  </section>

  <section class="slide slide153 t-insert" data-i="152" data-t="Insertion">
    <div class="particles">
      <span style="left:8%; animation-delay:0s;"></span><span style="left:18%; animation-delay:1s;"></span>
      <span style="left:30%; animation-delay:2s;"></span><span style="left:44%; animation-delay:3s;"></span>
      <span style="left:58%; animation-delay:4s;"></span><span style="left:70%; animation-delay:5s;"></span>
      <span style="left:82%; animation-delay:6s;"></span><span style="left:92%; animation-delay:7s;"></span>
    </div>
    <h2 class="anim" style="font-size:4.5vw;">Chapitre 5</h2>
    <h2 class="anim d2" style="font-size:4.5vw; font-weight:900;">Kanban</h2>
    <div class="picto anim d3">🏷️</div>
  </section>

  <section class="slide slide154 t-rise" data-i="153" data-t="Ascension">
    <div class="ribbon anim"></div>
    <h2 class="anim">Kanban — historique et objectifs</h2>
    <div class="roles">
      <div class="role-card blue anim d2">
        <div class="role-head">
          <div class="r-ico">📜</div>
          <h3>Historique</h3>
        </div>
        <ul>
          <li><b style="color:#f39c12;">1958</b>&nbsp;: implantation du Kanban chez <b style="color:#f39c12;">Toyota</b> (Japon)</li>
          <li>"Kanban" = <b>étiquette</b> en japonais</li>
          <li>Constat&nbsp;: les entreprises avaient tendance à faire de la <b style="color:#e74c3c;">surproduction</b></li>
        </ul>
        <div class="big-ico">📜</div>
      </div>
      <div class="role-card red anim d4">
        <div class="role-head">
          <div class="r-ico">🎯</div>
          <h3>Objectifs</h3>
        </div>
        <ul>
          <li>Produire le <b style="color:#f39c12;">produit demandé</b></li>
          <li>À la <b style="color:#f39c12;">date demandée</b></li>
          <li>En <b style="color:#f39c12;">quantité demandée</b></li>
        </ul>
        <div class="big-ico">🎯</div>
      </div>
    </div>
  </section>

  <section class="slide slide155 t-up" data-i="154" data-t="Verticale">
    <div class="ribbon anim"></div>
    <h2 class="anim">Kanban — principe&nbsp;: le flux tiré</h2>
    <div class="roles">
      <div class="role-card blue anim d2">
        <div class="role-head">
          <div class="r-ico">🔗</div>
          <h3>Le principe</h3>
        </div>
        <ul>
          <li>La <b style="color:#f39c12;">commande du client = demande au poste final</b></li>
          <li>Les composants sont <b>produits et acheminés</b> vers le poste final, assemblés et livrés (flux physique)</li>
        </ul>
        <div class="big-ico">🔗</div>
      </div>
      <div class="role-card red anim d4">
        <div class="role-head">
          <div class="r-ico">🧲</div>
          <h3>Flux tiré — pas flux poussé</h3>
        </div>
        <ul>
          <li>Le moyen de production <b style="color:#e74c3c;">appelle</b> les composants aux moyens situés <b style="color:#e74c3c;">en amont</b> = producteur</li>
          <li><b>Notion de flux tiré</b> (par opposition au flux <b style="color:#e74c3c;">poussé en MRP</b>)</li>
        </ul>
        <div class="big-ico">🧲</div>
      </div>
    </div>
  </section>

  <section class="slide slide156 t-push" data-i="155" data-t="Poussée">
    <div class="ribbon anim"></div>
    <h2 class="anim">Kanban — principe (2)</h2>
    <div class="ss-img anim d1"><img src="assets/assets_ss_image126.png" alt="Schéma du flux tiré — appels composants de poste en poste jusqu'à la commande client"></div>
  </section>

  <section class="slide slide157 t-blur" data-i="156" data-t="Flou">
    <div class="ribbon anim"></div>
    <h2 class="anim">Kanban — fonctionnement</h2>
    <div class="ss-steps">
      <div class="ss-step anim d1"><span class="n">1</span><span>Le <b style="color:#f39c12;">poste 2</b> consomme les pièces produites par le <b style="color:#f39c12;">poste 1</b></span></div>
      <div class="ss-step anim d2"><span class="n">2</span><span>Quand le poste 2 reçoit un container de pièces, l'opérateur <b style="color:#f39c12;">détache l'étiquette (Kanban)</b> et la renvoie au poste 1</span></div>
      <div class="ss-step anim d3"><span class="n">3</span><span>Quand le poste 1 a des <b style="color:#f39c12;">étiquettes</b> correspondant à un produit, il peut les réaliser et les envoyer au poste concerné</span></div>
    </div>
    <p class="ss-note anim d4">🏷️ L'étiquette indique&nbsp;: <b style="color:#f39c12;">machine productrice</b> • <b style="color:#f39c12;">machine utilisatrice</b> • <b style="color:#f39c12;">type de produit</b> • <b style="color:#f39c12;">capacité du container</b></p>
  </section>

  <section class="slide slide158 t-rotate" data-i="157" data-t="Rotation">
    <div class="ribbon anim"></div>
    <h2 class="anim">Kanban — fonctionnement (2)</h2>
    <div class="ss-img anim d1"><img src="assets/assets_ss_image128.png" alt="Schéma du fonctionnement — étiquettes, tableaux des postes et flux physique"></div>
  </section>

  <section class="slide slide159 t-zoom" data-i="158" data-t="Zoom">
    <div class="ribbon anim"></div>
    <h2 class="anim">Kanban — fonctionnement (3)</h2>
    <div class="ss-img anim d1"><img src="assets/assets_ss_image129.png" alt="Schéma du fonctionnement — 5 Kanbans entre les postes 2 et 3"></div>
  </section>

  <section class="slide slide160 t-insert" data-i="159" data-t="Insertion">
    <div class="ribbon anim"></div>
    <h2 class="anim">Calcul du nombre de Kanbans</h2>
    <div class="ss-steps">
      <div class="ss-step anim d1"><span class="n">1</span><span>Combien de <b style="color:#f39c12;">produits par container</b>&nbsp;?</span></div>
      <div class="ss-step anim d2"><span class="n">2</span><span>Combien de <b style="color:#f39c12;">containers</b>&nbsp;? (nb containers = nb Kanbans)</span></div>
      <div class="ss-step anim d3"><span class="n">3</span><span>Nb produits = <b style="color:#f39c12;">taille de lot</b> (production ou transfert)</span></div>
    </div>
    <p class="ss-note anim d4">⚖️ Contraintes&nbsp;: trop de pièces par container → <b style="color:#e74c3c;">encours importants</b> • trop peu → <b style="color:#e74c3c;">trop de reconfigurations</b></p>
  </section>

  <section class="slide slide161 t-rise" data-i="160" data-t="Ascension">
    <div class="ribbon anim"></div>
    <h2 class="anim">Calcul du nombre de Kanbans (2)</h2>
    <p class="ss-intro anim d1">Le nombre de Kanbans doit être défini puis <b style="color:#f39c12;">progressivement diminué</b> pour limiter l'encours</p>
    <div class="ss-fx anim d2"><b>n = ( D × L + G ) / C</b></div>
    <div class="def-grid">
      <div class="def-item anim d3"><div class="d-ico">📦</div><div class="d-txt"><b style="color:#f39c12;">D</b> — demande moyenne de pièces (par heure)</div></div>
      <div class="def-item anim d4"><div class="d-ico">⏱️</div><div class="d-txt"><b style="color:#f39c12;">L</b> — délai (en heures) de mise à disposition d'un container</div></div>
      <div class="def-item anim d5"><div class="d-ico">🧺</div><div class="d-txt"><b style="color:#f39c12;">C</b> — capacité d'un container</div></div>
      <div class="def-item anim d6" style="border-left-color:#e74c3c;"><div class="d-ico">🛡️</div><div class="d-txt"><b style="color:#e74c3c;">G</b> — stock de sécurité pour l'intégration des aléas</div></div>
    </div>
  </section>

  <section class="slide slide162 t-up" data-i="161" data-t="Verticale">
    <div class="ribbon anim"></div>
    <h2 class="anim">Calcul du nombre de Kanbans (3) — application</h2>
    <div class="def-grid">
      <div class="def-item anim d1"><div class="d-ico">📦</div><div class="d-txt"><b style="color:#f39c12;">D</b> — 500 pièces / heure</div></div>
      <div class="def-item anim d2"><div class="d-ico">⏱️</div><div class="d-txt"><b style="color:#f39c12;">L</b> — 30 minutes</div></div>
      <div class="def-item anim d3"><div class="d-ico">🧺</div><div class="d-txt"><b style="color:#f39c12;">C</b> — 50 pièces</div></div>
      <div class="def-item anim d4"><div class="d-ico">🛡️</div><div class="d-txt"><b style="color:#f39c12;">G</b> — 20 pièces</div></div>
    </div>
    <div class="ss-fx anim d5" style="font-size:1.8vw;"><b>n = (500 × 0,5 + 20) / 50 = <span style="color:#f39c12;">6 Kanbans</span> (= 6 containers)</b></div>
  </section>

  <section class="slide slide163 t-push" data-i="162" data-t="Poussée">
    <div class="ribbon anim"></div>
    <h2 class="anim">Kanban — conditions nécessaires</h2>
    <div class="def-grid">
      <div class="def-item anim d1"><div class="d-ico">📊</div><div class="d-txt"><b style="color:#f39c12;">Demande stable</b> (PDP lissé&nbsp;?)</div></div>
      <div class="def-item anim d2"><div class="d-ico">🏝️</div><div class="d-txt"><b style="color:#f39c12;">Flux simples</b> (îlots)</div></div>
      <div class="def-item anim d3"><div class="d-ico">⚡</div><div class="d-txt"><b style="color:#f39c12;">Temps de reconfiguration courts</b> (SMED&nbsp;?)</div></div>
      <div class="def-item anim d4"><div class="d-ico">🔧</div><div class="d-txt"><b style="color:#f39c12;">Pannes limitées</b> (maintenance préventive)</div></div>
      <div class="def-item anim d5"><div class="d-ico">🙋</div><div class="d-txt"><b style="color:#f39c12;">Personnel responsable</b></div></div>
      <div class="def-item anim d6"><div class="d-ico">🤝</div><div class="d-txt"><b style="color:#f39c12;">Partenariat avec les fournisseurs</b></div></div>
    </div>
  </section>

  <section class="slide slide164 t-blur" data-i="163" data-t="Flou">
    <div class="ribbon anim"></div>
    <h2 class="anim">Kanban — conséquences</h2>
    <div class="def-grid">
      <div class="def-item anim d1"><div class="d-ico">🏷️</div><div class="d-txt"><b style="color:#f39c12;">Étiquette (Kanban) = Ordre de Fabrication</b></div></div>
      <div class="def-item anim d2"><div class="d-ico">🔢</div><div class="d-txt"><b>Nombre de Kanbans limité</b> — soit sur un container de pièces réalisées, soit sur le tableau des pièces à réaliser</div></div>
      <div class="def-item anim d3" style="border-left-color:#e74c3c;"><div class="d-ico">🛑</div><div class="d-txt"><b style="color:#e74c3c;">Pas de Kanban sur le tableau d'un poste → le poste ne travaille pas&nbsp;!</b> Ce temps peut être utilisé pour l'<b style="color:#f39c12;">amélioration du poste</b></div></div>
    </div>
  </section>

  <section class="slide slide165 t-rotate" data-i="164" data-t="Rotation">
    <div class="ribbon anim"></div>
    <h2 class="anim">Conclusion sur le Kanban</h2>
    <div class="def-grid">
      <div class="def-item anim d1"><div class="d-ico">🎯</div><div class="d-txt"><b style="color:#f39c12;">Kanban adapté</b> pour une production <b>régulière d'une famille de produits</b> avec une production maîtrisée</div></div>
      <div class="def-item anim d2"><div class="d-ico">🤝</div><div class="d-txt"><b style="color:#f39c12;">Cohabitation MRP / Kanban possible</b> — pièces standards réalisées avec MRP et assemblage personnalisé (configuration)</div></div>
    </div>
  </section>

  <section class="slide slide166 t-zoom" data-i="165" data-t="Zoom">
    <div class="particles">
      <span style="left:8%; animation-delay:0s;"></span><span style="left:18%; animation-delay:1s;"></span>
      <span style="left:30%; animation-delay:2s;"></span><span style="left:44%; animation-delay:3s;"></span>
      <span style="left:58%; animation-delay:4s;"></span><span style="left:70%; animation-delay:5s;"></span>
      <span style="left:82%; animation-delay:6s;"></span><span style="left:92%; animation-delay:7s;"></span>
    </div>
    <h2 class="anim" style="font-size:4.5vw;">Chapitre 6</h2>
    <h2 class="anim d2" style="font-size:4.5vw; font-weight:900;">Juste à Temps</h2>
    <div class="picto anim d3">⏱️</div>
  </section>

  <section class="slide slide167 t-insert" data-i="166" data-t="Insertion">
    <div class="ribbon anim"></div>
    <h2 class="anim">Juste à Temps — objectifs</h2>
    <div class="roles">
      <div class="role-card blue anim d2">
        <div class="role-head">
          <div class="r-ico">📜</div>
          <h3>Historique &amp; principe</h3>
        </div>
        <ul>
          <li>Moyens développés chez <b style="color:#f39c12;">Toyota</b> (Japon)</li>
          <li>Produire <b style="color:#f39c12;">ce qui est nécessaire, quand c'est nécessaire</b></li>
        </ul>
        <div class="big-ico">📜</div>
      </div>
      <div class="role-card red anim d4">
        <div class="role-head">
          <div class="r-ico">0️⃣</div>
          <h3>Objectifs — les zéros</h3>
        </div>
        <ul>
          <li><b style="color:#e74c3c;">Zéro défaut, zéro délai, zéro stock, zéro papier, zéro panne</b> (+ zéro accident)</li>
          <li>Démarche d'<b style="color:#f39c12;">amélioration continue</b></li>
        </ul>
        <div class="big-ico">0️⃣</div>
      </div>
    </div>
  </section>

  <section class="slide slide168 t-rise" data-i="167" data-t="Ascension">
    <div class="ribbon anim"></div>
    <h2 class="anim">Juste à Temps — les moyens</h2>
    <div class="def-grid">
      <div class="def-item anim d1"><div class="d-ico">🗺️</div><div class="d-txt"><b style="color:#f39c12;">Rationalisation de l'implantation</b> des ressources de production</div></div>
      <div class="def-item anim d2"><div class="d-ico">⚡</div><div class="d-txt"><b style="color:#f39c12;">Diminution des temps de reconfiguration</b> (SMED)</div></div>
      <div class="def-item anim d3"><div class="d-ico">🔧</div><div class="d-txt"><b style="color:#f39c12;">Amélioration de la disponibilité</b> des ressources techniques (maintenance)</div></div>
      <div class="def-item anim d4"><div class="d-ico">🚚</div><div class="d-txt"><b style="color:#f39c12;">Amélioration des approvisionnements</b> (relations avec les fournisseurs)</div></div>
    </div>
  </section>

  <section class="slide slide169 t-up" data-i="168" data-t="Verticale">
    <div class="ribbon anim"></div>
    <h2 class="anim">Rationalisation de l'implantation des ressources</h2>
    <div class="ss-img anim d1"><img src="assets/assets_ss_image139.png" alt="Du job-shop (sections homogènes) vers les îlots — stock matières premières, implantation"></div>
    <p class="ss-note anim d3">Domaine&nbsp;: en <b style="color:#f39c12;">job-shop</b>, modification de l'implantation — de <b>sections homogènes</b> vers les <b style="color:#f39c12;">îlots</b></p>
  </section>

  <section class="slide slide170 t-push" data-i="169" data-t="Poussée">
    <div class="ribbon anim"></div>
    <h2 class="anim">Rationalisation de l'implantation (2) — démarche</h2>
    <div class="ss-steps">
      <div class="ss-step anim d1"><span class="n">1</span><span>Identification des <b style="color:#f39c12;">gammes de fabrication</b> (attention aux différences entre gamme théorique et gamme réelle)</span></div>
      <div class="ss-step anim d2"><span class="n">2</span><span><b style="color:#f39c12;">Regroupement des gammes similaires</b> pour créer des familles de produits (production similaire)</span></div>
      <div class="ss-step anim d3"><span class="n">3</span><span>Identification des <b style="color:#f39c12;">contraintes</b> (RT impossibles à déplacer, arrivées de fluides…)</span></div>
      <div class="ss-step anim d4"><span class="n">4</span><span>Définition de la <b style="color:#f39c12;">nouvelle implantation</b></span></div>
      <div class="ss-step anim d5"><span class="n">5</span><span>Planification des <b style="color:#f39c12;">déplacements</b> puis déplacement physique des RT</span></div>
    </div>
  </section>
"""

def main():
    with open(PATH, encoding="utf-8") as f:
        html = f.read()

    before = len(re.findall(r'<section class="slide', html))
    assert before == 130, f"attendu 130 slides, trouve {before}"

    # 1) CSS
    assert html.count("</style>") == 1
    html = html.replace("</style>", CSS + "</style>")

    # 2) insertion des slides apres la derniere (data-i="129")
    m = re.search(r'(<section class="slide[^"]*" data-i="129"[\s\S]*?</section>)(\s*</div>)', html)
    assert m, "point d'insertion introuvable"
    html = html[:m.end(1)] + NEW.rstrip("\n\n") + "\n" + html[m.start(2):]

    # 3) compteur statique
    html = html.replace('<span id="tot">130</span>', '<span id="tot">170</span>')

    after = len(re.findall(r'<section class="slide', html))
    assert after == 170, f"attendu 170 slides apres insertion, trouve {after}"

    with open(PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(html)
    print(f"OK : 130 -> {after} slides ; compteur 170")

if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""Batch 2 : slides source 11-40 -> slides 41-70 du diaporama.

Reconstructions HTML/CSS pur (aucune image embarquee) :
tables (PDP INT56, Calcul des Besoins), arbre nomenclature (lunettes),
Gantt CSS, graphiques charge/capacite CSS, chaines MRP2 et cercles pervers.
"""
import re
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

PATH = r"C:\ppt\index.html"

CSS = r"""
/* ===== Slides 41-70 (slideshare OCR) ===== */
.slide31, .slide50, .slide69 { background:linear-gradient(135deg,#e74c3c 0%,#c0392b 55%,#8e2418 100%); flex-direction:column; }
.ss-diag { display:flex; flex-direction:column; align-items:center; width:100%; }
.ss-topin { display:flex; align-items:center; gap:2%; margin-bottom:.4%; }
.ss-mini { background:rgba(255,255,255,.1); border:1px solid rgba(255,255,255,.22); border-radius:12px; padding:.6% 1.4%; font-size:1.25vw; font-weight:600; }
.ss-down { color:#f39c12; font-weight:900; font-size:1.7vw; animation:pulseArrow 2s infinite; }
.ss-chart { position:relative; display:flex; align-items:flex-end; gap:1.2%;
  width:68%; height:46%; margin:1.5% auto .5%;
  border-left:2px solid rgba(255,255,255,.35); border-bottom:2px solid rgba(255,255,255,.35); padding:0 2%; }
.ss-bar { flex:1; border-radius:5px 5px 0 0; background:linear-gradient(180deg,#54a8f2,#2f7fd6); }
.ss-bar.ov { background:linear-gradient(180deg,#7cd0ff,#3fa2ff); }
.ss-capline { position:absolute; left:0; right:0; border-top:2px dashed #f39c12; opacity:.9; }
.ss-caplab { position:absolute; right:.5%; transform:translateY(-115%); background:rgba(243,156,18,.92); color:#16130a; font-weight:800; font-size:.95vw; padding:.15% .7%; border-radius:8px; white-space:nowrap; }
.ss-chcap { position:absolute; top:-5.5%; left:.2%; font-size:1.25vw; font-weight:700; }
.ss-pcap { display:flex; justify-content:flex-end; width:68%; margin:0 auto; font-size:1.2vw; color:#f39c12; font-weight:600; }
.ss-2ch { display:flex; justify-content:center; gap:4%; width:100%; margin-top:1%; }
.ss-2ch .pane { flex:1; max-width:44%; }
.ss-2ch .pane h3 { font-size:1.3vw; margin-bottom:1.2%; color:#ecf0f1; font-weight:700; text-align:center; }
.ss-2ch .ss-chart { width:100%; height:30%; margin:.5% auto; }
.ss-2ch .ss-pcap { width:100%; }
.ss-chart .ss-chcap { display:none; }
.ss-chart.first .ss-chcap { display:block; }
.ss-gantt { display:flex; flex-direction:column; gap:1.6%; width:82%; margin:.8% auto; }
.ss-grow { display:flex; align-items:center; gap:1.2%; }
.ss-glabel { width:12%; text-align:right; font-weight:700; font-size:1.2vw; flex:none; }
.ss-gtrack { position:relative; flex:1; background:rgba(255,255,255,.06); border-radius:8px; height:5.4vh; min-height:44px; }
.ss-gbar { position:absolute; top:14%; bottom:14%; border-radius:8px; display:flex; align-items:center; justify-content:center; font-weight:800; font-size:1vw; box-shadow:0 3px 12px rgba(0,0,0,.35); }
.ss-gbar.ga { background:linear-gradient(135deg,#8ec8ff,#4aa3f0); color:#0d1b34; }
.ss-gbar.gb { background:linear-gradient(135deg,#b3bcc2,#7f8c9b); color:#101820; }
.ss-gbar.gc { background:linear-gradient(135deg,#ffd97a,#f39c12); color:#231a05; }
.ss-axis { display:flex; justify-content:flex-end; width:82%; margin:0 auto; font-size:1.15vw; color:#f39c12; font-weight:600; }
.ss-intro { font-size:1.3vw; margin-bottom:1.2%; opacity:.95; }
.ss-tbl { border-collapse:collapse; width:86%; margin:1.2% auto; font-size:1.05vw; background:rgba(10,18,38,.5); }
.ss-tbl caption { font-size:1.35vw; font-weight:800; margin-bottom:1%; color:#f39c12; }
.ss-tbl th, .ss-tbl td { border:1px solid rgba(255,255,255,.22); padding:.5% .8%; text-align:center; }
.ss-tbl th { background:linear-gradient(90deg,rgba(243,156,18,.28),rgba(231,76,60,.28)); font-weight:700; }
.ss-tbl td:first-child, .ss-tbl th:first-child { text-align:left; background:rgba(255,255,255,.06); font-weight:600; }
.ss-tbl tr.alt td { background:rgba(255,255,255,.035); }
.ss-tbl .neg { color:#ff9b8a; font-size:.92vw; display:block; }
.ss-chain { display:flex; justify-content:center; align-items:stretch; gap:.5%; width:97%; margin:0 auto 2%; }
.ss-node { flex:1; background:rgba(255,255,255,.07); border:1px solid rgba(255,255,255,.18); border-radius:14px; padding:1% .6%; font-size:1.1vw; font-weight:700; display:flex; align-items:center; justify-content:center; text-align:center; transition:all .3s ease; }
.ss-head { flex:none; width:9%; display:flex; align-items:center; justify-content:center; font-weight:800; color:#f39c12; font-size:1.05vw; }
.ss-chain .orphe { color:#f39c12; font-weight:900; font-size:1.6vw; display:flex; align-items:center; flex:none; }
.ss-tree { display:flex; flex-direction:column; align-items:center; gap:1%; margin:.5% auto 0; }
.ss-tree .tbox { background:rgba(255,255,255,.1); border:2px solid rgba(255,255,255,.35); border-radius:12px; padding:.8% 2.4%; font-size:1.5vw; font-weight:800; }
.ss-tree .tlinks { display:flex; gap:24%; font-size:1.5vw; color:#f39c12; font-weight:900; }
.ss-tree .trow { display:flex; gap:14%; }
.ss-tree .trow .tbox { font-size:1.35vw; padding:.7% 2%; font-weight:700; }
.ss-tree .tn { color:#f39c12; font-weight:900; margin-right:.5em; }
"""

NEW = r"""
  <section class="slide slide41 t-zoom" data-i="40" data-t="Zoom">
    <div class="ribbon anim"></div>
    <h2 class="anim">Plan de Charge</h2>
    <div class="roles">
      <div class="role-card blue anim d2">
        <div class="role-head">
          <div class="r-ico">📊</div>
          <h3>Définition</h3>
        </div>
        <ul>
          <li>Définit les <b style="color:#f39c12;">charges</b> dépendant des OF prévus par le Calcul des Besoins</li>
          <li>Comparaison de la <b style="color:#f39c12;">charge</b> à la <b style="color:#f39c12;">capacité</b></li>
          <li>Définit les actions à réaliser pour satisfaire les délais et les contraintes de production</li>
        </ul>
        <div class="big-ico">📊</div>
      </div>
      <div class="role-card red anim d4">
        <div class="role-head">
          <div class="r-ico">⏱️</div>
          <h3>Paramètres</h3>
        </div>
        <ul>
          <li>Horizon : <b style="color:#e74c3c;">1 à 6 mois</b></li>
          <li>Période : <b style="color:#e74c3c;">1 semaine à 1 mois</b></li>
          <li>Finesse des données : article, centre de charge</li>
        </ul>
        <div class="big-ico">⏱️</div>
      </div>
    </div>
  </section>

  <section class="slide slide42 t-insert" data-i="41" data-t="Insertion">
    <div class="ribbon anim"></div>
    <h2 class="anim">Plan de Charge (2)</h2>
    <div class="ss-diag">
      <div class="ss-topin anim d1">
        <span class="ss-mini">📏 Gammes</span>
        <span class="ss-down">⬇</span>
      </div>
      <div class="flow">
        <div class="flow-box anim d1">
          <div class="f-ico">📥</div>
          <h3>ENTRÉES</h3>
          <ul><li>OF proposés</li><li>Capacités de production</li></ul>
        </div>
        <div class="flow-arrow anim d2">➜</div>
        <div class="flow-box anim d2" style="border-color:#f39c12; background:rgba(243,156,18,.15);">
          <div class="f-ico">📊</div>
          <h3 style="color:#fff;">PLAN DE CHARGE</h3>
        </div>
        <div class="flow-arrow anim d3">➜</div>
        <div class="flow-box anim d3">
          <div class="f-ico">📤</div>
          <h3 style="color:#e74c3c;">SORTIES</h3>
          <ul><li>OF à réaliser par période</li><li>Charge par centre de charge</li></ul>
        </div>
      </div>
    </div>
  </section>

  <section class="slide slide43 t-rise" data-i="42" data-t="Ascension">
    <div class="ribbon anim"></div>
    <h2 class="anim">Plan de Charge (3)</h2>
    <div class="ss-chart anim d1">
      <span class="ss-chcap">Charge ↑</span>
      <div class="ss-bar" style="height:72%"></div>
      <div class="ss-bar" style="height:50%"></div>
      <div class="ss-bar" style="height:74%"></div>
      <div class="ss-bar ov" style="height:108%"></div>
      <div class="ss-bar" style="height:90%"></div>
      <div class="ss-bar" style="height:48%"></div>
      <div class="ss-bar" style="height:70%"></div>
      <div class="ss-capline" style="bottom:90%"><span class="ss-caplab">▬ Capacité</span></div>
    </div>
    <div class="ss-pcap anim d3">Période ➜</div>
    <p class="ss-note anim d4">Une période peut dépasser la <b style="color:#f39c12;">capacité</b> — le plan de charge vise à la maîtriser</p>
  </section>

  <section class="slide slide44 t-up" data-i="43" data-t="Verticale">
    <div class="ribbon anim"></div>
    <h2 class="anim">Équilibre charge / capacité</h2>
    <div class="roles">
      <div class="role-card blue anim d2">
        <div class="role-head">
          <div class="r-ico">⚖️</div>
          <h3>MRP2 intègre la contrainte de capacité (pas MRP)</h3>
        </div>
        <ul>
          <li>Pour <b style="color:#f39c12;">équilibrer</b> charge et capacité</li>
          <li><b>Variation de capacité</b> : heures supplémentaires, chômage partiel, nombre d'équipes, intérimaires, investissements machines</li>
        </ul>
        <div class="big-ico">⚖️</div>
      </div>
      <div class="role-card red anim d4">
        <div class="role-head">
          <div class="r-ico">🔁</div>
          <h3>Variation de charge</h3>
        </div>
        <ul>
          <li>Anticipation de charge</li>
          <li>Retard de livraison négocié</li>
          <li>Sous-traitance</li>
          <li>Utilisation de <b style="color:#e74c3c;">gammes de substitution</b></li>
        </ul>
        <div class="big-ico">🔁</div>
      </div>
    </div>
  </section>

  <section class="slide slide45 t-push" data-i="44" data-t="Poussée">
    <div class="ribbon anim"></div>
    <h2 class="anim">Ordonnancement</h2>
    <div class="roles">
      <div class="role-card blue anim d2">
        <div class="role-head">
          <div class="r-ico">⚙️</div>
          <h3>Définition</h3>
        </div>
        <ul>
          <li>Définit l'<b style="color:#f39c12;">ordre</b> dans lequel les Ordres de Fabrication doivent se succéder sur chaque poste de travail</li>
        </ul>
        <div class="big-ico">⚙️</div>
      </div>
      <div class="role-card red anim d4">
        <div class="role-head">
          <div class="r-ico">⏱️</div>
          <h3>Paramètres</h3>
        </div>
        <ul>
          <li>Horizon : <b style="color:#e74c3c;">1 mois</b></li>
          <li>Période : <b style="color:#e74c3c;">de 1 minute à 1 jour</b></li>
          <li>Finesse des données : la plus précise possible (opération, temps de changement de production…)</li>
        </ul>
        <div class="big-ico">⏱️</div>
      </div>
    </div>
  </section>

  <section class="slide slide46 t-blur" data-i="45" data-t="Flou">
    <div class="ribbon anim"></div>
    <h2 class="anim">Ordonnancement (2)</h2>
    <div class="ss-diag">
      <div class="ss-topin anim d1">
        <span class="ss-mini">📏 Gammes</span>
        <span class="ss-down">⬇</span>
        <span class="ss-mini">📋 Critères d'ordonnancement</span>
        <span class="ss-down">⬇</span>
      </div>
      <div class="flow">
        <div class="flow-box anim d1">
          <div class="f-ico">📥</div>
          <h3>ENTRÉES</h3>
          <ul><li>OF</li><li>Disponibilités des ressources</li></ul>
        </div>
        <div class="flow-arrow anim d2">➜</div>
        <div class="flow-box anim d2" style="border-color:#f39c12; background:rgba(243,156,18,.15);">
          <div class="f-ico">⚙️</div>
          <h3 style="color:#fff;">ORDONNANCEMENT</h3>
        </div>
        <div class="flow-arrow anim d3">➜</div>
        <div class="flow-box anim d3">
          <div class="f-ico">📤</div>
          <h3 style="color:#e74c3c;">SORTIES</h3>
          <ul><li>Succession d'OF à réaliser par ressource</li><li>Besoins en compétences</li></ul>
        </div>
      </div>
    </div>
  </section>

  <section class="slide slide47 t-rotate" data-i="46" data-t="Rotation">
    <div class="ribbon anim"></div>
    <h2 class="anim">Difficultés liées à l'ordonnancement</h2>
    <div class="def-grid">
      <div class="def-item anim d1"><div class="d-ico">🧮</div><div class="d-txt"><b style="color:#f39c12;">Combinatoire élevée</b> : beaucoup de produits, beaucoup d'opérations, beaucoup de ressources</div></div>
      <div class="def-item anim d2"><div class="d-ico">⏳</div><div class="d-txt">La <b>solution optimale</b> est difficile à obtenir dans un délai raisonnable</div></div>
      <div class="def-item anim d3" style="border-left-color:#e74c3c;"><div class="d-ico">🌪️</div><div class="d-txt">… et difficile à <b style="color:#e74c3c;">appliquer</b> : le caractère dynamique de la production (aléas) bouleverse la planification</div></div>
    </div>
  </section>

  <section class="slide slide48 t-zoom" data-i="47" data-t="Zoom">
    <div class="ribbon anim"></div>
    <h2 class="anim">Diagramme de Gantt</h2>
    <p class="ss-intro anim d1">📈 Représentation des opérations et des ressources par des <b style="color:#f39c12;">bâtonnets proportionnels</b> au temps d'occupation de la ressource par une opération.</p>
    <div class="ss-gantt">
      <div class="ss-grow anim d2">
        <div class="ss-glabel">Ressource 3</div>
        <div class="ss-gtrack"><div class="ss-gbar gb" style="left:50%; width:46%;">Produit B (20)</div></div>
      </div>
      <div class="ss-grow anim d3">
        <div class="ss-glabel">Ressource 2</div>
        <div class="ss-gtrack"><div class="ss-gbar gb" style="left:0%; width:37%;">Produit B (10)</div><div class="ss-gbar ga" style="left:40%; width:42%;">Produit A (20)</div></div>
      </div>
      <div class="ss-grow anim d4">
        <div class="ss-glabel">Ressource 1</div>
        <div class="ss-gtrack"><div class="ss-gbar ga" style="left:0%; width:37%;">Produit A (10)</div><div class="ss-gbar gc" style="left:37%; width:34%;">Produit C (30)</div></div>
      </div>
    </div>
    <div class="ss-axis anim d5">Période ➜</div>
  </section>

  <section class="slide slide49 t-insert" data-i="48" data-t="Insertion">
    <div class="ribbon anim"></div>
    <h2 class="anim">Lancement / suivi de la fabrication</h2>
    <div class="def-grid">
      <div class="def-item wide anim d1"><div class="d-ico">🤝</div><div class="d-txt"><b style="color:#f39c12;">Interface</b> entre la planification et la production</div></div>
      <div class="def-item wide anim d2"><div class="d-ico">📂</div><div class="d-txt"><b>Prépare le dossier de lancement</b> — demande d'approvisionnement (articles achetés) ; demande de fabrication (articles fabriqués) : OF, gamme opératoire, bons de travaux (1 par opération), fiche suiveuse, bons de sortie matière et outillages</div></div>
      <div class="def-item wide anim d3"><div class="d-ico">👀</div><div class="d-txt"><b>Suit la production</b> — transmission de l'information de fin de chaque opération</div></div>
    </div>
  </section>

  <section class="slide slide50 t-rise" data-i="49" data-t="Ascension">
    <div class="particles">
      <span style="left:8%; animation-delay:0s;"></span><span style="left:18%; animation-delay:1s;"></span>
      <span style="left:30%; animation-delay:2s;"></span><span style="left:44%; animation-delay:3s;"></span>
      <span style="left:58%; animation-delay:4s;"></span><span style="left:70%; animation-delay:5s;"></span>
      <span style="left:82%; animation-delay:6s;"></span><span style="left:92%; animation-delay:7s;"></span>
    </div>
    <h2 class="anim" style="font-size:3vw;">Méthode de gestion de production</h2>
    <h2 class="anim d2" style="font-size:4.5vw; font-weight:900;">MRP / MRP2</h2>
    <div class="picto anim d3">🧮</div>
  </section>

  <section class="slide slide51 t-up" data-i="50" data-t="Verticale">
    <div class="ribbon anim"></div>
    <h2 class="anim">Définitions</h2>
    <div class="roles">
      <div class="role-card blue anim d2">
        <div class="role-head">
          <div class="r-ico">🧮</div>
          <h3>MRP — Material Requirements Planning</h3>
        </div>
        <ul>
          <li>Définit un programme de production sur la base des <b style="color:#f39c12;">nomenclatures</b></li>
          <li>Sans prendre en compte les capacités des moyens de production (<b style="color:#f39c12;">capacité infinie</b>)</li>
        </ul>
        <div class="big-ico">🧮</div>
      </div>
      <div class="role-card red anim d4">
        <div class="role-head">
          <div class="r-ico">🏗️</div>
          <h3>MRP2 — Manufacturing Resources Planning</h3>
        </div>
        <ul>
          <li>Complète MRP en prenant en compte la limite de capacité des ressources (<b style="color:#e74c3c;">capacité finie</b>)</li>
          <li>Ajuste la charge en fonction des capacités (<b style="color:#e74c3c;">bouclage</b> du plan de charge)</li>
        </ul>
        <div class="big-ico">🏗️</div>
      </div>
    </div>
  </section>

  <section class="slide slide52 t-push" data-i="51" data-t="Poussée">
    <div class="ribbon anim"></div>
    <h2 class="anim">Limites de la gestion des stocks</h2>
    <div class="roles">
      <div class="role-card blue anim d2">
        <div class="role-head">
          <div class="r-ico">📦</div>
          <h3>Gestion des stocks</h3>
        </div>
        <ul>
          <li>Définit les quantités à stocker par compromis entre <b style="color:#f39c12;">coût de détention</b> et <b style="color:#f39c12;">coût d'acquisition</b></li>
          <li>Hypothèses : régularité de la demande, indépendance des produits gérés</li>
        </ul>
        <div class="big-ico">📦</div>
      </div>
      <div class="role-card red anim d4">
        <div class="role-head">
          <div class="r-ico">⚠️</div>
          <h3>Exemple</h3>
        </div>
        <ul>
          <li>Un produit est formé de <b>12 composants</b> gérés en gestion des stocks, avec un risque de rupture de 5 % chacun</li>
          <li>Probabilité que les 12 composants soient disponibles en même temps : 0,95¹² ≈ <b style="color:#e74c3c; font-size:1.4em;">0,54</b></li>
        </ul>
        <div class="big-ico">⚠️</div>
      </div>
    </div>
  </section>

  <section class="slide slide53 t-blur" data-i="52" data-t="Flou">
    <div class="ribbon anim"></div>
    <h2 class="anim">Besoins indépendants / dépendants</h2>
    <div class="roles">
      <div class="role-card blue anim d2">
        <div class="role-head">
          <div class="r-ico">🙋</div>
          <h3>Besoins indépendants (ou externes)</h3>
        </div>
        <ul>
          <li>Exprimés par les <b style="color:#f39c12;">clients</b> (produits finis, pièces de rechange)</li>
          <li>Demande régulière → <b style="color:#f39c12;">traitement statistique</b></li>
        </ul>
        <div class="big-ico">🙋</div>
      </div>
      <div class="role-card red anim d4">
        <div class="role-head">
          <div class="r-ico">🧩</div>
          <h3>Besoins dépendants (ou internes)</h3>
        </div>
        <ul>
          <li>Sous le <b style="color:#e74c3c;">contrôle de l'entreprise</b> — calculables à partir des besoins indépendants par décomposition arborescente des produits finis en composants</li>
          <li>Pas de consommation régulière → <b style="color:#e74c3c;">pas de traitement statistique</b></li>
        </ul>
        <div class="big-ico">🧩</div>
      </div>
    </div>
  </section>

  <section class="slide slide54 t-rotate" data-i="53" data-t="Rotation">
    <div class="ribbon anim"></div>
    <h2 class="anim">Principe du MRP</h2>
    <div class="def-grid">
      <div class="def-item anim d1"><div class="d-ico">🔗</div><div class="d-txt">Les <b style="color:#f39c12;">besoins dépendants</b> doivent être définis à partir des besoins indépendants&nbsp;!</div></div>
      <div class="def-item anim d2"><div class="d-ico">🧩</div><div class="d-txt">Les <b style="color:#f39c12;">besoins en composants et articles</b> doivent être calculés à partir des besoins en produits finis&nbsp;!</div></div>
      <div class="def-item anim d3" style="border-left-color:#e74c3c;"><div class="d-ico">🧮</div><div class="d-txt">Le <b style="color:#e74c3c;">calcul des besoins</b> (dépendants à partir des indépendants) est la base du MRP (donc de MRP2)&nbsp;!</div></div>
    </div>
  </section>

  <section class="slide slide55 t-zoom" data-i="54" data-t="Zoom">
    <div class="ribbon anim"></div>
    <h2 class="anim">Conditions préalables à l'implantation de MRP/MRP2</h2>
    <div class="def-grid">
      <div class="def-item anim d1"><div class="d-ico">📆</div><div class="d-txt">Existence d'un <b>Plan Directeur de Production</b></div></div>
      <div class="def-item anim d2"><div class="d-ico">🌳</div><div class="d-txt">Existence de <b>nomenclatures</b></div></div>
      <div class="def-item anim d3"><div class="d-ico">📦</div><div class="d-txt">États des <b>stocks</b></div></div>
      <div class="def-item anim d4"><div class="d-ico">⏳</div><div class="d-txt"><b>Délais d'obtention</b></div></div>
      <div class="def-item anim d5"><div class="d-ico">📏</div><div class="d-txt"><b>Gammes opératoires</b></div></div>
      <div class="def-item anim d6"><div class="d-ico">🚦</div><div class="d-txt"><b>Priorités</b> des produits</div></div>
      <div class="def-item anim d7"><div class="d-ico">⚖️</div><div class="d-txt"><b>Capacités de production</b> (MRP2)</div></div>
    </div>
  </section>

  <section class="slide slide56 t-insert" data-i="55" data-t="Insertion">
    <div class="ribbon anim"></div>
    <h2 class="anim">PDP</h2>
    <div class="roles">
      <div class="role-card blue anim d2">
        <div class="role-head">
          <div class="r-ico">📆</div>
          <h3>Définition</h3>
        </div>
        <ul>
          <li>Définit la <b style="color:#f39c12;">programmation de la production</b> des produits finis pour faire face à une demande <b style="color:#f39c12;">ferme et prévisionnelle</b> (transmise par les commerciaux)</li>
        </ul>
        <div class="big-ico">📆</div>
      </div>
      <div class="role-card red anim d4">
        <div class="role-head">
          <div class="r-ico">➡️</div>
          <h3>Rôle dans le calcul des besoins</h3>
        </div>
        <ul>
          <li>Le résultat du PDP est utilisé comme <b style="color:#e74c3c;">donnée d'entrée</b> au calcul des besoins</li>
          <li>pour définir les <b style="color:#e74c3c;">besoins nets jalonnés</b> des articles</li>
        </ul>
        <div class="big-ico">➡️</div>
      </div>
    </div>
  </section>

  <section class="slide slide57 t-rise" data-i="56" data-t="Ascension">
    <div class="ribbon anim"></div>
    <h2 class="anim">Plan Directeur de Production (exemple)</h2>
    <p class="ss-intro anim d1">Le produit fini a un <b style="color:#f39c12;">stock initial de 60 produits</b>.</p>
    <table class="ss-tbl anim d2">
      <caption>Produit INT56 — Lot de lancement 200 — Stock de sécurité 0</caption>
      <tr><th>Période</th><th>0</th><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th></tr>
      <tr><td>Plan des besoins commerciaux bruts</td><td></td><td>180</td><td>180</td><td>60</td><td>50</td><td>150</td><td>160</td></tr>
      <tr class="alt"><td>Stocks</td><td>60</td><td>80</td><td>100</td><td>40</td><td>190</td><td>40</td><td>80</td></tr>
      <tr><td>Plan des besoins commerciaux nets</td><td></td><td>120</td><td>100</td><td><span class="neg">(-40)</span>0</td><td>10</td><td><span class="neg">(-40)</span>0</td><td>120</td></tr>
      <tr class="alt"><td>Plan Directeur de Production</td><td></td><td>200</td><td>200</td><td>0</td><td>200</td><td>0</td><td>200</td></tr>
    </table>
  </section>

  <section class="slide slide58 t-up" data-i="57" data-t="Verticale">
    <div class="ribbon anim"></div>
    <h2 class="anim">Calcul des Besoins</h2>
    <div class="def-grid">
      <div class="def-item wide anim d1"><div class="d-ico">🔽</div><div class="d-txt">Pour chaque <b style="color:#f39c12;">produit</b> — en descendant dans la nomenclature — puis pour chaque <b style="color:#f39c12;">article</b> :</div></div>
      <div class="def-item anim d2"><div class="d-ico">🧲</div><div class="d-txt">Regrouper les <b>Besoins Bruts</b> issus des différents produits</div></div>
      <div class="def-item anim d3"><div class="d-ico">➖</div><div class="d-txt"><b style="color:#f39c12;">Besoin Net (P) = Besoin Brut (P) − Stock (P−1)</b></div></div>
      <div class="def-item anim d4"><div class="d-ico">🗓️</div><div class="d-txt"><b style="color:#f39c12;">Début OF = Période du Besoin Net − Délai de production</b></div></div>
      <div class="def-item anim d5"><div class="d-ico">📦</div><div class="d-txt">Quantité à produire dépend des <b>lots de production</b></div></div>
    </div>
  </section>

  <section class="slide slide59 t-push" data-i="58" data-t="Poussée">
    <div class="ribbon anim"></div>
    <h2 class="anim">Calcul des Besoins (exemple)</h2>
    <div class="ss-tree">
      <div class="tbox anim d1">👓 Lunettes</div>
      <div class="tlinks anim d2"><span>×2 ↙</span><span>↘ ×1</span></div>
      <div class="trow anim d2">
        <div class="tbox">🔩 branche</div>
        <div class="tbox">🔧 monture</div>
      </div>
    </div>
    <div class="def-grid" style="margin-top:1.5%;">
      <div class="def-item anim d3"><div class="d-ico">⏱️</div><div class="d-txt">Délai d'assemblage : <b style="color:#f39c12;">1 période</b></div></div>
      <div class="def-item anim d4"><div class="d-ico">⏱️</div><div class="d-txt">Délai de réalisation des branches : <b style="color:#f39c12;">2 périodes</b></div></div>
      <div class="def-item anim d5"><div class="d-ico">📦</div><div class="d-txt">Lot de production lunettes : <b style="color:#f39c12;">100</b></div></div>
      <div class="def-item anim d6"><div class="d-ico">📦</div><div class="d-txt">Lot de production branches : <b style="color:#f39c12;">200</b></div></div>
    </div>
  </section>

  <section class="slide slide60 t-blur" data-i="59" data-t="Flou">
    <div class="ribbon anim"></div>
    <h2 class="anim">Calcul des Besoins (exemple 2)</h2>
    <table class="ss-tbl anim d1" style="font-size:.98vw; width:94%;">
      <tr><th>Période</th><th>0</th><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th></tr>
      <tr><td>PDP lunettes</td><td></td><td>100</td><td>100</td><td>100</td><td>200</td><td>100</td><td>200</td></tr>
      <tr class="alt"><td>En-cours et stocks lunettes</td><td>200</td><td>100</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr>
      <tr><td>Besoins nets lunettes</td><td></td><td><span class="neg">(-100)</span>0</td><td>0</td><td>100</td><td>200</td><td>100</td><td>200</td></tr>
      <tr class="alt"><td>Ordres de lancement lunettes</td><td></td><td>0</td><td>100</td><td>200</td><td>100</td><td>200</td><td></td></tr>
      <tr><td>Besoins bruts branches</td><td></td><td>0</td><td>200</td><td>400</td><td>200</td><td>400</td><td></td></tr>
      <tr class="alt"><td>En-cours et stock branche</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td><td></td></tr>
      <tr><td>Besoins nets branches</td><td></td><td></td><td>100</td><td>300</td><td>100</td><td>300</td><td></td></tr>
      <tr class="alt"><td>Ordres de lancement branches</td><td>200</td><td>400</td><td>200</td><td>400</td><td></td><td></td><td></td></tr>
    </table>
  </section>

  <section class="slide slide61 t-rotate" data-i="60" data-t="Rotation">
    <div class="ribbon anim"></div>
    <h2 class="anim">Plan de Charge</h2>
    <div class="def-grid">
      <div class="def-item anim d1"><div class="d-ico">📊</div><div class="d-txt">Définit la <b style="color:#f39c12;">charge par période et par ressource</b></div></div>
      <div class="def-item anim d2"><div class="d-ico">🧭</div><div class="d-txt">Peut être réalisé <b>à tout moment</b>, à différents niveaux de détail — ressources : entreprise, usine, centre de charge, ressource — périodes : année, mois, jour</div></div>
      <div class="def-item anim d3" style="border-left-color:#e74c3c;"><div class="d-ico">🌊</div><div class="d-txt">Peut être <b style="color:#e74c3c;">lissé</b> (MRP2) suivant les capacités, en intégrant les <b>priorités des produits</b></div></div>
    </div>
  </section>

  <section class="slide slide62 t-zoom" data-i="61" data-t="Zoom">
    <div class="ribbon anim"></div>
    <h2 class="anim">Lissage du plan de charge</h2>
    <div class="ss-2ch">
      <div class="pane anim d1">
        <h3>Avant lissage</h3>
        <div class="ss-chart">
          <div class="ss-bar" style="height:62%"></div>
          <div class="ss-bar" style="height:48%"></div>
          <div class="ss-bar" style="height:66%"></div>
          <div class="ss-bar ov" style="height:108%"></div>
          <div class="ss-bar" style="height:88%"></div>
          <div class="ss-bar" style="height:50%"></div>
          <div class="ss-bar" style="height:68%"></div>
          <div class="ss-capline" style="bottom:90%"><span class="ss-caplab">▬ Capacité</span></div>
        </div>
        <div class="ss-pcap">Période ➜</div>
      </div>
      <div class="pane anim d3">
        <h3>Après lissage</h3>
        <div class="ss-chart">
          <div class="ss-bar" style="height:62%"></div>
          <div class="ss-bar" style="height:48%"></div>
          <div class="ss-bar" style="height:77%"></div>
          <div class="ss-bar" style="height:100%"></div>
          <div class="ss-bar" style="height:88%"></div>
          <div class="ss-bar" style="height:50%"></div>
          <div class="ss-bar" style="height:68%"></div>
          <div class="ss-capline" style="bottom:90%"><span class="ss-caplab" style="background:rgba(231,76,60,.9); color:#fff;">▬ Capacité</span></div>
        </div>
        <div class="ss-pcap">Période ➜</div>
      </div>
    </div>
    <p class="ss-note anim d5">⚡ On <b style="color:#f39c12;">déplace la surcharge</b> vers une période sous-chargée</p>
  </section>

  <section class="slide slide63 t-insert" data-i="62" data-t="Insertion">
    <div class="ribbon anim"></div>
    <h2 class="anim">Principe du MRP2</h2>
    <div class="ss-chain anim d1">
      <div class="ss-node">🧮 Calcul des Besoins</div>
      <div class="orphe">➜</div>
      <div class="ss-node">📊 Plan de charge</div>
      <div class="orphe">➜</div>
      <div class="ss-node">⚙️ Ordonnancement</div>
      <div class="orphe">➜</div>
      <div class="ss-node">🚀 Lancement</div>
      <div class="orphe">➜</div>
      <div class="ss-node">🔍 Contrôle et suivi</div>
    </div>
    <p class="ss-note anim d3">Du plus global au plus fin : chaque niveau <b style="color:#f39c12;">étage la planification</b></p>
  </section>

  <section class="slide slide64 t-rise" data-i="63" data-t="Ascension">
    <div class="ribbon anim"></div>
    <h2 class="anim">Difficultés dans la mise en œuvre</h2>
    <div class="def-grid">
      <div class="def-item anim d1"><div class="d-ico">💾</div><div class="d-txt"><b>Beaucoup de données</b> à traiter — difficulté de mise à jour</div></div>
      <div class="def-item anim d2"><div class="d-ico">🖥️</div><div class="d-txt"><b style="color:#f39c12;">Informatisation</b> (souvent) nécessaire</div></div>
      <div class="def-item anim d3"><div class="d-ico">💸</div><div class="d-txt"><b>Progiciels lourds et coûteux</b> (BPCS, MAPICS, SAP/R3 (ERP)… 300 k€)</div></div>
      <div class="def-item anim d4" style="border-left-color:#e74c3c;"><div class="d-ico">⚠️</div><div class="d-txt"><b style="color:#e74c3c;">Mauvaises performances en court terme</b> — déviation courante : utilisation maximale des machines</div></div>
    </div>
  </section>

  <section class="slide slide65 t-up" data-i="64" data-t="Verticale">
    <div class="ribbon anim"></div>
    <h2 class="anim">Cercles pervers</h2>
    <p class="ss-intro anim d1">🌀 Deux enchaînements auto-entretenus :</p>
    <div class="ss-chain anim d2">
      <div class="ss-head">Cercle 1</div>
      <div class="ss-node">📦 En-cours importants</div>
      <div class="orphe">➜</div>
      <div class="ss-node">👁️ Difficulté de suivi</div>
      <div class="orphe">➜</div>
      <div class="ss-node">❓ Incertitude sur les décalages</div>
      <div class="orphe">➜</div>
      <div class="ss-node">🗓️ Décalages de planification importants</div>
      <div class="orphe">↺</div>
    </div>
    <div class="ss-chain anim d3">
      <div class="ss-head">Cercle 2</div>
      <div class="ss-node">📦 En-cours importants</div>
      <div class="orphe">➜</div>
      <div class="ss-node">🕰️ Cycles de fab. longs</div>
      <div class="orphe">➜</div>
      <div class="ss-node">🔮 Anticiper les ventes</div>
      <div class="orphe">➜</div>
      <div class="ss-node">📜 Prévisions lointaines</div>
      <div class="orphe">➜</div>
      <div class="ss-node">❓ Incertitude importante</div>
      <div class="orphe">➜</div>
      <div class="ss-node">📦 Lots de production importants</div>
      <div class="orphe">↺</div>
    </div>
  </section>

  <section class="slide slide66 t-push" data-i="65" data-t="Poussée">
    <div class="ribbon anim"></div>
    <h2 class="anim">Progresser&nbsp;?</h2>
    <div class="roles">
      <div class="role-card blue anim d2">
        <div class="role-head">
          <div class="r-ico">🧾</div>
          <h3>La comptabilité valorise peu…</h3>
        </div>
        <ul>
          <li>la diminution des <b style="color:#f39c12;">stocks et encours</b></li>
          <li>la diminution des <b style="color:#f39c12;">cycles de production</b></li>
        </ul>
        <div class="big-ico">🧾</div>
      </div>
      <div class="role-card red anim d4">
        <div class="role-head">
          <div class="r-ico">💎</div>
          <h3>Pourtant…</h3>
        </div>
        <ul>
          <li>Cycle de production <b style="color:#e74c3c;">maîtrisé et court</b> + peu de stocks</li>
          <li><b style="color:#e74c3c;">Gain de trésorerie</b></li>
          <li><b style="color:#e74c3c;">Nouveaux marchés possibles</b></li>
        </ul>
        <div class="big-ico">💎</div>
      </div>
    </div>
  </section>

  <section class="slide slide67 t-blur" data-i="66" data-t="Flou">
    <div class="ribbon anim"></div>
    <h2 class="anim">Conclusion MRP/MRP2</h2>
    <div class="def-grid">
      <div class="def-item anim d1"><div class="d-ico">🏭</div><div class="d-txt">Méthode deGP pour de <b>nombreux produits</b>, avec de nombreux composants et articles</div></div>
      <div class="def-item anim d2"><div class="d-ico">🧮</div><div class="d-txt">Principe du <b style="color:#f39c12;">calcul des besoins en composants</b> à partir des besoins en produits finis</div></div>
      <div class="def-item anim d3"><div class="d-ico">♾️</div><div class="d-txt"><b style="color:#f39c12;">Capacité infinie</b> en MRP, <b style="color:#e74c3c;">capacité finie</b> en MRP2</div></div>
      <div class="def-item anim d4"><div class="d-ico">📊</div><div class="d-txt">Nécessite des <b>données techniques et commerciales fiables</b></div></div>
    </div>
  </section>

  <section class="slide slide68 t-rotate" data-i="67" data-t="Rotation">
    <div class="ribbon anim"></div>
    <h2 class="anim">Conclusion MRP/MRP2 (2)</h2>
    <div class="def-grid">
      <div class="def-item wide anim d1"><div class="d-ico">🖥️</div><div class="d-txt"><b style="color:#f39c12;">Informatisation</b> (GPAO, ERP) pour la gestion à moyen terme</div></div>
      <div class="def-item wide anim d2"><div class="d-ico">🍃</div><div class="d-txt"><b>Simplifier le problème à gérer</b> (concepts du Juste À Temps : MRP délais courts)</div></div>
      <div class="def-item wide anim d3" style="border-left-color:#e74c3c;"><div class="d-ico">✂️</div><div class="d-txt">Familles d'articles • lignes et îlots de production • diminution des <b style="color:#e74c3c;">lots de production et de transport</b> (maîtrise des procédés et des temps inter-opératoires) • maintenance préventive, SMED, 5S…</div></div>
    </div>
  </section>

  <section class="slide slide69 t-rise" data-i="68" data-t="Ascension">
    <div class="particles">
      <span style="left:8%; animation-delay:0s;"></span><span style="left:18%; animation-delay:1s;"></span>
      <span style="left:30%; animation-delay:2s;"></span><span style="left:44%; animation-delay:3s;"></span>
      <span style="left:58%; animation-delay:4s;"></span><span style="left:70%; animation-delay:5s;"></span>
      <span style="left:82%; animation-delay:6s;"></span><span style="left:92%; animation-delay:7s;"></span>
    </div>
    <h2 class="anim" style="font-size:4.5vw;">Chapitre 3</h2>
    <h2 class="anim d2" style="font-size:4.5vw; font-weight:900;">Données techniques &amp; GPAO / ERP</h2>
    <div class="picto anim d3">💾</div>
  </section>

  <section class="slide slide70 t-zoom" data-i="69" data-t="Zoom">
    <div class="ribbon anim"></div>
    <h2 class="anim">Les données</h2>
    <p class="ss-intro anim d1">La gestion de production nécessite de <b style="color:#f39c12;">nombreuses données</b> :</p>
    <div class="roles">
      <div class="role-card blue anim d2">
        <div class="role-head">
          <div class="r-ico">📊</div>
          <h3>Données commerciales</h3>
        </div>
        <ul>
          <li>Évolution du marché</li>
          <li>Liste des clients</li>
          <li>Liste des fournisseurs</li>
          <li>Planning des commandes</li>
        </ul>
        <div class="big-ico">📊</div>
      </div>
      <div class="role-card red anim d4">
        <div class="role-head">
          <div class="r-ico">🔧</div>
          <h3>Données techniques</h3>
        </div>
        <ul>
          <li>Fichier descriptif des articles</li>
          <li>État des stocks</li>
          <li>Nomenclatures</li>
          <li>Description des ressources</li>
          <li>Gammes de fabrication</li>
          <li>Calendriers</li>
        </ul>
        <div class="big-ico">🔧</div>
      </div>
    </div>
  </section>
"""

def main():
    with open(PATH, encoding="utf-8") as f:
        html = f.read()

    before = len(re.findall(r'<section class="slide', html))
    assert before == 40, f"attendu 40 slides, trouve {before}"

    # 1) CSS
    assert html.count("</style>") == 1
    html = html.replace("</style>", CSS + "</style>")

    # 2) insertion des slides apres la derniere (data-i="39")
    m = re.search(r'(<section class="slide[^"]*" data-i="39"[\s\S]*?</section>)(\s*</div>)', html)
    assert m, "point d'insertion introuvable"
    html = html[:m.end(1)] + NEW.rstrip("\n\n") + "\n" + html[m.start(2):]

    # 3) compteur statique
    html = html.replace('<span id="tot">40</span>', '<span id="tot">70</span>')

    after = len(re.findall(r'<section class="slide', html))
    assert after == 70, f"attendu 70 slides apres insertion, trouve {after}"

    with open(PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(html)
    print(f"OK : 40 -> {after} slides ; compteur 70")

if __name__ == "__main__":
    main()

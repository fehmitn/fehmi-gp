# -*- coding: utf-8 -*-
"""Batch 3 : slides source 41-70 -> slides 71-100 du diaporama.

Slides 71-88 : donnees techniques & demarche d'informatisation (def-grid /
roles / steps / table). Slides 89-97 : modules ERP (SAP R/3). Slides 98-100 :
intercalaire + stocks.
2 images originales recardees : assets_ss_image41.png (Donnees et GPAO),
assets_ss_image59.png (Structure d'un ERP).
"""
import re
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

PATH = r"C:\ppt\index.html"

CSS = r"""
/* ===== Slides 71-100 (slideshare OCR) ===== */
.slide98 { background:linear-gradient(135deg,#e74c3c 0%,#c0392b 55%,#8e2418 100%); flex-direction:column; }
.ss-steps { display:flex; flex-direction:column; gap:1%; width:78%; margin:1.2% auto; }
.ss-step { display:flex; align-items:center; gap:2%; color:#eef2ff; background:rgba(255,255,255,.07); border:1px solid rgba(255,255,255,.18); border-left:4px solid #f39c12; border-radius:12px; padding:1.1% 2%; font-size:1.3vw; font-weight:600; }
.ss-step .n { color:#f39c12; font-weight:900; font-size:1.45vw; min-width:3%; }
.ss-img { display:flex; align-items:center; justify-content:center; width:100%; height:74%; }
.ss-img img { max-width:88%; max-height:98%; border-radius:14px; padding:1.6%; background:rgba(255,255,255,.92); box-shadow:0 14px 45px rgba(0,0,0,.5); transition:transform .35s ease, box-shadow .35s ease; }
.ss-img img:hover { transform:scale(1.03); box-shadow:0 20px 60px rgba(0,0,0,.6); }
.ss-mods { display:grid; grid-template-columns:repeat(4,1fr); gap:1.6% 2%; width:92%; margin:1% auto; }
.ss-mod { color:#eef2ff; background:rgba(255,255,255,.07); border:1px solid rgba(255,255,255,.18); border-radius:12px; padding:1.4% 1.2%; font-size:1.02vw; text-align:center; }
.ss-mod b { display:block; color:#f39c12; font-size:1.3vw; margin-bottom:.4%; }
.ss-tbl td.c { font-weight:900; font-size:1.35vw; }

/* ===== Correctif titres slides 71-100 ===== */
.slide71, .slide72, .slide73, .slide74, .slide75, .slide76, .slide77, .slide78, .slide79, .slide80,
.slide81, .slide82, .slide83, .slide84, .slide85, .slide86, .slide87, .slide88, .slide89, .slide90,
.slide91, .slide92, .slide93, .slide94, .slide95, .slide96, .slide97, .slide98, .slide99, .slide100 { flex-direction:column; }
.slide71 h2, .slide72 h2, .slide73 h2, .slide74 h2, .slide75 h2, .slide76 h2, .slide77 h2, .slide78 h2, .slide79 h2, .slide80 h2,
.slide81 h2, .slide82 h2, .slide83 h2, .slide84 h2, .slide85 h2, .slide86 h2, .slide87 h2, .slide88 h2, .slide89 h2, .slide90 h2,
.slide91 h2, .slide92 h2, .slide93 h2, .slide94 h2, .slide95 h2, .slide96 h2, .slide97 h2, .slide98 h2, .slide99 h2, .slide100 h2 {
  font-size:3vw; color:#fff; font-weight:700; margin-bottom:.5%;
  align-self:flex-start;
}
.slide98 h2 { font-weight:900; margin-bottom:0; }
.slide71 .ribbon, .slide72 .ribbon, .slide73 .ribbon, .slide74 .ribbon, .slide75 .ribbon, .slide76 .ribbon, .slide77 .ribbon, .slide78 .ribbon, .slide79 .ribbon, .slide80 .ribbon,
.slide81 .ribbon, .slide82 .ribbon, .slide83 .ribbon, .slide84 .ribbon, .slide85 .ribbon, .slide86 .ribbon, .slide87 .ribbon, .slide88 .ribbon, .slide89 .ribbon, .slide90 .ribbon,
.slide91 .ribbon, .slide92 .ribbon, .slide93 .ribbon, .slide94 .ribbon, .slide95 .ribbon, .slide96 .ribbon, .slide97 .ribbon, .slide98 .ribbon, .slide99 .ribbon, .slide100 .ribbon {
  width:8%; height:5px; background:linear-gradient(90deg,#f39c12,#e74c3c);
  border-radius:5px; margin-bottom:3%; align-self:flex-start;
}
.slide98 .ribbon { display:none; }
"""

NEW = r"""
  <section class="slide slide71 t-rise" data-i="70" data-t="Ascension">
    <div class="ribbon anim"></div>
    <h2 class="anim">Données et GPAO</h2>
    <div class="ss-img anim d1"><img src="assets/assets_ss_image41.png" alt="Données et GPAO — flux entre les données et la planification"></div>
    <p class="ss-note anim d3">Commandes, stocks, nomenclatures, gammes et calendriers <b style="color:#f39c12;">alimentent la planification</b></p>
  </section>

  <section class="slide slide72 t-up" data-i="71" data-t="Verticale">
    <div class="ribbon anim"></div>
    <h2 class="anim">Nomenclatures</h2>
    <div class="ss-tree">
      <div class="tbox anim d1">👓 Lunettes</div>
      <div class="tlinks anim d2"><span>×2 ↙</span><span>↘ ×1</span></div>
      <div class="trow anim d2">
        <div class="tbox">🔩 branche</div>
        <div class="tbox">🔧 monture</div>
      </div>
    </div>
    <div class="def-grid" style="margin-top:1.5%;">
      <div class="def-item anim d3"><div class="d-ico">🌳</div><div class="d-txt"><b style="color:#f39c12;">Base de la décomposition</b> du produit fini en articles</div></div>
      <div class="def-item anim d4" style="border-left-color:#e74c3c;"><div class="d-ico">⚠️</div><div class="d-txt"><b style="color:#e74c3c;">Difficultés</b> : mise à jour • variantes</div></div>
    </div>
  </section>

  <section class="slide slide73 t-push" data-i="72" data-t="Poussée">
    <div class="ribbon anim"></div>
    <h2 class="anim">État des stocks</h2>
    <div class="roles">
      <div class="role-card blue anim d2">
        <div class="role-head">
          <div class="r-ico">📦</div>
          <h3>Rôle</h3>
        </div>
        <ul>
          <li>Permettent de définir <b style="color:#f39c12;">ce qu'il faut réellement produire</b> à partir des besoins</li>
          <li><b style="color:#f39c12;">Calcul des besoins nets</b> à partir des besoins bruts</li>
        </ul>
        <div class="big-ico">📦</div>
      </div>
      <div class="role-card red anim d4">
        <div class="role-head">
          <div class="r-ico">⚠️</div>
          <h3>Difficultés</h3>
        </div>
        <ul>
          <li><b>Inventaire</b> : périodicité&nbsp;? précision&nbsp;?</li>
          <li>Gérer ce qui est <b style="color:#e74c3c;">indispensable</b> (pas tout&nbsp;!)</li>
          <li><b>Informatiser</b> la gestion des stocks&nbsp;?</li>
        </ul>
        <div class="big-ico">⚠️</div>
      </div>
    </div>
  </section>

  <section class="slide slide74 t-blur" data-i="73" data-t="Flou">
    <div class="ribbon anim"></div>
    <h2 class="anim">Délais d'obtention</h2>
    <div class="roles">
      <div class="role-card blue anim d2">
        <div class="role-head">
          <div class="r-ico">⏳</div>
          <h3>À quoi ça sert</h3>
        </div>
        <ul>
          <li>Nécessaires pour le <b style="color:#f39c12;">jalonnement</b> (anticipation)</li>
        </ul>
        <div class="big-ico">⏳</div>
      </div>
      <div class="role-card red anim d4">
        <div class="role-head">
          <div class="r-ico">🧮</div>
          <h3>Composition du délai d'obtention</h3>
        </div>
        <ul>
          <li>Temps <b>opératoires</b> + temps <b>inter-opératoires</b> (attentes + transit)</li>
          <li>+ temps de <b>traitement administratif</b> + <b style="color:#e74c3c;">délai de sécurité</b></li>
        </ul>
        <div class="big-ico">🧮</div>
      </div>
    </div>
    <p class="ss-note anim d5">🕐 En production discrète, le temps d'attente représente <b style="color:#f39c12;">80&nbsp;% du délai d'obtention</b></p>
  </section>

  <section class="slide slide75 t-rotate" data-i="74" data-t="Rotation">
    <div class="ribbon anim"></div>
    <h2 class="anim">Gammes</h2>
    <div class="roles">
      <div class="role-card blue anim d2">
        <div class="role-head">
          <div class="r-ico">📏</div>
          <h3>Définition</h3>
        </div>
        <ul>
          <li>Définit l'<b style="color:#f39c12;">enchaînement des opérations</b> pour obtenir le produit fini à partir des composants</li>
          <li>Permet le <b>calcul des charges par ressource</b></li>
        </ul>
        <div class="big-ico">📏</div>
      </div>
      <div class="role-card red anim d4">
        <div class="role-head">
          <div class="r-ico">⚠️</div>
          <h3>Difficultés</h3>
        </div>
        <ul>
          <li><b>Mise à jour</b> des gammes</li>
          <li>Cohérence entre les <b style="color:#e74c3c;">gammes prévues</b> (Bureau des Méthodes) et les <b style="color:#e74c3c;">gammes réelles</b> (Production)</li>
        </ul>
        <div class="big-ico">⚠️</div>
      </div>
    </div>
  </section>

  <section class="slide slide76 t-zoom" data-i="75" data-t="Zoom">
    <div class="ribbon anim"></div>
    <h2 class="anim">Capacités de production</h2>
    <div class="roles">
      <div class="role-card blue anim d2">
        <div class="role-head">
          <div class="r-ico">🏭</div>
          <h3>Définition</h3>
        </div>
        <ul>
          <li>Définit la <b style="color:#f39c12;">charge limite par période</b> des ressources</li>
          <li>Les capacités sont <b style="color:#f39c12;">essentielles pour MRP2</b></li>
        </ul>
        <div class="big-ico">🏭</div>
      </div>
      <div class="role-card red anim d4">
        <div class="role-head">
          <div class="r-ico">⚠️</div>
          <h3>Difficultés</h3>
        </div>
        <ul>
          <li>Intégration de la <b style="color:#e74c3c;">disponibilité réelle</b> des ressources</li>
          <li><b>RT</b> : pannes, maintenance préventive, amélioration…</li>
          <li><b>RH</b> : absences, formations…</li>
        </ul>
        <div class="big-ico">⚠️</div>
      </div>
    </div>
  </section>

  <section class="slide slide77 t-insert" data-i="76" data-t="Insertion">
    <div class="ribbon anim"></div>
    <h2 class="anim">Priorités sur les produits</h2>
    <div class="roles">
      <div class="role-card blue anim d2">
        <div class="role-head">
          <div class="r-ico">🚦</div>
          <h3>Définition</h3>
        </div>
        <ul>
          <li>Définit l'<b style="color:#f39c12;">importance relative des produits</b></li>
          <li>Priorité <b>fixe</b> : client important, matière de valeur…</li>
          <li>Priorité <b style="color:#f39c12;">dynamique</b> : date de livraison, marge libre…</li>
        </ul>
        <div class="big-ico">🚦</div>
      </div>
      <div class="role-card red anim d4">
        <div class="role-head">
          <div class="r-ico">🎯</div>
          <h3>Utilisation</h3>
        </div>
        <ul>
          <li>Pour l'<b style="color:#e74c3c;">ordonnancement</b></li>
          <li>Pour l'ajustement du <b style="color:#e74c3c;">plan de charge</b> (en MRP2)</li>
        </ul>
        <div class="big-ico">🎯</div>
      </div>
    </div>
  </section>

  <section class="slide slide78 t-rise" data-i="77" data-t="Ascension">
    <div class="ribbon anim"></div>
    <h2 class="anim">Informatisation de la gestion de production (apports)</h2>
    <div class="def-grid">
      <div class="def-item anim d1"><div class="d-ico">💻</div><div class="d-txt"><b style="color:#f39c12;">Calculs performants</b> — calcul rapide des besoins nets jalonnés • plan de charge (lissé) • calcul et simulation de l'ordonnancement</div></div>
      <div class="def-item anim d2"><div class="d-ico">💾</div><div class="d-txt"><b>Mémorisation des informations</b> — historiques des pannes, des délais, des charges</div></div>
      <div class="def-item anim d3" style="border-left-color:#e74c3c;"><div class="d-ico">🧠</div><div class="d-txt"><b style="color:#e74c3c;">Aide à la décision</b> — pour le plan de charge et pour l'ordonnancement</div></div>
    </div>
  </section>

  <section class="slide slide79 t-up" data-i="78" data-t="Verticale">
    <div class="ribbon anim"></div>
    <h2 class="anim">Informatisation de la gestion de production (démarche)</h2>
    <p class="ss-intro anim d1">La démarche d'implantation d'un logiciel de <b style="color:#f39c12;">GPAO</b> doit permettre d'utiliser efficacement le logiciel</p>
    <div class="ss-steps">
      <div class="ss-step anim d1"><span class="n">1</span>Analyse de l'existant</div>
      <div class="ss-step anim d2"><span class="n">2</span>Expression des besoins</div>
      <div class="ss-step anim d3"><span class="n">3</span>Développement interne ou achat&nbsp;?</div>
      <div class="ss-step anim d4"><span class="n">4</span>Test des logiciels, jeu d'essai</div>
      <div class="ss-step anim d5"><span class="n">5</span>Décision</div>
      <div class="ss-step anim d6"><span class="n">6</span>Information, formation</div>
      <div class="ss-step anim d7"><span class="n">7</span>Développement, implantation</div>
    </div>
  </section>

  <section class="slide slide80 t-push" data-i="79" data-t="Poussée">
    <div class="ribbon anim"></div>
    <h2 class="anim">Analyse de l'existant</h2>
    <div class="roles">
      <div class="role-card blue anim d2">
        <div class="role-head">
          <div class="r-ico">🎯</div>
          <h3>Objectifs</h3>
        </div>
        <ul>
          <li>Identifier <b style="color:#f39c12;">comment se gère la production</b></li>
          <li>Identifier les <b>anomalies</b> (flux physiques, informations, décisions)</li>
        </ul>
        <div class="big-ico">🎯</div>
      </div>
      <div class="role-card red anim d4">
        <div class="role-head">
          <div class="r-ico">🧭</div>
          <h3>Méthodes</h3>
        </div>
        <ul>
          <li>Analyse fonctionnelle, analyse des flux, analyse des décisions (<b style="color:#e74c3c;">IDEF, GRAI</b>…)</li>
          <li>Recours à un <b>conseil extérieur</b> (subventions pour PMI via la DRIRE)</li>
        </ul>
        <div class="big-ico">🧭</div>
      </div>
    </div>
  </section>

  <section class="slide slide81 t-blur" data-i="80" data-t="Flou">
    <div class="ribbon anim"></div>
    <h2 class="anim">Expression des besoins</h2>
    <div class="roles">
      <div class="role-card blue anim d2">
        <div class="role-head">
          <div class="r-ico">🎯</div>
          <h3>Objectifs</h3>
        </div>
        <ul>
          <li>Définir le <b style="color:#f39c12;">cahier des charges</b></li>
        </ul>
        <div class="big-ico">🎯</div>
      </div>
      <div class="role-card red anim d4">
        <div class="role-head">
          <div class="r-ico">📋</div>
          <h3>Résultats</h3>
        </div>
        <ul>
          <li><b>Objectifs</b> (niveau de performance désiré)</li>
          <li><b>Conditions de maintenance</b></li>
          <li><b style="color:#e74c3c;">Évolution</b> du produit</li>
          <li>Relation entre le produit et les autres (<b style="color:#e74c3c;">comptabilité</b> par exemple)</li>
        </ul>
        <div class="big-ico">📋</div>
      </div>
    </div>
  </section>

  <section class="slide slide82 t-rotate" data-i="81" data-t="Rotation">
    <div class="ribbon anim"></div>
    <h2 class="anim">Développement interne ou achat&nbsp;?</h2>
    <p class="ss-intro anim d1">🎯 Décider <b style="color:#f39c12;">l'achat d'un progiciel</b> ou <b style="color:#f39c12;">le développement d'un logiciel</b> — comparaison&nbsp;:</p>
    <table class="ss-tbl anim d2" style="width:74%;">
      <tr><th>Critère</th><th>Progiciel</th><th>Logiciel</th></tr>
      <tr><td>Adaptation au besoin</td><td class="c">=</td><td class="c" style="color:#7cd0ff;">+&nbsp;?</td></tr>
      <tr class="alt"><td>Modification organisation</td><td class="c" style="color:#7cd0ff;">+</td><td class="c">=&nbsp;?</td></tr>
      <tr><td>Délai de livraison</td><td class="c" style="color:#7cd0ff;">+</td><td class="c" style="color:#ff9b8a;">−</td></tr>
      <tr class="alt"><td>Prix</td><td class="c" style="color:#7cd0ff;">+</td><td class="c" style="color:#ff9b8a;">−</td></tr>
      <tr><td>Maintenance</td><td class="c" style="color:#7cd0ff;">+</td><td class="c" style="color:#ff9b8a;">−</td></tr>
      <tr class="alt"><td>Évolution</td><td class="c" style="color:#7cd0ff;">+</td><td class="c" style="color:#ff9b8a;">−</td></tr>
    </table>
    <p class="ss-note anim d4">🟦 + = point fort du progiciel (acheté) • les logiciels internes s'adaptent mieux au besoin</p>
  </section>

  <section class="slide slide83 t-zoom" data-i="82" data-t="Zoom">
    <div class="ribbon anim"></div>
    <h2 class="anim">Test des logiciels et jeu d'essai</h2>
    <div class="roles">
      <div class="role-card blue anim d2">
        <div class="role-head">
          <div class="r-ico">🎯</div>
          <h3>Objectifs</h3>
        </div>
        <ul>
          <li>Valider l'<b style="color:#f39c12;">adéquation de la solution</b> à l'entreprise</li>
        </ul>
        <div class="big-ico">🎯</div>
      </div>
      <div class="role-card red anim d4">
        <div class="role-head">
          <div class="r-ico">🧪</div>
          <h3>Méthode</h3>
        </div>
        <ul>
          <li>Le <b style="color:#e74c3c;">jeu d'essai</b> doit être <b>représentatif</b> de l'entreprise (type de gamme, de ressources, de produits…) et des <b>volumes d'information</b> à traiter</li>
          <li>Le test doit <b style="color:#e74c3c;">valider le progiciel</b> par rapport aux attentes</li>
        </ul>
        <div class="big-ico">🧪</div>
      </div>
    </div>
  </section>

  <section class="slide slide84 t-insert" data-i="83" data-t="Insertion">
    <div class="ribbon anim"></div>
    <h2 class="anim">Choix</h2>
    <div class="roles">
      <div class="role-card blue anim d2">
        <div class="role-head">
          <div class="r-ico">🎯</div>
          <h3>Objectifs</h3>
        </div>
        <ul>
          <li>Retenir la solution (<b style="color:#f39c12;">1 progiciel</b> parmi une liste) ou valider un <b style="color:#f39c12;">logiciel</b></li>
        </ul>
        <div class="big-ico">🎯</div>
      </div>
      <div class="role-card red anim d4">
        <div class="role-head">
          <div class="r-ico">👥</div>
          <h3>Méthode</h3>
        </div>
        <ul>
          <li>L'ensemble des <b style="color:#e74c3c;">personnes concernées</b> doit être consulté&nbsp;:</li>
          <li>utilisateurs, direction, service informatique, service formation…</li>
        </ul>
        <div class="big-ico">👥</div>
      </div>
    </div>
  </section>

  <section class="slide slide85 t-rise" data-i="84" data-t="Ascension">
    <div class="ribbon anim"></div>
    <h2 class="anim">Information, formation</h2>
    <div class="roles">
      <div class="role-card blue anim d2">
        <div class="role-head">
          <div class="r-ico">🎯</div>
          <h3>Objectifs</h3>
        </div>
        <ul>
          <li><b style="color:#f39c12;">Impliquer chacun</b> dans le projet</li>
          <li>Ne pas laisser se créer une différence entre les <b>"initiés"</b> et les autres</li>
        </ul>
        <div class="big-ico">🎯</div>
      </div>
      <div class="role-card red anim d4">
        <div class="role-head">
          <div class="r-ico">🎓</div>
          <h3>Méthode</h3>
        </div>
        <ul>
          <li><b style="color:#e74c3c;">Information dès le début</b> de l'ensemble du personnel</li>
          <li>Formation aux <b>concepts de gestion de production</b>, au <b>logiciel</b> et éventuellement aux <b>méthodes d'analyse</b></li>
        </ul>
        <div class="big-ico">🎓</div>
      </div>
    </div>
  </section>

  <section class="slide slide86 t-up" data-i="85" data-t="Verticale">
    <div class="ribbon anim"></div>
    <h2 class="anim">Développement, implantation</h2>
    <div class="roles">
      <div class="role-card blue anim d2">
        <div class="role-head">
          <div class="r-ico">🎯</div>
          <h3>Objectifs</h3>
        </div>
        <ul>
          <li><b style="color:#f39c12;">Préparer les données</b> pour faciliter leur saisie</li>
        </ul>
        <div class="big-ico">🎯</div>
      </div>
      <div class="role-card red anim d4">
        <div class="role-head">
          <div class="r-ico">🛠️</div>
          <h3>Méthode</h3>
        </div>
        <ul>
          <li>Mettre en place la <b style="color:#e74c3c;">nouvelle organisation avant l'informatisation</b> (séparer les problèmes d'organisation des problèmes informatiques)</li>
          <li>Mettre en place d'abord une <b>application simple</b> rendant le <b style="color:#e74c3c;">maximum de service</b> aux utilisateurs</li>
        </ul>
        <div class="big-ico">🛠️</div>
      </div>
    </div>
  </section>

  <section class="slide slide87 t-push" data-i="86" data-t="Poussée">
    <div class="ribbon anim"></div>
    <h2 class="anim">Difficultés d'implantation</h2>
    <div class="def-grid">
      <div class="def-item anim d1"><div class="d-ico">👥</div><div class="d-txt"><b style="color:#f39c12;">Problèmes humains</b> — peur de l'informatique • remise en cause des rôles et des "pouvoirs" sur l'information • obligation de clarifier les responsabilités</div></div>
      <div class="def-item anim d2"><div class="d-ico">⏳</div><div class="d-txt"><b>Problèmes de délais</b> — retard de mise en place donc <b style="color:#e74c3c;">risque de démotivation</b></div></div>
      <div class="def-item anim d3" style="border-left-color:#e74c3c;"><div class="d-ico">📊</div><div class="d-txt"><b style="color:#e74c3c;">Problèmes de données</b> — attention au <b style="color:#e74c3c;">temps de saisie et de mise à jour&nbsp;!</b></div></div>
    </div>
  </section>

  <section class="slide slide88 t-blur" data-i="87" data-t="Flou">
    <div class="ribbon anim"></div>
    <h2 class="anim">ERP : Enterprise Resource Planning</h2>
    <div class="roles">
      <div class="role-card blue anim d2">
        <div class="role-head">
          <div class="r-ico">🏢</div>
          <h3>Définition</h3>
        </div>
        <ul>
          <li>Système <b style="color:#f39c12;">intégrant les différentes applications spécifiques</b> séparées</li>
          <li>Coût élevé : <b style="color:#f39c12;">plusieurs millions d'euros</b></li>
        </ul>
        <div class="big-ico">🏢</div>
      </div>
      <div class="role-card red anim d4">
        <div class="role-head">
          <div class="r-ico">✨</div>
          <h3>Caractéristiques</h3>
        </div>
        <ul>
          <li><b style="color:#e74c3c;">Base de données unique</b> (saisie unique)</li>
          <li><b style="color:#e74c3c;">Interface utilisateur unique</b></li>
          <li><b>Uniformité des règles de gestion</b></li>
          <li><b>Outils d'analyse</b> (Executive Information Systems, reporting)</li>
        </ul>
        <div class="big-ico">✨</div>
      </div>
    </div>
  </section>

  <section class="slide slide89 t-rotate" data-i="88" data-t="Rotation">
    <div class="ribbon anim"></div>
    <h2 class="anim">Structure d'un ERP</h2>
    <div class="ss-img anim d1"><img src="assets/assets_ss_image59.png" alt="Structure d'un ERP — base de données centrale reliée aux modules de gestion"></div>
    <p class="ss-note anim d3">Chaque module s'appuie sur la <b style="color:#f39c12;">base de données centrale unique</b></p>
  </section>

  <section class="slide slide90 t-zoom" data-i="89" data-t="Zoom">
    <div class="ribbon anim"></div>
    <h2 class="anim">Principaux progiciels dont ERP (PGI)</h2>
    <div class="def-grid">
      <div class="def-item anim d1"><div class="d-ico">🌍</div><div class="d-txt"><b style="color:#f39c12;">ERP généralistes</b> — SAP R/3, PeopleSoft, Oracle Applications, JD Edwards, Intentia</div></div>
      <div class="def-item anim d2"><div class="d-ico">🧪</div><div class="d-txt"><b>Agro-alimentaire / chimie</b> — Marcam Protean, Ross System Renaissance</div></div>
      <div class="def-item anim d3"><div class="d-ico">🚦</div><div class="d-txt"><b>Ordonnancement</b> — Dullin Ortems, Ouroumoff Préactor, Ordo</div></div>
      <div class="def-item anim d4" style="border-left-color:#e74c3c;"><div class="d-ico">🌊</div><div class="d-txt"><b style="color:#e74c3c;">Simulation de flux</b> — Serete Industries Witness, Log'in Cadence</div></div>
    </div>
  </section>

  <section class="slide slide91 t-insert" data-i="90" data-t="Insertion">
    <div class="ribbon anim"></div>
    <h2 class="anim">SAP R/3 : le plus diffusé</h2>
    <div class="ss-mods">
      <div class="ss-mod anim d1"><b>SD</b>Sales and Distribution</div>
      <div class="ss-mod anim d1"><b>MM</b>Materials Management</div>
      <div class="ss-mod anim d1"><b>PP</b>Production Planning</div>
      <div class="ss-mod anim d1"><b>QM</b>Quality Management</div>
      <div class="ss-mod anim d2"><b>PM</b>Plant Maintenance</div>
      <div class="ss-mod anim d2"><b>HR</b>Human Resources</div>
      <div class="ss-mod anim d2"><b>FI</b>Finance</div>
      <div class="ss-mod anim d2"><b>CO</b>Contrôle de gestion</div>
      <div class="ss-mod anim d3"><b>AM</b>Immobilisations</div>
      <div class="ss-mod anim d3"><b>PS</b>Gestion de projets</div>
      <div class="ss-mod anim d3"><b>WF</b>Workflow</div>
      <div class="ss-mod anim d3"><b>IS</b>Solutions métier</div>
    </div>
  </section>

  <section class="slide slide92 t-rise" data-i="91" data-t="Ascension">
    <div class="ribbon anim"></div>
    <h2 class="anim">Gestion commerciale — Module SD</h2>
    <div class="roles">
      <div class="role-card blue anim d2">
        <div class="role-head">
          <div class="r-ico">🛒</div>
          <h3>Sales and Distribution — fonctions</h3>
        </div>
        <ul>
          <li>Gestion des <b style="color:#f39c12;">prospects et clients</b></li>
          <li><b style="color:#f39c12;">Prévisions</b> moyen et court termes</li>
          <li><b>Saisie des commandes</b></li>
          <li>Détermination des <b style="color:#f39c12;">prix</b></li>
          <li><b>Facturation</b></li>
        </ul>
        <div class="big-ico">🛒</div>
      </div>
      <div class="role-card red anim d4">
        <div class="role-head">
          <div class="r-ico">🚚</div>
          <h3>Disponibilité &amp; transports</h3>
        </div>
        <ul>
          <li>Détermination de la <b style="color:#e74c3c;">disponibilité à la vente</b> (en conjonction avec les modules achat et production)</li>
          <li><b style="color:#e74c3c;">Planification des transports</b></li>
        </ul>
        <div class="big-ico">🚚</div>
      </div>
    </div>
  </section>

  <section class="slide slide93 t-up" data-i="92" data-t="Verticale">
    <div class="ribbon anim"></div>
    <h2 class="anim">Gestion des achats et des stocks — Module MM</h2>
    <div class="roles">
      <div class="role-card blue anim d2">
        <div class="role-head">
          <div class="r-ico">📦</div>
          <h3>Stocks &amp; produits finis</h3>
        </div>
        <ul>
          <li><b style="color:#f39c12;">Suivi des stocks</b> (valeur, quantité)</li>
          <li><b style="color:#f39c12;">Suivi des produits finis</b> (en lien avec la gestion commerciale)</li>
        </ul>
        <div class="big-ico">📦</div>
      </div>
      <div class="role-card red anim d4">
        <div class="role-head">
          <div class="r-ico">🛒</div>
          <h3>Achats &amp; magasins</h3>
        </div>
        <ul>
          <li><b>Matérial Management</b> — définition des <b style="color:#e74c3c;">demandes d'achats</b></li>
          <li><b style="color:#e74c3c;">Gestion des achats</b> (comparaison de fournisseurs)</li>
          <li><b>Gestion des magasins</b></li>
        </ul>
        <div class="big-ico">🛒</div>
      </div>
    </div>
  </section>

  <section class="slide slide94 t-push" data-i="93" data-t="Poussée">
    <div class="ribbon anim"></div>
    <h2 class="anim">Gestion de la production — Module PP</h2>
    <div class="def-grid">
      <div class="def-item anim d1"><div class="d-ico">📆</div><div class="d-txt"><b style="color:#f39c12;">Plan Industriel et Commercial</b></div></div>
      <div class="def-item anim d2"><div class="d-ico">📆</div><div class="d-txt"><b>Plan Directeur de Production</b></div></div>
      <div class="def-item anim d3"><div class="d-ico">🧮</div><div class="d-txt"><b style="color:#f39c12;">Calcul des Besoins</b> (MRP)</div></div>
      <div class="def-item anim d4"><div class="d-ico">📊</div><div class="d-txt"><b>Plan de charge</b></div></div>
      <div class="def-item anim d5" style="border-left-color:#e74c3c;"><div class="d-ico">🌊</div><div class="d-txt"><b style="color:#e74c3c;">Gestion des flux</b> (OF, Kanban…)</div></div>
    </div>
  </section>

  <section class="slide slide95 t-blur" data-i="94" data-t="Flou">
    <div class="ribbon anim"></div>
    <h2 class="anim">Gestion de la qualité — Module QM</h2>
    <div class="def-grid">
      <div class="def-item anim d1"><div class="d-ico">✅</div><div class="d-txt"><b style="color:#f39c12;">Réception fournisseurs</b></div></div>
      <div class="def-item anim d2"><div class="d-ico">⚠️</div><div class="d-txt"><b style="color:#e74c3c;">Incidents qualité</b></div></div>
      <div class="def-item anim d3"><div class="d-ico">🗑️</div><div class="d-txt"><b style="color:#e74c3c;">Rebuts</b></div></div>
      <div class="def-item anim d4"><div class="d-ico">📞</div><div class="d-txt"><b>Réclamation clients</b></div></div>
      <div class="def-item anim d5"><div class="d-ico">🔍</div><div class="d-txt"><b style="color:#f39c12;">Suivi de la conformité</b></div></div>
      <div class="def-item anim d6"><div class="d-ico">📈</div><div class="d-txt"><b style="color:#f39c12;">SPC et carte de contrôle</b></div></div>
    </div>
  </section>

  <section class="slide slide96 t-rotate" data-i="95" data-t="Rotation">
    <div class="ribbon anim"></div>
    <h2 class="anim">Gestion de la maintenance — Module PM</h2>
    <div class="def-grid">
      <div class="def-item anim d1"><div class="d-ico">🔧</div><div class="d-txt"><b style="color:#f39c12;">Description des ressources techniques</b></div></div>
      <div class="def-item anim d2"><div class="d-ico">💸</div><div class="d-txt"><b>Suivi des réparations</b> (coûts)</div></div>
      <div class="def-item anim d3" style="border-left-color:#e74c3c;"><div class="d-ico">🗓️</div><div class="d-txt"><b style="color:#e74c3c;">Planification de la maintenance préventive</b></div></div>
    </div>
  </section>

  <section class="slide slide97 t-zoom" data-i="96" data-t="Zoom">
    <div class="ribbon anim"></div>
    <h2 class="anim">Gestion des données techniques</h2>
    <div class="def-grid">
      <div class="def-item anim d1"><div class="d-ico">📦</div><div class="d-txt"><b style="color:#f39c12;">Articles</b> — chaque article est référencé et géré (description, règles de gestion, données comptables)</div></div>
      <div class="def-item anim d2"><div class="d-ico">🌳</div><div class="d-txt"><b>Nomenclatures</b> — font les liens entre articles (composant / composé)</div></div>
      <div class="def-item anim d3" style="border-left-color:#e74c3c;"><div class="d-ico">⚙️</div><div class="d-txt"><b style="color:#f39c12;">Postes de charge</b> — ensembles de ressources permettant de réaliser les mêmes opérations (mêmes coûts)</div></div>
    </div>
  </section>

  <section class="slide slide98 t-rise" data-i="97" data-t="Ascension">
    <div class="particles">
      <span style="left:8%; animation-delay:0s;"></span><span style="left:18%; animation-delay:1s;"></span>
      <span style="left:30%; animation-delay:2s;"></span><span style="left:44%; animation-delay:3s;"></span>
      <span style="left:58%; animation-delay:4s;"></span><span style="left:70%; animation-delay:5s;"></span>
      <span style="left:82%; animation-delay:6s;"></span><span style="left:92%; animation-delay:7s;"></span>
    </div>
    <h2 class="anim" style="font-size:4.5vw;">Chapitre 3</h2>
    <h2 class="anim d2" style="font-size:4.5vw; font-weight:900;">Gestion des stocks</h2>
    <div class="picto anim d3">📦</div>
  </section>

  <section class="slide slide99 t-up" data-i="98" data-t="Verticale">
    <div class="ribbon anim"></div>
    <h2 class="anim">Utilité des stocks</h2>
    <div class="def-grid">
      <div class="def-item anim d1"><div class="d-ico">⚡</div><div class="d-txt"><b style="color:#f39c12;">Cadence</b> — faire face à une différence entre la cadence de consommation et la cadence de production (anticipation de la production)</div></div>
      <div class="def-item anim d2"><div class="d-ico">🛡️</div><div class="d-txt"><b>Protection</b> — face aux incertitudes</div></div>
      <div class="def-item anim d3" style="border-left-color:#e74c3c;"><div class="d-ico">🔗</div><div class="d-txt"><b style="color:#e74c3c;">Découplage</b> — entre les opérations</div></div>
    </div>
  </section>

  <section class="slide slide100 t-push" data-i="99" data-t="Poussée">
    <div class="ribbon anim"></div>
    <h2 class="anim">Natures des stocks</h2>
    <div class="def-grid">
      <div class="def-item anim d1"><div class="d-ico">🧱</div><div class="d-txt"><b style="color:#f39c12;">Matières premières</b></div></div>
      <div class="def-item anim d2"><div class="d-ico">🛢️</div><div class="d-txt"><b>Matières consommables</b></div></div>
      <div class="def-item anim d3"><div class="d-ico">⚙️</div><div class="d-txt"><b style="color:#f39c12;">En-cours</b></div></div>
      <div class="def-item anim d4" style="border-left-color:#e74c3c;"><div class="d-ico">📦</div><div class="d-txt"><b style="color:#e74c3c;">Produits finis</b></div></div>
    </div>
  </section>
"""

def main():
    with open(PATH, encoding="utf-8") as f:
        html = f.read()

    before = len(re.findall(r'<section class="slide', html))
    assert before == 70, f"attendu 70 slides, trouve {before}"

    # 1) CSS
    assert html.count("</style>") == 1
    html = html.replace("</style>", CSS + "</style>")

    # 2) insertion des slides apres la derniere (data-i="69")
    m = re.search(r'(<section class="slide[^"]*" data-i="69"[\s\S]*?</section>)(\s*</div>)', html)
    assert m, "point d'insertion introuvable"
    html = html[:m.end(1)] + NEW.rstrip("\n\n") + "\n" + html[m.start(2):]

    # 3) compteur statique
    html = html.replace('<span id="tot">70</span>', '<span id="tot">100</span>')

    after = len(re.findall(r'<section class="slide', html))
    assert after == 100, f"attendu 100 slides apres insertion, trouve {after}"

    with open(PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(html)
    print(f"OK : 70 -> {after} slides ; compteur 100")

if __name__ == "__main__":
    main()

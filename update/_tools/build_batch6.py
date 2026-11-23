# -*- coding: utf-8 -*-
"""Batch 6 : slides source 141-180 -> slides 171-210 du diaporama.

Chapitre Juste a Temps (fin) : SMED (objectif, principe, demarche, exemples),
maintenance (disponibilite, types, politique), approvisionnements,
conclusion JAT.
Chapitre Logistique (intercalaire 179) : distribution physique, entreposage,
reseaux de distribution, DRP, affectation usines-depots, SCM, supply chain,
concepts, transports (route, fer, voie navigable, maritime, aerien), choix
du mode de transport.
2 images originales recardees : assets_ss_image155.png (reseaux de
distribution), assets_ss_image166.png (entreprise elargie).
1 intercalaire rouge : 179 (Logistique).
"""
import re
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

PATH = r"C:\ppt\index.html"

CSS = r"""
/* ===== Slides 171-210 (slideshare OCR) ===== */
/* Intercalaire rouge 179 */
.slide179 { background:linear-gradient(135deg,#e74c3c 0%,#c0392b 55%,#8e2418 100%); flex-direction:column; }
.slide179 h2 { color:#fff; align-self:flex-start; font-weight:900; margin-bottom:0; }
/* ===== Correctif titres slides 171-210 ===== */
.slide171, .slide172, .slide173, .slide174, .slide175, .slide176, .slide177, .slide178, .slide179, .slide180,
.slide181, .slide182, .slide183, .slide184, .slide185, .slide186, .slide187, .slide188, .slide189, .slide190,
.slide191, .slide192, .slide193, .slide194, .slide195, .slide196, .slide197, .slide198, .slide199, .slide200,
.slide201, .slide202, .slide203, .slide204, .slide205, .slide206, .slide207, .slide208, .slide209, .slide210 { flex-direction:column; }
.slide171 h2, .slide172 h2, .slide173 h2, .slide174 h2, .slide175 h2, .slide176 h2, .slide177 h2, .slide178 h2, .slide180 h2,
.slide181 h2, .slide182 h2, .slide183 h2, .slide184 h2, .slide185 h2, .slide186 h2, .slide187 h2, .slide188 h2, .slide189 h2, .slide190 h2,
.slide191 h2, .slide192 h2, .slide193 h2, .slide194 h2, .slide195 h2, .slide196 h2, .slide197 h2, .slide198 h2, .slide199 h2, .slide200 h2,
.slide201 h2, .slide202 h2, .slide203 h2, .slide204 h2, .slide205 h2, .slide206 h2, .slide207 h2, .slide208 h2, .slide209 h2, .slide210 h2 {
  font-size:3vw; color:#fff; font-weight:700; margin-bottom:.5%;
  align-self:flex-start;
}
.slide171 .ribbon, .slide172 .ribbon, .slide173 .ribbon, .slide174 .ribbon, .slide175 .ribbon, .slide176 .ribbon, .slide177 .ribbon, .slide178 .ribbon, .slide180 .ribbon,
.slide181 .ribbon, .slide182 .ribbon, .slide183 .ribbon, .slide184 .ribbon, .slide185 .ribbon, .slide186 .ribbon, .slide187 .ribbon, .slide188 .ribbon, .slide189 .ribbon, .slide190 .ribbon,
.slide191 .ribbon, .slide192 .ribbon, .slide193 .ribbon, .slide194 .ribbon, .slide195 .ribbon, .slide196 .ribbon, .slide197 .ribbon, .slide198 .ribbon, .slide199 .ribbon, .slide200 .ribbon,
.slide201 .ribbon, .slide202 .ribbon, .slide203 .ribbon, .slide204 .ribbon, .slide205 .ribbon, .slide206 .ribbon, .slide207 .ribbon, .slide208 .ribbon, .slide209 .ribbon, .slide210 .ribbon {
  width:8%; height:5px; background:linear-gradient(90deg,#f39c12,#e74c3c);
  border-radius:5px; margin-bottom:3%; align-self:flex-start;
}
/* Compactions specifiques */
.slide183 .ss-step { padding:.7% 1.6%; font-size:1.1vw; }
.slide183 .ss-steps { width:86%; }
.slide210 .ss-tbl { width:94%; font-size:1.05vw; }
.slide210 .ss-tbl td, .slide210 .ss-tbl th { padding:.8% 1%; }
"""

NEW = r"""
  <section class="slide slide171 t-blur" data-i="170" data-t="Flou">
    <div class="ribbon anim"></div>
    <h2 class="anim">Diminution des temps de reconfiguration — SMED</h2>
    <p class="ss-intro anim d1"><b style="color:#f39c12;">Single Minute Exchange of Die</b> (méthode japonaise)</p>
    <div class="roles">
      <div class="role-card blue anim d2">
        <div class="role-head">
          <div class="r-ico">🎯</div>
          <h3>Objectif</h3>
        </div>
        <ul>
          <li>Diminuer la <b style="color:#f39c12;">taille des lots</b> de production (compromis entre temps de reconfiguration et coût de stockage)</li>
        </ul>
        <div class="big-ico">🎯</div>
      </div>
      <div class="role-card red anim d4">
        <div class="role-head">
          <div class="r-ico">⚙️</div>
          <h3>Principe</h3>
        </div>
        <ul>
          <li><b style="color:#f39c12;">Transférer</b> les opérations réalisées à l'<b style="color:#e74c3c;">arrêt</b> de la machine pour les réaliser <b style="color:#f39c12;">en fonctionnement</b></li>
          <li>Limiter celles <b style="color:#e74c3c;">en fonctionnement</b></li>
        </ul>
        <div class="big-ico">⚙️</div>
      </div>
    </div>
  </section>

  <section class="slide slide172 t-rotate" data-i="171" data-t="Rotation">
    <div class="ribbon anim"></div>
    <h2 class="anim">SMED (2) — la démarche</h2>
    <div class="def-grid">
      <div class="def-item anim d1"><div class="d-ico">🔍</div><div class="d-txt"><b style="color:#f39c12;">Identification</b> des opérations internes (arrêt) et externes (en fonctionnement)</div></div>
      <div class="def-item anim d2"><div class="d-ico">🔄</div><div class="d-txt"><b>Transformation</b> des opérations internes en opérations externes (ou suppression)</div></div>
      <div class="def-item anim d3"><div class="d-ico">📏</div><div class="d-txt"><b style="color:#f39c12;">Standardisation</b> des fonctions (limiter les réglages)</div></div>
      <div class="def-item anim d4"><div class="d-ico">🔩</div><div class="d-txt"><b style="color:#f39c12;">Serrages fonctionnels</b> (1 seul pas)</div></div>
      <div class="def-item anim d5"><div class="d-ico">🧍</div><div class="d-txt"><b style="color:#f39c12;">Synchronisation</b> des tâches (1 opérateur pour plusieurs machines)</div></div>
      <div class="def-item anim d6"><div class="d-ico">🚫</div><div class="d-txt"><b style="color:#e74c3c;">Suppression des réglages</b> (pré-réglé) • <b style="color:#e74c3c;">mécanisation</b></div></div>
    </div>
  </section>

  <section class="slide slide173 t-zoom" data-i="172" data-t="Zoom">
    <div class="ribbon anim"></div>
    <h2 class="anim">SMED (3) — exemples</h2>
    <div class="roles">
      <div class="role-card blue anim d2">
        <div class="role-head">
          <div class="r-ico">🛠️</div>
          <h3>Outillage d'alésage</h3>
        </div>
        <ul>
          <li>Temps de reconfiguration avant SMED&nbsp;: <b style="color:#e74c3c;">8 heures</b></li>
          <li>Temps après SMED (1 an projet)&nbsp;: <b style="color:#f39c12;">3 minutes</b></li>
        </ul>
        <div class="big-ico">🛠️</div>
      </div>
      <div class="role-card red anim d4">
        <div class="role-head">
          <div class="r-ico">🧱</div>
          <h3>Moulage plastique</h3>
        </div>
        <ul>
          <li>Temps de reconfiguration avant SMED&nbsp;: <b style="color:#e74c3c;">2 heures</b></li>
          <li>Temps après SMED (10 keuro)&nbsp;: <b style="color:#f39c12;">15 minutes</b></li>
        </ul>
        <div class="big-ico">🧱</div>
      </div>
    </div>
  </section>

  <section class="slide slide174 t-insert" data-i="173" data-t="Insertion">
    <div class="ribbon anim"></div>
    <h2 class="anim">Amélioration de la disponibilité des RT — maintenance</h2>
    <div class="roles">
      <div class="role-card blue anim d2">
        <div class="role-head">
          <div class="r-ico">📶</div>
          <h3>Disponibilité</h3>
        </div>
        <ul>
          <li><b style="color:#f39c12;">Taux de panne</b> (robustesse, fiabilité)</li>
          <li><b style="color:#f39c12;">Durée des pannes</b> (maintenabilité)</li>
        </ul>
        <div class="big-ico">📶</div>
      </div>
      <div class="role-card red anim d4">
        <div class="role-head">
          <div class="r-ico">🔧</div>
          <h3>Types de maintenance</h3>
        </div>
        <ul>
          <li><b style="color:#f39c12;">Préventive</b> (systématique, prédictive)</li>
          <li><b style="color:#e74c3c;">Curative</b></li>
        </ul>
        <div class="big-ico">🔧</div>
      </div>
    </div>
  </section>

  <section class="slide slide175 t-rise" data-i="174" data-t="Ascension">
    <div class="ribbon anim"></div>
    <h2 class="anim">Types de maintenance</h2>
    <div class="def-grid">
      <div class="def-item anim d1" style="border-left-color:#e74c3c;"><div class="d-ico">🩹</div><div class="d-txt"><b style="color:#e74c3c;">Curative</b> — la maintenance est réalisée quand il y a une panne</div></div>
      <div class="def-item anim d2"><div class="d-ico">🗓️</div><div class="d-txt"><b style="color:#f39c12;">Préventive systématique</b> — les pièces d'usure sont changées périodiquement (changement de courroie tous les 100&nbsp;000&nbsp;km)</div></div>
      <div class="def-item anim d3"><div class="d-ico">📡</div><div class="d-txt"><b style="color:#f39c12;">Préventive prédictive</b> — les indicateurs anticipant la panne sont mesurés (vibrations, couple)&nbsp;; la pièce n'est changée que si la panne semble proche&nbsp;!</div></div>
    </div>
  </section>

  <section class="slide slide176 t-up" data-i="175" data-t="Verticale">
    <div class="ribbon anim"></div>
    <h2 class="anim">Politique de maintenance</h2>
    <p class="ss-intro anim d1">🎯 Objectif&nbsp;: <b style="color:#f39c12;">disponibilité au moindre coût</b></p>
    <div class="def-grid">
      <div class="def-item anim d2"><div class="d-ico">👷</div><div class="d-txt"><b style="color:#f39c12;">Maintenance de premier niveau</b> par l'opérateur (responsable&nbsp;? jusqu'à quel niveau&nbsp;?)</div></div>
      <div class="def-item anim d3"><div class="d-ico">⚖️</div><div class="d-txt"><b style="color:#f39c12;">Optimisation du coût</b> de maintenance par compromis entre préventif et curatif</div></div>
      <div class="def-item anim d4"><div class="d-ico">🔬</div><div class="d-txt"><b style="color:#f39c12;">Analyse des pannes</b> pour trouver la cause (<b>AMDEC</b>&nbsp;: Analyse des Modes de Défaillance, de leurs Effets et de leur Criticité)</div></div>
    </div>
  </section>

  <section class="slide slide177 t-push" data-i="176" data-t="Poussée">
    <div class="ribbon anim"></div>
    <h2 class="anim">Amélioration des approvisionnements — fournisseurs</h2>
    <div class="def-grid">
      <div class="def-item anim d1"><div class="d-ico">✅</div><div class="d-txt"><b style="color:#f39c12;">Assurance qualité</b> — contrôle des produits par le fournisseur&nbsp;; confiance du client (validée par <b>audit fournisseurs</b>)</div></div>
      <div class="def-item anim d2"><div class="d-ico">🤝</div><div class="d-txt"><b style="color:#f39c12;">Partenariat</b> — accord de longue durée&nbsp;; possibilité pour le fournisseur d'investir (donc de limiter les coûts de production)</div></div>
      <div class="def-item anim d3"><div class="d-ico">🚚</div><div class="d-txt"><b style="color:#f39c12;">Application du JAT chez le fournisseur</b> — livraisons en faible quantité mais forte fréquence&nbsp;; simplifications administratives</div></div>
    </div>
  </section>

  <section class="slide slide178 t-blur" data-i="177" data-t="Flou">
    <div class="ribbon anim"></div>
    <h2 class="anim">Conclusion sur le Juste à Temps</h2>
    <div class="def-grid">
      <div class="def-item anim d1"><div class="d-ico">0️⃣</div><div class="d-txt"><b style="color:#f39c12;">Vers l'entreprise idéale (5 zéros)&nbsp;!</b> — démarche d'<b>amélioration continue</b></div></div>
      <div class="def-item anim d2"><div class="d-ico">🧑‍🤝‍🧑</div><div class="d-txt"><b style="color:#f39c12;">Importance des ressources humaines</b> — responsabilité, participation à l'amélioration continue (QUALITÉ), paix sociale</div></div>
      <div class="def-item anim d3"><div class="d-ico">📉</div><div class="d-txt"><b>Résultats</b> — diminution de la taille des lots, diminution des encours, réduction du cycle de production, réduction des délais de livraison, diminution des coûts de production</div></div>
    </div>
  </section>

  <section class="slide slide179 t-rotate" data-i="178" data-t="Rotation">
    <div class="particles">
      <span style="left:8%; animation-delay:0s;"></span><span style="left:18%; animation-delay:1s;"></span>
      <span style="left:30%; animation-delay:2s;"></span><span style="left:44%; animation-delay:3s;"></span>
      <span style="left:58%; animation-delay:4s;"></span><span style="left:70%; animation-delay:5s;"></span>
      <span style="left:82%; animation-delay:6s;"></span><span style="left:92%; animation-delay:7s;"></span>
    </div>
    <h2 class="anim" style="font-size:4.5vw;">Chapitre 7</h2>
    <h2 class="anim d2" style="font-size:4.5vw; font-weight:900;">Logistique</h2>
    <div class="picto anim d3">🚚</div>
  </section>

  <section class="slide slide180 t-zoom" data-i="179" data-t="Zoom">
    <div class="ribbon anim"></div>
    <h2 class="anim">Distribution physique</h2>
    <div class="roles">
      <div class="role-card blue anim d2">
        <div class="role-head">
          <div class="r-ico">🎯</div>
          <h3>Objectif</h3>
        </div>
        <ul>
          <li><b style="color:#f39c12;">Mise à disposition</b> des produits fabriqués avec des contraintes de <b style="color:#f39c12;">niveau de service</b>, de <b style="color:#f39c12;">coût</b> et de <b style="color:#f39c12;">délai</b></li>
        </ul>
        <div class="big-ico">🎯</div>
      </div>
      <div class="role-card red anim d4">
        <div class="role-head">
          <div class="r-ico">📦</div>
          <h3>Opérations</h3>
        </div>
        <ul>
          <li>Traitement des commandes • manutention • emballage</li>
          <li>Entreposage • gestion des stocks • <b style="color:#e74c3c;">transport</b></li>
        </ul>
        <div class="big-ico">📦</div>
      </div>
    </div>
  </section>

  <section class="slide slide181 t-insert" data-i="180" data-t="Insertion">
    <div class="ribbon anim"></div>
    <h2 class="anim">Distribution physique (2) — niveaux</h2>
    <div class="roles">
      <div class="role-card blue anim d2">
        <div class="role-head">
          <div class="r-ico">🧾</div>
          <h3>Niveau opérationnel</h3>
        </div>
        <ul>
          <li>Gestion des <b style="color:#f39c12;">stocks</b></li>
          <li>Définition des <b style="color:#f39c12;">tournées</b></li>
          <li>Définition des <b style="color:#f39c12;">règles de gestion</b> de l'entrepôt</li>
        </ul>
        <div class="big-ico">🧾</div>
      </div>
      <div class="role-card red anim d4">
        <div class="role-head">
          <div class="r-ico">🏗️</div>
          <h3>Niveau structurel — le réseau</h3>
        </div>
        <ul>
          <li>Nombre de <b style="color:#e74c3c;">niveaux</b> (entrepôt central, dépôt, plate-forme)</li>
          <li>Nombre d'<b style="color:#e74c3c;">établissements</b> à chaque niveau</li>
          <li><b style="color:#e74c3c;">Localisation et capacité</b> des établissements</li>
        </ul>
        <div class="big-ico">🏗️</div>
      </div>
    </div>
  </section>

  <section class="slide slide182 t-rise" data-i="181" data-t="Ascension">
    <div class="ribbon anim"></div>
    <h2 class="anim">Gestion de l'entrepôt — raisons d'existence</h2>
    <div class="def-grid">
      <div class="def-item anim d1"><div class="d-ico">🛡️</div><div class="d-txt"><b style="color:#f39c12;">Se protéger contre les aléas</b></div></div>
      <div class="def-item anim d2"><div class="d-ico">⏱️</div><div class="d-txt"><b style="color:#f39c12;">Réduction des délais</b> de livraison</div></div>
      <div class="def-item anim d3"><div class="d-ico">🧩</div><div class="d-txt"><b style="color:#f39c12;">Regroupement</b> des produits de différents fournisseurs</div></div>
    </div>
  </section>

  <section class="slide slide183 t-up" data-i="182" data-t="Verticale">
    <div class="ribbon anim"></div>
    <h2 class="anim">Gestion de l'entrepôt (2) — circuit des produits</h2>
    <div class="ss-steps">
      <div class="ss-step anim d1"><span class="n">1</span>Déchargement du moyen de transport</div>
      <div class="ss-step anim d2"><span class="n">2</span>Contrôle quantité (et qualité)</div>
      <div class="ss-step anim d3"><span class="n">3</span>Transfert jusqu'à l'emplacement défini</div>
      <div class="ss-step anim d4"><span class="n">4</span>Déclaration d'entrée (informatique)</div>
      <div class="ss-step anim d5"><span class="n">5</span>Stockage (quelques jours à quelques semaines)</div>
      <div class="ss-step anim d6"><span class="n">6</span>Préparation des commandes</div>
      <div class="ss-step anim d7"><span class="n">7</span>Contrôle, emballage</div>
      <div class="ss-step anim d8"><span class="n">8</span>Transfert jusqu'au moyen de transport</div>
    </div>
  </section>

  <section class="slide slide184 t-push" data-i="183" data-t="Poussée">
    <div class="ribbon anim"></div>
    <h2 class="anim">Gestion de l'entrepôt (3) — méthodes de stockage</h2>
    <div class="def-grid">
      <div class="def-item anim d1"><div class="d-ico">📍</div><div class="d-txt"><b style="color:#f39c12;">Stockage affecté</b> — 1 référence occupe toujours le même emplacement&nbsp;; facilité de gestion mais risque de sur-dimensionnement de l'entrepôt (faible taux de remplissage)</div></div>
      <div class="def-item anim d2"><div class="d-ico">🎲</div><div class="d-txt"><b style="color:#f39c12;">Stockage banalisé (aléatoire)</b> — une référence est affectée à un emplacement disponible&nbsp;; gestion informatisée, fort taux de remplissage</div></div>
      <div class="def-item anim d3"><div class="d-ico">🔀</div><div class="d-txt"><b style="color:#f39c12;">Stockage mixte</b></div></div>
    </div>
  </section>

  <section class="slide slide185 t-blur" data-i="184" data-t="Flou">
    <div class="ribbon anim"></div>
    <h2 class="anim">Réseaux de distribution — structure</h2>
    <div class="ss-img anim d1"><img src="assets/assets_ss_image155.png" alt="Structures de réseaux — usines vers clients, entrepôt central, dépôts locaux"></div>
  </section>

  <section class="slide slide186 t-rotate" data-i="185" data-t="Rotation">
    <div class="ribbon anim"></div>
    <h2 class="anim">Réseaux de distribution (2)</h2>
    <div class="def-grid">
      <div class="def-item anim d1"><div class="d-ico">🚛</div><div class="d-txt"><b style="color:#f39c12;">Livraison directe</b> — sans rupture de charge de l'usine au client&nbsp;; lot suffisant pour remplir un camion ou un wagon, à destination d'un même client</div></div>
      <div class="def-item anim d2"><div class="d-ico">🏢</div><div class="d-txt"><b style="color:#f39c12;">Système à un étage</b> — centralise les productions de toutes les usines pour les acheminer vers les clients d'une zone géographique (pays)</div></div>
      <div class="def-item anim d3"><div class="d-ico">🏬</div><div class="d-txt"><b style="color:#f39c12;">Système à 2 étages</b> — avec préparation des commandes au niveau central (bas de reconditionnement) ou local</div></div>
    </div>
  </section>

  <section class="slide slide187 t-zoom" data-i="186" data-t="Zoom">
    <div class="ribbon anim"></div>
    <h2 class="anim">Évolution des réseaux de distribution (1)</h2>
    <div class="def-grid">
      <div class="def-item anim d1"><div class="d-ico">⏱️</div><div class="d-txt"><b style="color:#f39c12;">Juste à Temps</b> — augmentation de la fréquence des commandes, diminution de la taille des livraisons et réduction des délais</div></div>
      <div class="def-item anim d2"><div class="d-ico">📉</div><div class="d-txt"><b style="color:#f39c12;">Réduction des coûts de stockage</b> par diminution du nombre de dépôts&nbsp;; besoins supplémentaires satisfaits par sous-traitance</div></div>
      <div class="def-item anim d3"><div class="d-ico">🏛️</div><div class="d-txt"><b style="color:#f39c12;">Entrepôt central</b> avec plates-formes d'éclatement (sans stock) pour la livraison finale</div></div>
    </div>
  </section>

  <section class="slide slide188 t-insert" data-i="187" data-t="Insertion">
    <div class="ribbon anim"></div>
    <h2 class="anim">Évolution des réseaux de distribution (2)</h2>
    <div class="def-grid">
      <div class="def-item anim d1"><div class="d-ico">🤝</div><div class="d-txt"><b style="color:#f39c12;">Sociétés de distribution physique pour compte d'autrui</b> — transport, entreposage, préparation des commandes, gestion des stocks, conditionnement, étiquetage, réapprovisionnement des linéaires des grandes surfaces&nbsp;; systèmes informatiques spécifiques</div></div>
      <div class="def-item anim d2"><div class="d-ico">🛒</div><div class="d-txt"><b style="color:#f39c12;">En grande distribution</b> — plates-formes avec stock pour produit sec&nbsp;; plates-formes sans stock pour l'alimentaire frais</div></div>
    </div>
  </section>

  <section class="slide slide189 t-rise" data-i="188" data-t="Ascension">
    <div class="ribbon anim"></div>
    <h2 class="anim">Distribution Requirements Planning (DRP)</h2>
    <p class="ss-intro anim d1">📦 Calcul des <b style="color:#f39c12;">commandes à passer par l'entrepôt central</b> par consolidation des besoins exprimés par les dépôts locaux</p>
    <p class="ss-note anim d2">Les dépôts locaux font des <b style="color:#f39c12;">prévisions de distribution</b>. En tenant compte du <b>stock initial</b>, des <b>quantités de livraison</b> et des <b>délais de livraison</b>, les dépôts définissent les commandes à passer au magasin central (<b style="color:#f39c12;">// Calcul Besoins Nets</b>)</p>
  </section>

  <section class="slide slide190 t-up" data-i="189" data-t="Verticale">
    <div class="ribbon anim"></div>
    <h2 class="anim">Affectation des usines aux dépôts</h2>
    <p class="ss-intro anim d1">Un problème classique de <b style="color:#f39c12;">recherche opérationnelle</b> pouvant être résolu par&nbsp;:</p>
    <div class="def-grid">
      <div class="def-item anim d2"><div class="d-ico">🪨</div><div class="d-txt">La méthode du <b style="color:#f39c12;">stepping stone</b></div></div>
      <div class="def-item anim d3"><div class="d-ico">📐</div><div class="d-txt">La <b style="color:#f39c12;">programmation linéaire</b> (solver Excel)</div></div>
    </div>
  </section>

  <section class="slide slide191 t-push" data-i="190" data-t="Poussée">
    <div class="ribbon anim"></div>
    <h2 class="anim">Supply Chain Management (SCM)</h2>
    <div class="def-grid">
      <div class="def-item anim d1"><div class="d-ico">🪖</div><div class="d-txt"><b style="color:#f39c12;">Logistique</b> — origine militaire puis management (Harvard, 1977)</div></div>
      <div class="def-item anim d2"><div class="d-ico">🔗</div><div class="d-txt"><b style="color:#f39c12;">Supply Chain</b> — concept apparu dans les années 1990</div></div>
      <div class="def-item anim d3"><div class="d-ico">🏆</div><div class="d-txt"><b style="color:#f39c12;">Nécessité de domination par les prix ET par la différenciation</b> — coûts, qualité, délai, flexibilité (volume et mix-produit), niveau de service, risques</div></div>
    </div>
  </section>

  <section class="slide slide192 t-blur" data-i="191" data-t="Flou">
    <div class="ribbon anim"></div>
    <h2 class="anim">Logistique — définition</h2>
    <p class="ss-note anim d1" style="font-size:1.6vw; font-style:italic;">«&nbsp;Gestion des flux de produits et d'informations depuis l'achat des matières et composants jusqu'à leur utilisation par le client, visant à satisfaire la demande finale sous contraintes de <b style="color:#f39c12; font-style:normal;">délai</b>, <b style="color:#f39c12; font-style:normal;">qualité</b> et <b style="color:#f39c12; font-style:normal;">coût</b>&nbsp;»</p>
    <div class="def-grid">
      <div class="def-item anim d2"><div class="d-ico">🗂️</div><div class="d-txt"><b style="color:#f39c12;">Planification</b>, gestion des opérations, mesure de la performance du fournisseur au client</div></div>
      <div class="def-item anim d3"><div class="d-ico">🧭</div><div class="d-txt"><b style="color:#f39c12;">Achats, approvisionnements, production, distribution physique</b></div></div>
    </div>
  </section>

  <section class="slide slide193 t-rotate" data-i="192" data-t="Rotation">
    <div class="ribbon anim"></div>
    <h2 class="anim">Supply Chain</h2>
    <p class="ss-intro anim d1">La chaîne logistique globale ou <b style="color:#f39c12;">Supply Chain</b> est une extension de la logistique…</p>
    <div class="def-grid">
      <div class="def-item anim d2"><div class="d-ico">⬅️</div><div class="d-txt">À l'<b style="color:#f39c12;">amont</b> (fournisseurs des fournisseurs) et à l'<b style="color:#f39c12;">aval</b> (clients des clients)</div></div>
      <div class="def-item anim d3"><div class="d-ico">🧩</div><div class="d-txt">À d'<b style="color:#f39c12;">autres fonctions</b>&nbsp;: conception, achat, approvisionnement, production, distribution physique, <b>soutien logistique</b>, <b>recyclage</b></div></div>
    </div>
  </section>

  <section class="slide slide194 t-zoom" data-i="193" data-t="Zoom">
    <div class="ribbon anim"></div>
    <h2 class="anim">Coût de la supply chain</h2>
    <div class="ss-fx anim d1"><b>Coût de la Supply Chain ≈ 10&nbsp;% du CA</b></div>
    <div class="def-grid">
      <div class="def-item anim d2"><div class="d-ico">📦</div><div class="d-txt">Gestion des stocks&nbsp;: <b style="color:#f39c12;">3&nbsp;%</b></div></div>
      <div class="def-item anim d3"><div class="d-ico">🖥️</div><div class="d-txt">Administration et informatique&nbsp;: <b style="color:#f39c12;">2&nbsp;%</b></div></div>
      <div class="def-item anim d4"><div class="d-ico">🏢</div><div class="d-txt">Entreposage&nbsp;: <b style="color:#f39c12;">2,5&nbsp;%</b></div></div>
      <div class="def-item anim d5"><div class="d-ico">🚚</div><div class="d-txt">Transport&nbsp;: <b style="color:#f39c12;">3&nbsp;%</b> — calcul ramené à une quantité (euros/tonne)</div></div>
    </div>
    <p class="ss-note anim d6">⚠️ Si marge faible (grande consommation)&nbsp;: <b style="color:#e74c3c;">coût supply chain &gt; marge&nbsp;!</b> → organisation logistique performante</p>
  </section>

  <section class="slide slide195 t-insert" data-i="194" data-t="Insertion">
    <div class="ribbon anim"></div>
    <h2 class="anim">Concepts de la supply chain</h2>
    <div class="def-grid">
      <div class="def-item anim d1"><div class="d-ico">🌐</div><div class="d-txt"><b style="color:#f39c12;">Vision globale</b> (entreprise élargie)</div></div>
      <div class="def-item anim d2"><div class="d-ico">👥</div><div class="d-txt"><b style="color:#f39c12;">Segmentation de la clientèle</b></div></div>
      <div class="def-item anim d3"><div class="d-ico">🎯</div><div class="d-txt"><b style="color:#f39c12;">Adaptation au besoin</b></div></div>
      <div class="def-item anim d4"><div class="d-ico">🤝</div><div class="d-txt"><b style="color:#f39c12;">Partenariat</b> fournisseurs, producteurs, distributeurs</div></div>
      <div class="def-item anim d5"><div class="d-ico">⏳</div><div class="d-txt"><b style="color:#f39c12;">Différenciation retardée</b></div></div>
    </div>
  </section>

  <section class="slide slide196 t-rise" data-i="195" data-t="Ascension">
    <div class="ribbon anim"></div>
    <h2 class="anim">Vision globale — l'entreprise élargie</h2>
    <div class="ss-img anim d1"><img src="assets/assets_ss_image166.png" alt="Entreprise élargie — chaîne d'usines et de flux clients/fournisseurs"></div>
  </section>

  <section class="slide slide197 t-up" data-i="196" data-t="Verticale">
    <div class="ribbon anim"></div>
    <h2 class="anim">Segmentation de la clientèle</h2>
    <div class="def-grid">
      <div class="def-item anim d1"><div class="d-ico">📦</div><div class="d-txt"><b style="color:#f39c12;">Volume</b> (10&nbsp;000&nbsp;T/an → 1&nbsp;kg/mois)</div></div>
      <div class="def-item anim d2"><div class="d-ico">⏱️</div><div class="d-txt"><b style="color:#f39c12;">Délai</b> (1&nbsp;h → 1&nbsp;mois)</div></div>
      <div class="def-item anim d3"><div class="d-ico">🔁</div><div class="d-txt"><b style="color:#f39c12;">Régularité</b> (tous les jours → 3 fois par an)</div></div>
      <div class="def-item anim d4"><div class="d-ico">🌍</div><div class="d-txt"><b style="color:#f39c12;">Éloignement</b> (50&nbsp;m → 8&nbsp;000&nbsp;km)</div></div>
      <div class="def-item anim d5"><div class="d-ico">⭐</div><div class="d-txt"><b style="color:#f39c12;">Niveau de service</b> (99&nbsp;% géré → 90&nbsp;%)</div></div>
      <div class="def-item anim d6"><div class="d-ico">☠️</div><div class="d-txt"><b style="color:#f39c12;">Dangerosité</b> des produits</div></div>
      <div class="def-item anim d7"><div class="d-ico">🏙️</div><div class="d-txt"><b style="color:#f39c12;">Accessibilité</b> des lieux de livraison (en ville&nbsp;?)</div></div>
    </div>
  </section>

  <section class="slide slide198 t-push" data-i="197" data-t="Poussée">
    <div class="ribbon anim"></div>
    <h2 class="anim">Adaptation au besoin</h2>
    <div class="def-grid">
      <div class="def-item anim d1"><div class="d-ico">🧾</div><div class="d-txt"><b style="color:#f39c12;">Préparation de commandes particulières</b></div></div>
      <div class="def-item anim d2"><div class="d-ico">🚚</div><div class="d-txt"><b style="color:#f39c12;">Livraisons plusieurs fois par jour</b> par palettes</div></div>
      <div class="def-item anim d3"><div class="d-ico">🛃</div><div class="d-txt"><b style="color:#f39c12;">Exportation</b> (douanes, transitaires, commissionnaires)</div></div>
      <div class="def-item anim d4"><div class="d-ico">🧊</div><div class="d-txt"><b style="color:#f39c12;">Produits frais</b> (exemple&nbsp;: SC frais différent de SC épicerie chez Nestlé France)</div></div>
    </div>
  </section>

  <section class="slide slide199 t-blur" data-i="198" data-t="Flou">
    <div class="ribbon anim"></div>
    <h2 class="anim">Partenariat fournisseurs, producteurs, distributeurs</h2>
    <div class="def-grid">
      <div class="def-item anim d1"><div class="d-ico">📊</div><div class="d-txt"><b style="color:#f39c12;">Prévisions communes</b> des ventes</div></div>
      <div class="def-item anim d2"><div class="d-ico">✏️</div><div class="d-txt"><b style="color:#f39c12;">Conception commune</b> des produits</div></div>
      <div class="def-item anim d3"><div class="d-ico">🔗</div><div class="d-txt"><b style="color:#f39c12;">Conception commune de la chaîne logistique</b> (zones de stockage)</div></div>
      <div class="def-item anim d4"><div class="d-ico">💰</div><div class="d-txt"><b style="color:#f39c12;">Amélioration conjointe des coûts</b></div></div>
      <div class="def-item anim d5"><div class="d-ico">🛍️</div><div class="d-txt"><b style="color:#f39c12;">Développement de la fonction ACHATS</b></div></div>
    </div>
  </section>

  <section class="slide slide200 t-rotate" data-i="199" data-t="Rotation">
    <div class="ribbon anim"></div>
    <h2 class="anim">Flux d'informations</h2>
    <div class="def-grid">
      <div class="def-item anim d1"><div class="d-ico">🖥️</div><div class="d-txt"><b style="color:#f39c12;">ERP communs ou communicants</b></div></div>
      <div class="def-item anim d2"><div class="d-ico">🧮</div><div class="d-txt"><b style="color:#f39c12;">APS — Advanced Planning and Scheduling Systems</b>&nbsp;: progiciels de SCM apparus vers 1995&nbsp;; optimisation de l'ensemble de la chaîne logistique (prévision de demande, planification de production, approvisionnement)</div></div>
      <div class="def-item anim d3"><div class="d-ico">🧱</div><div class="d-txt"><b style="color:#f39c12;">Couche supérieure des ERP</b>, dont ils utilisent la base de données</div></div>
      <div class="def-item anim d4"><div class="d-ico">🏷️</div><div class="d-txt">Principaux&nbsp;: <b style="color:#f39c12;">Manugistics, I2, Synquest, Numetrix</b></div></div>
    </div>
  </section>

  <section class="slide slide201 t-zoom" data-i="200" data-t="Zoom">
    <div class="ribbon anim"></div>
    <h2 class="anim">Différenciation retardée</h2>
    <div class="def-grid">
      <div class="def-item anim d1"><div class="d-ico">⏳</div><div class="d-txt"><b style="color:#f39c12;">Différenciation le plus tard possible</b> (le plus près possible du client final)</div></div>
      <div class="def-item anim d2"><div class="d-ico">📦</div><div class="d-txt"><b style="color:#f39c12;">Livraison des produits banalisés</b> qui sont personnalisés à la dernière étape</div></div>
    </div>
  </section>

  <section class="slide slide202 t-insert" data-i="201" data-t="Insertion">
    <div class="ribbon anim"></div>
    <h2 class="anim">Transports</h2>
    <div class="roles">
      <div class="role-card blue anim d2">
        <div class="role-head">
          <div class="r-ico">🚛</div>
          <h3>Indispensable pour les flux physiques</h3>
        </div>
        <ul>
          <li>Fournisseurs → <b style="color:#f39c12;">usine</b></li>
          <li><b style="color:#f39c12;">Inter-usines</b></li>
          <li>Usines → <b style="color:#f39c12;">entrepôts</b></li>
          <li>Entrepôts → <b style="color:#f39c12;">clients</b></li>
        </ul>
        <div class="big-ico">🚛</div>
      </div>
      <div class="role-card red anim d4">
        <div class="role-head">
          <div class="r-ico">⭐</div>
          <h3>Important pour la qualité de service</h3>
        </div>
        <ul>
          <li><b style="color:#e74c3c;">Retards, erreurs, pertes, casses…</b></li>
        </ul>
        <div class="big-ico">⭐</div>
      </div>
    </div>
  </section>

  <section class="slide slide203 t-rise" data-i="202" data-t="Ascension">
    <div class="ribbon anim"></div>
    <h2 class="anim">Modes de transport</h2>
    <div class="roles">
      <div class="role-card blue anim d2">
        <div class="role-head">
          <div class="r-ico">🇪🇺</div>
          <h3>Dans l'Europe</h3>
        </div>
        <ul>
          <li>Modes principaux&nbsp;: <b style="color:#f39c12;">route, fer, voies navigables</b></li>
        </ul>
        <div class="big-ico">🇪🇺</div>
      </div>
      <div class="role-card red anim d4">
        <div class="role-head">
          <div class="r-ico">🛳️</div>
          <h3>Importations / exportations de l'UE</h3>
        </div>
        <ul>
          <li>Modes principaux&nbsp;: <b style="color:#e74c3c;">transports aériens et maritimes</b></li>
        </ul>
        <div class="big-ico">🛳️</div>
      </div>
    </div>
  </section>

  <section class="slide slide204 t-up" data-i="203" data-t="Verticale">
    <div class="ribbon anim"></div>
    <h2 class="anim">La route</h2>
    <div class="def-grid">
      <div class="def-item anim d1"><div class="d-ico">🥇</div><div class="d-txt"><b style="color:#f39c12;">Première place en France et en Europe</b> — 89&nbsp;% des tonnes chargées, 75&nbsp;% des tonnes&nbsp;×&nbsp;km</div></div>
      <div class="def-item anim d2"><div class="d-ico">📏</div><div class="d-txt">59&nbsp;% sur <b style="color:#f39c12;">moins de 50&nbsp;km</b>, 79&nbsp;% à moins de 150&nbsp;km</div></div>
      <div class="def-item anim d3"><div class="d-ico">📈</div><div class="d-txt"><b style="color:#f39c12;">Croissance forte</b> — développement des messageries express&nbsp;; seul moyen pour le <b>porte à porte</b>, malgré les encombrements des réseaux</div></div>
      <div class="def-item anim d4"><div class="d-ico">🧍</div><div class="d-txt">Taille moyenne des entreprises&nbsp;: <b style="color:#f39c12;">7 personnes</b></div></div>
    </div>
  </section>

  <section class="slide slide205 t-push" data-i="204" data-t="Poussée">
    <div class="ribbon anim"></div>
    <h2 class="anim">Le fer</h2>
    <div class="def-grid">
      <div class="def-item anim d1"><div class="d-ico">🥈</div><div class="d-txt"><b style="color:#f39c12;">Deuxième place en France</b> — 27&nbsp;% des tonnes&nbsp;×&nbsp;km (52 milliards de T.km), 9&nbsp;% des tonnes transportées (144 millions de T)</div></div>
      <div class="def-item anim d2" style="border-left-color:#e74c3c;"><div class="d-ico">📉</div><div class="d-txt"><b style="color:#e74c3c;">Régulière baisse de trafic</b> — inadapté au juste à temps</div></div>
      <div class="def-item anim d3"><div class="d-ico">🚋</div><div class="d-txt">Malgré <b style="color:#f39c12;">wagons adaptés</b> à chaque type de transport, possibilité <b>«&nbsp;rail-route&nbsp;»</b> et embarquement de semi-remorques</div></div>
      <div class="def-item anim d4"><div class="d-ico">⛓️</div><div class="d-txt">Principalement&nbsp;: <b style="color:#f39c12;">minerais, produits métallurgiques, produits agricoles, denrées alimentaires, combustibles</b></div></div>
    </div>
  </section>

  <section class="slide slide206 t-blur" data-i="205" data-t="Flou">
    <div class="ribbon anim"></div>
    <h2 class="anim">Voie navigable</h2>
    <div class="def-grid">
      <div class="def-item anim d1"><div class="d-ico">📉</div><div class="d-txt"><b style="color:#f39c12;">Faible part de marché</b> — 2&nbsp;% en France (16&nbsp;% en Allemagne, 50&nbsp;% aux Pays-Bas)&nbsp;; 5 milliards de T.km (1998)</div></div>
      <div class="def-item anim d2" style="border-left-color:#e74c3c;"><div class="d-ico">📉</div><div class="d-txt"><b style="color:#e74c3c;">Trafic en baisse</b> — faible réseau, entreprises artisanales</div></div>
      <div class="def-item anim d3"><div class="d-ico">🌱</div><div class="d-txt">Malgré <b style="color:#f39c12;">tarifs faibles</b> et <b style="color:#f39c12;">écologique</b></div></div>
    </div>
  </section>

  <section class="slide slide207 t-rotate" data-i="206" data-t="Rotation">
    <div class="ribbon anim"></div>
    <h2 class="anim">Transport maritime</h2>
    <div class="def-grid">
      <div class="def-item anim d1"><div class="d-ico">📈</div><div class="d-txt"><b style="color:#f39c12;">En progression</b> — 5 milliards de T dans le monde (1998), 22&nbsp;000 milliards de T.miles nautiques (1998)</div></div>
      <div class="def-item anim d2"><div class="d-ico">🛢️</div><div class="d-txt">Principalement des <b style="color:#f39c12;">matières premières</b>&nbsp;: produits pétroliers (39&nbsp;% des T), minerais, charbon, céréales</div></div>
      <div class="def-item anim d3"><div class="d-ico">📦</div><div class="d-txt">Les marchandises (plus de valeur ajoutée) sont surtout transportées en <b style="color:#f39c12;">containers</b> (20&nbsp;% du trafic total)</div></div>
    </div>
  </section>

  <section class="slide slide208 t-zoom" data-i="207" data-t="Zoom">
    <div class="ribbon anim"></div>
    <h2 class="anim">Transport aérien</h2>
    <div class="def-grid">
      <div class="def-item anim d1"><div class="d-ico">📈</div><div class="d-txt"><b style="color:#f39c12;">Progression</b> — 83 milliards de T.km dans le monde (1995)&nbsp;; 19&nbsp;% en valeur des échanges extra-communautaires (0,9&nbsp;% en tonnage)</div></div>
      <div class="def-item anim d2"><div class="d-ico">⚡</div><div class="d-txt"><b style="color:#f39c12;">Rapide</b> — 3 jours porte à porte entre Paris et Denver, contre 26 jours par voie maritime</div></div>
      <div class="def-item anim d3" style="border-left-color:#e74c3c;"><div class="d-ico">💸</div><div class="d-txt"><b style="color:#e74c3c;">Cher</b> (2,5 à 4 fois plus cher que le transport maritime, sans intégrer les opérations terminales)</div></div>
      <div class="def-item anim d4"><div class="d-ico">✈️</div><div class="d-txt">Avions spécialisés (<b style="color:#f39c12;">100&nbsp;T sur plus de 10&nbsp;000&nbsp;km</b>)</div></div>
    </div>
  </section>

  <section class="slide slide209 t-insert" data-i="208" data-t="Insertion">
    <div class="ribbon anim"></div>
    <h2 class="anim">Choix du mode de transport</h2>
    <p class="ss-intro anim d1">Choisir un mode pour un produit et une liaison&nbsp;? <b style="color:#f39c12;">Comparaison sur le porte à porte</b> et intégration du <b style="color:#f39c12;">coût du stock</b></p>
    <div class="def-grid">
      <div class="def-item anim d2"><div class="d-ico">🚦</div><div class="d-txt"><b style="color:#f39c12;">Critères sur le mode</b> — délai, fréquence, coût, fiabilité, risques&nbsp;; protection de l'environnement&nbsp;? Quelle société&nbsp;?</div></div>
      <div class="def-item anim d3"><div class="d-ico">🧊</div><div class="d-txt"><b style="color:#f39c12;">Critères sur le produit</b> — fragilité, température de conservation, URGENCE</div></div>
    </div>
  </section>

  <section class="slide slide210 t-rise" data-i="209" data-t="Ascension">
    <div class="ribbon anim"></div>
    <h2 class="anim">Choix du mode de transport (2)</h2>
    <table class="ss-tbl anim d1">
      <tr><th></th><th>Caractéristiques</th><th>Choix pour national</th><th>Choix pour international</th></tr>
      <tr>
        <th style="text-align:left;">Approvisionnement matières premières</th>
        <td>Volumes et tonnages importants • trafics réguliers</td>
        <td><b style="color:#f39c12;">Fer, voies navigables</b></td>
        <td><b style="color:#f39c12;">Transport maritime</b> (pétroliers, vraquiers)</td>
      </tr>
      <tr class="alt">
        <th style="text-align:left;">Transport inter-usines de sous-ensembles</th>
        <td>Envois réguliers • lots de 3 à 23&nbsp;T</td>
        <td>Concurrence <b style="color:#f39c12;">fer / route</b></td>
        <td>Concurrence <b style="color:#f39c12;">fer / route</b></td>
      </tr>
      <tr>
        <th style="text-align:left;">Livraisons vers le client (ou entrepôt)</th>
        <td>Variété d'expéditions • lots du kg à la T</td>
        <td><b style="color:#f39c12;">Groupage route, groupage fer</b></td>
        <td><b style="color:#f39c12;">Transport aérien</b></td>
      </tr>
    </table>
  </section>
"""

def main():
    with open(PATH, encoding="utf-8") as f:
        html = f.read()

    before = len(re.findall(r'<section class="slide', html))
    assert before == 170, f"attendu 170 slides, trouve {before}"

    # 1) CSS
    assert html.count("</style>") == 1
    html = html.replace("</style>", CSS + "</style>")

    # 2) insertion des slides apres la derniere (data-i="169")
    m = re.search(r'(<section class="slide[^"]*" data-i="169"[\s\S]*?</section>)(\s*</div>)', html)
    assert m, "point d'insertion introuvable"
    html = html[:m.end(1)] + NEW.rstrip("\n\n") + "\n" + html[m.start(2):]

    # 3) compteur statique
    html = html.replace('<span id="tot">170</span>', '<span id="tot">210</span>')

    after = len(re.findall(r'<section class="slide', html))
    assert after == 210, f"attendu 210 slides apres insertion, trouve {after}"

    with open(PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(html)
    print(f"OK : 170 -> {after} slides ; compteur 210")

if __name__ == "__main__":
    main()

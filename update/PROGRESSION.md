# 📍 État du chantier — Ajout des 180 slides slideshare

**Mis à jour :** 2026-11-24

## ✅ Terminé — Fonds photo par chapitre (slides 32–210)

Chaque chapitre a désormais **un thème visuel de fond**, appliqué uniquement aux
slides qui n'avaient pas d'image (les slides 1–30 gardent leurs photos
d'origine, les intercalaires rouges restent rouges).

| Chapitre | Slides | Images |
|---|---|---|
| Ch2 — Planification | 32–49, 51–68 | `bg_planning_online.jpg` / `_b` (salles de contrôle, NASA) |
| Ch3 — ERP / GPAO | 70–97 | `bg_erp_online.jpg` / `_b` (data centers) |
| Ch3 — Stocks | 99–135 | `bg_stock_online.jpg` / `_b` (entrepôts, palettes) |
| Ch4 — Prévisions | 137–152 | `bg_forecast_online.jpg` / `_b` (Bourse, NYSE) |
| Ch5 — Kanban | 154–165 | `bg_kanban_online.jpg` / `_b` (murs de post-its) |
| Ch6 — JAT / lean | 167–178 | `bg_lean_online.jpg` / `_b` (lignes de robots) |
| Ch7 — Logistique | 180–210 | photos existantes (port, conteneurs, quais, entrepôt) |

- **Variations intra-chapitre** : alternance des 2 variantes toutes les 2 slides,
  cadrage cyclé (center / left / right / haut / bas) et voile sombre modulé
  (0,86 → 0,93) — la photo reste perceptible sans nuire à la lisibilité.
- Script idempotent : `update/_tools/build_backgrounds.py` (bloc
  `/* ===== FONDS PHOTO PAR CHAPITRE ===== */` inséré avant `</style>`).
- Photos libres de droits (Wikimedia Commons), recadrées 1920×1080, légèrement
  floutées + assombries. Crédits complets : `assets/BACKGROUNDS-CREDITS.md`.
- Outils : `find_backgrounds.py` (recherche + planches-contact),
  `rebuild_dirs.py` (resynchronise vignettes ↔ `candidates.json`),
  `download_chosen.py` (téléchargement + retraitement, reprise sans doublon),
  `match_bg.py` (retrouve l'origine d'un fond par empreinte dHash),
  `fix_credits.py`, `final_sheet.py` (planche de contrôle).
- Vérification **visuelle** : slides 32, 45, 60, 70, 95, 100, 130, 137, 150,
  154, 165, 167, 178, 180, 194, 210 + contrôle que 1, 20 et les intercalaires
  31 / 136 / 153 / 166 / 179 sont inchangés.

> Génération d'images par IA (MiniMax H3, Grok Imagine) **indisponible** :
> « Insufficient balance » sur le compte OpenCode Models. Toutes les images
> sont donc des photos libres téléchargées (suffixe `_online`).

## ✅ Terminé — Alignement vertical des titres

Le contenu était centré verticalement (`justify-content:center`) : les slides
peu remplies affichaient un grand vide en haut et un titre trop bas.
`update/_tools/build_title_align.py` passe 199 slides en
`justify-content:flex-start; padding-top:13vh` (exclusion slide 1 + intercalaires
3, 11, 31, 50, 69, 98, 136, 153, 166, 179), avec compactage spécifique de la
slide 194 pour que la note reste au-dessus du compteur.

## Objectif global

Ajouter les **180 slides** de `slidsahre-file.pptx` (chaque slide = une image PNG,
texte récupéré par OCR) **à la suite** de la présentation actuelle
(`index.html`, 30 slides issues de `gp.pptx`).

## ✅ Terminé — Tranche 6 : slides source 141 → 180 (slides 171–210)

| Slide source | Slide présentation | Contenu | Mise en page |
|---|---|---|---|
| 141 | 171 | SMED — objectif et principe | roles 2 cartes (🎯 objectif / ⚙️ principe) |
| 142 | 172 | SMED (2) — démarche | def-grid 6 |
| 143 | 173 | SMED (3) — exemples | roles 2 cartes (alésage 8 h→3 min / moulage 2 h→15 min) |
| 144 | 174 | Maintenance — disponibilité des RT | roles 2 cartes |
| 145 | 175 | Types de maintenance | def-grid 3 (curative / préventive systématique / prédictive) |
| 146 | 176 | Politique de maintenance | intro + def-grid 3 (AMDEC) |
| 147 | 177 | Approvisionnements — fournisseurs | def-grid 3 |
| 148 | 178 | Conclusion Juste à Temps | def-grid 3 (5 zéros, RH, résultats) |
| 149 | 179 | Chapitre 7 — Logistique | intercalaire rouge + particules + picto 🚚 |
| 150 | 180 | Distribution physique | roles 2 cartes |
| 151 | 181 | Distribution physique (2) — niveaux | roles 2 cartes (opérationnel / structurel) |
| 152 | 182 | Gestion de l'entrepôt — raisons | def-grid 3 |
| 153 | 183 | Gestion de l'entrepôt (2) — circuit | **steps CSS** 8 étapes (`.ss-steps`) |
| 154 | 184 | Gestion de l'entrepôt (3) — stockage | def-grid 3 (affecté / banalisé / mixte) |
| 155 | 185 | Réseaux de distribution — structure | **image originale** (`assets_ss_image155.png`, schéma usines→clients) |
| 156 | 186 | Réseaux de distribution (2) | def-grid 3 (direct / 1 étage / 2 étages) |
| 157 | 187 | Évolution des réseaux (1) | def-grid 3 |
| 158 | 188 | Évolution des réseaux (2) | def-grid 2 |
| 159 | 189 | DRP | intro + note (calcul des besoins nets) |
| 160 | 190 | Affectation usines → dépôts | intro + def-grid 2 (stepping stone / PL) |
| 161 | 191 | Supply Chain Management (SCM) | def-grid 3 |
| 162 | 192 | Logistique — définition | note citation + def-grid 2 |
| 163 | 193 | Supply Chain | intro + def-grid 2 |
| 164 | 194 | Coût de la supply chain | formule encadrée + def-grid 4 + note (≈10 % du CA) |
| 165 | 195 | Concepts de la supply chain | def-grid 5 |
| 166 | 196 | Vision globale — entreprise élargie | **image originale** (`assets_ss_image166.png`, chaîne d'usines) |
| 167 | 197 | Segmentation de la clientèle | def-grid 7 |
| 168 | 198 | Adaptation au besoin | def-grid 4 |
| 169 | 199 | Partenariat fournisseurs/producteurs/distributeurs | def-grid 5 |
| 170 | 200 | Flux d'informations | def-grid 4 (ERP, APS…) |
| 171 | 201 | Différenciation retardée | def-grid 2 |
| 172 | 202 | Transports | roles 2 cartes |
| 173 | 203 | Modes de transport | roles 2 cartes (Europe / import-export) |
| 174 | 204 | La route | def-grid 4 |
| 175 | 205 | Le fer | def-grid 4 |
| 176 | 206 | Voie navigable | def-grid 3 |
| 177 | 207 | Transport maritime | def-grid 3 |
| 178 | 208 | Transport aérien | def-grid 4 |
| 179 | 209 | Choix du mode de transport | intro + def-grid 2 (mode / produit) |
| 180 | 210 | Choix du mode (2) — tableau | **table HTML** 3 lignes × 4 colonnes (national / international) |

Compteur : **210 slides**. 2 recadrages ajoutés (`assets_ss_image155.png`,
`assets_ss_image166.png` — ce dernier en crop PIL direct, le bbox auto de
`crop_slide.py` masquait l'usine en bas à droite). Compactages spécifiques
slides 183 (8 étapes) et 210 (tableau). Correctif titres `.slide171…210` — voir
le bloc `/* ===== Slides 171-210 (slideshare OCR) =====` dans index.html.
Vérification **visuelle** des 40 slides. Rien n'a été publié sur GitHub.

## ✅ Terminé — Tranche 5 : slides source 101 → 140 (slides 131–170)

| Slide source | Slide présentation | Contenu | Mise en page |
|---|---|---|---|
| 101 | 131 | Valorisation du stock | roles 2 cartes |
| 102 | 132 | Méthodes de valorisation | def-grid |
| 103 | 133 | FIFO | schéma CSS flux entrées/sorties |
| 104 | 134 | LIFO | schéma CSS flux entrées/sorties |
| 105 | 135 | Conclusion gestion des stocks | def-grid |
| 106 | 136 | Chapitre 4 — Prévisions | intercalaire rouge + picto 📈 |
| 107 | 137 | Prévisions — objectif | roles 2 cartes |
| 108 | 138 | Types de prévisions | def-grid |
| 109 | 139 | Prévisions et objectifs | **image originale** (`assets_ss_image109.png`) |
| 110 | 140 | Prévisions et objectifs (2) — exemple | **image originale** (`assets_ss_image110.png`) |
| 111 | 141 | Qui prévoit ? | comparaison 2 colonnes |
| 112 | 142 | Méthode de prévision | **steps CSS** (`.ss-steps`) |
| 113 | 143 | Données initiales | roles 2 cartes |
| 114 | 144 | Évolutions courantes — constante/tendance | **2 images originales** (`image114a/b`) |
| 115 | 145 | Évolutions courantes (2) — saisonnière/saut | **2 images originales** (`image115a/b`) |
| 116 | 146 | Moyenne mobile | **2 graphes recadrés** (`fx_mm_odd/even`) |
| 117 | 147 | Lissage exponentiel | **graphe recadré** (`fx_liss_exp`) |
| 118 | 148 | Tendance linéaire | **2 graphes recadrés** (`fx_reg_a/b`) |
| 119 | 149 | Exemple de prévision par tendance | **image originale** (`assets_ss_image119.png`) |
| 120 | 150 | Évolution saisonnière | **steps CSS** |
| 121 | 151 | Exemple de prévision saisonnière | **image originale** (`assets_ss_image121.png`) |
| 122 | 152 | Conclusion sur les prévisions | def-grid |
| 123 | 153 | Chapitre 5 — Kanban | intercalaire rouge + picto 🏷️ |
| 124 | 154 | Kanban — historique et objectifs | roles 2 cartes |
| 125 | 155 | Kanban — flux tiré | roles 2 cartes |
| 126 | 156 | Kanban — principe (2) | **image originale** (`assets_ss_image126.png`) |
| 127 | 157 | Kanban — fonctionnement | **steps CSS** |
| 128 | 158 | Kanban — fonctionnement (2) | **image originale** (`assets_ss_image128.png`) |
| 129 | 159 | Kanban — fonctionnement (3) | **image originale** (`assets_ss_image129.png`) |
| 130 | 160 | Calcul du nombre de Kanbans | **steps CSS** |
| 131 | 161 | Calcul du nombre de Kanbans (2) | def-grid |
| 132 | 162 | Calcul (3) — application | def-grid |
| 133 | 163 | Kanban — conditions nécessaires | def-grid |
| 134 | 164 | Kanban — conséquences | def-grid |
| 135 | 165 | Conclusion sur le Kanban | def-grid |
| 136 | 166 | Chapitre 6 — Juste à Temps | intercalaire rouge + picto ⏱️ |
| 137 | 167 | Juste à Temps — objectifs | roles 2 cartes |
| 138 | 168 | Juste à Temps — les moyens | def-grid |
| 139 | 169 | Rationalisation de l'implantation | **image originale** (`assets_ss_image139.png`) |
| 140 | 170 | Rationalisation (2) — démarche | **steps CSS** |

Compteur : **170 slides**. 17 recadrages ajoutés (`image109/110/114a/114b/115a/115b/119/121/126/128/129/139`,
formules/graphes `fx_liss_exp`, `fx_mm_odd/even`, `fx_reg_a/b`). Correctif titres
`.slide131…170` — voir le bloc `/* ===== Slides 131-170 (slideshare OCR) =====`.
Vérification **visuelle** des 40 slides. Rien n'a été publié sur GitHub.

## ✅ Terminé — Tranche 4 : slides source 71 → 100 (slides 101–130)

| Slide source | Slide présentation | Contenu | Mise en page |
|---|---|---|---|
| 71 | 101 | Augmenter les stocks ? | roles 2 cartes + note (4 aléas masqués) |
| 72 | 102 | Classification des stocks | roles 2 cartes + note Pareto 20/80 |
| 73 | 103 | Méthodologie ABC | **steps CSS** 5 étapes (`.ss-steps`) |
| 74 | 104 | Magasinage | roles 2 cartes (mono/multi-magasin) + note emplacements |
| 75 | 105 | Opérations de gestion : entrées/sorties | roles 2 cartes (réception/délivrance) |
| 76 | 106 | Les inventaires | intro + def-grid 3 (permanent/intermittent/tournant) |
| 77 | 107 | Valorisation des stocks | intro + def-grid 3 coûts |
| 78 | 108 | Coût d'acquisition | roles 2 cartes (commande ext. 15→150 € / lancement OF) |
| 79 | 109 | Coût de possession | def-grid 4 + note **25-40 %/an** |
| 80 | 110 | Coût de rupture | roles 2 cartes (domaines critiques / conséquences) |
| 81 | 111 | Quantités économiques | roles 2 cartes (objectif / contradiction) |
| 82 | 112 | Formule de Wilson | roles 2 cartes (objectif / 4 hypothèses) |
| 83 | 113 | Wilson (2) évolution du stock | **scie CSS** 0→Q + pointillé Q/2 (`.ss-saw`) |
| 84 | 114 | Wilson (3) graphiques | **image originale** (`assets_ss_image84.png`, 2 courbes q*/n*) |
| 85 | 115 | Wilson (4) variables | def-grid 7 (S/U/T/a/q/n/Z) |
| 86 | 116 | Wilson (5) optimisation n | Z en texte + **dérivée et n\* = √(SuT/2a) en images originales recadrées** (`assets_ss_fx_dn/n.png`) |
| 87 | 117 | Wilson (6) optimisation q | Z en texte + **dérivée et q\* = √(2aS/Tu) en images originales recadrées** (`assets_ss_fx_dq/q.png`) |
| 88 | 118 | Wilson (7) sensibilité | def-grid 3 (restrictif/robuste 40%-6%/arrondi 0,5 %) |
| 89 | 119 | Quantités économiques avec remise | intro + roles 2 cartes (rabais uniformes/incrémentaux) |
| 90 | 120 | Seuil de rabais unique (1) | **steps CSS** algorithme 5 étapes (Q<R→U1…) |
| 91 | 121 | Seuil de rabais unique (2) | def-grid 2 (optimum = 1 des 3 solutions) |
| 92 | 122 | Seuil de rabais unique (3) exemple | def-grid 4 chiffré (q1*=20 → CT 10 500 €, q2*=22 non admissible, CT(R)=8 706 €, optimum R=50) |
| 93 | 123 | Politiques de gestion des stocks | **table HTML 2×2** (période × quantité) + note |
| 94 | 124 | Méthode à point de commande | intro + **image originale** (`assets_ss_image94.png`) + formule **Pc = Délai × conso** |
| 95 | 125 | Méthode de recomplètement | roles 2 cartes + formule **Qi = R − qi + Délai × conso** |
| 96 | 126 | Comparaison des 2 méthodes | roles 2 cartes (point de commande / recomplètement) |
| 97 | 127 | Aléas et stock de sécurité | roles 2 cartes (aléas / contradiction-objectif) |
| 98 | 128 | Calcul du stock de sécurité | roles 2 cartes (hypothèses / période D) + formule **SS = k × σ × √D** |
| 99 | 129 | K selon taux de service | **table HTML** (90 %→1,28 / 95 %→1,65 / 99 %→2,23) |
| 100 | 130 | Exemple de calcul stock de sécurité | def-grid 3 chiffré (**SS = 1,65×20×√15 = 128 pièces** ; recompl. 1500+128 = 1628) |

Compteur : **130 slides**. Nouveaux blocs CSS : `.ss-fx` (formules encadrées) et
`.ss-saw` (scie du stock 0→Q) + correctif titres `.slide101…130` — voir le bloc
`/* ===== Slides 101-130 (slideshare OCR) =====` dans index.html. Compactage
spécifique de la slide 124 (contenu dense). Vérification **visuelle** des 30
slides via `update/_tools/shot_slides.py` (copie index + saut `#N` + Chrome
headless → `_check/render/slideNN.png`). Rien n'a été publié sur GitHub.

## ✅ Terminé — Tranche 3 : slides source 41 → 70 (slides 71–100)

| Slide source | Slide présentation | Contenu | Mise en page |
|---|---|---|---|
| 41 | 71 | Données et GPAO | **image originale** (`assets_ss_image41.png`, flux données ↔ planification) |
| 42 | 72 | Nomenclatures | arbre CSS Lunettes→2 branche/1 monture + def-grid 2 |
| 43 | 73 | État des stocks | roles 2 cartes (rôle / difficultés) |
| 44 | 74 | Délais d'obtention | roles 2 cartes + note (attente = 80 % du délai) |
| 45 | 75 | Gammes | roles 2 cartes |
| 46 | 76 | Capacités de production | roles 2 cartes |
| 47 | 77 | Priorités sur les produits | roles 2 cartes |
| 48 | 78 | Informatisation (apports) | def-grid 3 (calculs / mémorisation / aide décision) |
| 49 | 79 | Informatisation (démarche) | **steps CSS** 7 étapes numérotées (`.ss-steps`) |
| 50 | 80 | Analyse de l'existant | roles 2 cartes (objectifs / méthodes IDEF, GRAI) |
| 51 | 81 | Expression des besoins | roles 2 cartes |
| 52 | 82 | Développement interne ou achat ? | **table HTML** progiciel vs logiciel (symboles +/=/−) |
| 53 | 83 | Test des logiciels, jeu d'essai | roles 2 cartes |
| 54 | 84 | Choix | roles 2 cartes |
| 55 | 85 | Information, formation | roles 2 cartes |
| 56 | 86 | Développement, implantation | roles 2 cartes |
| 57 | 87 | Difficultés d'implantation | def-grid 3 |
| 58 | 88 | ERP | roles 2 cartes (déf + caractéristiques) |
| 59 | 89 | Structure d'un ERP | **image originale** (`assets_ss_image59.png`) |
| 60 | 90 | Principaux progiciels ERP | def-grid 4 (SAP R/3, Marcam, Ortems, Witness…) |
| 61 | 91 | SAP R/3 | **grille 12 modules** (`.ss-mods`, SD/MM/PP/QM/PM/HR/FI/CO/AM/PS/WF/IS) |
| 62 | 92 | Gestion commerciale (SD) | roles 2 cartes |
| 63 | 93 | Gestion des achats/stocks (MM) | roles 2 cartes |
| 64 | 94 | Gestion de la production (PP) | def-grid 5 (PIC→PDP→CB→plan de charge→flux) |
| 65 | 95 | Gestion de la qualité (QM) | def-grid 6 |
| 66 | 96 | Gestion de la maintenance (PM) | def-grid 3 |
| 67 | 97 | Données techniques | def-grid 3 (articles/nomenclatures/postes de charge) |
| 68 | 98 | Gestion des stocks (intercalaire) | rouge + particules + picto 📦 |
| 69 | 99 | Utilité des stocks | def-grid 3 |
| 70 | 100 | Natures des stocks | def-grid 4 |

Compteur : **100 slides**. Nouvelles classes CSS `ss-*` (`.ss-steps`, `.ss-img`,
`.ss-mods`) + correctif titres `.slide71…100` — voir le bloc
`/* ===== Slides 71-100 (slideshare OCR) =====` dans index.html.
Nouveaux outils : `update/_tools/export_view.py` (slide N → PNG),
`crop_slide.py` (recadrage auto + suppression du n° de page d'origine).
Rien n'a été publié sur GitHub.

## ✅ Terminé — Tranche 2 : slides source 11 → 40 (slides 41–70)

| Slide source | Slide présentation | Contenu | Mise en page |
|---|---|---|---|
| 11 | 41 | Plan de Charge | roles 2 cartes (déf + paramètres) |
| 12 | 42 | Plan de Charge (2) | flow + entrée supérieure (Gammes ⬇) |
| 13 | 43 | Plan de Charge (3) | **graphe CSS** barres charge/capacité |
| 14 | 44 | Équilibre charge/capacité | roles 2 cartes |
| 15 | 45 | Ordonnancement | roles 2 cartes |
| 16 | 46 | Ordonnancement (2) | flow + 2 entrées supérieures |
| 17 | 47 | Difficultés | def-grid 3 |
| 18 | 48 | Diagramme de Gantt | **Gantt CSS** (3 ressources, bars A/B/C) |
| 19 | 49 | Lancement / suivi | def-grid nested |
| 20 | 50 | MRP/MRP2 (intercalaire) | particules + picto 🧮 |
| 21 | 51 | Définitions MRP/MRP2 | roles 2 cartes |
| 22 | 52 | Limites gestion des stocks | roles 2 cartes (0,95¹²≈0,54) |
| 23 | 53 | Besoins indép./dép. | roles 2 cartes |
| 24 | 54 | Principe du MRP | def-grid 3 |
| 25 | 55 | Conditions préalables | def-grid 7 items |
| 26 | 56 | PDP | roles 2 cartes |
| 27 | 57 | PDP (exemple) | **table HTML** Produit INT56 (Périodes 0–6, bruts/stocks/nets/PDP) |
| 28 | 58 | Calcul des Besoins | def-grid avec formules |
| 29 | 59 | CB (exemple) | **arbre HTML** lunettes→branche×2/monture×1 + données |
| 30 | 60 | CB (exemple 2) | **table HTML** 8 lignes × Périodes 0–6 (lunettes/branches, nets, ordres) |
| 31 | 61 | Plan de Charge | def-grid 3 |
| 32 | 62 | Lissage | **2 graphes CSS** avant/après |
| 33 | 63 | Principe du MRP2 | **image originale** (crop, hiérarchie PIC→PDP→CBN→PC→ordo→lancement→suivi) |
| 34 | 64 | Difficultés de mise en œuvre | def-grid 4 |
| 35 | 65 | Cercles pervers | **image originale** (crop, 2 cycles en cercle) |
| 36 | 66 | Progresser ? | roles 2 cartes |
| 37–38 | 67–68 | Conclusions MRP/MRP2 | def-grid |
| 39 | 69 | Chapitre 3 (intercalaire) | Données techniques & GPAO/ERP, picto 💻 |
| 40 | 70 | Les données | roles 2 cartes (commerciales/techniques) |

Compteur : **70 slides**. Nouvelles classes CSS `ss-*` ajoutées (tableaux, graphes,
Gantt, chaînes, arbre) — voir le bloc `/* ===== Slides 41-70 */` dans index.html.
Fonds rouges d'intercalaires corrigés (S31, S50, S69). Rien n'a été publié sur GitHub.

### 🔧 Rétro-correctifs lisibilité (retour utilisateur)

- **Couleurs** : règle globale `color:#eef2ff` ajoutée aux composants ss-* et aux
  tableaux `.ss-tbl` (le texte noir hérité par défaut rendait S57/S60 illisibles)
- **S43, S48, S63, S65** : reconstructions CSS remplacées par les **images
  originales recadrées** (`assets/assets_ss_image13/18/33/35.png`, via le pattern
  `.org-chart` à fond blanc = effet carte) — source 33 inclut les flèches de
  retour MRP2, 65 les vrais cercles
- **S59** : arbre lunettes original recadré (`assets_ss_image29.png`) + 4 def-items
  à droite ; emojis enexports abandonnés
- **S62 (lissage)** : conservée en CSS (2 graphes), libellés recolorés
- Crops automatiques : bbox pixels sombres, script `update/_tools/` (voir `_check/view/`)

## 💾 État sauvegardé (pour reprendre)

- `update/_ocr_state.json` — progression : **180/180 OCR-fait**, prochaine = **aucune** (OCR terminé)
- `update/ocr_texts/slide_NNN.txt` — texte OCR brut (jamais refaire)
- `update/_tools/` — `ocr_slides.py` (OCR réutilisable), `export_view.py`
  (export PNG pour lecture visuelle), `crop_slide.py` (recadrage image),
  `crop_region.py` (recadrage zone nommée, p.ex. formules), `profile_dark.py` /
  `profile_dark_x.py` (profils de pixels sombres pour cadrage fin),
  `shot_slides.py` (capture rendu HTML via Chrome headless → `_check/render/`),
  `build_batch1/2/3/4/5/6.py`, `check_batch4/5/6.py` (vérif structurelle),
  `export_view.py 101 140` par paquets (export PNG des sources) — batch6 = dernier
- `_check/` (gitignoré) — extraction pptx (slide N = `imageN.bin`, via `_rels`) + aperçus PNG dans `_check/view/`
- `C:\ppt\tessdata\` (gitignoré) — pack `fra.traineddata`
- Vérifier les slides douteuses **visuellement** : convertir le .bin en PNG, puis lire
  l'image (tableaux/graphes : OCR insuffisant), comme pour le batch 2.

### Pour continuer plus tard (agent OpenCode) — publication des slides 131–210

**Reprise au point : TOUT EST INTÉGRÉ** — les 180 slides slideshare sont dans
`index.html` (30 d'origine + 180 = **210 slides**, compteur 210). Derniers commits
locaux : `b8f6de8` (tranche 5, slides 131–170), `a9f5ea6` (tranche 6, slides 171–210).
**Aucun push n'a été fait** : la publication GitHub est en attente de demande explicite.

Dernier correctif (tranche 6) : slide 196 — le crop `assets_ss_image166.png` est un
crop PIL direct (8 %, 23 %, 100 %, 99 % de la source), car le bbox automatique de
`crop_slide.py` laissait un bloc blanc sur l'usine en bas à droite.

1. OCR **terminé** pour tout le pptx (`update/_ocr_state.json` : 180/180).
2. Intégration **terminée** : sources 1–180 → slides 31–210.
3. Vérification **visuelle terminée** pour les 180 slides (`shot_slides.py` → `_check/render/`).
4. Publier sur GitHub **quand l'utilisateur le demande** : suivre la procédure de
   `INSTRUCTIONS-UPDATE.md` (renommage de l'ancienne version en `.vNN.html` avant
   remplacement). Ne pas pousser sans demande explicite.

## ⚠️ Points d'attention

- Artefacts OCR à nettoyer : pictos (`ä`, `E`, `Fi`, `LL"`), numéros d'origine (35→73)
- Tableaux et graphes : OCR insuffisant → lecture visuelle des PNG obligatoire
- Formules et exposants (0,95¹²) : vérifier la mise en forme
- Slides douteuses repérées non encore traitées : aucune dans 11–40
  (les 5 « pauvres en texte » 13, 20, 32, 33, 39 étaient toutes utilisables)

### 🔧 Correctif dispositions/titres (retour utilisateur)

- **Symptôme** : à partir de la slide 32, titre à gauche + centré verticalement + noir
- **Cause** : les styles de titre `h2` blancs et `.ribbon` sont définis **par slide**
  (`.slide3 h2 … .slide30 h2`) pour les slides 1-30 uniquement ; les nouvelles
  slides 31-70 n'avaient ni couleur (noir par défaut), ni `flex-direction:column`
  (flex row par défaut → titre à gauche), ni ruban visible. Pas de règle `h2`
  globale dans le design system.
- **Fix** (`update/_tools/build_fix4.py`) : bloc CSS couvrant
  `.slide31 … .slide70` : `flex-direction:column` + `h2` blanc 3vw bold
  aligné haut-gauche (intercalaires S31/S50/S69 en 900, leur font-size inline
  reste prioritaire) + `.ribbon` orange/rouge 8%×5px.

## ✅ Terminé — Tranche 1 (historique)

| Slide source | Slide présentation | Titre | Mise en page |
|---|---|---|---|
| 1 | 31 | Chapitre 2 — Planification | intercalaire (particules + picto 📆) |
| 2 | 32 | Planifier | def-grid (SYNCHRONISER / OPTIMISER / RÉAGIR) || 3 | 33 | 6 niveaux de planification | def-grid 6 items |
| 4 | 34 | PIC | roles 2 cartes (définition + paramètres) |
| 5 | 35 | PIC (2) | flow ENTRÉES→PIC→SORTIES |
| 6 | 36 | PDP | roles 2 cartes |
| 7 | 37 | PDP (2) | flow |
| 8 | 38 | Calcul des Besoins | roles 2 cartes |
| 9 | 39 | Calcul des Besoins (2) | flow |
| 10 | 40 | Mécanisme du CB | def-grid avec formules |

Compteur du diaporama : **40 slides**. Rien n'a été publié sur GitHub.

## 💾 État sauvegardé (pour reprendre)

- `update/_ocr_state.json` — numéro des slides OCR-fait (`done`), suivante (`next` = **11**), total 180
- `update/ocr_texts/slide_NNN.txt` — texte OCR brut par slide (1 fichier / slide, jamais refaire)
- `update/_tools/ocr_slides.py` — script OCR réutilisable
- `_check/` (gitignoré) — extraction du pptx, images PNG dans `_check/ppt/media/` (`imageN.bin` = PNG ; correspondance slide N → `imageN.bin` via `ppt/slides/_rels/slideN.xml.rels`)
- `C:\ppt\tessdata\` (gitignoré) — pack français `fra.traineddata`

### Pour continuer plus tard (agent OpenCode)

1. OCR de la tranche suivante :
   `python update\_tools\ocr_slides.py 11 20`
2. Lire les textes dans `update/ocr_texts/slide_011.txt` …
3. **Classer chaque slide** :
   - texte → mise en page def-grid / roles / flow (design system de `INSTRUCTIONS-UPDATE.md`)
   - schéma 100% graphique (OCR pauvre) → extraire l'image `_check\ppt\media\imageNN.bin`,
     la copier en `assets/assets_imageNN.png` et l'afficher via le pattern `.end-chart img`
   - hybride texte + schéma simple → reconstruction flow
4. Script d'insertion à créer sur le modèle de `update/_tools/build_batch1.py`
   (insertion après la dernière `<section>`, avant `</div>` du conteneur, data-i
   continu, classes slide41, slide42…, counter à mettre à jour, transitions t-*
   à faire tourner)
5. Publier sur GitHub seulement quand toutes les slides sont intégrées
   (procédure étapes 4-5 de `INSTRUCTIONS-UPDATE.md`), avec renommage de
   l'ancienne version en `.vNN.html`.

## ⚠️ Points d'attention vus sur la tranche 1

- Artefacts OCR à nettoyer : pictos (`ä`, `E`, `Fi`, `LL"`), numéros de slides d'origine (35, 36, 43…)
- Schémas multi-colonnes : l'OCR mélange les colonnes → restructurer posément
- Formules (`q*`, U1/U2, seuils de rabais) : OCR approximatif → reformulation manuelle

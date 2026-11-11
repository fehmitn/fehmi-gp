# 📍 État du chantier — Ajout des 180 slides slideshare

**Mis à jour :** 2026-11-11

## Objectif global

Ajouter les **180 slides** de `slidsahre-file.pptx` (chaque slide = une image PNG,
texte récupéré par OCR) **à la suite** de la présentation actuelle
(`index.html`, 30 slides issues de `gp.pptx`).

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
  `shot_slides.py` (capture rendu HTML via Chrome headless → `_check/render/`),
  `build_batch1/2/3/4.py`, `check_batch4.py` (vérif structurelle) — batch4 = dernier
- `_check/` (gitignoré) — extraction pptx (slide N = `imageN.bin`, via `_rels`) + aperçus PNG dans `_check/view/`
- `C:\ppt\tessdata\` (gitignoré) — pack `fra.traineddata`
- Vérifier les slides douteuses **visuellement** : convertir le .bin en PNG, puis lire
  l'image (tableaux/graphes : OCR insuffisant), comme pour le batch 2.

### Pour continuer plus tard (agent OpenCode) — intégration des slides 131–210

1. OCR **terminé** pour tout le pptx : lire `update/ocr_texts/slide_101.txt` … `slide_180.txt`
   et classer : texte / schéma / tableau / intercalaire
2. Tranches restantes à intégrer dans index.html :
   source 101–140 → slides 131–170, source 141–180 → slides 171–210
3. Mise en page def-grid / roles / flow / `ss-*` (design system de `INSTRUCTIONS-UPDATE.md`) ;
   schémas complexes → `export_view.py N` puis `crop_slide.py N l t r b` → `assets/assets_ss_imageNN.png` + `.ss-img`
4. Script `build_batch5.py` sur le modèle de `build_batch4.py`
   (insertion après la dernière `<section data-i="129">`, classes slide131…, counter 130→170,
   transitions : reprendre le cycle à la suite de la slide 130 = `t-rotate`,
   i.e. cycle redémarré à l'intercalaire 98 : rise/up/push/blur/rotate/zoom/insert)
5. Vérifier visuellement : `python update/_tools/shot_slides.py 131 … 170` puis lire les PNG
6. Publier sur GitHub quand toutes les slides sont intégrées (renommage `.vNN.html` avant remplacement).

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

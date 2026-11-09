# 🔄 Procédure de mise à jour du diaporama — LISEZ-MOI

## Pour l'utilisateur (Fehmi)

Quand le fichier `gp.pptx` a été modifié, il suffit de relancer OpenCode dans
`C:\ppt` et d'écrire simplement :

```
update
```

ou une phrase du type : « mets à jour le diaporama avec le nouveau gp.pptx ».

Aucun script à lancer : c'est l'agent OpenCode qui fait tout (extraction, mise à
jour du HTML, publication sur GitHub, push).

---

## 📁 État actuel (référence)

| Élément | Emplacement / valeur |
|---|---|
| Version courante du diaporama | **`C:\ppt\index.html`** (racine du dépôt, 30 slides) — fonds photo `bg_*.jpg` sur les 30 slides (sync du dossier `update`, 09/11/2026) |
| Anciennes versions | `.v7.html`, `.v8.html`, `.v9.html` gardées à la racine (la v9 n'a PAS les fonds photo ; après une regénération, numéroter la version remplacée en `.v10.html`, `.v11.html`…) |
| Médias du diaporama | **`C:\ppt\assets\`** → `assets_image15.png` … `assets_image24.png` + fonds `bg_*.jpg` + `IMAGES_CREDITS.md` |
| Copie de travail Git | **`C:\ppt` lui-même** (le dossier est un dépôt git ; `fehmi-gp\` supprimé) |
| Dépôt GitHub | **https://github.com/fehmitn/fehmi-gp** (compte `fehmitn`) |
| Site en ligne (GitHub Pages) | **https://fehmitn.github.io/fehmi-gp/** (branche `main`, racine) |
| Source PowerPoint | `C:\ppt\gp.pptx` (30 slides ; slide 1 : video `media1.mp4` non utilisée, fond = `image15.png`) |

> Références dans le HTML : les images sont citées `src="assets/assets_imageNN.png"`.

---

## Pour l'agent OpenCode (procédure à suivre)

### Étape 1 — Extraire le nouveau gp.pptx
```powershell
Remove-Item "C:\ppt\_extract_tmp" -Recurse -Force -ErrorAction SilentlyContinue
Expand-Archive -Path "C:\ppt\gp.pptx" -DestinationPath "C:\ppt\_extract_tmp" -Force
```
Lire ensuite `ppt/slides/slide*.xml` (touches `<a:t>` pour les textes),
`ppt/slides/_rels/slide*.xml.rels` (images/vidéos référencées) et
`ppt/media/` (les fichiers média).

### Étape 2 — Médias
Copier dans **`C:\ppt\assets\`** tout nouveau média avec le préfixe `assets_`
(nommage : `assets_imageNN.ext`, `assets_mediaN.mp4`). Vérifier si
`assets_image15/16/17.png` ont changé (comparer avec `Get-FileHash`) avant de
les écraser.

### Étape 3 — Mettre à jour le diaporama HTML
Le diaporama actuel : **`C:\ppt\index.html`** (fichier unique, auto-suffisant),
30 slides comme `gp.pptx`. C'est ce fichier qui est servi par GitHub Pages.

Faire une **mise à jour ciblée** avec l'outil édition (edit) sur ce fichier :
- Remplacer le contenu textuel de chaque `<section class="slide">`
- Ajuster le **nombre de slides** si le pptx en contient désormais plus ou moins
  (mettre à jour aussi `<b id="cur">1</b> / <span id="tot">30</span>` dans le HTML ;
  le JS calcule déjà `total = slides.length` et crée les dots automatiquement)
- Mettre à jour `<img class="bgimg" src="assets/assets_image15.png">` si le fond change
- Si une slide contient désormais une image ou vidéo, suivre les patterns existants
  (`.bgimg` en fond assombri, `<img>` dans `.end-chart` / `.card-img`, `.role-card`…)

⚠️ Si le contenu change trop profondément (nouveaux types de slides, graphiques
SmartArt, tableaux), régénérer plutôt le fichier HTML complet en conservant le
même design (voir ci-dessous). Avant de remplacer `index.html`, renommer
l'ancienne version actuelle en `.vNN.html` (numéro suivant : v10, v11…) afin de
garder un historique numéroté, et `index.html` reste toujours le nom de la
version courante.

### Étape 4 — Publier sur GitHub (dépôt `fehmitn/fehmi-gp`, racine = `C:\ppt`)
```powershell
Set-Location C:\ppt
git add .
git -c user.name="fehmitn" -c user.email="fehmitn@users.noreply.github.com" commit -m "update depuis gp.pptx"
git push
```
Le site https://fehmitn.github.io/fehmi-gp/ se régénère tout seul (~1 min).
Vérifier le statut du build si besoin :
```powershell
gh api repos/fehmitn/fehmi-gp/pages/builds | ConvertFrom-Json |
  Select-Object status, commit | Format-List
```
(`update\`, `_extract_tmp\` sont exclus du dépôt via `.gitignore`.)

### Étape 5 — Nettoyer
Supprimer les médias `assets\*` devenus inutilisés après vérification,
puis l'extraction temporaire :
```powershell
Remove-Item "C:\ppt\_extract_tmp" -Recurse -Force
```

---

## 🎨 Design system à conserver (identité visuelle)

| Élément | Valeur |
|---|---|
| Police | Poppins (Google Fonts), graisses 300→900 |
| Fond principal | dégradé bleu nuit `#0f1b3d → #1e2d50 → #24356b` |
| Accents | orange `#f39c12` + rouge `#e74c3c` (dégradés, rubans, nums) |
| Slide intercalaire (ex. slide 3) | fond rouge `#e74c3c → #8e2418`, titre 4.5vw, picto flottant |
| Texte | blanc `#fff` / `#ecf0f1`, graisse 300 pour le corps |
| Animations d'entrée | classe `.anim` + `.d1`–`.d7` (délais 0.2s → 1.7s), `slideInUp` et `zoomIn` |
| Hover cartes | `translateX` ou `translateY(-8px)` + ombre `rgba(0,0,0,.45)` |
| Ruban sous titres | voir classe `.ribbon` (dégradé orange→rouge, 8% largeur, 5px hauteur) |
| Images de schémas | `.end-chart img` (slides 17/21–23/26 agrandies : `max-width:100%`, zone `flex:1.75`, slide 17 : `end-wrap` 88% + img 120%) |
| Images dans cartes | `.role-card .card-img` (slide 16 : ~96% largeur, texte au-dessus) |
| Bandeaux contexte | `.slide-banner` (slides 24 & 27) |
| Quiz (slides 29–30) | `.quiz-grid` / `.quiz-item` face avant↔arrière (classe `.flip`), options `.q-opt` (✅ `.good` / ❌ `.bad`), définition `.q-def.show`, reset via `resetQuiz()` dans `go()` |

## 🎮 Interactions à conserver
- **Clic n'importe où** : avance au slide suivant (hors boutons, dots et cartes du quiz)
- Navigation : flèches ← →, Espace, PageUp/PageDown, swipe tactile
- Boutons `‹` (précédent), `⛶` (plein écran, touche F), `›` (suivant)
- Barre de progression dégradée en haut, compteur `1 / 30` en bas gauche,
  dots cliquables en bas centre
- Révélation par étapes (`.step`, slides 9 & 10) : le clic révèle d'abord les étapes
- Quiz slides 29–30 : clic sur une carte → question à 4 choix ; ✅ correct
  (définition affichée) / ❌ à revoir (on peut retenter) ; bouton `↩︎ retour` ;
  remise à zéro automatique au changement de slide
- ⚠️ Le toast « nom de la transition » (⟲ Zoom…) a été **supprimé** à la demande
- Vidéo slide 1 (optionnel, cf. `assets_media1.mp4` du pptx) en fond si souhaité
- Auto-play slide : intervalle commenté dans le JS (désactivé par défaut)

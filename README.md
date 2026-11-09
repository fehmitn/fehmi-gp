# 🏭 Présentation — Gestion de Production

Diaporama animé (HTML/CSS/JS, fichier unique) généré à partir de `gp.pptx`.

🌐 **Voir la présentation en ligne : https://fehmitn.github.io/fehmi-gp/**

## Contenu

| Fichier | Rôle |
|---|---|
| `index.html` | Diaporama animé (30 slides, quiz interactifs slides 29–30) |
| `gp.pptx` | Source PowerPoint |
| `assets/` | Images du diaporama (`assets_image15–24.png`) + fonds photo `bg_*.jpg` |

## 🖼️ Fonds photo des slides

Chaque slide a un fond photo (usine moderne, entrepôt, logistique, robots) avec un voile sombre pour garder le texte lisible. Choisis selon le thème de la slide :

| Slides | Fond |
|---|---|
| 1, 18, 30 | Chaîne d'assemblage Opel (Gliwice) |
| 2, 21 | Entrepôt à rayonnages de palettes |
| 3, 28 | Port conteneurs d'Anvers au crépuscule |
| 4, 24 | Usine Continental au bord du canal (Hannover) |
| 5, 6, 25 | Robots Stäubli |
| 7, 26 | Atelier de machines CNC |
| 8, 23 | Terminal à conteneurs de Bremerhaven |
| 9, 29 | Dock logistique de nuit |
| 10, 20 | Ligne d'assemblage Geely |
| 11, 19 | Ligne de production GM (Gliwice) |
| 12, 13, 27 | Entrepôt sombre, palettes filmées |
| 14, 15, 22 | Chargement conteneur au chariot élévateur |
| 16, 17 | Robots de palettisation KUKA |

Sources et licences (CC0 / CC BY / CC BY-SA, Wikimedia Commons) : `assets/IMAGES_CREDITS.md`
⚠️ **Licences CC BY / CC BY-SA obligent le crédit des auteurs** : ne pas supprimer `assets/IMAGES_CREDITS.md`.

## 🔄 Session du 09/11/2026 — travail fait sur le PC secondaire

Travail réalisé sur un **PC secondaire** (sans accès GitHub). Le dossier est copié dans un dossier **`UPDATE`** sur le **PC principal**, puis synchronisé et poussé vers GitHub depuis le dossier principal.

### ✅ Ce qui a été fait

1. **Fonds photo ajoutés aux 30 slides** de `index.html` :
   - 13 photos libres de droits (usines modernes, robots, entrepôts, logistique) téléchargées depuis Wikimedia Commons, choisies et vérifiées une par une selon le thème de chaque slide
   - ajout d'un bloc CSS « FONDS PHOTO » en fin de `<style>` (lignes 632–659) : chaque classe `.slideN` reçoit `background: voile sombre + photo center/cover no-repeat`
   - voile dégradé bleu nuit opacity .72–.93 → le texte blanc/orange reste parfaitement lisible
   - les dégradés d'origine restent en secours : ce bloc surcharge les règles précédentes (cascading CSS)
   - effets existants **inchangés** : transitions entre slides, animations `.anim` en cascade, particules flottantes, quiz
   - ajout d'une lueur dorée subtile derrière le contenu des slides 1 et 18 (`.slide1::after`, `.slide18::after`, avec `isolation:isolate` + `z-index:-1` pour que le texte passe dessus)
2. **Nouveaux fichiers dans `assets/` :**
   - `bg_assembly_hero.jpg`, `bg_assembly_2.jpg`, `bg_assembly_busy.jpg`, `bg_robots_yellow.jpg`, `bg_palletizing.jpg`, `bg_cnc_facility.jpg`, `bg_factory_dusk.jpg`, `bg_warehouse_rack.jpg`, `bg_warehouse_dark.jpg`, `bg_container_load.jpg`, `bg_port_dusk.jpg`, `bg_port_day.jpg`, `bg_night_dock.jpg` — 13 fonds, ~9,4 Mo au total, largeur 1600 px
   - `IMAGES_CREDITS.md` — crédits/licences/auteurs (obligatoire pour CC BY / CC BY-SA)
3. **`README.md`** mis à jour (cette section + tableau des fonds photo).
   - `bg_assembly_korea.jpg` (photo Hyundai, sombre/dépassée) a été téléchargé puis **supprimé**, remplacé par `bg_assembly_2.jpg` (Opel/GM Gliwice) pour les slides 11 et 19 — le CSS ne référence aucun fichier orphelin.

### 📦 À faire sur le PC principal

1. Copier tout le dossier dans un dossier **`UPDATE`** sur le PC principal (le dépôt principal reste en place), puis suivre le workflow décrit dans la section [🔄 Workflow de synchronisation via le dossier UPDATE](#-workflow-de-synchronisation-via-le-dossier-update-pc-principal)
2. Vérifier : `index.html` + `assets/` contient bien les 13 `bg_*.jpg` + `IMAGES_CREDITS.md` (en plus des 10 `assets_image*.png` d'origine → 23 images au total)
3. Pousser sur GitHub :

```powershell
git add .
git commit -m "Ajout fonds photo usine/entrepôt sur les 30 slides + crédits Wikimedia"
git push
```

4. GitHub Pages se met à jour automatiquement → vérifier https://fehmitn.github.io/fehmi-gp/ après quelques minutes

## 🔄 Workflow de synchronisation via le dossier UPDATE (PC principal)

Comment pousser sur GitHub le travail fait sur un autre PC :

1. **Copier le dossier courant** (complet : `index.html`, `gp.pptx`, `assets/`, `README.md`…) dans un dossier **`UPDATE`** sur le PC principal, par exemple `C:\sst\UPDATE\fehmi-gp`.
   Le **dossier principal** du dépôt (ex. `C:\sst\fehmi-gp-main`) reste tel quel.
2. **Ouvrir l'agent dans le dossier principal** (sur le PC principal), puis lui donner ce prompt (copier/coller) :

   ```text
   J'AI FAIT DES MISES À JOUR DANS LE DOSSIER UPDATE. SYNCHRONISE LE DOSSIER PRINCIPAL AVEC LE DOSSIER UPDATE ET FAIS UN PUSH COMMIT SUR GITHUB.
   ```

3. L'agent doit alors :
   - comparer le dossier principal avec le dossier `UPDATE` (fichiers modifiés, nouveaux, supprimés),
   - copier les changements de `UPDATE` vers le dossier principal,
   - vérifier le résultat (fichiers présents, liens, images),
   - pousser sur GitHub :

     ```powershell
     git add .
     git commit -m "Synchronisation depuis le dossier UPDATE"
     git push
     ```

4. GitHub Pages se met à jour automatiquement → vérifier https://fehmitn.github.io/fehmi-gp/ après quelques minutes.

> 💡 Adapter le chemin du dossier `UPDATE` dans le prompt si besoin, par exemple :
> « J'ai fait des mises à jour dans `C:\sst\UPDATE\fehmi-gp`. Synchronise le dossier principal `C:\sst\fehmi-gp-main` avec ce dossier UPDATE et fais un push commit sur GitHub. »

## 🎮 Utilisation

- Naviguer : flèches `←` `→`, `Espace`, `PgUp`/`PgDn`, swipe tactile
- Plein écran : touche `F` ou bouton `⛶`
- Quiz (slides 29 & 30) : cliquer sur une carte, choisir une réponse ✅/❌, la définition s'affiche ; bouton `↩︎ retour`

## 🔄 Mise à jour depuis le PowerPoint

Modifier `gp.pptx`, puis mettre à jour `index.html` (slides, images) et push :

```powershell
git add .
git commit -m "update depuis gp.pptx"
git push
```

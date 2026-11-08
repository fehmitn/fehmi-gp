# 🏭 Présentation — Gestion de Production

Diaporama animé (HTML/CSS/JS, fichier unique) généré à partir de `gp.pptx`.

🌐 **Voir la présentation en ligne : https://fehmitn.github.io/fehmi-gp/**

## Contenu

| Fichier | Rôle |
|---|---|
| `index.html` | Diaporama animé (30 slides, quiz interactifs slides 29–30) |
| `gp.pptx` | Source PowerPoint |
| `assets/` | Images du diaporama (`assets_image15–24.png`) |

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

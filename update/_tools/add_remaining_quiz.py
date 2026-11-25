# -*- coding: utf-8 -*-
"""Ajoute 2 slides de quiz a la fin de chaque chapitre restant (3 a 7).

Points d'insertion (anciens numeros) : apres 99, 137, 154, 167, 180, 212.
Chaque insertion decale les slides suivantes de +2 : 212 -> 224 slides.
"""
import io
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")


def card(num, ico, word, question, opts, answer, definition):
    lines = ['      <div class="quiz-item anim d%d">' % num,
             '        <div class="quiz-face quiz-front">',
             '          <div class="q-ico">%s</div>' % ico,
             '          <div class="q-wd">%s</div>' % word,
             '          <div class="q-hint">🖱️ cliquez pour le quiz</div>',
             '        </div>',
             '        <div class="quiz-face quiz-back">',
             '          <div class="q-back">↩︎ retour</div>',
             '          <div class="q-quest">%s</div>' % question]
    for i, o in enumerate(opts):
        attr = ' data-ok="1"' if i == answer else ""
        lines.append('          <div class="q-opt"%s>%s</div>' % (attr, o))
    lines += ['          <div class="q-verdict"></div>',
              '          <div class="q-def">%s</div>' % definition,
              '        </div>', '      </div>']
    return "\n".join(lines)


PATH = r"C:\ppt\index.html"
AFTER = [99, 137, 154, 167, 180, 212]
TOTAL = 224


def remap(n):
    return n + 2 * sum(1 for k in AFTER if k < n)


# ---------------------------------------------------------------- contenus

SETS = [
    dict(
        after=99, img="bg_erp_online.jpg", pos="center 50%", ov=(.86, .91),
        title="Chapitre 3 — Quiz : données techniques & GPAO", trans="t-zoom",
        cards=[
            ("📋", "Nomenclature", "Une nomenclature (BOM), c'est :",
             ["A. la liste des fournisseurs",
              "B. la liste hiérarchique des composants et quantités d'un produit",
              "C. le planning des machines",
              "D. le stock de sécurité"], 1,
             "📋 Définition : arborescence des composants (niveaux) avec les quantités nécessaires à la fabrication d'un produit fini ; base du calcul des besoins."),
            ("🗂️", "Données techniques", "Laquelle n'est pas une donnée technique ?",
             ["A. la nomenclature", "B. la gamme de fabrication",
              "C. le délai d'obtention", "D. le prix de vente client"], 3,
             "🗂️ Définition : données techniques = nomenclatures, gammes, temps, capacités, délais, état des stocks et priorités — nécessaires à la GPAO."),
            ("⚙️", "Gamme", "Une gamme de fabrication précise :",
             ["A. les opérations, postes et temps de fabrication",
              "B. les prix d'achat", "C. les livraisons clients", "D. les effectifs"], 0,
             "⚙️ Définition : séquence des opérations avec les postes de travail, les temps et les moyens nécessaires pour transformer la matière."),
            ("🧾", "Informatisation", "Quelle est la bonne suite d'étapes ?",
             ["A. Choix → test → analyse → formation",
              "B. Analyse → expression des besoins → choix → développement/achat → test → formation → implantation",
              "C. Formation → achat → analyse",
              "D. Test → expression des besoins → analyse"], 1,
             "🧾 Définition : la démarche part de l'existant, formalise les besoins, compare développement interne et achat, teste (jeu d'essai), puis forme et implante."),
            ("🧪", "Jeu d'essai", "Le jeu d'essai sert à :",
             ["A. former les utilisateurs avant la mise en œuvre",
              "B. tester le logiciel avec des données représentatives avant le choix",
              "C. négocier le prix", "D. calculer les stocks"], 1,
             "🧪 Définition : jeu de données fictives mais réalistes pour valider les fonctions du progiciel avant la décision d'achat."),
            ("🧱", "ERP", "Un ERP (Enterprise Resource Planning) est :",
             ["A. un logiciel de paie uniquement",
              "B. un système intégré couvrant les fonctions commerciale, achats, production, qualité, maintenance…",
              "C. un entrepôt automatisé", "D. une méthode de prévision"], 1,
             "🧱 Définition : progiciel de gestion intégré qui partage une base de données commune entre tous les services de l'entreprise."),
        ],
        title2="Chapitre 3 — Quiz : les modules d'un ERP", trans2="t-rise",
        cards2=[
            ("🏢", "SAP R/3", "SAP R/3 est :",
             ["A. le progiciel ERP le plus diffusé", "B. une nomenclature",
              "C. un mode de transport", "D. un indicateur de stock"], 0,
             "🏢 Définition : SAP R/3 est l'ERP le plus répandu, composé de modules couvrant les principaux domaines de l'entreprise."),
            ("📦", "Module MM", "Le module MM d'un ERP gère :",
             ["A. la gestion commerciale", "B. les achats et les stocks",
              "C. la paie", "D. la maintenance"], 1,
             "📦 Définition : MM (Materials Management) = achats, stocks, inventaires et facturation fournisseurs."),
            ("🏭", "Module PP", "Le module PP concerne :",
             ["A. la production (ordres, planification)",
              "B. la qualité", "C. les ventes", "D. les ressources humaines"], 0,
             "🏭 Définition : PP (Production Planning) = planification de production, ordres de fabrication, capacités et nomenclatures."),
            ("✅", "Module QM", "Le module QM couvre :",
             ["A. la gestion de la qualité", "B. le transport",
              "C. la trésorerie", "D. les prévisions"], 0,
             "✅ Définition : QM (Quality Management) = contrôle qualité, plans de contrôle, traçabilité et non-conformités."),
            ("🔧", "Module PM", "Le module PM est dédié à :",
             ["A. la maintenance", "B. la paie",
              "C. la distribution", "D. les achats"], 0,
             "🔧 Définition : PM (Plant Maintenance) = maintenance préventive/curative, plans d'intervention et historique des pannes."),
            ("⚠️", "Implantation", "Une difficulté fréquente d'un projet ERP est :",
             ["A. le manque de données fiables et la résistance au changement",
              "B. l'excès de modules", "C. l'excès de stocks", "D. la faible informatisation"], 0,
             "⚠️ Définition : fiabilité des données, conduite du changement, formation et coût sont les principaux facteurs de risque d'un projet ERP."),
        ],
    ),
    dict(
        after=137, img="bg_stock_online.jpg", pos="center 45%", ov=(.87, .92),
        title="Chapitre 3 — Quiz : gestion des stocks", trans="t-zoom",
        cards=[
            ("📦", "Pourquoi stocker ?", "Un stock permet notamment de :",
             ["A. découpler approvisionnement et consommation",
              "B. supprimer tout aléa", "C. augmenter les coûts",
              "D. remplacer la prévision"], 0,
             "📦 Définition : le stock sert de tampon entre l'offre et la demande, protège contre les aléas et permet des économies d'échelle."),
            ("🔤", "Méthode ABC", "En classification ABC, les articles A sont :",
             ["A. peu nombreux mais à forte valeur",
              "B. très nombreux et à faible valeur",
              "C. intermédiaires", "D. périssables"], 0,
             "🔤 Définition : ABC classe les articles selon leur valeur de consommation : A = forte valeur (suivi strict), C = faible valeur (suivi simple)."),
            ("💰", "Coûts", "Le coût de possession correspond à :",
             ["A. au prix d'achat", "B. au coût de rupture",
              "C. au coût de stockage, immobilisation, assurance, obsolescence",
              "D. au coût de transport"], 2,
             "💰 Définition : posséder un stock coûte (entreposage, capital immobilisé, assurance, pertes) ; le coût d'acquisition est le prix d'achat."),
            ("🧮", "Wilson", "La formule de Wilson donne :",
             ["A. le stock de sécurité",
              "B. la quantité de commande économique qui minimise coût de commande + coût de possession",
              "C. le délai de livraison", "D. le prix de vente"], 1,
             "🧮 Définition : Q* = √(2·D·C / h) : compromis optimal entre coût de passation de commande et coût de détention du stock."),
            ("📋", "Inventaire", "Un inventaire physique sert à :",
             ["A. vérifier que le stock réel correspond au stock informatique",
              "B. fixer les prix", "C. commander", "D. valoriser la production"], 0,
             "📋 Définition : comptage physique périodique ou tournant pour détecter écarts, erreurs, vols et détériorations."),
            ("🔄", "FIFO / LIFO", "En période d'inflation, la méthode LIFO valorise les sorties :",
             ["A. au coût le plus ancien", "B. au coût le plus récent",
              "C. au coût moyen", "D. au prix de vente"], 1,
             "🔄 Définition : FIFO sort les articles les plus anciens (stock final à coût récent) ; LIFO sort les plus récents (stock final à coût ancien)."),
        ],
        title2="Chapitre 3 — Quiz : politiques de stock", trans2="t-rise",
        cards2=[
            ("🎯", "Point de commande", "Avec la méthode du point de commande :",
             ["A. on commande une quantité fixe quand le stock atteint un seuil",
              "B. on commande à dates fixes",
              "C. on commande toujours la même valeur", "D. on ne commande jamais"], 0,
             "🎯 Définition : quantité fixe (souvent Q*), intervalle variable : déclenchement dès que le stock disponible passe sous le seuil."),
            ("📅", "Recomplètement", "La méthode de recomplètement consiste à :",
             ["A. commander à période fixe pour remonter le stock à un niveau cible",
              "B. commander dès que le stock est nul",
              "C. commander en continu", "D. stocker sans limite"], 0,
             "📅 Définition : période fixe, quantité variable : à chaque revue, on commande la différence entre le niveau cible et le stock disponible."),
            ("🛡️", "Stock de sécurité", "Le stock de sécurité couvre :",
             ["A. les aléas de demande et de délai",
              "B. les commandes fermes", "C. les surplus de production",
              "D. les impôts"], 0,
             "🛡️ Définition : SS = k·σ·√D (k dépend du taux de service) : il protège contre la variabilité de la demande pendant le délai."),
            ("📈", "Taux de service", "Un taux de service de 95 % signifie :",
             ["A. 95 % des commandes sont servies sans rupture",
              "B. 5 % du stock est périmé", "C. 95 % du stock est vendu",
              "D. le délai est de 5 jours"], 0,
             "📈 Définition : plus le taux de service visé est élevé, plus le coefficient k (et donc le stock de sécurité) augmente."),
            ("🏷️", "Remise quantitative", "Une remise sur quantité peut :",
             ["A. rendre économique une commande plus grosse que Q*",
              "B. supprimer le coût de possession",
              "C. réduire le délai à zéro", "D. annuler le stock de sécurité"], 0,
             "🏷️ Définition : la remise modifie le coût d'acquisition et peut changer la quantité optimale : on compare l'économie d'achat au surcoût de stockage."),
            ("⚖️", "Comparaison", "Par rapport au point de commande, le recomplètement :",
             ["A. a des intervalles fixes et des quantités variables",
              "B. a des quantités fixes et des intervalles variables",
              "C. n'utilise pas de stock de sécurité",
              "D. ne concerne que les matières premières"], 0,
             "⚖️ Définition : point de commande = quantité fixe / intervalle variable ; recomplètement = intervalle fixe / quantité variable."),
        ],
    ),
    dict(
        after=154, img="bg_forecast_online.jpg", pos="center 50%", ov=(.86, .92),
        title="Chapitre 4 — Quiz : prévisions", trans="t-zoom",
        cards=[
            ("🔮", "Objectif", "Faire des prévisions, c'est :",
             ["A. estimer la demande future pour guider production et achats",
              "B. connaître le prix exact", "C. supprimer les stocks",
              "D. garantir le succès"], 0,
             "🔮 Définition : anticiper la demande (quantité, période) pour dimensionner capacités, achats et stocks ; c'est une estimation, pas une certitude."),
            ("👥", "Qui prévoit ?", "Les prévisions sont élaborées par :",
             ["A. le seul service production",
              "B. les services commerciaux, production, achats et direction",
              "C. les fournisseurs uniquement", "D. la comptabilité uniquement"], 1,
             "👥 Définition : le commercial apporte la connaissance client, la production les contraintes, les achats les délais ; la direction arbitre."),
            ("🧭", "Méthodes", "Une méthode qualitative de prévision est :",
             ["A. la moyenne mobile", "B. l'avis d'experts / méthode Delphi",
              "C. le lissage exponentiel", "D. la tendance linéaire"], 1,
             "🧭 Définition : qualitatives = avis d'experts, sondages, Delphi (quand l'historique est faible) ; quantitatives = modèles sur séries chronologiques."),
            ("📊", "Composantes", "Une série chronologique peut comporter :",
             ["A. tendance, saisonnalité, cycle et bruit",
              "B. uniquement le prix", "C. seulement les commandes",
              "D. les stocks seuls"], 0,
             "📊 Définition : tendance (long terme), saisonnalité (périodique), cycle, et variations irrégulières appelées bruit."),
            ("➗", "Moyenne mobile", "La moyenne mobile de période n :",
             ["A. fait la moyenne des n dernières valeurs",
              "B. donne la valeur maximale", "C. corrige l'inflation",
              "D. calcule le stock"], 0,
             "➗ Définition : F(t) = (A(t-1)+…+A(t-n))/n : simple, mais elle réagit avec retard aux changements de tendance."),
            ("🎚️", "Lissage exponentiel", "Dans le lissage exponentiel, le coefficient α :",
             ["A. donne plus de poids à la donnée la plus récente",
              "B. est toujours nul", "C. mesure le stock",
              "D. est la période de moyenne"], 0,
             "🎚️ Définition : Ft = α·At-1 + (1-α)·Ft-1 ; α proche de 1 = forte réactivité, α faible = forte stabilité."),
        ],
        title2="Chapitre 4 — Quiz : méthodes de prévision", trans2="t-rise",
        cards2=[
            ("📐", "Tendance linéaire", "La méthode de tendance linéaire :",
             ["A. ajuste une droite aux données historiques",
              "B. calcule un stock de sécurité", "C. classe les articles ABC",
              "D. choisit un transporteur"], 0,
             "📐 Définition : régression linéaire (moindres carrés) : F(t) = a + b·t, adaptée aux séries avec tendance régulière."),
            ("🌸", "Saisonnalité", "La saisonnalité désigne :",
             ["A. des variations régulières selon la saison ou le mois",
              "B. une panne machine", "C. un retard aléatoire",
              "D. une hausse permanente"], 0,
             "🌸 Définition : variations répétitives à intervalle régulier (ex. pics de décembre) ; on les corrige par des indices saisonniers."),
            ("⤴️", "Saut", "Un « saut » dans une série correspond à :",
             ["A. un changement brutal de niveau", "B. une variation douce",
              "C. une erreur de saisie systématique", "D. une tendance saisonnière"], 0,
             "⤴️ Définition : rupture brusque de niveau (nouveau produit, changement de prix, perte de client) ; la moyenne mobile lisse mal ce type d'évolution."),
            ("➖", "Constante", "Une série constante se prévoit par :",
             ["A. la moyenne des valeurs passées", "B. une tendance linéaire",
              "C. un indice saisonnier", "D. le lissage exponentiel avec α = 1"], 0,
             "➖ Définition : niveau stable autour d'une moyenne : la moyenne mobile ou le lissage exponentiel donnent une estimation correcte."),
            ("📏", "Erreur", "L'erreur de prévision se mesure par :",
             ["A. l'écart entre valeur prévue et valeur réalisée",
              "B. le coût d'achat", "C. le délai de livraison",
              "D. le nombre de clients"], 0,
             "📏 Définition : on suit l'erreur moyenne absolue ou le MAPE ; une méthode est choisie selon sa précision et son coût de mise en œuvre."),
            ("🧩", "Choix de la méthode", "Le choix d'une méthode dépend :",
             ["A. de l'horizon, des données disponibles et de la précision requise",
              "B. du prix du produit uniquement",
              "C. du nombre de fournisseurs", "D. du stock de sécurité"], 0,
             "🧩 Définition : court terme + peu de données → méthodes simples ; long terme + historique riche → modèles avec tendance et saisonnalité."),
        ],
    ),
    dict(
        after=167, img="bg_kanban_online.jpg", pos="center 55%", ov=(.87, .93),
        title="Chapitre 5 — Quiz : le Kanban", trans="t-zoom",
        cards=[
            ("🗂️", "Kanban", "Un kanban est :",
             ["A. une carte qui déclenche la fabrication ou le mouvement de pièces",
              "B. un logiciel ERP", "C. un type de stock", "D. une machine"], 0,
             "🗂️ Définition : « fiche signal » en japonais : support visuel qui autorise la production ou le transport d'une quantité standardisée."),
            ("🏯", "Origine", "Le kanban a été développé par :",
             ["A. Toyota, dans le système de production juste-à-temps",
              "B. SAP", "C. Ford", "D. Boeing"], 0,
             "🏯 Définition : issu du Toyota Production System, le kanban est un outil du flux tiré du juste-à-temps."),
            ("⬅️", "Flux tiré", "Dans un flux tiré :",
             ["A. la consommation déclenche la production en aval",
              "B. la production précède la demande",
              "C. on produit pour le stock", "D. les fournisseurs décident"], 0,
             "⬅️ Définition : c'est le besoin du poste aval qui tire la production du poste amont, à l'inverse d'un flux poussé (MRP)."),
            ("🔁", "Boucle", "Le cycle kanban est :",
             ["A. consommation → carte renvoyée → ordre de fabrication → livraison",
              "B. prévision → stock → vente",
              "C. achat → stockage → attente", "D. panne → réparation"], 0,
             "🔁 Définition : la carte accompagne les pièces ; une fois consommées, elle remonte à l'amont et autorise une nouvelle fabrication."),
            ("📉", "Bénéfice", "Le kanban permet surtout de :",
             ["A. réduire les encours et rendre les problèmes visibles",
              "B. augmenter les stocks", "C. allonger les délais",
              "D. supprimer la qualité"], 0,
             "📉 Définition : en limitant le nombre de cartes, on plafonne les encours ; tout blocage apparaît immédiatement et déclenche l'amélioration."),
            ("✅", "Condition", "Le kanban exige :",
             ["A. une production répétitive et des flux relativement stables",
              "B. des produits uniques", "C. des machines peu fiables",
              "D. une demande imprévisible"], 0,
             "✅ Définition : il suppose des références récurrentes, des délais courts, une qualité fiable et une forte discipline des équipes."),
        ],
        title2="Chapitre 5 — Quiz : calcul et conditions", trans2="t-rise",
        cards2=[
            ("🧮", "Nombre de kanbans", "Le nombre de kanbans dépend :",
             ["A. de la demande, du délai, de la marge et de la capacité du conteneur",
              "B. du prix de vente", "C. du nombre de clients",
              "D. du taux d'imposition"], 0,
             "🧮 Définition : N = ⌈(D × T × (1 + marge)) / C⌉ : demande × délai de cycle divisé par la quantité contenue dans un bac."),
            ("🪣", "Conteneur", "Le conteneur kanban sert à :",
             ["A. standardiser la quantité circulant entre deux postes",
              "B. stocker sans limite", "C. emballer pour le client",
              "D. protéger la machine"], 0,
             "🪣 Définition : chaque bac contient une quantité fixe ; le nombre de bacs fixe le stock maximum autorisé dans la boucle."),
            ("⚙️", "Conditions", "Laquelle est requise pour le kanban ?",
             ["A. la fiabilité des machines et la qualité des pièces",
              "B. un stock de sécurité élevé", "C. des fournisseurs multiples",
              "D. de longues séries irrégulières"], 0,
             "⚙️ Définition : sans qualité et sans disponibilité machine, le flux tiré s'interrompt : les kanbans révèlent alors les dysfonctionnements."),
            ("📢", "Conséquence", "Une conséquence du kanban est :",
             ["A. l'implication des opérateurs dans l'amélioration continue",
              "B. la hausse des encours", "C. la baisse de la qualité",
              "D. l'allongement des délais"], 0,
             "📢 Définition : en rendant les flux visibles, le kanban responsabilise les équipes et accélère la résolution des problèmes."),
            ("🚫", "Idée reçue", "Le kanban signifie-t-il « zéro stock » ?",
             ["A. Non : il vise un stock minimal et contrôlé",
              "B. Oui : aucun stock n'est autorisé",
              "C. Oui : uniquement chez le fournisseur",
              "D. Non : il augmente le stock"], 0,
             "🚫 Définition : le kanban plafonne le stock au strict nécessaire (quelques bacs), mais ne supprime pas tout stock tampon."),
            ("🔄", "Kanban vs MRP", "Par rapport au MRP, le kanban est :",
             ["A. un système tiré, réactif et visuel",
              "B. un système poussé calculé par ordinateur",
              "C. une méthode de valorisation", "D. un mode de transport"], 0,
             "🔄 Définition : MRP = flux poussé par le plan ; kanban = flux tiré par la consommation, avec des cartes physiques."),
        ],
    ),
    dict(
        after=180, img="bg_lean_online.jpg", pos="center 50%", ov=(.86, .92),
        title="Chapitre 6 — Quiz : Juste à Temps", trans="t-zoom",
        cards=[
            ("🎯", "Objectifs du JAT", "Le Juste à Temps vise :",
             ["A. produire au bon moment, en bonne quantité, avec le moins de gaspillage",
              "B. produire le plus possible pour le stock",
              "C. augmenter les délais", "D. supprimer la maintenance"], 0,
             "🎯 Définition : produire ce qui est nécessaire, quand il faut, en quantité juste : zéro gaspillage, zéro surstock, zéro défaut, zéro panne."),
            ("🛠️", "Moyens", "Lequel n'est pas un moyen du JAT ?",
             ["A. SMED", "B. maintenance préventive",
              "C. kanban", "D. augmentation systématique des lots"], 3,
             "🛠️ Définition : moyens du JAT : implantation rationalisée, réduction des temps de reconfiguration (SMED), maintenance, kanban, 5S, qualité."),
            ("🏗️", "Implantation", "Rationaliser l'implantation consiste à :",
             ["A. rapprocher les postes et organiser des flux continus / îlots",
              "B. éloigner les machines", "C. augmenter les distances",
              "D. stocker entre chaque poste"], 0,
             "🏗️ Définition : réduire les distances et les déplacements, créer des îlots de production et des flux tendus entre les postes."),
            ("⏱️", "SMED", "L'objectif du SMED est de :",
             ["A. réduire le temps de changement de série",
              "B. augmenter la taille des lots", "C. remplacer la maintenance",
              "D. calculer les stocks"], 0,
             "⏱️ Définition : Single-Minute Exchange of Die : passer d'un produit à un autre en moins de 10 minutes en séparant tâches internes et externes."),
            ("🔧", "Maintenance", "La maintenance préventive :",
             ["A. agit avant la panne selon un plan",
              "B. agit après la panne", "C. attend la panne",
              "D. ne concerne que les bâtiments"], 0,
             "🔧 Définition : préventive = actions programmées ; curative = après panne ; prédictive = surveillance de l'état pour anticiper la panne."),
            ("🤝", "Fournisseurs", "Dans une démarche JAT, les fournisseurs sont :",
             ["A. peu nombreux, partenaires, avec livraisons fréquentes",
              "B. nombreux pour jouer sur les prix",
              "C. choisis au dernier moment", "D. responsables du stock client"], 0,
             "🤝 Définition : le partenariat fournisseur (qualité, délais, livraisons fréquentes et petites quantités) est une condition du flux tendu."),
        ],
        title2="Chapitre 6 — Quiz : amélioration continue", trans2="t-rise",
        cards2=[
            ("💎", "Bénéfices", "Un JAT bien conduit apporte :",
             ["A. trésorerie, qualité et réactivité",
              "B. plus de stock", "C. plus de travail en cours",
              "D. des délais plus longs"], 0,
             "💎 Définition : moins d'encours = trésorerie libérée ; moins de stock = défauts détectés plus vite ; flux courts = meilleure réactivité."),
            ("🧹", "5S", "Le 5S vise principalement :",
             ["A. l'ordre, la propreté et la discipline au poste de travail",
              "B. le calcul de Wilson", "C. le choix du transport",
              "D. la prévision des ventes"], 0,
             "🧹 Définition : Seiri, Seiton, Seiso, Seiketsu, Shitsuke : débarrasser, ranger, nettoyer, standardiser, respecter."),
            ("📉", "Gaspillage", "Un gaspillage (muda) est :",
             ["A. toute activité qui ne crée pas de valeur pour le client",
              "B. une opération nécessaire", "C. un stock de sécurité",
              "D. une commande client"], 0,
             "📉 Définition : surproduction, attente, transport inutile, surtraitement, stock, défauts, mouvements : le JAT cherche à les éliminer."),
            ("🏁", "Conclusion JAT", "La réussite du JAT repose sur :",
             ["A. l'implication de tous et l'amélioration continue",
              "B. un seul logiciel", "C. le hasard",
              "D. l'augmentation des stocks"], 0,
             "🏁 Définition : le JAT est une démarche globale : méthodes, outils et culture d'amélioration continue (kaizen) impliquant tous les acteurs."),
            ("🚚", "Lien logistique", "Le JAT suppose une logistique :",
             ["A. fiable et réactive, avec des flux synchronisés",
              "B. lente mais peu chère", "C. sans suivi",
              "D. à stock élevé"], 0,
             "🚚 Définition : sans transport et approvisionnement fiables, le flux tendu s'interrompt : la logistique est un maillon clé du JAT."),
            ("🧮", "Taille de lot", "Le JAT recommande :",
             ["A. de petits lots et des changements fréquents",
              "B. de très grands lots", "C. de produire pour le stock",
              "D. des livraisons annuelles"], 0,
             "🧮 Définition : petits lots = flexibilité, délais courts et moins d'encours ; rendus possibles par le SMED et la fiabilité machine."),
        ],
    ),
    dict(
        after=212, img="bg_port_day.jpg", pos="center 50%", ov=(.86, .92),
        title="Chapitre 7 — Quiz : logistique & distribution", trans="t-zoom",
        cards=[
            ("🚚", "Distribution physique", "La distribution physique consiste à :",
             ["A. acheminer les produits du producteur jusqu'au client",
              "B. fabriquer les produits", "C. prévoir la demande",
              "D. valoriser le stock"], 0,
             "🚚 Définition : elle couvre le transport, l'entreposage, la manutention et la préparation des commandes jusqu'à la livraison client."),
            ("🏢", "Entrepôt", "Une raison d'exister d'un entrepôt est :",
             ["A. découpler production et consommation / consolider les flux",
              "B. supprimer les transports", "C. remplacer les fournisseurs",
              "D. augmenter les délais"], 0,
             "🏢 Définition : l'entrepôt stocke, consolide, répartit et protège les marchandises entre les étapes de la chaîne."),
            ("🔄", "Circuit produits", "Le circuit typique en entrepôt est :",
             ["A. réception → stockage → préparation → expédition",
              "B. expédition → stockage → réception",
              "C. stockage → commande → réception",
              "D. commande → production → stockage"], 0,
             "🔄 Définition : réception (contrôle), mise en stock, prélèvement / préparation (picking), puis expédition et suivi."),
            ("🧱", "Stockage", "Le stockage en racks permet :",
             ["A. d'utiliser la hauteur et d'organiser les emplacements",
              "B. d'éliminer la manutention", "C. de supprimer les inventaires",
              "D. de valoriser FIFO"], 0,
             "🧱 Définition : racks, palettisation, emplacements codés et méthodes FIFO/LIFO structurent le magasinage et facilitent le picking."),
            ("🗺️", "Réseaux", "Un réseau de distribution peut être :",
             ["A. direct ou passer par des dépôts / plates-formes",
              "B. limité à un seul camion", "C. sans flux d'information",
              "D. identique pour tous les produits"], 0,
             "🗺️ Définition : le nombre et la position des dépôts résultent d'un arbitrage entre coût logistique et délai de service."),
            ("📍", "Affectation", "Affecter des usines aux dépôts consiste à :",
             ["A. choisir quelles usines approvisionnent quels dépôts",
              "B. fixer les prix de vente", "C. nommer les transporteurs",
              "D. calculer les stocks de sécurité"], 0,
             "📍 Définition : optimisation du réseau : minimiser coûts de transport et de stock tout en respectant les délais demandés par les clients."),
        ],
        title2="Chapitre 7 — Quiz : supply chain & transports", trans2="t-rise",
        cards2=[
            ("🔗", "SCM", "Le Supply Chain Management (SCM) est :",
             ["A. la gestion intégrée des flux de l'amont à l'aval",
              "B. la gestion du stock uniquement",
              "C. le transport maritime uniquement",
              "D. la prévision des ventes uniquement"], 0,
             "🔗 Définition : le SCM coordonne les flux physiques, d'information et financiers à travers tout le réseau de partenaires."),
            ("💰", "Coût logistique", "Le coût de la supply chain représente approximativement :",
             ["A. 10 % du chiffre d'affaires", "B. 1 % du CA",
              "C. 50 % du CA", "D. 90 % du CA"], 0,
             "💰 Définition : transport, stockage, manutention et administration logistique pèsent environ 10 % du CA (variable selon les secteurs)."),
            ("⏳", "Différenciation retardée", "La différenciation retardée consiste à :",
             ["A. personnaliser le produit le plus tard possible dans la chaîne",
              "B. personnaliser dès la commande fournisseur",
              "C. standardiser après la livraison", "D. supprimer le transport"], 0,
             "⏳ Définition : garder un produit générique jusqu'au dernier moment pour réduire le stock de variantes et mieux répondre à la demande."),
            ("🛣️", "La route", "Le transport routier est adapté :",
             ["A. aux courtes distances et aux livraisons porte-à-porte",
              "B. aux très longues distances internationales",
              "C. aux gros tonnages uniquement",
              "D. aux seules matières premières"], 0,
             "🛣️ Définition : souple et rapide, mais coûteux au tonne-kilomètre ; idéal pour le dernier kilomètre."),
            ("🚂", "Fer / voie navigable", "Le fer et la voie navigable sont avantageux pour :",
             ["A. les gros volumes sur de longues distances",
              "B. la livraison au client final", "C. les colis express",
              "D. les produits périssables urgents"], 0,
             "🚂 Définition : capacité élevée et faible coût au tonne-km, mais faible souplesse et délais plus longs."),
            ("✈️", "Choix du mode", "Le transport aérien est choisi :",
             ["A. pour les marchandises urgentes et de forte valeur",
              "B. pour les gros tonnages peu chers",
              "C. pour les matières premières en vrac", "D. par défaut pour tout"], 0,
             "✈️ Définition : rapide mais très coûteux : réservé aux produits à forte valeur ajoutée, urgents ou périssables."),
        ],
    ),
]


def make_slide(number, data_i, trans, title, cards_list, foot=True):
    out = []
    out.append('  <section class="slide slide%d %s quiz-compact" data-i="%d" data-t="%s">' %
               (number, trans, data_i, "Zoom" if trans == "t-zoom" else "Ascension"))
    out.append('    <div class="ribbon anim"></div>')
    out.append('    <h2 class="anim">%s</h2>' % title)
    out.append('    <div class="quiz-grid">')
    out.append("\n".join(card(i + 1, *c) for i, c in enumerate(cards_list)))
    out.append('    </div>')
    if foot:
        out.append('    <p class="quiz-foot anim d7">🖱️ Cliquez sur une carte, choisissez la bonne réponse : <b>✅ correct</b> / <b>❌ à revoir</b>, la définition s\'affiche ensuite.</p>')
    out.append('  </section>')
    return "\n".join(out)


def shift(text):
    text = re.sub(r"\.slide(\d+)\b",
                  lambda m: ".slide%d" % remap(int(m.group(1))), text)
    text = re.sub(r'section class="slide slide(\d+)\b',
                  lambda m: 'section class="slide slide%d' % remap(int(m.group(1))), text)
    text = re.sub(r'data-i="(\d+)"',
                  lambda m: 'data-i="%d"' % (remap(int(m.group(1)) + 1) - 1), text)
    text = re.sub(r"SLIDE (\d+)",
                  lambda m: "SLIDE %d" % remap(int(m.group(1))), text)
    text = re.sub(r'(?m)^(\s*)\[(\d+),(\s*)"',
                  lambda m: "%s[%d,%s\"" % (m.group(1), remap(int(m.group(2))), m.group(3)), text)
    return text


def main():
    html = open(PATH, encoding="utf-8").read()
    html = shift(html)

    # Insertion en ordre decroissant pour ne pas decaler les marqueurs suivants
    quiz_numbers = []
    for st in sorted(SETS, key=lambda x: -x["after"]):
        k = remap(st["after"])
        marker = '<section class="slide slide%d ' % k
        assert html.count(marker) == 1, "marqueur introuvable : " + marker
        start = html.index(marker)
        end = html.index("</section>", start) + len("</section>")
        n1, n2 = k + 1, k + 2
        quiz_numbers += [n1, n2]
        block = "\n\n" + make_slide(n1, n1 - 1, st["trans"], st["title"], st["cards"]) + "\n\n" \
                + make_slide(n2, n2 - 1, st["trans2"], st["title2"], st["cards2"]) + "\n"
        html = html[:end] + block + html[end:]
        print("+ quiz %d-%d apres slide %d" % (n1, n2, k))

    # CSS de rattrapage pour les nouvelles slides (avant le bloc d'alignement)
    nums = sorted(quiz_numbers)
    sels = ", ".join(".slide%d" % n for n in nums)
    sels_h = ", ".join(".slide%d h2" % n for n in nums)
    sels_r = ", ".join(".slide%d .ribbon" % n for n in nums)
    css = (
        "/* ===== Correctif titres : quiz des chapitres 3 a 7 ===== */\n"
        + sels + " { flex-direction:column; }\n"
        + sels_h + " {\n  font-size:3vw; color:#fff; font-weight:700; margin-bottom:.5%;\n"
        "  align-self:flex-start;\n}\n"
        + sels_r + " {\n  width:8%; height:5px; background:linear-gradient(90deg,#f39c12,#e74c3c);\n"
        "  border-radius:5px; margin-bottom:3%; align-self:flex-start;\n}\n"
        "/* Verso plus dense : les definitions longues restent visibles */\n"
        ".quiz-compact .quiz-grid { height:78%; }\n"
        ".quiz-compact .quiz-face { gap:2.5%; padding:3% 6%; }\n"
        ".quiz-compact .q-opt { font-size:.86vw; line-height:1.25; padding:.55% 1.2%; }\n"
        ".quiz-compact .q-def { font-size:.78vw; line-height:1.3; padding:1% 1.5%; }\n"
        ".quiz-compact .q-verdict { font-size:.8vw; min-height:1vw; }\n\n"
    )
    mark = "/* ===== Alignement vertical des titres ===== */"
    assert html.count(mark) == 1
    html = html.replace(mark, css + mark, 1)

    html = html.replace('<span id="tot">212</span>', '<span id="tot">224</span>')
    open(PATH, "w", encoding="utf-8", newline="\n").write(html)
    print("OK : 12 slides de quiz ajoutees, total %d slides" % TOTAL)


if __name__ == "__main__":
    main()

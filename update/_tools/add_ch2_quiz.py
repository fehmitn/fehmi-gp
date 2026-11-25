# -*- coding: utf-8 -*-
"""Ajoute 2 slides de quiz a la fin du chapitre 2 (apres l'ancienne slide 68).

Les slides 69..210 deviennent 71..212. Le script decale :
  - .slideN en CSS, .slideN dans les <section>, data-i, commentaires SLIDE N,
  - entrees TOC des chapitres 3..7,
  - puis insere les deux nouvelles slides (69 et 70, data-i 68 et 69).
"""
import io
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
PATH = r"C:\ppt\index.html"

# ---------------------------------------------------------------- quiz HTML

def card(num, ico, word, question, opts, answer, definition):
    """opts = liste de 4 chaines 'A. ...' ; answer = index (0-based) de la bonne."""
    lines = []
    lines.append('      <div class="quiz-item anim d%d">' % num)
    lines.append('        <div class="quiz-face quiz-front">')
    lines.append('          <div class="q-ico">%s</div>' % ico)
    lines.append('          <div class="q-wd">%s</div>' % word)
    lines.append('          <div class="q-hint">🖱️ cliquez pour le quiz</div>')
    lines.append('        </div>')
    lines.append('        <div class="quiz-face quiz-back">')
    lines.append('          <div class="q-back">↩︎ retour</div>')
    lines.append('          <div class="q-quest">%s</div>' % question)
    for i, o in enumerate(opts):
        attr = ' data-ok="1"' if i == answer else ""
        lines.append('          <div class="q-opt"%s>%s</div>' % (attr, o))
    lines.append('          <div class="q-verdict"></div>')
    lines.append('          <div class="q-def">%s</div>' % definition)
    lines.append('        </div>')
    lines.append('      </div>')
    return "\n".join(lines)


QUIZ1 = """  <!-- ============ SLIDE 69 : CHAPITRE 2 — QUIZ PLANIFICATION ============ -->
  <section class="slide slide69 t-zoom" data-i="68" data-t="Zoom">
    <div class="ribbon anim"></div>
    <h2 class="anim">Chapitre 2 — Quiz : la planification</h2>
    <div class="quiz-grid">
%s
    </div>
    <p class="quiz-foot anim d7">🖱️ Cliquez sur une carte, choisissez la bonne réponse : <b>✅ correct</b> / <b>❌ à revoir</b>, la définition s'affiche ensuite.</p>
  </section>
""" % "\n".join([
    card(1, "📅", "PIC", "Le Plan Industriel et Commercial (PIC), c'est :", [
        "A. le détail des opérations machine par machine",
        "B. la programmation des livraisons quotidiennes",
        "C. un plan global d'activité à moyen terme, par famille de produits",
        "D. le calcul des besoins en composants",
    ], 2, "📅 Définition : le PIC traduit prévisions et commandes en activité globale par famille de produits, à moyen terme (mois), en vérifiant la charge globale."),
    card(2, "🗓️", "PDP", "Le Plan Directeur de Production (PDP) sert à :", [
        "A. décomposer le PIC par produit et par période, puis vérifier la capacité",
        "B. remplacer le calcul des besoins",
        "C. fixer les prix de vente",
        "D. planifier la maintenance",
    ], 0, "🗓️ Définition : le PDP détaille le PIC en produits finis et en périodes (semaines / mois) ; il constitue l'entrée du calcul des besoins (MRP)."),
    card(3, "🧮", "Calcul des besoins", "Le MRP calcule les besoins en composants à partir de :", [
        "A. des seules commandes fournisseurs",
        "B. du PDP, de la nomenclature (BOM) et des stocks",
        "C. du plan de charge uniquement",
        "D. des prévisions de ventes seules",
    ], 1, "🧮 Définition : besoins bruts (PDP) → besoins nets (– stocks et réceptions attendues) → ordres planifiés, grâce aux nomenclatures et aux délais."),
    card(4, "📊", "Plan de charge", "Un plan de charge permet de :", [
        "A. comparer la charge prévue à la capacité disponible par poste et par période",
        "B. calculer le stock de sécurité",
        "C. établir la nomenclature",
        "D. tracer un diagramme de Gantt",
    ], 0, "📊 Définition : il répartit la charge de travail par poste et par période, la compare à la capacité, puis permet de détecter les surcharges et de lisser la production."),
    card(5, "🗓️", "Ordonnancement", "L'ordonnancement consiste à :", [
        "A. prévoir les ventes à moyen terme",
        "B. fixer l'ordre et les dates des opérations sur les moyens disponibles",
        "C. gérer les commandes d'achat",
        "D. clôturer la comptabilité",
    ], 1, "🗓️ Définition : placer les opérations dans le temps et sur les ressources, en respectant les contraintes de capacité et les délais — décision à court terme."),
    card(6, "📈", "Diagramme de Gantt", "Un diagramme de Gantt représente :", [
        "A. les stocks en fonction du temps",
        "B. les tâches en fonction du temps, avec début, durée et avancement",
        "C. la nomenclature des produits",
        "D. le plan de charge global",
    ], 1, "📈 Définition : graphique temps / tâches : chaque barre montre le début, la durée et la fin d'une opération — outil de suivi de l'avancement."),
])

QUIZ2 = """  <!-- ============ SLIDE 70 : CHAPITRE 2 — QUIZ MRP / MRP2 ============ -->
  <section class="slide slide70 t-rise" data-i="69" data-t="Ascension">
    <div class="ribbon anim"></div>
    <h2 class="anim">Chapitre 2 — Quiz : MRP / MRP2 et exploitation</h2>
    <div class="quiz-grid">
%s
    </div>
    <p class="quiz-foot anim d7">🖱️ Cliquez sur une carte, choisissez la bonne réponse : <b>✅ correct</b> / <b>❌ à revoir</b>, la définition s'affiche ensuite.</p>
  </section>
""" % "\n".join([
    card(1, "🔗", "Besoins", "Un besoin dépendant est un besoin :", [
        "A. exprimé directement par le client",
        "B. issu uniquement de la prévision commerciale",
        "C. calculé à partir d'un autre besoin (composants d'un produit fini)",
        "D. sans lien avec la production",
    ], 2, "🔗 Définition : besoin indépendant = produit fini (clients / prévisions) ; besoin dépendant = composants calculés à partir du PDP et de la nomenclature."),
    card(2, "⚙️", "MRP2", "Le MRP2 ajoute au MRP :", [
        "A. la gestion de la capacité (plan de charge, capacité finie)",
        "B. la prévision des ventes",
        "C. la facturation client",
        "D. le Plan Industriel et Commercial",
    ], 0, "⚙️ Définition : le MRP calcule les besoins en composants (capacité infinie) ; le MRP2 y ajoute le plan de charge avec capacité finie et le retour d'information."),
    card(3, "✅", "Conditions d'implantation", "Pour implanter le MRP, il faut d'abord :", [
        "A. disposer de données fiables (nomenclatures, stocks, délais, PDP)",
        "B. supprimer tous les stocks",
        "C. augmenter les effectifs",
        "D. acheter un ERP",
    ], 0, "✅ Définition : le MRP exige des données exactes et à jour : nomenclature (BOM), stocks, délais d'approvisionnement et plan directeur de production."),
    card(4, "🔁", "Cercle pervers", "Le cercle pervers décrit :", [
        "A. la baisse des stocks sans conséquence",
        "B. l'engrenage retards → heures supplémentaires → surcharge → nouveaux retards",
        "C. la hausse régulière de la productivité",
        "D. le lissage du plan de charge",
    ], 1, "🔁 Définition : plus on est en retard, plus on ajoute d'heures et de priorités, ce qui désorganise la production et génère de nouveaux retards."),
    card(5, "💰", "Progresser", "Un cycle court et peu de stocks permettent :", [
        "A. un gain de trésorerie et une meilleure réactivité",
        "B. une hausse des stocks de sécurité",
        "C. des délais de livraison plus longs",
        "D. davantage de travail en cours",
    ], 0, "💰 Définition : réduire les délais et les encours libère de la trésorerie et ouvre de nouveaux marchés, même si la comptabilité valorise peu ces gains."),
    card(6, "🏁", "Bonus : capacité", "Dans le MRP de base, la capacité est considérée comme :", [
        "A. finie",
        "B. infinie",
        "C. nulle",
        "D. variable",
    ], 1, "🏁 Définition : le MRP ignore d'abord la capacité (hypothèse infinie) ; le MRP2 introduit la capacité finie grâce au plan de charge."),
])

# ---------------------------------------------------------------- decalage

def shift(text):
    # CSS et HTML : .slideN / slide slideN
    text = re.sub(r"\.slide(\d+)\b",
                  lambda m: ".slide%d" % (int(m.group(1)) + 2 if int(m.group(1)) >= 69 else int(m.group(1))),
                  text)
    text = re.sub(r'section class="slide slide(\d+)\b',
                  lambda m: 'section class="slide slide%d' % (int(m.group(1)) + 2 if int(m.group(1)) >= 69 else int(m.group(1))),
                  text)
    text = re.sub(r'data-i="(\d+)"',
                  lambda m: 'data-i="%d"' % (int(m.group(1)) + 2 if int(m.group(1)) >= 68 else int(m.group(1))),
                  text)
    text = re.sub(r"SLIDE (\d+)",
                  lambda m: "SLIDE %d" % (int(m.group(1)) + 2 if int(m.group(1)) >= 69 else int(m.group(1))),
                  text)
    # entrees TOC (chapitres 3 a 7)
    text = re.sub(r"(?m)^(\s*)\[(\d+),(\s*)\"",
                  lambda m: "%s[%d,%s\"" % (m.group(1),
                                          int(m.group(2)) + 2 if int(m.group(2)) >= 69 else int(m.group(2)),
                                          m.group(3)),
                  text)
    return text


def main():
    html = open(PATH, encoding="utf-8").read()
    assert html.count('<section class="slide slide69 ') == 1, "insertion point introuvable"
    html = shift(html)

    marker = '<section class="slide slide71 '
    assert html.count(marker) == 1, "chapitre 3 introuvable apres decalage"
    html = html.replace(marker, QUIZ1 + "\n" + QUIZ2 + "\n\n" + marker, 1)
    html = html.replace('<span id="tot">210</span>', '<span id="tot">212</span>')
    open(PATH, "w", encoding="utf-8", newline="\n").write(html)
    print("OK : 2 slides de quiz ajoutees (69-70), total 212 slides")


if __name__ == "__main__":
    main()

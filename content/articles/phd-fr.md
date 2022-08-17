Title: Typage Bidirectionnel pour le Calcul des Constructions Inductives
Slug: phd
Category: Thèse
Lang: fr
Date: 2022-06-24
Pdf_loc: 22-phd.pdf
Github: https://github.com/MevenBertrand/PhD-Thesis

Durant leurs plus de 50 ans d'existence, les assistants à la preuve
se sont établis comme des outils permettant un haut niveau
de fiabilité dans de nombreuses applications.
Cependant, du fait de leur complexité grandissante, la solution historique de faire confiance à
un petit noyau stable n'est plus suffisante pour avancer en évitant des bugs critiques.
Mais les assistants à la preuve sont utilisés depuis des décennies pour certifier la
correction de programmes, pourquoi pas *la leur* ?
C'est l'ambition du projet MetaCoq,
visant à construire le premier noyau réaliste à la correction formellement prouvée,
pour l'assistant à la preuve Coq.
Ne faites plus confiance au programme, seulement à sa preuve !

Cette thèse étudie la structure bidirectionnelle qui sous-tend
l'algorithme de typage implémenté par le noyau de Coq,
dans le contexte du Calcul des Constructions Inductives (CIC) qui fonde celui-ci.
Le tout est formalisé dans le cadre de MetaCoq, et constitue
un passage obligé pour atteindre l'objectif du projet, fournissant
un intermédiaire entre l’implémentation et sa spécification.
Enfin, le contrôle renforcé sur le calcul offert par le typage bidirectionnel
est une pièce nécessaire à la conception d'une extension graduelle
de CIC, qui vise à apporter au développement en Coq la flexibilité
du typage dynamique et constitue la dernière partie de la thèse.
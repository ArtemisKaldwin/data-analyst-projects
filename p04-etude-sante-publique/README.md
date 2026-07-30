# P4 — Étude de sécurité alimentaire mondiale (données FAO)

**Outils :** Python, pandas
**Fichiers de ce dossier :** `notebook.ipynb` (code, sorties retirées), `notebook_export.pdf` (rendu complet avec graphiques), `presentation.pptx`

## Contexte / besoin métier

Comprendre pourquoi la sous-nutrition persiste dans le monde alors que la production alimentaire mondiale est théoriquement suffisante, et identifier les paradoxes entre production, export et sous-nutrition domestique.

## Données

Quatre tables FAO croisées par pays et année (référence 2017) :
- `population` (zone / année / population)
- `disponibilité alimentaire` (zone / produit / origine animale ou végétale / kcal, kg, matières grasses par personne)
- `aide alimentaire` (pays bénéficiaire / année / produit / valeur, depuis 2013)
- `sous-nutrition` (zone / année / valeur)

## Démarche

- Jointures pandas et agrégations (`groupby`) pour construire une vue consolidée par pays.
- Construction d'indicateurs : proportion de sous-nutrition, disponibilité calorique théorique par personne (référence 2 400 puis 2 100 kcal), part des céréales destinée à l'alimentation animale vs humaine.
- Étude de cas ciblée : la Thaïlande, premier exportateur mondial de manioc, pour illustrer le paradoxe production-export-sous-nutrition.

## Résultats + impact / recommandations

- La production calorique mondiale actuelle pourrait théoriquement nourrir **136%** de la population mondiale (112% avec les seules calories végétales).
- **7,1%** de la population mondiale (environ 535 millions de personnes) est sous-alimentée en 2017.
- **4,65%** des ressources alimentaires mondiales sont perdues ou gaspillées.
- **36,29%** des céréales produites sont destinées à l'alimentation animale plutôt qu'humaine.
- Cas Thaïlande : 83,4% de la production de manioc est exportée, mais 9,0% de la population reste sous-alimentée malgré ce statut de premier exportateur mondial.
- Pays les plus touchés par la sous-nutrition (Haïti, Corée du Nord, Madagascar, Libéria...) ne correspondent pas directement aux pays recevant le plus d'aide alimentaire (Syrie, Éthiopie, Yémen...), un écart révélateur d'une possible inefficacité dans l'allocation de l'aide.

## Limites + prochaines pistes

- Analyse descriptive et corrélative, sans test statistique formel pour confirmer les écarts observés.
- Choix méthodologiques discutés en cours de projet (quelle référence calorique retenir, quelle liste de céréales inclure), documentés mais non arbitrés de façon définitive.
- Piste : croiser ces données avec des indicateurs économiques et politiques pour expliquer l'écart entre pays aidés et pays réellement sous-alimentés.

---

*Note : les sorties (graphiques, tableaux) du notebook ont été retirées pour réduire la taille du fichier sur ce repo. Le rendu complet avec visualisations est disponible dans `notebook_export.pdf`, dans ce même dossier.*

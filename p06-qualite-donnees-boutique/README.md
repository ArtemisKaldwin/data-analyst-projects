# P6 — Qualité de données pour une boutique en ligne (Bottleneck)

**Outils :** Python, pandas
**Fichiers de ce dossier :** `notebook.ipynb` (code, sorties retirées), `notebook_export.pdf` (rendu complet avec graphiques), `presentation.pdf`

## Contexte / besoin métier
Boutique de spiritueux vendant sur deux canaux (ERP interne et site web), avec des données fragmentées (prix erronés, doublons, références manquantes). Objectif : consolider les bases et fiabiliser les données pour orienter les décisions de gestion de stock.

## Données
- `erp.xlsx` (825 lignes) : ID produit, prix d'achat, prix de vente, quantité en stock.
- `web.xlsx` (1 513 lignes) : SKU, ventes totales, statut de mise en vente, image, visibilité.
- `liaison.xlsx` (825 lignes) : table de correspondance ID interne / ID web.
- 100% conforme RGPD, aucune donnée personnelle.

## Démarche
Jointures (ERP avec liaison en jointure interne, puis avec le web en jointure complète), détection d'anomalies (méthode IQR à 1,5×, Z-score à partir de 3), puis analyse des prix, du chiffre d'affaires, des quantités, des marges et des corrélations entre variables.

## Résultats + impact / recommandations
- 22 anomalies corrigées (prix manquants ou négatifs, doublons, SKU absents, images manquantes).
- 111 références présentes en ERP mais absentes du site web.
- 19 valeurs aberrantes de prix identifiées, correspondant aux alcools forts et bouteilles de prestige.
- **Chiffre d'affaires total analysé : 143 680 €.**
- Loi 80/20 confirmée : 433 références (52,5% du catalogue) réalisent 80% des ventes en quantité.
- Valorisation totale des stocks : 298 540 €, avec une rotation moyenne de 3 mois mais certaines références (champagnes de prestige) immobilisées jusqu'à 31 mois.
- 4 références identifiées à marge négative, à corriger en priorité.

## Limites + prochaines pistes
Corrélations présentées de façon descriptive, sans test statistique formalisant leur significativité. Détection d'outliers strictement univariée sur le prix (Z-score, IQR), incapable de repérer un article dont le prix est normal mais dont la combinaison stock/ventes est atypique. Piste : automatiser les contrôles de cohérence entre ERP et site web via un dictionnaire de données partagé.

**Ces deux limites ont été traitées dans une itération ultérieure** — voir [`mission1-amelioration-ia/`](./mission1-amelioration-ia) ci-dessous.

## Amélioration critique augmentée par l'IA (Mission 1)

Ce notebook a servi de base à un exercice distinct : l'améliorer de façon critique et documentée à l'aide de l'IA, en comparant plusieurs options et en justifiant chaque choix (qualité, biais, coût, reproductibilité, conformité) plutôt qu'en acceptant une suggestion telle quelle.

- **Veille technologique** : comparaison de trois méthodes de détection d'anomalies multivariées (Isolation Forest, Local Outlier Factor, One-Class SVM), Isolation Forest retenu et justifié.
- **Nouveau résultat obtenu** : 19 articles ont une combinaison stock/ventes anormale invisible à l'analyse de prix univariée du notebook original — la preuve chiffrée de la limite identifiée en veille.
- **Validation statistique ajoutée** : tests de significativité (Pearson + Spearman, p-values) sur les corrélations, qui révèlent une relation forte entre stock et prix d'achat (Spearman r=-0,55, p<0,0001) totalement invisible à un simple coefficient de Pearson (r=-0,02).
- **Incident détecté et corrigé, documenté sans le masquer** : le premier brouillon du notebook amélioré contenait un bug de formatage (sauts de ligne perdus dans 17 cellules) qui empêchait toute exécution. Diagnostiqué, corrigé, puis le notebook a été réellement exécuté de bout en bout (0 erreur sur 92 cellules) avant de considérer le livrable fiable.

Dossier complet, avec cahier des charges, organisation projet (lots, backlog, risques) et documentation : [`mission1-amelioration-ia/`](./mission1-amelioration-ia).

---

*Note : les sorties (graphiques, tableaux) du notebook ont été retirées pour réduire la taille du fichier sur ce repo. Le rendu complet avec visualisations est disponible dans `notebook_export.pdf`, dans ce même dossier.*

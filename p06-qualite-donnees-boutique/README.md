# P6 — Qualité de données pour une boutique en ligne (Bottleneck)

**Outils :** Python, pandas

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
Corrélations présentées de façon descriptive, sans test statistique formalisant leur significativité. Piste : automatiser les contrôles de cohérence entre ERP et site web via un dictionnaire de données partagé.

---

*Note : les sorties (graphiques, tableaux) du notebook ont été retirées pour réduire la taille du fichier sur ce repo. Le rendu complet avec visualisations est disponible dans l'export PDF cité dans la fiche portfolio.*

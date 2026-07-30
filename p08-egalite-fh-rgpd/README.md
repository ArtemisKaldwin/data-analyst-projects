# P8 — Indicateurs d'égalité femmes-hommes en conformité RGPD

**Outils :** KNIME (pipeline ETL visuel), export CSV

## Contexte / besoin métier
Cabinet de plus de 150 salariés, soumis à l'obligation légale de publier son index d'égalité professionnelle femmes-hommes (obligatoire au-delà de 50 salariés, publication avant le 1er mars). Mission mandatée par la DRH, avec un enjeu RSE fort.

## Données
Fichiers Salariés, Rémunération et Informations professionnelles issus du SIRH, joints via un pipeline KNIME de 28 nœuds. Conformité RGPD assurée par minimisation des données : les colonnes non nécessaires au calcul de l'index sont supprimées avant tout export, produisant un CSV anonymisé.

## Démarche
Pipeline KNIME : import et nettoyage, jointures RH, agrégation par sexe, type de contrat, ancienneté et temps de travail, visualisations (diagrammes en barres, camemberts, boîtes à moustaches), export vers Power BI/Tableau. Indicateurs calculés selon le référentiel du Ministère du Travail (index sur 100 points) : écart de rémunération (40 pts), écart de taux d'augmentation (20 pts), écart de taux de promotion (15 pts), augmentations au retour de congé maternité (15 pts), parité du top 10 des rémunérations (10 pts).

## Résultats + impact / recommandations
- **Score global : 85/100.**
- Taux d'augmentation légèrement favorable aux femmes (67% contre 61% chez les hommes).
- Taux de promotion comparable entre les deux sexes (environ 18% contre 17%).
- Écart identifié dans le top 10 des rémunérations : environ 70% d'hommes contre 30% de femmes, révélant un plafond de verre malgré des indicateurs globalement équilibrés en bas et milieu de distribution.

## Limites + prochaines pistes
Les écarts significatifs se concentrent en haut de la distribution des salaires et ne sont pas visibles sur les indicateurs médians. Piste : action RH ciblée sur l'accès des femmes aux postes les mieux rémunérés plutôt que sur les écarts globaux.

# P7 — Dashboard de suivi de portefeuille de projets

**Outils :** Power BI

## Contexte / besoin métier
Suivre l'avancement d'un portefeuille de projets multi-pays et multi-types (IT, marketing...) : budgets, délais, livrables et couverture géographique, dans un outil de pilotage unique et dynamique.

## Données
Tables Projects_plans, Projects_Locations, Actual_Costs, Actual_Duration, Project type, table de dates, et une table de suivi de visites sécurité.

## Démarche
Dashboard construit en 11 pages : synthèse globale, tops et analyses clés, retards et durées, budgets et coûts, livrables, répartition par pays, types de projets et portefeuille, planning (Gantt), mise à jour, modèle de données, infobulles. Visuels : cartes KPI, colonnes groupées, carte Azure, treemap, nuage de points, graphique combiné, Gantt personnalisé, jauges.

## Résultats + impact / recommandations
Mesures construites autour de l'écart budgétaire (planifié vs réel), du taux de projets en retard, de la durée moyenne planifiée vs réelle et du taux de réalisation des livrables, avec un classement des pays les plus en retard ou en dépassement budgétaire pour prioriser les actions correctives.

## Limites + prochaines pistes
Projet sans présentation écrite associée : le contexte métier précis (secteur, commanditaire) n'est pas documenté au-delà du contenu du dashboard lui-même. Piste : associer une note de cadrage au dashboard pour faciliter sa prise en main par de nouveaux utilisateurs.

# P3 — Requêtage d'une base de contrats d'assurance habitation

**Outils :** SQL (MySQL Workbench, SQL Power Architect)
**Fichiers de ce dossier :** `1_document_technique.pdf` (schéma relationnel et choix techniques), `2_liste_requetes.pdf` (les 12 requêtes SQL avec leurs résultats), `3_methodologie.pdf`, `4_grille.pdf` (grille d'auto-évaluation)

## Contexte / besoin métier
Analyser les données de contrats d'assurance habitation d'une entreprise pour comprendre le marché et orienter des décisions stratégiques, à partir d'une base relationnelle à construire.

## Données
Deux tables reliées par une clé étrangère commune (code département + code commune) : `Contrat` (30 335 lignes) et `Région` (38 916 lignes), volumes vérifiés par comptage SQL.

## Démarche
Exploration des données sources, construction d'un dictionnaire de données, modélisation du schéma relationnel (SQL Power Architect), création des tables MySQL, import via assistant, contrôle d'intégrité, puis rédaction de 12 requêtes SQL répondant à des questions métier précises.

## Résultats + impact / recommandations
Questions métier couvertes par les requêtes : localisation des contrats par commune et département, classement des départements par cotisation moyenne, nombre de contrats par région, top 5 des surfaces les plus élevées, surface moyenne à Paris, prix moyen de cotisation mensuelle, nombre de formules "Integral" en Pays de la Loire, répartition par catégorie de valeur déclarée, communes comptant au moins 150 contrats.

## Limites + prochaines pistes
Livrable purement méthodologique et technique, sans synthèse business au-delà des résultats bruts des requêtes. Piste : transformer ces requêtes en tableau de bord exploitable directement par les équipes commerciales.

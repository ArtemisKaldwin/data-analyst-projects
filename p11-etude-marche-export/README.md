# P11 — Étude de marché export pour une filière avicole bio

**Outils :** Python, pandas, scikit-learn (ACP, KMeans, CAH)
**Livrables sources :** rapport de préparation/nettoyage (PDF), rapport de clustering (PDF), présentation (PDF)

## Contexte / besoin métier

Une entreprise française de poulet bio premium (nom du cas : "La Poule qui Chante") fait face à un marché domestique saturé et cherche, pour son COMEX, à identifier les marchés export à cibler en priorité.

## Données

125 pays, 22 variables (11 indicateurs sur 2 années, 2021 et 2022), issues de trois sources :
- Banque Mondiale : PIB par habitant, croissance, inflation, population, urbanisation, émissions de CO2 par habitant, tarif douanier, stabilité politique, contrôle de la corruption.
- FAO : consommation de viande en kcal/jour, importations de poulet.
- CEPII : distance pondérée depuis la France, codes ISO pays.

Nettoyage : suppression des doublons pays (Chine, Nigeria, Afrique du Sud apparaissaient chacun 4 fois) pour revenir à 125 pays uniques, retrait d'une variable trop lacunaire (`logistics_index`), standardisation (`StandardScaler`) avant analyse.

## Démarche

1. Analyse en composantes principales (ACP) pour l'exploration : 6 composantes retenues, 80,26% de variance expliquée. Première composante (33,76%) interprétée comme "développement économique", deuxième (14,06%) comme "taille de marché", troisième (11,39%) comme "instabilité conjoncturelle".
2. Clustering KMeans sur les données standardisées : le K optimal statistiquement (coude, silhouette) est 3, mais jugé trop grossier pour une décision commerciale. K=6 retenu pour des raisons métier.
3. Classification ascendante hiérarchique (méthode de Ward) en complément, pour affiner les 6 groupes en 20 profils plus fins et permettre un ciblage plus précis.

## Résultats + impact / recommandations

- Profils identifiés en K=6 : Europe et OCDE (41 pays, cible prioritaire), Chine (isolée, marché géant), 30 pays émergents dynamiques (cible moyen terme), 46 pays en développement (trop hétérogènes pour une action directe), 6 pays instables (à exclure), Inde (isolée, consommation de viande très faible).
- Le raffinement en 20 groupes fait ressortir deux priorités : l'Europe occidentale (8 pays dont Allemagne, France, Royaume-Uni, Belgique, proximité logistique et bio déjà valorisé) et l'Europe du Nord ultra-premium (6 pays dont Luxembourg, Suisse, Danemark, marges potentielles maximales).
- **Recommandation finale : cibler en priorité 14 pays d'Europe occidentale et du Nord à court terme**, avec l'Amérique latine émergente et certains marchés asiatiques dynamiques en cibles moyen terme. Exclusion explicite de l'Inde (culture alimentaire majoritairement végétarienne) et des pays en crise politique ou économique (Liban, Zimbabwe, Iran, Ukraine, Turquie au moment de l'étude).

## Limites + prochaines pistes

- Le nombre de clusters statistiquement optimal (3) a été volontairement écarté au profit d'un découpage plus actionnable (6, puis 20) : ce choix reste un arbitrage métier assumé, pas un optimum mathématique.
- Le groupe des 46 pays en développement reste hétérogène malgré la CAH complémentaire, ce que les auteurs du rapport signalent eux-mêmes comme une limite.
- Piste : affiner l'analyse des 14 pays prioritaires avec des données de réglementation import/export spécifiques au secteur avicole bio.

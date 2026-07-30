# P5 — Base de données relationnelle immobilière

**Outils :** SQL (MySQL), DBeaver

## Contexte / besoin métier
Projet "DATAImmo" : structurer des données immobilières hétérogènes (DVF, INSEE) en une base relationnelle fiable et conforme RGPD, pour permettre des analyses croisées géographiques et démographiques.

## Données
DVF (Demandes de Valeurs Foncières, data.gouv.fr) pour les ventes immobilières, données INSEE de recensement par commune, référentiel géographique communes/départements/régions.

## Démarche
Encodage UTF-8, suppression des caractères non imprimables, normalisation des codes géographiques, création d'identifiants uniques. SGBD MySQL retenu plutôt que SQLite pour la gestion des contraintes de clés étrangères à volume important. Étapes : création des tables avec clés primaires/étrangères, nettoyage des CSV, import progressif, contrôle de conformité (comptage de lignes, vérification des clés étrangères et des types).

## Résultats + impact / recommandations
- **31 378 appartements vendus** analysés sur le premier semestre 2020, l'Île-de-France en tête des volumes de vente.
- Répartition par nombre de pièces : 2 pièces (31,2%), 3 pièces (28,6%), 1 pièce (21,5%).
- Prix au m² les plus élevés : Paris (11 978 €), Hauts-de-Seine (7 303 €), Val-de-Marne (5 118 €).
- Écart de prix au m² de 12,4% entre un 2 pièces et un 3 pièces.
- Évolution des ventes de +3,68% entre le premier et le deuxième trimestre 2020.

## Limites + prochaines pistes
Schéma relationnel volontairement simple (deux tables principales) pour ce périmètre. Certaines pages de la présentation contenaient des schémas visuels non retranscrits ici. Piste : enrichir le schéma avec une table dédiée aux caractéristiques du bien pour affiner les analyses de prix.

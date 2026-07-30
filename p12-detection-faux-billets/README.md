# P12 — Détection de faux billets par machine learning

**Outils :** Python, pandas, scikit-learn
**Livrables sources :** notebook d'analyse (PDF), script d'application (`.pkl`), notebook de test (PDF), présentation (PDF)

## Contexte / besoin métier

Mission pour l'ONCFM (Organisation Nationale de Lutte Contre le Faux-Monnayage) : construire un outil capable de classer automatiquement un billet comme vrai ou faux à partir de mesures géométriques, et le livrer sous une forme réutilisable en production (script, pas seulement un notebook).

## Données

- 1 500 billets, 6 variables géométriques : `diagonal`, `height_left`, `height_right`, `margin_low`, `margin_up`, `length`.
- Répartition : 1 000 vrais billets (66,7%), 500 faux (33,3%).
- 37 valeurs manquantes sur `margin_low` (2,5% du jeu de données), imputées par un Random Forest Regressor entraîné sans la variable cible (`is_genuine`) pour éviter toute fuite de données. Répartition des valeurs manquantes vérifiée entre classes (29 vrais / 8 faux) pour écarter un biais d'imputation.
- Corrélations avec la variable cible : `length` (+0,85), `margin_low` (-0,78), `margin_up` (-0,61), `height_right` (-0,49), `height_left` (-0,38), `diagonal` (+0,13, quasi inutile).

## Démarche

1. Prétraitement : split train/validation/test (64/16/20), stratifié, `StandardScaler`.
2. Trois modèles comparés : régression logistique, KNN (k=5), forêt aléatoire (100 arbres) ; un KMeans non supervisé (2 clusters) en complément exploratoire.
3. Analyse en composantes principales pour vérifier la séparabilité (2 composantes expliquent 60% de la variance, la première composante seule sépare nettement les deux classes).
4. `GridSearchCV` sur la régression logistique (36 combinaisons d'hyperparamètres), optimisé sur le **recall des faux billets** plutôt que l'accuracy globale : dans ce contexte métier, laisser passer un faux billet coûte plus cher qu'un faux positif sur un vrai billet.
5. Validation croisée à 5 plis pour confirmer la stabilité du modèle retenu.

## Résultats + impact / recommandations

- Modèle final : régression logistique optimisée (`C=0,1`, solver `liblinear`, pipeline `StandardScaler + LogisticRegression`).
- **Recall sur les faux billets : 99%** (1 faux billet manqué sur 100 en moyenne).
- AUC = 1,000 en validation croisée, écart train/validation quasi nul (pas de surapprentissage détecté).
- Script déployable livré avec deux fonctions : `predire_billets()` (entrée dictionnaire ou liste de dictionnaires) et `predire_depuis_csv()` (chargement direct d'un CSV), toutes deux basées sur le modèle sérialisé `model_final.pkl` et retournant la prédiction avec sa probabilité associée.
- Testé sur un jeu de production simulé (5 billets) : prédictions cohérentes avec des probabilités de confiance comprises entre 90% et 99,6%.

## Limites + prochaines pistes

- Jeu de données de taille modeste (1 500 billets), ce qui limite la capacité du modèle à généraliser à des types de faux billets non représentés dans l'échantillon.
- 2,5% des valeurs d'entrée sont imputées plutôt que mesurées directement : à surveiller si la proportion de valeurs manquantes augmente en production.
- Piste : élargir l'échantillon d'entraînement et réévaluer périodiquement le modèle face à de nouvelles techniques de contrefaçon.

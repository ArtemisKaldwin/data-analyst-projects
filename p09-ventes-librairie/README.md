# P9 — Analyse des ventes d'une librairie en ligne

**Outils :** Python, pandas, SciPy
**Fichiers de ce dossier :** `notebook.ipynb` (code, sorties retirées), `notebook_export.pdf` (rendu complet avec graphiques), `support_presentation.pdf`

## Contexte / besoin métier

Comprendre les moteurs réels des ventes d'une librairie en ligne en croisant clients, produits et transactions, en distinguant les corrélations statistiquement significatives des corrélations réellement exploitables pour une décision marketing.

## Données

Trois tables sources jointes en une vue consolidée (`df_final`) :
- Transactions (historique d'achats)
- Products (informations produit)
- Customers (profil client)

Variables dérivées créées : chiffre d'affaires, âge du client, mois de la transaction. Nettoyage : typage des dates, gestion des valeurs manquantes et des doublons.

## Démarche

1. Courbe de Lorenz pour mesurer la concentration du chiffre d'affaires et exclure les quatre "super-clients" qui faussaient les analyses de tendance.
2. Tests de normalité (Shapiro, QQ-plots) pour choisir entre corrélation de Pearson et de Spearman selon la distribution des variables.
3. Tests adaptés au type de variables croisées : Khi² pour deux variables qualitatives, Kruskal-Wallis pour une variable quantitative contre une qualitative.
4. Systématiquement, calcul d'une mesure de taille d'effet (V de Cramér) en complément du test de significativité, pour éviter de surinterpréter un résultat statistiquement significatif mais négligeable en pratique.

## Résultats + impact / recommandations

- Genre × catégorie de livre achetée : test du Khi² hautement significatif (p ≈ 2,5×10⁻³⁴) mais V de Cramér = 0,015, soit un effet quasi nul. **Recommandation : ne pas orienter la segmentation marketing sur le genre pour ce critère.**
- Âge × chiffre d'affaires : corrélation de Spearman globale négative (r ≈ -0,185), mais le signal diffère fortement par segment d'âge : chez les 21-53 ans, corrélation positive significative (r ≈ 0,071, p < 0,001) ; chez les 54-95 ans, corrélation non significative. **Recommandation : cibler les moins de 50 ans avec des offres premium/upsell, et les plus de 50 ans avec des actions de fidélisation.**
- Âge × catégorie de livre dominante : différences d'âge très significatives selon la catégorie (test de Kruskal-Wallis), avec des profils marqués (manga chez les 18-30 ans, littérature classique et essais chez les 45 ans et plus).

## Limites + prochaines pistes

- Analyse purement corrélationnelle : aucune expérimentation contrôlée (A/B test) n'a été menée pour confirmer un lien de causalité.
- Piste : tester en conditions réelles les recommandations de segmentation par âge via une campagne A/B avant généralisation.

---

*Note : les sorties (graphiques, tableaux) du notebook ont été retirées pour réduire la taille du fichier sur ce repo. Le rendu complet avec visualisations est disponible dans `notebook_export.pdf`, dans ce même dossier.*

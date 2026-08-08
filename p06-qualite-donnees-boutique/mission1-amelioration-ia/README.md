# Amélioration critique du P6, augmentée par l'IA

Reprise du notebook Bottleneck un an après sa livraison, pour traiter les deux limites
que sa version d'origine identifiait elle-même en conclusion.

## Ce qui a changé, et pourquoi

Le notebook initial ne repérait les valeurs aberrantes que sur le prix, en univarié.
Un article dont le prix est parfaitement normal mais dont la combinaison stock / ventes
est atypique lui échappait. Il lisait par ailleurs ses corrélations sur une carte de
chaleur, sans test permettant de distinguer un vrai lien d'un artefact de l'échantillon.

Trois méthodes de détection multivariée ont été instruites, deux codées et exécutées sur
les données réelles, une écartée avant implémentation. Deux tests de corrélation ont été
ajoutés. Le notebook d'origine n'a jamais été modifié : tout se passe sur une copie, ce
qui permet une comparaison avant / après à tout moment.

## Résultats mesurés

| Indicateur | Valeur |
|---|---|
| Anomalies stock/ventes invisibles à l'analyse du prix seul | **41 articles** |
| Recoupement Isolation Forest / IQR (indice de Jaccard) | 23,64 % |
| Recoupement Local Outlier Factor / IQR | 7,94 % |
| Recoupement entre les deux méthodes multivariées | 25,49 % |
| Temps de calcul mesuré — Isolation Forest | 46,9 ms |
| Temps de calcul mesuré — Local Outlier Factor | 1,7 ms |
| Paires de variables testées (Pearson et Spearman) | 15 |
| Exécution complète du notebook | 94 cellules, 0 erreur, ≈ 5 s |

Le résultat le plus notable ne concerne pas les anomalies : entre le stock et le prix
d'achat, Pearson conclut à l'absence de lien (r = −0,024, p = 0,52) là où Spearman trouve
une relation forte et hautement significative (r = −0,551, p < 0,0001). Un coefficient
affiché seul, comme dans la version d'origine, pouvait donc masquer une vraie relation
métier.

Second résultat gardé plutôt qu'écarté : le chronomètre contredit la théorie. Sur
825 lignes, Local Outlier Factor est 27 fois plus rapide qu'Isolation Forest, à rebours
de l'avantage de complexité qu'on prête habituellement à cette dernière. La décision ne
repose donc pas sur la vitesse, mais sur le recoupement avec l'analyse existante et sur
le nombre de réglages à défendre.

## Contenu du dossier

| Fichier | Contenu |
|---|---|
| `Belkacemi_Kawtar_1_notebook_V2_AMELIORE.ipynb` | Le notebook, exécuté intégralement |
| `veille_technologique.docx` | Besoin de veille, trois solutions comparées sur sept critères, sources datées, dispositif de veille continue |
| `cahier_des_charges.docx` | Contexte, parties prenantes, périmètre, contraintes, ressources, critères de réussite, besoins en formation |
| `PROJET_ORGANISATION.docx` | Lots, backlog, planning daté, registre des risques |
| `README.docx` | Traçabilité des choix et des essais, résultats, limites, reproductibilité |

## Reproduire

Les trois fichiers sources (`erp.xlsx`, `web.xlsx`, `liaison.xlsx`) doivent se trouver
à côté du notebook. Tous les chemins sont relatifs, la graine aléatoire est figée à 42,
et les versions exactes des bibliothèques sont consignées dans `README.docx`.

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install jupyter nbconvert pandas numpy scikit-learn scipy openpyxl matplotlib seaborn plotly xlsxwriter
jupyter nbconvert --to notebook --execute --inplace Belkacemi_Kawtar_1_notebook_V2_AMELIORE.ipynb
```

## Limites assumées

Le taux d'anomalies annoncé à l'algorithme est hérité de la méthode univariée : c'est une
hypothèse simplificatrice, explicitée plutôt que masquée. Sans vérité terrain, le
recoupement entre méthodes ne dit pas laquelle a raison — ce sont des pistes
d'investigation, pas des faits établis. Le résultat de vitesse n'est pas généralisable à
un catalogue plus grand. Enfin 13,45 % du catalogue n'a pas d'équivalent côté site :
toutes les analyses portent sur un sous-ensemble.

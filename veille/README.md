# Système de veille métier et technologique

Kawtar Belkacemi — Data Analyst

Veille continue, sourcée et **partiellement automatisée** sur les méthodes d'analyse
de données, la qualité de données et les outils du métier.

---

## 1. Pourquoi ces sources

Le périmètre de veille découle directement des besoins rencontrés en projet :
détecter des anomalies, fiabiliser des jeux de données, valider statistiquement
un résultat, restituer à des non-techniciens. Chaque source est retenue pour une
raison précise, pas parce qu'elle est populaire.

| Famille | Source | Pourquoi elle est suivie | Fréquence utile |
|---|---|---|---|
| Outils | scikit-learn — releases GitHub | Les méthodes que j'utilise (Isolation Forest, LOF) y évoluent ; les notes de version signalent les changements de comportement | à chaque version |
| Outils | pandas — releases GitHub | Socle de tous mes notebooks ; ruptures d'API à anticiper | à chaque version |
| Outils | scikit-learn — PyPI | Confirme la disponibilité effective des versions | à chaque version |
| Recherche | arXiv `stat.ML` | Nouvelles méthodes de détection d'anomalies et de traitement des données manquantes, avant leur arrivée dans les bibliothèques | quotidien, lecture hebdo |
| Métier | Real Python | Pratique appliquée, qualité pédagogique constante | hebdomadaire |
| Métier | KDnuggets | Panorama métier, retours d'expérience | hebdomadaire |
| Alertes | 4 alertes par mots-clés (Google News RSS) | Déclenchement par sujet et non par source : `anomaly detection`, `data quality`, `détection d'anomalies`, `Power BI` | continu |
| Lecteur seul | Power BI blog (Microsoft) | Source pertinente mais qui refuse les requêtes automatisées (HTTP 403) : suivie dans un lecteur RSS, pas par le script | hebdomadaire |

**Critère de sélection retenu :** une source est gardée si elle apporte soit un
signal de rupture (version, méthode nouvelle), soit un retour d'expérience
transposable. Les sources purement promotionnelles sont écartées.

---

## 2. Ce qui est automatisé

Trois briques :

1. **`sources.opml`** — la liste des flux, au format OPML standard.
   Importable tel quel dans n'importe quel lecteur RSS (Feedly, NetNewsWire, Thunderbird).
2. **`veille.py`** — interroge tous les flux, filtre les entrées sur un dictionnaire
   de mots-clés pondérés, et produit un digest Markdown daté et trié par pertinence.
3. **Planification hebdomadaire** — une tâche `cron` lance le script tous les lundis
   à 8 h et dépose le digest de la semaine dans ce dossier.

Le filtrage n'est pas un simple « contient le mot » : chaque mot-clé porte un poids
(`isolation forest` = 4, `pandas` = 2, `pipeline` = 1) et le score d'une entrée est
la somme des poids trouvés dans son titre et son résumé. Le digest est trié par ce
score, ce qui fait remonter en premier ce qui touche mon cœur de périmètre.

---

## 3. Utilisation

```bash
python3 veille.py                # 30 derniers jours
python3 veille.py --days 7       # digest hebdomadaire
python3 veille.py --days 60      # rattrapage
```

Aucune dépendance externe : uniquement la bibliothèque standard Python.

Planification déjà installée (`crontab -l` pour vérifier) :

```
0 8 * * 1  cd <dossier>/veille && /usr/bin/python3 veille.py --days 7
```

Pour la retirer : `crontab -e` puis supprimer la ligne.

---

## 4. Fichiers

| Fichier | Rôle |
|---|---|
| `sources.opml` | Liste des flux, importable dans un lecteur RSS |
| `veille.py` | Collecte, filtrage pondéré, génération du digest |
| `digest_AAAA-MM-JJ.md` | Digests produits, datés — la trace de la veille dans le temps |

---

## 5. Limites assumées

- **Les alertes par mots-clés renvoient des résultats classés par pertinence**, pas
  par date : le digest peut donc afficher peu d'entrées « récentes » sur ces sources.
  C'est le comportement de Google News, pas un défaut du script.
- **Une source est inaccessible aux robots** (Power BI blog, HTTP 403). Elle reste
  déclarée dans l'OPML et suivie manuellement en lecteur RSS ; le digest le signale
  explicitement plutôt que de la masquer.
- **Le filtrage par mots-clés reste littéral** : une méthode nouvelle décrite avec
  un vocabulaire inattendu passera au travers. C'est pourquoi la lecture directe
  du flux arXiv reste hebdomadaire, en complément du digest.

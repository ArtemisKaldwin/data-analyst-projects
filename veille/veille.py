#!/usr/bin/env python3
"""
Veille technologique automatisée — Data Analyst
Kawtar Belkacemi

Lit les flux RSS/Atom déclarés dans sources.opml, filtre les entrées récentes
sur un dictionnaire de mots-clés métier, et produit un digest Markdown daté.

Usage :
    python veille.py                 # digest des 30 derniers jours
    python veille.py --days 7        # digest hebdomadaire

Automatisation (cron, tous les lundis à 8 h) :
    0 8 * * 1  cd /chemin/veille && python veille.py --days 7
"""
import argparse, datetime as dt, re, sys, urllib.request, xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime

# Mots-clés qui définissent le périmètre de veille (pondérés)
KEYWORDS = {
    "anomaly": 3, "anomalies": 3, "outlier": 3, "isolation forest": 4,
    "local outlier": 4, "novelty detection": 3,
    "data quality": 3, "qualité": 2, "missing data": 2, "imputation": 2,
    "correlation": 2, "spearman": 3, "pearson": 3, "p-value": 3,
    "statistical test": 3, "significance": 2,
    "pandas": 2, "scikit-learn": 3, "sklearn": 3, "polars": 2, "duckdb": 2,
    "dashboard": 1, "power bi": 2, "reproducib": 3, "pipeline": 1,
}

UA = {"User-Agent": "Mozilla/5.0 (veille-data-analyst)"}


SKIP_GROUPS = {"LecteurSeul"}   # sources qui bloquent les robots : lecteur RSS uniquement


def read_opml(path="sources.opml"):
    """Retourne (feeds interrogeables, sources reservees au lecteur RSS)."""
    root = ET.parse(path).getroot()
    feeds, reader_only = [], []
    for group in root.find("body"):
        target = reader_only if group.get("title") in SKIP_GROUPS else feeds
        if group.get("xmlUrl"):
            target.append((group.get("text", "?"), group.get("xmlUrl")))
        for child in group:
            if child.get("xmlUrl"):
                target.append((child.get("text", "?"), child.get("xmlUrl")))
    return feeds, reader_only


def fetch(url, timeout=20):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def parse_date(txt):
    if not txt:
        return None
    txt = txt.strip()
    try:
        return parsedate_to_datetime(txt).replace(tzinfo=None)
    except Exception:
        pass
    for fmt in ("%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%d"):
        try:
            return dt.datetime.strptime(txt, fmt).replace(tzinfo=None)
        except Exception:
            continue
    return None


def entries(xml_bytes):
    """Supporte RSS 2.0 et Atom."""
    out = []
    try:
        root = ET.fromstring(xml_bytes)
    except ET.ParseError:
        return out
    ns = {"a": "http://www.w3.org/2005/Atom"}
    for it in root.iter():
        tag = it.tag.split("}")[-1]
        if tag not in ("item", "entry"):
            continue
        def txt(*names):
            for n in names:
                el = it.find(n) if "}" not in n else it.find(n)
                if el is None:
                    el = it.find(f"{{http://www.w3.org/2005/Atom}}{n}")
                if el is not None and (el.text or el.get("href")):
                    return (el.text or el.get("href") or "").strip()
            return ""
        link = txt("link")
        if not link:
            le = it.find("{http://www.w3.org/2005/Atom}link")
            link = le.get("href") if le is not None else ""
        out.append({
            "title": re.sub(r"\s+", " ", txt("title")),
            "link": link,
            "date": parse_date(txt("pubDate", "updated", "published")),
            "summary": re.sub(r"<[^>]+>", " ", txt("description", "summary"))[:400],
        })
    return out


def score(e):
    blob = (e["title"] + " " + e["summary"]).lower()
    return sum(w for k, w in KEYWORDS.items() if k in blob)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=30)
    ap.add_argument("--opml", default="sources.opml")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()

    since = dt.datetime.now() - dt.timedelta(days=a.days)
    feeds, reader_only = read_opml(a.opml)
    kept, stats = [], []

    for name, url in feeds:
        try:
            es = entries(fetch(url))
            n_recent = 0
            for e in es:
                if e["date"] and e["date"] < since:
                    continue
                n_recent += 1
                sc = score(e)
                if sc > 0:
                    e["source"], e["score"] = name, sc
                    kept.append(e)
            stats.append((name, len(es), n_recent, "ok"))
        except Exception as ex:
            stats.append((name, 0, 0, f"ERREUR : {type(ex).__name__}"))

    kept.sort(key=lambda e: (-e["score"], e["title"]))
    today = dt.date.today().isoformat()
    L = []
    L.append(f"# Digest de veille — {today}")
    L.append("")
    L.append(f"Fenêtre : {a.days} derniers jours · {len(feeds)} sources interrogées · "
             f"{len(kept)} entrées retenues sur critères de pertinence.")
    L.append("")
    L.append("## Sources interrogées")
    L.append("")
    L.append("| Source | Entrées | Récentes | État |")
    L.append("|---|---:|---:|---|")
    for n, tot, rec, st in stats:
        L.append(f"| {n} | {tot} | {rec} | {st} |")
    L.append("")
    if reader_only:
        L.append("_Sources suivies en lecteur RSS uniquement (elles refusent les requêtes automatisées) : "
                 + ", ".join(n for n, _ in reader_only) + "._")
        L.append("")
    L.append("## Entrées retenues (triées par pertinence)")
    L.append("")
    if not kept:
        L.append("_Aucune entrée ne correspond aux mots-clés sur la période._")
    for e in kept[:25]:
        d = e["date"].date().isoformat() if e["date"] else "n.d."
        L.append(f"- **{e['title']}**  \n  `{e['source']}` · {d} · pertinence {e['score']} · <{e['link']}>")
    L.append("")
    L.append("## Périmètre de veille (mots-clés pondérés)")
    L.append("")
    L.append(", ".join(f"`{k}`({w})" for k, w in sorted(KEYWORDS.items(), key=lambda x: -x[1])))

    md = "\n".join(L)
    out = a.out or f"digest_{today}.md"
    open(out, "w", encoding="utf-8").write(md)
    print(md[:1500])
    print(f"\n[écrit] {out}")


if __name__ == "__main__":
    main()

# Technisches Glossar

Sammlung der technischen Begriffe, die in der Dokumentation von
`incolume.py.changelog` verwendet werden.

Diese Datei dient als **Glossar** (Top-100-Begriffe des Projekts), geordnet nach
Kategorien, mit der Definition und dem Ort, an dem der Begriff in der
Dokumentation erscheint.

> Letzte Aktualisierung: 2026-11-16
> Produktversion: 1.6.0a11 (dev)

---

## Architektur und Erstellung

| Begriff | Definition |
|---|---|
| **mkdocs** | Statisches Werkzeug zur Erzeugung einer HTML-Dokumentation aus Markdown-Dateien. |
| **mkdocstrings** | MkDocs-Plugin, das automatisch eine API-Dokumentation aus den Docstrings des Python-Codes erzeugt. |
| **material** | Material-Thema für MkDocs (moderne Website, Hell-/Dunkel-Modus, Farbpalette). |
| **i18n** | Internationalisierung — mehrere Sprachen (pt-BR, en, de, es, fr, it). |
| **nav_translations** | Zuordnung der Navigationstitel für jede Sprache in `mkdocs.yml`. |
| **gh-deploy** | MkDocs-Befehl, der die Dokumentation im Branch `webdoc` oder auf GitHub Pages veröffentlicht. |
| **webdoc** | Integrations-Branch, der zum Veröffentlichen der mit `gh-deploy` erzeugten Website dient. |
| **CHANGELOG.md** | Datei mit dem Änderungsprotokoll nach dem Keep-a-Changelog-Standard. |
| **ADR** | Architecture Decision Record — Dokument, das Architekturentscheidungen festhält. |
| **PRD** | Product Requirements Document — Dokument mit den Produktanforderungen. |
| **SPEC** | Specification — Dokument zur Umsetzung/technischen Spezifikation. |
| **PLAN-001** | Plan zur Verbesserung der Dokumentation — Dokument zur Sprint-Planung. |
| **CI/CD** | *Continuous Integration / Continuous Deployment* — kontinuierliche Integration und Auslieferung. |
| **GitHub Pages** | Von GitHub gehosteter Dienst zum Veröffentlichen statischer Websites. |
| **uv** | Abhängigkeitsmanager und Projekt-Builder für Python (Alternative zu `pip`). |
| **taskipy** | Task-Runner (`task`), inspiriert von `npm scripts`; dient zum Anpassen der CLI. |

---

## Methoden und Prozesse

| Begriff | Definition |
|---|---|
| **Keep a Changelog** | Offene Spezifikation für das Format von `CHANGELOG.md`-Dateien. |
| **Semantic Versioning (SemVer)** | Regeln für die Versionierung `MAJOR.MINOR.PATCH` mit `rc`, `alpha` usw. |
| **Conventional Commits** | Spezifikation für Commit-Nachrichten mit Präfixen (`feat:`, `fix:`, `chore:`). |
| **TDD** | *Test-Driven Development* — testgetriebene Entwicklung (rot → grün → refaktorisieren). |
| **AC** | *Acceptance Criteria* — Akzeptanzkriterium einer Issue/Task. |
| **P0 / P1 / P2** | Prioritätsstufen: kritisch, hoch, mittel. |
| **Sprint** | Lieferzyklus (in der Regel 1–2 Wochen) mit zuvor geplanten Issues. |
| **Worktree** | Isoliertes Arbeitsverzeichnis, das von einem Branch abgeleitet ist. |
| **Rebase** | Integrationstechnik, die Commits auf einen anderen Branch neu anwendet. |
| **Fast-forward / Merge --no-ff** | Strategien zum Merge von Branches; hier wird `--no-ff` verwendet, um den Aufgabenverlauf zu erhalten. |

---

## Qualität und Validierung

| Begriff | Definition |
|---|---|
| **ruff** | Moderner Linter und Formatter für Python (Ersatz für `flake8`, `black`, `isort`). |
| **mypy** | Statischer Type-Checker für Python. |
| **pytest** | Framework für Unit-Tests in Python. |
| **coverage 99,7%** | Minimal erforderliche Code-Abdeckung durch Tests (Qualitätsregel). |
| **Strict mode** | Validierungsmodus „Strict“ von MkDocs (bricht bei Warnungen ab). |
| **broken link** | Interner Link, der auf eine nicht existierende Datei verweist. |
| **UTF-8 strict** | Validierung der UTF-8-Kodierung ohne Ersetzung ungültiger Zeichen. |
| **mojibake** | Durch einen Kodierungsfehler beschädigter Text (z. B. `Ã£` statt `ã`). |
| **HTML entity** | Darstellung von Sonderzeichen über ihre numerische Kodierung (z. B. `&amp;`). |
| **Badge** | Visuelles Symbol in Markdown mit Status (grüne CI, Version usw.) über externe Dienste. |

---

## Auslieferung und Veröffentlichung

| Begriff | Definition |
|---|---|
| **publish** | Prozess, die erzeugte Dokumentation auf den Hosting-Server zu laden. |
| **site_name** | Titel, der im Kopfbereich der erzeugten Website angezeigt wird. |
| **edit_uri** | URI, die die direkte Bearbeitung von Seiten über GitHub ermöglicht. |
| **edit_uri: tree/branch/docs** | Muster, das zum Erzeugen von Bearbeitungslinks auf GitHub verwendet wird. |
| **theme** | Erscheinungsbild und Layout der Website (hier: `material`). |
| **light/dark mode** | Unterstützung für helle und dunkle Darstellung über die Material-Paleta. |
| **sidebar** | Seitenleiste mit schrittweiser Navigation durch die Themen. |
| **permalink** | Permanente URL eines Abschnitts (erzeugt automatische Anker). |
| **autolink** | Erzeugt automatische Anker aus Überschriften. |
| **emoji** | Erweiterung, die die Verwendung von Emojis in Markdown ermöglicht. |
| **pagetocat** | Erzeugt eine Inhaltsübersicht (TOC) am Anfang der Seite. |
| **toc permalink** | Ermöglicht das Klicken auf das Link-Symbol, um zu einer Überschrift zu gelangen. |

---

## Umgebungsvariablen und Konfigurationsdateien

| Begriff | Definition |
|---|---|
| **pyproject.toml** | Konfigurationsdatei des Python-Pakets (PEP 621): Abhängigkeiten, Version, Skripte. |
| **uv.lock** | Lockfile von `uv` mit den exakten Versionen aller Abhängigkeiten. |
| **tox.ini / pyproject.toml [tool.tox]** | Konfiguration mehrerer Python-Versionen und Testumgebungen. |
| **.changelog.toml** | Optionale Konfigurationsdatei des CHANGELOG-Generators. |
| **version.txt** | Datei, die die aktuelle Paketversion zur Laufzeit vorhält. |
| **.gitattributes** | Definiert, wie Git die Dateien im Repository behandelt. |
| **CI/CD workflow** | Skript für GitHub Actions (`.github/workflows/*.yml`). |
| **pre-commit** | Git-Hook, der vor jedem Commit ausgeführt wird (Code-Qualität). |
| **environment** | Isolierte Python-Umgebung (`.venv/`), verwaltet über `uv`. |
| **coverage_report** | Verzeichnis mit dem HTML-Bericht zur Testabdeckung. |
| **docs/** | Wurzelverzeichnis der Markdown-Dokumentation. |
| **incolume/**, **src/** | Python-Quellcode des Pakets. |

---

## Nützliche Befehle

| Begriff | Definition |
|---|---|
| `uv sync` | Synchronisiert die Umgebung mit `uv.lock` und installiert Abhängigkeiten. |
| `uv run` | Führt einen Befehl in der aktivierten Umgebung aus. |
| `uv run task setup` | Richtet die Git-Hooks ein (`core.hooksPath`). |
| `uv run task -l` | Listet alle verfügbaren Tasks auf (`taskipy`). |
| `uv run ruff check` | Führt den Linter aus. |
| `uv run ruff format` | Formatiert den Code. |
| `uv run mypy` | Prüft statische Typen. |
| `uv run pytest` | Führt die Testsuite aus. |
| `uv run mkdocs build` | Erzeugt die Dokumentation in `_site/` (oder `site/`). |
| `uv run mkdocs serve` | Stellt die Dokumentation auf localhost bereit. |
| `uv run mkdocs gh-deploy --remote-branch webdoc` | Veröffentlicht die Dokumentation auf GitHub Pages (`webdoc`). |
| `uv run tox` | Führt die Multi-Version-Testmatrix aus. |
| `uv run task changelog` | Erzeugt oder aktualisiert `CHANGELOG.md`. |
| `git tag -n` | Listet Tags mit Anmerkungen; Quelle der Versionen im CHANGELOG. |
| `uv version` | Erhöht die Paketversion (siehe [semver.org](https://semver.org)). |
| `git worktree` | Verwaltet mehrere Arbeitsverzeichnisse des Repositorys. |

---

## Glossar nach Häufigkeit (Top)

Nach relativer Häufigkeit in der Dokumentation sortiert.

| Begriff | Vorkommen | Typischer Kontext |
|---|---|---|
| **Markdown** | 226 | Dokumentationsformat, Endung `.md`. |
| **CHANGELOG** | 137 | Änderungsprotokoll, Datei `CHANGELOG.md`. |
| **Python** | 102 | Hauptsprache. |
| **API** | 96 | Programmierschnittstelle für Anwendungen. |
| **URL** | 99 | Ressourcen-Locator im Web. |
| **GitHub** | 44 | Code-Hosting-Plattform. |
| **CI/CD** | 45 | Kontinuierliche Integration/Auslieferung. |
| **Issue** | — | Aufgabe oder Fehler, der im Projekt-Tracker erfasst ist. |
| **AC** | — | *Acceptance Criteria* — Akzeptanzkriterium. |
| **README** | — | Einstiegsdokumentation des Repositorys. |
| **Versioning** | — | Versionsverwaltung (`MAJOR.MINOR.PATCH`). |
| **Conventional Commit** | — | Spezifikation für Commit-Nachrichten. |
| **Keep a Changelog** | — | Standard für die Formatierung von `CHANGELOG.md`. |
| **Semantic Versioning** | — | Regeln `MAJOR.MINOR.PATCH`. |
| **SemVer** | — | Abkürzung für Semantic Versioning. |
| **MkDocs** | — | Werkzeug zur Erzeugung statischer Websites. |
| **material** | — | Material-Thema für MkDocs. |
| **i18n** | — | Internationalisierung. |
| **nav_translations** | — | Zuordnung der Navigationstitel pro Sprache. |
| **gh-deploy** | — | Veröffentlichungsbefehl von MkDocs. |
| **webdoc** | — | Integrations-Branch für GitHub Pages. |
| **uv** | — | Abhängigkeitsmanager und Builder. |
| **taskipy** | — | Task-Runner. |
| **ruff** | — | Linter und Formatter für Python. |
| **mypy** | — | Statischer Typprüfer. |
| **pytest** | — | Test-Framework. |
| **coverage** | — | Code-Abdeckung durch Tests. |
| **UnicodeDecodeError** | — | Kodierungsfehler beim Lesen einer Datei. |
| **mojibake** | — | Durch einen Kodierungsfehler beschädigter Text. |
| **toctoc** | — | Automatische Inhaltsübersicht. |
| **ACR** | — | *Acceptance Criteria Rule* — Akzeptanzregel. |

---

## Referenzen

- [Keep a Changelog](https://keepachangelog.com/en/1.0.0)
- [Semantic Versioning](https://semver.org/spec/v2.0.0.html)
- [Conventional Commits](https://www.conventionalcommits.org/pt-br/v1.0.0)
- [MkDocs](https://www.mkdocs.org)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [MkDocs i18n Plugin](https://mkdocs-material.squidfunk.com/configuration/i18n/)
- [GitHub Pages](https://pages.github.com)

---

*Quelle: Überprüfung der Dokumentation von `incolume.py.changelog` (v1.6.0a11, dev).*

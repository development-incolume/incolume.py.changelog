# Glossaire technique

Référentiel des termes techniques utilisés dans la documentation du projet
`incolume.py.changelog`.

Ce fichier sert de **glossaire** (top 100 des termes du projet), organisé par
catégorie, avec leur définition et l'endroit où le terme apparaît dans la
documentation.

> Dernière mise à jour : 2026-11-16

---

## Architecture et génération

| Terme | Définition |
|---|---|
| **mkdocs** | Générateur statique de documentation HTML à partir de fichiers Markdown. |
| **mkdocstrings** | Plugin de MkDocs qui génère automatiquement la documentation de l'API à partir des docstrings du code Python. |
| **material** | Thème Material pour MkDocs (site moderne, mode sombre/clair, palette de couleurs). |
| **i18n** | Internationalisation — plusieurs langues (pt-BR, en, de, es, fr, it). |
| **nav_translations** | Mappage des titres de navigation pour chaque langue dans `mkdocs.yml`. |
| **gh-deploy** | Commande de MkDocs qui publie la documentation sur la branche `webdoc` ou sur GitHub Pages. |
| **webdoc** | Branche d'intégration utilisée pour la publication du site généré via `gh-deploy`. |
| **CHANGELOG.md** | Fichier de suivi des modifications suivant la norme Keep a Changelog. |
| **ADR** | Architecture Decision Record — document qui consigne les décisions d'architecture. |
| **PRD** | Product Requirements Document — document des exigences du produit. |
| **SPEC** | Spécification — document d'exécution/spécification technique. |
| **PLAN-001** | Plan d'amélioration de la documentation — document de planification de la sprint. |
| **CI/CD** | *Continuous Integration / Continuous Deployment* — intégration et livraison continues. |
| **GitHub Pages** | Service hébergé par GitHub pour publier des sites statiques. |
| **uv** | Gestionnaire de dépendances et constructeur de projets Python (alternative à `pip`). |
| **taskipy** | Exécuteur de tâches (`task`) inspiré des `npm scripts` ; utilisé pour personnaliser la CLI. |
---

## Méthodologies et processus

| Terme | Définition |
|---|---|
| **Keep a Changelog** | Spécification ouverte pour le format des fichiers `CHANGELOG.md`. |
| **Semantic Versioning (SemVer)** | Règles de versionnement `MAJOR.MINOR.PATCH` avec `rc`, `alpha`, etc. |
| **Conventional Commits** | Spécification des messages de commit avec préfixes (`feat:`, `fix:`, `chore:`). |
| **TDD** | *Test-Driven Development* — développement piloté par les tests (rouge → vert → refactoriser). |
| **AC** | *Acceptance Criteria* — critère d'acceptation d'une issue/tâche. |
| **P0 / P1 / P2** | Niveaux de priorité : critique, haute, moyenne. |
| **Sprint** | Cycle de livraison (généralement 1 à 2 semaines) avec des issues planifiées au préalable. |
| **Worktree** | Répertoire de travail isolé dérivé d'une branche. |
| **Rebase** | Technique d'intégration qui réapplique des commits au-dessus d'une autre branche. |
| **Fast-forward / Merge --no-ff** | Stratégies de fusion de branches ; ici, on utilise `--no-ff` pour conserver l'historique des tâches. |

---

## Qualité et validation

| Terme | Définition |
|---|---|
| **ruff** | Linter et formateur moderne pour Python (remplace `flake8`, `black`, `isort`). |
| **mypy** | Vérificateur statique de types (type checker) pour Python. |
| **pytest** | Framework de tests unitaires pour Python. |
| **coverage 99,7 %** | Couverture de code minimale exigée dans les tests (règle de qualité). |
| **Strict mode** | Mode de validation maximale de MkDocs (échoue sur les avertissements). |
| **broken link** | Lien interne qui pointe vers un fichier inexistant. |
| **UTF-8 strict** | Validation de l'encodage UTF-8 sans substitution des caractères invalides. |
| **mojibake** | Texte corrompu par une erreur d'encodage (ex. : `Ã£` au lieu de `ã`). |
| **HTML entity** | Représentation des caractères spéciaux au moyen de leur code numérique (ex. : `&amp;`). |
| **Badge** | Icône visuelle en Markdown affichant un statut (CI verte, version, etc.) via des services externes. |
---

## Livraisons et publication

| Terme | Définition |
|---|---|
| **publish** | Processus de mise en ligne de la documentation générée sur le serveur d'hébergement. |
| **site_name** | Titre affiché dans l'en-tête du site généré. |
| **edit_uri** | URI utilisée pour l'édition directe des pages via GitHub. |
| **edit_uri: tree/branch/docs** | Format utilisé pour générer les liens d'édition sur GitHub. |
| **theme** | Apparence et mise en page du site (ici : `material`). |
| **light/dark mode** | Prise en charge des modes clair et sombre via la palette Material. |
| **sidebar** | Barre latérale avec navigation progressive dans les sujets. |
| **permalink** | URL permanente d'une section (génère des ancres automatiques). |
| **autolink** | Crée des ancres automatiques à partir des en-têtes. |
| **emoji** | Extension qui permet d'utiliser des emojis dans Markdown. |
| **pagetocat** | Génère une table des matières (TOC) en haut de la page. |
| **toc permalink** | Permet de cliquer sur l'icône du paragraphe pour atteindre un en-tête. |

---

## Variables d'environnement et fichiers de configuration

| Terme | Définition |
|---|---|
| **pyproject.toml** | Fichier de configuration du paquet Python (PEP 621) : dépendances, version, scripts. |
| **uv.lock** | Fichier de verrouillage de `uv` avec les versions exactes de toutes les dépendances. |
| **tox.ini / pyproject.toml [tool.tox]** | Configuration de plusieurs versions de Python et des environnements de test. |
| **.changelog.toml** | Fichier de configuration optionnel du générateur de CHANGELOG. |
| **version.txt** | Fichier qui stocke la version actuelle du paquet en runtime. |
| **.gitattributes** | Définit la manière dont Git traite les fichiers du dépôt. |
| **CI/CD workflow** | Script GitHub Actions (`.github/workflows/*.yml`). |
| **pre-commit** | Hook Git exécuté avant chaque commit (qualité du code). |
| **environment** | Environnement Python isolé (`.venv/`), géré via `uv`. |
| **coverage_report** | Répertoire contenant le rapport HTML de couverture des tests. |
| **docs/** | Répertoire racine de la documentation en Markdown. |
| **incolume/**, **src/** | Code source Python du paquet. |
---

## Commandes utiles

| Terme | Définition |
|---|---|
| `uv sync` | Synchronise l'environnement virtuel avec `uv.lock` et installe les dépendances. |
| `uv run` | Exécute une commande dans l'environnement activé. |
| `uv run task setup` | Configure les hooks Git (`core.hooksPath`). |
| `uv run task -l` | Liste toutes les tâches disponibles (`taskipy`). |
| `uv run ruff check` | Exécute le linter. |
| `uv run ruff format` | Formate le code. |
| `uv run mypy` | Vérifie les types statiques. |
| `uv run pytest` | Exécute la suite de tests. |
| `uv run mkdocs build` | Génère la documentation dans `_site/` (ou `site/`). |
| `uv run mkdocs serve` | Sert la documentation en localhost. |
| `uv run mkdocs gh-deploy --remote-branch webdoc` | Publie la documentation sur GitHub Pages (`webdoc`). |
| `uv run tox` | Lance la matrice de tests multi-versions. |
| `uv run gcl` | Génère ou met à jour le `CHANGELOG.md`. |
| `git tag -n` | Liste les tags annotés ; source des versions dans le CHANGELOG. |
| `uv version` | Incrémente la version du paquet (voir [semver.org](https://semver.org)). |
| `git worktree` | Gère les répertoires de travail multiples du dépôt. |

---

## Glossaire par fréquence (Top)

Termes classés par fréquence relative dans la documentation.

| Terme | Occurrences | Contexte typique |
|---|---|---|
| **Markdown** | 226 | Format de documentation, extension `.md`. |
| **CHANGELOG** | 137 | Suivi des modifications, fichier `CHANGELOG.md`. |
| **Python** | 102 | Langage de programmation principal. |
| **API** | 96 | Interface de programmation d'applications. |
| **URL** | 99 | Localisateur de ressources sur le web. |
| **GitHub** | 44 | Plateforme d'hébergement de code. |
| **CI/CD** | 45 | Intégration/livraison continue. |
| **Issue** | — | Tâche ou bogue suivi dans le tracker du projet. |
| **AC** | — | *Acceptance Criteria* — critère d'acceptation. |
| **README** | — | Documentation initiale du dépôt. |
| **Versioning** | — | Gestion des versions (`MAJOR.MINOR.PATCH`). |
| **Conventional Commit** | — | Spécification des messages de commit. |
| **Keep a Changelog** | — | Norme de formatage du `CHANGELOG.md`. |
| **Semantic Versioning** | — | Règles `MAJOR.MINOR.PATCH`. |
| **SemVer** | — | Abréviation de Semantic Versioning. |
| **MkDocs** | — | Outil de génération de site statique. |
| **material** | — | Thème Material pour MkDocs. |
| **i18n** | — | Internationalisation. |
| **nav_translations** | — | Mappage des titres de navigation par langue. |
| **gh-deploy** | — | Commande de publication de MkDocs. |
| **webdoc** | — | Branche d'intégration pour GitHub Pages. |
| **uv** | — | Gestionnaire de dépendances et constructeur. |
| **taskipy** | — | Exécuteur de tâches. |
| **ruff** | — | Linter et formateur pour Python. |
| **mypy** | — | Vérificateur statique de types. |
| **pytest** | — | Framework de tests. |
| **coverage** | — | Couverture de code par les tests. |
| **UnicodeDecodeError** | — | Erreur d'encodage lors de la lecture d'un fichier. |
| **mojibake** | — | Texte corrompu par une erreur d'encodage. |
| **toctoc** | — | Table des matières automatique. |
| **ACR** | — | *Acceptance Criteria Rule* — règle d'acceptation. |

---

## Références

- [Keep a Changelog](https://keepachangelog.com/en/1.0.0)
- [Semantic Versioning](https://semver.org/spec/v2.0.0.html)
- [Conventional Commits](https://www.conventionalcommits.org/pt-br/v1.0.0)
- [MkDocs](https://www.mkdocs.org)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [MkDocs i18n Plugin](https://mkdocs-material.squidfunk.com/configuration/i18n/)
- [GitHub Pages](https://pages.github.com)

---

*Source : révision de la documentation de `incolume.py.changelog` (v1.6.0a11, dev).*

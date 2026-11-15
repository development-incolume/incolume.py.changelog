# Guide de Contribution (Développement)

Règles et conventions pour développer `incolume.py.changelog`.

## Code de conduite

Détails dans le [Code de conduite](code_of_conduct.md).

## Standards appliqués

Méthodologies et conventions du projet dans
[Conventions et Méthodologies](README.md).

## Prérequis

- Git
- Python `>=3.11,<4`
- `uv` (recommandé)

## Environnement de développement

```shell
git clone https://github.com/development-incolume/incolume.py.changelog.git
cd incolume.py.changelog
uv sync --python 3.12
uv run task setup
```

- `uv sync` crée l'environnement et installe les dépendances de
  `pyproject.toml` selon `uv.lock`.
- `uv run task setup` définit `git config core.hooksPath .git-hooks/`, activant
  les hooks du projet.

## Qualité du code

```shell
uv run ruff check tests incolume
uv run ruff format tests incolume
uv run mypy tests incolume
uv run pytest
```

- Couverture minimale : **99,7 %**.
- Ne pas modifier les tests pour faire passer l'implémentation.

## Tests multi-version

```shell
uv run tox
uv run tox -e 3.11
uv run tox -e typing
uv run tox -e lint
```

## Automatisation (taskipy)

```shell
uv run task -l
```

Tâches principales : `tests`, `lint`, `changelog`, `docs-serve`, `docs-build`,
`safety`, `setup`.

## Documentation

```shell
uv run task docs-serve   # serveur local
uv run task docs-build   # générer et publier sur la branche webdoc
```

## Sécurité

```shell
uv run bandit -c pyproject.toml -r incolume/
uv run pip-audit
uv run safety check
```

## Versionnement

```shell
uv version --bump <major|minor|patch|alpha|beta|rc|stable>
```

La version vit dans `pyproject.toml` (`[project]`) et doit être reportée dans
`[tool.poetry]` et dans `incolume/py/changelog/version.txt`. Le commit de version
est `build: incolume-py-changelog <version>`, sur `dev`, après le merge.

## Flux de livraison

- Branche dérivée de `dev`, avec une issue ouverte.
- Test du critère avant l'implémentation.
- `ruff`/`mypy`/`pytest` vert avant de committer.
- Merge `--no-ff` (revu par Kevin).

# Guide de contribution (développement)

Documentation rapide à l'intention des contributeurs du projet
`incolume.py.changelog`.

## Par où commencer

1. Lisez le fichier [AGENTS.md](../../AGENTS.md) — règles de travail, identité et
   flux de livraison.
2. Lisez le fichier [SPEC-001](../analysis_artifacts/SPEC-001-execucao.md) si
   vous avez besoin du détail de l'exécution.
3. Lisez le fichier [PLAN-001](../analysis_artifacts/PLAN-001-documentacao.md)
   sur l'amélioration de la documentation.

## Mais vous n'avez pas à tout lire d'un coup

Le document d'exécution ci-dessous est le point de départ pour les tâches du
cœur Backend/API :

- `src/…`, `config/` et `apps/core/` — la couche backend/API ;
- Issues AC-02, AC-11, AC-12, AC-15, AC-18 et AC-19.

Les adaptateurs et la désinfection ne relèvent plus de la responsabilité de
celui qui lit ce document (`Bob` se trouvant désormais dans
`adapters/office/` et `render/`).

## Prérequis

- Git
- Python `>=3.11,<4`
- `uv` (recommandé)
- L'identité actuelle du dépôt :

```shell
git config user.name "Britodfbr"
git config user.email "brito@incolume.com.br"
```

## Environnement de développement

```shell
git clone https://github.com/development-incolume/incolume.py.changelog.git
cd incolume.py.changelog
uv sync --python 3.12
uv run task setup
```

- `uv sync` crée l'environnement et installe les dépendances de `pyproject.toml`
  selon `uv.lock`.
- `uv run task setup` configure `git config core.hooksPath .git-hooks/`,
  activant les hooks du projet.

## Qualité du code

```shell
uv run ruff check tests incolume
uv run ruff format tests incolume
uv run mypy tests incolume
uv run pytest
```

- Couverture minimale : **99,7 %**.
- Ne modifiez jamais un test pour faire passer l'implémentation.

## Tests multi-versions

```shell
uv run tox
uv run tox -e 3.11
uv run tox -e typing
uv run tox -e lint
```

## Automatisation (`taskipy`)

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

La version **ne** se trouve **pas** uniquement dans `pyproject.toml` :
également dans `version.txt` et dans `[tool.poetry]`. Après chaque merge d'une
tâche terminée, exécutez toujours :

```shell
uv version --bump alpha
```

Le commit de version reste sur `dev` :

```shell
git commit -m "build: $(uv version)"
```

## Flux de livraison

1. Branche dérivée de `dev`, avec une issue ouverte.
2. Test du critère **avant** l'implémentation (rouge → vert → refactoriser).
3. `ruff`/`mypy`/`pytest` verts avant de committer.
4. Merge `--no-ff` sur `dev` avec la relecture de Kevin.

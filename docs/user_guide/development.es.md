# Guía de Contribución (Desarrollo)

Reglas y convenciones para desarrollar `incolume.py.changelog`.

## Código de conducta

Detalles en el [Código de Conducta](code_of_conduct).

## Estándares aplicados

Metodologías y convenciones del proyecto en
[Convenciones y Metodologías](README).

## Requisitos

- Git
- Python `>=3.11,<4`
- `uv` (recomendado)

## Entorno de desarrollo

```shell
git clone https://github.com/development-incolume/incolume.py.changelog.git
cd incolume.py.changelog
uv sync --python 3.12
uv run task setup
```

- `uv sync` crea el entorno e instala las dependencias de `pyproject.toml`
  según `uv.lock`.
- `uv run task setup` configura `git config core.hooksPath .git-hooks/`, activando
  los hooks del proyecto.

## Calidad del código

```shell
uv run ruff check tests incolume
uv run ruff format tests incolume
uv run mypy tests incolume
uv run pytest
```

- Cobertura mínima: **99,7 %**.
- No edites los tests para que la implementación pase.

## Tests multi-versión

```shell
uv run tox
uv run tox -e 3.11
uv run tox -e typing
uv run tox -e lint
```

## Automatización (taskipy)

```shell
uv run task -l
```

Tareas principales: `tests`, `lint`, `changelog`, `docs-serve`, `docs-build`,
`safety`, `setup`.

## Documentación

```shell
uv run task docs-serve   # servidor local
uv run task docs-build   # generar y publicar en el branch webdoc
```

## Seguridad

```shell
uv run bandit -c pyproject.toml -r incolume/
uv run pip-audit
uv run safety check
```

## Versionado

```shell
uv version --bump <major|minor|patch|alpha|beta|rc|stable>
```

La versión vive en `pyproject.toml` (`[project]`) y debe reflejarse en
`[tool.poetry]` y en `incolume/py/changelog/version.txt`. El commit de versión es
`build: incolume-py-changelog <versión>`, en `dev`, después del merge.

## Flujo de entrega

- Branch derivado de `dev`, con una issue abierta.
- Test del criterio antes de la implementación.
- `ruff`/`mypy`/`pytest` en verde antes de committer.
- Merge `--no-ff` (revisado por Kevin).

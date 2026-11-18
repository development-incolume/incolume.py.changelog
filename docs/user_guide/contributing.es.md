# Guía de Contribución (Desarrollo)

Documentación rápida para colaboradores de `incolume.py.changelog`.

## Por dónde empezar

1. Lee el [AGENTS.md](../../AGENTS.md) – reglas de trabajo, identidad y flujo de
   entrega.
2. Lee el [SPEC-001](../analysis_artifacts/SPEC-001-execucao.md) si necesitas
   el detalle de la ejecución.
3. Lee el [PLAN-001](../analysis_artifacts/PLAN-001-documentacao.md) sobre la
   mejora de la documentación.

## Pero no hace falta leerlo todo de una vez

El documento de ejecución siguiente es el punto de partida para las tareas del
núcleo de Backend/API:

- `src/…`, `config/` y `apps/core/` — la capa de backend/API;
- Issues AC-02, AC-11, AC-12, AC-15, AC-18 y AC-19.

Los adaptadores, la sanitización (y ahora `Bob` en `adapters/office/` y
`render/`) ya no son responsabilidad de la persona que lee este documento.

## Requisitos previos

- Git
- Python `>=3.11,<4`
- `uv` (recomendado)
- La identidad actual del repositorio:

```shell
git config user.name "Britodfbr"
git config user.email "brito@incolume.com.br"
```

## Entorno de desarrollo

```shell
git clone https://github.com/development-incolume/incolume.py.changelog.git
cd incolume.py.changelog
uv sync --python 3.12
uv run task setup
```

- `uv sync` creará el entorno e instalará las dependencias de `pyproject.toml`
  según `uv.lock`.
- `uv run task setup` configura `git config core.hooksPath .git-hooks/`,
  activando los hooks del proyecto.

## Calidad del código

```shell
uv run ruff check tests incolume
uv run ruff format tests incolume
uv run mypy tests incolume
uv run pytest
```

- Cobertura mínima: **99,7 %**.
- Nunca edites los tests para que la implementación pase.

## Tests multi-versión

```shell
uv run tox
uv run tox -e 3.11
uv run tox -e typing
uv run tox -e lint
```

## Automatización (`taskipy`)

```shell
uv run task -l
```

Tareas principales: `tests`, `lint`, `changelog`, `docs-serve`, `docs-build`,
`safety`, `setup`.

## Documentación

```shell
uv run task docs-serve   # servidor local
uv run task docs-build   # generar y publicar en la rama webdoc
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

La versión **no** está solo en `pyproject.toml`: también en `version.txt` y
`[tool.poetry]`. Después del merge de una tarea concluida, ejecuta siempre:

```shell
uv version --bump alpha
```

El commit de versión se hace en `dev`:

```shell
git commit -m "build: $(uv version)"
```

## Flujo de entrega

1. Rama derivada de `dev`, con una issue abierta.
2. Prueba del criterio **antes** de la implementación (rojo → verde → refactorizar).
3. `ruff`/`mypy`/`pytest` en verde antes de hacer commit.
4. Merge `--no-ff` en `dev` con la revisión de Kevin.

# Contribution Guide (Development)

Quick documentation for contributors to `incolume.py.changelog`.

## Where to start

1. Read [AGENTS.md](../agents.md) – work rules, identity and delivery
   flow.
2. Read [SPEC-001](https://github.com/development-incolume/incolume.py.changelog/blob/dev/docs/analysis_artifacts/SPEC-001-execucao.md) if you need
   the execution details.
3. Read [PLAN-001](https://github.com/development-incolume/incolume.py.changelog/blob/dev/docs/analysis_artifacts/PLAN-001-documentacao.md) about the
   documentation improvement.

## But you don't need to read it all at once

The execution document below is the starting point for the Backend/API
core tasks:

- `src/…`, `config/` and `apps/core/` — the backend/API layer;
- AC-02, AC-11, AC-12, AC-15, AC-18 and AC-19 issues.

Adapters and sanitization (and now `Bob` in `adapters/office/` and
`render/`) are no longer the responsibility of the person reading this document.

## Prerequisites

- Git
- Python `>=3.11,<4`
- `uv` (preferred)
- The current repository identity:

```shell
git config user.name "Britodfbr"
git config user.email "brito@incolume.com.br"
```

## Development environment

```shell
git clone https://github.com/development-incolume/incolume.py.changelog.git
cd incolume.py.changelog
uv sync --python 3.12
uv run task setup
```

- `uv sync` creates the environment and installs the dependencies from
  `pyproject.toml` as locked in `uv.lock`.
- `uv run task setup` sets `git config core.hooksPath .git-hooks/`,
  enabling the project hooks.

## Code quality

```shell
uv run ruff check tests incolume
uv run ruff format tests incolume
uv run mypy tests incolume
uv run pytest
```

- Minimum coverage: **99.7%**.
- Never edit a test to make the implementation pass.

## Multi-version tests

```shell
uv run tox
uv run tox -e 3.11
uv run tox -e typing
uv run tox -e lint
```

## Automation (`taskipy`)

```shell
uv run task -l
```

Main tasks: `qa`, `ty`, `test-all`, `bandit`, `safety`, `setup`.

## Documentation

```shell
uv run mkdocs serve   # local server
uv run mkdocs gh-deploy --config-file mkdocs.yml --remote-branch webdoc   # build and publish to the webdoc branch
```

## Security

```shell
uv run bandit -c pyproject.toml -r incolume/
uv run pip-audit
uv run safety check
```

## Versioning

```shell
uv version --bump <major|minor|patch|alpha|beta|rc|stable>
```

The version is **not** only in `pyproject.toml`: also `version.txt` and
`[tool.poetry]`. Always after merging a completed task, run:

```shell
uv version --bump alpha
```

The version commit stays on `dev`:

```shell
git commit -m "build: $(uv version)"
```

## Delivery flow

1. Branch derived from `dev`, with an open issue.
2. Test for the criterion **before** the implementation (red → green → refactor).
3. `ruff`/`mypy`/`pytest` green before committing.
4. `--no-ff` merge into `dev` with review by Kevin.

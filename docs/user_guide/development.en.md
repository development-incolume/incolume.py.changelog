# Contribution Guide (Development)

Rules and conventions for developing `incolume.py.changelog`.

## Code of conduct

Details in the [Code of Conduct](code_of_conduct).

## Applied standards

Project methodologies and conventions in
[Conventions and Methodologies](README).

## Requirements

- Git
- Python `>=3.11,<4`
- `uv` (preferred)

## Development environment

```shell
git clone https://github.com/development-incolume/incolume.py.changelog.git
cd incolume.py.changelog
uv sync --python 3.12
uv run task setup
```

- `uv sync` creates the environment and installs the dependencies from
  `pyproject.toml` as locked in `uv.lock`.
- `uv run task setup` sets `git config core.hooksPath .git-hooks/`, enabling the
  project hooks.

## Code quality

```shell
uv run ruff check tests incolume
uv run ruff format tests incolume
uv run mypy tests incolume
uv run pytest
```

- Minimum coverage: **99.7%**.
- Do not edit tests to make the implementation pass.

## Multi-version tests

```shell
uv run tox
uv run tox -e 3.11
uv run tox -e typing
uv run tox -e lint
```

## Automation (taskipy)

```shell
uv run task -l
```

Main tasks: `tests`, `lint`, `changelog`, `docs-serve`, `docs-build`,
`safety`, `setup`.

## Documentation

```shell
uv run task docs-serve   # local server
uv run task docs-build   # build and publish to the webdoc branch
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

The version lives in `pyproject.toml` (`[project]`) and must be reflected in
`[tool.poetry]` and in `incolume/py/changelog/version.txt`. The version commit is
`build: incolume-py-changelog <version>`, on `dev`, after the merge.

## Delivery flow

- Branch derived from `dev`, with an open issue.
- Criterion test before the implementation.
- `ruff`/`mypy`/`pytest` green before committing.
- Merge `--no-ff` (reviewed by Kevin).

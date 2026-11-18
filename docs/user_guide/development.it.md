# Guida al Contributo (Sviluppo)

Regole e convenzioni per sviluppare `incolume.py.changelog`.

## Codice di condotta

Dettagli nel [Codice di condotta](code_of_conduct.md).

## Standard applicati

Metodologie e convenzioni del progetto in
[Convenzioni e Metodologie](README.md).

## Prerequisiti

- Git
- Python `>=3.11,<4`
- `uv` (consigliato)

## Ambiente di sviluppo

```shell
git clone https://github.com/development-incolume/incolume.py.changelog.git
cd incolume.py.changelog
uv sync --python 3.12
uv run task setup
```

- `uv sync` crea l'ambiente e installa le dipendenze da `pyproject.toml`
  come specificato in `uv.lock`.
- `uv run task setup` imposta `git config core.hooksPath .git-hooks/`, attivando
  gli hook del progetto.

## Qualità del codice

```shell
uv run ruff check tests incolume
uv run ruff format tests incolume
uv run mypy tests incolume
uv run pytest
```

- Copertura minima: **99,7%**.
- Non modificare i test per far passare l'implementazione.

## Test multi-versione

```shell
uv run tox
uv run tox -e 3.11
uv run tox -e typing
uv run tox -e lint
```

## Automazione (taskipy)

```shell
uv run task -l
```

Attività principali: `tests`, `lint`, `changelog`, `docs-serve`, `docs-build`,
`safety`, `setup`.

## Documentazione

```shell
uv run task docs-serve   # server locale
uv run task docs-build   # genera e pubblica sul branch webdoc
```

## Sicurezza

```shell
uv run bandit -c pyproject.toml -r incolume/
uv run pip-audit
uv run safety check
```

## Versionamento

```shell
uv version --bump <major|minor|patch|alpha|beta|rc|stable>
```

La versione è definita in `pyproject.toml` (`[project]`) e deve essere riportata in
`[tool.poetry]` e in `incolume/py/changelog/version.txt`. Il commit di versione è
`build: incolume-py-changelog <versione>`, nel branch `dev`, dopo il merge.

## Flusso di consegna

- Branch derivato da `dev`, con una issue aperta.
- Test del criterio prima dell'implementazione.
- `ruff`/`mypy`/`pytest` verdi prima del commit.
- Merge `--no-ff` (revisione di Kevin).

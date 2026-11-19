# Guida al Contributo (Sviluppo)

Documentazione rapida per i contributori di `incolume.py.changelog`.

## Da dove iniziare

1. Leggi l'[AGENTS.md](../agents.md) – regole di lavoro, identità e flusso di
   consegna.
2. Leggi lo [SPEC-001](https://github.com/development-incolume/incolume.py.changelog/blob/dev/docs/analysis_artifacts/SPEC-001-execucao.md) se serve il
   dettaglio dell'esecuzione.
3. Leggi il [PLAN-001](https://github.com/development-incolume/incolume.py.changelog/blob/dev/docs/analysis_artifacts/PLAN-001-documentacao.md) sul
   miglioramento della documentazione.

## Ma non è necessario leggere tutto in una volta

Il documento di esecuzione qui sotto è il punto di partenza per le attività del
nucleo Backend/API:

- `src/…`, `config/` e `apps/core/` — il livello backend/API;
- Issue AC-02, AC-11, AC-12, AC-15, AC-18 e AC-19.

Non è più responsabilità di chi legge questo documento gli adattatori, la
sanificazione (e ora `Bob` in `adapters/office/` e `render/`).

## Prerequisiti

- Git
- Python `>=3.11,<4`
- `uv` (consigliato)
- L'identità attuale del repository:

```shell
git config user.name "Britodfbr"
git config user.email "brito@incolume.com.br"
```

## Ambiente di sviluppo

```shell
git clone https://github.com/development-incolume/incolume.py.changelog.git
cd incolume.py.changelog
uv sync --python 3.12
uv run task setup
```

- `uv sync` crea l'ambiente e installa le dipendenze da `pyproject.toml`
  come specificato in `uv.lock`.
- `uv run task setup` imposta `git config core.hooksPath .git-hooks/`,
  attivando gli hook del progetto.

## Qualità del codice

```shell
uv run ruff check tests incolume
uv run ruff format tests incolume
uv run mypy tests incolume
uv run pytest
```

- Copertura minima: **99,7%**.
- Non modificare mai i test per far passare l'implementazione.

## Test multi-versione

```shell
uv run tox
uv run tox -e 3.11
uv run tox -e typing
uv run tox -e lint
```

## Automazione (`taskipy`)

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

La versione **non** è solo in `pyproject.toml`: anche in `version.txt` e in
`[tool.poetry]`. Sempre dopo il merge di un'attività completata eseguire:

```shell
uv version --bump alpha
```

Il commit di versione va in `dev`:

```shell
git commit -m "build: $(uv version)"
```

## Flusso di consegna

1. Branch derivato da `dev`, con una issue aperta.
2. Test del criterio **prima** dell'implementazione (rosso → verde →
   rifattorizzare).
3. `ruff`/`mypy`/`pytest` verdi prima del commit.
4. Merge `--no-ff` in `dev` con la revisione di Kevin.

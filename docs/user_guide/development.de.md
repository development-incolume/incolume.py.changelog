# Beitragsleitfaden (Entwicklung)

Regeln und Konventionen zur Entwicklung von `incolume.py.changelog`.

## Verhaltenskodex

Details im [Verhaltenskodex](code_of_conduct).

## Angewandte Standards

Methodiken und Konventionen des Projekts in
[Konventionen und Methodiken](README).

## Anforderungen

- Git
- Python `>=3.11,<4`
- `uv` (bevorzugt)

## Entwicklungsumgebung

```shell
git clone https://github.com/development-incolume/incolume.py.changelog.git
cd incolume.py.changelog
uv sync --python 3.12
uv run task setup
```

- `uv sync` erstellt die Umgebung und installiert die Abhängigkeiten aus
  `pyproject.toml` gemäß `uv.lock`.
- `uv run task setup` setzt `git config core.hooksPath .git-hooks/` und aktiviert
  die Projekt-Hooks.

## Code-Qualität

```shell
uv run ruff check tests incolume
uv run ruff format tests incolume
uv run mypy tests incolume
uv run pytest
```

- Minimale Abdeckung: **99,7 %**.
- Tests nicht ändern, damit die Implementierung besteht.

## Multi-Version-Tests

```shell
uv run tox
uv run tox -e 3.11
uv run tox -e typing
uv run tox -e lint
```

## Automatisierung (taskipy)

```shell
uv run task -l
```

Wichtigste Aufgaben: `tests`, `lint`, `changelog`, `docs-serve`, `docs-build`,
`safety`, `setup`.

## Dokumentation

```shell
uv run task docs-serve   # lokaler Server
uv run task docs-build   # erzeugen und im Branch webdoc veröffentlichen
```

## Sicherheit

```shell
uv run bandit -c pyproject.toml -r incolume/
uv run pip-audit
uv run safety check
```

## Versionierung

```shell
uv version --bump <major|minor|patch|alpha|beta|rc|stable>
```

Die Version liegt in `pyproject.toml` (`[project]`) und muss in
`[tool.poetry]` sowie in `incolume/py/changelog/version.txt` übernommen werden.
Der Versions-Commit ist `build: incolume-py-changelog <Version>`, auf `dev`,
nach dem Merge.

## Abliefluss

- Branch abgeleitet von `dev`, mit geöffneter Issue.
- Kriterientest vor der Implementierung.
- `ruff`/`mypy`/`pytest` grün vor dem Commit.
- Merge `--no-ff` (Prüfung durch Kevin).

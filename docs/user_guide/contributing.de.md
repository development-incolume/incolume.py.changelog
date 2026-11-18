# Beitragsleitfaden (Entwicklung)

Kurzanleitung für Mitwirkende an `incolume.py.changelog`.

## Wo anfangen

1. Lesen Sie die [AGENTS.md](../../AGENTS.md) – Regeln, Identität und
   Ablieferungsfluss.
2. Lesen Sie [SPEC-001](../analysis_artifacts/SPEC-001-execucao.md), wenn Sie die
   Details der Umsetzung benötigen.
3. Lesen Sie [PLAN-001](../analysis_artifacts/PLAN-001-documentacao.md) zur
   Verbesserung der Dokumentation.

## Aber Sie müssen nicht alles auf einmal lesen

Das Umsetzungsdokument unten ist der Ausgangspunkt für die Aufgaben des
Backend-/API-Kerns:

- `src/…`, `config/` und `apps/core/` — die Backend-/API-Schicht;
- Issues AC-02, AC-11, AC-12, AC-15, AC-18 und AC-19.

Adapter, Sanitisierung (und mittlerweile `Bob` in `adapters/office/` und
`render/`) liegen nicht mehr in der Verantwortung der Person, die dieses
Dokument liest.

## Voraussetzungen

- Git
- Python `>=3.11,<4`
- `uv` (bevorzugt)
- Die aktuelle Repository-Identität:

```shell
git config user.name "Britodfbr"
git config user.email "brito@incolume.com.br"
```

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
- Tests niemals bearbeiten, damit die Implementierung besteht.

## Multi-Version-Tests

```shell
uv run tox
uv run tox -e 3.11
uv run tox -e typing
uv run tox -e lint
```

## Automatisierung (`taskipy`)

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

Die Version steht **nicht** nur in `pyproject.toml`: auch in `version.txt` und
`[tool.poetry]`. Führen Sie nach dem Merge einer abgeschlossenen Aufgabe immer
aus:

```shell
uv version --bump alpha
```

Der Versions-Commit liegt auf `dev`:

```shell
git commit -m "build: $(uv version)"
```

## Ablieferungsfluss

1. Branch abgeleitet von `dev`, mit geöffneter Issue.
2. Kriterientest **vor** der Implementierung (rot → grün → refaktorisieren).
3. `ruff`/`mypy`/`pytest` grün vor dem Commit.
4. Merge `--no-ff` nach `dev` mit Prüfung durch Kevin.

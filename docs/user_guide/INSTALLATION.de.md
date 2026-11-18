# Installation

Das `incolume.py.changelog` wird auf PyPI und TestPyPI veröffentlicht.

## Anforderungen

- Python `>=3.11,<4`
- `pip`, `pipenv`, `poetry` oder `uv`

## Mit pip

```shell
pip install incolume.py.changelog
```

## Mit pipenv

```shell
pipenv install incolume.py.changelog
```

## Mit poetry

```shell
poetry add incolume.py.changelog
```

Direkt aus dem Repository:

```shell
poetry add git+https://github.com/development-incolume/incolume.py.changelog.git
```

## Mit uv

In einem Projekt:

```shell
uv add incolume.py.changelog
```

In einer virtuellen Umgebung:

```shell
uv venv -p 3.12
uv pip install incolume.py.changelog
```

## Test-Release (TestPyPI)

```shell
uv pip install --index-url https://test.pypi.org/simple/ incolume.py.changelog
```

## Installation prüfen

```shell
uv run changelog --help
uv run python -c "import incolume.py.changelog as c; print(c.__version__)"
```

## Installation für die Entwicklung

```shell
git clone https://github.com/development-incolume/incolume.py.changelog.git
cd incolume.py.changelog
uv sync --python 3.12
uv run task setup
```

Siehe die [Entwicklung](development)-Anleitung für die komplette Umgebung.

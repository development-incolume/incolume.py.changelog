# Installation

Le `incolume.py.changelog` est publié sur PyPI et TestPyPI.

## Prérequis

- Python `>=3.11,<4`
- `pip`, `pipenv`, `poetry` ou `uv`

## Avec pip

```shell
pip install incolume.py.changelog
```

## Avec pipenv

```shell
pipenv install incolume.py.changelog
```

## Avec poetry

```shell
poetry add incolume.py.changelog
```

Directement depuis le dépôt :

```shell
poetry add git+https://github.com/development-incolume/incolume.py.changelog.git
```

## Avec uv

Dans un projet :

```shell
uv add incolume.py.changelog
```

Dans un environnement virtuel :

```shell
uv venv -p 3.12
uv pip install incolume.py.changelog
```

## Version de test (TestPyPI)

```shell
uv pip install --index-url https://test.pypi.org/simple/ incolume.py.changelog
```

## Vérifier l'installation

```shell
uv run changelog --help
uv run python -c "import incolume.py.changelog as c; print(c.__version__)"
```

## Installation pour le développement

```shell
git clone https://github.com/development-incolume/incolume.py.changelog.git
cd incolume.py.changelog
uv sync --python 3.12
uv run task setup
```

Voir le guide [Développement](development.md) pour l'environnement complet.

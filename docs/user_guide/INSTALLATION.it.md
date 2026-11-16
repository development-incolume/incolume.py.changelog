# Installazione

Il `incolume.py.changelog` è pubblicato su PyPI e TestPyPI.

## Requisiti

- Python `>=3.11,<4`
- `pip`, `pipenv`, `poetry` o `uv`

## Con pip

```shell
pip install incolume.py.changelog
```

## Con pipenv

```shell
pipenv install incolume.py.changelog
```

## Con poetry

```shell
poetry add incolume.py.changelog
```

Direttamente dal repository:

```shell
poetry add git+https://github.com/development-incolume/incolume.py.changelog.git
```

## Con uv

In un progetto:

```shell
uv add incolume.py.changelog
```

In un ambiente virtuale:

```shell
uv venv -p 3.12
uv pip install incolume.py.changelog
```

## Versione di test (TestPyPI)

```shell
uv pip install --index-url https://test.pypi.org/simple/ incolume.py.changelog
```

## Verificare l'installazione

```shell
uv run changelog --help
uv run python -c "import incolume.py.changelog as c; print(c.__version__)"
```

## Installazione per lo sviluppo

```shell
git clone https://github.com/development-incolume/incolume.py.changelog.git
cd incolume.py.changelog
uv sync --python 3.12
uv run task setup
```

Vedi la guida [Sviluppo](development) per l'ambiente completo.

# Instalação

O `incolume.py.changelog` é publicado no PyPI e no TestPyPI.

## Requisitos

- Python `>=3.11,<4`
- `pip`, `pipenv`, `poetry` ou `uv`

## Com pip

```shell
pip install incolume.py.changelog
```

## Com pipenv

```shell
pipenv install incolume.py.changelog
```

## Com poetry

```shell
poetry add incolume.py.changelog
```

Diretamente do repositório:

```shell
poetry add git+https://github.com/development-incolume/incolume.py.changelog.git
```

## Com uv

Em um projeto:

```shell
uv add incolume.py.changelog
```

Em um ambiente virtual:

```shell
uv venv -p 3.12
uv pip install incolume.py.changelog
```

## Versão de testes (TestPyPI)

```shell
uv pip install --index-url https://test.pypi.org/simple/ incolume.py.changelog
```

## Verificar a instalação

```shell
uv run changelog --help
uv run python -c "import incolume.py.changelog as c; print(c.__version__)"
```

## Instalação para desenvolvimento

```shell
git clone https://github.com/development-incolume/incolume.py.changelog.git
cd incolume.py.changelog
uv sync --python 3.12
uv run task setup
```

Veja o [Desenvolvimento](development) para o ambiente completo.

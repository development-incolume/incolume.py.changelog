# Instalación

El `incolume.py.changelog` se publica en PyPI y TestPyPI.

## Requisitos

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

Directamente desde el repositorio:

```shell
poetry add git+https://github.com/development-incolume/incolume.py.changelog.git
```

## Con uv

En un proyecto:

```shell
uv add incolume.py.changelog
```

En un entorno virtual:

```shell
uv venv -p 3.12
uv pip install incolume.py.changelog
```

## Versión de prueba (TestPyPI)

```shell
uv pip install --index-url https://test.pypi.org/simple/ incolume.py.changelog
```

## Verificar la instalación

```shell
uv run changelog --help
uv run python -c "import incolume.py.changelog as c; print(c.__version__)"
```

## Instalación para desarrollo

```shell
git clone https://github.com/development-incolume/incolume.py.changelog.git
cd incolume.py.changelog
uv sync --python 3.12
uv run task setup
```

Consulta la guía de [Desarrollo](development.md) para el entorno completo.

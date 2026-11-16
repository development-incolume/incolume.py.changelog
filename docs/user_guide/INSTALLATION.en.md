# Installation

The `incolume.py.changelog` is published on PyPI and TestPyPI.

## Requirements

- Python `>=3.11,<4`
- `pip`, `pipenv`, `poetry` or `uv`

## With pip

```shell
pip install incolume.py.changelog
```

## With pipenv

```shell
pipenv install incolume.py.changelog
```

## With poetry

```shell
poetry add incolume.py.changelog
```

Directly from the repository:

```shell
poetry add git+https://github.com/development-incolume/incolume.py.changelog.git
```

## With uv

In a project:

```shell
uv add incolume.py.changelog
```

In a virtual environment:

```shell
uv venv -p 3.12
uv pip install incolume.py.changelog
```

## Test release (TestPyPI)

```shell
uv pip install --index-url https://test.pypi.org/simple/ incolume.py.changelog
```

## Verify the installation

```shell
uv run changelog --help
uv run python -c "import incolume.py.changelog as c; print(c.__version__)"
```

## Installation for development

```shell
git clone https://github.com/development-incolume/incolume.py.changelog.git
cd incolume.py.changelog
uv sync --python 3.12
uv run task setup
```

See the [Development](development) guide for the full environment.

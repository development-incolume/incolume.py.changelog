# Incolume Python Changelog

--------

_Projeto desenvolvido e administrado por incolume.com.br_

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/incolume.py.changelog?color=00FFFF)
[![Codecov](https://img.shields.io/codecov/c/github/development-incolume/incolume.py.changelog?color=00FFFF&label=codecov&logo=codecov)]((https://codecov.io/gh/development-incolume/incolume.py.changelog))
![PyPI - Version](https://img.shields.io/pypi/v/incolume.py.changelog?color=00FFFF&label=pypi+package)

[![Tests CI/CD](https://github.com/development-incolume/incolume.py.changelog/actions/workflows/unit-tests.yml/badge.svg)](https://github.com/development-incolume/incolume.py.changelog/actions/workflows/unit-tests.yml)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/incolume.py.changelog)
![PyPI - Status](https://img.shields.io/pypi/status/incolume.py.changelog)

[![Metodology: PEP8](https://img.shields.io/badge/%20Metodology-PEP8-%23aabbcc?style=flat&labelColor=4444444)](https://peps.python.org/pep-0008/)
[![Metodology: PEP20](https://img.shields.io/badge/%20Metodology-PEP20-%23aabbcc?style=flat&labelColor=4444444)](https://peps.python.org/pep-0020/)
[![Metodology: SemVer](https://img.shields.io/badge/%20Metodology-SemVer-%23aabbcc?style=flat&labelColor=4444444)](https://semver.org/lang/pt-BR)
[![Metodology: keep-a-changelog](https://img.shields.io/badge/%20Metodology-keepachangelog-%23aabbcc?style=flat&labelColor=4444444)](https://keepachangelog.com/pt-BR/1.0.0/)
[![Metodology: conventionalcommits](https://img.shields.io/badge/%20Metodology-conventionalcommits-%23aabbcc?style=flat&labelColor=4444444)](https://www.conventionalcommits.org/pt-br/v1.0.0/#specification)

[!["style: ruff"](https://img.shields.io/badge/code%20style-ruff-black)](https://github.com/astral-sh/ruff)
[![Style: isort](https://img.shields.io/badge/%20Format%20Style-isort-black?style=flat&labelColor=4444444)](https://pycqa.github.io/isort/)
[![style: pydocstyle](https://img.shields.io/badge/%20Format%20Style-pydocstyle-black?style=flat&labelColor=444444)](http://www.pydocstyle.org/en/stable/)

[![Linter: mypy](https://img.shields.io/badge/%20Linter-Mypy-blue?color=000000)](https://mypy.readthedocs.io/en/stable/)
[![Linter: pylint](https://img.shields.io/badge/%20Linter-pylint-blue?color=000000)](https://pylint.pycqa.org/en/latest/)
[![Linter: flake8](https://img.shields.io/badge/%20Linter-flake8-blue?color=000000)](https://flake8.pycqa.org/en/latest/)

[![security: bandit](https://img.shields.io/badge/%20Security-bandit-red?color=6633cc)](https://bandit.readthedocs.io/en/latest/)
[![security: pipaudit](https://img.shields.io/badge/%20Security-pipaudit-red?color=6633cc)](https://pypi.org/project/pip-audit/)
[![security: safety](https://img.shields.io/badge/%20Security-safety-red?color=6633cc)](https://pypi.org/project/safety/)

![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/development-incolume/incolume.py.changelog?color=d5f56c)
![GitHub repo size](https://img.shields.io/github/repo-size/development-incolume/incolume.py.changelog?color=d5f56c)

[![Downloads](https://pepy.tech/badge/incolume-py-changelog?color=black)](https://pepy.tech/project/incolume-py-changelog)
[![Downloads](https://pepy.tech/badge/incolume-py-changelog/month)](https://pepy.tech/project/incolume-py-changelog)
[![Downloads](https://pepy.tech/badge/incolume-py-changelog/week)](https://pepy.tech/project/incolume-py-changelog)

![GitHub issues](https://img.shields.io/github/issues-raw/development-incolume/incolume.py.changelog?color=1383eb)
![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/development-incolume/incolume.py.changelog?color=1383eb)
![GitHub issues by-label](https://img.shields.io/github/issues-raw/development-incolume/incolume.py.changelog/enhancement?color=1383eb)
![GitHub closed issues by-label](https://img.shields.io/github/issues-closed-raw/development-incolume/incolume.py.changelog/enhancement?color=1383eb)
![GitHub issues by-label](https://img.shields.io/github/issues-raw/development-incolume/incolume.py.changelog/bug?color=1383eb)

![PyPI - License](https://img.shields.io/pypi/l/incolume.py.changelog?color=75545d)
---

### Incolume Python Changelog

Este gera o Changelog a partir dos registros encontrados em `git tag -n`.

## Instalar o pacote

### Instalação com pip
```shell
pip install incolume.py.changelog
```
### Instalação com pipenv
```shell
pipenv install incolume.py.changelog
```

### Instalação com poetry
```shell
poetry add -G dev incolume.py.changelog
```

```shell
poetry add -G dev git+https://github.com/development-incolume/incolume.py.changelog#main
```

### Instalação com uv
```shell
uv venv -p 3.8
uv pip add --dev incolume.py.changelog==0.13.1
```

## Atualizar o pacote
### Atualização com pip
```shell
pip install -U incolume.py.changelog
```
### Atualização com pipenv
```shell
pipenv update incolume.py.changelog
```
### Atualização com poetry
```shell
poetry update -G dev incolume.py.changelog
```

```shell
poetry update -G dev git+https://github.com/development-incolume/incolume.py.changelog#main
```

### Atualização com uv
```shell
uv venv -p 3.8
uv pip add --dev incolume.py.changelog==0.13.1
```

## Gerar pacote a partir dos fontes para instalação

```shell
poetry build
```

## Exemplos e Uso
Exemplos e outras curiosidades sobre este projeto podem
ser visualizadas em [docs/api](docs/api/index.md).


## Registro de Mudanças ##
Disponível em [docs/about/CHANGELOG.md](docs/about/CHANGELOG.md).


## Contribuidores ##
Disponível em [docs/about/CONTRIBUTORS.md](docs/about/CONTRIBUTORS.md).


## Tecnologias adotadas
Disponível em [docs/user_guide/development.md](docs/user_guide/development.md).
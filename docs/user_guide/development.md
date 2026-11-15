# Guia de Contribuição (Desenvolvimento)

Regras e convenções para desenvolver o `incolume.py.changelog`.

## Código de conduta

Detalhes em [Código de Conduta](code_of_conduct.md).

## Padrões aplicados

Metodologias e convenções do projeto em
[Convenções e Metodologias](README.md).

## Pré-requisitos

- Git
- Python `>=3.11,<4`
- `uv` (preferencial)

## Ambiente de desenvolvimento

```shell
git clone https://github.com/development-incolume/incolume.py.changelog.git
cd incolume.py.changelog
uv sync --python 3.12
uv run task setup
```

- `uv sync` cria o ambiente e instala as dependências de `pyproject.toml`
  conforme `uv.lock`.
- `uv run task setup` configura `git config core.hooksPath .git-hooks/`,
  ativando os hooks do projeto.

## Qualidade de código

```shell
uv run ruff check tests incolume
uv run ruff format tests incolume
uv run mypy tests incolume
uv run pytest
```

- Cobertura mínima: **99,7%**.
- Não editar testes para a implementação passar.

## Testes multi-versão

```shell
uv run tox
uv run tox -e 3.11
uv run tox -e typing
uv run tox -e lint
```

## Automação (taskipy)

```shell
uv run task -l
```

Principais tarefas: `tests`, `lint`, `changelog`, `docs-serve`, `docs-build`,
`safety`, `setup`.

## Documentação

```shell
uv run task docs-serve   # servidor local
uv run task docs-build   # gerar e publicar no branch webdoc
```

## Segurança

```shell
uv run bandit -c pyproject.toml -r incolume/
uv run pip-audit
uv run safety check
```

## Versionamento

```shell
uv version --bump <major|minor|patch|alpha|beta|rc|stable>
```

A versão vive em `pyproject.toml` (`[project]`) e deve ser refletida em
`[tool.poetry]` e em `incolume/py/changelog/version.txt`. O commit de versão é
`build: incolume-py-changelog <versão>`, em `dev`, após o merge.

## Fluxo de entrega

- Branch derivada de `dev`, com issue aberta.
- Teste do critério antes da implementação.
- `ruff`/`mypy`/`pytest` verdes antes de committer.
- Merge `--no-ff` (revisão do Kevin).

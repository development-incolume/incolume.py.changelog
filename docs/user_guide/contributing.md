# Guia de Contribuição (Desenvolvimento)

Documentação rápida para colaboradores do `incolume.py.changelog`.

## Onde começa

1. Leia o [AGENTS.md](../../AGENTS.md) – regras de trabalho, identidade e fluxo de
   entrega.
2. Leia o [SPEC-001](../analysis_artifacts/SPEC-001-execucao.md) se precisar
   do detalhamento da execução.
3. Leia o [PLAN-001](../analysis_artifacts/PLAN-001-documentacao.md) sobre a
   melhoria da documentação.

## Mas não precisa ler tudo de uma vez

O documento de execução abaixo é o ponto de partida para as tarefas do
núcleo de Backend/API:

- `src/…`, `config/` e `apps/core/` — a camada de backend/API;
- Issues AC-02, AC-11, AC-12, AC-15, AC-18 e AC-19.

Não é mais responsabilidade de quem lê este documento adaptadores, sanitização
(e agora `Bob` em `adapters/office/` e `render/`).

## Pré-requisitos

- Git
- Python `>=3.11,<4`
- `uv` (preferencial)
- A identidade atual do repositório:

```shell
git config user.name "Britodfbr"
git config user.email "brito@incolume.com.br"
```

## Ambiente de desenvolvimento

```shell
git clone https://github.com/development-incolume/incolume.py.changelog.git
cd incolume.py.changelog
uv sync --python 3.12
uv run task setup
```

- `uv sync` criará o ambiente e instalará as dependências de `pyproject.toml`
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
- Nunca edite teste para a implementação passar.

## Testes multi-versão

```shell
uv run tox
uv run tox -e 3.11
uv run tox -e typing
uv run tox -e lint
```

## Automação (`taskipy`)

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

A versão **não** está no `pyproject.toml` só: também `version.txt` e
`[tool.poetry]`. Sempre após o merge de uma tarefa concluída rode:

```shell
uv version --bump alpha
```

O commit de versão fica em `dev`:

```shell
git commit -m "build: $(uv version)"
```

## Fluxo de entrega

1. Branch derivada de `dev`, com issue aberta.
2. Teste do critério **antes** da implementação (vermelho → verde → refatorar).
3. `ruff`/`mypy`/`pytest` verdes antes de commitar.
4. Merge `--no-ff` em `dev` com a revisão do Kevin.

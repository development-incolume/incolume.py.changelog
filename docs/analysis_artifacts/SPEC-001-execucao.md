# SPEC-001 — Execução: geração e manutenção do CHANGELOG

- **Data:** 2026-11-14
- **Projeto:** incolume.py.changelog
- **Versão do produto:** 1.5.0
- **Status:** Proposta (aguardando revisão)
- **Autor:** Brito (Britodfbr)
- **Coautor:** Dr. Nefário OpenBot
- **Fonte:** derivado do repositório — `pyproject.toml`, `.changelog.toml`,
  `incolume/py/changelog/`, `.github/workflows/*.yml`, `mkdocs.yml`, `tox.toml`.

## 1. Escopo

Como gerar, configurar, validar e publicar o `CHANGELOG.md`, e como manter a
documentação do projeto. Detalha o "como" do `PRD-001` sob as decisões do
`ADR-001`.

## 2. Pré-requisitos

- Python `>=3.11,<4` e `uv`.
- Repositório git com tags anotadas.
- No repositório: `uv sync --python 3.12` (o `uv` pode escolher 3.15, que ainda
  não tem wheel para algumas dependências).

## 3. Gerar o CHANGELOG

```shell
uv run task changelog
```

O comando (taskipy `changelog`) executa `uv run gcl docs/about/CHANGELOG.md
-ru <url_compare>`, isto é, `update_changelog` com o arquivo e a URL de
compare da configuração.

- A fonte é `git tag -n`, lida em UTF-8 explícito (`get_git_tags`).
- O arquivo de saída é definido por `.changelog.toml` (`settings.file`).
- A ordem é reversa por padrão (`settings.reverse = true`).

### 3.1 Formato da anotação da tag

Uma linha por tag, com categorias separadas por `;`:

```
1.5.0  added: ...; changed: ...; fixed: ...;
```

Categorias aceitas (ignora maiúsculas/minúsculas):
`Added`, `Changed`, `Deprecated`, `Removed`, `Fixed`, `Security` e as
equivalentes pt-BR (`Adicionado`, `Modificado`, `Obsoleto`, `Removido`,
`Corrigido`, `Segurança`).

## 4. Configuração

Arquivos procurados, na ordem (`core.py::select_configuration_fl`):
`changelog.toml`, `.changelog.toml`, `pyproject.toml`.

Chaves (`settings`):

| Chave | Tipo | Descrição |
|---|---|---|
| `file` | str | Caminho do CHANGELOG |
| `reverse` | bool | Ordem reversa |
| `url_compare` | str | URL base de compare |
| `url_keepachangelog` | str | URL do Keep a Changelog |
| `url_semver` | str | URL do SemVer |
| `url_convetional_commit` | str | URL do Conventional Commits |

Configuração parcial é aceita (qualquer subconjunto das chaves).

## 5. CLI

| Comando | Destino |
|---|---|
| `changelog`, `gcl`, `gencl`, `gchangelog` | `incolume.py.changelog.cli:changelog` |
| `greeting` | `incolume.py.changelog.cli:greeting` |

Opções do `changelog`: `file_changelog`, `--url/-u`, `--reverse/-r`,
`--generate-config/-g`.

## 6. Qualidade

```shell
uv run ruff check --fix tests incolume
uv run ruff format tests incolume
uv run mypy tests incolume
uv run pytest
```

- Cobertura mínima: 99,7%.
- Não editar testes para a implementação passar.

## 7. Documentação

- `docs/` com mkdocs Material; `nav` deve expor todos os `.md` (órfão é débito).
- Idiomas: pt-BR (default) + en/de/es/fr/it; verificar por arquivo, não pelo
  site (fallback esconde falta de tradução).
- Publicação: `mkdocs gh-deploy --remote-branch webdoc` no workflow `main`.

## 8. Versionamento e release

- `uv version --bump <sem>`; ajustar `[tool.poetry] version` e `version.txt`.
- Commit de versão em `dev`, após o merge: `build: incolume-py-changelog <v>`.
- Release: tag anotada → workflow `multplatform-ci-cd.yml` (build, release,
  publicação).

## 9. Pendências

- Padronizar os arquivos de versão e o `uv.lock` no commit de versão.
- Definir onde o `PLAN-001` e os artefatos ficam no `nav` do mkdocs.
- Alinhar o workflow de release para tags PEP 440 (`1.5.0a6`), que hoje não
  cria a GitHub Release automaticamente.

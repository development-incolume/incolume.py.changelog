# ADR-001 — Arquitetura: geração de CHANGELOG

- **Data:** 2026-11-14
- **Projeto:** incolume.py.changelog
- **Versão do produto:** 1.5.0
- **Status:** Proposta (aguardando revisão)
- **Autor:** Brito (Britodfbr)
- **Coautor:** Dr. Nefário OpenBot
- **Fonte:** derivado do repositório — `incolume/py/changelog/`, `pyproject.toml`,
  `.github/workflows/*.yml`, `mkdocs.yml`, `.changelog.toml`.

## Contexto

O repositório precisa de um CHANGELOG confiável, reproduzível e de baixo
esforço de manutenção, e de uma documentação pública multilíngue. As decisões
abaixo registram as escolhas de arquitetura que sustentam isso e as
consequências de cada uma.

## Decisões

### AD-01 — O CHANGELOG é gerado, nunca editado à mão

- **Decisão:** `docs/about/CHANGELOG.md` é saída do `incolume.py.changelog` a
  partir das anotações das tags (`git tag -n`).
- **Consequência:** correções passam por corrigir o gerador ou a anotação da
  tag e regerar (`uv run task changelog`). Nenhuma tarefa de documentação
  prevê edição manual.
- **Evidência:** `changelog.py::update_changelog`, `.changelog.toml`.

### AD-02 — Leitura das tags em UTF-8 explícito

- **Decisão:** `get_git_tags()` executa `git tag -n` e decodifica como UTF-8,
  independente do locale.
- **Consequência:** elimina o mojibake observado na 1.5.0 em ambiente não-UTF-8.
- **Evidência:** `changelog.py::get_git_tags`; issue #176 e PLAN-001.

### AD-03 — Python `>=3.11,<4` com `uv`

- **Decisão:** `uv` como gerenciador de ambiente e dependências; `pyproject.toml`
  e `uv.lock` versionados.
- **Consequência:** substitui `pyenv`, `bumpversion` e `twine`; ambiente
  reproduzível.

### AD-04 — `ruff` e `mypy` como únicos validadores de código

- **Decisão:** `ruff check`, `ruff format` e `mypy`.
- **Consequência:** `black`, `blue`, `isort`, `pydocstyle` e `pylint` foram
  descontinuados; a documentação do projeto não deve mais citá-los.

### AD-05 — Versão PEP 440 via `uv version`, espelhada em três arquivos

- **Decisão:** a versão vive em `pyproject.toml` (`[project]`) e é refletida em
  `[tool.poetry]` e em `incolume/py/changelog/version.txt`.
- **Consequência:** `uv version` não cobre todos os arquivos; o commit de
  versão é ajustado à mão nos que faltam.

### AD-06 — Pacote importável em `incolume/py/changelog/`

- **Decisão:** manter o pacote em `incolume/py/changelog/` (sem `src/`).
- **Consequência:** `mkdocstrings` usa `paths: [incolume]`; imports absolutos.

### AD-07 — Documentação mkdocs Material com i18n

- **Decisão:** mkdocs-material + `mkdocs-static-i18n`, pt-BR como default e
  fallback, com en/de/es/fr/it.
- **Consequência:** arquivos sem tradução renderizam o default; a matriz de
  cobertura deve ser verificada por arquivo, não pelo site.

### AD-08 — CHANGELOG em pt-BR; documentação traduzida

- **Decisão:** o CHANGELOG gerado é pt-BR (não é traduzido); a documentação é
  mantida nos seis idiomas.
- **Consequência:** revisão textual é exigida por idioma antes de aceitar o
  documento.

### AD-09 — CI por evento

- **Decisão:** `unit-tests.yml` em `dev`/PR; `multplatform-ci-cd.yml` em tag
  (build, release, publicação); `docs_ci_cd.yml` em `main` (deploy de docs).
- **Consequência:** a documentação só é publicada após o merge no `main`.

## Alternativas consideradas

- **CHANGELOG manual:** descartada — dessincroniza e não é auditável.
- **Gerador genérico (externo):** descartada — o repositório mantém o próprio
  gerador, integrando com o ecossistema incolume.

## Referências

- `PLAN-001-documentacao.md`, `PRD-001-geracao-changelog.md`,
  `SPEC-001-execucao.md`.

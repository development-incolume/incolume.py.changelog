# PRD-001 — Produto: geração de CHANGELOG

- **Data:** 2026-11-14
- **Projeto:** incolume.py.changelog
- **Versão do produto:** 1.7.0a11
- **Status:** Aprovado
- **Autor:** Brito (Britodfbr)
- **Coautor:** Dr. Nefário OpenBot
- **Fonte:** derivado do repositório — `README`, `docs/`, `pyproject.toml`,
  `incolume/py/changelog/`, `.changelog.toml` e issues.

## 1. Visão geral

O `incolume.py.changelog` é um pacote importável e uma CLI que gera o
`CHANGELOG` de um repositório a partir das anotações das tags
(`git tag -n`), classificando as mensagens em categorias e gravando o arquivo
no formato Keep a Changelog.

## 2. Problema

Manter `CHANGELOG` à mão é propenso a dessincronia com as tags, omite
alterações e gera retrabalho a cada release. A fonte de verdade das mudanças
já existe — as anotações das tags — mas não há um gerador próprio que as
converta em CHANGELOG de forma repetível e independente do ambiente.

## 3. Objetivos

- Gerar o `CHANGELOG` de forma determinística a partir de `git tag -n`.
- Padronizar as mensagens nas categorias do Keep a Changelog.
- Ser reutilizável pelos demais repositórios do ecossistema incolume.
- Documentar o produto em seis idiomas (pt, en, de, es, fr, it).

## 4. Público-alvo

- Mantenedores dos repositórios `incolume.py.*` e demais projetos Python que
  adotam Keep a Changelog + SemVer + Conventional Commits.

## 5. Requisitos funcionais

| ID | Requisito | Fonte de verdade |
|---|---|---|
| RF-01 | Ler as anotações das tags (`git tag -n`), decodificando como UTF-8 explícito | `incolume/py/changelog/changelog.py` |
| RF-02 | Classificar as mensagens em Added/Changed/Deprecated/Removed/Fixed/Security (e equivalentes pt-BR) | `changelog.py::msg_classify` |
| RF-03 | Gerar `CHANGELOG` com cabeçalho, corpo e rodapé (links de compare) | `changelog.py::changelog_write` |
| RF-04 | Ordenar as versões de forma reversa (mais recente primeiro) | `changelog.py::update_changelog` |
| RF-05 | Expor CLI `changelog`/`gcl`/`gencl`/`gchangelog` e `greeting` | `pyproject.toml::[project.scripts]` |
| RF-06 | Aceitar configuração em `changelog.toml`, `.changelog.toml` ou `pyproject.toml` | `core.py::load_config` |
| RF-07 | Permitir configuração parcial (apenas `file`, `reverse`, `url_compare`, `url_keepachangelog`, `url_semver`, `url_convetional_commit`) | `core.py::load_config` |
| RF-08 | Sincronizar a versão entre `[project]`, `[tool.poetry]` e `version.txt` | `core.py::update_version` |
| RF-09 | Publicar a documentação estática (mkdocs) a partir do `main` | `.github/workflows/docs_ci_cd.yml` |

## 6. Requisitos não funcionais

| ID | Requisito |
|---|---|
| RNF-01 | Python `>=3.11,<4` |
| RNF-02 | Gerenciador `uv`; `pyproject.toml` + `uv.lock` versionados |
| RNF-03 | Qualidade: `ruff check`, `ruff format`, `mypy` |
| RNF-04 | Testes `pytest` com cobertura mínima de 99,7% |
| RNF-05 | Multiplataforma (Windows, Linux, macOS) e multi-versão (3.11–3.14) |
| RNF-06 | Documentação em pt-BR (default) e en/de/es/fr/it |
| RNF-07 | O CHANGELOG gerado não depende do locale da máquina |

## 7. Fora de escopo

- Edição manual do `CHANGELOG` (é saída da ferramenta).
- Tradução do `CHANGELOG` (gerado).
- Criação/alteração de tags (a anotação é responsabilidade de quem releaseia).
- Publicação de release e versionamento (tratados no SPEC-001).

## 8. Métricas de sucesso

- `CHANGELOG` gerado sem mojibake e idêntico em qualquer ambiente.
- Documentação refletindo o repositório (deploy verde no `main`).
- Cobertura de testes ≥ 99,7% mantida.

## 9. Riscos

- Anotações de tag fora do padrão commitado → mensagens não classificadas.
- Tags não buscadas em pipelines (checkout sem `--tags`) → CHANGELOG vazio.
- Divergência entre as seis línguas da documentação.

## 10. Pendências

- Confirmar se o CHANGELOG deve existir por idioma (hoje: pt, gerado).
- Confirmar o destino da documentação de API (mkdocstrings já configurado).

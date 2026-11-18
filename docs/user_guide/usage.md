# Guia de Uso

Como gerar e manter o `CHANGELOG` com o `incolume.py.changelog`.

## Pré-requisitos

- Repositório git com **tags anotadas** (a anotação é a fonte do CHANGELOG).
- Ambiente com Python `>=3.11,<4` e `uv` (instalação em
  [Instalação](INSTALLATION)).

## Gerar o CHANGELOG

```shell
uv run task changelog
```

O comando lê `git tag -n`, classifica as mensagens e grava o arquivo
configurado (por padrão `docs/about/CHANGELOG`).

O arquivo é **gerado** — não deve ser editado à mão.

## CLI

| Comando | Descrição |
|---|---|
| `changelog [FILE]` | Gera o CHANGELOG no arquivo informado |
| `gcl`, `gencl`, `gchangelog` | Apelidos do comando acima |
| `greeting [NOME]` | Saudação de exemplo |

Opções do `changelog`:

| Opção | Atalho | Descrição |
|---|---|---|
| `--url` | `-u` | URL base de compare |
| `--reverse` | `-r` | Ordem reversa (mais recente primeiro) |
| `--generate-config` | `-g` | Gera um arquivo de configuração de exemplo |

## Configuração

Arquivos procurados, na ordem: `changelog.toml`, `.changelog.toml`,
`pyproject.toml` (seção `[tool.changelog.settings]`).

```toml
[settings]
file = "docs/about/CHANGELOG"
reverse = true
url_compare = "https://github.com/development-incolume/incolume.py.changelog/compare"
url_keepachangelog = "https://keepachangelog.com/en/1.0.0"
url_semver = "https://semver.org/spec/v2.0.0.html"
url_convetional_commit = "https://www.conventionalcommits.org/pt-br/v1.0.0"
```

A configuração pode ser parcial (qualquer subconjunto das chaves).

## Anotação das tags

Uma linha por tag, com categorias separadas por `;`:

```text
1.5.0  added: novo recurso; fixed: correção de falha;
```

Categorias aceitas: `Added`, `Changed`, `Deprecated`, `Removed`, `Fixed`,
`Security` e as equivalentes pt-BR (`Adicionado`, `Modificado`, `Obsoleto`,
`Removido`, `Corrigido`, `Segurança`).

## API Python

```python
from incolume.py.changelog.changelog import update_changelog

update_changelog(changelog_file='docs/about/CHANGELOG', reverse=True)
```

## Ver também

- [Instalação](INSTALLATION)
- [Documentação da API](../api/index)
- [Desenvolvimento](development)

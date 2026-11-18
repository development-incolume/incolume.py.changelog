# Usage Guide

How to generate and maintain the `CHANGELOG.md` with `incolume.py.changelog`.

## Requirements

- Git repository with **annotated tags** (the annotation is the source of the CHANGELOG).
- Environment with Python `>=3.11,<4` and `uv` (see
  [Installation](INSTALLATION.md)).

## Generate the CHANGELOG

```shell
uv run task changelog
```

The command reads `git tag -n`, classifies the messages and writes the
configured file (by default `docs/about/CHANGELOG.md`).

The file is **generated** — it must not be edited by hand.

## CLI

| Command | Description |
|---|---|
| `changelog [FILE]` | Generates the CHANGELOG in the given file |
| `gcl`, `gencl`, `gchangelog` | Aliases of the command above |
| `greeting [NAME]` | Example greeting |

Options of `changelog`:

| Option | Short | Description |
|---|---|---|
| `--url` | `-u` | Base compare URL |
| `--reverse` | `-r` | Reverse order (newest first) |
| `--generate-config` | `-g` | Generates an example configuration file |

## Configuration

Files looked up, in order: `changelog.toml`, `.changelog.toml`,
`pyproject.toml` (`[tool.changelog.settings]` section).

```toml
[settings]
file = "docs/about/CHANGELOG.md"
reverse = true
url_compare = "https://github.com/development-incolume/incolume.py.changelog/compare"
url_keepachangelog = "https://keepachangelog.com/en/1.0.0"
url_semver = "https://semver.org/spec/v2.0.0.html"
url_convetional_commit = "https://www.conventionalcommits.org/pt-br/v1.0.0"
```

The configuration may be partial (any subset of the keys).

## Tag annotation

One line per tag, with categories separated by `;`:

```text
1.5.0  added: new feature; fixed: bug fix;
```

Accepted categories: `Added`, `Changed`, `Deprecated`, `Removed`, `Fixed`,
`Security` and the pt-BR equivalents (`Adicionado`, `Modificado`, `Obsoleto`,
`Removido`, `Corrigido`, `Segurança`).

## Python API

```python
from incolume.py.changelog.changelog import update_changelog

update_changelog(changelog_file='docs/about/CHANGELOG.md', reverse=True)
```

## See also

- [Installation](INSTALLATION.md)
- [API Documentation](../api/index.md)
- [Development](development.md)

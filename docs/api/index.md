# Documentação da API

Documentação automática dos módulos do `incolume.py.changelog`, gerada com
mkdocstrings a partir das docstrings do código.

## Módulos

::: incolume.py.changelog

::: incolume.py.changelog.changelog

::: incolume.py.changelog.core

::: incolume.py.changelog.cli

## Uso rápido

Via API Python:

```python
from incolume.py.changelog.changelog import update_changelog

update_changelog(changelog_file='docs/about/CHANGELOG.md', reverse=True)
```

Via CLI:

```shell
uv run changelog docs/about/CHANGELOG.md --reverse
```

Veja o [Guia de Uso](../user_guide/usage.md) e a
[Instalação](../user_guide/INSTALLATION.md).

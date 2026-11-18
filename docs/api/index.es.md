# Documentación de la API

Documentación automática de los módulos de `incolume.py.changelog`, generada con
mkdocstrings a partir de los docstrings del código.

## Módulos

::: incolume.py.changelog

::: incolume.py.changelog.changelog

::: incolume.py.changelog.core

::: incolume.py.changelog.cli

## Uso rápido

Vía API de Python:

```python
from incolume.py.changelog.changelog import update_changelog

update_changelog(changelog_file='docs/about/CHANGELOG.md', reverse=True)
```

Vía CLI:

```shell
uv run changelog docs/about/CHANGELOG.md --reverse
```

Consulta la [Guía de uso](../user_guide/usage.md) y la
[Instalación](../user_guide/INSTALLATION.md).

# Documentation de l'API

Documentation automatique des modules de `incolume.py.changelog`, générée avec
mkdocstrings à partir des docstrings du code.

## Modules

::: incolume.py.changelog

::: incolume.py.changelog.changelog

::: incolume.py.changelog.core

::: incolume.py.changelog.cli

## Démarrage rapide

Via l'API Python :

```python
from incolume.py.changelog.changelog import update_changelog

update_changelog(changelog_file='docs/about/CHANGELOG.md', reverse=True)
```

Via la CLI :

```shell
uv run changelog docs/about/CHANGELOG.md --reverse
```

Voir le [Guide d'utilisation](../user_guide/usage.md) et
l'[Installation](../user_guide/INSTALLATION.md).

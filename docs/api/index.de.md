# API-Dokumentation

Automatische Dokumentation der Module von `incolume.py.changelog`, erzeugt mit
mkdocstrings aus den Docstrings des Codes.

## Module

::: incolume.py.changelog

::: incolume.py.changelog.changelog

::: incolume.py.changelog.core

::: incolume.py.changelog.cli

## Schnellstart

Über die Python-API:

```python
from incolume.py.changelog.changelog import update_changelog

update_changelog(changelog_file='docs/about/CHANGELOG', reverse=True)
```

Über die CLI:

```shell
uv run changelog docs/about/CHANGELOG --reverse
```

Siehe die [Verwendung](../user_guide/usage) und die
[Installation](../user_guide/INSTALLATION).

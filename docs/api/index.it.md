# Documentazione dell'API

Documentazione automatica dei moduli di `incolume.py.changelog`, generata con
mkdocstrings a partire dalle docstring del codice.

## Moduli

::: incolume.py.changelog

::: incolume.py.changelog.changelog

::: incolume.py.changelog.core

::: incolume.py.changelog.cli

## Avvio rapido

Via API Python:

```python
from incolume.py.changelog.changelog import update_changelog

update_changelog(changelog_file='docs/about/CHANGELOG', reverse=True)
```

Via CLI:

```shell
uv run changelog docs/about/CHANGELOG --reverse
```

Vedi la [Guida all'uso](../user_guide/usage) e
l'[Installazione](../user_guide/INSTALLATION).

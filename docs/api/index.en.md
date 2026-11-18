# API Documentation

Automatic documentation of the `incolume.py.changelog` modules, generated with
mkdocstrings from the code docstrings.

## Modules

::: incolume.py.changelog

::: incolume.py.changelog.changelog

::: incolume.py.changelog.core

::: incolume.py.changelog.cli

## Quick start

Via Python API:

```python
from incolume.py.changelog.changelog import update_changelog

update_changelog(changelog_file='docs/about/CHANGELOG', reverse=True)
```

Via CLI:

```shell
uv run changelog docs/about/CHANGELOG --reverse
```

See the [Usage Guide](../user_guide/usage) and the
[Installation](../user_guide/INSTALLATION).

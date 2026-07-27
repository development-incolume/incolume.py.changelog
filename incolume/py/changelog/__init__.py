"""Module incolume.py.changelog."""

from incolume.py.changelog.core import (
    __title__,
    __version__,
    confproject,
    key_versions_2_sort,
    logger,
    toml,
    update_version,
    versionfile,
)

__all__ = [
    '__title__',
    '__version__',
    'confproject',
    'key_versions_2_sort',
    'logger',
    'toml',
    'update_version',
    'versionfile',
]

update_version(pyproject_fl=confproject)  # noqa: RUF067

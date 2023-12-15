"""Configurate tests."""
from pathlib import Path
from tempfile import NamedTemporaryFile

import pytest


@pytest.fixture(scope='session')
def semver_regex() -> str:
    """Fixture para regex de validação do Versionamento Semântico."""
    return r'^\d+(\.\d+){2}((-\w+\.\d+)|(\w+\d+))?$'


@pytest.fixture()
def changelog_stamps():
    """Return labels Keep a Changelog."""
    return 'Added Changed Deprecated Removed Fixed Security'.upper().strip()


@pytest.fixture()
def return_git_tag():
    """Return fake `git tag -n`."""
    return """1.0.0 Added: Fake record; other fake; Fixed: Fake fixed
    1.3.0 Fixed: Fake record; other fake; Changed: Fake fixed
    1.5.0 Added: Fake record; other fake; Fixed: Fake fixed
    2.2.0 Security: Fake record; other record; Fake fixed"""


@pytest.fixture()
def file_temp():
    """Generate aleatory filename into tempdir for tests."""
    return Path(NamedTemporaryFile(delete=False).name)

"""Configurate tests."""
# -*- coding: utf-8 -*-
from pathlib import Path
from tempfile import NamedTemporaryFile, gettempdir

import pytest


@pytest.fixture(scope="function")
def temp_file_name():
    """Generate aleatory filename into tempdir for tests."""
    return Path(NamedTemporaryFile().name)


@pytest.fixture(scope="function")
def changelog_stamps():
    """Return labels Keep a Changelog."""
    return "Added Changed Deprecated Removed Fixed Security".upper().strip()


@pytest.fixture(scope="function")
def return_git_tag():
    """Return fake `git tag -n`."""
    return """1.0.0 Added: Fake record; other fake; Fixed: Fake fixed
    1.3.0 Fixed: Fake record; other fake; Changed: Fake fixed
    1.5.0 Added: Fake record; other fake; Fixed: Fake fixed
    2.2.0 Security: Fake record; other record; Fake fixed"""


@pytest.fixture
def ftemp():
    """Return NamedTemporaryFile."""
    return NamedTemporaryFile(delete=False).name

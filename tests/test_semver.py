"""Testes para validação versionamento semântico."""

import re

import pytest

from incolumepy.utils import __version__

__author__ = "@britodfbr"  # pragma: no cover


@pytest.mark.parametrize(
    ["entrance", "expected"],
    (
        (__version__, True),
        ("0.0.1", True),
        ("0.1.0", True),
        ("1.0.0", True),
        ("1.0.1", True),
        ("1.1.1", True),
        ("1.1.1-rc0", True),
        ("1.1.1-rc.0", True),
        ("1.1.1-rc-0", True),
        ("1.0.1-dev0", True),
        ("1.0.1-dev.0", True),
        ("1.0.1-dev.1", True),
        ("1.0.1-dev.2", True),
        ("1.0.1-alpha.0", True),
        ("1.0.1-alpha.266", True),
        ("1.0.1-dev.0", True),
        ("1.0.1-beta.0", True),
        ("1.1.1-alpha.99999", True),
        ("1.1.1-rc.99999", True),
        ("1.1.99999", True),
        ("1.999999.1", True),
    ),
)
def test_version(entrance, expected):
    assert re.fullmatch(r"\d(\.\d){2}(-?\w+\.?\d+)?", __version__, flags=re.I)


if __name__ == "__main__":
    ...

"""Test module for cli."""
from __future__ import annotations

import os
from typing import Any, Dict, TYPE_CHECKING
import pytest
from incolume.py.changelog import cli

if TYPE_CHECKING:
    from click.testing import CliRunner
    from pathlib import Path


@pytest.mark.parametrize(
    'envvar entrance expected'.split(),
    [
        pytest.param('', {'args': 'Yoda'}, 'Oi Yoda!\n'),
        pytest.param('Yoda', {'args': ''}, 'Oi Yoda!\n'),
        pytest.param('Visitante', {'args': 'obiwan'}, 'Oi Obiwan!\n'),
        pytest.param('Yoda', {}, 'Oi Yoda!\n'),
    ],
)
def test_gretting(
    cli_runner: CliRunner,
    envvar: str,
    entrance: Any,
    expected: str,
) -> None:
    """Test cli gretting."""
    if envvar:
        os.environ['USERNAME'] = envvar
    result = cli_runner.invoke(cli.greeting, **entrance)
    assert result.exit_code == 0
    assert result.output == expected


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        ({}, True),
    ],
)
def test_changelog(
    cli_runner: CliRunner,
    *,
    file_temp: Path,
    entrance: Dict[str, Any],
    expected: bool,
) -> None:
    """Test cli changelog."""
    entrance.update({'args': [file_temp.as_posix()]})
    assert bool(cli_runner.invoke(cli.changelog, **entrance)) == expected

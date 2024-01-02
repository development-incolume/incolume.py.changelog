"""Test module for cli."""
import os
from pathlib import Path
from typing import Any, Dict
from unittest import mock

import pytest
from click.testing import CliRunner

from incolume.py.changelog import cli


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
        ({}, 'True'),
        # ({'url': 'http://example.org/xpto'}, True),
        # ({'url': 'http://example.org/xpto', 'reverse': False}, True),
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
    with mock.patch('time.strftime') as t, \
        mock.patch('subprocess.getoutput', autospec=True) as m:
        t.return_value = '2024-01-01T00:01:00.000000001-0300'
        m.return_value = '2024-01-01T00:01:00.000000001-0300'
        result = cli_runner.invoke(cli.changelog, **entrance)
        assert result.output.strip() == expected

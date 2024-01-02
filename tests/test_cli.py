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
        pytest.param({'args': ''}, True, marks=()),
        pytest.param({'args': ['-u', 'http://example.org/xpto']}, True, marks=()),
        pytest.param({'args': ['--url', 'http://example.org/xpto', 'reverse', 'false']}, True, marks=()),
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
    entrance.update({'args': [file_temp.as_posix(), *entrance.get('args')]})
    with mock.patch(
        f'incolume.py.changelog.changelog.changelog_messages', autospec=True) as m:
        m.return_value = [
            (
                '1.1.0',
                {
                    'key': '1.1.0',
                    'date': '2023-12-21',
                    'messages': {
                        'Added': ['g', 'u'],
                        'Removed': ['1', '2'],
                   },
                },
            ),
        ]
        result = cli_runner.invoke(cli.changelog, **entrance)
        assert bool(result.output.strip()) == expected

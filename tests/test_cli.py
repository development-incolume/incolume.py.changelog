"""Test module for cli."""

from __future__ import annotations
import os
from typing import Any, TYPE_CHECKING
from unittest import mock

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
        pytest.param([], True, marks=()),
        pytest.param(['-u', 'http://example.org/xpto'], True, marks=()),
        pytest.param(
            [
                '--url',
                'http://example.org/xpto',
                'reverse',
                'false',
            ],
            True,
            marks=(),
        ),
    ],
)
def test_changelog(
    cli_runner: CliRunner,
    *,
    file_temp: Path,
    entrance: list[str],
    expected: bool,
) -> None:
    """Test cli changelog."""
    params = [file_temp.as_posix(), *entrance]

    with mock.patch(
        'incolume.py.changelog.changelog.changelog_messages',
        autospec=True,
    ) as m:
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
        result = cli_runner.invoke(cli.changelog, params)
        assert bool(result.output.strip()) == expected

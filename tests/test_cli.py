from click.testing import CliRunner
from incolume.py.changelog import cli 
import pytest
import os


@pytest.fixture()
def cli_runner() -> CliRunner:
    """Fixture to CliRunner."""
    return CliRunner()


@pytest.mark.parametrize(
    'envvar entrance expected'.split(),
    [
        pytest.param('', {'args': 'Yoda'}, 'Oi Yoda!\n'),
        pytest.param('Yoda', {'args': ''}, 'Oi Yoda!\n'),
        pytest.param('Visitante', {'args': 'obiwan'}, 'Oi Obiwan!\n'),
    ]
)
def test_hello(cli_runner: CliRunner, envvar: str, entrance: dict, expected: str) -> None:
    """Test it."""
    if envvar:
        os.environ["USERNAME"] = envvar
    result = cli_runner.invoke(cli.greeting, **entrance)
    assert result.exit_code == 0
    assert result.output == expected
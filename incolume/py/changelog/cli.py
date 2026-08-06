"""CLI - Command Line Interface module."""

import click
from icecream import ic

from incolume.py.changelog.changelog import update_changelog
from incolume.py.changelog.core import load_config, select_configuration_fl

try:
    config: dict[str, str | bool] = load_config(select_configuration_fl())
except ValueError:  # pragma: no cover
    config = {}

ic(config)  # type: ignore [reportPrivateUsage]


@click.command()
@click.argument('nome', envvar='USERNAME', type=click.STRING)
def greeting(nome: str) -> None:
    """Retorna a saudação para o nome passado.

    Args:
      nome: Nome de usuário

    Return:
      Não há retorno. Uma saudação é exibida na tela.

    Raises:
      None

    Examples:
        >>> greeting Yoda
        Oi Yoda!

        >>> greeting
        Oi <usuário logado>

    """
    click.echo(f'Oi {nome.title()}!')


@click.command()
@click.argument(
    'file_changelog',
    type=click.STRING,
    default=config.pop('file', 'CHANGELOG.md'),
)
@click.option(
    '--url',
    '-u',
    default=config.pop(
        'url_compare',
        'https://github.com/development-incolume/incolume.py.changelog/-/compare',
    ),
    help='Url compare from repository of project.',
)
@click.option(
    '--reverse',
    '-r',
    default=config.pop('reverse', False),
    is_flag=True,
    help='Reverse order of records.',
)
def changelog(
    file_changelog: str,
    url: str = '',
    *,
    reverse: bool = True,
) -> None:
    """Operacionaliza uma interface CLI para módulo incolume.py.changelog.

    Args:
        file_changelog:  changelog full filename.
        url: url compare from repository of project.
        reverse: Reverse order of records.

    Return:
        True if success

    Raises:
        ValueError: When there is not git tag records.

    """
    result = update_changelog(
        changelog_file=file_changelog,
        urlcompare=url,
        reverse=reverse,
        **config,
    )
    click.echo(f'{result}')

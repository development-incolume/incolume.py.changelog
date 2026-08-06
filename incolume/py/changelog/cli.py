"""CLI - Command Line Interface module."""

import click
from icecream import ic

from incolume.py.changelog.changelog import (
    URL_COMPARE,
    generate_changelog_config_model,
    update_changelog,
)
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
        URL_COMPARE,
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
@click.option(
    '--generate-config',
    '-g',
    is_flag=True,
    help='Generate configure file for changelog.',
)
def changelog(
    file_changelog: str,
    url: str = '',
    *,
    reverse: bool = True,
    generate_config: bool = False,
) -> None:
    """Operacionaliza uma interface CLI para módulo incolume.py.changelog.

    Args:
        file_changelog:  changelog full filename.
        url: url compare from repository of project.
        reverse: Reverse order of records.
        generate_config: Generate configuration file for changelog.

    Return:
        True if success

    Raises:
        ValueError: When there is not git tag records.

    """
    if generate_config:
        click.secho('Generating configuration file for changelog...', fg='green')
        generate_changelog_config_model(**config)
        click.secho('Done!', fg='green')
        return

    result = update_changelog(
        changelog_file=file_changelog,
        urlcompare=url,
        reverse=reverse,
        **config,
    )
    click.secho(f'{result}', fg='green')

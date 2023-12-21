"""CLI - Command Line Interface module."""
from __future__ import annotations

from typing import TYPE_CHECKING

import click
from incolume.py.changelog.changelog import update_changelog

if TYPE_CHECKING:
    from pathlib import Path  # pragma: no cover


@click.command()
@click.argument('nome', envvar='USERNAME', type=click.STRING)
def greeting(nome: str) -> None:
    """Retorna a saudação para o nome passado.

    Args:
      nome: Nome de usuário

    Returns:
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
    default='CHANGELOG.md',
)
@click.option(
    '--url',
    '-u',
    default='https://github.com/development-incolume/'
            'incolume.py.changelog/-/compare',
    help='Url compare from repository of project.',
)
@click.option(
    '--reverse',
    '-r',
    default=True,
    help='Reverse order of records.',
)
def changelog(
    file_changelog: str | Path,
    url: str = '',
    *,
    reverse: bool = True,
) -> bool:
    """Operacionaliza uma interface CLI para módulo incolume.py.changelog.

    Args:
        file_changelog:  changelog full filename.
        url: url compare from repository of project.
        reverse: Reverse order of records.

    Returns:
        True if success

    Raises:
        ValueError: When there is not git tag records.

    """
    return update_changelog(
        changelog_file=file_changelog,
        urlcompare=url,
        reverse=reverse,
    )

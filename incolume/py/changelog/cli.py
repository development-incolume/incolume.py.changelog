"""Command Line Interface module."""

from pathlib import Path

import click

from incolume.py.changelog.changelog import update_changelog


@click.command()
@click.argument("nome", envvar="USERNAME", type=click.STRING)
def greeting(nome: str) -> None:
    """Retorna o cumprimento para o nome passado.

    :param nome: str
    :return: None

    Examples:

    >>> greeting Yoda
    Oi Yoda!

    >>> greeting
    Oi <usuário logado>

    """
    click.echo(f"Oi {nome.title()}!")


@click.command()
@click.argument("file_changelog", type=click.STRING, default="CHANGELOG.md")
@click.option(
    "--url",
    "-u",
    default="https://github.com/development-incolume/incolume.py.changelog/-/compare",
    help="Url compare from repository of project.",
)
@click.option(
    "--reverse", "-r", default=True, help="Reverse order of records."
)
def changelog(file_changelog: str | Path, url: str = "", reverse: bool = True):
    """Operacionaliza uma interface CLI para módulo incolume.py.changelog.

    :param changelog_file:  changelog full filename.
    :param url: url compare from repository of project.
    :param reverse: bool.
    :return: bool. True if success

    """
    return update_changelog(
        changelog_file=file_changelog,
        urlcompare=url,
        reverse=reverse,
    )

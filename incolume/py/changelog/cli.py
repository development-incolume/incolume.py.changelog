"""Command Line Interface module."""

from pathlib import Path

import click

from incolumepy.utils.changelog import update_changelog


@click.command()
@click.argument("nome", envvar="USER", type=click.STRING)
def greeting(nome):
    """Retorna o cumprimento para o nome passado.

    :param nome: str
    :return: None
    """
    click.echo(f"Oi {nome}!")


@click.command()
# @click.argument('stream', type=click.STRING)
@click.argument("file_changelog", type=click.STRING, default="CHANGELOG.md")
@click.option(
    "--url",
    "-u",
    default="https://gitlab.com/development-incolume/"
    "incolumepy.utils/-/compare",
    help="Url compare from repository of project.",
)
@click.option(
    "--reverse", "-r", default=True, help="Reverse order of records."
)
def changelog(file_changelog: str | Path, url: str = "", reverse: bool = True):
    """Operacionaliza uma interface CLI para módulo incolumepy.utils.changelog.

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

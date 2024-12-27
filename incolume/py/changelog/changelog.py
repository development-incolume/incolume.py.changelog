"""Changelog Module."""

from __future__ import annotations

import inspect
import logging
import re
import subprocess
import sys
from pathlib import Path
from typing import Any, Final

import git
from incolume.py.changelog import __title__, __version__, key_versions_2_sort

# ruff: noqa: S605 S607
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s;%(levelname)-8s;%(name)s;'
    '%(module)s;%(funcName)s;%(message)s',
)

CHANGELOG_FILE: Final[Path] = Path(__file__).parents[2] / 'CHANGELOG.md'


def get_os_command(key: str) -> str:
    """Generate command to git tag according OS.

    Args:
        key: Tag with semantic version.

    Return:
        A string with the command referring to the OS.

    Raises:
        None

    Examples:
        In Windows:
        >>> get_os_command('1.0.0')
        'git show -s --format=%cs 1.0.0^^{commit} --'

        In Linux:
        >>> get_os_command('1.0.0')
        'git show -s --format=%cs 1.0.0^{commit} --'
    """
    cmd_supply = {
        'win': r'^^{commit} --',
    }
    cmd = rf'git show -s --format=%cs {key}'
    os_id = sys.platform.casefold()[:3]
    cmd += cmd_supply.get(os_id, r'^{commit} --')

    logging.debug(cmd)
    return cmd


def msg_classify(msg: str, lang: str = '') -> dict[str, Any]:
    """Classify and sort one record for messages git tag -n.

    Args:
        lang: Language of command.
        msg: Message of command.
        **kwargs: Anyone of the positional items.

    Return:
        A dictionary with the version, date and a message.

    Raises:
        ValueError: If lang selected don't have support.

    Examples:
        >>> msg_classify('1.0.0 Adicionado: Nova funcionalidade.', 'pt-BR')
        {'key': '0.1.0', 'date': '2023-12-18',
        'messages': {'Added': ['Nova funcionalidade.']}

        >>> msg_classify('Corregido: corrección de error.', 'es-AR')
        ValueError: es-AR not suported! Use en-US, pt-BR
    """
    logging.debug(lang)
    suport_lang: dict[str, Any] = {
        'en-US': {
            'Added': 'Added',
            'Changed': 'Changed',
            'Deprecated': 'Deprecated',
            'Removed': 'Removed',
            'Fixed': 'Fixed',
            'Security': 'Security',
        },
        'pt-BR': {
            'Adicionado': 'Added',
            'Modificado': 'Changed',
            'Obsoleto': 'Deprecated',
            'Removido': 'Removed',
            'Corrigido': 'Fixed',
            'Segurança': 'Security',
        },
    }
    suport_lang.update(
        {'all': {k: v for d in suport_lang.values() for k, v in d.items()}},
    )
    if lang not in suport_lang:
        logging.error(
            ValueError(f'{lang} not suported! Use {suport_lang.keys()}'),
        )

    key, msg = msg.split(maxsplit=1)
    cmd = get_os_command(key)
    date = subprocess.getoutput(cmd).strip()
    logging.debug(date)

    logging.debug('key=%s; date=%s; msg=%s', key, date, msg)
    selected_lang = suport_lang.get(lang, suport_lang['all'])
    regex: str = rf"({'|'.join(selected_lang.keys())})\s?:"

    txt = re.sub(
        regex,
        r'§§\1§:',
        msg,
        flags=re.IGNORECASE,
    )
    logging.debug('txt=%s', txt)
    dct: dict[str, Any] = {}
    for i, j in sorted(
        x.strip().rstrip(';').split('§:') for x in txt.strip().split('§§') if x
    ):
        dct.setdefault(selected_lang[i.capitalize()], []).extend(
            j.strip().split(';'),
        )

    return {'key': key, 'date': date, 'messages': dct}


def changelog_messages(
    *,
    text: str,
    start: str | int | None = None,
    end: str | int | None = None,
    **kwargs: str,
) -> list[tuple[str, dict[str, Any]]]:
    """Changelog messages sort and classify.

    Args:
        end: End of Message
        start: Start of Message
        text: Changelog's message
        **kwargs: Anyone of the positional items.

    Return:
        return a list of tuples with a changelog menssage per line.

    Raises:
        None

    Examples:
        >>> changelog_messages('1.0.0 Security: a;b;c;'
        'Removed: 1;2;3; Changed: a;b;c;d;e;'
        'Fixed: http://example.com; http://httpbin.com;'
        'Deprecated: 1;2;3;a;s;b; Added: a1;a2;a3.',
        '1.1.0 Removed: 1;2'
        'Added: g;u')
        [('1.0.0',{'key': '1.0.0', 'date': '2023-12-21',
        'messages': {
        'Added': ['a1', 'a2', 'a3.'],
        'Changed': ['a', 'b', 'c', 'd', 'e'],
        'Deprecated': ['1', '2', '3', 'a', 's', 'b'],
        'Fixed': ['http://example.com', 'http://httpbin.com',],
        'Removed': ['1', '2', '3'],
        'Security': ['a', 'b', 'c'],},},),
        ('1.1.0',{'key': '1.1.0', 'date': '2023-12-21',
        'messages': {
        'Added': ['g', 'u'],
        'Removed: ['1', '2'],},},)]
    """
    logging.debug('parameters: (%s %s %s %s)', text, start, end, kwargs)
    lang: str = kwargs.get('lang', '')
    if start is not None:
        start = int(start)
    if end is not None:
        end = int(end)

    records = []
    for msg in text.strip().splitlines()[start:end]:
        logging.debug('msg=%s', msg)
        record = msg_classify(msg=msg, lang=lang)
        logging.debug('record=%s', record)
        records.append((record['key'], record))
    logging.debug('type return %s=%s', inspect.stack()[0][3], type(records))
    logging.debug('return %s=%s', inspect.stack()[0][3], records)
    return records


def changelog_header(
    **kwargs: str,
) -> list[str]:
    r"""Header of changelog file.

    Args:
        url_keepachangelog (str): url for keep changelog.
        url_semver (str): url for semantic version.
        url_convetional_commit (str): url for convetional commit.
        url_project (str): url principal for project.
        kwargs: Anyone of the others items.

    Return:
        Return a list with a header of changelog file.

    Raises:
        None

    Examples:
        >>> changelog_header()
        ['# CHANGELOG\n\n\n',
        'All notable changes to this project',
        ' will be documented in this file.\n\n',
        'The format is based on ',
        '[Keep a Changelog](https://keepachangelog.com/en/1.0.0/), ',
        'this project adheres to'
        '[Semantic Versioning](https://semver.org/spec/v2.0.0.html) '
        'and [Conventional Commit]'
        '(https://www.conventionalcommits.org/pt-br/v1.0.0/).\n\n',
        'This file was automatically generated for',
        ' [incolume.py.changelog](https://gitlab.com/development-incolume/'
        'incolumepy.utils/-/tree/0.2.0a2)',
        '\n\n---\n']

        >>> changelog_header(
            url_keepachangelog='https://keepachangelog.com/en/2.0.0/',
            url_semver=https://semver.org/spec/v1.0.0.html)
        ["# CHANGELOG\n\n\n",
        "All notable changes to this project",
        " will be documented in this file.\n\n",
        "The format is based on ",
        "[Keep a Changelog](https://keepachangelog.com/en/2.0.0/),",
        "this project adheres to "
        "[Semantic Versioning](https://semver.org/spec/v1.0.0.html)"
        "and [Conventional Commit]"
        "(https://www.conventionalcommits.org/pt-br/v1.0.0/).\n\n",
        "This file was automatically generated for",
        "[incolume.py.changelog](https://github.com/development-"
        "incolume/incolume.py.changelog/-/tree/0.2.0a0)",
        "\n\n---\n"]
    """
    url_keepachangelog = kwargs.get(
        'url_keepachangelog',
        'https://keepachangelog.com/en/1.0.0/',
    )
    url_semver = kwargs.get(
        'url_semver',
        'https://semver.org/spec/v2.0.0.html',
    )
    url_convetional_commit = kwargs.get(
        'url_convetional_commit',
        'https://www.conventionalcommits.org/pt-br/v1.0.0/',
    )
    url_project = kwargs.get(
        'url_project',
        'https://github.com/development-incolume/incolume.py.changelog',
    )
    return [
        '# CHANGELOG\n\n\n',
        'All notable changes to this project',
        ' will be documented in this file.\n\n',
        'The format is based on ',
        f'[Keep a Changelog]({url_keepachangelog}), ',
        'this project adheres to '
        f'[Semantic Versioning]({url_semver}) '
        f'and [Conventional Commit]({url_convetional_commit}).\n\n',
        'This file was automatically generated for',
        f' [{__title__}]({url_project}/-/tree/{__version__})',
        '\n\n---\n',
    ]


def changelog_body(
    content: list[tuple[str, dict[str, Any]]],
    content_formated: list[str],
    **kwargs: str,
) -> list[str]:
    """Body of changelog file.

    Args:
        content: Content of changelog.
        content_formated: Content formated of changelog.
        **kwargs: Anyone of the positional items.

    Return:
        Return a list with a content of changelog's body.

    Raises:
        None

    Examples:
        >>> changelog_body([('1.0.1', {Added: 'New function'})],
        ['1.0.1', 'Added', 'New Function'])
        ['[1.0.1]', 'Added', 'New Function']
    """
    logging.debug(kwargs)
    content_formated.extend(Changelog.iter_logs(content[:-1]))
    content_formated.extend(Changelog.iter_logs(content[-1:], linked=False))
    return content_formated


def changelog_footer(
    content: list[tuple[str, dict[str, Any]]],
    content_formated: list[str],
    **kwargs: str,
) -> list[str]:
    r"""Footer of changelog file.

    Args:
        content: Content of changelog's footer
        content_formated: Content formated of changelog's footer
        urlcompare: Url to compare.
        **kwargs: Anyone of the positional items.

    Return:
        Return a list with a footer of changelog file.

    Raises:
        None

    Examples:
        >>> changelog_footer([('1.0.1',{Added: 'New function'})],
        ['1.0.1', 'Added', 'New Function'])
        ['1.0.1', 'Added', 'New Function',
        '\n---\n\n',
        '[1.0.1]: https://github.com/development-incolume/'
        'incolume.py.changelog/-/compare/1.0.0...1.0.1']
    """
    urlcompare = (
        kwargs.get('urlcompare')
        or 'https://github.com/development-incolume/'
        'incolume.py.changelog/-/compare'
    )
    logging.debug('urlcompare=%s', urlcompare)
    content_formated.append('\n\n---\n\n')
    y: dict[str, Any] = {}
    for _, x in content[::-1]:
        if y:
            content_formated.append(
                f'[{x["key"]}]: {urlcompare}/{y["key"]}...{x["key"]}\n',
            )
        y = x
    return content_formated


def changelog_write(
    *,
    content: list[tuple[str, dict[str, Any]]],
    **kwargs: str,
) -> bool:
    """Write CHANGELOG.md file formatted.

    Args:
        changelog_file: Path of changelog file.
        content: Content to write the changelog
        **kwargs: Anyone of the positional items.

    Return:
        True if success.

    Raises:
        None

    Examples:
        >>> changelog_write(['Added: funcionalidade nova.'])
        True
    """
    changelog_file = Path(kwargs.get('changelog_file') or CHANGELOG_FILE)
    logging.debug('changelog_file=%s', changelog_file)

    content_formated = changelog_header()
    content_formated = changelog_body(content, content_formated, **kwargs)
    content_formated = changelog_footer(content, content_formated, **kwargs)

    with changelog_file.open('w') as f:
        f.writelines(content_formated)
        return True


def update_changelog(
    changelog_file: str = '',
    *,
    reverse: bool = True,
    **kwargs: str,
) -> bool:
    """Update Changelog.md file.

    Args:
        changelog_file: changelog full filename.
        reverse: reverse to the last update be the first.
        urlcompare(str): Url to compare.
        **kwargs: Anyone of the positional items.

    Return:
        True if success

    Raises:
        None

    Examples:
        >>> update_changelog()
        True
        >>> update_changelog(changelog_file='/tmp/CHANGELOG.md')
        True
        >>> update_changelog(changelog_file=Path('CHANGELOG.md'),
        urlcompare="https://github.com/development-incolume/"
        "incolume.py.changelog/-/compare")
        True
    """
    logging.debug('argumentos=%s,%s,%s', changelog_file, reverse, kwargs)
    urlcompare: str = (
        kwargs.get('urlcompare')
        or 'https://github.com/development-incolume'
        '/incolume.py.changelog/-/compare'
    )
    content: str = kwargs.get('content', subprocess.getoutput('git tag -n'))
    logging.info('registros encontrados ..')
    logging.debug('content=%s', content)

    return changelog_write(
        content=sorted(
            changelog_messages(
                text=content,
                start=kwargs.get('start'),
                end=kwargs.get('end'),
            ),
            reverse=reverse,
            key=key_versions_2_sort,
        ),
        urlcompare=urlcompare,
        changelog_file=changelog_file,
    )


class Changelog:
    """Changelog class."""

    def __init__(
        self: Changelog,
        file_output: Path | str = '',
        url_compare: str = '',
        *,
        reverse: bool = True,
        **kwargs: str,
    ):
        """Initialize from Changelog class.

        Args:
            file_output: The output file of changelog.
            reverse: reverse to the last update be the first.
            url_compare: Url to compare.
            url_convetional_commit(str): Url of convetional commit.
            url_keepachangelog(str): Url of keep a changelog.
            url_principal(str): Url principal do projeto.
            url_semver(str): Url of semantic version.
            **kwargs: Anyone of the positional items.

        Return:
            None
        """
        self.file_output = (
            file_output or kwargs.get('file_output') or Path('CHANGELOG.md')
        )
        self.url_compare = url_compare or kwargs.get('url_compare')
        self.reverse = reverse
        self.url_principal = kwargs.get(
            'url_pricipal',
            'https://gitlab.com/development-incolume/incolume.py.changelog',
        )
        self.url_keepachangelog = kwargs.get(
            'url_keepachangelog',
            'https://keepachangelog.com/en/1.0.0/',
        )
        self.url_semver = kwargs.get(
            'url_semver',
            'https://semver.org/spec/v2.0.0.html',
        )
        self.url_convetional_commit = kwargs.get(
            'url_convetional_commit',
            'https://www.conventionalcommits.org/pt-br/v1.0.0/',
        )

    @staticmethod
    def iter_logs(
        content: list[tuple[str, dict[str, Any]]],
        *,
        linked: bool = True,
    ) -> list[str]:
        r"""Iterador de registros git.

        Args:
            content: Content register in git.
            linked: If has link.

        Return:
            A list with the version, date and a message.

        Raises:
            None

        Examples:
            >>> iter_logs(
            [('1.0.0a5', {'date': '2023-12-21', 'key': '1.0.0a5',
            'messages': {'Added': ['New function', 'One more new function.'],
            'Fixed': ['A bug of connection.'],},},),], False)
            ['\n\n## 1.0.0a5\t &#8212; \t2023-12-21:',
            '\n### Added',
            '\n  - New function;',
            '\n  - One more new function;',
            '\n### Fixed',
            '\n  - A bug of connection.",;',],
        """
        result = []
        for _, entrada in content:
            logging.debug(entrada)
            if linked:
                result.append(
                    f"\n\n## [{entrada['key']}]\t &#8212; "
                    f"\t{entrada['date']}:",
                )
            else:
                result.append(
                    f"\n\n## {entrada['key']}\t &#8212; \t{entrada['date']}:",
                )

            for label, msgs in entrada['messages'].items():
                result.append(f'\n### {label.capitalize()}')
                for msg in msgs:
                    frase = msg.strip()
                    frase = frase[0].upper() + frase[1:]
                    result.append(f'\n  - {frase};')
        return result

    def _header(self: Changelog) -> list[str]:
        r"""Header of changelog file.

        Return:
            Return a list with a header of changelog file.

        Raises:
            None

        Examples:
            >>> changelog_header()
            ['# CHANGELOG\n\n\n',
            'All notable changes to this project',
            ' will be documented in this file.\n\n',
            'The format is based on ',
            '[Keep a Changelog](https://keepachangelog.com/en/1.0.0/), ',
            'this project adheres to'
            '[Semantic Versioning](https://semver.org/spec/v2.0.0.html) '
            'and [Conventional Commit]'
            '(https://www.conventionalcommits.org/pt-br/v1.0.0/).\n\n',
            'This file was automatically generated for',
            ' [incolume.py.changelog](https://github.com/development-incolume/'
            'incolume.py.changelog/-/tree/0.2.0a2)',
            '\n\n---\n']

            >>> changelog_header(
            url_keepachangelog='https://keepachangelog.com/en/2.0.0/',
            url_semver=https://semver.org/spec/v1.0.0.html)
            ["# CHANGELOG\n\n\n",
            "All notable changes to this project",
            " will be documented in this file.\n\n",
            "The format is based on ",
            "[Keep a Changelog](https://keepachangelog.com/en/2.0.0/),",
            "this project adheres to "
            "[Semantic Versioning](https://semver.org/spec/v1.0.0.html)"
            "and [Conventional Commit]"
            "(https://www.conventionalcommits.org/pt-br/v1.0.0/).\n\n",
            "This file was automatically generated for",
            "[incolume.py.changelog](https://github.com/development-incolume/'
            'incolume.py.changelog/-/tree/0.2.0a0)",
            "\n\n---\n"]
        """
        return [
            '# CHANGELOG\n\n\n',
            'All notable changes to this project',
            ' will be documented in this file.\n\n',
            'The format is based on ',
            f'[Keep a Changelog]({self.url_keepachangelog}), ',
            'this project adheres to '
            f'[Semantic Versioning]({self.url_semver}) '
            f'and [Conventional Commit]({self.url_convetional_commit}).\n\n',
            'This file was automatically generated for',
            f' [{__title__}]({self.url_principal}/-/tree/{__version__})',
            '\n\n---\n',
        ]

    def _footer(
        self: Changelog,
        content: list[tuple[str, dict[str, Any]]],
        content_formated: list[str],
        **kwargs: str,
    ) -> list[str]:
        r"""Footer of changelog file.

        Args:
            content: Content of changelog's footer
            content_formated: Content formated of changelog's footer
            urlcompare: Url to compare.
            **kwargs: Anyone of the positional items.

        Return:
            Return a list with a footer of changelog file.

        Raises:
            None

        Examples:
            >>> changelog_footer([('1.0.1',{Added: 'New function'})],
            ['1.0.1', 'Added', 'New Function'])
            ['1.0.1', 'Added', 'New Function',
            '\n---\n\n',
            '[1.0.1]: https://github.com/development-incolume/'
            'incolume.py.changelog/-/compare/1.0.0...1.0.1']
        """
        urlcompare = (
            kwargs.get('urlcompare')
            or 'https://github.com/development-incolume/'
            'incolume.py.changelog/-/compare'
        )
        logging.debug('urlcompare=%s', urlcompare)
        content_formated.append('\n\n---\n\n')
        y: dict[str, Any] = {}
        for _, x in content[::-1]:
            if y:
                content_formated.append(
                    f'[{x["key"]}]: {urlcompare}/{y["key"]}...{x["key"]}\n',
                )
            y = x
        return content_formated

    def __call__(self: Changelog, *args: Any, **kwds: Any) -> Changelog:
        """Call class."""
        logging.debug('args: %s; kwargs: %s', args, kwds)
        repo = git.Repo()  # noqa: F841
        return self


def run() -> None:
    """Examples ran.

    Return:
        None
    """
    msg = subprocess.getoutput('git tag -n').splitlines()[-14]
    logging.debug(msg)
    logging.debug('msg_classify=%s', msg_classify(msg=msg))

    msg = subprocess.getoutput('git tag -n')
    result = changelog_messages(text=msg)

    logging.debug('result=%s', result)
    logging.debug('type(result)=%s', type(result))
    result = sorted(result, reverse=True, key=key_versions_2_sort)
    logging.debug('result = %s; result type = %s', result, type(result))

    changelog_write(content=result)
    update_changelog()
    logging.info(
        msg_classify(
            '0.1.0           added: Projeto emancipado de '
            'https://gitlab.com/development-incolume/incolumepy.utils',
        ),
    )


if __name__ == '__main__':  # pragma: no cover
    run()

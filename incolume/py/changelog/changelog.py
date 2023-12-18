"""Changelog Module."""
from __future__ import annotations

import inspect
import logging
import re
import subprocess
from pathlib import Path
from typing import Any

from incolume.py.changelog import __title__, __version__, key_versions_2_sort

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s;%(levelname)-8s;%(name)s;'
           '%(module)s;%(funcName)s;%(message)s',
)

CHANGELOG_FILE = Path(__file__).parents[2] / 'CHANGELOG.md'


def msg_classify(msg: str, lang: str = '') -> dict[str, Any]:
    """Classify and sort one record for messages git tag -n.

    Args:
        lang: Language of command.
        msg: Message of command.

    Returns:
        dict: 

    Raises:
        ValueError: If lang selected don't have support.
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
    # cmd = re.escape("git show -s --format=%%cs '%s^{commit}'" % key)
    # print(cmd)
    # logging.debug(cmd)
    # date = subprocess.getoutput(cmd)
    ref = key + r"^^{commit}"
    cmd = ['git', 'show', '-s', '--format=%cs', ref]
    print(cmd)
    logging.debug(cmd)
    result = subprocess.run(
        cmd,
        shell=True, 
        capture_output=True, 
        text=True,
    )
    logging.error(result.stderr)
    date = result.stdout.strip()
    logging.debug(date)

    logging.debug('key=%s; date=%s; msg=%s', key, date, msg)
    selected_lang = suport_lang.get(lang, suport_lang['all'])
    regex: str = rf"({'|'.join(selected_lang.keys())})\s?:"
    
    txt = re.sub(
      regex,
      r'§§\1§:',
      msg,
      flags=re.I,
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
    start: int | None = None,
    end: int | None = None,
    **kwargs: str,
) -> list[tuple[str, dict[str, Any]]]:
    """Changelog messages sort and classify.

    Args:
        text: str
        start: (int, str, None)
        end: (int, str, None)

    Returns:
        list: return a list with a changelog menssage.

    Raises:
        None
    """
    logging.debug('parameters: (%s %s %s %s)', text, start, end, kwargs)
    lang = kwargs.get('lang', '')

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
    url_keepachangelog: str = "",
    url_semver: str = "",
    url_convetional_commit: str = "",
) -> list[str]:
    r"""
    Header of changelog file.

    Args:
        url_keepachangelog: str
        url_semver: str
        url_convetional_commit: str

    Returns:
        list: Return a list with a header of changelog file.

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
            url_semver=https://semver.org/spec/v1.0.0.html,
            )
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
        "[incolume.py.changelog](https://gitlab.com/development-incolume/"
        "incolumepy.utils/-/tree/0.2.0a0)",
        "\n\n---\n"]
    """
    url_keepachangelog = (
        url_keepachangelog or 'https://keepachangelog.com/en/1.0.0/'
    )
    url_semver = url_semver or 'https://semver.org/spec/v2.0.0.html'
    url_convetional_commit = (
        url_convetional_commit
        or 'https://www.conventionalcommits.org/pt-br/v1.0.0/'
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
        f' [{__title__}](https://gitlab.com/development-incolume/'
        f'incolumepy.utils/-/tree/{__version__})',
        '\n\n---\n',
    ]


def changelog_body(
    content: list[tuple[str, dict[str, Any]]],
    content_formated: list[str],
    **kwargs: str,
) -> list[str]:
    """
    Body of changelog file.

    Args:
        content: List[Tuple[str, Dict[str, Any]]]
        content_formated: list

    Returns:
        list: Return a list with a content of changelog's body.

    Raises:
        None
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
    """
    Footer of changelog file.

    Args:
        content: List[Tuple[str, Dict[str, Any]]]
        content_formated: list
        urlcompare: str

    Returns:
        list: Return a list with a footer of changelog file.

    Raises:
        None
    """
    urlcompare = (
        kwargs.get('urlcompare')
        or 'https://gitlab.com/development-incolume/incolumepy.utils/-/compare'
    )
    logging.debug('urlcompare=%s', urlcompare)
    content_formated.append('\n---\n\n')
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
        content: List[Tuple[str, Dict[str, Any]]]
        changelog_file: str, pathlib

    Returns:
        bool: True if success.
        
    Raises:
        None
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
        urlcompare: str
        reverse: bool
        changelog_file:  changelog full filename.
        
    Returns:
        bool: True if success

    Raises:
        None

    Examples:

        >>> update_changelog()
        True
        >>> update_changelog(changelog_file='/tmp/CHANGELOG.md')
        True
        >>> update_changelog(changelog_file=Path('CHANGELOG.md'),
        urlcompare="https://gitlab.com/development-incolume
        /incolumepy.utils/-/compare")
        True
    """
    logging.debug('argumentos=%s,%s,%s', changelog_file, reverse, kwargs)
    urlcompare: str = (
        kwargs.get('urlcompare')
        or 'https://gitlab.com/development-incolume/incolumepy.utils/-/compare'
    )
    content: str = kwargs.get('content', subprocess.getoutput('git tag -n'))
    logging.info('registros encontrados ..')
    logging.debug('content=%s', content)

    return changelog_write(
        content=sorted(
            changelog_messages(
                text=content,
                start=kwargs.get('start', None),
                end=kwargs.get('end', None),
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
        """
        Initialize from Changelog class.
        
        Args:
            file_output: str, Path
            url_compare: str
            reverse: bool
            url_principal: str
            url_keepachangelog: str
            url_semver: str
            url_convetional_commit: str
        """
        self.file_output = file_output or Path("CHANGELOG.md")
        self.url_compare = url_compare
        self.reverse = reverse
        self.url_principal = kwargs.get(
            'url_pricipal',
            'https://gitlab.com/development-incolume/incolume.py.changelog',
        )
        self.url_keepachangelog = kwargs.get(
            'url_keepachangelog', 'https://keepachangelog.com/en/1.0.0/',
        )
        self.url_semver = kwargs.get(
            'url_semver', 'https://semver.org/spec/v2.0.0.html',
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
        """
        Iterador de registros git.

        Args:
            content: List[Tuple[str, Dict[str, Any]]]
            linked: bool

        Return:
            list

        Raises:
            None
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


    def header(self) -> list[str]:
        """
        Header of changelog file.

        Returns:
            Return a list with a header of changelog file.

        Raises:
            None
        """
        return [
            "# CHANGELOG\n\n\n",
            "All notable changes to this project",
            " will be documented in this file.\n\n",
            "The format is based on ",
            f"[Keep a Changelog]({self.url_keepachangelog}), ",
            "this project adheres to "
            f"[Semantic Versioning]({self.url_semver}) "
            f"and [Conventional Commit]({self.url_convetional_commit}).\n\n",
            "This file was automatically generated for",
            f" [{__title__}]({self.url_principal}/-/tree/{__version__})",
            "\n\n---\n",
            ]


def run() -> None:
    """Examples ran.

    Returns:
        None
    """
    # msg = subprocess.getoutput('git tag -n').splitlines()[-14]
    # logging.debug(msg)
    # logging.debug('msg_classify=%s', msg_classify(msg=msg))

    # msg = subprocess.getoutput('git tag -n')
    # result = changelog_messages(text=msg)

    # logging.debug('result=%s', result)
    # logging.debug('type(result)=%s', type(result))
    # result = sorted(result, reverse=True, key=key_versions_2_sort)
    # logging.debug('result = %s; result type = %s', result, type(result))

    # changelog_write(content=result)
    # update_changelog()
    print(msg_classify('0.1.0           added: Projeto emancipado de https://gitlab.com/development-incolume/incolumepy.utils'))


if __name__ == '__main__':  # pragma: no cover
    run()

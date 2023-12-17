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

    :param lang:
    :param msg: str
    :return: dict

    Raises:
        ValueError: Invalid format string
    """
    logging.debug(lang)
    suport_lang: dict[Any, Any] = {
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
    cmd = 'git show -s --format=%%cs %s^{commit}' % key
    logging.debug(cmd)
    date = subprocess.getoutput(cmd)
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
    *, text: str, start: Any = None, end: Any = None, **kwargs,
) -> list[tuple[str, dict[str, Any]]]:
    """Changelog messages sort and classify.

    :param text: str
    :param start: (int, str, None)
    :param end: (int, str, None)
    :return: list
    """
    logging.debug('parameters: (%s %s %s %s)', text, start, end, kwargs)
    lang = kwargs.get('lang', '')

    records = []
    for msg in text.strip().splitlines()[start:end]:
        logging.debug('msg=%s', msg)
        record = msg_classify(msg=msg, lang=lang)
        logging.debug('record=%s', record)
        # records.setdefault(record['key']).update(**record)
        records.append((record['key'], record))
    logging.debug('type return %s=%s', inspect.stack()[0][3], type(records))
    logging.debug('return %s=%s', inspect.stack()[0][3], records)
    return records


def changelog_header(
    url_keepachangelog: str = '',
    url_semver: str = '',
    url_convetional_commit: str = '',
) -> list[str]:
    """Header of changelog file."""
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
    **kwargs,
) -> list[str]:
    """Body of changelog file."""
    content_formated.extend(Changelog.iter_logs(content[:-1]))
    content_formated.extend(Changelog.iter_logs(content[-1:], linked=False))
    return content_formated


def changelog_footer(
    content: list[tuple[str, dict[str, Any]]],
    content_formated: list[str],
    **kwargs,
) -> list[str]:
    """Footer of changelog file."""
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
    *, content: list[tuple[str, dict[str, Any]]], **kwargs,
) -> bool:
    """Write CHANGELOG.md file formatted.

    :param content: List[Tuple[str, Dict[str, Any]]]
    :param changelog_file: str, pathlib
    :param urlcompare: str
    :return: bool. True if success.
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
    *,
    changelog_file: Any = None,
    reverse: bool = True,
    **kwargs,
) -> bool:
    """Update Changelog.md file.

    :param urlcompare: url compare from repository of project.
    :param reverse: bool.
    :param changelog_file:  changelog full filename.
    :return: bool. True if success

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
        **kwargs,
    ):
        """Initialize from Changelog class.

        :param: file_output: Path

        """
        self.file_output = file_output or Path('CHANGELOG.md')
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
        content: list[tuple[str, dict[str, Any]]], *, linked: bool = True,
    ) -> list[str]:
        """Iterador de registros git."""
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

    def header(self: Changelog) -> list[str]:
        """Header of changelog file."""
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


def run():
    """Examples ran.

    :return: None
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


if __name__ == '__main__':  # pragma: no cover
    run()

"""Principal module."""

from __future__ import annotations

import logging
import re
from collections.abc import Container
from pathlib import Path
from typing import Union

import toml

confproject = Path(__file__).parents[3] / 'pyproject.toml'
versionfile = Path(__file__).parent / 'version.txt'
versionfile.write_text(
    toml.load(confproject)['tool']['poetry']['version'] + '\n',
)

__version__ = versionfile.read_text().strip()
__title__ = 'incolume.py.changelog'


def key_versions_2_sort(
    x: Union[list[str], tuple[str]],
    qdig: int = 0,
    regex: str = '',
) -> str:
    """Sort by SemVer notation.

    Args:
        regex: regex to version format.
        qdig: Quantity digits to sort.
        x: x[key, value] -> 'git tag -ln' output.

    Return:
        Return a list sorted.

    Raises:
        TypeError: if parameter x not be a tuple or list.

    Examples:
        >>> key_version_2_sort(('1.1.1rc0', 'aaa'))
        '00010501.080000'
    """
    qdig = qdig or 5
    if not isinstance(x, Container):
        msg = f"'x={x}', must be tuple or list."  # type: ignore [unreachable]
        raise TypeError(msg)

    classifies = {
        'post': 9 * 10**qdig,
        'rc': 8 * 10 ** (qdig - 1),
        'alpha': 2 * 10 ** (qdig - 1),
        'a': 2 * 10 ** (qdig - 1),
        'dev': 0,
    }
    regex = regex or r'(\d+)\.(\d+)\.(\d+)((-?\D+)(\d+))?'
    get_major_minor_patch_build = re.compile(regex)
    logging.debug(get_major_minor_patch_build)
    try:
        # pegar major, minor e patch
        values = get_major_minor_patch_build.search(x[0])
        major = values.group(1)  # type: ignore [union-attr]
        minor = values.group(2)  # type: ignore [union-attr]
        patch = values.group(3)  # type: ignore [union-attr]
        build = values.group(6)  # type: ignore [union-attr]
        # pegar build, se não tiver colocar uma alta 99999
        build = build or '9' * qdig
        logging.debug(
            'values.group(5): %s',
            values.group(5),  # type: ignore [union-attr]
        )
        plus = classifies.get(
            re.sub(
                r'[-.]',
                '',
                str(values.group(5)).lower(),  # type: ignore [union-attr]
            ),
            0,
        )
        logging.debug('plus: %s', plus)
        build = int(build) + plus
        result = f'{major:0>4}{minor:0>4}{patch:0>4}.{build:0>6}'
    except AttributeError:
        result = str(x[0])
    return result


def logger(str_format='', datefmt='', level=0, filelog=None):
    """Logger function for log.

    Args:
        str_format: format of string to log
        datefmt: format date to log
        level: can be (logging.DEBUG, logging.INFO, logging.WARNING,
       logging.ERROR, logging.CRITICAL)
        filelog: log's file .py

    Return:
        None

    """
    str_format = (
        str_format
        or '%(asctime)s;%(levelname)-8s;%(name)s;'
        '%(module)s;%(funcName)s;%(message)s'
    )
    datefmt = datefmt or '%Y/%m/%d %H:%M:%S %z'
    # create logger
    level = level or logging.DEBUG
    filelog = filelog or Path(__file__).with_suffix('.py')

    logging.basicConfig(
        filename=filelog,
        level=level,
        format=str_format,
        datefmt=datefmt,
    )

    console = logging.StreamHandler()
    formatter = logging.Formatter(str_format)
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)

    return logging.getLogger()

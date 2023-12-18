"""Principal module."""
import logging
import re
from collections.abc import Collection
from pathlib import Path
from typing import Any

import toml

confproject = Path(__file__).parents[3] / 'pyproject.toml'
versionfile = Path(__file__).parent / 'version.txt'
versionfile.write_text(
    toml.load(confproject)['tool']['poetry']['version'] + '\n',
)

__version__ = versionfile.read_text().strip()
__title__ = 'incolume.py.changelog'


def key_versions_2_sort(
    x: Collection[str], qdig: int = 0, regex: str = '',
) -> str:
    """Sort by SemVer notation.

    :param regex: regex to version format.
    :param qdig: Quantity digits to sort.
    :param x: x[key, value] -> 'git tag -ln' output
    :return: list sorted
    """
    qdig = qdig or 5
    if not isinstance(x, tuple | list):
        msg = "'x' must be tuple or list."
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
        major = values.group(1)
        minor = values.group(2)
        patch = values.group(3)
        build = values.group(6)
        # pegar build, se não tiver colocar uma alta 99999
        build = build or '9' * qdig
        logging.debug('values.group(5): %s', values.group(5))
        plus = classifies.get(
            re.sub(r'[-.]', '', str(values.group(5)).lower()),
            0,
        )
        logging.debug('plus: %s', plus)
        build = int(build) + plus
        result = f'{major:0>4}{minor:0>2}{patch:0>2}.{build:0>6}'
    except AttributeError:
        result = str(x[0])
    return result


def logger(str_format='', datefmt='', level=0, filelog=None):
    """Logger function for log.

    :str_format:
    :datefmt:
    :level: can be (logging.DEBUG, logging.INFO, logging.WARNING,
       logging.ERROR, logging.CRITICAL)
    :filelog:
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
        filename=filelog, level=level, format=str_format, datefmt=datefmt,
    )

    console = logging.StreamHandler()
    formatter = logging.Formatter(str_format)
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)

    return logging.getLogger()


def namespace(package_name: str) -> list[str]:
    """Return the namespace.

    Example:
    package_name='incolumepy.package.module'
    ['incolumepy','incolumepy.package'].

    :param package_name: str
    :return: list

    >>> namespace('incolumepy.package.subpackage.module')
    ['incolumepy', 'incolumepy.package', 'incolumepy.package.subpackage']

    >>> namespace('incolumepy.package.module')
    ['incolumepy', 'incolumepy.package']

    >>> namespace('incolumepy.package')
    ['incolumepy']

    >>> namespace('incolumepy')
    ['incolumepy']
    """
    logging.debug('package_name=%s', package_name)
    result: list[Any] = []
    temp = ''
    try:
        bits = package_name.split('.')
    except AttributeError:
        return result

    if len(bits) <= 1:
        logging.debug('bits=%s', bits)
        return bits

    for bit in bits[:-1]:
        temp = f'{temp}.{bit}' if temp else bit
        logging.debug('temp=%s', temp)
        result.append(temp)
    logging.debug('result=%s', result)
    return result

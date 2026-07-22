"""Principal module."""

from __future__ import annotations

import contextlib
import logging
import re
from collections.abc import Container
from pathlib import Path
from typing import NoReturn

import tomlkit as toml
from icecream import ic

confproject = Path(__file__).parents[3] / 'pyproject.toml'
versionfile = Path(__file__).parent / 'version.txt'

# setting default values for logger variables
logger_variables: dict[str, str | int | Path] = {
    'str_format': (
        '%(asctime)s;%(levelname)-8s;%(name)s;'
        '%(module)s;%(funcName)s;%(message)s'
    ),
    'datefmt': '%Y/%m/%d %H:%M:%S %z',
    'level': logging.INFO,
    'name': __name__,
    'filelog': Path(__file__).with_suffix('.log'),
    'filemode': 'a',
}


def modify_logger_runtime(
    var_name: str,
    new_value: str | float | None,
) -> NoReturn:
    """Access the global scope dictionary directly."""
    logger_variables[var_name] = new_value


def key_versions_2_sort(
    x: tuple[str, ...] | list[str],
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
        >>> key_versions_2_sort(('1.1.1rc0', 'aaa'))
        '000100010001.080000'
        >>> key_versions_2_sort(('1.1.1post1',))
        '000100010001.900001'
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


def update_version(pyproject_fl: Path, version_fl: Path | None = None) -> bool:
    """Update version into file."""
    pyproject_fl = pyproject_fl or confproject
    version_fl = version_fl or versionfile
    ic(version_fl)

    version_project, version_poetry, current_version = (
        '',
        '',
        '',
    )
    data: toml.TOMLDocument | None = None
    try:
        data = toml.load(pyproject_fl.open(encoding='utf-8'))
    except (FileExistsError, FileNotFoundError, UnicodeDecodeError):
        return False

    with contextlib.suppress(KeyError):
        version_project = data['project']['version']
        version_poetry = data['tool']['poetry']['version']

        current_version = max(
            version_poetry,
            version_project,
            key=lambda value: key_versions_2_sort((value,)),
        )
        ic(f'{current_version=}, {version_poetry=}, {version_project=}')

        data['tool']['poetry']['version'] = current_version
        data['project']['version'] = current_version

    version_fl.write_text(f'{current_version}\n', encoding='utf-8')
    toml.dump(data, pyproject_fl.open('w', encoding='utf-8'))

    return True


def logger(
    *args: tuple[str, ...],
    **kwargs: dict[str, str | int] | str | int | Path,
) -> logging.Logger:
    """Logger function for log.

    Args:
        args: str = positional arguments,
        kwargs: str = keyword arguments,
        The positional/keyword arguments are:
        - str_format: str = format of string to log,
        - datefmt: str = format date to log,
        - level: int = can be (logging.DEBUG, logging.INFO, logging.WARNING,
       logging.ERROR, logging.CRITICAL),
        - name: str = name of logger,
        - filelog: Path = log's file .py
        - filemode: str = mode to open log's file, can be 'a' or 'w'.

    Return:
        Return a logging.Logger object.

    """
    # logger variables
    pos: int = 0
    str_format: str = ''
    datefmt: str = ''
    level: int = logging.INFO
    name: str = ''
    filelog: Path = Path(__file__).with_suffix('.log')
    filemode: str = 'a'

    # load values for create logger
    if len(args) > pos:
        for key, value in logger_variables.items():
            try:
                logger_variables[key] = args[pos]
            except IndexError:
                logger_variables[key] = kwargs.get(key) or value
            pos += 1

    logging.basicConfig(
        filename=filelog,
        level=level,
        format=str_format,
        datefmt=datefmt,
        filemode=filemode,
    )

    # create logger
    console = logging.StreamHandler()
    formatter = logging.Formatter(str_format)
    console.setFormatter(formatter)
    logger_obj = logging.getLogger(name=name)
    logger_obj.addHandler(console)
    print(
        f'>>> {logger_obj.level=}, {logger_obj.name=}, {logger_obj.getEffectiveLevel()=}',
    )
    return logger_obj


__version__ = versionfile.read_text().strip()
__title__ = 'incolume.py.changelog'

if __name__ == '__main__':
    ic(key_versions_2_sort(('1.1.1rc90',)))
    ic(key_versions_2_sort(('1.0.1a90',)))
    ic(
        max(
            ['1.0.1a90', '1.1.0rc90', '1.1.1rc9', '1.1.1rc8', '1.1.1rc7'],
            key=lambda value: key_versions_2_sort((value,)),
        ),
    )

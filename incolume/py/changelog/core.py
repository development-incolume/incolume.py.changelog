"""Principal module."""

from __future__ import annotations

import contextlib
import logging
import re
from collections.abc import Container, Mapping
from pathlib import Path

import tomlkit as toml
from icecream import ic

confproject = Path(__file__).parents[3] / 'pyproject.toml'
versionfile = Path(__file__).parent / 'version.txt'
confchangelog = [
    confproject.with_name('changelog.toml'),
    confproject.with_name('.changelog.toml'),
    confproject,
]

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


def find_project_root(
    start_dir: Path | str = '', markers: tuple[str, ...] | None = None
) -> Path:
    """Find the project root directory by looking for specific markers."""
    if isinstance(start_dir, str):
        start_dir = Path(start_dir).resolve()

    if markers is None:
        markers = (
            'pyproject.toml',
            '.git',
            'requirements.txt',
            'setup.cfg',
            '.venv',
        )
    current = start_dir

    while current != current.parent:
        for marker in markers:
            if (current / marker).exists():
                return current
        current = current.parent

    msg = 'Project root not found (no markers detected).'
    raise FileNotFoundError(msg)


def select_configuration_fl(
    conf_changelog_fl: Path | None = None, files: list[Path] | None = None
) -> Path:
    """Check if the configuration file exists."""
    files = (
        [conf_changelog_fl, *files]  # type: ignore [list-item]
        if isinstance(files, list)
        else [conf_changelog_fl, *confchangelog]  # type: ignore [list-item]
    )
    for file in [f for f in files if f]:
        if file.exists():
            return file
    msg = (
        'Any Configuration file found: '
        f'{", ".join([file.name for file in files])}'
    )
    raise FileNotFoundError(msg)


def load_config(conf_changelog_fl: Path) -> Mapping[str, str | bool]:
    """Check if the configuration file exists."""
    loaded: toml.TOMLDocument = toml.load(conf_changelog_fl.open('rb'))
    config: Mapping[str, str | bool] = {}
    match loaded:
        case (
            {
                'settings': {'file': str()},
            }
            | {
                'settings': {'reverse': bool()},
            }
            | {
                'settings': {'url_compare': str()},
            }
            | {
                'settings': {'url_keepachangelog': str()},
            }
            | {
                'settings': {'url_semver': str()},
            }
            | {
                'settings': {'url_convetional_commit': str()},
            }
        ):
            config = loaded['settings']
        case (
            {
                'tool': {
                    'changelog': {
                        'settings': {
                            'file': str(),
                        }
                    }
                }
            }
            | {
                'tool': {
                    'changelog': {
                        'settings': {
                            'reverse': bool(),
                        }
                    }
                }
            }
            | {
                'tool': {
                    'changelog': {
                        'settings': {
                            'url_compare': str(),
                        }
                    }
                }
            }
            | {
                'tool': {
                    'changelog': {
                        'settings': {
                            'url_keepachangelog': str(),
                        }
                    }
                }
            }
            | {
                'tool': {
                    'changelog': {
                        'settings': {
                            'url_semver': str(),
                        }
                    }
                }
            }
            | {
                'tool': {
                    'changelog': {
                        'settings': {
                            'url_convetional_commit': str(),
                        }
                    }
                }
            }
        ):
            config = loaded['tool']['changelog']['settings']
        case _:
            msg = f'Invalid configuration: {conf_changelog_fl.as_posix()}'
            raise ValueError(msg)
    return config


def modify_logger_runtime(
    var_name: str,
    new_value: str | int | Path,
) -> None:
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

    def _format_from_match(match: re.Match[str] | None, qdig: int) -> str:
        if match is None:
            raise AttributeError
        # pegar major, minor e patch
        major = match.group(1)  # type: ignore [union-attr]
        minor = match.group(2)  # type: ignore [union-attr]
        patch = match.group(3)  # type: ignore [union-attr]
        build = match.group(6)  # type: ignore [union-attr]
        # pegar build, se não tiver colocar uma alta 99999
        build = build or '9' * qdig
        plus = classifies.get(
            re.sub(r'[-.]', '', str(match.group(5)).lower()),  # type: ignore [union-attr]
            0,
        )
        logging.debug('match.group(5): %s', plus)
        build = int(build) + plus
        return f'{major:0>4}{minor:0>4}{patch:0>4}.{build:0>6}'

    try:
        result = _format_from_match(
            get_major_minor_patch_build.search(x[0]), qdig
        )
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
    *args: str | int | Path,
    **kwargs: str | int | Path,
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
    ic(
        f'>>> {logger_obj.level=}, {logger_obj.name=},'
        f' {logger_obj.getEffectiveLevel()=}',
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

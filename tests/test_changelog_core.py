"""Test package."""

from __future__ import annotations
from collections import OrderedDict
import re
from typing import Any, ClassVar, TYPE_CHECKING
from inspect import stack
import logging
import pytest
from tempfile import gettempdir
from incolume.py.changelog import core as pkg
from icecream import ic
from pathlib import Path
from shutil import rmtree
from dataclasses import dataclass
from dotenv import load_dotenv
from os import getenv

if TYPE_CHECKING:
    from collections.abc import Callable
    from collections.abc import Generator


__author__ = '@britodfbr'  # pragma: no cover

load_dotenv()

ic.disable()
if getenv('DEBUG') or getenv('DEBUG_MODE') or getenv('INCOLUME_DEBUG_MODE'):
    ic.enable()


@dataclass
class Entrance:
    """Entrance for testing."""

    fileconfig: Path
    fileversion: Path


class TestFindProjectRoot:
    """Test case for module."""

    base_dir: ClassVar[Path]

    @pytest.fixture(autouse=True, scope='class')
    @classmethod
    def class_setup_teardown(
        cls,
    ) -> Generator[Callable[..., None], None, None]:
        """Set up/teardown class."""
        ic(f'Setup Class {cls.__name__}')
        cls.base_dir = Path(gettempdir(), cls.__name__)
        yield  # type: ignore[misc]
        ic(f'Teardown Class {cls.__name__}')

    @pytest.fixture(autouse=True)
    def method_setup_teardown(
        self, request
    ) -> Generator[Callable[..., None], None, None]:
        """Set up/teardown method."""
        ic(f'Setup Method: {request.function.__name__}')
        self.directory = self.base_dir / request.function.__name__
        yield  # type: ignore[misc]
        ic(f'Teardown Method: {request.function.__name__}')

    def test_find_project_root0(self) -> None:
        """Test for find_project_root."""
        assert pkg.find_project_root() == Path(__file__).parent.parent

    def test_find_project_root1(self) -> None:
        """Test for find_project_root."""
        self.directory.joinpath('noproject', 'a', 'b', 'c').mkdir(
            parents=True, exist_ok=True
        )

        with pytest.raises(
            FileNotFoundError,
            match=re.escape('Project root not found (no markers detected).'),
        ):
            pkg.find_project_root(
                start_dir=self.directory / 'noproject' / 'a' / 'b' / 'c',
                markers=('pyproject.toml',),
            )

    def test_find_project_root2(self) -> None:
        """Test for find_project_root."""
        self.directory.joinpath('project_test').mkdir(
            parents=True, exist_ok=True
        )
        self.directory.joinpath('project_test', 'pyproject.toml').touch()
        assert (
            pkg.find_project_root(self.directory / 'project_test')
            == self.directory / 'project_test'
        )

    def test_find_project_root3(self) -> None:
        """Test for find_project_root."""
        self.directory.joinpath('anotherproject', 'venv').mkdir(
            parents=True, exist_ok=True
        )
        self.directory.joinpath('anotherproject', 'a', 'b', 'c').mkdir(
            parents=True, exist_ok=True
        )

        assert (
            pkg.find_project_root(
                start_dir=self.directory / 'anotherproject' / 'a' / 'b' / 'c',
                markers=('venv',),
            )
            == self.directory / 'anotherproject'
        )


class TestConfiguration:
    """Test case for module."""

    def test_configuration_fl0(self) -> None:
        """Test for check_configuration."""
        fl = Path(gettempdir(), stack()[0][3], 'nonexistent_file.toml')
        with pytest.raises(
            FileNotFoundError,
            match=r'Any Configuration file found: nonexistent_file.toml',
        ):
            pkg.select_configuration_fl(fl, [])

    def test_configuration_fl1(self) -> None:
        """Test for check_configuration."""
        fl = Path(gettempdir(), stack()[0][3], 'nonexistent_file.toml')
        assert pkg.select_configuration_fl(fl).name in {
            '.changelog.toml',
            'changelog.toml',
            'pyproject.toml',
        }

    def test__configuration_fl2(self) -> None:
        """Test for check_configuration."""
        fl = Path(gettempdir(), stack()[0][3], 'existent_file.toml')
        fl.parent.mkdir(parents=True, exist_ok=True)
        fl.write_bytes(b'')
        assert pkg.select_configuration_fl(fl) == fl

    @pytest.mark.parametrize(
        ['entrance', 'configuration', 'expected'],
        [
            pytest.param(
                Path(gettempdir(), stack()[0][3], 'nonexistent_file.toml'),
                {
                    'settings': {
                        'file': Path(
                            gettempdir(), stack()[0][3], 'nonexistent_file.md'
                        ).as_posix(),
                        'reverse': True,
                        'url_compare': 'https://xpto.com/incolume.py.changelog/-/compare',
                        'url_convetional_commit': 'https://www.conventionalcommits.org/pt-br/9.0.0',
                        'url_keepachangelog': 'https://keepachangelog.com/en/9.0.0',
                        'url_semver': 'https://semver.org/spec/9.0.0.html',
                    }
                },
                {
                    'url_compare': '',
                    'url_keepachangelog': '',
                    'url_semver': '',
                    'url_convetional_commit': '',
                },
                marks=[],
            ),
            pytest.param(
                Path(gettempdir(), stack()[0][3], 'changelog.toml'),
                {
                    'settings': {
                        'file': Path(
                            gettempdir(), stack()[0][3], 'changelog.md'
                        ).as_posix(),
                        'reverse': False,
                        'url_compare': '',
                        'url_keepachangelog': '',
                        'url_semver': '',
                        'url_convetional_commit': '',
                    }
                },
                {},
                marks=[],
            ),
            pytest.param(
                Path(gettempdir(), stack()[0][3], '.changelog.toml'),
                {
                    'settings': {
                        'file': Path(
                            gettempdir(), stack()[0][3], '.changelog.md'
                        ).as_posix(),
                        'reverse': False,
                        'url_compare': '',
                        'url_keepachangelog': '',
                        'url_semver': '',
                        'url_convetional_commit': '',
                    }
                },
                {},
                marks=[],
            ),
            pytest.param(
                Path(gettempdir(), stack()[0][3], 'pyproject.toml'),
                {
                    'tool': {
                        'changelog': {
                            'settings': {
                                'file': Path(
                                    gettempdir(), stack()[0][3], 'pyproject.md'
                                ).as_posix(),
                                'reverse': False,
                                'url_compare': '',
                                'url_keepachangelog': '',
                                'url_semver': '',
                                'url_convetional_commit': '',
                            }
                        }
                    }
                },
                {},
                marks=[],
            ),
            pytest.param(
                Path(gettempdir(), stack()[0][3], 'another_file.toml'),
                {
                    'tool': {
                        'changelog': {
                            'setter': {
                                'file': Path(
                                    gettempdir(),
                                    stack()[0][3],
                                    'another_file.md',
                                ).as_posix(),
                                'reverse': False,
                                'url_compare': '',
                                'url_keepachangelog': '',
                                'url_semver': '',
                                'url_convetional_commit': '',
                            }
                        }
                    }
                },
                {},
                marks=[],
            ),
        ],
    )
    def test_load_config(self, entrance, configuration, expected) -> None:
        """Test for load_config."""
        entrance.parent.mkdir(parents=True, exist_ok=True)
        pkg.toml.dump(configuration, entrance.open('w', encoding='utf-8'))
        try:
            assert set(expected).issubset(set(pkg.load_config(entrance)))
        except ValueError:
            with pytest.raises(
                ValueError,
                match=r'Invalid configuration: .*',
            ):
                pkg.load_config(entrance)


class TestChangelogInit:
    """Test case for module."""

    nonefile: ClassVar = Path(gettempdir(), stack()[0][3], 'none.toml')
    confproject0: ClassVar = Path(gettempdir(), stack()[0][3], 'poetry.toml')
    confproject1: ClassVar = Path(gettempdir(), stack()[0][3], 'project.toml')
    versionfile: ClassVar = Path(gettempdir(), stack()[0][3], 'version.txt')

    @classmethod
    def setup_class(cls) -> None:
        """Set up class."""
        logging.info(ic(f'starting class {cls.__name__} execution'))
        cls.confproject0.parent.mkdir(exist_ok=True, parents=True)
        cls.confproject1.parent.mkdir(exist_ok=True, parents=True)
        cls.versionfile.parent.mkdir(exist_ok=True, parents=True)

    @classmethod
    def teardown_class(cls) -> None:
        """Tear down class."""
        logging.info(
            ic(f'finishing class {cls.__name__} execution'),
        )
        rmtree(cls.confproject0.parent, ignore_errors=True)

    def setup_method(self, method) -> None:
        """Set up method."""
        logging.info(ic(f'starting execution ({method}) of {stack()[0][3]}'))
        self.confproject0.write_text('[tool.poetry]\nversion = "0.1.0"')
        self.confproject1.write_text('[project]\nversion = "0.1.0"')

    def teardown_method(self, method) -> None:
        """Tear down method."""
        logging.info(ic(f'finishing execution ({method}) of {stack()[0][3]}'))
        rmtree(self.confproject0, ignore_errors=True)
        rmtree(self.confproject1, ignore_errors=True)

    @pytest.mark.parametrize(
        ['entrance', 'expected'],
        [
            pytest.param('test_var', 'new_value', marks=[]),
            pytest.param('test_var', 123, marks=[]),
            pytest.param('test_var', 123.456, marks=[]),
            pytest.param('test_var', True, marks=[]),
        ],
    )
    def test_modify_logger_runtime(self, entrance: str, expected: Any) -> None:
        """Test for modify_logger_runtime."""
        pkg.modify_logger_runtime(entrance, expected)
        assert pkg.logger_variables[entrance] == expected

    @pytest.mark.parametrize(
        ['entrance', 'expected'],
        [
            pytest.param(Entrance(nonefile, versionfile), False, marks=[]),
            pytest.param(Entrance(confproject0, versionfile), True, marks=[]),
            pytest.param(
                Entrance(confproject1, versionfile),
                True,
                marks=[],
            ),
        ],
    )
    def test_update_version(
        self,
        *,
        entrance: Entrance,
        expected: bool,
    ) -> None:
        """Unittest."""
        assert (
            pkg.update_version(entrance.fileconfig, entrance.fileversion)
            == expected
        )

    @pytest.mark.parametrize(
        ['xcpt', 'entrance', 'expected'],
        [
            pytest.param(
                None,
                {'x': ('0.5.11', 'aaa')},
                '000000050011.099999',
            ),
            pytest.param(
                None,
                {'x': ('0.5.11-dev0', 'aaa')},
                '000000050011.000000',
            ),
            pytest.param(
                None,
                {'x': ('0.5.1-dev9', 'aaa')},
                '000000050001.000009',
            ),
            pytest.param(
                None,
                {'x': ('0.5.1-dev19', 'aaa')},
                '000000050001.000019',
            ),
            pytest.param(
                None,
                {'x': ('0.5.1-dev99', 'aaa')},
                '000000050001.000099',
            ),
            pytest.param(
                None,
                {'x': ('0.5.1-alpha9', 'aaa')},
                '000000050001.020009',
            ),
            pytest.param(
                None,
                {'x': ('0.5.1-beta9', 'aaa')},
                '000000050001.000009',
            ),
            pytest.param(
                None,
                {'x': ('0.5.1-rc.9', 'aaa')},
                '000000050001.080009',
            ),
            pytest.param(
                None,
                {'x': ('0.5.1-rc.1', 'aaa')},
                '000000050001.080001',
            ),
            pytest.param(
                None,
                {'x': ('0.5.1-rc1', 'aaa')},
                '000000050001.080001',
            ),
            pytest.param(
                None,
                {'x': ('0.5.1rc1', 'aaa')},
                '000000050001.080001',
            ),
            pytest.param(
                None,
                {'x': ('0.5.1-alpha.1', 'aaa')},
                '000000050001.020001',
            ),
            pytest.param(
                None,
                {'x': ('0.5.1-alpha.2', 'aaa')},
                '000000050001.020002',
            ),
            pytest.param(
                None,
                {'x': ('0.5.1-alpha.3', 'aaa')},
                '000000050001.020003',
            ),
            pytest.param(
                None,
                {'x': ('0.5.1-alpha.4', 'aaa')},
                '000000050001.020004',
            ),
            pytest.param(
                None,
                {'x': ('0.5.1-alpha.0', 'aaa')},
                '000000050001.020000',
            ),
            pytest.param(
                None,
                {'x': ('0.5.1-post.0', 'aaa')},
                '000000050001.900000',
            ),
            pytest.param(
                None,
                {'x': ('1.5.1-post5', 'aaa')},
                '000100050001.900005',
            ),
            pytest.param(None, {'x': ('1.5', 'aaa')}, '1.5'),
            pytest.param(
                None,
                {'x': ('1.5.1-rc.0', 'aaa')},
                '000100050001.080000',
            ),
            pytest.param(
                None,
                {'x': ('1.5.1-rc0', 'aaa')},
                '000100050001.080000',
            ),
            pytest.param(
                None,
                {'x': ('1.5.1rc0', 'aaa')},
                '000100050001.080000',
            ),
            pytest.param(
                None,
                {'x': ('1.5.1-a.0', 'aaa')},
                '000100050001.020000',
            ),
            pytest.param(
                None,
                {'x': ('1.5.1-a0', 'aaa')},
                '000100050001.020000',
            ),
            pytest.param(
                None,
                {'x': ('1.5.1a0', '')},
                '000100050001.020000',
            ),
            pytest.param(None, {'x': ('1.5.1', 'aaa')}, '000100050001.099999'),
            pytest.param(None, {'x': ('1.5.1rc999',)}, '000100050001.080999'),
            pytest.param(
                {
                    'expected_exception': TypeError,
                    'match': 'must be tuple or list.',
                },
                {'x': 1},
                '00010501.099999',
            ),
        ],
    )
    def test_key_versions_2_sort(
        self,
        *,
        xcpt: Any,
        entrance: dict[str, str],
        expected: str,
    ) -> None:
        """Test for key_versions_2_sort."""
        try:
            assert pkg.key_versions_2_sort(**entrance) == expected
        except TypeError:
            with pytest.raises(**xcpt):
                assert pkg.key_versions_2_sort(**entrance) == expected

    @pytest.mark.parametrize(
        ['entrance', 'reverse', 'expected'],
        [
            (
                {
                    '2019.5.1': 'aaa',
                    '2019.5.1-dev9': 'aaa',
                    '2019.5.1-alpha9': 'aaa',
                    '2019.5.1-beta9': 'aaa',
                    '2019.5.1-rc.9': 'aaa',
                    '2019.5.1-rc1': 'aaa',
                    '2019.5.1-post0': 'aaa',
                    '2019.5.0': 'aaa',
                    '2019.5.2-a.0': 'aaa',
                },
                True,
                [
                    ('2019.5.2-a.0', 'aaa'),
                    ('2019.5.1-post0', 'aaa'),
                    ('2019.5.1', 'aaa'),
                    ('2019.5.1-rc.9', 'aaa'),
                    ('2019.5.1-rc1', 'aaa'),
                    ('2019.5.1-alpha9', 'aaa'),
                    ('2019.5.1-dev9', 'aaa'),
                    ('2019.5.1-beta9', 'aaa'),
                    ('2019.5.0', 'aaa'),
                ],
            ),
            (
                {
                    '0.1.0': '1',
                    '0.1.0-dev.0': '2',
                    '0.1.0-post.0': '3',
                    '0.1.0-a.1': '4',
                    '0.1.0-a.0': '5',
                    '0.1.1-a.0': '6',
                    '0.1.0-rc.1': '7',
                    '0.1.0-rc.2': '8',
                },
                False,
                [
                    ('0.1.0-dev.0', '2'),
                    ('0.1.0-a.0', '5'),
                    ('0.1.0-a.1', '4'),
                    ('0.1.0-rc.1', '7'),
                    ('0.1.0-rc.2', '8'),
                    ('0.1.0', '1'),
                    ('0.1.0-post.0', '3'),
                    ('0.1.1-a.0', '6'),
                ],
            ),
            pytest.param(
                OrderedDict(
                    {
                        '2019.5.1': 'aaa',
                        '2019.5.11': 'aaa',
                        '2019.5.11-dev0': 'aaa',
                        '2019.5.1-dev9': 'aaa',
                        '2019.5.1-dev19': 'aaa',
                        '2019.5.1-dev99': 'aaa',
                        '2019.5.1-alpha9': 'aaa',
                        '2019.5.1-beta9': 'aaa',
                        '2019.5.1-rc.9': 'aaa',
                        '2019.5.1-rc1': 'aaa',
                        '2019.5.1-alpha.1': 'aaa',
                        '2019.5.1-alpha.2': 'aaa',
                        '2019.5.1-alpha.3': 'aaa',
                        '2019.5.1-alpha.4': 'aaa',
                        '2019.5.1-alpha.0': 'aaa',
                        '2019.5.1-post0': 'aaa',
                        '2019.5.11-post.0': 'aaa',
                        '2019.5.11-dev1': 'aaa',
                        '2019.5.2-dev0': 'aaa',
                        '2019.5.2-dev1': 'aaa',
                        '2019.5.2-dev2': 'aaa',
                        '2019.5.2-alpha.0': 'aaa',
                        '2019.5.1-dev98': 'aaa',
                        '2019.5.2': 'aaa',
                        '2019.5.0': 'aaa',
                    },
                ),
                True,
                [
                    ('2019.5.11-post.0', 'aaa'),
                    ('2019.5.11', 'aaa'),
                    ('2019.5.11-dev1', 'aaa'),
                    ('2019.5.11-dev0', 'aaa'),
                    ('2019.5.2', 'aaa'),
                    ('2019.5.2-alpha.0', 'aaa'),
                    ('2019.5.2-dev2', 'aaa'),
                    ('2019.5.2-dev1', 'aaa'),
                    ('2019.5.2-dev0', 'aaa'),
                    ('2019.5.1-post0', 'aaa'),
                    ('2019.5.1', 'aaa'),
                    ('2019.5.1-rc.9', 'aaa'),
                    ('2019.5.1-rc1', 'aaa'),
                    ('2019.5.1-alpha9', 'aaa'),
                    ('2019.5.1-alpha.4', 'aaa'),
                    ('2019.5.1-alpha.3', 'aaa'),
                    ('2019.5.1-alpha.2', 'aaa'),
                    ('2019.5.1-alpha.1', 'aaa'),
                    ('2019.5.1-alpha.0', 'aaa'),
                    ('2019.5.1-dev99', 'aaa'),
                    ('2019.5.1-dev98', 'aaa'),
                    ('2019.5.1-dev19', 'aaa'),
                    ('2019.5.1-dev9', 'aaa'),
                    ('2019.5.1-beta9', 'aaa'),
                    ('2019.5.0', 'aaa'),
                ],
                marks=(),
            ),
        ],
    )
    def test_apply_key_versions_2_sort(
        self,
        *,
        entrance: dict[str, str],
        reverse: bool,
        expected: list[tuple[str, str]],
    ) -> None:
        """Sort with this function."""
        result = sorted(
            entrance.items(),
            key=pkg.key_versions_2_sort,
            reverse=reverse,
        )
        assert result == expected

    @pytest.mark.parametrize(
        'entrance',
        [
            pytest.param(
                (
                    '%(message)s',
                    '%Y/%m/%dT%H:%M:%S(%z)',
                ),
                marks=[],
            ),
            pytest.param(
                {
                    'filelog': Path(
                        gettempdir(),
                        stack()[0][3],
                        'logfile.log',
                    ),
                    'level': pkg.logging.FATAL,
                },
                marks=[],
            ),
            pytest.param(
                (
                    '%(message)s',
                    '%Y/%m/%dT%H:%M:%S(%z)',
                    pkg.logging.WARNING,
                    'testing_logger_1',
                    Path(gettempdir(), stack()[0][3], 'logfile.log'),
                    'w',
                ),
                marks=[],
            ),
            pytest.param(
                {
                    'str_format': '%(message)s',
                    'date_format': '%Y/%m/%dT%H:%M:%S(%z)',
                    'level': pkg.logging.CRITICAL,
                    'name': 'testing_logger_2',
                    'filename': Path(
                        gettempdir(),
                        stack()[0][3],
                        'logfile.log',
                    ),
                    'filemode': 'w',
                },
                marks=[],
            ),
            pytest.param(
                {
                    'filemode': 'r+',
                },
                marks=[],
            ),
        ],
    )
    def test_logger(self, entrance: dict[str, any]) -> None:  # type: ignore[valid-type]
        """Logger."""
        if isinstance(entrance, dict):
            logg = pkg.logger(**entrance)
        if isinstance(entrance, tuple):  # type: ignore[unreachable]
            logg = pkg.logger(*entrance)  # type: ignore[unreachable]
        ic(logg.level, logg.name, logg.getEffectiveLevel())
        assert isinstance(logg, pkg.logging.Logger)

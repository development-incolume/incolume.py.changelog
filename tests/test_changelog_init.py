"""Test package."""

from __future__ import annotations
from collections import OrderedDict
from typing import Any, ClassVar, NoReturn
from inspect import stack
import logging
import pytest
from tempfile import gettempdir
from incolume.py import changelog as pkg
from icecream import ic
from pathlib import Path
from shutil import rmtree
from dataclasses import dataclass
from dotenv import load_dotenv
from os import  getenv


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


class TestChangelogInit:
    """Test case for module."""

    nonefile: ClassVar = Path(gettempdir(), stack()[0][3], 'none.toml')
    confproject0: ClassVar = Path(gettempdir(), stack()[0][3], 'poetry.toml')
    confproject1: ClassVar = Path(gettempdir(), stack()[0][3], 'project.toml')
    versionfile: ClassVar = Path(gettempdir(), stack()[0][3], 'version.txt')

    @classmethod
    def setup_class(cls):
        """Setup class."""
        logging.info(ic(f'starting class {cls.__name__} execution'))
        cls.confproject0.parent.mkdir(exist_ok=True, parents=True)
        cls.confproject1.parent.mkdir(exist_ok=True, parents=True)
        cls.versionfile.parent.mkdir(exist_ok=True, parents=True)

    @classmethod
    def teardown_class(cls):
        """Teardown class."""
        logging.info(
            ic(f'finishing class {cls.__name__} execution'),
        )
        rmtree(cls.confproject0.parent, ignore_errors=True)

    def setup_method(self, method):
        """Setup method."""
        logging.info(ic(f'starting execution ({method}) of {stack()[0][3]}'))
        self.confproject0.write_text('[tool.poetry]\nversion = "0.1.0"')
        self.confproject1.write_text('[project]\nversion = "0.1.0"')

    def teardown_method(self, method):
        """Teardown method."""
        logging.info(ic(f'finishing execution ({method}) of {stack()[0][3]}'))
        rmtree(self.confproject0, ignore_errors=True)
        rmtree(self.confproject1, ignore_errors=True)

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
    ) -> NoReturn:
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
                {'x': ('1.5.1-post0', 'aaa')},
                '000100050001.900000',
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
                {'x': ('1.5.1a0', 'aaa')},
                '000100050001.020000',
            ),
            pytest.param(None, {'x': ('1.5.1', 'aaa')}, '000100050001.099999'),
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
            with pytest.raises(**xcpt):  # noqa: PT010
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

    def test_logger(self, file_temp: Path) -> None:
        """Logger."""
        logg = pkg.logger(filelog=file_temp)
        assert isinstance(logg, pkg.logging.Logger)

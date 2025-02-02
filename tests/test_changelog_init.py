"""Test package."""

from __future__ import annotations
from collections import OrderedDict
from typing import Any, TYPE_CHECKING

import pytest

from incolume.py import changelog as pkg

if TYPE_CHECKING:
    from pathlib import Path


__author__ = '@britodfbr'  # pragma: no cover


@pytest.mark.parametrize(
    'xcpt entrance expected'.split(),
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
        pytest.param(None, {'x': ('0.5.1-rc1', 'aaa')}, '000000050001.080001'),
        pytest.param(None, {'x': ('0.5.1rc1', 'aaa')}, '000000050001.080001'),
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
        pytest.param(None, {'x': ('1.5.1-rc0', 'aaa')}, '000100050001.080000'),
        pytest.param(None, {'x': ('1.5.1rc0', 'aaa')}, '000100050001.080000'),
        pytest.param(None, {'x': ('1.5.1-a.0', 'aaa')}, '000100050001.020000'),
        pytest.param(None, {'x': ('1.5.1-a0', 'aaa')}, '000100050001.020000'),
        pytest.param(None, {'x': ('1.5.1a0', 'aaa')}, '000100050001.020000'),
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
    'entrance reverse expected'.split(),
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


def test_logger(file_temp: Path) -> None:
    """Logger."""
    logg = pkg.logger(filelog=file_temp)
    assert isinstance(logg, pkg.logging.Logger)

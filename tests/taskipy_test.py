"""Contrato: tasks do taskipy declaradas em pyproject.toml."""

import tomllib
from pathlib import Path
from typing import cast

import pytest

__author__ = '@britodfbr'  # pragma: no cover

ROOT = Path(__file__).resolve().parents[1]


def _tasks() -> dict[str, str]:
    """Retorna as tasks declaradas em pyproject.toml."""
    data = tomllib.loads((ROOT / 'pyproject.toml').read_text(encoding='utf-8'))
    return cast('dict[str, str]', data['tool']['taskipy']['tasks'])


@pytest.mark.fast
class TestTaskipy:
    """As tasks do taskipy estão ativas."""

    @pytest.mark.parametrize(
        'task',
        [
            'bandit',
            'check-all',
            'pre_check-all',
            'post_check-all',
            'lint_mypy',
        ],
    )
    def test_task_presente(self, task: str) -> None:
        """A task está declarada e não comentada."""
        assert task in _tasks(), f'task {task!r} ausente'

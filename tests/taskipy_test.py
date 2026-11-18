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
            'pre_sec',
            'qa',
            'safety',
            'sec',
            'setup',
            'test-all',
            'ty',
        ],
    )
    def test_task_presente(self, task: str) -> None:
        """A task está declarada e não comentada."""
        assert task in _tasks(), f'task {task!r} ausente'

    @pytest.mark.parametrize(
        'task',
        [
            'changelog',
            'check-all',
            'clean',
            'clean-all',
            'docs-build',
            'docs-serve',
            'gcl',
            'lint',
            'lint_mypy',
            'lint_ruff',
            'post_check-all',
            'pre_check-all',
            'pre_changelog',
            'pre_clean-all',
            'pre_docs-build',
            'pre_lint',
            'pre_test-all',
            'pre_tests',
            'tests',
        ],
    )
    def test_task_removida(self, task: str) -> None:
        """A task redundante foi retirada."""
        assert task not in _tasks(), f'task {task!r} deveria ter sido retirada'

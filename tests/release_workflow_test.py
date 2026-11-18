"""Contrato do workflow de release (multplatform-ci-cd.yml)."""

from pathlib import Path

import pytest

__author__ = '@britodfbr'  # pragma: no cover

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / '.github' / 'workflows' / 'multplatform-ci-cd.yml'


def _text() -> str:
    """Retorna o conteúdo do workflow de release."""
    return WORKFLOW.read_text(encoding='utf-8')


@pytest.mark.fast
class TestReleaseWorkflow:
    """Contrato do workflow de release."""

    def test_workflow_existe(self) -> None:
        """Workflow existe."""
        assert WORKFLOW.is_file(), f'{WORKFLOW=}'

    def test_dispara_em_dev_e_pr(self) -> None:
        """Dispara em push/pull_request para dev e em tags."""
        text = _text()
        assert '- dev' in text
        assert '- "*.*.*"' in text

    def test_actions_atuais(self) -> None:
        """Usa actions/checkout e setup-python na versão atual."""
        text = _text()
        assert 'actions/checkout@v2' not in text
        assert 'actions/checkout@v3' not in text
        assert 'actions/setup-python@v2' not in text
        assert 'actions/setup-python@v3' not in text

    def test_release_somente_em_tags(self) -> None:
        """Jobs de release só rodam em tag."""
        text = _text()
        assert 'refs/tags' in text

    def test_prerelease_nao_fixo(self) -> None:
        """Prerelease é derivado da tag, não fixo em true."""
        text = _text()
        assert 'prerelease: true' not in text
        assert 'prerelease: ${{' in text

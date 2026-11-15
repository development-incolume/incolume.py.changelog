"""Testes do contrato do workflow de docs (docs_ci_cd.yml)."""

from pathlib import Path

import pytest

__author__ = '@britodfbr'  # pragma: no cover

WORKFLOW = (
    Path(__file__).resolve().parents[1]
    / '.github'
    / 'workflows'
    / 'docs_ci_cd.yml'
)


@pytest.mark.fast
class TestCase:
    """Contrato do job Docs by CI/CD."""

    def test_workflow_existe(self) -> None:
        """Workflow existe."""
        assert WORKFLOW.is_file(), f'{WORKFLOW=}'

    def test_validacao_de_links(self) -> None:
        """O workflow roda uma validação de links que falha em quebrado."""
        text = WORKFLOW.read_text(encoding='utf-8')
        assert 'link quebrado' in text
        assert 'links internos OK' in text

    def test_validacao_de_encoding(self) -> None:
        """O workflow roda uma validação de encoding UTF-8 estrita."""
        text = WORKFLOW.read_text(encoding='utf-8')
        assert 'encoding UTF-8 inválido' in text
        assert "codecs.open(p, encoding='utf-8', errors='strict')" in text

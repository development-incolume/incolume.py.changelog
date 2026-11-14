"""Testes do contrato do workflow de CI/CD (codecov)."""

from pathlib import Path

import pytest

__author__ = '@britodfbr'  # pragma: no cover

WORKFLOW = (
    Path(__file__).resolve().parents[1]
    / '.github'
    / 'workflows'
    / 'multplatform-ci-cd.yml'
)


def _coverage_job_block() -> str:
    """Retorna o bloco do job ``coverage`` do workflow."""
    text = WORKFLOW.read_text(encoding='utf-8')
    start = text.index('\n  coverage:')
    end = text.index('\n  build:', start)
    return text[start:end]


@pytest.mark.fast
class TestCase:
    """Contrato do job Coverage by codecov."""

    def test_workflow_existe(self) -> None:
        """Workflow existe."""
        assert WORKFLOW.is_file(), f'{WORKFLOW=}'

    def test_checkout_sem_token_do_codecov(self) -> None:
        """Checkout não usa o token do Codecov como credencial do GitHub."""
        assert (
            'token: ${{ secrets.CODECOV_TOKEN }}' not in _coverage_job_block()
        )

    def test_gera_relatorio_de_cobertura(self) -> None:
        """Job de coverage roda pytest para gerar o relatório."""
        assert 'uv run pytest' in _coverage_job_block()

    def test_upload_aponta_o_relatorio(self) -> None:
        """Upload aponta para o relatório de cobertura gerado."""
        assert 'files: coverage_report/cov.xml' in _coverage_job_block()

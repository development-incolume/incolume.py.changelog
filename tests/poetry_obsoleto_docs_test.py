"""Contrato: a documentação não manda espelhar versão em [tool.poetry]."""

from pathlib import Path

import pytest

__author__ = '@britodfbr'  # pragma: no cover

ROOT = Path(__file__).resolve().parents[1]

DOCS = (
    ('AGENTS.md',),
    ('docs', 'analysis_artifacts', 'ADR-001-geracao-changelog.md'),
    ('docs', 'analysis_artifacts', 'SPEC-001-execucao.md'),
)


@pytest.mark.fast
class TestPoetryObsoletoDocs:
    """A documentação trata [tool.poetry] como obsoleto."""

    def test_nao_manda_espelhar_versao_em_poetry(self) -> None:
        """Nenhum documento orienta ajustar [tool.poetry] version."""
        for parts in DOCS:
            text = ROOT.joinpath(*parts).read_text(encoding='utf-8')
            assert '[tool.poetry] version' not in text, parts

    def test_version_txt_segue_como_fonte(self) -> None:
        """version.txt permanece como arquivo espelhado."""
        for parts in DOCS:
            text = ROOT.joinpath(*parts).read_text(encoding='utf-8')
            assert 'version.txt' in text, parts

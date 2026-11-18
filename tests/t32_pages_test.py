"""Testes do contrato de padronização de URLs sem .md (T3.2).

Critério de aceite: nenhum link interno de docs/ aponta para .md;
todos usam o caminho de página (sem sufixo).
"""

from pathlib import Path

import re

import pytest

REPO = Path(__file__).resolve().parents[1]
MKDOCS = REPO / 'mkdocs.yml'
DOCS = REPO / 'docs'


@pytest.mark.fast
class TestCase:
    """Contrato da padronização de URLs sem .md."""

    def test_mkdocs_nao_usa_dot_md_nos_links(self) -> None:
        """O nav do mkdocs.yml não usa o sufixo .md."""
        text = MKDOCS.read_text(encoding='utf-8')
        for line in text.splitlines():
            stripped = line.strip()
            if stripped.startswith('- '):
                assert '.md' not in stripped, f'link .md no nav: {stripped}'

    def test_docs_sem_link_relativo_dot_md(self) -> None:
        """Nenhum link relativo de docs/ aponta para .md."""
        pattern = re.compile(r'\]\([^)\s]+\)\)')
        for md in sorted(DOCS.rglob('*.md')):
            for i, line in enumerate(md.read_text(encoding='utf-8'), 1):
                for href in pattern.findall(line):
                    if href.startswith(('http:', 'https:', 'mailto:')):
                        continue
                    assert not href.endswith('.md'), (
                        f'{md}:{i} link relativo para .md: {href}'
                    )


__author__ = '@britodfbr'  # pragma: no cover

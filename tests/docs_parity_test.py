"""Testes de paridade estrutural entre os idiomas de um documento."""

import re
from pathlib import Path

import pytest

__author__ = '@britodfbr'  # pragma: no cover

DOCS = Path(__file__).resolve().parents[1] / 'docs' / 'user_guide'
LANGS = ('de', 'en', 'es', 'fr', 'it')
HEADING = re.compile(r'^(#+)', re.MULTILINE)


def _levels(path: Path) -> list[int]:
    """Retorna os níveis dos headings, na ordem em que aparecem."""
    text = path.read_text(encoding='utf-8')
    return [len(m.group(1)) for m in HEADING.finditer(text)]


@pytest.mark.fast
class TestParidade:
    """Paridade estrutural entre pt-BR e os demais idiomas."""

    def test_conventional_commits_equivalente(self) -> None:
        """COVENTIONAL_COMMITS: mesma estrutura nos cinco idiomas."""
        base = _levels(DOCS / 'COVENTIONAL_COMMITS.md')
        for lang in LANGS:
            assert _levels(DOCS / f'COVENTIONAL_COMMITS.{lang}.md') == base, (
                lang
            )

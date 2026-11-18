"""Testes do contrato do guia de contribuição (T3.4).

Critério de aceite: o guia de contribuição `docs/user_guide/development.md`
está disponível nos todos os idiomas, e segue a estrutura mínima do
template de documento do projeto.
"""

from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[1]
DOCS = REPO / 'docs'
USER_GUIDE = DOCS / 'user_guide'
LANGS = ('en', 'de', 'es', 'fr', 'it')


@pytest.mark.fast
class TestCase:
    """Contrato do guia de contribuição."""

    def test_guia_existe(self) -> None:
        """O arquivo de contribuição existe na raiz do doc."""
        assert (USER_GUIDE / 'development.md').is_file()

    def test_guia_presente_em_todas_linguas(self) -> None:
        """O guia de contribuição está presente em todos os idiomas."""
        for lang in LANGS:
            path = USER_GUIDE / f'development.{lang}.md'
            assert path.is_file(), f'faltando {path}'

    def test_guia_e_legivel(self) -> None:
        """O guia contém pelo menos uma seção principal."""
        sections_min = 3
        text = (USER_GUIDE / 'development.md').read_text(encoding='utf-8')
        lines = text.splitlines()
        sections = [line for line in lines if line.startswith('## ')]
        assert len(sections) >= sections_min, (
            'menos de 3 seções no guia de contribuição'
        )

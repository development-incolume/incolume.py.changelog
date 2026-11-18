"""Testes dos exemplos de API documentados em ``docs/api/``.

Critério de aceite: cada exemplo de código executável consta nos
arquivos ``docs/api/index.*.md`` e pode ser executado sem erro, produzindo
saída consistente.
"""

import ast
import re
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[1]
DOCS = REPO / 'docs'
DOCS_API = DOCS / 'api'
LANGS = ('en', 'de', 'es', 'fr', 'it')  # 'md' é o default (português)

__author__ = '@britodfbr'  # pragma: no cover


@pytest.mark.fast
class TestCase:
    """Contrato dos exemplos de API dentro da documentação."""

    def test_docs_api_existe(self) -> None:
        """O diretório ``docs/api`` existe."""
        assert DOCS_API.is_dir(), f'{DOCS_API=}'

    def test_linguas_disponiveis(self) -> None:
        """Todas as línguas possuem o arquivo de API."""
        for lang in LANGS:
            path = DOCS_API / f'index.{lang}.md'
            assert path.is_file(), f'faltando {path}'

    def test_pt_default_existe(self) -> None:
        """O exemplo em português (default) existe."""
        assert (DOCS_API / 'index.md').is_file()

    def test_exemplos_python_execuaveis(self) -> None:
        """Código em blocos ```python dos docs é compilável."""
        for lang in LANGS:
            path = DOCS_API / f'index.{lang}.md'
            text = path.read_text(encoding='utf-8')
            # Extrai todos os blocos de código marcados como python
            blocks = re.findall(r'```python\n(.*?)```', text, re.DOTALL)
            assert blocks, f'nenhum bloco python em {path}'
            for i, block in enumerate(blocks):
                try:
                    ast.parse(block)
                except SyntaxError as exc:
                    pytest.fail(f'{path}:{i + 1}.py:{exc.msg}')
            for node in ast.walk(ast.parse(''.join(blocks))):
                if isinstance(node, ast.FunctionDef):
                    assert node.name.islower(), (
                        f'função não snake_case: {node.name} em {path}'
                    )

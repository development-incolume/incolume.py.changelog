"""Testes do contrato de navegação i18n do ``mkdocs.yml``."""

import re
from pathlib import Path
from typing import Any, cast

import pytest
import yaml

__author__ = '@britodfbr'  # pragma: no cover

MKDOCS = Path(__file__).resolve().parents[1] / 'mkdocs.yml'

PYTHON_NAME = re.compile(r'!!python/name:\S+')


def _load() -> dict[str, Any]:
    """Carrega o mkdocs.yml, ignorando as tags ``!!python/name:``."""
    text = PYTHON_NAME.sub('', MKDOCS.read_text(encoding='utf-8'))
    return cast('dict[str, Any]', yaml.safe_load(text))


def _nav_titles(nav: list[dict[str, Any]]) -> list[str]:
    """Retorna todos os títulos do nav, recursivamente."""
    titles: list[str] = []
    for item in nav:
        for title, value in item.items():
            titles.append(title)
            if isinstance(value, list):
                titles.extend(_nav_titles(value))
    return titles


def _i18n() -> dict[str, Any]:
    """Retorna a configuração do plugin i18n."""
    data = _load()
    plugins = [
        plugin
        for plugin in data['plugins']
        if isinstance(plugin, dict) and 'i18n' in plugin
    ]
    assert plugins, 'plugin i18n não encontrado no mkdocs.yml'
    return cast('dict[str, Any]', plugins[0]['i18n'])


@pytest.mark.fast
class TestCase:
    """Contrato do nav i18n."""

    def test_mkdocs_existe(self) -> None:
        """Arquivo mkdocs.yml existe."""
        assert MKDOCS.is_file(), f'{MKDOCS=}'

    def test_todo_nav_traduzido_em_todos_os_locales(self) -> None:
        """Toda chave do nav tem tradução nos locales não default."""
        data = _load()
        titles = set(_nav_titles(data['nav']))
        for lang in _i18n()['languages']:
            if lang.get('default'):
                continue
            translations = lang.get('nav_translations') or {}
            missing = sorted(titles - set(translations))
            assert not missing, f'{lang["locale"]}: faltam {missing}'

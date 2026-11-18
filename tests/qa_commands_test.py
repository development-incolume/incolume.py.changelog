"""Contrato de padronização dos comandos de QA.

As quatro fontes (AGENTS.md, SPEC-001, tox.toml e unit-tests.yml) devem
conter exatamente o conjunto canônico de comandos de QA.
"""

from pathlib import Path

import pytest

__author__ = '@britodfbr'  # pragma: no cover

ROOT = Path(__file__).resolve().parents[1]

QA_COMMANDS = (
    'ruff check --fix tests/ incolume/',
    'ruff format tests/ incolume/',
    'mypy tests/ incolume/',
    'ty check tests/ incolume/',
    'pytest -vvv tests/ incolume/',
)


def _text(*parts: str) -> str:
    """Retorna o conteúdo de um arquivo do repositório."""
    return ROOT.joinpath(*parts).read_text(encoding='utf-8')


def _expand(text: str) -> str:
    """Substitui `$d` pelo valor canônico."""
    return text.replace('$d', 'tests/ incolume/')


@pytest.mark.fast
class TestQACommands:
    """O conjunto canônico de QA está presente nas quatro fontes."""

    def test_agents_md(self) -> None:
        """AGENTS.md do repo usa os comandos canônicos."""
        text = _expand(_text('AGENTS.md'))
        for cmd in QA_COMMANDS:
            assert cmd in text, f'{cmd!r} ausente em AGENTS.md'

    def test_spec001(self) -> None:
        """SPEC-001 usa os comandos canônicos."""
        text = _expand(
            _text('docs', 'analysis_artifacts', 'SPEC-001-execucao.md')
        )
        for cmd in QA_COMMANDS:
            assert cmd in text, f'{cmd!r} ausente em SPEC-001'

    def test_unit_tests_workflow(self) -> None:
        """CI (unit-tests.yml) executa os comandos canônicos."""
        text = _expand(_text('.github', 'workflows', 'unit-tests.yml'))
        for cmd in QA_COMMANDS:
            assert cmd in text, f'{cmd!r} ausente em unit-tests.yml'

    def test_tox(self) -> None:
        """tox.toml executa os comandos canônicos."""
        lines = _text('tox.toml').splitlines()
        for cmd in QA_COMMANDS:
            tokens = cmd.split()
            assert any(
                all(f'"{token}"' in line for token in tokens) for line in lines
            ), f'{cmd!r} ausente em tox.toml'

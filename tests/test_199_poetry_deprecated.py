"""Testes do contrato da task #199: marcação de Poetry como obsoleto.

Critérios de aceitação (AC-199):
1. Notificação em Unreleased sobre a marcação de Poetry como obsoleto
2. Remoção da configuração Poetry vinculada ao projeto
3. Atualização da versão para o próximo step de release
"""

import re
import tomllib
from pathlib import Path


def test_poetry_secao_removida_do_pyproject() -> None:
    """A seção [tool.poetry] não deve permanecer ativa no pyproject.toml."""
    pyproject_path = Path(__file__).parent.parent / 'pyproject.toml'
    content = pyproject_path.read_text(encoding='utf-8')

    # Verifica se não há seção [tool.poetry] ativa
    # Se existir, deve estar marcada como deprecated/obsoleta
    poetry_section = re.search(
        r'\[tool\.poetry\](.*?)(?=\n\[|$)', content, re.DOTALL
    )
    if poetry_section is None:
        return
    assert re.search(r'(?i)obsolete|deprecated', poetry_section.group(0)), (
        'A seção [tool.poetry] deve ser marcada como obsoleta/deprecated'
    )


def test_poetry_toml_nao_deve_representar_configuracao_ativa() -> None:
    """O poetry.toml deve ser removido ou claramente obsoleto."""
    poetry_toml = Path(__file__).parent.parent / 'poetry.toml'
    if poetry_toml.exists():
        content = poetry_toml.read_text(encoding='utf-8')
        # O poetry.toml deve conter configuração obsoleta ou ser removido
        assert 'in-project' not in content or 'obsolete' in content.lower(), (
            'poetry.toml deve ser marcado como obsoleto ou removido'
        )


def test_version_atualizada() -> None:
    """A versão do version.txt acompanha a versão canônica do projeto."""
    pyproject_path = Path(__file__).parent.parent / 'pyproject.toml'
    pyproject = tomllib.loads(pyproject_path.read_text(encoding='utf-8'))
    version_file = (
        Path(__file__).parent.parent
        / 'incolume'
        / 'py'
        / 'changelog'
        / 'version.txt'
    )
    version = version_file.read_text(encoding='utf-8').strip()
    assert version == pyproject['project']['version'], (
        f'Versão divergente: version.txt={version}, '
        f'pyproject={pyproject["project"]["version"]}'
    )


def test_changelog_notifica_depreciacao_poetry() -> None:
    """O CHANGELOG deve conter notificação sobre a depreciação da Poetry."""
    changelog = (
        Path(__file__).parent.parent / 'docs' / 'about' / 'CHANGELOG.md'
    )
    content = changelog.read_text(encoding='utf-8')

    # Verifica se há notificação sobre a marcação de Poetry como obsoleto
    assert 'poetry' in content.lower(), 'CHANGELOG deve mencionar Poetry'
    assert 'obsoleto' in content.lower() or 'deprecated' in content.lower(), (
        'CHANGELOG deve indicar que Poetry está obsoleto/deprecated'
    )

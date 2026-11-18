"""Contrato: nenhuma pasta de `wt/` pode ficar órfã."""

import os
from pathlib import Path

import pytest

__author__ = '@britodfbr'  # pragma: no cover


def _main_root() -> Path:
    """Retorna a raiz do clone principal (vale para worktrees)."""
    for candidate in Path(__file__).resolve().parents:
        git = candidate / '.git'
        if git.is_dir():
            return candidate
        if git.is_file():
            texto = git.read_text(encoding='utf-8').strip()
            gitdir = Path(texto.split(':', 1)[1].strip())
            if not gitdir.is_absolute():
                gitdir = candidate / gitdir
            return gitdir.resolve().parent.parent.parent
    msg = 'clone principal nao encontrado'
    raise RuntimeError(msg)


def _registrados(main: Path) -> set[str]:
    """Caminhos absolutos dos worktrees registrados."""
    achados = {os.path.normcase(os.path.normpath(str(main)))}
    for gitdir in sorted((main / '.git' / 'worktrees').glob('*/gitdir')):
        alvo = Path(gitdir.read_text(encoding='utf-8').strip())
        if alvo.name == '.git':
            alvo = alvo.parent
        achados.add(os.path.normcase(os.path.normpath(str(alvo))))
    return achados


@pytest.mark.fast
def test_sem_worktrees_orfaos() -> None:
    """Toda pasta em `wt/` é um worktree registrado."""
    main = _main_root()
    wt = main / 'wt'
    if not wt.is_dir():
        pytest.skip('wt/ inexistente')
    registrados = _registrados(main)
    orfaos = [
        pasta.name
        for pasta in sorted(wt.iterdir())
        if pasta.is_dir()
        and os.path.normcase(os.path.normpath(str(pasta))) not in registrados
    ]
    assert not orfaos, f'worktrees orfaos: {orfaos}'

# AGENTS.md — regras do repositório

Regras para qualquer agente, pessoa ou IDE que trabalhe neste repositório.
Valem sobre preferências locais.

A fonte geral é o `AGENTS.md` do workspace MINIONS
(`C:\Users\brito\OpenBot\Agents\agent-adafc140-73c4-4872-9d03-b89872d70187\AGENTS.md`):
TDD, identidade de commit, rito de issues e git/merge. **Regras não se
duplicam** — o que não está aqui, vale o do workspace. Este arquivo registra
apenas o que é específico deste projeto.

## Escopo

- Ferramenta `incolume.py.changelog`: gera `CHANGELOG.md` a partir das anotações
  das tags.
- Pacote importável em `incolume/py/changelog/`; não mover para `src/`.
- `mkdocs.yml` usa tags `!!python/name:` (emojis do Material): o hook `check-yaml`
  roda com `args: [--unsafe]` (issue #177).

## Build e versionamento

Semver. A versão vive em `pyproject.toml` e só muda por `uv version`, nunca à mão.

- **O `uv version` não cobre `version.txt`.** Todo bump atualiza também:
  - `incolume/py/changelog/version.txt`.
- **Primeira tarefa de um ciclo:** `uv version --bump minor --bump alpha`.
- **Correção de bugs/fix apenas:** `uv version --bump patch --bump alpha`.
- **Cada tarefa concluída em `dev`:** `uv version --bump alpha` (`a1` → `a2` → …).
- **Fim de sprint:** `uv version --bump stable`.
- **O commit de versão fica sempre em `dev`**, nunca na branch da tarefa, e vem
  depois do merge: `git ci -m "build: $(uv version)"`.
- O commit de versão não fecha issue e não altera código.
- `CHANGELOG.md` é **gerado** por `uv run task changelog` (a partir das anotações
  das tags, `git tag -n`); nunca escrito à mão. O arquivo da raiz só aponta para
  `docs/about/CHANGELOG.md`. Regenerar no commit da versão estável.

## Qualidade

- Antes de commitar: `ruff check --fix tests incolume`,
  `ruff format tests incolume`, `mypy tests incolume`, `pytest tests incolume`.
- Cobertura mínima de 99.7% (`.coveragerc`).

## Git e entrega

- Merge sempre `--no-ff`.
- **Nunca faça merge cruzado.** Antes do merge, faça `git rebase dev` na
  branch — o merge parte do **HEAD de `dev`**.
- Conflito se resolve na branch, durante o rebase, nunca no commit de merge.

## Commits

- `<tipo>: #<issue> <descrição>` — português, minúscula, imperativa, sem ponto.
- Tipos: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`,
  `ci`, `chore`, `revert`.
- `docs:`, `chore:` e `refactor:` não fecham issue.

## Hooks

- `pre-commit` com `incolume.py.githooks`; instalar com `pre-commit install`.
- `task setup` configura `git config core.hooksPath .git-hooks/`.
- Worktree ligada: os hooks do githooks falham com `.git` arquivo — issues
  #386 e #387 do `incolume.py.githooks`. Por isso commits em `wt/` podem
  precisar de hooks desativados.

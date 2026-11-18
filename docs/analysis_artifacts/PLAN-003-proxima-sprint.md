# PLAN-003 — Próxima sprint: débitos de docs e CI

- **Data:** 2026-11-18
- **Projeto:** incolume.py.changelog
- **Versão do projeto:** 1.7.0
- **Status:** Proposta (aguardando revisão)
- **Autor:** Brito (Britodfbr)
- **Coautor:** Dr. Nefário OpenBot

## 0. Premissa

O `PLAN-002` foi concluído e a release `1.7.0` fechada. Restam débitos de
documentação e de CI.

## 1. Escopo

- Repositório: `incolume.py.changelog`.
- Objetivo: deixar o CI do `main` verde e limpar os resíduos de worktree.
- Fora do escopo: a issue #175 (Knowledge Bits) e a dívida de traduções.

## 2. Backlog

| Issue | Tema | Estado |
|---|---|---|
| #216 | docs — links quebrados | aberta |
| #217 | ci — tagged-release idempotente | aberta |
| #218 | chore — worktrees órfãos | aberta |
| #175 | Knowledge Bits | fora do plano |

## 3. Plano em sprints

| Sprint | Objetivo | Tarefas | Critério de aceite |
|---|---|---|---|
| **1 — Docs** | CI do `main` verde | #216 | validador de links sem quebrados |
| **2 — CI** | release idempotente | #217 | reexecução da tag não falha |
| **3 — Limpeza** | sem resíduos | #218 | `wt/` limpo |

## 4. Riscos e pendências

- O token `dev-incolume` segue read-only; as issues foram abertas em `britodfbr`.
- A dívida de traduções (PLAN-001/002) segue aberta.

## 5. Fora de escopo

- A issue #175 (Knowledge Bits).
- Tradução do `CHANGELOG` (gerado).
- Reescrita de código fora do necessário para as tarefas.

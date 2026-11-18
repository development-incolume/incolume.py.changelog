# PLAN-004 — Sprint: consolidação do taskipy e próximo ciclo

- **Data:** 2026-11-18
- **Projeto:** incolume.py.changelog
- **Versão do projeto:** 1.9.0a3
- **Status:** Proposta (aguardando revisão)
- **Autor:** Brito (Britodfbr)
- **Coautor:** Dr. Nefário OpenBot

## 0. Premissa

O `PLAN-003` foi concluído, a release `1.8.0` foi fechada e o `taskipy` foi
sanitizado (de 25 para 6 tasks). Este plano mapeia a sprint seguinte.

## 1. Estado

| Item | Valor |
|---|---|
| `dev` | `24d5bc9` — `1.9.0a3` |
| `tags` / `main` | `1.8.0` |
| Issues abertas | #175 |
| CI `main` (Docs Generator) | success |
| CI `dev` (Unit Tests) | success |

## 2. Taskipy atual (6 tasks)

| Task | Comando | Cobertura |
|---|---|---|
| `bandit` | `uv run --extra security bandit -c pyproject.toml -r {path}` | segurança |
| `safety` | `uv run --extra security safety check` | segurança |
| `pre_sec` / `sec` | agregador → `bandit` + `safety` | segurança |
| `test-all` | `uv run pytest -m "not webtest"` | testes |
| `setup` | `git config core.hooksPath .git-hooks/` | ambiente |

A QA canônica (`ruff check --fix`, `ruff format`, `mypy`, `ty check`,
`pytest -vvv`) roda por fora do `taskipy`.

## 3. Mapeamento da sprint

| Item | Tipo | Origem | Esforço |
|---|---|---|---|
| Tarefa de QA canônica (`qa`) | gap do taskipy | sanitização (#221/#222) | pequeno |
| Tarefa `ty` | gap do taskipy | sanitização (#221/#222) | pequeno |
| Fechar a release `1.9.0` | ciclo | `dev` em `a3` | pequeno |
| #175 — Knowledge Bits (Click config) | issue aberta | backlog | médio |
| Dívida de traduções (`glossario` só em pt) | dívida | PLAN-001/002 | médio |

## 4. Plano de ação

| Sprint | Objetivo | Tarefas | Critério de aceite |
|---|---|---|---|
| **1 — QA** | Uma task para a QA canônica | `qa`, `ty` | `uv run task qa` executa ruff + mypy + ty + pytest |
| **2 — Release** | Fechar `1.9.0` | — | fluxo `dev → tags → main` com release publicada |
| **3 — Produto** | #175 (se o usuário quiser) | #175 | a decidir |
| **4 — Docs** | traduções pendentes | `glossario` | pt/de/en/es/fr/it |

## 5. Riscos e pendências

- O token `dev-incolume` segue read-only; as issues foram abertas em `britodfbr`.
- A QA canônica não tem task; o `taskipy` cobre só `bandit`, `safety`, `test-all` e `setup`.

## 6. Fora de escopo

- Reescrita de código fora do necessário para as tarefas.
- Tradução do `CHANGELOG` (gerado).

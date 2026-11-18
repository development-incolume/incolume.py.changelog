# PLAN-004 — Sprint: consolidação do taskipy e próximo ciclo

- **Data:** 2026-11-18
- **Projeto:** incolume.py.changelog
- **Versão do projeto:** 1.9.0
- **Status:** Em andamento (sprints 1–2 concluídas)
- **Autor:** Brito (Britodfbr)
- **Coautor:** Dr. Nefário OpenBot

## 0. Premissa

O `PLAN-003` foi concluído, a release `1.9.0` foi fechada e o `taskipy` foi
sanitizado (de 25 para 8 tasks). Este plano mapeia a sprint em curso.

## 1. Estado

| Item | Valor |
|---|---|
| `dev` | `f1733d6` — `1.9.0` |
| `tags` / `main` | `1.9.0` |
| Issues abertas | #175, #226 |
| CI `main` (Docs Generator) | success |
| CI `dev` (Unit Tests) | success |

## 2. Taskipy atual (8 tasks)

| Task | Comando | Cobertura |
|---|---|---|
| `bandit` | `uv run --extra security bandit -c pyproject.toml -r {path}` | segurança |
| `safety` | `uv run --extra security safety check` | segurança |
| `pre_sec` / `sec` | agregador → `bandit` + `safety` | segurança |
| `ty` | `uv run ty check {path}` | tipos |
| `qa` | ruff check --fix + ruff format + mypy + ty check + pytest -vvv | QA canônica |
| `test-all` | `uv run pytest -m "not webtest"` | testes |
| `setup` | `git config core.hooksPath .git-hooks/` | ambiente |

## 3. Mapeamento da sprint

| Item | Tipo | Origem | Esforço |
|---|---|---|---|
| Tarefa de QA canônica (`qa`) | gap do taskipy | sanitização (#221/#222) | ✓ #224 |
| Tarefa `ty` | gap do taskipy | sanitização (#221/#222) | ✓ #224 |
| Fechar a release `1.9.0` | ciclo | `dev` em `a3` | ✓ release publicada |
| #175 — Knowledge Bits (Click config) | issue aberta | backlog | fora |
| Dívida de traduções (`glossario`, `contributing`) | dívida | PLAN-001/002 | #226 |

## 4. Plano de ação

| Sprint | Objetivo | Tarefas | Critério de aceite |
|---|---|---|---|
| **1 — QA** | Uma task para a QA canônica | `qa`, `ty` | ✓ concluída (#224) |
| **2 — Release** | Fechar `1.9.0` | — | ✓ concluída (release publicada) |
| **3 — Produto** | #175 (se o usuário quiser) | #175 | fora |
| **4 — Docs** | traduções pendentes | `glossario`, `contributing` (#226) | pt/de/en/es/fr/it |

## 5. Riscos e pendências

- O token `dev-incolume` segue read-only; as issues foram abertas em `britodfbr`.
- A QA canônica tem task (`qa`); `ty` isolado também.

## 6. Fora de escopo

- Reescrita de código fora do necessário para as tarefas.
- Tradução do `CHANGELOG` (gerado).

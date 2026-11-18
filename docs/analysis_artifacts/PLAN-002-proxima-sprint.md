# PLAN-002 — Próxima sprint: backlog técnico e documentação

- **Data:** 2026-11-17
- **Projeto:** incolume.py.changelog
- **Versão do projeto:** 1.6.0
- **Status:** Proposta (aguardando revisão)
- **Autor:** Brito (Britodfbr)
- **Coautor:** Dr. Nefário OpenBot

## 0. Premissa

O `PLAN-001` (melhoria da documentação) foi concluído e a release `1.6.0` foi
fechada. Restou backlog técnico e de documentação. Este plano organiza esse
backlog em sprints, sem agrupar tarefas numa issue só: cada tarefa do plano
tem a sua issue, branch e critério de aceite.

## 1. Escopo

- Repositório: `incolume.py.changelog`.
- Objetivo: zerar o backlog técnico e deixar a documentação coerente com o
  repositório em `1.6.0`.
- Fora do escopo: a issue #175 (Knowledge Bits), conforme decisão do usuário.

## 2. Backlog

| Issue | Tema | Estado |
|---|---|---|
| #203 | QA e esteira | aberta |
| #204 | Documentação — `[tool.poetry]` obsoleto | aberta |
| #205 | Release — workflow | aberta |
| #206 | Documentação — PLAN-001 | aberta |
| #210 | i18n — seletor de idiomas | aberta |
| #192 | i18n residual — T2.7 | aberta |
| #175 | Knowledge Bits (Click config) | fora do plano |

## 3. Plano em sprints

| Sprint | Objetivo | Tarefas | Critério de aceite |
|---|---|---|---|
| **1 — QA e esteira** | Uma fonte única para os comandos de QA e CI que valida em vez de corrigir | #203 | Um único conjunto de comandos documentado; `AGENTS.md`, SPEC-001, `tox` e CI alinhados; `tox -e lint` e `tox -e typing` coerentes |
| **2 — Documentação** | Artefatos coerentes com a versão `1.6.0` | #204; atualizar versão/status dos artefatos (`PRD-001`, `ADR-001`, `SPEC-001`, `PLAN-001`) para `1.6.0`; fechar #206 | Artefatos com versão `1.6.0`; nenhum documento manda espelhar versão em `[tool.poetry]`; #206 encerrada |
| **3 — Release** | Workflow de release alinhado ao ADR-001 AD-09 | #205 | Workflow dispara em `dev` e em PR; actions na versão atual; release não marcada indevidamente como `prerelease` |
| **4 — i18n** | Revisão textual das traduções e seletor de idiomas no site | #192, #210 | Traduções (de/en/es/fr/it) revisadas por idioma; links de idioma corrigidos no site |

## 4. Riscos e pendências

- A CI aplica `ruff check --fix` e `ruff format` sem `--check`, modificando a
  árvore em vez de validar (#203).
- A GitHub Release `1.6.0` foi criada com `prerelease: true`, pois o workflow
  define `prerelease: true` sempre (#205).
- O `AGENTS.md` do repo ainda manda ajustar `[tool.poetry] version` no commit de
  versão (#204).
- A issue #192 é dívida residual do PLAN-001 e segue aberta.

## 5. Fora de escopo

- Tradução do `CHANGELOG` (gerado).
- Mudança de versão, release ou publicação.
- A issue #175 (Knowledge Bits).
- Reescrita de código fora do necessário para as tarefas.

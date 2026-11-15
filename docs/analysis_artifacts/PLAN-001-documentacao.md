# PLAN-001 — Plano de melhoria da documentação

- **Data:** 2026-11-14
- **Projeto:** incolume.py.changelog
- **Versão do projeto:** 1.5.0
- **Status:** Proposta (aguardando revisão)
- **Autor:** Brito (Britodfbr)
- **Coautor:** Dr. Nefário OpenBot

## 0. Premissa

O `CHANGELOG.md` é **saída do próprio `incolume.py.changelog`**, gerado a
partir das anotações das tags (`git tag -n`). Ele **nunca** é editado à mão e
não é traduzido arquivo a arquivo. Toda correção de conteúdo do CHANGELOG
passa por corrigir o gerador (ou a anotação da tag) e regerar com
`uv run task changelog`.

Consequência verificada: o `docs/about/CHANGELOG.md` commitado na `1.5.0`
saiu com mojibake (`repositÃ³rio`, `SerÃ¡`) porque a leitura de
`subprocess.getoutput('git tag -n')` usa o locale da máquina. Rodando a
ferramenta neste ambiente, a saída é UTF-8 correta. O defeito, portanto, é do
caminho de leitura do gerador — não do arquivo.

## 1. Escopo

- Repositório: `incolume.py.changelog`.
- Documentação varrida: `README.md`, `docs/**` (mkdocs), `mkdocs.yml`,
  `.github/workflows/*.yml`, `.pre-commit-config.yaml`, `.changelog.toml`,
  `tox.toml`, `pyproject.toml` (como fonte de verdade).
- Idiomas propostos no `mkdocs.yml` (i18n): **pt (default), en, de, es, fr, it**.

## 2. Inventário e cobertura por idioma

| Documento | pt | en | de | es | fr | it | Estado |
|---|---|---|---|---|---|---|---|
| `README.md` (repo) | ✓ | — | — | — | — | — | desatualizado |
| `docs/index.md` | ✓ | — | — | — | — | — | desatualizado |
| `docs/api/index.md` | ✓ | — | — | — | — | — | incompleto |
| `user_guide/README.md` | ✓ | — | — | — | — | — | órfão (fora do nav) |
| `user_guide/development.md` | ✓ | vazio | vazio | vazio | vazio | vazio | desatualizado |
| `user_guide/INSTALLATION` | — | ✓ | — | — | — | — | conteúdo errado/órfão |
| `user_guide/usage` | — | ✓ | — | — | — | — | conteúdo alheio |
| `user_guide/markdown.md` | ✓ | — | — | — | — | — | conteúdo alheio |
| `user_guide/code_of_conduct` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ok |
| `user_guide/COVENTIONAL_COMMITS` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | divergente (en 84 × pt 31 linhas) |
| `user_guide/keep-a-changelog` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ok |
| `user_guide/semver` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ok |
| `user_guide/writing-your-docs` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | genérico (template mkdocs) |
| `user_guide/zenpy` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ok |
| `about/CONTRIBUTORS` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ok |
| `about/LICENSE` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ok |
| `about/CHANGELOG` | ✓ | — | — | — | — | — | gerado (com mojibake na 1.5.0) |

## 3. Achados

### A. Conteúdo errado ou de outro projeto

- `user_guide/markdown.md` (992 linhas): é o template do
  **coding-dojo / `incolume.py.model-2023-07-05`**, não um guia de Markdown.
- `user_guide/usage.en.md` (412 linhas): o mesmo template, em inglês.
- `user_guide/INSTALLATION.en.md`: título "Guia de Uso", mistura pt/en, fixa
  a versão `1.0.0` e aponta links errados (`user_guide/api/index.md`,
  `user_guide/user_guide/development.md`).

### B. Vazios

- `user_guide/development.{en,de,es,fr,it}.md` — **0 bytes**.

### C. Desatualizado

- `development.md`: Python 3.10 (o projeto é `>=3.11,<4`); cita
  `black/blue/isort/pydocstyle/pylint/flake8/pylama` (removidos); cita
  `Makefile` (inexistente no repo); tox `py310,py311` (real: 3.11–3.14);
  caminhos `incolumepy/`.
- `README.md`: `uv pip add` (comando inexistente); pin `==0.15.0` e `==1.0.0`;
  `uv venv -p 3.10`; badge do codecov com `]((https://…` quebrado.
- `docs/index.md`: typo "resgistros"; cita `pylint/isort/pydocstyle`; typo
  "Contribuíção".
- `about/CHANGELOG.md`: mojibake (UTF-8 duplo) após a regeneração da 1.5.0.

### D. Faltando

- `docs/api/index.md` só documenta `changelog` e `cli`; faltam `core` e
  `__init__`, e não há exemplos de uso.
- `docs/analysis_artifacts/` existe e está **vazio**.
- Sem `README.md` em en/de/es/fr/it.
- `nav` do mkdocs não expõe `development`, `INSTALLATION`, `usage`,
  `user_guide/README`.
- `nav_translations`: en/es/fr/it sem `Conventional Commit` e
  `Keep a CHANGELOG`; nenhum idioma traduz `MarkDown`, `Mkdocs`, `Semver`,
  `Zen Python`.

### E. Infraestrutura de docs

- `.github/workflows/docs_ci_cd.yml` roda `uv sync` **sem o grupo `doc`** →
  `mkdocs` não instalado → `Failed to spawn: mkdocs` (deploy falha desde
  ago/2026; o site publicado está parado).
- `.github/workflows/multplatform-ci-cd.yml`: `Tagged Release` não aceita tag
  PEP 440 (`1.5.0a6`) — a release do GitHub não é criada.

### F. i18n

- Seis locales configurados; apenas 3 documentos com tradução completa;
  o fallback pt encobre as lacunas.

## 4. Proposta de melhoria

1. **Uma fonte de verdade por documento**, pt-BR como default e demais
   idiomas como tradução — sem fallback silencioso para conteúdo específico
   do projeto.
2. Separar **referência genérica** (semver, keep-a-changelog, conventional,
   zenpy) de **guia do projeto** (development, installation, usage, api), que
   tem de ser 100% específico.
3. **Acionável**: todo comando e versão precisa bater com `pyproject.toml`,
   `tox.toml` e os workflows reais.
4. **Automatizar**: CI de docs que instala o grupo `doc` e valida links e
   encoding antes do deploy.
5. **Navegação completa**: todo `.md` de `docs/` ou está no `nav` ou é
   removido.
6. **CHANGELOG é gerado**: nenhuma tarefa prevê edição ou tradução manual.

## 5. Plano em sprints

| Sprint | Objetivo | Tarefas | Idiomas | Critério de aceite |
|---|---|---|---|---|
| **0 — Crítico** (1 dia) | Parar a sangria | T0.1 corrigir a leitura UTF-8 do gerador (teste vermelho com locale latin-1) e regerar `CHANGELOG.md` via `uv run task changelog`; T0.2 corrigir `docs_ci_cd.yml` (`uv sync --all-groups`, actions atuais); T0.3 corrigir `README.md`; T0.4 corrigir `docs/index.md` | pt | CI de docs verde; CHANGELOG sem mojibake; README sem links/comandos quebrados |
| **1 — Conteúdo base pt** (3–5 dias) | Docs do projeto corretos | T1.1 reescrever `markdown.md`; T1.2 reescrever `usage.md`; T1.3 criar `INSTALLATION.md` (pt) e remover o `.en` errado; T1.4 reescrever `development.md`; T1.5 documentar `api/index.md` (`core`, `__init__`, exemplos); T1.6 decidir `analysis_artifacts` (criar PRD/ADR/SPEC ou remover); T1.7 ajustar o `nav` | pt | Cada doc existente no nav; nenhum template alheio; comandos verificados |
| **2 — i18n** (5–7 dias) | Seis idiomas completos | T2.1 traduzir `index.md`; T2.2 traduzir `markdown`, `development`, `INSTALLATION`, `usage`, `api/index`, `user_guide/README`; T2.3 preencher `development.*` vazios; T2.4 completar `nav_translations`; T2.5 revisar divergência `COVENTIONAL_COMMITS.en` | de/en/es/fr/it | Matriz 100% sem arquivos vazios; nav traduzida |
| **3 — Qualidade** (3–5 dias) | Sustentável | T3.1 validação de links/encoding no CI; T3.2 padronizar URLs sem `.md`; T3.3 exemplos de API testáveis; T3.4 guia de contribuição (mkdocs/i18n/tags) nos seis idiomas; T3.5 publicar e conferir o site | todos | Deploy verde; site refletindo o repo |

## 6. Riscos e pendências

- O site de docs está parado desde ago/2026 (Sprint 0 destrava).
- A qualidade fim a fim das traduções existentes não foi revisada
  (amostragem apenas).
- O conteúdo interno de `core.py` ainda não foi mapeado para detalhar a API.
- O repo moveu concorrentemente durante a auditoria (estável `1.5.0` em
  `27737be`); o plano assume esse HEAD.

## 7. Fora de escopo

- Tradução do `CHANGELOG.md` (gerado).
- Mudança de versão, release ou publicação.
- Reescrita de código fora do gerador de changelog.

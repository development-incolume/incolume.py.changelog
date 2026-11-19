# Glossário Técnico

Repositório de termos técnicos usados na documentação do
`incolume.py.changelog`.

Este arquivo serve como **glossário** (top-100 termos do projeto), organizados
por categoria, com a definição e o local onde o termo aparece na documentação.

> Última atualização: 2026-11-16
> Versão do produto: 1.6.0a11 (dev)

---

## Arquitetura e Geração

| Termo | Definição |
|---|---|
| **mkdocs** | Ferramenta estática de geração de documentação em HTML a partir de arquivos Markdown. |
| **mkdocstrings** | Plugin do MkDocs que gera documentação de API automaticamente a partir de docstrings do código Python. |
| **material** | Tema Material para MkDocs (site moderno, dark/light mode, paleta de cores). |
| **i18n** | Internacionalização — múltiplos idiomas (pt-BR, en, de, es, fr, it). |
| **nav_translations** | Mapeamento de títulos de navegação para cada idioma no `mkdocs.yml`. |
| **gh-deploy** | Comando do MkDocs que publica a documentação no branch `webdoc` ou GitHub Pages. |
| **webdoc** | Branch de integração usada para publicação do site gerado via `gh-deploy`. |
| **CHANGELOG.md** | Arquivo de registro de mudanças seguindo o padrão Keep a Changelog. |
| **ADR** | Architecture Decision Record — documento que registra decisões arquiteturais. |
| **PRD** | Product Requirements Document — documento de requisitos do produto. |
| **SPEC** | Specification — documento de execução/especificação técnica. |
| **PLAN-001** | Plano de melhoria da documentação — documento de planejamento da sprint. |
| **CI/CD** | *Continuous Integration / Continuous Deployment* — integração e entrega contínuas. |
| **GitHub Pages** | Serviço hospedado pelo GitHub para publicação de sites estáticos. |
| **uv** | Gerenciador de dependências e montador de projetos Python (alternativa a `pip`). |
| **taskipy** | Executador de tarefas (`task`) inspirado no `npm scripts`; usado para customizar a CLI. |

---

## Metodologias e Processo

| Termo | Definição |
|---|---|
| **Keep a Changelog** | Especificação aberta para o formato de arquivos `CHANGELOG.md`. |
| **Semantic Versioning (SemVer)** | Regras para versionamento `MAJOR.MINOR.PATCH` com `rc`, `alpha`, etc. |
| **Conventional Commits** | Especificação de mensagens de commit com prefixes (`feat:`, `fix:`, `chore:`). |
| **TDD** | *Test-Driven Development* — desenvolvimento guiado por testes (vermelho → verde → refatorar). |
| **AC** | *Acceptance Criteria* — critério de aceite de uma issue/task. |
| **P0 / P1 / P2** | Níveis de prioridade: crítico, alto, médio. |
| **Sprint** | Ciclo de entrega (geralmente 1–2 semanas) com issues previamente planejadas. |
| **Worktree** | Diretório de trabalho isolado derivado de uma branch. |
| **Rebase** | Técnica de integração que reaplica commits para cima de outra branch. |
| **Fast-forward / Merge --no-ff** | Estratégias de merge de branch; aqui usa-se `--no-ff` para manter a história de tarefas. |

---

## Qualidade e Validação

| Termo | Definição |
|---|---|
| **ruff** | Linter e formatador moderno em Python (substituto de `flake8`, `black`, `isort`). |
| **mypy** | Checador estático de tipos (type checker) em Python. |
| **pytest** | Framework de testes unitários em Python. |
| **coverage 99,7%** | Cobertura mínima de código necessária nos testes (regra de qualidade). |
| **Strict mode** | Modo de validação máxima do MkDocs (quebra em warnings). |
| **broken link** | Link interno que aponta para arquivo inexistente. |
| **UTF-8 strict** | Validação de encoding UTF-8 sem substituição de caracteres inválidos. |
| **mojibake** | Texto corrompido por erro de codificação (ex.: `Ã£` em vez de `ã`). |
| **HTML entity** | Representação de caracteres especiais usando sua codificação numérica (ex.: `&amp;`). |
| **Badge** | Ícone visual em Markdown com status (CI verde, version, etc.) via serviços externos. |

---

## Entregas e Publicação

| Termo | Definição |
|---|---|
| **publish** | Processo de subir a documentação gerada para o servidor de hospedagem. |
| **site_name** | Título exibido no cabeçalho do site gerado. |
| **edit_uri** | URI usada para edição direta de páginas pelo GitHub. |
| **edit_uri: tree/branch/docs** | Padrão usado para gerar links de edição no GitHub. |
| **theme** | Visual e layout do site (aqui: `material`). |
| **light/dark mode** | Suporte a modo claro e escuro via paleta do Material. |
| **sidebar** | Barra lateral com navegação progressiva pelos tópicos. |
| **permalink** | URL permanente de uma seção (gera âncoras automáticas). |
| **autolink** | Cria âncoras automáticas a partir de cabeçalhos. |
| **emoji** |Extensão que permite usar emojis no Markdown. |
| **pagetocat** | Gera uma tabela de conteúdo (TOC) no topo da página. |
| **toc permalink** | Permite clicar no ícone do link para ir a um cabeçalho. |

---

## Variáveis Ambientes e Arquivos de Configuração

| Termo | Definição |
|---|---|
| **pyproject.toml** | Arquivo de configuração do pacote Python (PEP 621): dependências, version, scripts. |
| **uv.lock** | Lockfile do `uv` com versões exatas de todas as dependências. |
| **tox.ini / pyproject.toml [tool.tox]** | Configuração de múltiplas versões Python e ambientes de teste. |
| **.changelog.toml** | Arquivo de configuração opcional do gerador de CHANGELOG. |
| **version.txt** | Arquivo que guarda a versão atual do pacote em runtime. |
| **.gitattributes** | Define como o Git trata os arquivos no repositório. |
| **CI/CD workflow** | Script do GitHub Actions (`.github/workflows/*.yml`). |
| **pre-commit** | Hook git executado antes de cada commit (qualidade de código). |
| **environment** | Ambiente isolado Python (`.venv/`), gerenciado via `uv`. |
| **coverage_report** | Diretório com relatório HTML de cobertura de testes. |
| **docs/** | Diretório raiz da documentação em Markdown. |
| **incolume/**, **src/** | Código-fonte Python do pacote. |

---

## Comandos Úteis

| Termo | Definição |
|---|---|
| `uv sync` | Sincroniza o ambiente virtual com `uv.lock` e instala dependências. |
| `uv run` | Executa um comando dentro do ambiente ativado. |
| `uv run task setup` | Configura os hooks do git (`core.hooksPath`). |
| `uv run task -l` | Lista todas as tarefas disponíveis (`taskipy`). |
| `uv run ruff check` | Executa o linter. |
| `uv run ruff format` | Formata o código. |
| `uv run mypy` | Verifica tipos estáticos. |
| `uv run pytest` | Executa a suíte de testes. |
| `uv run mkdocs build` | Gera a documentação em `_site/` (ou `site/`). |
| `uv run mkdocs serve` | Serve a documentação em localhost. |
| `uv run mkdocs gh-deploy --remote-branch webdoc` | Publica a documentação no GitHub Pages (`webdoc`). |
| `uv run tox` | Roda a matriz de testes multi-versão. |
| `uv run gcl` | Gera ou atualiza o `CHANGELOG.md`. |
| `git tag -n` | Lista tags com anotações; fonte das versões no CHANGELOG. |
| `uv version` | Incrementa a versão do pacote (veja [semver.org](https://semver.org)). |
| `git worktree` | Gerencia diretórios de trabalho múltiplos do repositório. |

---

## Glossário por Frequência (Top)

Ordenados pela frequência relativa na documentação.

| Termo | Ocorrências | Contexto típico |
|---|---|---|
| **Markdown** | 226 | Formato de documentação, extensão `.md`. |
| **CHANGELOG** | 137 | Registro de mudanças, arquivo `CHANGELOG.md`. |
| **Python** | 102 | Linguagem de programação principal. |
| **API** | 96 | Interface de programação de aplicações. |
| **URL** | 99 | Localizador de recursos na web. |
| **GitHub** | 44 | Plataforma de hospedagem de código. |
| **CI/CD** | 45 | Integração/continua entrega. |
| **Issue** | — | Tarefa ou bug rastreado no tracker do projeto. |
| **AC** | — | *Acceptance Criteria* — critério de aceite. |
| **README** | — | Documentação inicial do repositório. |
| **Versioning** | — | Gerenciamento de versões (`MAJOR.MINOR.PATCH`). |
| **Conventional Commit** | — | Especificação de mensagens de commit. |
| **Keep a Changelog** | — | Padrão para formatação de `CHANGELOG.md`. |
| **Semantic Versioning** | — | Regras `MAJOR.MINOR.PATCH`. |
| **SemVer** | — | Abreviatura de Semantic Versioning. |
| **MkDocs** | — | Ferramenta de geração de site estático. |
| **material** | — | Tema Material para MkDocs. |
| **i18n** | — | Internacionalização. |
| **nav_translations** | — | Mapeamento de títulos de navegação por idioma. |
| **gh-deploy** | — | Comando de publicação do MkDocs. |
| **webdoc** | — | Branch de integração para GitHub Pages. |
| **uv** | — | Gerenciador de dependências e montador. |
| **taskipy** | — | Executador de tarefas. |
| **ruff** | — | Linter e formatador em Python. |
| **mypy** | — | Verificador estático de tipos. |
| **pytest** | — | Framework de testes. |
| **coverage** | — | Cobertura de código em testes. |
| **UnicodeDecodeError** | — | Erro de encoding ao ler arquivo. |
| **mojibake** | — | Texto corrompido por erro de codificação. |
| **toctoc** | — | Tabela de conteúdo automática. |
| **ACR** | — | *Acceptance Criteria Rule* — regra de aceite. |

---

## Referências

- [Keep a Changelog](https://keepachangelog.com/en/1.0.0)
- [Semantic Versioning](https://semver.org/spec/v2.0.0.html)
- [Conventional Commits](https://www.conventionalcommits.org/pt-br/v1.0.0)
- [MkDocs](https://www.mkdocs.org)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [MkDocs i18n Plugin](https://mkdocs-material.squidfunk.com/configuration/i18n/)
- [GitHub Pages](https://pages.github.com)

---

*Fonte: revisão da documentação de `incolume.py.changelog` (v1.6.0a11, dev).*

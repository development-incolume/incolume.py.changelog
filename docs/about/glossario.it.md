# Glossario tecnico

Archivio di termini tecnici usati nella documentazione di
`incolume.py.changelog`.

Questo file funge da **glossario** (i 100 termini più usati del progetto),
organizzati per categoria, con la definizione e il punto della documentazione
in cui compare il termine.

> Ultimo aggiornamento: 2026-11-16

---

## Architettura e generazione

| Termine | Definizione |
|---|---|
| **mkdocs** | Strumento statico per la generazione di documentazione HTML a partire da file Markdown. |
| **mkdocstrings** | Plugin di MkDocs che genera automaticamente la documentazione delle API a partire dalle docstring del codice Python. |
| **material** | Tema Material per MkDocs (sito moderno, modalità chiara/scura, palette di colori). |
| **i18n** | Internazionalizzazione — più lingue (pt-BR, en, de, es, fr, it). |
| **nav_translations** | Mappatura dei titoli di navigazione per ciascuna lingua in `mkdocs.yml`. |
| **gh-deploy** | Comando di MkDocs che pubblica la documentazione sul branch `webdoc` o su GitHub Pages. |
| **webdoc** | Branch di integrazione usato per la pubblicazione del sito generato tramite `gh-deploy`. |
| **CHANGELOG.md** | File di registro delle modifiche conforme allo standard Keep a Changelog. |
| **ADR** | Architecture Decision Record — documento che registra le decisioni architetturali. |
| **PRD** | Product Requirements Document — documento dei requisiti del prodotto. |
| **SPEC** | Specification — documento di esecuzione/specifica tecnica. |
| **PLAN-001** | Piano di miglioramento della documentazione — documento di pianificazione della sprint. |
| **CI/CD** | *Continuous Integration / Continuous Deployment* — integrazione e distribuzione continue. |
| **GitHub Pages** | Servizio ospitato da GitHub per la pubblicazione di siti statici. |
| **uv** | Gestore di dipendenze e strumento di build per progetti Python (alternativa a `pip`). |
| **taskipy** | Esecutore di attività (`task`) ispirato agli `npm scripts`; usato per personalizzare la CLI. |

---

## Metodologie e processo

| Termine | Definizione |
|---|---|
| **Keep a Changelog** | Specifica aperta per il formato dei file `CHANGELOG.md`. |
| **Semantic Versioning (SemVer)** | Regole per il versionamento `MAJOR.MINOR.PATCH` con `rc`, `alpha`, ecc. |
| **Conventional Commits** | Specifica dei messaggi di commit con prefissi (`feat:`, `fix:`, `chore:`). |
| **TDD** | *Test-Driven Development* — sviluppo guidato dai test (rosso → verde → rifattorizzare). |
| **AC** | *Acceptance Criteria* — criterio di accettazione di una issue/attività. |
| **P0 / P1 / P2** | Livelli di priorità: critico, alto, medio. |
| **Sprint** | Ciclo di consegna (in genere 1–2 settimane) con issue pianificate in anticipo. |
| **Worktree** | Directory di lavoro isolata derivata da un branch. |
| **Rebase** | Tecnica di integrazione che riapplica i commit al di sopra di un altro branch. |
| **Fast-forward / Merge --no-ff** | Strategie di merge tra branch; qui si usa `--no-ff` per preservare la cronologia delle attività. |

---

## Qualità e validazione

| Termine | Definizione |
|---|---|
| **ruff** | Linter e formattatore moderno per Python (sostituto di `flake8`, `black`, `isort`). |
| **mypy** | Controllore statico dei tipi (type checker) per Python. |
| **pytest** | Framework di test unitari in Python. |
| **coverage 99,7%** | Copertura minima di codice richiesta nei test (regola di qualità). |
| **Strict mode** | Modalità di validazione massima di MkDocs (interrompe in caso di warning). |
| **broken link** | Link interno che punta a un file inesistente. |
| **UTF-8 strict** | Validazione della codifica UTF-8 senza sostituzione dei caratteri non validi. |
| **mojibake** | Testo corrotto da un errore di codifica (es.: `Ã£` invece di `ã`). |
| **HTML entity** | Rappresentazione dei caratteri speciali tramite la loro codifica numerica (es.: `&amp;`). |
| **Badge** | Icona visiva in Markdown con lo stato (CI verde, versione, ecc.) tramite servizi esterni. |

---

## Consegne e pubblicazione

| Termine | Definizione |
|---|---|
| **publish** | Processo di caricamento della documentazione generata sul server di hosting. |
| **site_name** | Titolo mostrato nell'intestazione del sito generato. |
| **edit_uri** | URI usata per la modifica diretta delle pagine tramite GitHub. |
| **edit_uri: tree/branch/docs** | Schema usato per generare i link di modifica su GitHub. |
| **theme** | Aspetto e layout del sito (qui: `material`). |
| **light/dark mode** | Supporto alla modalità chiara e scura tramite la palette di Material. |
| **sidebar** | Barra laterale con navigazione progressiva tra gli argomenti. |
| **permalink** | URL permanente di una sezione (genera ancore automatiche). |
| **autolink** | Crea ancore automatiche a partire dalle intestazioni. |
| **emoji** | Estensione che consente di usare le emoji in Markdown. |
| **pagetocat** | Genera una tabella dei contenuti (TOC) in cima alla pagina. |
| **toc permalink** | Consente di fare clic sull'icona dell'ancora per andare a un'intestazione. |

---

## Variabili d'ambiente e file di configurazione

| Termine | Definizione |
|---|---|
| **pyproject.toml** | File di configurazione del pacchetto Python (PEP 621): dipendenze, versione, script. |
| **uv.lock** | Lockfile di `uv` con le versioni esatte di tutte le dipendenze. |
| **tox.ini / pyproject.toml [tool.tox]** | Configurazione di versioni Python multiple e ambienti di test. |
| **.changelog.toml** | File di configurazione opzionale del generatore di CHANGELOG. |
| **version.txt** | File che conserva la versione attuale del pacchetto in runtime. |
| **.gitattributes** | Definisce come Git tratta i file nel repository. |
| **CI/CD workflow** | Script di GitHub Actions (`.github/workflows/*.yml`). |
| **pre-commit** | Hook git eseguito prima di ogni commit (qualità del codice). |
| **environment** | Ambiente Python isolato (`.venv/`), gestito tramite `uv`. |
| **coverage_report** | Directory con il report HTML di copertura dei test. |
| **docs/** | Directory radice della documentazione in Markdown. |
| **incolume/**, **src/** | Codice sorgente Python del pacchetto. |

---

## Comandi utili

| Termine | Definizione |
|---|---|
| `uv sync` | Sincronizza l'ambiente virtuale con `uv.lock` e installa le dipendenze. |
| `uv run` | Esegue un comando nell'ambiente attivato. |
| `uv run task setup` | Configura gli hook di git (`core.hooksPath`). |
| `uv run task -l` | Elenca tutte le attività disponibili (`taskipy`). |
| `uv run ruff check` | Esegue il linter. |
| `uv run ruff format` | Formatta il codice. |
| `uv run mypy` | Verifica i tipi statici. |
| `uv run pytest` | Esegue la suite di test. |
| `uv run mkdocs build` | Genera la documentazione in `_site/` (o `site/`). |
| `uv run mkdocs serve` | Serve la documentazione in localhost. |
| `uv run mkdocs gh-deploy --remote-branch webdoc` | Pubblica la documentazione su GitHub Pages (`webdoc`). |
| `uv run tox` | Esegue la matrice di test multi-versione. |
| `uv run gcl` | Genera o aggiorna `CHANGELOG.md`. |
| `git tag -n` | Elenca i tag con annotazioni; fonte delle versioni nel CHANGELOG. |
| `uv version` | Incrementa la versione del pacchetto (vedi [semver.org](https://semver.org)). |
| `git worktree` | Gestisce directory di lavoro multiple del repository. |

---

## Glossario per frequenza (top)

Ordinati per frequenza relativa nella documentazione.

| Termine | Occorrenze | Contesto tipico |
|---|---|---|
| **Markdown** | 226 | Formato di documentazione, estensione `.md`. |
| **CHANGELOG** | 137 | Registro delle modifiche, file `CHANGELOG.md`. |
| **Python** | 102 | Linguaggio di programmazione principale. |
| **API** | 96 | Interfaccia di programmazione delle applicazioni. |
| **URL** | 99 | Localizzatore di risorse sul web. |
| **GitHub** | 44 | Piattaforma di hosting del codice. |
| **CI/CD** | 45 | Integrazione/distribuzione continua. |
| **Issue** | — | Attività o bug tracciato nel tracker del progetto. |
| **AC** | — | *Acceptance Criteria* — criterio di accettazione. |
| **README** | — | Documentazione iniziale del repository. |
| **Versioning** | — | Gestione delle versioni (`MAJOR.MINOR.PATCH`). |
| **Conventional Commit** | — | Specifica dei messaggi di commit. |
| **Keep a Changelog** | — | Standard per la formattazione di `CHANGELOG.md`. |
| **Semantic Versioning** | — | Regole `MAJOR.MINOR.PATCH`. |
| **SemVer** | — | Abbreviazione di Semantic Versioning. |
| **MkDocs** | — | Strumento di generazione di siti statici. |
| **material** | — | Tema Material per MkDocs. |
| **i18n** | — | Internazionalizzazione. |
| **nav_translations** | — | Mappatura dei titoli di navigazione per lingua. |
| **gh-deploy** | — | Comando di pubblicazione di MkDocs. |
| **webdoc** | — | Branch di integrazione per GitHub Pages. |
| **uv** | — | Gestore di dipendenze e strumento di build. |
| **taskipy** | — | Esecutore di attività. |
| **ruff** | — | Linter e formattatore per Python. |
| **mypy** | — | Verificatore statico dei tipi. |
| **pytest** | — | Framework di test. |
| **coverage** | — | Copertura del codice nei test. |
| **UnicodeDecodeError** | — | Errore di codifica durante la lettura di un file. |
| **mojibake** | — | Testo corrotto da un errore di codifica. |
| **toctoc** | — | Tabella dei contenuti automatica. |
| **ACR** | — | *Acceptance Criteria Rule* — regola di accettazione. |

---

## Riferimenti

- [Keep a Changelog](https://keepachangelog.com/en/1.0.0)
- [Semantic Versioning](https://semver.org/spec/v2.0.0.html)
- [Conventional Commits](https://www.conventionalcommits.org/pt-br/v1.0.0)
- [MkDocs](https://www.mkdocs.org)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [MkDocs i18n Plugin](https://mkdocs-material.squidfunk.com/configuration/i18n/)
- [GitHub Pages](https://pages.github.com)

---

*Fonte: revisione della documentazione di `incolume.py.changelog` (v1.6.0a11, dev).*

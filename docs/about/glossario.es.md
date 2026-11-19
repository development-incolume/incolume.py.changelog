# Glosario Técnico

Repositorio de términos técnicos usados en la documentación de
`incolume.py.changelog`.

Este archivo sirve como **glosario** (top-100 términos del proyecto), organizados
por categoría, con la definición y el lugar donde aparece el término en la documentación.

> Última actualización: 2026-11-16
> Versión del producto: 1.6.0a11 (dev)

---

## Arquitectura y Generación

| Término | Definición |
|---|---|
| **mkdocs** | Herramienta estática de generación de documentación en HTML a partir de archivos Markdown. |
| **mkdocstrings** | Plugin de MkDocs que genera documentación de API automáticamente a partir de los docstrings del código Python. |
| **material** | Tema Material para MkDocs (sitio moderno, modo oscuro/claro, paleta de colores). |
| **i18n** | Internacionalización — múltiples idiomas (pt-BR, en, de, es, fr, it). |
| **nav_translations** | Mapeo de títulos de navegación para cada idioma en `mkdocs.yml`. |
| **gh-deploy** | Comando de MkDocs que publica la documentación en la rama `webdoc` o GitHub Pages. |
| **webdoc** | Rama de integración usada para la publicación del sitio generado mediante `gh-deploy`. |
| **CHANGELOG.md** | Archivo de registro de cambios que sigue el estándar Keep a Changelog. |
| **ADR** | Architecture Decision Record — documento que registra decisiones de arquitectura. |
| **PRD** | Product Requirements Document — documento de requisitos del producto. |
| **SPEC** | Specification — documento de ejecución/especificación técnica. |
| **PLAN-001** | Plan de mejora de la documentación — documento de planificación del sprint. |
| **CI/CD** | *Continuous Integration / Continuous Deployment* — integración y despliegue continuos. |
| **GitHub Pages** | Servicio alojado en GitHub para la publicación de sitios estáticos. |
| **uv** | Gestor de dependencias y constructor de proyectos Python (alternativa a `pip`). |
| **taskipy** | Ejecutor de tareas (`task`) inspirado en `npm scripts`; usado para personalizar la CLI. |

---

## Metodologías y Proceso

| Término | Definición |
|---|---|
| **Keep a Changelog** | Especificación abierta para el formato de los archivos `CHANGELOG.md`. |
| **Semantic Versioning (SemVer)** | Reglas para el versionado `MAJOR.MINOR.PATCH` con `rc`, `alpha`, etc. |
| **Conventional Commits** | Especificación de mensajes de commit con prefijos (`feat:`, `fix:`, `chore:`). |
| **TDD** | *Test-Driven Development* — desarrollo guiado por pruebas (rojo → verde → refactorizar). |
| **AC** | *Acceptance Criteria* — criterio de aceptación de una issue/tarea. |
| **P0 / P1 / P2** | Niveles de prioridad: crítico, alto, medio. |
| **Sprint** | Ciclo de entrega (generalmente 1–2 semanas) con issues planificadas previamente. |
| **Worktree** | Directorio de trabajo aislado derivado de una rama. |
| **Rebase** | Técnica de integración que reaplica commits sobre otra rama. |
| **Fast-forward / Merge --no-ff** | Estrategias de fusión de ramas; aquí se usa `--no-ff` para mantener el historial de tareas. |

---

## Calidad y Validación

| Término | Definición |
|---|---|
| **ruff** | Linter y formateador moderno en Python (sustituto de `flake8`, `black`, `isort`). |
| **mypy** | Comprobador estático de tipos (type checker) en Python. |
| **pytest** | Framework de pruebas unitarias en Python. |
| **coverage 99,7%** | Cobertura mínima de código necesaria en las pruebas (regla de calidad). |
| **Strict mode** | Modo de validación máxima de MkDocs (falla con warnings). |
| **broken link** | Enlace interno que apunta a un archivo inexistente. |
| **UTF-8 strict** | Validación de codificación UTF-8 sin sustitución de caracteres inválidos. |
| **mojibake** | Texto corrupto por error de codificación (ej.: `Ã£` en lugar de `ã`). |
| **HTML entity** | Representación de caracteres especiales mediante su codificación numérica (ej.: `&amp;`). |
| **Badge** | Icono visual en Markdown con estado (CI verde, versión, etc.) mediante servicios externos. |

---

## Entregas y Publicación

| Término | Definición |
|---|---|
| **publish** | Proceso de subir la documentación generada al servidor de alojamiento. |
| **site_name** | Título mostrado en la cabecera del sitio generado. |
| **edit_uri** | URI usada para la edición directa de páginas por GitHub. |
| **edit_uri: tree/branch/docs** | Patrón usado para generar enlaces de edición en GitHub. |
| **theme** | Aspecto y layout del sitio (aquí: `material`). |
| **light/dark mode** | Soporte para modo claro y oscuro mediante la paleta de Material. |
| **sidebar** | Barra lateral con navegación progresiva por los temas. |
| **permalink** | URL permanente de una sección (genera anclajes automáticos). |
| **autolink** | Crea anclajes automáticos a partir de los encabezados. |
| **emoji** | Extensión que permite usar emojis aquí en Markdown. |
| **pagetocat** | Genera una tabla de contenido (TOC) en la parte superior de la página. |
| **toc permalink** | Permite hacer clic en el icono del enlace para ir a un encabezado. |

---

## Variables de Entorno y Archivos de Configuración

| Término | Definición |
|---|---|
| **pyproject.toml** | Archivo de configuración del paquete Python (PEP 621): dependencias, versión, scripts. |
| **uv.lock** | Lockfile de `uv` con las versiones exactas de todas las dependencias. |
| **tox.ini / pyproject.toml [tool.tox]** | Configuración de múltiples versiones de Python y entornos de prueba. |
| **.changelog.toml** | Archivo de configuración opcional del generador de CHANGELOG. |
| **version.txt** | Archivo que guarda la versión actual del paquete en tiempo de ejecución. |
| **.gitattributes** | Define cómo trata Git a los archivos del repositorio. |
| **CI/CD workflow** | Script de GitHub Actions (`.github/workflows/*.yml`). |
| **pre-commit** | Hook de git ejecutado antes de cada commit (calidad del código). |
| **environment** | Entorno aislado de Python (`.venv/`), gestionado mediante `uv`. |
| **coverage_report** | Directorio con el informe HTML de cobertura de pruebas. |
| **docs/** | Directorio raíz de la documentación en Markdown. |
| **incolume/**, **src/** | Código fuente Python del paquete. |

---

## Comandos Útiles

| Término | Definición |
|---|---|
| `uv sync` | Sincroniza el entorno virtual con `uv.lock` e instala las dependencias. |
| `uv run` | Ejecuta un comando dentro del entorno activado. |
| `uv run task setup` | Configura los hooks de git (`core.hooksPath`). |
| `uv run task -l` | Lista todas las tareas disponibles (`taskipy`). |
| `uv run ruff check` | Ejecuta el linter. |
| `uv run ruff format` | Formatea el código. |
| `uv run mypy` | Verifica los tipos estáticos. |
| `uv run pytest` | Ejecuta la suite de pruebas. |
| `uv run mkdocs build` | Genera la documentación en `_site/` (o `site/`). |
| `uv run mkdocs serve` | Sirve la documentación en localhost. |
| `uv run mkdocs gh-deploy --remote-branch webdoc` | Publica la documentación en GitHub Pages (`webdoc`). |
| `uv run tox` | Ejecuta la matriz de pruebas multi-versión. |
| `uv run gcl` | Genera o actualiza el `CHANGELOG.md`. |
| `git tag -n` | Lista las etiquetas con anotaciones; fuente de las versiones en el CHANGELOG. |
| `uv version` | Incrementa la versión del paquete (ver [semver.org](https://semver.org)). |
| `git worktree` | Gestiona los directorios de trabajo múltiples del repositorio. |

---

## Glosario por Frecuencia (Top)

Ordenados por la frecuencia relativa en la documentación.

| Término | Apariciones | Contexto típico |
|---|---|---|
| **Markdown** | 226 | Formato de documentación, extensión `.md`. |
| **CHANGELOG** | 137 | Registro de cambios, archivo `CHANGELOG.md`. |
| **Python** | 102 | Lenguaje de programación principal. |
| **API** | 96 | Interfaz de programación de aplicaciones. |
| **URL** | 99 | Localizador de recursos en la web. |
| **GitHub** | 44 | Plataforma de alojamiento de código. |
| **CI/CD** | 45 | Integración/despliegue continuos. |
| **Issue** | — | Tarea o bug rastreado en el tracker del proyecto. |
| **AC** | — | *Acceptance Criteria* — criterio de aceptación. |
| **README** | — | Documentación inicial del repositorio. |
| **Versioning** | — | Gestión de versiones (`MAJOR.MINOR.PATCH`). |
| **Conventional Commit** | — | Especificación de mensajes de commit. |
| **Keep a Changelog** | — | Estándar para el formato de `CHANGELOG.md`. |
| **Semantic Versioning** | — | Reglas `MAJOR.MINOR.PATCH`. |
| **SemVer** | — | Abreviatura de Semantic Versioning. |
| **MkDocs** | — | Herramienta de generación de sitios estáticos. |
| **material** | — | Tema Material para MkDocs. |
| **i18n** | — | Internacionalización. |
| **nav_translations** | — | Mapeo de títulos de navegación por idioma. |
| **gh-deploy** | — | Comando de publicación de MkDocs. |
| **webdoc** | — | Rama de integración para GitHub Pages. |
| **uv** | — | Gestor de dependencias y constructor. |
| **taskipy** | — | Ejecutor de tareas. |
| **ruff** | — | Linter y formateador en Python. |
| **mypy** | — | Verificador estático de tipos. |
| **pytest** | — | Framework de pruebas. |
| **coverage** | — | Cobertura de código en las pruebas. |
| **UnicodeDecodeError** | — | Error de codificación al leer un archivo. |
| **mojibake** | — | Texto corrupto por error de codificación. |
| **toctoc** | — | Tabla de contenido automática. |
| **ACR** | — | *Acceptance Criteria Rule* — regla de aceptación. |

---

## Referencias

- [Keep a Changelog](https://keepachangelog.com/en/1.0.0)
- [Semantic Versioning](https://semver.org/spec/v2.0.0.html)
- [Conventional Commits](https://www.conventionalcommits.org/pt-br/v1.0.0)
- [MkDocs](https://www.mkdocs.org)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [MkDocs i18n Plugin](https://mkdocs-material.squidfunk.com/configuration/i18n/)
- [GitHub Pages](https://pages.github.com)

---

*Fuente: revisión de la documentación de `incolume.py.changelog` (v1.6.0a11, dev).*

# Glossary

Repository of technical terms used in the
`incolume.py.changelog` documentation.

This file serves as a **glossary** (top-100 project terms), organized by
category, with the definition and where the term appears in the documentation.

> Last updated: 2026-11-16
> Product version: 1.6.0a11 (dev)

---

## Architecture and Generation

| Term | Definition |
|---|---|
| **mkdocs** | Static tool for generating HTML documentation from Markdown files. |
| **mkdocstrings** | MkDocs plugin that generates API documentation automatically from Python code docstrings. |
| **material** | Material theme for MkDocs (modern site, dark/light mode, color palette). |
| **i18n** | Internationalization — multiple languages (pt-BR, en, de, es, fr, it). |
| **nav_translations** | Mapping of navigation titles for each language in `mkdocs.yml`. |
| **gh-deploy** | MkDocs command that publishes the documentation to the `webdoc` branch or GitHub Pages. |
| **webdoc** | Integration branch used to publish the site generated via `gh-deploy`. |
| **CHANGELOG.md** | Change log file following the Keep a Changelog standard. |
| **ADR** | Architecture Decision Record — a document that records architectural decisions. |
| **PRD** | Product Requirements Document — the product requirements document. |
| **SPEC** | Specification — the execution/technical specification document. |
| **PLAN-001** | Documentation improvement plan — the sprint planning document. |
| **CI/CD** | *Continuous Integration / Continuous Deployment* — continuous integration and delivery. |
| **GitHub Pages** | Service hosted by GitHub for publishing static sites. |
| **uv** | Python dependency manager and project builder (an alternative to `pip`). |
| **taskipy** | Task runner (`task`) inspired by `npm scripts`; used to customize the CLI. |

---

## Methodologies and Process

| Term | Definition |
|---|---|
| **Keep a Changelog** | Open specification for the `CHANGELOG.md` file format. |
| **Semantic Versioning (SemVer)** | Rules for `MAJOR.MINOR.PATCH` versioning with `rc`, `alpha`, etc. |
| **Conventional Commits** | Commit message specification with prefixes (`feat:`, `fix:`, `chore:`). |
| **TDD** | *Test-Driven Development* — development guided by tests (red → green → refactor). |
| **AC** | *Acceptance Criteria* — the acceptance criterion of an issue/task. |
| **P0 / P1 / P2** | Priority levels: critical, high, medium. |
| **Sprint** | Delivery cycle (usually 1–2 weeks) with previously planned issues. |
| **Worktree** | Isolated working directory derived from a branch. |
| **Rebase** | Integration technique that replays commits on top of another branch. |
| **Fast-forward / Merge --no-ff** | Merge strategies for branches; here `--no-ff` is used to preserve the task history. |

---

## Quality and Validation

| Term | Definition |
|---|---|
| **ruff** | Modern Python linter and formatter (replacement for `flake8`, `black`, `isort`). |
| **mypy** | Static type checker for Python. |
| **pytest** | Python unit test framework. |
| **coverage 99.7%** | Minimum code coverage required in tests (quality rule). |
| **Strict mode** | MkDocs maximum validation mode (fails on warnings). |
| **broken link** | Internal link pointing to a nonexistent file. |
| **UTF-8 strict** | UTF-8 encoding validation without replacing invalid characters. |
| **mojibake** | Text corrupted by an encoding error (e.g., `Ã£` instead of `ã`). |
| **HTML entity** | Representation of special characters using their numeric encoding (e.g., `&amp;`). |
| **Badge** | Visual icon in Markdown showing status (green CI, version, etc.) via external services. |

---

## Delivery and Publishing

| Term | Definition |
|---|---|
| **publish** | Process of uploading the generated documentation to the hosting server. |
| **site_name** | Title displayed in the header of the generated site. |
| **edit_uri** | URI used for direct editing of pages through GitHub. |
| **edit_uri: tree/branch/docs** | Pattern used to generate edit links on GitHub. |
| **theme** | Look and layout of the site (here: `material`). |
| **light/dark mode** | Light and dark mode support via the Material palette. |
| **sidebar** | Sidebar with progressive navigation through the topics. |
| **permalink** | Permanent URL of a section (generates automatic anchors). |
| **autolink** | Creates automatic anchors from headings. |
| **emoji** | Extension that allows using emojis in Markdown. |
| **pagetocat** | Generates a table of contents (TOC) at the top of the page. |
| **toc permalink** | Allows clicking the link icon to jump to a heading. |

---

## Environment Variables and Configuration Files

| Term | Definition |
|---|---|
| **pyproject.toml** | Python package configuration file (PEP 621): dependencies, version, scripts. |
| **uv.lock** | `uv` lockfile with the exact versions of all dependencies. |
| **tox.ini / pyproject.toml [tool.tox]** | Configuration of multiple Python versions and test environments. |
| **.changelog.toml** | Optional configuration file for the CHANGELOG generator. |
| **version.txt** | File that stores the current package version at runtime. |
| **.gitattributes** | Defines how Git treats the files in the repository. |
| **CI/CD workflow** | GitHub Actions script (`.github/workflows/*.yml`). |
| **pre-commit** | Git hook run before each commit (code quality). |
| **environment** | Isolated Python environment (`.venv/`), managed via `uv`. |
| **coverage_report** | Directory with the HTML test coverage report. |
| **docs/** | Root directory of the Markdown documentation. |
| **incolume/**, **src/** | Python source code of the package. |

---

## Useful Commands

| Term | Definition |
|---|---|
| `uv sync` | Syncs the virtual environment with `uv.lock` and installs dependencies. |
| `uv run` | Runs a command inside the activated environment. |
| `uv run task setup` | Configures the git hooks (`core.hooksPath`). |
| `uv run task -l` | Lists all available tasks (`taskipy`). |
| `uv run ruff check` | Runs the linter. |
| `uv run ruff format` | Formats the code. |
| `uv run mypy` | Checks static types. |
| `uv run pytest` | Runs the test suite. |
| `uv run mkdocs build` | Generates the documentation into `_site/` (or `site/`). |
| `uv run mkdocs serve` | Serves the documentation on localhost. |
| `uv run mkdocs gh-deploy --remote-branch webdoc` | Publishes the documentation to GitHub Pages (`webdoc`). |
| `uv run tox` | Runs the multi-version test matrix. |
| `uv run task changelog` | Generates or updates `CHANGELOG.md`. |
| `git tag -n` | Lists tags with annotations; source of the versions in the CHANGELOG. |
| `uv version` | Increments the package version (see [semver.org](https://semver.org)). |
| `git worktree` | Manages multiple working directories of the repository. |

---

## Glossary by Frequency (Top)

Ordered by relative frequency in the documentation.

| Term | Occurrences | Typical context |
|---|---|---|
| **Markdown** | 226 | Documentation format, `.md` extension. |
| **CHANGELOG** | 137 | Change log, `CHANGELOG.md` file. |
| **Python** | 102 | Main programming language. |
| **API** | 96 | Application programming interface. |
| **URL** | 99 | Web resource locator. |
| **GitHub** | 44 | Code hosting platform. |
| **CI/CD** | 45 | Integration/continuous delivery. |
| **Issue** | — | Task or bug tracked in the project tracker. |
| **AC** | — | *Acceptance Criteria* — acceptance criterion. |
| **README** | — | Initial repository documentation. |
| **Versioning** | — | Version management (`MAJOR.MINOR.PATCH`). |
| **Conventional Commit** | — | Commit message specification. |
| **Keep a Changelog** | — | Standard for formatting `CHANGELOG.md`. |
| **Semantic Versioning** | — | `MAJOR.MINOR.PATCH` rules. |
| **SemVer** | — | Short for Semantic Versioning. |
| **MkDocs** | — | Static site generation tool. |
| **material** | — | Material theme for MkDocs. |
| **i18n** | — | Internationalization. |
| **nav_translations** | — | Mapping of navigation titles per language. |
| **gh-deploy** | — | MkDocs publishing command. |
| **webdoc** | — | Integration branch for GitHub Pages. |
| **uv** | — | Dependency manager and project builder. |
| **taskipy** | — | Task runner. |
| **ruff** | — | Python linter and formatter. |
| **mypy** | — | Static type checker. |
| **pytest** | — | Test framework. |
| **coverage** | — | Code coverage in tests. |
| **UnicodeDecodeError** | — | Encoding error when reading a file. |
| **mojibake** | — | Text corrupted by an encoding error. |
| **toctoc** | — | Automatic table of contents. |
| **ACR** | — | *Acceptance Criteria Rule* — acceptance rule. |

---

## References

- [Keep a Changelog](https://keepachangelog.com/en/1.0.0)
- [Semantic Versioning](https://semver.org/spec/v2.0.0.html)
- [Conventional Commits](https://www.conventionalcommits.org/pt-br/v1.0.0)
- [MkDocs](https://www.mkdocs.org)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [MkDocs i18n Plugin](https://mkdocs-material.squidfunk.com/configuration/i18n/)
- [GitHub Pages](https://pages.github.com)

---

*Source: review of the `incolume.py.changelog` documentation (v1.6.0a11, dev).*

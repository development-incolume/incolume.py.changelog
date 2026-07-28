# CHANGELOG


All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html) and [Conventional Commit](https://www.conventionalcommits.org/pt-br/v1.0.0/).

This file was automatically generated for [incolume.py.changelog](https://github.com/development-incolume/incolume.py.changelog/-/tree/0.20.0a9)

---


## [Unreleased]	 &#8212; 	2026-07-27:
### Added
  - Adicionado suporte a Python 3.14 conforme Status of Python versions (https://devguide.python.org/versions/#versions);
### Changed
  - Emancipado configuraÃ§Ã£o para pytest;
### Deprecated
  - SerÃ¡ Descontinuado suporte a Python 3.10 conforme Status of Python versions (https://devguide.python.org/versions/#versions);
  - SerÃ¡ Descontinuado suporte a Python 3.11 conforme Status of Python versions (https://devguide.python.org/versions/#versions);

## [0.19.0]	 &#8212; 	2026-07-23:
### Changed
  - CorreÃ§Ãµes lint CI/CD;
  - GeraÃ§Ã£o de path/arquivo de CHANGELOG.md automÃ¡ticos;
  - Melhoria de performance na execuÃ§Ã£o de rotinas do pacote `core`;
  - AtualizaÃ§Ã£o dos pacotes de dependÃªncia;
  - Retificado parametros para compatibilidade com `mypy`;
  - Atualizado configuraÃ§Ã£o para `codecov-cli`;
  - `codecov-cli` substituÃ­do por `codecov action`;
### Deprecated
  - SerÃ¡ Descontinuado suporte a Python 3.10 conforme Status of Python versions (https://devguide.python.org/versions/#versions);
### Removed
  - Pacote `codecov-cli`;

## [0.19.0rc4]	 &#8212; 	2026-07-15:
### Changed
  - Atualizado configuraÃ§Ã£o para `codecov-cli`;

## [0.19.0rc3]	 &#8212; 	2026-07-15:
### Changed
  - Retificado parametros para compatibilidade com `mypy`;

## [0.19.0rc2]	 &#8212; 	2026-07-15:
### Changed
  - Retificado parametros para compatibilidade com `mypy`;

## [0.19.0rc1]	 &#8212; 	2026-07-14:
### Changed
  - AtualizaÃ§Ã£o dos pacotes de dependÃªncia;

## [0.19.0rc0]	 &#8212; 	2026-07-14:
### Changed
  - CorreÃ§Ãµes lint CI/CD;
  - GeraÃ§Ã£o de path/arquivo de CHANGELOG.md automÃ¡ticos;
  - Melhoria de performance na execuÃ§Ã£o de rotinas do pacote `core`;

## [0.18.0]	 &#8212; 	2026-07-13:
### Added
  - TraduÃ§Ã£o do arquivo COVENTIONAL_COMMITS.md em alemÃ£o, espanhol, francÃªs, inglÃªs, italiano e portuguÃªs;
  - TraduÃ§Ã£o do arquivo writing-your-docs.md em alemÃ£o, espanhol, francÃªs, inglÃªs, italiano e portuguÃªs;
  - TraduÃ§Ã£o do arquivo zenpy.md em alemÃ£o, espanhol, francÃªs, inglÃªs, italiano e portuguÃªs;
  - TraduÃ§Ã£o do arquivo keep-a-changelog.md em alemÃ£o, espanhol, francÃªs, inglÃªs, italiano e portuguÃªs;
  - Adicionado pacote `tomlkit`;
### Changed
  - AtualizaÃ§Ã£o de versÃ£o simultÃ¢nea em `pyproject.toml` e `version.txt` com aplicativos `uv` e `poetry`;
  - Funcionalidades do pacote centralizado no mÃ³dulo `core`;
### Removed
  - Removido pacote `toml`;

## [0.17.0]	 &#8212; 	2025-08-16:
### Removed
  - Descontinuado compatibilidade e suporte a Python 3.8 conforme Status of Python versions (https://devguide.python.org/versions/#versions);
  - Descontinuado compatibilidade e suporte a Python 3.9 conforme Status of Python versions (https://devguide.python.org/versions/#versions);
  - Removido pacote `black`;
  - Removido pacote `pylint`;
  - Removido pacote `isort`;
  - Removido pacote `pydocstyle`;
  - Removido pacote `flake8`;
### Changed
  - ValidaÃ§Ã£o CI/CD obrigatÃ³ria para `mypy`, `lint` e `format code`;
  - Gerenciador `uv` introduzido em ci/cd para gerar documentaÃ§Ã£o;
  - Gerenciador `uv` introduzido na execuÃ§Ã£o do comando `tox`;
  - Configurado compatibilidade cruzada de dependÃªncias entre `uv`e `poetry`;

## [0.16.0]	 &#8212; 	2025-08-16:
### Deprecated
  - SerÃ¡ Descontinuado suporte a Python 3.8 conforme Status of Python versions (https://devguide.python.org/versions/#versions);
  - SerÃ¡ Descontinuado suporte a Python 3.9 conforme Status of Python versions (https://devguide.python.org/versions/#versions);
  - Black;
  - Pylint;
  - Isort;
  - Pydocstyle;
  - Flake8;
  - Poetry;
### Changed
  - Gerenciador `uv` definido como gerenciador principal;
  - `ruff` definido como verificador e formatador principal;
### Fixed
  - AmpliaÃ§Ã£o da cobertura para 100% do cÃ³digo atual;

## [0.15.0]	 &#8212; 	2025-08-14:
### Added
  - Adicionado definiÃ§Ãµes para compatibilidade plena com gerenciador `uv`;
  - Ativado a ferramenta `ruff` como validador e formatador de cÃ³digo para o projeto;
  - Ativado configuraÃ§Ã£o de script para ambiente atualizado do pyproject.toml;
  - Controle de exibiÃ§Ã£o verbosa no terminal por variaveis de ambiente;
### Changed
  - AtualizaÃ§Ã£o do modelo para pyproject.toml;
  - Ampliado cobertura para mÃ³dulo principal;
  - AtualizaÃ§Ã£o de performance em ci/cd para funcionar com `uv` + `ruff`;
### Deprecated
  - Flake8;
  - Isort;
  - Pylint;
### Fixed
  - CorreÃ§Ã£o no timestamp para evitar conflito no Windows;
  - Strip de URL para url-compare;
  - Suspenso temporariamente testes de docstring em conflito;

## [0.14.0]	 &#8212; 	2025-01-15:
### Fixed
  - Desativado temporariamente ci/cd para formataÃ§Ã£o com ruff;
  - Desativado temporariamente ci/cd para lint com ruff;
  - Tratamento de exceÃ§Ã£o FileNotFoundError ao carregar versionamento do pacote;

## [0.13.1]	 &#8212; 	2024-12-29:
### Changed
  - Atualizado documentaÃ§Ã£o;
### Fixed
  - Desativado temporariamente ci/cd para formataÃ§Ã£o e lint com ruff;

## [0.13.0]	 &#8212; 	2024-12-28:
### Fixed
  - Ajuste no script CI/CD;
  - Refinamento de testes unitÃ¡rios para CI/CD;
  - Ajuste no git workflow;

## [0.12.3]	 &#8212; 	2024-12-27:
### Fixed
  - Recuperado arquivo de restriÃ§Ãµes para `poetry`;

## [0.12.2]	 &#8212; 	2024-12-27:
### Fixed
  - Ajuste nas restriÃ§Ãµes de dependÃªncias;

## [0.12.1]	 &#8212; 	2024-12-27:
### Fixed
  - Corrigido contexto de mock para funcionamento em python 3.8 ou superior;

## [0.12.0]	 &#8212; 	2024-12-27:
### Changed
  - ParÃ¢metro `-r/--reverse` transformado em flag;
  - Removido a necessidade de informar valor em parametro `reverse`;
### Fixed
  - CorreÃ§Ã£o em testes para CI/CD;
  - Trabalhado encode para sistemas Windows;

## [0.11.5]	 &#8212; 	2024-08-27:
### Fixed
  - AlteraÃ§Ã£o na configuraÃ§Ã£o para sanar erro de execuÃ§Ã£o exclusivo em CI/CD;

## [0.11.4]	 &#8212; 	2024-08-27:
### Changed
  - AtualizaÃ§Ã£o da ferramenta `ruff` e respectiva configuraÃ§Ã£o;
### Fixed
  - AtualziaÃ§Ã£o de conflitos no ambiente para CI/CD;

## [0.11.3]	 &#8212; 	2024-08-27:
### Fixed
  - AtualziaÃ§Ã£o do ambiente para CI/CD;

## [0.11.2]	 &#8212; 	2024-08-27:
### Fixed
  - DependÃªncias para ambiente de CI/CD atualizadas;

## [0.11.1]	 &#8212; 	2024-08-27:
### Fixed
  - Conflito de validaÃ§Ã£o entre `isort` e `ruff`;

## [0.11.0]	 &#8212; 	2024-08-27:
### Changed
  - ParÃ¢metro `-r/--reverse` transformado em flag, e removido a necessidade de informar valor;
### Fixed
  - CorreÃ§Ã£o em testes para CI/CD;

## [0.10.0]	 &#8212; 	2024-08-26:
### Added
  - Gerenciador de pacotes poetry para projeto;
  - Pacote `ruff` adicionado como formatador e validador de estilos;
### Changed
  - Ambiente virtual local, para melhor funcionamento em Windows;
  - Melhoria de performance de metodos da geraÃ§Ã£o de `CHANGELOG.md`;
  - FormataÃ§Ã£o e validaÃ§Ã£o de cÃ³digo ruff aplicados;

## [0.9.0]	 &#8212; 	2024-05-14:
### Added
  - Acrescentado traduÃ§Ãµes para `cÃ³digo de conduta` (DE, EN, ES, PT, FR, IT);
  - Acrescentado traduÃ§Ãµes para  `semver.md` (DE, EN, ES, PT, FR, IT);
### Changed
  - Atualizado badges da pÃ¡gina inicial da documentaÃ§Ã£o;
  - Atualizado badges do README;
  - AtualizaÃ§Ã£o da estrutura do README do projeto;
  - Atualizado exemplos de utilizaÃ§Ã£o de mÃ©todos para API.;
  - Exemplos de utilizaÃ§Ã£o do programa na documentaÃ§Ã£o;

## [0.9.0rc0]	 &#8212; 	2024-01-16:
### Added
  - Acrescentado traduÃ§Ãµes para `cÃ³digo de conduta` (DE, EN, ES, PT, FR, IT);
  - Acrescentado traduÃ§Ãµes para  `semver.md` (DE, EN, ES, PT, FR, IT);
### Changed
  - Exemplos de utilizaÃ§Ã£o do programa na documentaÃ§Ã£o.;

## [0.8.0]	 &#8212; 	2024-01-06:
### Added
  - Acrescentado campo de busca na documentaÃ§Ã£o da API;
  - Acrescentado modo noturno na pÃ¡gina oficial de documentaÃ§Ã£o da API;
  - Acrescentado suporte a multiplos idiomas para documentaÃ§Ã£o;
  - Acrescentado traduÃ§Ã£o do cÃ³digo de contuda em italiano;
  - Acrescentado traduÃ§Ã£o do cÃ³digo de contuda em francÃªs;
  - Acrescentado traduÃ§Ã£o do cÃ³digo de contuda em espanhol;
  - Acrescentado traduÃ§Ã£o do cÃ³digo de contuda em alemÃ£o;
  - Acrescentado traduÃ§Ã£o do cÃ³digo de contuda em inglÃªs;
  - Acrescentado traduÃ§Ã£o do contributors.md em inglÃªs;
  - Acrescentado traduÃ§Ã£o do zenpy.md em inglÃªs;
### Deprecated
  - SerÃ¡ substituÃ­do em breve o pacote `isort`;
### Fixed
  - Redefinido renderizaÃ§Ã£o de rodapÃ© do arquivo CHANGELOG.md;

## [0.7.0]	 &#8212; 	2024-01-05:
### Added
  - Formatador de cÃ³digo redefindo com `ruff`;
  - Adicionado badges de `wheel` e `stable`;
### Changed
  - Renomeado workflow CI/CD `python-package.yml -> unit-tests.yml`;
  - AtualizaÃ§Ã£o da documentaÃ§Ã£o com exemplos de utilizaÃ§Ã£o da API;
  - ReativaÃ§Ã£o dos scripts de automaÃ§Ã£o `taskipy`;
  - ReativaÃ§Ã£o dos scripts de automaÃ§Ã£o `makefile`;
  - ReativaÃ§Ã£o dos scripts de automaÃ§Ã£o `tox`;
  - InformaÃ§Ãµes referente ao projeto atualizadas na pÃ¡gina de documentaÃ§Ã£o;
### Removed
  - Removido pacote `blue`;
  - Desativado formatador `blue` em CI/CD;

## [0.6.2]	 &#8212; 	2024-01-04:
### Added
  - AtivaÃ§Ã£o da configuraÃ§Ã£o `Codecov.io`.;
### Fixed
  - CorreÃ§Ã£o na excuÃ§Ã£o de testes unitÃ¡rios em CI/CD;
  - CorreÃ§Ã£o de geraÃ§Ã£o de relatÃ³rio de cobertura no container CI/CD.;

## [0.6.1]	 &#8212; 	2024-01-02:
### Fixed
  - Habilitado diretiva `workflow_dispatch` para executar workflow manualmente;

## [0.6.0]	 &#8212; 	2024-01-02:
### Fixed
  - CorreÃ§Ã£o na excuÃ§Ã£o de testes unitÃ¡rios em CI/CD;

## [0.6.0rc0]	 &#8212; 	2024-01-02:
### Fixed
  - CorreÃ§Ã£o na excuÃ§Ã£o de testes unitÃ¡rios em CI/CD;

## [0.5.0]	 &#8212; 	2024-01-01:
### Fixed
  - CorreÃ§Ã£o em aÃ§Ãµes de fluxo CI/CD;
  - Sanado conflito entre ferramentas de validaÃ§Ã£o de tipo;
  - Sanado conflito entre ferramentas de ordenaÃ§Ã£o de pacotes;
  - Sanado conflito entre ferramentas lint;

## [0.5.0rc0]	 &#8212; 	2023-12-31:
### Fixed
  - Sanado conflito entre ferramentas de validaÃ§Ã£o de tipo;
  - Sanado conflito entre ferramentas de ordenaÃ§Ã£o de pacotes;
  - Sanado conflito entre ferramentas lint;

## [0.4.0]	 &#8212; 	2023-12-31:
### Changed
  - Atualizado verificaÃ§Ã£o de tipo estÃ¡tico `mypy` para compatibilidade de versÃ£o a partir do Python 3.8;
  - Atualizado logo do projeto;
### Fixed
  - Ajuste de conflitos entre ruff e mypy;
  - Recuperado cobertura de 100% no mÃ³dulo changelog.cli;

## [0.3.0]	 &#8212; 	2023-12-24:
### Added
  - Acrescentado validaÃ§Ã£o CI/CD multiplataforma ao projeto;
  - Definido checagem lint via ruff para CI/CD;
  - IncluÃ­do guia para markdown no menu da documentaÃ§Ã£o;
  - IncluÃ­do validaÃ§Ã£o CI/CD para QA (Quality Assurance);
  - Acrescentado suporte a Python 3.12;
  - Acrescentado fluxo para publicaÃ§Ã£o em TestPyPi;
  - Acrescentado fluxo para publicaÃ§Ã£o em Pypi;
  - Acrescentado fluxo CI/CD para geraÃ§Ã£o de documentaÃ§Ã£o;
  - Acrescentado documentaÃ§Ã£o web online (https://development-incolume.github.io/incolume.py.changelog/);
### Changed
  - Atingido cobertura de 100% no mÃ³dulo changelog.cli;
  - Atingido cobertura de 100% no mÃ³dulo changelog.changelog;
  - Atingido cobertura de 100% no mÃ³dulo changelog;
  - Acrescentado exemplos dos mÃ©todos da API;
  - Uniformizado testes multiplataforma para (Linux e Windows);
  - Cobertura parcial para estilo mypy;

## [0.3.0rc4]	 &#8212; 	2023-12-24:
### Added
  - Acrescentado validaÃ§Ã£o CI/CD multiplataforma ao projeto;
  - Definido checagem lint via ruff para CI/CD;
  - IncluÃ­do guia para markdown no menu da documentaÃ§Ã£o;
  - IncluÃ­do validaÃ§Ã£o CI/CD para QA (Quality Assurance);
  - Acrescentado suporte a Python 3.12;
  - Acrescentado fluxo para publicaÃ§Ã£o em TestPyPi;
  - Acrescentado fluxo para publicaÃ§Ã£o em Pypi;
  - Acrescentado fluxo CI/CD para geraÃ§Ã£o de documentaÃ§Ã£o;
  - Acrescentado documentaÃ§Ã£o web online;
### Changed
  - Atingido cobertura de 100% no mÃ³dulo changelog.cli;
  - Atingido cobertura de 100% no mÃ³dulo changelog.changelog;
  - Atingido cobertura de 100% no mÃ³dulo changelog;
  - Acrescentado exemplos dos mÃ©todos da API;
  - Uniformizado testes multiplataforma para (Linux e Windows);
  - Cobertura parcial para estilo mypy;

## [0.3.0rc3]	 &#8212; 	2023-12-24:
### Added
  - Acrescentado validaÃ§Ã£o CI/CD multiplataforma ao projeto;
  - Definido checagem lint via ruff para CI/CD;
  - IncluÃ­do guia para markdown no menu da documentaÃ§Ã£o;
  - IncluÃ­do validaÃ§Ã£o CI/CD para QA (Quality Assurance);
  - Acrescentado suporte a Python 3.12;
  - Acrescentado fluxo para publicaÃ§Ã£o em TestPyPi;
  - Acrescentado fluxo para publicaÃ§Ã£o em Pypi;
  - Acrescentado fluxo CI/CD para geraÃ§Ã£o de documentaÃ§Ã£o;
  - Acrescentado documentaÃ§Ã£o web online;
### Changed
  - Atingido cobertura de 100% no mÃ³dulo changelog.cli;
  - Atingido cobertura de 100% no mÃ³dulo changelog.changelog;
  - Atingido cobertura de 100% no mÃ³dulo changelog;
  - Acrescentado exemplos dos mÃ©todos da API;
  - Uniformizado testes multiplataforma para (Linux e Windows);
  - Cobertura parcial para estilo mypy;

## [0.3.0rc2]	 &#8212; 	2023-12-23:
### Added
  - Acrescentado validaÃ§Ã£o CI/CD multiplataforma ao projeto;
  - Definido checagem lint via ruff para CI/CD;
  - IncluÃ­do guia para markdown no menu da documentaÃ§Ã£o;
  - IncluÃ­do validaÃ§Ã£o CI/CD para QA (Quality Assurance);
  - Acrescentado suporte a Python 3.12;
  - Acrescentado fluxo para publicaÃ§Ã£o em TestPyPi;
  - Acrescentado fluxo para publicaÃ§Ã£o em Pypi;
### Changed
  - Atingido cobertura de 100% no mÃ³dulo changelog.cli;
  - Atingido cobertura de 100% no mÃ³dulo changelog.changelog;
  - Atingido cobertura de 100% no mÃ³dulo changelog;
  - Acrescentado exemplos dos mÃ©todos da API;
  - Uniformizado testes multiplataforma para (Linux e Windows);
  - Cobertura parcial para estilo mypy;

## [0.3.0rc1]	 &#8212; 	2023-12-23:
### Added
  - Acrescentado validaÃ§Ã£o CI/CD multiplataforma ao projeto;
  - Definido checagem lint via ruff para CI/CD;
  - IncluÃ­do guia para markdown no menu da documentaÃ§Ã£o;
  - IncluÃ­do validaÃ§Ã£o CI/CD para QA (Quality Assurance);
  - Acrescentado suporte a Python 3.12;
  - Acrescentado fluxo para publicaÃ§Ã£o em TestPyPi;
### Changed
  - Atingido cobertura de 100% no mÃ³dulo changelog.cli;
  - Atingido cobertura de 100% no mÃ³dulo changelog.changelog;
  - Atingido cobertura de 100% no mÃ³dulo changelog;
  - Acrescentado exemplos dos mÃ©todos da API;
  - Uniformizado testes multiplataforma para (Linux e Windows);
  - Cobertura parcial para estilo mypy;

## [0.3.0rc0]	 &#8212; 	2023-12-23:
### Added
  - Acrescentado validaÃ§Ã£o CI/CD multiplataforma ao projeto;
  - Definido checagem lint via ruff para CI/CD;
  - IncluÃ­do guia para markdown no menu da documentaÃ§Ã£o;
  - IncluÃ­do validaÃ§Ã£o CI/CD para QA (Quality Assurance);
  - Acrescentado suporte a Python 3.12;
### Changed
  - Atingido cobertura de 100% no mÃ³dulo changelog.cli;
  - Atingido cobertura de 100% no mÃ³dulo changelog.changelog;
  - Atingido cobertura de 100% no mÃ³dulo changelog;
  - Acrescentado exemplos dos mÃ©todos da API;
  - Uniformizado testes multiplataforma para (Linux e Windows);
  - Cobertura parcial para estilo mypy;

## [0.2.0]	 &#8212; 	2023-12-21:
### Added
  - Pacotes de documentaÃ§Ã£o;
  - Pacotes de seguranÃ§a de software;
  - Pacotes de desenvolvimento;
  - Pacote types-toml;
  - Ferramentas de QA;
  - DocumentaÃ§Ã£o padrÃ£o(Google Style);
  - DocumentaÃ§Ã£o de API;
  - Badges para documentaÃ§Ã£o;
  - Estilo PEP8;
  - 100% de cobertura no mÃ³dulo cli;
  - Compatibilidade com Python 3.8;
  - ValidaÃ§Ã£o com ruff para todas as versÃµes de Python configuradas;
  - CI/CD funcional para multiplataforma;
### Changed
  - README atualizado;
  - Menu atualizado;
  - Caracteres para Slugfy no nome do brach;
  - RealocaÃ§Ã£o de Changelog para diretÃ³rio docs;
  - URLs do projeto atualizada;
  - Comandos de terminal via script atualizados;
  - Retorno do fixture;
### Fixed
  - Linters corrigidos;
  - Comando de captura de datas;
  - Namespace duplicado;

## 0.1.0	 &#8212; 	2023-12-12:
### Added
  - Projeto emancipado de https://gitlab.com/development-incolume/incolumepy.utils;

---

[0.2.0]: https://github.com/development-incolume/incolume.py.changelog/-/compare/0.1.0...0.2.0
[0.3.0rc0]: https://github.com/development-incolume/incolume.py.changelog/-/compare/0.2.0...0.3.0rc0
[0.3.0rc1]: https://github.com/development-incolume/incolume.py.changelog/-/compare/0.3.0rc0...0.3.0rc1
[0.3.0rc2]: https://github.com/development-incolume/incolume.py.changelog/-/compare/0.3.0rc1...0.3.0rc2
[0.3.0rc3]: https://github.com/development-incolume/incolume.py.changelog/-/compare/0.3.0rc2...0.3.0rc3
[0.3.0rc4]: https://github.com/development-incolume/incolume.py.changelog/-/compare/0.3.0rc3...0.3.0rc4
[0.3.0]: https://github.com/development-incolume/incolume.py.changelog/-/compare/0.3.0rc4...0.3.0
[0.4.0]: https://github.com/development-incolume/incolume.py.changelog/-/compare/0.3.0...0.4.0
[0.5.0rc0]: https://github.com/development-incolume/incolume.py.changelog/-/compare/0.4.0...0.5.0rc0
[0.5.0]: https://github.com/development-incolume/incolume.py.changelog/-/compare/0.5.0rc0...0.5.0
[0.6.0rc0]: https://github.com/development-incolume/incolume.py.changelog/-/compare/0.5.0...0.6.0rc0
[0.6.0]: https://github.com/development-incolume/incolume.py.changelog/-/compare/0.6.0rc0...0.6.0
[0.6.1]: https://github.com/development-incolume/incolume.py.changelog/-/compare/0.6.0...0.6.1
[0.6.2]: https://github.com/development-incolume/incolume.py.changelog/-/compare/0.6.1...0.6.2
[0.7.0]: https://github.com/development-incolume/incolume.py.changelog/-/compare/0.6.2...0.7.0
[0.8.0]: https://github.com/development-incolume/incolume.py.changelog/-/compare/0.7.0...0.8.0
[0.9.0rc0]: https://github.com/development-incolume/incolume.py.changelog/-/compare/0.8.0...0.9.0rc0
[0.9.0]: https://github.com/development-incolume/incolume.py.changelog/-/compare/0.9.0rc0...0.9.0
[0.10.0]: https://github.com/development-incolume/incolume.py.changelog/-/compare/0.9.0...0.10.0
[0.11.0]: https://github.com/development-incolume/incolume.py.changelog/-/compare/0.10.0...0.11.0
[0.11.1]: https://github.com/development-incolume/incolume.py.changelog/-/compare/0.11.0...0.11.1
[0.11.2]: https://github.com/development-incolume/incolume.py.changelog/-/compare/0.11.1...0.11.2
[0.11.3]: https://github.com/development-incolume/incolume.py.changelog/-/compare/0.11.2...0.11.3
[0.11.4]: https://github.com/development-incolume/incolume.py.changelog/-/compare/0.11.3...0.11.4
[0.11.5]: https://github.com/development-incolume/incolume.py.changelog/-/compare/0.11.4...0.11.5
[0.12.0]: https://github.com/development-incolume/incolume.py.changelog/-/compare/0.11.5...0.12.0
[0.12.1]: https://github.com/development-incolume/incolume.py.changelog/-/compare/0.12.0...0.12.1
[0.12.2]: https://github.com/development-incolume/incolume.py.changelog/-/compare/0.12.1...0.12.2
[0.12.3]: https://github.com/development-incolume/incolume.py.changelog/-/compare/0.12.2...0.12.3
[0.13.0]: https://github.com/development-incolume/incolume.py.changelog/-/compare/0.12.3...0.13.0
[0.13.1]: https://github.com/development-incolume/incolume.py.changelog/-/compare/0.13.0...0.13.1
[0.14.0]: https://github.com/development-incolume/incolume.py.changelog/-/compare/0.13.1...0.14.0
[0.15.0]: https://github.com/development-incolume/incolume.py.changelog/-/compare/0.14.0...0.15.0
[0.16.0]: https://github.com/development-incolume/incolume.py.changelog/-/compare/0.15.0...0.16.0
[0.17.0]: https://github.com/development-incolume/incolume.py.changelog/-/compare/0.16.0...0.17.0
[0.18.0]: https://github.com/development-incolume/incolume.py.changelog/-/compare/0.17.0...0.18.0
[0.19.0rc0]: https://github.com/development-incolume/incolume.py.changelog/-/compare/0.18.0...0.19.0rc0
[0.19.0rc1]: https://github.com/development-incolume/incolume.py.changelog/-/compare/0.19.0rc0...0.19.0rc1
[0.19.0rc2]: https://github.com/development-incolume/incolume.py.changelog/-/compare/0.19.0rc1...0.19.0rc2
[0.19.0rc3]: https://github.com/development-incolume/incolume.py.changelog/-/compare/0.19.0rc2...0.19.0rc3
[0.19.0rc4]: https://github.com/development-incolume/incolume.py.changelog/-/compare/0.19.0rc3...0.19.0rc4
[0.19.0]: https://github.com/development-incolume/incolume.py.changelog/-/compare/0.19.0rc4...0.19.0
[Unreleased]: https://github.com/development-incolume/incolume.py.changelog/-/compare/0.19.0...Unreleased

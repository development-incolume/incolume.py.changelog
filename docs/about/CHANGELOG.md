# CHANGELOG


All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html) and [Conventional Commit](https://www.conventionalcommits.org/pt-br/v1.0.0/).

This file was automatically generated for [incolume.py.changelog](https://github.com/development-incolume/incolume.py.changelog/-/tree/0.13.1)

---


## [0.13.1]	 &#8212; 	2024-12-29:
### Changed
  - Atualizado documentação;
### Fixed
  - Desativado temporariamente ci/cd para formatação e lint com ruff;

## [0.13.0]	 &#8212; 	2024-12-28:
### Fixed
  - Ajuste no script CI/CD;
  - Refinamento de testes unitários para CI/CD;
  - Ajuste no git workflow;

## [0.12.3]	 &#8212; 	2024-12-27:
### Fixed
  - Recuperado arquivo de restrições para `poetry`;

## [0.12.2]	 &#8212; 	2024-12-27:
### Fixed
  - Ajuste nas restrições de dependências;

## [0.12.1]	 &#8212; 	2024-12-27:
### Fixed
  - Corrigido contexto de mock para funcionamento em python 3.8 ou superior;

## [0.12.0]	 &#8212; 	2024-12-27:
### Changed
  - Parâmetro `-r/--reverse` transformado em flag;
  - Removido a necessidade de informar valor em parametro `reverse`;
### Fixed
  - Correção em testes para CI/CD;
  - Trabalhado encode para sistemas Windows;

## [0.11.5]	 &#8212; 	2024-08-27:
### Fixed
  - Alteração na configuração para sanar erro de execução exclusivo em CI/CD;

## [0.11.4]	 &#8212; 	2024-08-27:
### Changed
  - Atualização da ferramenta `ruff` e respectiva configuração;
### Fixed
  - Atualziação de conflitos no ambiente para CI/CD;

## [0.11.3]	 &#8212; 	2024-08-27:
### Fixed
  - Atualziação do ambiente para CI/CD;

## [0.11.2]	 &#8212; 	2024-08-27:
### Fixed
  - Dependências para ambiente de CI/CD atualizadas;

## [0.11.1]	 &#8212; 	2024-08-27:
### Fixed
  - Conflito de validação entre `isort` e `ruff`;

## [0.11.0]	 &#8212; 	2024-08-27:
### Changed
  - Parâmetro `-r/--reverse` transformado em flag, e removido a necessidade de informar valor;
### Fixed
  - Correção em testes para CI/CD;

## [0.10.0]	 &#8212; 	2024-08-26:
### Added
  - Gerenciador de pacotes poetry para projeto;
  - Pacote `ruff` adicionado como formatador e validador de estilos;
### Changed
  - Ambiente virtual local, para melhor funcionamento em Windows;
  - Melhoria de performance de metodos da geração de `CHANGELOG.md`;
  - Formatação e validação de código ruff aplicados;

## [0.9.0]	 &#8212; 	2024-05-14:
### Added
  - Acrescentado traduções para `código de conduta` (DE, EN, ES, PT, FR, IT);
  - Acrescentado traduções para  `semver.md` (DE, EN, ES, PT, FR, IT);
### Changed
  - Atualizado badges da página inicial da documentação;
  - Atualizado badges do README;
  - Atualização da estrutura do README do projeto;
  - Atualizado exemplos de utilização de métodos para API.;
  - Exemplos de utilização do programa na documentação;

## [0.9.0rc0]	 &#8212; 	2024-01-16:
### Added
  - Acrescentado traduções para `código de conduta` (DE, EN, ES, PT, FR, IT);
  - Acrescentado traduções para  `semver.md` (DE, EN, ES, PT, FR, IT);
### Changed
  - Exemplos de utilização do programa na documentação.;

## [0.8.0]	 &#8212; 	2024-01-06:
### Added
  - Acrescentado campo de busca na documentação da API;
  - Acrescentado modo noturno na página oficial de documentação da API;
  - Acrescentado suporte a multiplos idiomas para documentação;
  - Acrescentado tradução do código de contuda em italiano;
  - Acrescentado tradução do código de contuda em francês;
  - Acrescentado tradução do código de contuda em espanhol;
  - Acrescentado tradução do código de contuda em alemão;
  - Acrescentado tradução do código de contuda em inglês;
  - Acrescentado tradução do contributors.md em inglês;
  - Acrescentado tradução do zenpy.md em inglês;
### Deprecated
  - Será substituído em breve o pacote `isort`;
### Fixed
  - Redefinido renderização de rodapé do arquivo CHANGELOG.md;

## [0.7.0]	 &#8212; 	2024-01-05:
### Added
  - Formatador de código redefindo com `ruff`;
  - Adicionado badges de `wheel` e `stable`;
### Changed
  - Renomeado workflow CI/CD `python-package.yml -> unit-tests.yml`;
  - Atualização da documentação com exemplos de utilização da API;
  - Reativação dos scripts de automação `taskipy`;
  - Reativação dos scripts de automação `makefile`;
  - Reativação dos scripts de automação `tox`;
  - Informações referente ao projeto atualizadas na página de documentação;
### Removed
  - Removido pacote `blue`;
  - Desativado formatador `blue` em CI/CD;

## [0.6.2]	 &#8212; 	2024-01-04:
### Added
  - Ativação da configuração `Codecov.io`.;
### Fixed
  - Correção na excução de testes unitários em CI/CD;
  - Correção de geração de relatório de cobertura no container CI/CD.;

## [0.6.1]	 &#8212; 	2024-01-02:
### Fixed
  - Habilitado diretiva `workflow_dispatch` para executar workflow manualmente;

## [0.6.0]	 &#8212; 	2024-01-02:
### Fixed
  - Correção na excução de testes unitários em CI/CD;

## [0.6.0rc0]	 &#8212; 	2024-01-02:
### Fixed
  - Correção na excução de testes unitários em CI/CD;

## [0.5.0]	 &#8212; 	2024-01-01:
### Fixed
  - Correção em ações de fluxo CI/CD;
  - Sanado conflito entre ferramentas de validação de tipo;
  - Sanado conflito entre ferramentas de ordenação de pacotes;
  - Sanado conflito entre ferramentas lint;

## [0.5.0rc0]	 &#8212; 	2023-12-31:
### Fixed
  - Sanado conflito entre ferramentas de validação de tipo;
  - Sanado conflito entre ferramentas de ordenação de pacotes;
  - Sanado conflito entre ferramentas lint;

## [0.4.0]	 &#8212; 	2023-12-31:
### Changed
  - Atualizado verificação de tipo estático `mypy` para compatibilidade de versão a partir do Python 3.8;
  - Atualizado logo do projeto;
### Fixed
  - Ajuste de conflitos entre ruff e mypy;
  - Recuperado cobertura de 100% no módulo changelog.cli;

## [0.3.0]	 &#8212; 	2023-12-24:
### Added
  - Acrescentado validação CI/CD multiplataforma ao projeto;
  - Definido checagem lint via ruff para CI/CD;
  - Incluído guia para markdown no menu da documentação;
  - Incluído validação CI/CD para QA (Quality Assurance);
  - Acrescentado suporte a Python 3.12;
  - Acrescentado fluxo para publicação em TestPyPi;
  - Acrescentado fluxo para publicação em Pypi;
  - Acrescentado fluxo CI/CD para geração de documentação;
  - Acrescentado documentação web online (https://development-incolume.github.io/incolume.py.changelog/);
### Changed
  - Atingido cobertura de 100% no módulo changelog.cli;
  - Atingido cobertura de 100% no módulo changelog.changelog;
  - Atingido cobertura de 100% no módulo changelog;
  - Acrescentado exemplos dos métodos da API;
  - Uniformizado testes multiplataforma para (Linux e Windows);
  - Cobertura parcial para estilo mypy;

## [0.3.0rc4]	 &#8212; 	2023-12-24:
### Added
  - Acrescentado validação CI/CD multiplataforma ao projeto;
  - Definido checagem lint via ruff para CI/CD;
  - Incluído guia para markdown no menu da documentação;
  - Incluído validação CI/CD para QA (Quality Assurance);
  - Acrescentado suporte a Python 3.12;
  - Acrescentado fluxo para publicação em TestPyPi;
  - Acrescentado fluxo para publicação em Pypi;
  - Acrescentado fluxo CI/CD para geração de documentação;
  - Acrescentado documentação web online;
### Changed
  - Atingido cobertura de 100% no módulo changelog.cli;
  - Atingido cobertura de 100% no módulo changelog.changelog;
  - Atingido cobertura de 100% no módulo changelog;
  - Acrescentado exemplos dos métodos da API;
  - Uniformizado testes multiplataforma para (Linux e Windows);
  - Cobertura parcial para estilo mypy;

## [0.3.0rc3]	 &#8212; 	2023-12-24:
### Added
  - Acrescentado validação CI/CD multiplataforma ao projeto;
  - Definido checagem lint via ruff para CI/CD;
  - Incluído guia para markdown no menu da documentação;
  - Incluído validação CI/CD para QA (Quality Assurance);
  - Acrescentado suporte a Python 3.12;
  - Acrescentado fluxo para publicação em TestPyPi;
  - Acrescentado fluxo para publicação em Pypi;
  - Acrescentado fluxo CI/CD para geração de documentação;
  - Acrescentado documentação web online;
### Changed
  - Atingido cobertura de 100% no módulo changelog.cli;
  - Atingido cobertura de 100% no módulo changelog.changelog;
  - Atingido cobertura de 100% no módulo changelog;
  - Acrescentado exemplos dos métodos da API;
  - Uniformizado testes multiplataforma para (Linux e Windows);
  - Cobertura parcial para estilo mypy;

## [0.3.0rc2]	 &#8212; 	2023-12-23:
### Added
  - Acrescentado validação CI/CD multiplataforma ao projeto;
  - Definido checagem lint via ruff para CI/CD;
  - Incluído guia para markdown no menu da documentação;
  - Incluído validação CI/CD para QA (Quality Assurance);
  - Acrescentado suporte a Python 3.12;
  - Acrescentado fluxo para publicação em TestPyPi;
  - Acrescentado fluxo para publicação em Pypi;
### Changed
  - Atingido cobertura de 100% no módulo changelog.cli;
  - Atingido cobertura de 100% no módulo changelog.changelog;
  - Atingido cobertura de 100% no módulo changelog;
  - Acrescentado exemplos dos métodos da API;
  - Uniformizado testes multiplataforma para (Linux e Windows);
  - Cobertura parcial para estilo mypy;

## [0.3.0rc1]	 &#8212; 	2023-12-23:
### Added
  - Acrescentado validação CI/CD multiplataforma ao projeto;
  - Definido checagem lint via ruff para CI/CD;
  - Incluído guia para markdown no menu da documentação;
  - Incluído validação CI/CD para QA (Quality Assurance);
  - Acrescentado suporte a Python 3.12;
  - Acrescentado fluxo para publicação em TestPyPi;
### Changed
  - Atingido cobertura de 100% no módulo changelog.cli;
  - Atingido cobertura de 100% no módulo changelog.changelog;
  - Atingido cobertura de 100% no módulo changelog;
  - Acrescentado exemplos dos métodos da API;
  - Uniformizado testes multiplataforma para (Linux e Windows);
  - Cobertura parcial para estilo mypy;

## [0.3.0rc0]	 &#8212; 	2023-12-23:
### Added
  - Acrescentado validação CI/CD multiplataforma ao projeto;
  - Definido checagem lint via ruff para CI/CD;
  - Incluído guia para markdown no menu da documentação;
  - Incluído validação CI/CD para QA (Quality Assurance);
  - Acrescentado suporte a Python 3.12;
### Changed
  - Atingido cobertura de 100% no módulo changelog.cli;
  - Atingido cobertura de 100% no módulo changelog.changelog;
  - Atingido cobertura de 100% no módulo changelog;
  - Acrescentado exemplos dos métodos da API;
  - Uniformizado testes multiplataforma para (Linux e Windows);
  - Cobertura parcial para estilo mypy;

## [0.2.0]	 &#8212; 	2023-12-21:
### Added
  - Pacotes de documentação;
  - Pacotes de segurança de software;
  - Pacotes de desenvolvimento;
  - Pacote types-toml;
  - Ferramentas de QA;
  - Documentação padrão(Google Style);
  - Documentação de API;
  - Badges para documentação;
  - Estilo PEP8;
  - 100% de cobertura no módulo cli;
  - Compatibilidade com Python 3.8;
  - Validação com ruff para todas as versões de Python configuradas;
  - CI/CD funcional para multiplataforma;
### Changed
  - README atualizado;
  - Menu atualizado;
  - Caracteres para Slugfy no nome do brach;
  - Realocação de Changelog para diretório docs;
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

# Guia de contribuíção (Desenvolvimento)

O desenvolvimento deste projeto segue algumas regras e convenções
básicas. Como _estilo de formatação de código_,

## Código de conduta

Detalhes em [docs/user_guide/code_of_conduct.md](code_of_conduct.md).

## Padrões aplicados

Este projeto segue as recomendações descritas em
[Tecnologias](../prefacio.md#tecnologias-adotadas) e
[Convenções](../prefacio.md#convenções-adotadas) Adotadas.


## Prerequisitos

    - Sistema Operacional Linux Like (preferencialmente) ou WSL
    - git client
    - python 3.10+
    - pyenv + pip; ou
    - pyenv + poetry 1.2.0+;
    - uv 0.8.11+ (preferencialmente);


## Iniciando ambiente de desenvolvimento

Para definir a versão do Python para o ambiente, considerando o uso do `uv` ou `poetry`,
e instalar as dependências execute os comandos abaixo:

### com uv

    $ uv sync -p 3.10

### com poetry

    $ poetry env use 3.10
    $ poetry install

Estes comandos criarão um ambiente virtual em Python, na versão especificada,
apresentada no exemplo como 3.10, e instalará todas as dependências fixadas em `pyproject.toml` com suas
restrições especificadas em `uv.lock` ou `poetry.lock`.

Após o ambiente criado com suas dependências instaladas, execute o comando referente ao gerenciador escolhido:

    $ uv run task setup;

ou

    $ poetry run task setup

Este comando garantirá que os hooks do projeto sejam ativados, e executados nos eventos apropriados.

## Qualidade de Código

É utilizado de ferramentas validadoras de qualidade de código estático,
também denominadas linters.

Há uso das seguintes:

    - black / blue
    - isort
    - mypy
    - pydocstyle
    - pylint
    - ruff

Entretanto todos concentrados na ferramenta `ruff`, para ganho de performance e simplicidade na configuração.

## Segurança e Garantia de Qualidade

Neste projeto há preocupação com a garantia de qualidade (Quality Assurance) e também com a segurança do código implementado, os pacotes
`bandit`, `pip-audit` e `safety` são utilizados para monitoramento de segurança das dependências.

## Mas que pacotes e ferramentas são estas no projeto?

### bandit

Bandit é uma ferramenta projetada para encontrar problemas de segurança comuns no código Python. Para fazer isso, o Bandit processa cada arquivo, cria um AST a partir dele e executa os plug-ins apropriados nos nodos do AST.
Depois que o Bandit terminar de escanear todos os arquivos, ele gerará um relatório.
    ```shell
    bandit -c pyproject.toml -r incolume/ test/
    ```

### black

O `black` é classificado como Autoformator, são programas que
refatoram seu código para se adequar ao PEP 8 automaticamente.
    ```shell
    black --check incolume/ tests/
    ```

### blue

o blue é um autoformatador de código um pouco menos intransigente do
que o black, e segue a ideia de formatar automaticamente o código
Python, totalmente inspirada pelo black.
    ```shell
    blue --check incolume/ tests/
    ```

### flake8

Flake8 é um envolucro em torno das ferramentas: PyFlakes, pycodestyle e Roteiro McCabe de Ned Batchelder
    ```shell
    flake8 --config pyproject.toml incolume/ tests/
    ```

### pylama

O `pylama` é um envolucro que contém: PyFlakes, pycodestyle, McCabe.

    ```shell
    pylama incolumepy tests
    ```

### isort

O `isort` é um utilitário para classificar as importações
em ordem alfabética e separadas automaticamente em seções e por tipo.
    ```shell
    isort incolumepy tests
    ```

### mypy

O `Mypy` é essencialmente um analizador de código estático melhorado e com
verificador de tipos, que pode detectar muitos erros de programação
analisando o código, sem precisar executá-lo.
Ele possui um poderoso sistema de tipos com recursos como
inferência de tipos, digitação gradual, genéricos e tipos de união.
    ```shell
    mypy incolumepy
    ```

### pip-audit

O `pip-audit` é uma ferramenta para escanear pacotes em ambientes Python que possuem vulnerabilidades conhecidas.
Este pacote faz uso do Python Packaging Advisory Database (https://github.com/pypa/advisory-database) através da API PyPI JSON como relatório de vulnerabilidade de código
    ```shell
    pip-audit
    ```

### pydocstyle

O `pydocstyle` é uma ferramenta de análise estática para verificar a
conformidade com as convenções docstring do Python. Ele suporta a maior
parte do PEP 257, entretanto não deve ser considerado uma
implementação de referência.
    ```shell
    pydocstyle incolumepy tests
    ```

### pylint

O `Pylint` é uma ferramenta de análise de código estático do Python
que procura erros de programação, ajuda a impor um padrão de codificação,
detecta cheiros de código e oferece sugestões simples de refatoração.
É altamente configurável, possuindo pragmas especiais para controlar
seus erros e avisos de dentro do seu código, bem como de um extenso
arquivo de configuração. Também é possível escrever seus próprios plugins
para adicionar suas próprias verificações ou para estender o `pylint`
de uma forma ou de outra.
    ```shell
    pylint incolumepy tests
    ```

### ruff

O `ruff` é um linter Python extremamente rápido, codificado em rust.

Ruff  pode ser usado para substituir Flake8 (mais dezenas de plugins), Black, Blue, isort, pydocstyle, pyupgrade, autoflake, e mais, tudo isso enquanto executa dezenas ou centenas de vezes mais rápido do que qualquer ferramenta individual.

    **Autoformatador (Ruff format)**

    `ruff format` é o ponto de entrada principal para o formatador. Ele aceita uma lista de arquivos ou diretórios e formata todos os arquivos Python descobertos:
        ```shell
        ruff format .
        ruff format incolume/ tests/
        ```

    **Verificador linter (Ruff check)**

    `ruff check` é o ponto de entrada principal para o linter Ruff. Ele aceita uma lista de arquivos ou diretórios e lint todos os arquivos Python descobertos, corrigindo opcionalmente quaisquer erros corrigíveis:
        ```shell
        ruff check .
        ```

    **Corretor linter (Ruff check fix)**

    `ruff` oferece suporte a correções automáticas para uma variedade de erros de lint. Por exemplo, Ruff pode remover importações não utilizadas, reformatar docstrings, reescrever anotações de tipo para usar a sintaxe Python mais recente e muito mais.

    Para habilitar correções, passe o `--fix` sinalizador para ruff check:
        ```shell
        ruff check . --fix
        ```

### safety

O `safety` verifica as dependências instaladas quanto a vulnerabilidades
de segurança conhecidas.
Por padrão, ele usa o banco de dados de vulnerabilidades Python aberto
[Safety DB](https://github.com/pyupio/safety-db).
    ```shell
    safety check
    ```

### uv

O `uv` gerencia dependências e ambientes de projetos, com suporte para lockfiles, workspaces e muito mais semelhante ao `poetry`, também oferece suporte à construção e publicação de projetos, mesmo que eles não sejam gerenciados com o UV.

### poetry

O `poetry` é uma ferramenta para gestão de dependências e pacotes Python. Ele permite que seja declarado as bibliotecas das quais o projeto depende e as gerenciará (instalará/atualizará) de forma facilitada. O Poetry oferece um arquivo de bloqueio para garantir instalações repetíveis e pode construir seu projeto para distribuição.

### pip

`pip` é um sistema de gerenciamento de pacotes padrão usado para instalar e gerenciar pacotes de software escritos em Python. Muitos pacotes podem ser encontrados no indice oficial de pacotes denominado *Python Package Index (PyPI)*.

### pyenv

`Pyenv` é uma ferramenta para gerenciar ambientes virtuais independentes com versões distintas do interpretador Python em um sistema operacional sem comprometer a instalação nativa. Ele permite que você altere facilmente a versão global do Python utilizada em seu sistema, bem como a versão específica de cada projeto. Isso é útil para garantir a compatibilidade com vários projetos que possam exigir versões diferentes do Python.

### git

o `git` é um sistema de controle de versões distribuído, usado principalmente no desenvolvimento de software, mas pode ser usado para registrar o histórico de edições de qualquer tipo de arquivo (como livros, dissertações, monografias, código de software, ). O Git foi inicialmente projetado e desenvolvido por Linus Torvalds para o desenvolvimento do kernel Linux, mas foi adotado por muitos outros projetos.

Cada diretório de trabalho do Git é um repositório com um histórico completo e habilidade total de acompanhamento das revisões, não dependente de acesso a uma rede ou a um servidor central, também facilita a reprodutibilidade científica em uma ampla gama de disciplinas.

Além disto é um software livre, distribuído sob os termos da versão 2 da GNU General Public License.

## Ferramentas de Automação

Para facilitar o trabalho, várias das tarefas estão
automatizadas pelo githooks, e/ou Makefile, e/ou tox e/ou taskipy.

### Tox

#### Verificação básica

Na Verificação básica engloba:
    - black
    - blue
    - isort
    - pydocstyle
    - mypy
    - pylint
    - py310
    - py311

    ```shell
    tox
    ```

#### Verificação dos testes com as versões python disponíveis

    ```shell
    tox -e py310,py311
    ```

#### Verificação de três linters apenas no em um módulo

    ```shell
    tox -e pydocstyle,black,isort -- -k incolume/py/pack/module.py
    ```

#### Verificação de todos os linters configurados

    ```shell
    tox -e linters
    ```

#### Verificação e relatório de cobertura

    ```shell
    tox -e stats
    ```

#### Verificação resumida de segurança

    ```shell
    tox -e safety
    ```

#### Execução completa

Executa todas as verificações diponíveis contidas no `tox`.
    ```shell
    tox -e ALL
    ```

### Makefile

O `Makefile` foi personalizado para rodar com as opções necessárias.
Com o help você verá todas as opções. Este comando é exclusivo para linux like.
    ```shell
    make help
    ```

#### Iniciar ambiente dev

Através do `Makefile`, pode-se criar um ambiente virtual para o projeto,
conforme a versão python predefinida, instalando todas as dependências
necessárias, além de ativar as configurações em passos simples.

    ```shell
    make setup
    ```

#### Limpeza básica do ambiente

Limpeza de arquivos temporários, logs, compilados e afins.
    ```shell
    make clean
    ```

#### Limpeza profunda do ambiente

Além da limpeza básica, são removidos dist, build, htmlcov, .tox, *_cache,
e outros conteúdos gerados pelas ferramentas de desenvolvimento.
    ```shell
    make clean-all
    ```

#### Gerar a documentação atualizada

    ```shell
    make docsgen
    ```

#### Verificação de segurança e exposição de motivos

    ```shell
    make safety
    ```


### Taskipy

Com `taskipy` as tarefas são definidas puramente com Python em um arquivo
e pode-se executar rotinas complexas com comandos simples.

    ```shell
    $ poetry run task -l

    bandit          poetry run bandit -c pyproject.toml -r incolume/ test/
    check-all       Checking all
    clean           Shallow clean into environment (.pyc, .cache, .egg, .log, et all)
    clean-all       Deep cleanning into environment (dist, build, htmlcov, .tox, *_cache, et all)
    docs-build      Generate documentation
    docs-serve      Run server documentation
    lint            Checking all linters configurated
    lint_black      Checking with black
    lint_blue       Checking with blue
    lint_flake8     Checking with flake8
    lint_isort      Checking with isort
    lint_mypy       Checking with mypy
    lint_pydocstyle Checking with pydocstyle
    lint_pylint     Checking with pylint
    patch           Generate a patch Sematic Version
    premajor        poetry version premajor
    preminor        poetry version preminor
    prerelease      poetry version prerelease
    safety          Check safety of packages into project.
    sec             Checking environment's safety
    changelog       Update changelog file
    setup           Configure environment develop
    ```

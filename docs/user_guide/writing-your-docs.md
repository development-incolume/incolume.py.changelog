## Bem-vindo ao MkDocs

Para documentação completa acesse [mkdocs.org](https://www.mkdocs.org).

## Comandos

* `mkdocs new [dir-name]` - Criar um novo projeto.
* `mkdocs serve` - Iniciar o auto carregamento para docs server.
* `mkdocs build` - Compilar o site de documetação.
* `mkdocs -h` - Exibe a menssagem de ajuda e saí.

## Layout do projeto

    mkdocs.yml    # O arquivo de configuração.
    docs/
        index.md  # A página de documentação.
        ...       # Outras páginas markdown, imagens e demais arquivos.

## Documentação Web aplicada em github pages
    mkdocs gh-deploy --config-file mkdocs.yml --remote-branch webdoc

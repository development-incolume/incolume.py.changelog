## Bienvenido a MkDocs

Para obtener la documentación completa, visite [mkdocs.org](https://www.mkdocs.org).

## Comandos

* `mkdocs new [dir-name]` - Crea un nuevo proyecto.
* `mkdocs serve` - Inicia la carga automática para el servidor de documentos.
* `mkdocs build` - Construye el sitio de documentación.
* `mkdocs -h` - Muestra el mensaje de ayuda y sale.

## Diseño del proyecto

    mkdocs.yml    # El archivo de configuración.
    docs/
        index.md  # La página de documentación.
        ...       # Otras páginas markdown, imágenes y demás archivos.

## Documentación web aplicada en GitHub Pages

    mkdocs gh-deploy --config-file mkdocs.yml --remote-branch webdoc

## Bienvenido a MkDocs

Para obtener la documentación completa, visite [mkdocs.org](https://www.mkdocs.org).

## Comandos

* `mkdocs new [dir-name]` - Crea un nuevo proyecto.
* `mkdocs serve` - Inicia la carga automática para el servidor de documentos.
* `mkdocs build` - Construye el sitio de documentación.
* `mkdocs -h` - Mostrar el mensaje de ayuda y salir.

## Diseño del proyecto

    mkdocs.yml # El archivo de configuración.
 docs/
 index.md # La página de documentación.
...       # Otras páginas markdown, imágenes y otros archivos.

## Documentación web aplicada a las páginas de github
 mkdocs gh-deploy --config-file mkdocs.yml --remote-branch webdoc

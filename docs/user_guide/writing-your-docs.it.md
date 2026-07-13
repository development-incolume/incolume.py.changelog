## Benvenuti in MkDocs

Per una documentazione completa, visitare [mkdocs.org](https://www.mkdocs.org).

## Comandi

* `mkdocs new [dir-name]` - Crea un nuovo progetto.
* `mkdocs serve` - Avvia il caricamento automatico per il server docs.
* `mkdocs build` - Costruisce il sito di documentazione.
* `mkdocs -h` - Visualizza il messaggio di aiuto ed esce.

## Layout del progetto

    mkdocs.yml # Il file di configurazione.
 docs/
 index.md # La pagina di documentazione.
...       # Altre pagine markdown, immagini e altri file.

## Documentazione web applicata alle pagine github
 mkdocs gh-deploy --config-file mkdocs.yml --remote-branch webdoc

## Willkommen bei MkDocs

Die vollständige Dokumentation finden Sie auf [mkdocs.org](https://www.mkdocs.org).

## Befehle

* `mkdocs new [dir-name]` - Erzeugt ein neues Projekt.
* `mkdocs serve` - Startet das automatische Laden für den Docs-Server.
* `mkdocs build` - Erstellt die Dokumentationsseite.
* `mkdocs -h` - Anzeige der Hilfemeldung und Beenden.

## Projekt-Layout

    mkdocs.yml # Die Konfigurationsdatei.
 docs/
 index.md # Die Dokumentationsseite.
...       # Andere Markdown-Seiten, Bilder und andere Dateien.

## Web-Dokumentation auf Github-Seiten angewendet
 mkdocs gh-deploy --config-file mkdocs.yml --remote-branch webdoc

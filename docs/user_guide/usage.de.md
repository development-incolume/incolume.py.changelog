# Verwendung

Wie man das `CHANGELOG.md` mit `incolume.py.changelog` erzeugt und pflegt.

## Anforderungen

- Git-Repository mit **annotierten Tags** (die Annotation ist die Quelle des CHANGELOG).
- Umgebung mit Python `>=3.11,<4` und `uv` (siehe
  [Installation](INSTALLATION.md)).

## CHANGELOG erzeugen

```shell
uv run task changelog
```

Der Befehl liest `git tag -n`, klassifiziert die Meldungen und schreibt die
konfigurierte Datei (standardmäßig `docs/about/CHANGELOG.md`).

Die Datei wird **erzeugt** — sie sollte nicht von Hand bearbeitet werden.

## CLI

| Befehl | Beschreibung |
|---|---|
| `changelog [DATEI]` | Erzeugt das CHANGELOG in der angegebenen Datei |
| `gcl`, `gencl`, `gchangelog` | Aliase des obigen Befehls |
| `greeting [NAME]` | Beispielbegrüßung |

Optionen von `changelog`:

| Option | Kurzform | Beschreibung |
|---|---|---|
| `--url` | `-u` | Basis-Vergleichs-URL |
| `--reverse` | `-r` | Umgekehrte Reihenfolge (neueste zuerst) |
| `--generate-config` | `-g` | Erzeugt eine Beispiel-Konfigurationsdatei |

## Konfiguration

Dateien in dieser Reihenfolge gesucht: `changelog.toml`, `.changelog.toml`,
`pyproject.toml` (Abschnitt `[tool.changelog.settings]`).

```toml
[settings]
file = "docs/about/CHANGELOG.md"
reverse = true
url_compare = "https://github.com/development-incolume/incolume.py.changelog/compare"
url_keepachangelog = "https://keepachangelog.com/en/1.0.0"
url_semver = "https://semver.org/spec/v2.0.0.html"
url_convetional_commit = "https://www.conventionalcommits.org/pt-br/v1.0.0"
```

Die Konfiguration kann partiell sein (jede Teilmenge der Schlüssel).

## Tag-Annotation

Eine Zeile pro Tag, mit Kategorien getrennt durch `;`:

```text
1.5.0  added: neue Funktion; fixed: Fehlerbehebung;
```

Akzeptierte Kategorien: `Added`, `Changed`, `Deprecated`, `Removed`, `Fixed`,
`Security` und die pt-BR-Äquivalente (`Adicionado`, `Modificado`, `Obsoleto`,
`Removido`, `Corrigido`, `Segurança`).

## Python-API

```python
from incolume.py.changelog.changelog import update_changelog

update_changelog(changelog_file='docs/about/CHANGELOG.md', reverse=True)
```

## Siehe auch

- [Installation](INSTALLATION.md)
- [API-Dokumentation](../api/index.md)
- [Entwicklung](development.md)

# Guida all'uso

Come generare e mantenere il `CHANGELOG.md` con `incolume.py.changelog`.

## Prerequisiti

- Repository git con **tag annotati** (l'annotazione è la fonte del CHANGELOG).
- Ambiente con Python `>=3.11,<4` e `uv` (vedi
  [Installazione](INSTALLATION.md)).

## Generare il CHANGELOG

```shell
uv run task changelog
```

Il comando legge `git tag -n`, classifica i messaggi e scrive il file
configurato (per impostazione predefinita `docs/about/CHANGELOG.md`).

Il file è **generato** — non deve essere modificato a mano.

## CLI

| Comando | Descrizione |
|---|---|
| `changelog [FILE]` | Genera il CHANGELOG nel file indicato |
| `gcl`, `gencl`, `gchangelog` | Alias del comando precedente |
| `greeting [NOME]` | Saluto di esempio |

Opzioni di `changelog`:

| Opzione | Scorciatoia | Descrizione |
|---|---|---|
| `--url` | `-u` | URL base di confronto |
| `--reverse` | `-r` | Ordine inverso (il più recente per primo) |
| `--generate-config` | `-g` | Genera un file di configurazione di esempio |

## Configurazione

File cercati, in ordine: `changelog.toml`, `.changelog.toml`,
`pyproject.toml` (sezione `[tool.changelog.settings]`).

```toml
[settings]
file = "docs/about/CHANGELOG.md"
reverse = true
url_compare = "https://github.com/development-incolume/incolume.py.changelog/compare"
url_keepachangelog = "https://keepachangelog.com/en/1.0.0"
url_semver = "https://semver.org/spec/v2.0.0.html"
url_convetional_commit = "https://www.conventionalcommits.org/pt-br/v1.0.0"
```

La configurazione può essere parziale (qualsiasi sottoinsieme delle chiavi).

## Annotazione dei tag

Una riga per tag, con categorie separate da `;`:

```text
1.5.0  added: nuova funzionalità; fixed: correzione di un bug;
```

Categorie accettate: `Added`, `Changed`, `Deprecated`, `Removed`, `Fixed`,
`Security` e le equivalenti pt-BR (`Adicionado`, `Modificado`, `Obsoleto`,
`Removido`, `Corrigido`, `Segurança`).

## API Python

```python
from incolume.py.changelog.changelog import update_changelog

update_changelog(changelog_file='docs/about/CHANGELOG.md', reverse=True)
```

## Vedi anche

- [Installazione](INSTALLATION.md)
- [Documentazione dell'API](../api/index.md)
- [Sviluppo](development.md)

# Guide d'utilisation

Comment générer et maintenir le `CHANGELOG.md` avec `incolume.py.changelog`.

## Prérequis

- Dépôt git avec des **tags annotés** (l'annotation est la source du CHANGELOG).
- Environnement avec Python `>=3.11,<4` et `uv` (voir
  [Installation](INSTALLATION.md)).

## Générer le CHANGELOG

```shell
uv run task changelog
```

La commande lit `git tag -n`, classe les messages et écrit le fichier
configuré (par défaut `docs/about/CHANGELOG.md`).

Le fichier est **généré** — il ne doit pas être modifié à la main.

## CLI

| Commande | Description |
|---|---|
| `changelog [FICHIER]` | Génère le CHANGELOG dans le fichier indiqué |
| `gcl`, `gencl`, `gchangelog` | Alias de la commande ci-dessus |
| `greeting [NOM]` | Salutation d'exemple |

Options de `changelog` :

| Option | Raccourci | Description |
|---|---|---|
| `--url` | `-u` | URL de comparaison de base |
| `--reverse` | `-r` | Ordre inverse (le plus récent en premier) |
| `--generate-config` | `-g` | Génère un fichier de configuration d'exemple |

## Configuration

Fichiers recherchés, dans l'ordre : `changelog.toml`, `.changelog.toml`,
`pyproject.toml` (section `[tool.changelog.settings]`).

```toml
[settings]
file = "docs/about/CHANGELOG.md"
reverse = true
url_compare = "https://github.com/development-incolume/incolume.py.changelog/compare"
url_keepachangelog = "https://keepachangelog.com/en/1.0.0"
url_semver = "https://semver.org/spec/v2.0.0.html"
url_convetional_commit = "https://www.conventionalcommits.org/pt-br/v1.0.0"
```

La configuration peut être partielle (tout sous-ensemble des clés).

## Annotation des tags

Une ligne par tag, avec les catégories séparées par `;` :

```text
1.5.0  added: nouvelle fonctionnalité; fixed: correction de bug;
```

Catégories acceptées : `Added`, `Changed`, `Deprecated`, `Removed`, `Fixed`,
`Security` et les équivalentes pt-BR (`Adicionado`, `Modificado`, `Obsoleto`,
`Removido`, `Corrigido`, `Segurança`).

## API Python

```python
from incolume.py.changelog.changelog import update_changelog

update_changelog(changelog_file='docs/about/CHANGELOG.md', reverse=True)
```

## Voir aussi

- [Installation](INSTALLATION.md)
- [Documentation de l'API](../api/index.md)
- [Développement](development.md)

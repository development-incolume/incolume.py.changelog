# Guía de uso

Cómo generar y mantener el `CHANGELOG` con `incolume.py.changelog`.

## Requisitos

- Repositorio git con **etiquetas anotadas** (la anotación es la fuente del CHANGELOG).
- Entorno con Python `>=3.11,<4` y `uv` (ver
  [Instalación](INSTALLATION)).

## Generar el CHANGELOG

```shell
uv run task changelog
```

El comando lee `git tag -n`, clasifica los mensajes y escribe el archivo
configurado (por defecto `docs/about/CHANGELOG`).

El archivo se **genera** — no debe editarse a mano.

## CLI

| Comando | Descripción |
|---|---|
| `changelog [ARCHIVO]` | Genera el CHANGELOG en el archivo indicado |
| `gcl`, `gencl`, `gchangelog` | Alias del comando anterior |
| `greeting [NOMBRE]` | Saludo de ejemplo |

Opciones de `changelog`:

| Opción | Atajo | Descripción |
|---|---|---|
| `--url` | `-u` | URL base de comparación |
| `--reverse` | `-r` | Orden inverso (el más reciente primero) |
| `--generate-config` | `-g` | Genera un archivo de configuración de ejemplo |

## Configuración

Archivos buscados, en orden: `changelog.toml`, `.changelog.toml`,
`pyproject.toml` (sección `[tool.changelog.settings]`).

```toml
[settings]
file = "docs/about/CHANGELOG"
reverse = true
url_compare = "https://github.com/development-incolume/incolume.py.changelog/compare"
url_keepachangelog = "https://keepachangelog.com/en/1.0.0"
url_semver = "https://semver.org/spec/v2.0.0.html"
url_convetional_commit = "https://www.conventionalcommits.org/pt-br/v1.0.0"
```

La configuración puede ser parcial (cualquier subconjunto de las claves).

## Anotación de las etiquetas

Una línea por etiqueta, con categorías separadas por `;`:

```text
1.5.0  added: nueva funcionalidad; fixed: corrección de error;
```

Categorías aceptadas: `Added`, `Changed`, `Deprecated`, `Removed`, `Fixed`,
`Security` y las equivalentes pt-BR (`Adicionado`, `Modificado`, `Obsoleto`,
`Removido`, `Corrigido`, `Segurança`).

## API de Python

```python
from incolume.py.changelog.changelog import update_changelog

update_changelog(changelog_file='docs/about/CHANGELOG', reverse=True)
```

## Ver también

- [Instalación](INSTALLATION)
- [Documentación de la API](../api/index)
- [Desarrollo](development)

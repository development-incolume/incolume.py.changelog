# Mantener un registro de cambios

## ¿Qué es un registro de cambios?
Un registro de cambios es un archivo que contiene una lista seleccionada, ordenada cronológicamente, de los cambios significativos de cada versión de un proyecto.

## ¿Por qué mantener un registro de cambios?
Para facilitar a los usuarios y colaboradores la visualización precisa de los cambios significativos que se han realizado entre cada versión publicada de un proyecto.

## ¿Quién necesita un registro de cambios?
Las personas lo necesitan. Ya sean consumidores o desarrolladores, los usuarios finales del software son seres humanos que se preocupan por lo que hay en el software. Cuando el software cambia, la gente quiere saber por qué y cómo.

## ¿Cómo hacer un buen registro de cambios?
### Principios fundamentales
- Los registros de cambios son para humanos, no para máquinas.
- Debe haber una entrada para cada versión.
- Los cambios del mismo tipo deben agruparse.
- Las versiones y secciones deben ser enlazables (con enlaces).
- La versión más reciente aparece en primer lugar.
- Se muestra la fecha de lanzamiento de cada versión.
- Indique si sigue el [versionado semántico](https://semver.org/).


### Tipos de cambios
- **Added**: (Añadido) para nuevas características.
- **Changed**: (Modificado) para cambios en características existentes.
- **Deprecated**: (Obsoleto) para características que se eliminarán en próximas versiones.
- **Removed**: (Eliminado) para características eliminadas en esta versión.
- **Fixed**: (Corregido) para cualquier corrección de errores.
- **Security**: (Seguridad) en caso de vulnerabilidades.

## ¿Cómo aplicar el registro de cambios en este proyecto?
 Este proyecto utiliza el paquete python incolumepy.utils, que tiene la
   prerrogativa de crear un `CHANGELOG.md` automáticamente a partir de las
entradas de `git tag -n`.

Ejemplos:
```shell
git tag -f Unreleased -m 'added: Se han añadido instrucciones sobre Keep a CHANGELOG.md en docs/user_guide/keep-a-chagelog.md'
git tag -f `poetry version -s` -m “added: Se han añadido instrucciones sobre Keep a CHANGELOG.md en docs/user_guide/keep-a-chagelog.md”
git tag -f 1.0.0 -m 'Added: (Añadido) para nuevas funciones;
Changed: (Modificado) para cambios en funciones existentes;
Obsoleto: (Obsoleto) para recursos que se eliminarán en próximas versiones;
Eliminado: (Eliminado) para recursos eliminados en esta versión;
Corregido: (Corregido) para cualquier corrección de errores;
Seguridad: (Seguridad) en caso de vulnerabilidades;'
```

### Actualizar CHANGELOG.md
```shell
task gcl
```

## Referencia
- https://keepachangelog.com/pt-BR/1.0.0/

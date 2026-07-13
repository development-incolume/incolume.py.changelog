# Git commits messages

---

Este proyecto sigue Conventional Commits, una especificación para añadir un significado legible por humanos y máquinas
a los mensajes de confirmación.

```bash
<tipo>[ámbito opcional]: <descripción>

[cuerpo opcional]

[pie(s) de página opcional(es)]
```

La confirmación contiene los siguientes elementos estructurales, para comunicar la intención a los consumidores de su biblioteca:

**type**: el tipo de confirmación (feat|feature, fix|bugfix, chore, refactor, docs, style, test, perf, ci, build, revert)
    + **feat**: Un commit del tipo feat introduce una nueva característica en el código base (esto se correlaciona con MINOR en el Versionado Semántico).
    + **fix** o **bugfix**: Una confirmación del tipo fix corrige un error del código base (se corresponde con PATCH en el versionado semántico).
    + **chore**: Cambios que no están relacionados con una corrección o funcionalidad y no modifican los archivos src o de prueba (por ejemplo, actualización de dependencias);
    + **refactor**: código refactorizado que no corrige un error ni añade una característica;
    + **docs**: actualizaciones de la documentación, como el README u otros archivos markdown o rst;
    + **estilo**: Cambios que no afectan al significado del código, probablemente relacionados con el formato del código, como espacios en blanco, falta de puntos y comas, estilo negro aplicado, etc;
    + **test**: Inclusión de pruebas nuevas o corrección de pruebas anteriores;
    + **perf**: mejoras de rendimiento;
    + **ci**: Relacionados con la integración continua;
    + **build**: cambios que afectan al sistema de compilación o a dependencias externas;
    + **revert**: revierte una prueba anterior

Traducción realizada con la versión gratuita del traductor DeepL.com

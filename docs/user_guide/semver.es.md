# Especificación del Versionado Semántico (SemVer)
Esta especificación se puede ver íntegramente en su dirección oficial en https://semver.org.

## Especificación
Las palabras clave “DEBE”, “NO DEBE”, “OBLIGATORIO”, “DEBERÁ”, “NO DEBERÁ”, “DEBERÍA”, “NO DEBERÍA”, “RECOMENDADO”, “PUEDE” y “OPCIONAL” en este documento serán interpretadas como se describe en RFC 2119-es.

1. El Software que usa Versionado Semántico DEBE declarar una API pública. Esta API puede ser declarada en el propio código o debe existir estrictamente en la documentación. Sin importar como sea realizado, este DEBERÍA ser preciso y comprensiva.
1. Un número de versión normal DEBE tener la forma de X.Y.Z donde X, Y y Z son números enteros no negativos, y NO DEBEN ser precedidos de ceros. X es la versión mayor, Y es la versión menor, y Z es la versión parche. Cada elemento DEBE incrementarse numéricamente. Por ejemplo: 1.9.0 -> 1.10.0 -> 1.11.0
1. Una vez que el paquete versionado ha sido publicado, el contenido de esa versión NO DEBE ser modificado. Cualquier modificación DEBE ser publicada como una nueva versión.
1. Una versión mayor en cero (0.y.z) se considera como desarrollo inicial. Todo PUEDE cambiar en cualquier momento. La API pública NO DEBERÍA ser considerado estable.
1. La versión 1.0.0 define la API pública. La manera en que cada número de versión es incrementado después de esta publicación dependerá de su API pública y cómo cambia.
1. La versión parche Z (x.y.Z | x > 0) DEBE ser incrementada si solamente se introducen correcciones de errores compatibles con versiones anteriores. Una corrección de error se define como un cambio interno que corrige un comportamiento incorrecto.
1. La versión menor Y (x.Y.z | x > 0) DEBE ser incrementada si se introduce funcionalidad nueva y compatible con la versión anterior de la API pública. Esta DEBE ser incrementada si se introduce cualquier funcionalidad a la API pública o mejora al código privado. Esta PUEDE incluir cambios a nivel de parches. La versión parche DEBE reiniciarse a 0 cuando una versión menor se incrementa.
1. La versión mayor (X.y.z | X > 0) DEBE ser incrementada solamente si se introducen cambios incompatibles con la versión anterior de la API pública. Este PUEDE incluir cambios de nivel menor y parches. Versiones parche y menores DEBEN ser reiniciadas a 0 cuando una versión mayor es incrementada.
1. Una versión de prelanzamiento PUEDE ser denotada agregando un guión y una serie de identificadores separados por puntos, inmediatamente seguida de la versión parche. Los identificadores DEBEN ser compuestos solo de caracteres alfanuméricos ASCII y guión ([0-9A-Za-z-]). Los identificadores NO DEBEN estar vacíos. Identificadores numéricos NO DEBEN ser precedidos de cero. Versiones de prelanzamiento tienen una precedencia inferior que una versión normal. Una versión de prelanzamiento indica que esa versión no es estable y puede no satisfacer los requerimientos de compatibilidad destinados como se denota en la versión normal asociada. Por ejemplo: 1.0.0-alpha, 1.0.0-alpha.1, 1.0.0-0.3.7, 1.0.0-x.7.z.92.
1. Metadatos de compilación PUEDEN ser denotados agregando el signo más y una serie de identificadores separados por puntos, inmediatamente seguido de la versión parche o prelanzamiento. Los identificadores DEBEN ser compuestos de solo caracteres alfanuméricos ASCII y guión ([0-9A-Za-z-]). Los identificadores NO DEBEN estar vacíos. Identificadores numéricos NO DEBEN ser precedidos de cero. Los metadatos de compilación DEBEN ser ignorados cuando se determina la precedencia de la versión. Por lo tanto, dos versiones que difieren solamente en los metadatos de compilación tienen la misma precedencia. Por ejemplo: 1.0.0-alpha+001, 1.0.0+20130313144700, 1.0.0-beta+exp.sha.5114f85.
1. La precedencia se refiere a cómo las versiones se comparan entre ellas cuando se ordenan.
1. La precedencia DEBE ser calculada separando los identificadores de la versión en mayor, menor, parche y prelanzamiento (dejando de lado los metadatos de compilación).
1. La precedencia es determinada por la primera diferencia al comparar cada uno de los identificadores de izquierda a derecha como se indica: mayor, menor y parche son siempre comparadas numéricamente.

    Por ejemplo: 1.0.0 < 2.0.0 < 2.1.0 < 2.1.1.

1. Cuando la versión mayor, menor y parche son iguales, la versión de prelanzamiento tiene menor precedencia que la versión normal.

    Por ejemplo: 1.0.0-alpha < 1.0.0.

1. La precedencia para dos versiones de prelanzamiento con la misma versión mayor, menor y parche DEBE ser determinada comparando cada identificador separado por punto, de izquierda a derecha, hasta que una diferencia sea encontrada como se indica:

>- Los identificadores compuestos solamente por números se comparan numéricamente.
>- Los identificadores con letras o guiones se comparan lexicográficamente en el orden ASCII.
>- Los identificadores numéricos siempre tienen menor precedencia que los no numéricos.
>- Un conjunto mayor de campos de prelanzamiento tiene mayor precedencia que uno menor, si todos los identificadores anteriores son iguales.

    Por ejemplo: 1.0.0-alpha < 1.0.0-alpha.1 < 1.0.0-alpha.beta < 1.0.0-beta < 1.0.0-beta.2 < 1.0.0-beta.11 < 1.0.0-rc.1 < 1.0.0.

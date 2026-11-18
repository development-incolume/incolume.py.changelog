# Markdown - Sintaxis básica

---

_basado en https://www.markdownguide.org/basic-syntax/_

---

## Visión general
Casi todas las aplicaciones de Markdown admiten la sintaxis básica descrita en el documento de diseño original de Markdown. Existen pequeñas variaciones y discrepancias entre los procesadores de Markdown; se anotan en el texto siempre que es posible.

## Títulos

Para crear un título, añade signos de número (`#`) delante de una palabra o frase.
La cantidad de signos de número que uses debe corresponder al nivel del título.
Por ejemplo, para crear un título de nivel tres (`<h3>`), usa tres signos de número (por ejemplo, `### My Header`).

| Marcado                | 	HTML                       | Salida renderizada       |
|---------------------|------------------------------|--------------------------|
| `# Heading level 1` | 	`<h1>Heading level 1</h1>` | <h1>Heading level 1</h1> |
| `# Heading level 2` | 	`<h2>Heading level 2</h2>` | <h2>Heading level 2</h2> |
| `# Heading level 3` | 	`<h3>Heading level 3</h3>` | <h3>Heading level 3</h3> |
| `# Heading level 4` | 	`<h4>Heading level 4</h4>` | <h4>Heading level 4</h4> |
| `# Heading level 5` | 	`<h5>Heading level 5</h5>` | <h5>Heading level 5</h5> |
| `# Heading level 6` | 	`<h6>Heading level 6</h6>` | <h6>Heading level 6</h6> |

## Sintaxis alternativa
Como alternativa, en la línea debajo del texto, añade cualquier número de caracteres `==` para un título de nivel 1 o caracteres `--` para un título de nivel 2.

| Marcado                                                                | 	HTML                       | Salida renderizada       |
|---------------------------------------------------------------------------|------------------------------|--------------------------|
| <code class="highlighter-rouge">Heading level 1<br>===============</code> | 	`<h1>Heading level 1</h1>` | <h1>Heading level 1</h1> |
| <code class="highlighter-rouge">Heading level 2<br>---------------</code> | 	`<h2>Heading level 2</h2>` | <h2>Heading level 2</h2> |

## Encabezados: mejores prácticas
Las aplicaciones de Markdown no se ponen de acuerdo sobre cómo tratar la falta de espacio entre los signos de número (`#`) y el nombre del título. Por compatibilidad, coloca siempre un espacio entre los signos de número y el nombre del título.

|  ✅&nbsp; Haz esto     | ❌&nbsp; No hagas esto |
|:--------------------:|:---------------------:|
| `# Here's a Heading` |  `#Here's a Heading`  |


También debes colocar líneas en blanco antes y después de un título por compatibilidad.

| ✅  Haz así                                                                                  | ❌ No así                                                                                         |
|------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| <code>Try to put a blank line before...<br><br># Heading<br><br>...and after a heading.</code> | <code>Without blank lines, this might not look right.<br># Heading<br>        Don't do this!</code> |


## Párrafos

Para crear párrafos, usa una línea en blanco para separar una o más líneas de texto.

| Markdown                                   | 	HTML	                                      | Salida renderizada                       |
|---------------------------------------------|---------------------------------------------|-----------------------------------------|
| <code>Párrafo1.<br><br>Párrafo2.</code> | `<p>Párrafo1.</p><p>Párrafo2.</p>` | <code>Párrafo1.<br>Párrafo2.</code> |

## Mejores prácticas de párrafo

A menos que el [párrafo esté en una lista](#añadir-elementos-a-las-listas), no sangres los párrafos con espacios ni tabulaciones.

>  ℹ **Nota:** Si necesitas sangrar párrafos en la salida, consulta la sección sobre cómo sangrar (tabulación).

|          ✅&nbsp; Haz esto                            | ❌&nbsp; No hagas esto                                      |
| ---------------------------------------------------------- | ---------------------------------------------------------------- |
| No coloques tabulaciones ni espacios antes de los párrafos.  | Esto puede provocar problemas de formato inesperados.        |
| Mantén las líneas alineadas a la izquierda así.            | No añadas tabulaciones ni espacios antes de los párrafos.    |

## Saltos de línea

Para crear un salto de línea o una nueva línea (`<br>`), termina la línea con dos o más espacios y pulsa Enter.

| Marcado                | HTML                             | Salida renderizada       |
| --------------------------- | ---------------------------------|----------------------------|
| Esta es la primera línea.   | <p>Esta es la primera línea.<br> | Esta es la primera línea.   |
| Y esta es la segunda línea.  | Y esta es la segunda línea.</p>  | Y esta es la segunda línea. |

### Prácticas recomendadas para saltos de línea
<!-- TODO: line-break-best-practices -->
Puedes usar dos o más espacios (lo que se denomina habitualmente "espacios en blanco finales") para los saltos de línea en casi todas las aplicaciones de Markdown, pero es algo controvertido. Cuesta ver los espacios en blanco al final en un editor, y muchas personas colocan dos espacios de forma accidental o intencionada después de cada frase. Por ese motivo, quizá prefieras usar otra cosa distinta de los espacios en blanco finales para los saltos de línea. Si tu aplicación de Markdown [admite HTML](#html), puedes usar la etiqueta HTML `<br>`.
Por compatibilidad, usa el espacio en blanco final o la etiqueta HTML `<br>` al final de la línea.
Hay otras dos opciones que no recomiendo usar. CommonMark y algunos otros lenguajes de marcado ligeros permiten escribir una barra invertida ( `\` ) al final de la línea, pero no todas las aplicaciones de Markdown lo admiten, por lo que no es una buena opción en términos de compatibilidad. Y al menos algunos lenguajes de marcado ligeros no necesitan nada al final de la línea: basta con pulsar Enter y crearán un salto de línea.

| ✅&nbsp; Haz esto                     | ❌&nbsp; No hagas esto                       |
| ---------------------------------------- | ----------------------------------------------- |
| Primera línea con dos espacios al final. | Primera línea con una barra invertida al final.\ |
| Y la siguiente línea.                    | Y la siguiente línea.                         |
| Primera línea con la etiqueta HTML al final.<br> | Primera línea sin nada al final.      |
| Y la siguiente línea.                    | Y la siguiente línea.                         |

## Énfasis

Puedes añadir énfasis poniendo el texto en negrita o cursiva.

### Negrita

Para el texto en negrita, añade dos asteriscos o guiones bajos antes y después de una palabra o frase. Para poner en negrita la parte central de una palabra y dar énfasis, añade dos asteriscos sin espacios alrededor de las letras.

| Marcado                     | HTML                                        | Salida renderizada               |
| ------------------------------ | ------------------------------------------- | --------------------------------|
| Me encanta `**texto en negrita**`. | Me encanta <strong>texto en negrita</strong>. | Me encanta **texto en negrita**. |
| Me encanta `__texto en negrita__`. | Me encanta <strong>texto en negrita</strong>. | Me encanta __texto en negrita__. |
| El amor `**es**` en negrita        | El amor<strong>es</strong> en negrita        | El amor **es** en negrita        |

#### Mejores prácticas en negrita

Las aplicaciones de Markdown no se ponen de acuerdo sobre cómo tratar los guiones bajos en medio de una palabra. Por compatibilidad, usa asteriscos para la negrita en medio de una palabra y dar énfasis.

|✅&nbsp; Haz esto     | ❌&nbsp; No hagas esto |
|------------------------|----------------------- |
| El amor `**es**` en negrita | El amor`__es__` en negrita |

### Cursiva

Para poner el texto en cursiva, añade un asterisco o un guion bajo antes y después de una palabra o frase. Para poner en cursiva la parte central de una palabra y dar énfasis, añade un asterisco sin espacios alrededor de las letras.

| Marcado                                   | HTML                                            | Salida renderizada                        |
| -------------------------------------------- | ----------------------------------------------- | ---------------------------------------- |
| El texto en cursiva es el `*maullido del gato*`.  | El texto en cursiva es el <em>maullido del gato</em>. | El texto en cursiva es el *maullido del gato*. |
| El texto en cursiva es el `_maullido del gato_`.  | El texto en cursiva es el <em>maullido del gato</em>. | El texto en cursiva es el _maullido del gato_. |
| Un `*gato*` maulla                         | Un <em>gato</em> maulla                    | Un *gato* maulla                         |

#### Mejores prácticas en cursiva
<!-- TODO: italic-best-practices -->

Las aplicaciones de Markdown no se ponen de acuerdo sobre cómo tratar los guiones bajos en medio de una palabra. Por compatibilidad, usa asteriscos para la cursiva en medio de una palabra y dar énfasis.

|✅&nbsp; Haz esto     |❌&nbsp; No hagas esto    |
|------------------------| ------------------------ |
| Un `*gato*` maulla     | Un`_gato_` maulla      |

### Negrita y cursiva
<!-- TODO: bold-and-italic -->

Para enfatizar el texto con negrita y cursiva a la vez, añade tres asteriscos o guiones bajos antes y después de una palabra o frase. Para poner negrita y cursiva en medio de una palabra y dar énfasis, añade tres asteriscos sin espacios alrededor de las letras.

| Marcado                                       | HTML                                                                | Salida renderizada                              |
| ------------------------------------------------ | ------------------------------------------------------------------- | ---------------------------------------------- |
| Este texto es `***realmente importante***`.      | Este texto es `<em><strong>realmente importante</strong></em>`.     | Este texto es ***realmente importante***.      |
| Este texto es `___realmente importante___`.      | Este texto es `<em><strong>realmente importante</strong></em>`.     | Este texto es ___realmente importante___.      |
| Este texto es `__*realmente importante*__`.      | Este texto es `<em><strong>realmente importante</strong></em>`.     | Este texto es __*realmente importante*__.      |
| Este texto es `**_realmente importante**_`.      | Este texto es `<em><strong>realmente importante</strong></em>`.     | Este texto es **_realmente importante**_.      |
| Este texto es realmente `***muy***` importante. | Este texto es realmente `<em><strong>muy importante</strong></em>`.| Este texto es realmente ***muy*** importante. |

>  ℹ **Nota:** el orden de las etiquetas `em` y `strong` puede invertirse según el procesador de Markdown que uses.

#### Prácticas recomendadas para negrita y cursiva
<!-- TODO: bold-and-italic-best-practices -->

Las aplicaciones de Markdown no se ponen de acuerdo sobre cómo tratar los guiones bajos en medio de una palabra. Por compatibilidad, usa asteriscos para negrita y cursiva en medio de una palabra y dar énfasis.

|✅&nbsp; Haz esto                               |❌&nbsp; No hagas esto                          |
|-------------------------------------------------| ----------------------------------------------- |
| Este texto es realmente `***muy***` importante.| Este texto es realmente`___muy___`importante.|

## Citas en bloque

Para crear una cita en bloque, añade un `>` delante de un párrafo.

    > Dorothy followed her through many of the beautiful rooms in her castle.

La salida renderizada queda así:

> Dorothy la siguió por muchas de las hermosas habitaciones de su castillo.


### Citas en bloque con varios párrafos
<!-- TODO: blockquotes-with-multiple-paragraphs -->

Las citas en bloque pueden contener varios párrafos. Añade un `>` en las líneas en blanco entre los párrafos.

    > Dorothy la siguió por muchas de las hermosas habitaciones de su castillo.

    >

    > La Bruja le ordenó que limpiara las cacerolas y los calderos, barriera el suelo y mantuviera el fuego alimentado con leña.

La salida renderizada queda así:

> Dorothy la siguió por muchas de las hermosas habitaciones de su castillo.
>
> La Bruja le ordenó que limpiara las cacerolas y los calderos, barriera el suelo y mantuviera el fuego alimentado con leña.

### Citas anidadas
<!-- TODO: nested-blockquotes -->

Las citas en bloque pueden anidarse. Añade un `>>` delante del párrafo que quieras anidar.

    > Dorothy la siguió por muchas de las hermosas habitaciones de su castillo.

    >

    >> La Bruja le ordenó que limpiara las cacerolas y los calderos, barriera el suelo y mantuviera el fuego alimentado con leña.

La salida renderizada queda así:

> Dorothy la siguió por muchas de las hermosas habitaciones de su castillo.
>
> La Bruja le ordenó que limpiara las cacerolas y los calderos, barriera el suelo y mantuviera el fuego alimentado con leña.

### Citas en bloque con otros elementos
<!-- TODO: blockquotes-with-other-elements -->

Las citas en bloque pueden contener otros elementos formatados en Markdown. No todos los elementos se pueden usar

    > #### ¡Los resultados trimestrales parecen geniales!

    >

    > - Los ingresos se salían del gráfico.

    > - Los beneficios fueron mayores que nunca.

    >

    > *Todo* va según lo **planeado**.

La salida renderizada queda así:

> #### ¡Los resultados trimestrales parecen geniales!
>
> - Los ingresos se salían del gráfico.
> - Los beneficios fueron mayores que nunca.
>
> *Todo* va según lo **planeado**.

### Prácticas recomendadas para citas en bloque
<!-- TODO: blockquotes-best-practices -->

Por compatibilidad, coloca líneas en blanco antes y después de las citas.

| ✅&nbsp; Haz esto                        | ❌&nbsp; No hagas esto                             |
| ------------------------------------------ | -------------------------------------------------- |
| Intenta colocar una línea en blanco antes... | Sin líneas en blanco, esto puede no quedar bien.\
|                                            | > Esto es una cita en bloque\
| > Esto es una cita en bloque                | ¡No hagas esto!\
|                                            |                                                    |
| ...y después de una cita en bloque.          |                                                    |

## Listas

Puedes organizar elementos en listas ordenadas y desordenadas.

### Listas ordenadas
<!-- TODO: ordered-lists -->

Para crear una lista ordenada, añade elementos de línea con números seguidos de puntos. Los números no tienen por qué estar en orden numérico, pero la lista debe empezar por el número uno.

| Marcado                                       | HTML                                                                | Salida renderizada                              |
| ------------------------------------------------ | ------------------------------------------------------------------- | ---------------------------------------------- |
| 1. Primer elemento <br> 2. Segundo elemento <br> 3. Tercer elemento <br> 4. Cuarto elemento| `<ol>`<br>ㅤ`<li>Primer elemento</li>`<br>ㅤ`<li>Segundo elemento</li>`<br>ㅤ`<li>Tercer elemento</li>`<br>ㅤ`<li>Cuarto elemento</li>`<br>`</ol>`| 1. Primer elemento <br> 2. Segundo elemento <br> 3. Tercer elemento <br> 4. Cuarto elemento|
| 1. Primer elemento <br> 1. Segundo elemento <br> 1. Tercer elemento <br> 1. Cuarto elemento| `<ol>`<br>ㅤ`<li>Primer elemento</li>`<br>ㅤ`<li>Segundo elemento</li>`<br>ㅤ`<li>Tercer elemento</li>`<br>ㅤ`<li>Cuarto elemento</li>`<br>`</ol>`| 1. Primer elemento <br> 2. Segundo elemento <br> 3. Tercer elemento <br> 4. Cuarto elemento|
| 1. Primer elemento <br> 8. Segundo elemento <br> 3. Tercer elemento <br> 5. Cuarto elemento| `<ol>`<br>ㅤ`<li>Primer elemento</li>`<br>ㅤ`<li>Segundo elemento</li>`<br>ㅤ`<li>Tercer elemento</li>`<br>ㅤ`<li>Cuarto elemento</li>`<br>`</ol>`| 1. Primer elemento <br> 2. Segundo elemento <br> 3. Tercer elemento <br> 4. Cuarto elemento|
| 1. Primer elemento <br> 2. Segundo elemento <br> 3. Tercer elemento <br>ㅤㅤ1. Elemento sangrado <br>ㅤㅤ2. Elemento sangrado <br> 4. Cuarto elemento | `<ol>`<br>ㅤ`<li>Primer elemento</li>`<br>ㅤ`<li>Segundo elemento</li>`<br>ㅤ`<li>Tercer elemento</li>`<br>ㅤ`<li>Cuarto elemento</li>`<br>`</ol>`| 1. Primer elemento <br> 2. Segundo elemento <br> 3. Tercer elemento <br>ㅤㅤ1. Elemento sangrado <br>ㅤㅤ2. Elemento sangrado <br> 4. Cuarto elemento |

#### Mejores prácticas de lista ordenada
<!-- TODO: ordered-list-best-practices -->

CommonMark y algunos otros lenguajes de marcado ligeros permiten usar paréntesis `( ))` como delimitador (por ejemplo, 1) _First item_), pero no todas las aplicaciones de Markdown lo admiten, por lo que no es una buena opción en términos de compatibilidad. Por compatibilidad, usa solo puntos.

|✅&nbsp; Haz esto |❌&nbsp; No hagas esto |
| ----------------- | ---------------------- |
|1. First item<br>  |1) First item<br>       |
|2. Second item     |2) Second item          |

### Listas desordenadas
<!-- TODO: unordered-lists -->

Para crear una lista desordenada, añade guiones ( `-` ), asteriscos ( `*` ) o signos de suma ( `+` ) delante de los elementos de línea. Sangra uno o más elementos para crear una lista anidada.

| Marcado                                       | HTML                                                                | Salida renderizada                              |
| ------------------------------------------------ | ------------------------------------------------------------------- | ---------------------------------------------- |
| - Primer elemento <br> - Segundo elemento <br> - Tercer elemento <br> - Cuarto elemento| `<ul>`<br>ㅤ`<li>Primer elemento</li>`<br>ㅤ`<li>Segundo elemento</li>`<br>ㅤ`<li>Tercer elemento</li>`<br>ㅤ`<li>Cuarto elemento</li>`<br>`</ul>`| • Primer elemento <br> • Segundo elemento <br> • Tercer elemento <br> • Cuarto elemento|
| * Primer elemento <br> * Segundo elemento <br> * Tercer elemento <br> * Cuarto elemento| `<ul>`<br>ㅤ`<li>Primer elemento</li>`<br>ㅤ`<li>Segundo elemento</li>`<br>ㅤ`<li>Tercer elemento</li>`<br>ㅤ`<li>Cuarto elemento</li>`<br>`</ul>`| • Primer elemento <br> • Segundo elemento <br> • Tercer elemento <br> • Cuarto elemento|
| + Primer elemento <br> + Segundo elemento <br> + Tercer elemento <br> + Cuarto elemento| `<ul>`<br>ㅤ`<li>Primer elemento</li>`<br>ㅤ`<li>Segundo elemento</li>`<br>ㅤ`<li>Tercer elemento</li>`<br>ㅤ`<li>Cuarto elemento</li>`<br>`</ul>`| • Primer elemento <br> • Segundo elemento <br> • Tercer elemento <br> • Cuarto elemento|
| - Primer elemento <br> - Segundo elemento <br> - Tercer elemento <br>ㅤㅤ- Elemento sangrado <br>ㅤㅤ- Elemento sangrado <br> - Cuarto elemento | `<ul>`<br>ㅤ`<li>Primer elemento</li>`<br>ㅤ`<li>Segundo elemento</li>`<br>ㅤ`<li>Tercer elemento</li>`<br>ㅤ`<li>Cuarto elemento</li>`<br>`</ul>`| • Primer elemento <br> • Segundo elemento <br> • Tercer elemento <br>ㅤㅤ◦ Elemento sangrado <br>ㅤㅤ◦ Elemento sangrado <br> • Cuarto elemento |

#### Iniciar elementos de lista desordenada con números
<!-- TODO: starting-unordered-list-items-with-numbers -->

Si necesitas iniciar un elemento de lista desordenada con un número seguido de un punto, puedes usar una barra invertida ( `\` ) para [escapar](#escapar-caracteres) del punto.

| Marcado                                                      | HTML                                         | Salida renderizada                    |
| --------------------------------------------------------------- | -------------------------------------------- | ------------------------------------ |
| - 1968\. ¡Un gran año!<br>- Creo que 1969 fue el segundo mejor. |`<ul>`<br>ㅤ`<li>1968. ¡Un gran año!</li>`<br>`<li>Creo que 1969 fue el segundo mejor.</li>`<br>`</ul>` |• 1968. ¡Un gran año!<br>• Creo que 1969 fue el segundo mejor.|

#### Prácticas recomendadas para listas desordenadas
<!-- TODO: unordered-list-best-practices -->

Las aplicaciones de Markdown no se ponen de acuerdo sobre cómo tratar los distintos delimitadores en una misma lista. Por compatibilidad, no mezcles delimitadores en la misma lista `–` elige uno y manténlo.

| ✅&nbsp; Haz esto                                                       | ❌&nbsp; No hagas esto |
| ------------------------------------------------------------------------ | ----------------------- |
| - Primer elemento<br>- Segundo elemento<br>- Tercer elemento<br>- Cuarto elemento    | + Primer elemento<br>* Segundo elemento<br>- Tercer elemento<br>+ Cuarto elemento|


### Añadir elementos a las listas
<!-- TODO: adding-elements-in-lists -->

Para añadir otro elemento a una lista manteniendo la continuidad de la lista, sangra el elemento con cuatro espacios o una tabulación, como se muestra en los siguientes ejemplos.

>  ℹ **Consejo:** Si las cosas no aparecen como se esperaba, comprueba de nuevo que has sangrado los elementos de la lista con cuatro espacios o una tabulación.

#### Párrafos

    * Este es el primer elemento de la lista.
    * Aquí está el segundo elemento de la lista.

        Necesito añadir otro párrafo debajo del segundo elemento de la lista.

    * Y aquí está el tercer elemento de la lista.

La salida renderizada queda así:

* Este es el primer elemento de la lista.
* Aquí está el segundo elemento de la lista.

    Necesito añadir otro párrafo debajo del segundo elemento de la lista.

* Y aquí está el tercer elemento de la lista.

#### Citas en bloque
<!-- TODO: blockquotes -->

    * Este es el primer elemento de la lista.
    * Aquí está el segundo elemento de la lista.

        > Una cita en bloque quedaría muy bien debajo del segundo elemento de la lista.

    * Y aquí está el tercer elemento de la lista

La salida renderizada queda así:

* Este es el primer elemento de la lista.
* Aquí está el segundo elemento de la lista.
    > Una cita en bloque quedaría muy bien debajo del segundo elemento de la lista.
* Y aquí está el tercer elemento de la lista

#### Bloques de código
<!-- TODO: code-blocks-1 -->

[Los bloques de código](#bloques-de-código) normalmente se sangran con cuatro espacios o una tabulación. Cuando están dentro de una lista, sangra con ocho espacios o dos tabulaciones.

    1. Abre el archivo.
    2. Encuentra el siguiente bloque de código en la línea 21:

        <html>
          <head>
            <title>Test</title>
          </head>

    3. Actualiza el título para que coincida con el nombre de tu sitio.

La salida renderizada queda así:

1. Abre el archivo.
2. Encuentra el siguiente bloque de código en la línea 21:

        <html>
          <head>
            <title>Test</title>
          </head>

3. Actualiza el título para que coincida con el nombre de tu sitio.

#### Imágenes
<!-- TODO: images -->

    1. Abre el archivo que contiene la mascota de Linux.
    2. Maravíllate con su belleza.

        ![Tux, the Linux mascot](https://mdg.imgix.net/assets/images/tux.png?auto=format&fit=clip&q=40&w=100)

    3. Cierra el archivo.

La salida renderizada queda así:

1. Abre el archivo que contiene la mascota de Linux.
2. Maravíllate con su belleza.

    ![Tux, the Linux mascot](https://mdg.imgix.net/assets/images/tux.png?auto=format&fit=clip&q=40&w=100)

3. Cierra el archivo.

#### Listas
<!-- TODO: lists -->

Puedes anidar una lista desordenada dentro de una lista ordenada, o viceversa.

    1. Primer elemento
    2. Segundo elemento
    3. Tercer elemento
          - Elemento sangrado
          - Elemento sangrado
    4. Cuarto elemento

La salida renderizada queda así:

1. Primer elemento
2. Segundo elemento
3. Tercer elemento
      - Elemento sangrado
      - Elemento sangrado
4. Cuarto elemento

## Código

Para denotar una palabra o frase como código, enciérrala entre comillas graves ( ` ).

|Marcado                              |HTML                                                  |Salida renderizada                       |
| -------------------------------------- | ---------------------------------------------------- |--------------------------------------- |
|``En el símbolo del sistema, escribe `Nano`.``| En el símbolo del sistema, escribe <code>Nano</code>.     |En el símbolo del sistema, escribe `nano`.  |

### Escapar comillas graves
<!-- TODO: escaping-backticks -->

Si la palabra o frase que quieras denotar como código incluye una o más comillas graves, puedes escaparla encerrando la palabra o frase entre comillas graves dobles `( `` )`.

|Marcado                             |HTML                                              |Salida renderizada           |
| ------------------------------------- | ------------------------------------------------ | -------------------------  |
|``Usa `code` en tu archivo Markdown.``| <code>Usa `code` en tu archivo Markdown.</code> |Usa `code` en tu archivo Markdown.|

### Bloques de código
<!-- TODO: code-blocks -->

Para crear bloques de código, sangra cada línea del bloque con al menos cuatro espacios o una tabulación.

    <html>
      <head>
      </head>
    </html>

La salida renderizada queda así:

    <html>
      <head>
      </head>
    </html>

>  ℹ **Nota:** Para crear bloques de código sin sangrar líneas, usa los [bloques de código delimitados](https://www.markdownguide.org/extended-syntax/#fenced-code-blocks).

## Reglas horizontales

Para crear una regla horizontal, usa tres o más asteriscos ( `***` ), guiones ( `---` ) o guiones bajos ( `___` ) en una línea, solos.

    ***
    ---
    ______________
La salida renderizada de los tres parece idéntica:
_____________________________________________________

### Prácticas recomendadas para reglas horizontales

Por compatibilidad, coloca líneas en blanco antes y después de las reglas horizontales.
| ✅&nbsp; Haz esto                                                                      | ❌&nbsp; No hagas esto |
|----------------------------------------------------------------------------------------- |------------------------|
|Intenta colocar una línea en blanco antes...<br><br>---<br><br>...y después de una regla horizontal. |Sin líneas en blanco, esto sería un título.<br>---<br>¡No hagas esto!|

## Enlaces

Para crear un enlace, pon el texto del enlace entre corchetes (por ejemplo, `[Duck Duck Go]`) y síguelo inmediatamente con la URL entre paréntesis (por ejemplo, `(https://duckduckgo.com)`).

    My favorite search engine is [Duck Duck Go](https://duckduckgo.com).


La salida renderizada queda así:

Mi buscador favorito es [Duck Duck Go](https://duckduckgo.com).

>  ℹ **Nota:** Para enlazar a un elemento de la misma página, consulta [enlazar a IDs de encabezado](https://www.markdownguide.org/extended-syntax/#linking-to-heading-ids). Para crear un enlace que se abra en una pestaña o ventana nueva, consulta la sección sobre [destinos de enlace](https://www.markdownguide.org/hacks/#link-targets).

### Añadir títulos
<!-- TODO: adding-titles -->

Opcionalmente, puedes añadir un título a un enlace. Aparecerá como un consejo cuando el usuario pase el ratón por encima del enlace. Para añadir un título, colócalo entre comillas después de la URL.

    My favorite search engine is [Duck Duck Go](https://duckduckgo.com "The best search engine for privacy").

La salida renderizada queda así:

Mi buscador favorito es [Duck Duck Go](https://duckduckgo.com).

### URLs y direcciones de correo electrónico

Para convertir rápidamente una URL o una dirección de correo electrónico en un enlace, enciérrala entre corchetes angulares.

    <https://www.markdownguide.org>
    <fake@example.com>

La salida renderizada queda así:
 <https://www.markdownguide.org>

 <fake@example.com>

### Formato de enlaces

Para [enfatizar](#énfase) los enlaces, añade asteriscos antes y después de los corchetes y paréntesis. Para denotar enlaces como [código](#código), añade comillas graves entre corchetes.
    Me encanta apoyar a **[EFF](https://eff.org)**.

    Este es el *[Markdown Guide](https://www.markdownguide.org)*.

    Consulta la sección sobre [`code`](#código).

La salida renderizada queda así:

Me encanta apoyar a **[EFF](https://eff.org)**.

Este es el *[Markdown Guide](https://www.markdownguide.org)*.

Consulta la sección sobre [`code`](#código).

### Enlaces de estilo de referencia
<!-- TODO: reference-style-links -->

Los enlaces de estilo de referencia son un tipo especial de enlace que hace que las URLs sean más fáciles de mostrar y leer en Markdown. Los enlaces de estilo de referencia se construyen en dos partes: la parte que mantienes alineada con tu texto y la parte que almacenas en otro lugar del archivo para que el texto siga siendo fácil de leer.

#### Formato de la primera parte del enlace
<!-- TODO: formatting-the-first-part-of-the-link -->

La primera parte de un enlace de estilo de referencia se formatea con dos conjuntos de corchetes. El primer conjunto de corchetes rodea el texto que debe aparecer enlazado. El segundo conjunto de corchetes muestra una etiqueta que se usa para apuntar al enlace que almacenas en otra parte del documento.

Aunque no es obligatorio, puedes incluir un espacio entre el primer y el segundo conjunto de corchetes. La etiqueta del segundo conjunto de corchetes no distingue entre mayúsculas y minúsculas y puede incluir letras, números, espacios o puntuación.

Esto significa que los siguientes formatos de ejemplo son aproximadamente equivalentes para la primera parte del enlace:

* [hobbit-hole][1]
* [hobbit-hole][1]

#### Formato de la segunda parte del enlace
<!-- TODO: formatting-the-second-part-of-the-link -->

La segunda parte de un enlace de estilo de referencia se formatea con los siguientes atributos:

    1. La etiqueta, entre corchetes, seguida inmediatamente de dos puntos y al menos un espacio (por exemplo, [label]: ).
    2. La URL del enlace, que puedes colocar opcionalmente entre corchetes angulares.
    3. El título opcional del enlace, que puedes colocar entre comillas dobles, comillas simples o paréntesis.

Esto significa que los siguientes formatos de ejemplo son aproximadamente equivalentes para la segunda parte del enlace:

    * [1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle
    * [1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle "Hobbit lifestyles"
    * [1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle 'Hobbit lifestyles'
    * [1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle (Hobbit lifestyles)
    * [1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle "Hobbit lifestyles"
    * [1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle 'Hobbit lifestyles'
    * [1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle (Hobbit lifestyles)

Puedes colocar esta segunda parte del enlace en cualquier lugar de tu documento Markdown. Algunas personas la colocan inmediatamente después del párrafo en el que aparece, mientras que otras la colocan al final del documento (como notas al final o al pie).

#### Un ejemplo para juntar las piezas
<!-- TODO: an-example-putting-the-parts-together -->

Imagina que añades una URL como un [enlace de URL estándar](#enlaces) a un párrafo y que queda así en Markdown:

    En un agujero en el suelo vivía un hobbit. No era un agujero asqueroso, sucio y húmedo, lleno de extremidades
    de gusanos y con olor a lodo, ni tampoco un agujero seco, vacío y arenoso, sin nada donde sentarse o comer:
    era un [agujero de hobbit](https://en.wikipedia.org/wiki/Hobbit#Lifestyle "Hobbit lifestyles"), y eso significa comodidad.

Aunque pueda apuntar a información adicional interesante, la URL mostrada no aporta mucho al texto sin formato existente y solo lo hace más difícil de leer. Para corregirlo, puedes formatear la URL así:

    En un agujero en el suelo vivía un hobbit. No un agujero asqueroso, sucio y húmedo, lleno de extremidades de gusanos y con olor a lodo, ni tampoco un agujero seco, vacío y arenoso, sin nada donde sentarse o comer: era un [agujero de hobbit](https://en.wikipedia.org/wiki/Hobbit#Lifestyle), y eso significa comodidad.

En ambos casos anteriores, la salida renderizada sería idéntica:

>
> En un agujero en el suelo vivía un hobbit. No era un agujero asqueroso, sucio y húmedo, lleno de extremidades de gusanos y con olor a lodo, ni tampoco un agujero seco, vacío y arenoso, sin nada donde sentarse o comer: era un [agujero de hobbit](https://en.wikipedia.org/wiki/Hobbit#Lifestyle), y eso significa comodidad.
>

y el HTML del enlace sería:

    <a href="https://en.wikipedia.org/wiki/Hobbit#Lifestyle title="Hobbit lifestyles">hobbit-hole</a>

### Prácticas recomendadas de enlaces
<!-- TODO: link-best-practices -->

Las aplicaciones de Markdown no se ponen de acuerdo sobre cómo tratar los espacios en medio de una URL. Por compatibilidad, intenta codificar en URL los espacios con 20%. Como alternativa, si tu aplicación de Markdown [admite HTML](#html), puedes usar la etiqueta HTML.

| ✅&nbsp; Haz esto                                       | ❌&nbsp; No hagas esto                               |
| -------------------------------------------------------- | ------------------------------------------------------|
|`[link](https://www.example.com/my%20great%20page)`<br><br>`<a href="https://www.example.com/my great page">link</a>`|`[link](https://www.example.com/my great page)`<br><br>|

Los paréntesis en medio de una URL también pueden ser problemáticos. Por compatibilidad, intenta codificar en URL el paréntesis de apertura `(()` con %28 y el paréntesis de cierre `( ))` con %29. Como alternativa, si tu aplicación de Markdown [admite HTML](#html), puedes usar la etiqueta HTML.

| ✅&nbsp; Haz esto                                       | ❌&nbsp; No hagas esto                               |
| -------------------------------------------------------- | ------------------------------------------------------|
|`[a novel](https://en.wikipedia.org/wiki/The_Milagro_Beanfield_War_%28novel%29)`<br><br>`<a href="https://en.wikipedia.org/wiki/The_Milagro_Beanfield_War_(novel)">a novel</a>`|`[a novel](https://en.wikipedia.org/wiki/The_Milagro_Beanfield_War_(novel))`|

## Imágenes

Para añadir una imagen, pon un signo de exclamación ( `!` ), seguido del texto alternativo entre corchetes y la ruta o URL del recurso de imagen entre paréntesis. Opcionalmente, puedes añadir un título entre comillas después de la ruta o la URL.

    ![The San Juan Mountains are beautiful!](/assets/images/san-juan-mountains.jpg "San Juan Mountains")

La salida renderizada queda así:

![The San Juan Mountains are beautiful!](https://mdg.imgix.net/assets/images/san-juan-mountains.jpg?auto=format&fit=clip&q=40&w=800 "San Juan Mountains")

>  ℹ **Nota:** Para cambiar el tamaño de una imagen, consulta la sección sobre [tamaño de imagen](https://www.markdownguide.org/hacks/#image-size). Para añadir un pie de foto, consulta la sección sobre [pies de imagen](https://www.markdownguide.org/hacks/#image-captions).

### Enlazar imágenes
<!-- TODO: linking-images -->

Para añadir un enlace a una imagen, pon el Markdown de la imagen entre corchetes y añade el enlace entre paréntesis.

    [![An old rock in the desert](/assets/images/shiprock.jpg "Shiprock, New Mexico by Beau Rogers")](https://www.flickr.com/photos/beaurogers/31833779864/in/photolist-Qv3rFw-34mt9F-a9Cmfy-5Ha3Zi-9msKdv-o3hgjr-hWpUte-4WMsJ1-KUQ8N-deshUb-vssBD-6CQci6-8AFCiD-zsJWT-nNfsgB-dPDwZJ-bn9JGn-5HtSXY-6CUhAL-a4UTXB-ugPum-KUPSo-fBLNm-6CUmpy-4WMsc9-8a7D3T-83KJev-6CQ2bK-nNusHJ-a78rQH-nw3NvT-7aq2qf-8wwBso-3nNceh-ugSKP-4mh4kh-bbeeqH-a7biME-q3PtTf-brFpgb-cg38zw-bXMZc-nJPELD-f58Lmo-bXMYG-bz8AAi-bxNtNT-bXMYi-bXMY6-bXMYv)


La salida renderizada queda así:

[![An old rock in the desert](https://mdg.imgix.net/assets/images/shiprock.jpg?auto=format&fit=clip&q=40&w=800 "Shiprock, New Mexico by Beau Rogers")](https://www.flickr.com/photos/beaurogers/31833779864/in/photolist-Qv3rFw-34mt9F-a9Cmfy-5Ha3Zi-9msKdv-o3hgjr-hWpUte-4WMsJ1-KUQ8N-deshUb-vssBD-6CQci6-8AFCiD-zsJWT-nNfsgB-dPDwZJ-bn9JGn-5HtSXY-6CUhAL-a4UTXB-ugPum-KUPSo-fBLNm-6CUmpy-4WMsc9-8a7D3T-83KJev-6CQ2bK-nNusHJ-a78rQH-nw3NvT-7aq2qf-8wwBso-3nNceh-ugSKP-4mh4kh-bbeeqH-a7biME-q3PtTf-brFpgb-cg38zw-bXMZc-nJPELD-f58Lmo-bXMYG-bz8AAi-bxNtNT-bXMYi-bXMY6-bXMYv)

## Escapar caracteres

Para mostrar un carácter literal que de otro modo se usaría para formatear texto en un documento Markdown, añade una barra invertida ( `\` ) delante del carácter.

    \* Without the backslash, this would be a bullet in an unordered list.

La salida renderizada queda así:

* Sin la barra invertida, esto sería un marcador en una lista desordenada.

### Caracteres que puedes escapar
<!-- TODO: characters-you-can-escape -->

Puedes usar una barra invertida para escapar los siguientes caracteres.

|Caracteres   |Nombre                                                                            |
| ----------- | ------------------------------------------------------------------------------ |
|\            |barra invertida                                                                 |
|`            |backtick (véase también [escape de backticks en el código](#escapar-comillas-graves)) |
|*            |asterisco                                                                       |
|_            |guion bajo                                                                      |
|{}           |llaves                                                                          |
|[]           |corchetes                                                                       |
|<>           |corchetes angulares                                                             |
|()           |paréntesis                                                                      |
|#            |almohadilla                                                                     |
|+            |signo más                                                                       |
|-            |signo menos (guion)                                                             |
|.            |punto                                                                           |
|!            |signo de exclamación                                                            |
||            |barra vertical                                                                  |

## HTML

Muchas aplicaciones de Markdown permiten usar etiquetas HTML en texto formateado con Markdown. Es útil si prefieres ciertas etiquetas HTML a la sintaxis Markdown. Por ejemplo, algunas personas encuentran más fácil usar etiquetas HTML para las imágenes. Usar HTML también es útil cuando necesitas cambiar los atributos de un elemento, como especificar el [color del texto](https://www.markdownguide.org/hacks/#color) o cambiar el ancho de una imagen.

Para usar HTML, pon las etiquetas en el texto de tu archivo formateado con Markdown.

    This **word** is bold. This <em>word</em> is italic.

La salida renderizada queda así:

Esta **palabra** está en negrita. Esta *palabra* está en cursiva.

### Prácticas recomendadas de HTML
<!-- TODO: html-best-practices -->

Por motivos de seguridad, no todas las aplicaciones de Markdown admiten HTML en los documentos Markdown. En caso de duda, consulta la documentación de tu aplicación de Markdown. Algunas aplicaciones solo admiten un subconjunto de etiquetas HTML.

Usa líneas en blanco para separar los elementos HTML de nivel de bloque, como `<table>`, `<pre>` y `<p>`, del contenido circundante. Intenta no sangrar las etiquetas con tabulaciones ni espacios: esto puede interferir en el formato.

No puedes usar la sintaxis Markdown dentro de etiquetas HTML de nivel de bloque. Por ejemplo, `<p>italic and **bold**</p>` no funcionará.

## Emojis

[Emojis para Markdown](https://gist.github.com/rxaviers/7360908)

### Personas

| :bowtie: `:bowtie:`                                             | :smile: `:smile:`                                               | :laughing: `:laughing:`                     |
|-----------------------------------------------------------------|-----------------------------------------------------------------|---------------------------------------------|
| :blush: `:blush:`                                               | :smiley: `:smiley:`                                             | :relaxed: `:relaxed:`                       |
| :smirk: `:smirk:`                                               | :heart_eyes: `:heart_eyes:`                                     | :kissing_heart: `:kissing_heart:`           |
| :kissing_closed_eyes: `:kissing_closed_eyes:`                   | :flushed: `:flushed:`                                           | :relieved: `:relieved:`                     |
| :satisfied: `:satisfied:`                                       | :grin: `:grin:`                                                 | :wink: `:wink:`                             |
| :stuck_out_tongue_winking_eye: `:stuck_out_tongue_winking_eye:` | :stuck_out_tongue_closed_eyes: `:stuck_out_tongue_closed_eyes:` | :grinning: `:grinning:`                     |
| :kissing: `:kissing:`                                           | :kissing_smiling_eyes: `:kissing_smiling_eyes:`                 | :stuck_out_tongue: `:stuck_out_tongue:`     |
| :sleeping: `:sleeping:`                                         | :worried: `:worried:`                                           | :frowning: `:frowning:`                     |
| :anguished: `:anguished:`                                       | :open_mouth: `:open_mouth:`                                     | :grimacing: `:grimacing:`                   |
| :confused: `:confused:`                                         | :hushed: `:hushed:`                                             | :expressionless: `:expressionless:`         |
| :unamused: `:unamused:`                                         | :sweat_smile: `:sweat_smile:`                                   | :sweat: `:sweat:`                           |
| :disappointed_relieved: `:disappointed_relieved:`               | :weary: `:weary:`                                               | :pensive: `:pensive:`                       |
| :disappointed: `:disappointed:`                                 | :confounded: `:confounded:`                                     | :fearful: `:fearful:`                       |
| :cold_sweat: `:cold_sweat:`                                     | :persevere: `:persevere:`                                       | :cry: `:cry:`                               |
| :sob: `:sob:`                                                   | :joy: `:joy:`                                                   | :astonished: `:astonished:`                 |
| :scream: `:scream:`                                             | :neckbeard: `:neckbeard:`                                       | :tired_face: `:tired_face:`                 |
| :angry: `:angry:`                                               | :rage: `:rage:`                                                 | :triumph: `:triumph:`                       |
| :sleepy: `:sleepy:`                                             | :yum: `:yum:`                                                   | :mask: `:mask:`                             |
| :sunglasses: `:sunglasses:`                                     | :dizzy_face: `:dizzy_face:`                                     | :imp: `:imp:`                               |
| :smiling_imp: `:smiling_imp:`                                   | :neutral_face: `:neutral_face:`                                 | :no_mouth: `:no_mouth:`                     |
| :innocent: `:innocent:`                                         | :alien: `:alien:`                                               | :yellow_heart: `:yellow_heart:`             |
| :blue_heart: `:blue_heart:`                                     | :purple_heart: `:purple_heart:`                                 | :heart: `:heart:`                           |
| :green_heart: `:green_heart:`                                   | :broken_heart: `:broken_heart:`                                 | :heartbeat: `:heartbeat:`                   |
| :heartpulse: `:heartpulse:`                                     | :two_hearts: `:two_hearts:`                                     | :revolving_hearts: `:revolving_hearts:`     |
| :cupid: `:cupid:`                                               | :sparkling_heart: `:sparkling_heart:`                           | :sparkles: `:sparkles:`                     |
| :star: `:star:`                                                 | :star2: `:star2:`                                               | :dizzy: `:dizzy:`                           |
| :boom: `:boom:`                                                 | :collision: `:collision:`                                       | :anger: `:anger:`                           |
| :exclamation: `:exclamation:`                                   | :question: `:question:`                                         | :grey_exclamation: `:grey_exclamation:`     |
| :grey_question: `:grey_question:`                               | :zzz: `:zzz:`                                                   | :dash: `:dash:`                             |
| :sweat_drops: `:sweat_drops:`                                   | :notes: `:notes:`                                               | :musical_note: `:musical_note:`             |
| :fire: `:fire:`                                                 | :hankey: `:hankey:`                                             | :poop: `:poop:`                             |
| :shit: `:shit:`                                                 | :+1: `:+1:`                                                     | :thumbsup: `:thumbsup:`                     |
| :-1: `:-1:`                                                     | :thumbsdown: `:thumbsdown:`                                     | :ok_hand: `:ok_hand:`                       |
| :punch: `:punch:`                                               | :facepunch: `:facepunch:`                                       | :fist: `:fist:`                             |
| :v: `:v:`                                                       | :wave: `:wave:`                                                 | :hand: `:hand:`                             |
| :raised_hand: `:raised_hand:`                                   | :open_hands: `:open_hands:`                                     | :point_up: `:point_up:`                     |
| :point_down: `:point_down:`                                     | :point_left: `:point_left:`                                     | :point_right: `:point_right:`               |
| :raised_hands: `:raised_hands:`                                 | :pray: `:pray:`                                                 | :point_up_2: `:point_up_2:`                 |
| :clap: `:clap:`                                                 | :muscle: `:muscle:`                                             | :metal: `:metal:`                           |
| :fu: `:fu:`                                                     | :walking: `:walking:`                                           | :runner: `:runner:`                         |
| :running: `:running:`                                           | :couple: `:couple:`                                             | :family: `:family:`                         |
| :two_men_holding_hands: `:two_men_holding_hands:`               | :two_women_holding_hands: `:two_women_holding_hands:`           | :dancer: `:dancer:`                         |
| :dancers: `:dancers:`                                           | :ok_woman: `:ok_woman:`                                         | :no_good: `:no_good:`                       |
| :information_desk_person: `:information_desk_person:`           | :raising_hand: `:raising_hand:`                                 | :bride_with_veil: `:bride_with_veil:`       |
| :person_with_pouting_face: `:person_with_pouting_face:`         | :person_frowning: `:person_frowning:`                           | :bow: `:bow:`                               |
| :couplekiss: `:couplekiss:`                                     | :couple_with_heart: `:couple_with_heart:`                       | :massage: `:massage:`                       |
| :haircut: `:haircut:`                                           | :nail_care: `:nail_care:`                                       | :boy: `:boy:`                               |
| :girl: `:girl:`                                                 | :woman: `:woman:`                                               | :man: `:man:`                               |
| :baby: `:baby:`                                                 | :older_woman: `:older_woman:`                                   | :older_man: `:older_man:`                   |
| :person_with_blond_hair: `:person_with_blond_hair:`             | :man_with_gua_pi_mao: `:man_with_gua_pi_mao:`                   | :man_with_turban: `:man_with_turban:`       |
| :construction_worker: `:construction_worker:`                   | :cop: `:cop:`                                                   | :angel: `:angel:`                           |
| :princess: `:princess:`                                         | :smiley_cat: `:smiley_cat:`                                     | :smile_cat: `:smile_cat:`                   |
| :heart_eyes_cat: `:heart_eyes_cat:`                             | :kissing_cat: `:kissing_cat:`                                   | :smirk_cat: `:smirk_cat:`                   |
| :scream_cat: `:scream_cat:`                                     | :crying_cat_face: `:crying_cat_face:`                           | :joy_cat: `:joy_cat:`                       |
| :pouting_cat: `:pouting_cat:`                                   | :japanese_ogre: `:japanese_ogre:`                               | :japanese_goblin: `:japanese_goblin:`       |
| :see_no_evil: `:see_no_evil:`                                   | :hear_no_evil: `:hear_no_evil:`                                 | :speak_no_evil: `:speak_no_evil:`           |
| :guardsman: `:guardsman:`                                       | :skull: `:skull:`                                               | :feet: `:feet:`                             |
| :lips: `:lips:`                                                 | :kiss: `:kiss:`                                                 | :droplet: `:droplet:`                       |
| :ear: `:ear:`                                                   | :eyes: `:eyes:`                                                 | :nose: `:nose:`                             |
| :tongue: `:tongue:`                                             | :love_letter: `:love_letter:`                                   | :bust_in_silhouette: `:bust_in_silhouette:` |
| :busts_in_silhouette: `:busts_in_silhouette:`                   | :speech_balloon: `:speech_balloon:`                             | :thought_balloon: `:thought_balloon:`       |
| :feelsgood: `:feelsgood:`                                       | :finnadie: `:finnadie:`                                         | :goberserk: `:goberserk:`                   |
| :godmode: `:godmode:`                                           | :hurtrealbad: `:hurtrealbad:`                                   | :rage1: `:rage1:`                           |
| :rage2: `:rage2:`                                               | :rage3: `:rage3:`                                               | :rage4: `:rage4:`                           |
| :suspect: `:suspect:`                                           | :trollface: `:trollface:`                                       |

### Naturaleza

| :sunny: `:sunny:`                                               | :umbrella: `:umbrella:`                         | :cloud: `:cloud:`                                             |
|-----------------------------------------------------------------|-------------------------------------------------|---------------------------------------------------------------|
| :snowflake: `:snowflake:`                                       | :snowman: `:snowman:`                           | :zap: `:zap:`                                                 |
| :cyclone: `:cyclone:`                                           | :foggy: `:foggy:`                               | :ocean: `:ocean:`                                             |
| :cat: `:cat:`                                                   | :dog: `:dog:`                                   | :mouse: `:mouse:`                                             |
| :hamster: `:hamster:`                                           | :rabbit: `:rabbit:`                             | :wolf: `:wolf:`                                               |
| :frog: `:frog:`                                                 | :tiger: `:tiger:`                               | :koala: `:koala:`                                             |
| :bear: `:bear:`                                                 | :pig: `:pig:`                                   | :pig_nose: `:pig_nose:`                                       |
| :cow: `:cow:`                                                   | :boar: `:boar:`                                 | :monkey_face: `:monkey_face:`                                 |
| :monkey: `:monkey:`                                             | :horse: `:horse:`                               | :racehorse: `:racehorse:`                                     |
| :camel: `:camel:`                                               | :sheep: `:sheep:`                               | :elephant: `:elephant:`                                       |
| :panda_face: `:panda_face:`                                     | :snake: `:snake:`                               | :bird: `:bird:`                                               |
| :baby_chick: `:baby_chick:`                                     | :hatched_chick: `:hatched_chick:`               | :hatching_chick: `:hatching_chick:`                           |
| :chicken: `:chicken:`                                           | :penguin: `:penguin:`                           | :turtle: `:turtle:`                                           |
| :bug: `:bug:`                                                   | :honeybee: `:honeybee:`                         | :ant: `:ant:`                                                 |
| :beetle: `:beetle:`                                             | :snail: `:snail:`                               | :octopus: `:octopus:`                                         |
| :tropical_fish: `:tropical_fish:`                               | :fish: `:fish:`                                 | :whale: `:whale:`                                             |
| :whale2: `:whale2:`                                             | :dolphin: `:dolphin:`                           | :cow2: `:cow2:`                                               |
| :ram: `:ram:`                                                   | :rat: `:rat:`                                   | :water_buffalo: `:water_buffalo:`                             |
| :tiger2: `:tiger2:`                                             | :rabbit2: `:rabbit2:`                           | :dragon: `:dragon:`                                           |
| :goat: `:goat:`                                                 | :rooster: `:rooster:`                           | :dog2: `:dog2:`                                               |
| :pig2: `:pig2:`                                                 | :mouse2: `:mouse2:`                             | :ox: `:ox:`                                                   |
| :dragon_face: `:dragon_face:`                                   | :blowfish: `:blowfish:`                         | :crocodile: `:crocodile:`                                     |
| :dromedary_camel: `:dromedary_camel:`                           | :leopard: `:leopard:`                           | :cat2: `:cat2:`                                               |
| :poodle: `:poodle:`                                             | :paw_prints: `:paw_prints:`                     | :bouquet: `:bouquet:`                                         |
| :cherry_blossom: `:cherry_blossom:`                             | :tulip: `:tulip:`                               | :four_leaf_clover: `:four_leaf_clover:`                       |
| :rose: `:rose:`                                                 | :sunflower: `:sunflower:`                       | :hibiscus: `:hibiscus:`                                       |
| :maple_leaf: `:maple_leaf:`                                     | :leaves: `:leaves:`                             | :fallen_leaf: `:fallen_leaf:`                                 |
| :herb: `:herb:`                                                 | :mushroom: `:mushroom:`                         | :cactus: `:cactus:`                                           |
| :palm_tree: `:palm_tree:`                                       | :evergreen_tree: `:evergreen_tree:`             | :deciduous_tree: `:deciduous_tree:`                           |
| :chestnut: `:chestnut:`                                         | :seedling: `:seedling:`                         | :blossom: `:blossom:`                                         |
| :ear_of_rice: `:ear_of_rice:`                                   | :shell: `:shell:`                               | :globe_with_meridians: `:globe_with_meridians:`               |
| :sun_with_face: `:sun_with_face:`                               | :full_moon_with_face: `:full_moon_with_face:`   | :new_moon_with_face: `:new_moon_with_face:`                   |
| :new_moon: `:new_moon:`                                         | :waxing_crescent_moon: `:waxing_crescent_moon:` | :first_quarter_moon: `:first_quarter_moon:`                   |
| :waxing_gibbous_moon: `:waxing_gibbous_moon:`                   | :full_moon: `:full_moon:`                       | :waning_gibbous_moon: `:waning_gibbous_moon:`                 |
| :last_quarter_moon: `:last_quarter_moon:`                       | :waning_crescent_moon: `:waning_crescent_moon:` | :last_quarter_moon_with_face: `:last_quarter_moon_with_face:` |
| :first_quarter_moon_with_face: `:first_quarter_moon_with_face:` | :moon: `:moon:`                                 | :earth_africa: `:earth_africa:`                               |
| :earth_americas: `:earth_americas:`                             | :earth_asia: `:earth_asia:`                     | :volcano: `:volcano:`                                         |
| :milky_way: `:milky_way:`                                       | :partly_sunny: `:partly_sunny:`                 | :octocat: `:octocat:`                                         |
| :squirrel: `:squirrel:`                                         |

### Objetos

| :bamboo: `:bamboo:`                                                 | :gift_heart: `:gift_heart:`                                 | :dolls: `:dolls:`                                   |
|---------------------------------------------------------------------|-------------------------------------------------------------|-----------------------------------------------------|
| :school_satchel: `:school_satchel:`                                 | :mortar_board: `:mortar_board:`                             | :flags: `:flags:`                                   |
| :fireworks: `:fireworks:`                                           | :sparkler: `:sparkler:`                                     | :wind_chime: `:wind_chime:`                         |
| :rice_scene: `:rice_scene:`                                         | :jack_o_lantern: `:jack_o_lantern:`                         | :ghost: `:ghost:`                                   |
| :santa: `:santa:`                                                   | :christmas_tree: `:christmas_tree:`                         | :gift: `:gift:`                                     |
| :bell: `:bell:`                                                     | :no_bell: `:no_bell:`                                       | :tanabata_tree: `:tanabata_tree:`                   |
| :tada: `:tada:`                                                     | :confetti_ball: `:confetti_ball:`                           | :balloon: `:balloon:`                               |
| :crystal_ball: `:crystal_ball:`                                     | :cd: `:cd:`                                                 | :dvd: `:dvd:`                                       |
| :floppy_disk: `:floppy_disk:`                                       | :camera: `:camera:`                                         | :video_camera: `:video_camera:`                     |
| :movie_camera: `:movie_camera:`                                     | :computer: `:computer:`                                     | :tv: `:tv:`                                         |
| :iphone: `:iphone:`                                                 | :phone: `:phone:`                                           | :telephone: `:telephone:`                           |
| :telephone_receiver: `:telephone_receiver:`                         | :pager: `:pager:`                                           | :fax: `:fax:`                                       |
| :minidisc: `:minidisc:`                                             | :vhs: `:vhs:`                                               | :sound: `:sound:`                                   |
| :speaker: `:speaker:`                                               | :mute: `:mute:`                                             | :loudspeaker: `:loudspeaker:`                       |
| :mega: `:mega:`                                                     | :hourglass: `:hourglass:`                                   | :hourglass_flowing_sand: `:hourglass_flowing_sand:` |
| :alarm_clock: `:alarm_clock:`                                       | :watch: `:watch:`                                           | :radio: `:radio:`                                   |
| :satellite: `:satellite:`                                           | :loop: `:loop:`                                             | :mag: `:mag:`                                       |
| :mag_right: `:mag_right:`                                           | :unlock: `:unlock:`                                         | :lock: `:lock:`                                     |
| :lock_with_ink_pen: `:lock_with_ink_pen:`                           | :closed_lock_with_key: `:closed_lock_with_key:`             | :key: `:key:`                                       |
| :bulb: `:bulb:`                                                     | :flashlight: `:flashlight:`                                 | :high_brightness: `:high_brightness:`               |
| :low_brightness: `:low_brightness:`                                 | :electric_plug: `:electric_plug:`                           | :battery: `:battery:`                               |
| :calling: `:calling:`                                               | :email: `:email:`                                           | :mailbox: `:mailbox:`                               |
| :postbox: `:postbox:`                                               | :bath: `:bath:`                                             | :bathtub: `:bathtub:`                               |
| :shower: `:shower:`                                                 | :toilet: `:toilet:`                                         | :wrench: `:wrench:`                                 |
| :nut_and_bolt: `:nut_and_bolt:`                                     | :hammer: `:hammer:`                                         | :seat: `:seat:`                                     |
| :moneybag: `:moneybag:`                                             | :yen: `:yen:`                                               | :dollar: `:dollar:`                                 |
| :pound: `:pound:`                                                   | :euro: `:euro:`                                             | :credit_card: `:credit_card:`                       |
| :money_with_wings: `:money_with_wings:`                             | :e-mail: `:e-mail:`                                         | :inbox_tray: `:inbox_tray:`                         |
| :outbox_tray: `:outbox_tray:`                                       | :envelope: `:envelope:`                                     | :incoming_envelope: `:incoming_envelope:`           |
| :postal_horn: `:postal_horn:`                                       | :mailbox_closed: `:mailbox_closed:`                         | :mailbox_with_mail: `:mailbox_with_mail:`           |
| :mailbox_with_no_mail: `:mailbox_with_no_mail:`                     | :door: `:door:`                                             | :smoking: `:smoking:`                               |
| :bomb: `:bomb:`                                                     | :gun: `:gun:`                                               | :hocho: `:hocho:`                                   |
| :pill: `:pill:`                                                     | :syringe: `:syringe:`                                       | :page_facing_up: `:page_facing_up:`                 |
| :page_with_curl: `:page_with_curl:`                                 | :bookmark_tabs: `:bookmark_tabs:`                           | :bar_chart: `:bar_chart:`                           |
| :chart_with_upwards_trend: `:chart_with_upwards_trend:`             | :chart_with_downwards_trend: `:chart_with_downwards_trend:` | :scroll: `:scroll:`                                 |
| :clipboard: `:clipboard:`                                           | :calendar: `:calendar:`                                     | :date: `:date:`                                     |
| :card_index: `:card_index:`                                         | :file_folder: `:file_folder:`                               | :open_file_folder: `:open_file_folder:`             |
| :scissors: `:scissors:`                                             | :pushpin: `:pushpin:`                                       | :paperclip: `:paperclip:`                           |
| :black_nib: `:black_nib:`                                           | :pencil2: `:pencil2:`                                       | :straight_ruler: `:straight_ruler:`                 |
| :triangular_ruler: `:triangular_ruler:`                             | :closed_book: `:closed_book:`                               | :green_book: `:green_book:`                         |
| :blue_book: `:blue_book:`                                           | :orange_book: `:orange_book:`                               | :notebook: `:notebook:`                             |
| :notebook_with_decorative_cover: `:notebook_with_decorative_cover:` | :ledger: `:ledger:`                                         | :books: `:books:`                                   |
| :bookmark: `:bookmark:`                                             | :name_badge: `:name_badge:`                                 | :microscope: `:microscope:`                         |
| :telescope: `:telescope:`                                           | :newspaper: `:newspaper:`                                   | :football: `:football:`                             |
| :basketball: `:basketball:`                                         | :soccer: `:soccer:`                                         | :baseball: `:baseball:`                             |
| :tennis: `:tennis:`                                                 | :8ball: `:8ball:`                                           | :rugby_football: `:rugby_football:`                 |
| :bowling: `:bowling:`                                               | :golf: `:golf:`                                             | :mountain_bicyclist: `:mountain_bicyclist:`         |
| :bicyclist: `:bicyclist:`                                           | :horse_racing: `:horse_racing:`                             | :snowboarder: `:snowboarder:`                       |
| :swimmer: `:swimmer:`                                               | :surfer: `:surfer:`                                         | :ski: `:ski:`                                       |
| :spades: `:spades:`                                                 | :hearts: `:hearts:`                                         | :clubs: `:clubs:`                                   |
| :diamonds: `:diamonds:`                                             | :gem: `:gem:`                                               | :ring: `:ring:`                                     |
| :trophy: `:trophy:`                                                 | :musical_score: `:musical_score:`                           | :musical_keyboard: `:musical_keyboard:`             |
| :violin: `:violin:`                                                 | :space_invader: `:space_invader:`                           | :video_game: `:video_game:`                         |
| :black_joker: `:black_joker:`                                       | :flower_playing_cards: `:flower_playing_cards:`             | :game_die: `:game_die:`                             |
| :dart: `:dart:`                                                     | :mahjong: `:mahjong:`                                       | :clapper: `:clapper:`                               |
| :memo: `:memo:`                                                     | :pencil: `:pencil:`                                         | :book: `:book:`                                     |
| :art: `:art:`                                                       | :microphone: `:microphone:`                                 | :headphones: `:headphones:`                         |
| :trumpet: `:trumpet:`                                               | :saxophone: `:saxophone:`                                   | :guitar: `:guitar:`                                 |
| :shoe: `:shoe:`                                                     | :sandal: `:sandal:`                                         | :high_heel: `:high_heel:`                           |
| :lipstick: `:lipstick:`                                             | :boot: `:boot:`                                             | :shirt: `:shirt:`                                   |
| :tshirt: `:tshirt:`                                                 | :necktie: `:necktie:`                                       | :womans_clothes: `:womans_clothes:`                 |
| :dress: `:dress:`                                                   | :running_shirt_with_sash: `:running_shirt_with_sash:`       | :jeans: `:jeans:`                                   |
| :kimono: `:kimono:`                                                 | :bikini: `:bikini:`                                         | :ribbon: `:ribbon:`                                 |
| :tophat: `:tophat:`                                                 | :crown: `:crown:`                                           | :womans_hat: `:womans_hat:`                         |
| :mans_shoe: `:mans_shoe:`                                           | :closed_umbrella: `:closed_umbrella:`                       | :briefcase: `:briefcase:`                           |
| :handbag: `:handbag:`                                               | :pouch: `:pouch:`                                           | :purse: `:purse:`                                   |
| :eyeglasses: `:eyeglasses:`                                         | :fishing_pole_and_fish: `:fishing_pole_and_fish:`           | :coffee: `:coffee:`                                 |
| :tea: `:tea:`                                                       | :sake: `:sake:`                                             | :baby_bottle: `:baby_bottle:`                       |
| :beer: `:beer:`                                                     | :beers: `:beers:`                                           | :cocktail: `:cocktail:`                             |
| :tropical_drink: `:tropical_drink:`                                 | :wine_glass: `:wine_glass:`                                 | :fork_and_knife: `:fork_and_knife:`                 |
| :pizza: `:pizza:`                                                   | :hamburger: `:hamburger:`                                   | :fries: `:fries:`                                   |
| :poultry_leg: `:poultry_leg:`                                       | :meat_on_bone: `:meat_on_bone:`                             | :spaghetti: `:spaghetti:`                           |
| :curry: `:curry:`                                                   | :fried_shrimp: `:fried_shrimp:`                             | :bento: `:bento:`                                   |
| :sushi: `:sushi:`                                                   | :fish_cake: `:fish_cake:`                                   | :rice_ball: `:rice_ball:`                           |
| :rice_cracker: `:rice_cracker:`                                     | :rice: `:rice:`                                             | :ramen: `:ramen:`                                   |
| :stew: `:stew:`                                                     | :oden: `:oden:`                                             | :dango: `:dango:`                                   |
| :egg: `:egg:`                                                       | :bread: `:bread:`                                           | :doughnut: `:doughnut:`                             |
| :custard: `:custard:`                                               | :icecream: `:icecream:`                                     | :ice_cream: `:ice_cream:`                           |
| :shaved_ice: `:shaved_ice:`                                         | :birthday: `:birthday:`                                     | :cake: `:cake:`                                     |
| :cookie: `:cookie:`                                                 | :chocolate_bar: `:chocolate_bar:`                           | :candy: `:candy:`                                   |
| :lollipop: `:lollipop:`                                             | :honey_pot: `:honey_pot:`                                   | :apple: `:apple:`                                   |
| :green_apple: `:green_apple:`                                       | :tangerine: `:tangerine:`                                   | :lemon: `:lemon:`                                   |
| :cherries: `:cherries:`                                             | :grapes: `:grapes:`                                         | :watermelon: `:watermelon:`                         |
| :strawberry: `:strawberry:`                                         | :peach: `:peach:`                                           | :melon: `:melon:`                                   |
| :banana: `:banana:`                                                 | :pear: `:pear:`                                             | :pineapple: `:pineapple:`                           |
| :sweet_potato: `:sweet_potato:`                                     | :eggplant: `:eggplant:`                                     | :tomato: `:tomato:`                                 |
| :corn: `:corn:`                                                     |

### Lugares

| :house: `:house:`                             | :house_with_garden: `:house_with_garden:`             | :school: `:school:`                                 |
|-----------------------------------------------|-------------------------------------------------------|-----------------------------------------------------|
| :office: `:office:`                           | :post_office: `:post_office:`                         | :hospital: `:hospital:`                             |
| :bank: `:bank:`                               | :convenience_store: `:convenience_store:`             | :love_hotel: `:love_hotel:`                         |
| :hotel: `:hotel:`                             | :wedding: `:wedding:`                                 | :church: `:church:`                                 |
| :department_store: `:department_store:`       | :european_post_office: `:european_post_office:`       | :city_sunrise: `:city_sunrise:`                     |
| :city_sunset: `:city_sunset:`                 | :japanese_castle: `:japanese_castle:`                 | :european_castle: `:european_castle:`               |
| :tent: `:tent:`                               | :factory: `:factory:`                                 | :tokyo_tower: `:tokyo_tower:`                       |
| :japan: `:japan:`                             | :mount_fuji: `:mount_fuji:`                           | :sunrise_over_mountains: `:sunrise_over_mountains:` |
| :sunrise: `:sunrise:`                         | :stars: `:stars:`                                     | :statue_of_liberty: `:statue_of_liberty:`           |
| :bridge_at_night: `:bridge_at_night:`         | :carousel_horse: `:carousel_horse:`                   | :rainbow: `:rainbow:`                               |
| :ferris_wheel: `:ferris_wheel:`               | :fountain: `:fountain:`                               | :roller_coaster: `:roller_coaster:`                 |
| :ship: `:ship:`                               | :speedboat: `:speedboat:`                             | :boat: `:boat:`                                     |
| :sailboat: `:sailboat:`                       | :rowboat: `:rowboat:`                                 | :anchor: `:anchor:`                                 |
| :rocket: `:rocket:`                           | :airplane: `:airplane:`                               | :helicopter: `:helicopter:`                         |
| :steam_locomotive: `:steam_locomotive:`       | :tram: `:tram:`                                       | :mountain_railway: `:mountain_railway:`             |
| :bike: `:bike:`                               | :aerial_tramway: `:aerial_tramway:`                   | :suspension_railway: `:suspension_railway:`         |
| :mountain_cableway: `:mountain_cableway:`     | :tractor: `:tractor:`                                 | :blue_car: `:blue_car:`                             |
| :oncoming_automobile: `:oncoming_automobile:` | :car: `:car:`                                         | :red_car: `:red_car:`                               |
| :taxi: `:taxi:`                               | :oncoming_taxi: `:oncoming_taxi:`                     | :articulated_lorry: `:articulated_lorry:`           |
| :bus: `:bus:`                                 | :oncoming_bus: `:oncoming_bus:`                       | :rotating_light: `:rotating_light:`                 |
| :police_car: `:police_car:`                   | :oncoming_police_car: `:oncoming_police_car:`         | :fire_engine: `:fire_engine:`                       |
| :ambulance: `:ambulance:`                     | :minibus: `:minibus:`                                 | :truck: `:truck:`                                   |
| :train: `:train:`                             | :station: `:station:`                                 | :train2: `:train2:`                                 |
| :bullettrain_front: `:bullettrain_front:`     | :bullettrain_side: `:bullettrain_side:`               | :light_rail: `:light_rail:`                         |
| :monorail: `:monorail:`                       | :railway_car: `:railway_car:`                         | :trolleybus: `:trolleybus:`                         |
| :ticket: `:ticket:`                           | :fuelpump: `:fuelpump:`                               | :vertical_traffic_light: `:vertical_traffic_light:` |
| :traffic_light: `:traffic_light:`             | :warning: `:warning:`                                 | :construction: `:construction:`                     |
| :beginner: `:beginner:`                       | :atm: `:atm:`                                         | :slot_machine: `:slot_machine:`                     |
| :busstop: `:busstop:`                         | :barber: `:barber:`                                   | :hotsprings: `:hotsprings:`                         |
| :checkered_flag: `:checkered_flag:`           | :crossed_flags: `:crossed_flags:`                     | :izakaya_lantern: `:izakaya_lantern:`               |
| :moyai: `:moyai:`                             | :circus_tent: `:circus_tent:`                         | :performing_arts: `:performing_arts:`               |
| :round_pushpin: `:round_pushpin:`             | :triangular_flag_on_post: `:triangular_flag_on_post:` | :jp: `:jp:`                                         |
| :kr: `:kr:`                                   | :cn: `:cn:`                                           | :us: `:us:`                                         |
| :fr: `:fr:`                                   | :es: `:es:`                                           | :it: `:it:`                                         |
| :ru: `:ru:`                                   | :gb: `:gb:`                                           | :uk: `:uk:`                                         |
| :de: `:de:`                                   |

### Símbolos

| :one: `:one:`                                                         | :two: `:two:`                                                 | :three: `:three:`                                         |
|-----------------------------------------------------------------------|---------------------------------------------------------------|-----------------------------------------------------------|
| :four: `:four:`                                                       | :five: `:five:`                                               | :six: `:six:`                                             |
| :seven: `:seven:`                                                     | :eight: `:eight:`                                             | :nine: `:nine:`                                           |
| :keycap_ten: `:keycap_ten:`                                           | :1234: `:1234:`                                               | :zero: `:zero:`                                           |
| :hash: `:hash:`                                                       | :symbols: `:symbols:`                                         | :arrow_backward: `:arrow_backward:`                       |
| :arrow_down: `:arrow_down:`                                           | :arrow_forward: `:arrow_forward:`                             | :arrow_left: `:arrow_left:`                               |
| :capital_abcd: `:capital_abcd:`                                       | :abcd: `:abcd:`                                               | :abc: `:abc:`                                             |
| :arrow_lower_left: `:arrow_lower_left:`                               | :arrow_lower_right: `:arrow_lower_right:`                     | :arrow_right: `:arrow_right:`                             |
| :arrow_up: `:arrow_up:`                                               | :arrow_upper_left: `:arrow_upper_left:`                       | :arrow_upper_right: `:arrow_upper_right:`                 |
| :arrow_double_down: `:arrow_double_down:`                             | :arrow_double_up: `:arrow_double_up:`                         | :arrow_down_small: `:arrow_down_small:`                   |
| :arrow_heading_down: `:arrow_heading_down:`                           | :arrow_heading_up: `:arrow_heading_up:`                       | :leftwards_arrow_with_hook: `:leftwards_arrow_with_hook:` |
| :arrow_right_hook: `:arrow_right_hook:`                               | :left_right_arrow: `:left_right_arrow:`                       | :arrow_up_down: `:arrow_up_down:`                         |
| :arrow_up_small: `:arrow_up_small:`                                   | :arrows_clockwise: `:arrows_clockwise:`                       | :arrows_counterclockwise: `:arrows_counterclockwise:`     |
| :rewind: `:rewind:`                                                   | :fast_forward: `:fast_forward:`                               | :information_source: `:information_source:`               |
| :ok: `:ok:`                                                           | :twisted_rightwards_arrows: `:twisted_rightwards_arrows:`     | :repeat: `:repeat:`                                       |
| :repeat_one: `:repeat_one:`                                           | :new: `:new:`                                                 | :top: `:top:`                                             |
| :up: `:up:`                                                           | :cool: `:cool:`                                               | :free: `:free:`                                           |
| :ng: `:ng:`                                                           | :cinema: `:cinema:`                                           | :koko: `:koko:`                                           |
| :signal_strength: `:signal_strength:`                                 | :u5272: `:u5272:`                                             | :u5408: `:u5408:`                                         |
| :u55b6: `:u55b6:`                                                     | :u6307: `:u6307:`                                             | :u6708: `:u6708:`                                         |
| :u6709: `:u6709:`                                                     | :u6e80: `:u6e80:`                                             | :u7121: `:u7121:`                                         |
| :u7533: `:u7533:`                                                     | :u7a7a: `:u7a7a:`                                             | :u7981: `:u7981:`                                         |
| :sa: `:sa:`                                                           | :restroom: `:restroom:`                                       | :mens: `:mens:`                                           |
| :womens: `:womens:`                                                   | :baby_symbol: `:baby_symbol:`                                 | :no_smoking: `:no_smoking:`                               |
| :parking: `:parking:`                                                 | :wheelchair: `:wheelchair:`                                   | :metro: `:metro:`                                         |
| :baggage_claim: `:baggage_claim:`                                     | :accept: `:accept:`                                           | :wc: `:wc:`                                               |
| :potable_water: `:potable_water:`                                     | :put_litter_in_its_place: `:put_litter_in_its_place:`         | :secret: `:secret:`                                       |
| :congratulations: `:congratulations:`                                 | :m: `:m:`                                                     | :passport_control: `:passport_control:`                   |
| :left_luggage: `:left_luggage:`                                       | :customs: `:customs:`                                         | :ideograph_advantage: `:ideograph_advantage:`             |
| :cl: `:cl:`                                                           | :sos: `:sos:`                                                 | :id: `:id:`                                               |
| :no_entry_sign: `:no_entry_sign:`                                     | :underage: `:underage:`                                       | :no_mobile_phones: `:no_mobile_phones:`                   |
| :do_not_litter: `:do_not_litter:`                                     | :non-potable_water: `:non-potable_water:`                     | :no_bicycles: `:no_bicycles:`                             |
| :no_pedestrians: `:no_pedestrians:`                                   | :children_crossing: `:children_crossing:`                     | :no_entry: `:no_entry:`                                   |
| :eight_spoked_asterisk: `:eight_spoked_asterisk:`                     | :eight_pointed_black_star: `:eight_pointed_black_star:`       | :heart_decoration: `:heart_decoration:`                   |
| :vs: `:vs:`                                                           | :vibration_mode: `:vibration_mode:`                           | :mobile_phone_off: `:mobile_phone_off:`                   |
| :chart: `:chart:`                                                     | :currency_exchange: `:currency_exchange:`                     | :aries: `:aries:`                                         |
| :taurus: `:taurus:`                                                   | :gemini: `:gemini:`                                           | :cancer: `:cancer:`                                       |
| :leo: `:leo:`                                                         | :virgo: `:virgo:`                                             | :libra: `:libra:`                                         |
| :scorpius: `:scorpius:`                                               | :sagittarius: `:sagittarius:`                                 | :capricorn: `:capricorn:`                                 |
| :aquarius: `:aquarius:`                                               | :pisces: `:pisces:`                                           | :ophiuchus: `:ophiuchus:`                                 |
| :six_pointed_star: `:six_pointed_star:`                               | :negative_squared_cross_mark: `:negative_squared_cross_mark:` | :a: `:a:`                                                 |
| :b: `:b:`                                                             | :ab: `:ab:`                                                   | :o2: `:o2:`                                               |
| :diamond_shape_with_a_dot_inside: `:diamond_shape_with_a_dot_inside:` | :recycle: `:recycle:`                                         | :end: `:end:`                                             |
| :on: `:on:`                                                           | :soon: `:soon:`                                               | :clock1: `:clock1:`                                       |
| :clock130: `:clock130:`                                               | :clock10: `:clock10:`                                         | :clock1030: `:clock1030:`                                 |
| :clock11: `:clock11:`                                                 | :clock1130: `:clock1130:`                                     | :clock12: `:clock12:`                                     |
| :clock1230: `:clock1230:`                                             | :clock2: `:clock2:`                                           | :clock230: `:clock230:`                                   |
| :clock3: `:clock3:`                                                   | :clock330: `:clock330:`                                       | :clock4: `:clock4:`                                       |
| :clock430: `:clock430:`                                               | :clock5: `:clock5:`                                           | :clock530: `:clock530:`                                   |
| :clock6: `:clock6:`                                                   | :clock630: `:clock630:`                                       | :clock7: `:clock7:`                                       |
| :clock730: `:clock730:`                                               | :clock8: `:clock8:`                                           | :clock830: `:clock830:`                                   |
| :clock9: `:clock9:`                                                   | :clock930: `:clock930:`                                       | :heavy_dollar_sign: `:heavy_dollar_sign:`                 |
| :copyright: `:copyright:`                                             | :registered: `:registered:`                                   | :tm: `:tm:`                                               |
| :x: `:x:`                                                             | :heavy_exclamation_mark: `:heavy_exclamation_mark:`           | :bangbang: `:bangbang:`                                   |
| :interrobang: `:interrobang:`                                         | :o: `:o:`                                                     | :heavy_multiplication_x: `:heavy_multiplication_x:`       |
| :heavy_plus_sign: `:heavy_plus_sign:`                                 | :heavy_minus_sign: `:heavy_minus_sign:`                       | :heavy_division_sign: `:heavy_division_sign:`             |
| :white_flower: `:white_flower:`                                       | :100: `:100:`                                                 | :heavy_check_mark: `:heavy_check_mark:`                   |
| :ballot_box_with_check: `:ballot_box_with_check:`                     | :radio_button: `:radio_button:`                               | :link: `:link:`                                           |
| :curly_loop: `:curly_loop:`                                           | :wavy_dash: `:wavy_dash:`                                     | :part_alternation_mark: `:part_alternation_mark:`         |
| :trident: `:trident:`                                                 | :black_square: `:black_square:`                               | :white_square: `:white_square:`                           |
| :white_check_mark: `:white_check_mark:`                               | :black_square_button: `:black_square_button:`                 | :white_square_button: `:white_square_button:`             |
| :black_circle: `:black_circle:`                                       | :white_circle: `:white_circle:`                               | :red_circle: `:red_circle:`                               |
| :large_blue_circle: `:large_blue_circle:`                             | :large_blue_diamond: `:large_blue_diamond:`                   | :large_orange_diamond: `:large_orange_diamond:`           |
| :small_blue_diamond: `:small_blue_diamond:`                           | :small_orange_diamond: `:small_orange_diamond:`               | :small_red_triangle: `:small_red_triangle:`               |
| :small_red_triangle_down: `:small_red_triangle_down:`                 | :shipit: `:shipit:`                                           |

## Referencias

- https://www.markdownguide.org/basic-syntax/

# Markdown - Grundlegende Syntax

---

_basierend auf https://www.markdownguide.org/basic-syntax/_

---

## Übersicht
Fast alle Markdown-Anwendungen unterstützen die im ursprünglichen Markdown-Entwurfsdokument beschriebene Grundsyntax. Es gibt geringe Varianten und Abweichungen zwischen den Markdown-Prozessoren – sie werden, wo möglich, im Text vermerkt.

## Überschriften

Um eine Überschrift zu erstellen, fügen Sie vor ein Wort oder einen Satz Rautenzeichen (`#`) ein.
Die Anzahl der verwendeten Rautenzeichen muss der Ebene der Überschrift entsprechen.
Verwenden Sie beispielsweise für eine Überschrift der dritten Ebene (`<h3>`) drei Rautenzeichen (zum Beispiel `### My Header`).

| Markup          | \tHTML                       | Gerenderte Ausgabe        |
|---------------------|------------------------------|--------------------------|
| `# Heading level 1` | \t`<h1>Heading level 1</h1>` | <h1>Heading level 1</h1> |
| `# Heading level 2` | \t`<h2>Heading level 2</h2>` | <h1>Heading level 1</h1> |
| `# Heading level 3` | \t`<h3>Heading level 3</h3>` | <h3>Heading level 3</h3> |
| `# Heading level 4` | \t`<h4>Heading level 4</h4>` | <h4>Heading level 4</h4> |
| `# Heading level 5` | \t`<h5>Heading level 5</h5>` | <h5>Heading level 5</h5> |
| `# Heading level 6` | \t`<h6>Heading level 6</h6>` | <h6>Heading level 6</h6> |

## Alternative Syntax
Alternativ können Sie in der Zeile unter dem Text eine beliebige Anzahl von `==`-Zeichen für eine Überschrift der Ebene 1 oder `--`-Zeichen für eine Überschrift der Ebene 2 einfügen.

| Markup                                                                | \tHTML                       | Gerenderte Ausgabe        |
|---------------------------------------------------------------------------|------------------------------|--------------------------|
| <code class="highlighter-rouge">Heading level 1<br>===============</code> | \t`<h1>Heading level 1</h1>` | <h1>Heading level 1</h1> |
| <code class="highlighter-rouge">Heading level 2<br>---------------</code> | \t`<h2>Heading level 2</h2>` | <h2>Heading level 2</h2> |

## Überschriften: Bewährte Praktiken
Die Markdown-Anwendungen sind sich nicht einig darüber, wie mit einem fehlenden Leerzeichen zwischen den Rautenzeichen (`#`) und dem Überschriftentext umgegangen wird. Aus Kompatibilitätsgründen setzen Sie immer ein Leerzeichen zwischen die Rautenzeichen und den Überschriftentext.

|  ✅&nbsp; So machen Sie es   | ❌&nbsp; Nicht so |
|:--------------------:|:---------------------:|
| `# Here's a Heading` |  `#Here's a Heading`  |


Aus Kompatibilitätsgründen setzen Sie außerdem Leerzeilen vor und nach einer Überschrift.

| ✅  So machen Sie es                                                                                  | ❌ Nicht so                                                                                         |
|------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| <code>Try to put a blank line before...<br><br># Heading<br><br>...and after a heading.</code> | <code>Without blank lines, this might not look right.<br># Heading<br>        Don't do this!</code> |


## Absätze

Um Absätze zu erstellen, verwenden Sie eine Leerzeile, um eine oder mehrere Textzeilen voneinander zu trennen.

| MarkDown                                    | \tHTML\t                                      | Gerenderte Ausgabe                       |
|---------------------------------------------|---------------------------------------------|-----------------------------------------|
| <code>Paragrafo1.<br><br>Paragrafo2.</code> | `<p>Paragrafo1.</p><p>Paragrafo2.</p>` | <code>Paragrafo1.<br>Paragrafo2.</code> |

## Bewährte Praktiken für Absätze

Sofern der [Absatz in einer Liste enthalten ist](#adicionando-elementos-em-listas), rücken Sie Absätze nicht mit Leerzeichen oder Tabulatoren ein.

>  ℹ **Hinweis:** Wenn Sie Absätze in der Ausgabe einrücken müssen, finden Sie Informationen im Abschnitt über Einrückungen (Tabulatoren).

|          ✅&nbsp; So machen Sie es                                | ❌&nbsp; Nicht so                                          |
| ---------------------------------------------------------- | ---------------------------------------------------------------- |
| Setzen Sie keine Tabulatoren oder Leerzeichen vor die Absätze.    | Das kann zu unerwarteten Formatierungsproblemen führen.       |
| Halten Sie die Zeilen wie hier linksbündig.             | Fügen Sie keine Tabulatoren oder Leerzeichen vor die Absätze ein.         |

## Zeilenumbrüche

Um einen Zeilenumbruch oder eine neue Zeile (`<br>`) zu erstellen, beenden Sie eine Zeile mit zwei oder mehr Leerzeichen und drücken Sie die Eingabetaste.

| Markup                  | HTML                             | Gerenderte Ausgabe          |
| --------------------------- | ---------------------------------|----------------------------|
| Dies ist die erste Zeile.    | <p>Esta é a primeira linha.<br>  | Dies ist die erste Zeile.   |
| Und dies ist die zweite Zeile.   | E esta é a segunda linha.</p>    | Und dies ist die zweite Zeile.  |

### Bewährte Praktiken für Zeilenumbrüche
<!-- TODO: line-break-best-practices -->

Sie können in fast allen Markdown-Anwendungen zwei oder mehr Leerzeichen (umgangssprachlich „trailing spaces“) für Zeilenumbrüche verwenden, aber das ist umstritten. In einem Editor ist es schwierig, Leerzeichen am Zeilenende zu erkennen, und viele Menschen setzen versehentlich oder absichtlich nach jedem Satz zwei Leerzeichen. Aus diesem Grund können Sie für Zeilenumbrüche auch etwas anderes als Leerzeichen am Zeilenende verwenden. Wenn Ihre Anwendung [Markdown HTML unterstützt](#html), können Sie das HTML-Tag `<br>` verwenden.

Aus Kompatibilitätsgründen verwenden Sie Leerzeichen am Zeilenende oder das HTML-Tag `<br>` am Ende der Zeile.

Es gibt zwei weitere Optionen, die ich nicht empfehle. CommonMark und einige andere leichte Auszeichnungssprachen erlauben ein Backslash-Zeichen (`\`) am Zeilenende, aber nicht alle Markdown-Anwendungen unterstützen das; aus Kompatibilitätssicht ist es also keine gute Option. Und zumindest einige leichte Auszeichnungssprachen benötigen nichts am Zeilenende – Sie drücken einfach die Eingabetaste und es wird ein Zeilenumbruch erzeugt.

| ✅&nbsp; So machen Sie es                       | ❌&nbsp; Nicht so                         |
| ---------------------------------------- | ----------------------------------------------- |
| Erste Zeile mit zwei Leerzeichen danach.        | Primeira linha com uma barra invertida depois.\ |
| Und die nächste Zeile.                       |Und die nächste Zeile.                               |                  |
| First line with the HTML tag after.<br>  | Erste Zeile ohne etwas danach.                 |
|Und die nächste Zeile.                        |Und die nächste Zeile.                               |

## Hervorhebung

Sie können Hervorhebungen erzeugen, indem Sie Text fett oder kursiv setzen.

### Fett

Um Text fett zu setzen, fügen Sie vor und nach einem Wort oder Satz zwei Sternchen oder Unterstriche ein. Um die Mitte eines Wortes fett zu setzen, fügen Sie zwei Sternchen ohne Leerzeichen um die Buchstaben ein.

| Markup                     | HTML                                        | Gerenderte Ausgabe               |
| ------------------------------ | ------------------------------------------- | --------------------------------|
| Eu amo `**texto em negrito**`. | Eu adoro <strong>texto em negrito</strong>. | Eu adoro **texto em negrito** . |
| Eu amo `__texto em negrito__`. | Eu adoro <strong>texto em negrito</strong>. | Eu adoro __texto em negrito__ . |
| O amor `**é**` negrito         | O amor<strong>é</strong>negrito             | O amor **é** negrito            |

#### Bewährte Praktiken für Fettdruck

Die Markdown-Anwendungen sind sich nicht einig darüber, wie mit Unterstrichen in der Mitte eines Wortes umgegangen wird. Aus Kompatibilitätsgründen verwenden Sie Sternchen, um die Mitte eines Wortes fett zu setzen.

|✅&nbsp; So machen Sie es     | ❌&nbsp; Nicht so |
|------------------------|----------------------- |
| O amor `**é**` negrito | O amor`__é__`negrito    |

### Kursiv

Um Text kursiv zu setzen, fügen Sie vor und nach einem Wort oder Satz ein Sternchen oder einen Unterstrich ein. Um die Mitte eines Wortes kursiv zu setzen, fügen Sie ein Sternchen ohne Leerzeichen um die Buchstaben ein.

| Markup                                   | HTML                                            | Gerenderte Ausgabe                        |
| -------------------------------------------- | ----------------------------------------------- | ---------------------------------------- |
| O texto em itálico é o `*miado do gato*`.    | O texto em itálico é o <em>miado do gato</em>.  | O texto em itálico é o *miado do gato* . |
| O texto em itálico é o `_miado do gato_`.    | O texto em itálico é o <em>miado do gato</em>.  | O texto em itálico é o _miado do gato_ . |
| Um `*gato*` miau                             | Um <em>gato</em>> miau                          | Um *gato* miau                           |

#### Bewährte Praktiken für Kursivschrift
<!-- TODO: italic-best-practices -->

Die Markdown-Anwendungen sind sich nicht einig darüber, wie mit Unterstrichen in der Mitte eines Wortes umgegangen wird. Aus Kompatibilitätsgründen verwenden Sie Sternchen, um die Mitte eines Wortes kursiv zu setzen.

|✅&nbsp; So machen Sie es     |❌&nbsp; Nicht so    |
|------------------------| ------------------------ |
| Um `*gato*` miau       | Um`_gato_`miau         |

### Fett und Kursiv
<!-- TODO: bold-and-italic -->

Um Text gleichzeitig fett und kursiv zu betonen, fügen Sie vor und nach einem Wort oder Satz drei Sternchen oder Unterstriche ein. Um die Mitte eines Wortes fett und kursiv zu setzen, fügen Sie drei Sternchen ohne Leerzeichen um die Buchstaben ein.

| Markup                                       | HTML                                                                | Gerenderte Ausgabe                              |
| ------------------------------------------------ | ------------------------------------------------------------------- | ---------------------------------------------- |
| Este texto é `***realmente importante***`.       | Este texto é `<em><strong>realmente importante</strong></em>`.      | Este texto é ***realmente importante***.       |
| Este texto é `___realmente importante___`.       | Este texto é `<em><strong>realmente importante</strong></em>`.      | Este texto é ___realmente importante___.       |
| Este texto é `__*realmente importante*__`.       | Este texto é `<em><strong>realmente importante</strong></em>`.      | Este texto é __*realmente importante*__.       |
| Este texto é `**_realmente importante**_`.       | Este texto é `<em><strong>realmente importante</strong></em>`.      | Este texto é **_realmente importante**_.       |
| Este texto é realmente `***muito***` importante. | Este texto é realmente `<em><strong>muito importante</strong></em>`.| Este texto é realmente ***muito*** importante. |

>  ℹ **Hinweis:** Die Reihenfolge der Tags `em` und `strong` kann je nach verwendetem Markdown-Prozessor umgekehrt sein.

#### Bewährte Praktiken für Fett und Kursiv
<!-- TODO: bold-and-italic-best-practices -->

Die Markdown-Anwendungen sind sich nicht einig darüber, wie mit Unterstrichen in der Mitte eines Wortes umgegangen wird. Aus Kompatibilitätsgründen verwenden Sie Sternchen, um die Mitte eines Wortes fett und kursiv zu setzen.

|✅&nbsp; So machen Sie es                               |❌&nbsp; Nicht so                          |
|-------------------------------------------------| ----------------------------------------------- |
| Este texto é realmente `***muito***` importante.| Este texto é realmente`___muito___`importante.|

## Blockzitate

Um ein Blockzitat zu erstellen, fügen Sie vor einen Absatz ein `>` ein.

    > Dorothy followed her through many of the beautiful rooms in her castle.

Die gerenderte Ausgabe sieht so aus:

> Dorothy folgte ihr durch viele der schönen Zimmer ihres Schlosses.


### Blockzitate mit mehreren Absätzen
<!-- TODO: blockquotes-with-multiple-paragraphs -->

Blockzitate können mehrere Absätze enthalten. Fügen Sie in den Leerzeilen zwischen den Absätzen ein `>` ein.

    > Dorothy a seguiu por muitos dos belos quartos de seu castelo.

    >

    > A Bruxa ordenou-lhe que limpasse as panelas e as chaleiras, varresse o chão e mantivesse o fogo alimentado com lenha.

Die gerenderte Ausgabe sieht so aus:

> Dorothy folgte ihr durch viele der schönen Zimmer ihres Schlosses.
>
> Die Hexe befahl ihr, die Töpfe und Kessel zu scheuern, den Boden zu fegen und das Feuer mit Holz am Brennen zu halten.

### Verschachtelte Blockzitate
<!-- TODO: nested-blockquotes -->

Blockzitate können verschachtelt werden. Fügen Sie vor den Absatz, den Sie verschachteln möchten, ein `>>` ein.

    > Dorothy a seguiu por muitos dos belos quartos de seu castelo.

    >

    >> A Bruxa ordenou-lhe que limpasse as panelas e as chaleiras, varresse o chão e mantivesse o fogo alimentado com lenha.

Die gerenderte Ausgabe sieht so aus:

> Dorothy folgte ihr durch viele der schönen Zimmer ihres Schlosses.
>
>> Die Hexe befahl ihr, die Töpfe und Kessel zu scheuern, den Boden zu fegen und das Feuer mit Holz am Brennen zu halten.

### Blockzitate mit anderen Elementen
<!-- TODO: blockquotes-with-other-elements -->

Blockzitate können andere Markdown-formatierte Elemente enthalten. Nicht alle Elemente können verwendet werden ​`​​​—` Sie müssen ausprobieren, welche funktionieren.

    > #### Os resultados trimestrais parecem ótimos!

    >

    > - A receita estava fora do gráfico.

    > - Os lucros foram maiores do que nunca.

    >

    > *Tudo* está indo conforme o **planejado** .

Die gerenderte Ausgabe sieht so aus:

> #### Die Quartalsergebnisse sehen großartig aus!
>
> - Der Umsatz war außerhalb des Diagramms.
> - Die Gewinne waren so hoch wie nie zuvor.
>
> *Alles* geht nach **Plan**.

### Bewährte Praktiken für Blockzitate
<!-- TODO: blockquotes-best-practices -->

Aus Kompatibilitätsgründen setzen Sie Leerzeilen vor und nach die Zitate.

| ✅&nbsp; So machen Sie es                        | ❌&nbsp; Nicht so                             |
| ------------------------------------------ | -------------------------------------------------- |
| Versuchen Sie, eine Leerzeile davor zu setzen... | Sem linhas em branco, isso pode não parecer certo.\
|                                            | > Esta é uma citação em bloco\
| > Esta é uma citação em bloco              | Não faça isso!\
|                                            |                                                    |
| ...und nach einem Blockzitat.       |                                                    |

## Listen

Sie können Elemente in geordneten und ungeordneten Listen sortieren.

### Geordnete Listen
<!-- TODO: ordered-lists -->

Um eine geordnete Liste zu erstellen, fügen Sie Listenelemente mit Zahlen gefolgt von Punkten ein. Die Zahlen müssen nicht in numerischer Reihenfolge stehen, aber die Liste muss mit der Zahl eins beginnen.

| Markup                                       | HTML                                                                | Gerenderte Ausgabe                              |
| ------------------------------------------------ | ------------------------------------------------------------------- | ---------------------------------------------- |
| 1. Primeiro item <br> 2. Segundo item <br> 3. Terceiro item <br> 4. Quarto item| `<ol>`<br>ㅤ`<li>Primeiro item</li>`<br>ㅤ`<li>Segundo item</li>`<br>ㅤ`<li>Terceiro item</li>`<br>ㅤ`<li>Quarto item</li>`<br>`</ol>`| 1. Primeiro item <br> 2. Segundo item <br> 3. Terceiro item <br> 4. Quarto item|
| 1. Primeiro item <br> 1. Segundo item <br> 1. Terceiro item <br> 1. Quarto item| `<ol>`<br>ㅤ`<li>Primeiro item</li>`<br>ㅤ`<li>Segundo item</li>`<br>ㅤ`<li>Terceiro item</li>`<br>ㅤ`<li>Quarto item</li>`<br>`</ol>`| 1. Primeiro item <br> 2. Segundo item <br> 3. Terceiro item <br> 4. Quarto item|
| 1. Primeiro item <br> 8. Segundo item <br> 3. Terceiro item <br> 5. Quarto item| `<ol>`<br>ㅤ`<li>Primeiro item</li>`<br>ㅤ`<li>Segundo item</li>`<br>ㅤ`<li>Terceiro item</li>`<br>ㅤ`<li>Quarto item</li>`<br>`</ol>`| 1. Primeiro item <br> 2. Segundo item <br> 3. Terceiro item <br> 4. Quarto item|
| 1. Primeiro item <br> 2. Segundo item <br> 3. Terceiro item <br>ㅤㅤ1. Item recuado <br>ㅤㅤ2. Item recuado <br> 4. Quarto item | `<ol>`<br>ㅤ`<li>Primeiro item</li>`<br>ㅤ`<li>Segundo item</li>`<br>ㅤ`<li>Terceiro item</li>`<br>ㅤ`<li>Quarto item</li>`<br>`</ol>`| 1. Primeiro item <br> 2. Segundo item <br> 3. Terceiro item <br>ㅤㅤ1. Item recuado <br>ㅤㅤ2. Item recuado <br> 4. Quarto item |

#### Bewährte Praktiken für geordnete Listen
<!-- TODO: ordered-list-best-practices -->

CommonMark und einige andere leichte Auszeichnungssprachen erlauben die Verwendung von Klammern `( ))` als Trennzeichen (zum Beispiel 1) _First item_), aber nicht alle Markdown-Anwendungen unterstützen das; aus Kompatibilitätssicht ist es also keine gute Option. Verwenden Sie ausschließlich Punkte.

|✅&nbsp; So machen Sie es |❌&nbsp; Nicht so |
| ----------------- | ---------------------- |
|1. First item<br>  |1) First item<br>       |
|2. Second item     |2) Second item          |

### Ungeordnete Listen
<!-- TODO: unordered-lists -->

Um eine ungeordnete Liste zu erstellen, fügen Sie den Listenelementen Bindestriche (`-`), Sternchen (`*`) oder Pluszeichen (`+`) voran. Rücken Sie ein oder mehrere Elemente ein, um eine verschachtelte Liste zu erstellen.

| Markup                                       | HTML                                                                | Gerenderte Ausgabe                              |
| ------------------------------------------------ | ------------------------------------------------------------------- | ---------------------------------------------- |
| - Primeiro item <br> - Segundo item <br> - Terceiro item <br> - Quarto item| `<ul>`<br>ㅤ`<li>Primeiro item</li>`<br>ㅤ`<li>Segundo item</li>`<br>ㅤ`<li>Terceiro item</li>`<br>ㅤ`<li>Quarto item</li>`<br>`</ul>`| • Primeiro item <br> • Segundo item <br> • Terceiro item <br> • Quarto item|
| * Primeiro item <br> * Segundo item <br> * Terceiro item <br> * Quarto item| `<ul>`<br>ㅤ`<li>Primeiro item</li>`<br>ㅤ`<li>Segundo item</li>`<br>ㅤ`<li>Terceiro item</li>`<br>ㅤ`<li>Quarto item</li>`<br>`</ul>`| • Primeiro item <br> • Segundo item <br> • Terceiro item <br> • Quarto item|
| + Primeiro item <br> + Segundo item <br> + Terceiro item <br> + Quarto item| `<ul>`<br>ㅤ`<li>Primeiro item</li>`<br>ㅤ`<li>Segundo item</li>`<br>ㅤ`<li>Terceiro item</li>`<br>ㅤ`<li>Quarto item</li>`<br>`</ul>`| • Primeiro item <br> • Segundo item <br> • Terceiro item <br> • Quarto item|
| - Primeiro item <br> - Segundo item <br> - Terceiro item <br>ㅤㅤ- Item recuado <br>ㅤㅤ- Item recuado <br> - Quarto item | `<ul>`<br>ㅤ`<li>Primeiro item</li>`<br>ㅤ`<li>Segundo item</li>`<br>ㅤ`<li>Terceiro item</li>`<br>ㅤ`<li>Quarto item</li>`<br>`</ul>`| • Primeiro item <br> • Segundo item <br> • Terceiro item <br>ㅤㅤ◦ Item recuado <br>ㅤㅤ◦ Item recuado <br> • Quarto item |

#### Ungeordnete Listen mit Zahlen beginnen
<!-- TODO: starting-unordered-list-items-with-numbers -->

Wenn Sie ein ungeordnetes Listenelement mit einer Zahl gefolgt von einem Punkt beginnen müssen, können Sie den Punkt mit einem Backslash (`/`) [escapen](#caracteres-escapando).

| Markup                                                      | HTML                                         | Gerenderte Ausgabe                    |
| --------------------------------------------------------------- | -------------------------------------------- | ------------------------------------ |
| - 1968\. Um ótimo ano!<br>- Acho que 1969 foi o segundo melhor. |`<ul>`<br>ㅤ`<li>1968. Um ótimo ano!</li>`<br>`<li>Acho que 1969 foi o segundo melhor.</li>`<br>`</ul>` |• 1968. Um ótimo ano!<br>• Acho que 1969 foi o segundo melhor.|

#### Bewährte Praktiken für ungeordnete Listen
<!-- TODO: unordered-list-best-practices -->

Die Markdown-Anwendungen sind sich nicht einig darüber, wie mit unterschiedlichen Trennzeichen in derselben Liste umgegangen wird. Aus Kompatibilitätsgründen mischen Sie Trennzeichen in derselben Liste nicht `–` wählen Sie eines und behalten Sie es bei.

| ✅&nbsp; So machen Sie es                                                       | ❌&nbsp; Nicht so |
| ------------------------------------------------------------------------ | ----------------------- |
| - Primeiro item<br>- Segundo item<br>- Terceiro item<br>- Quarto item    | + Primeiro item<br>* Segundo item<br>- Terceiro item<br>+ Quarto item|


### Elemente zu Listen hinzufügen
<!-- TODO: adding-elements-in-lists -->

Um ein weiteres Element zu einer Liste hinzuzufügen, ohne den Listenzusammenhang zu unterbrechen, rücken Sie das Element mit vier Leerzeichen oder einem Tabulator ein, wie in den folgenden Beispielen gezeigt.

>  ℹ **Tipp:** Wenn die Dinge nicht wie erwartet aussehen, überprüfen Sie, ob Sie die Listenelemente mit vier Leerzeichen oder einem Tabulator eingerückt haben.

#### Absätze

    * Este é o primeiro item da lista.
    * Aqui está o segundo item da lista.

        Preciso adicionar outro parágrafo abaixo do segundo item da lista.

    * E aqui está o terceiro item da lista.

Die gerenderte Ausgabe sieht so aus:

* Dies ist das erste Element der Liste.
* Hier ist das zweite Element der Liste.

    Ich muss einen weiteren Absatz unter das zweite Listenelement einfügen.

* Und hier ist das dritte Element der Liste.

#### Blockzitate
<!-- TODO: blockquotes -->

    * Este é o primeiro item da lista.
    * Aqui está o segundo item da lista.

        > Uma citação em bloco ficaria ótima abaixo do segundo item da lista.

    * E aqui está o terceiro item da lista

Die gerenderte Ausgabe sieht so aus:

* Dies ist das erste Element der Liste.
* Hier ist das zweite Element der Liste.
    > Ein Blockzitat würde unter dem zweiten Listenelement gut aussehen.
* Und hier ist das dritte Element der Liste

#### Codeblöcke
<!-- TODO: code-blocks-1 -->

[Codeblöcke](#blocos-de-codigos) werden normalerweise mit vier Leerzeichen oder einem Tabulator eingerückt. Wenn sie in einer Liste stehen, rücken Sie sie mit acht Leerzeichen oder zwei Tabulatoren ein.

    1. Abra o arquivo.
    2. Encontre o seguinte bloco de código na linha 21:

        <html>
          <head>
            <title>Test</title>
          </head>

    3. Atualize o título para corresponder ao nome do seu site.

Die gerenderte Ausgabe sieht so aus:

1. Öffnen Sie die Datei.
2. Finden Sie den folgenden Codeblock in Zeile 21:

        <html>
          <head>
            <title>Test</title>
          </head>

3. Aktualisieren Sie den Titel, damit er mit dem Namen Ihrer Website übereinstimmt.

#### Bilder
<!-- TODO: images -->

    1. Abra o arquivo que contém o mascote do Linux.
    2. Maravilhe-se com sua beleza.

        ![Tux, the Linux mascot](/assets/images/tux.png)

    3. Feche o arquivo.

Die gerenderte Ausgabe sieht so aus:

1. Öffnen Sie die Datei mit dem Linux-Maskottchen.
2. Bewundern Sie seine Schönheit.

    ![Tux, the Linux mascot](https://mdg.imgix.net/assets/images/tux.png?auto=format&fit=clip&q=40&w=100)

3. Schließen Sie die Datei.

#### Listen
<!-- TODO: lists -->

Sie können eine ungeordnete Liste in einer geordneten Liste verschachteln oder umgekehrt.

    1. Primeiro item
    2. Segundo item
    3. Terceiro item
          - Item recuado
          - Item recuado
    4. Quarto item

Die gerenderte Ausgabe sieht so aus:

1. Erstes Element
2. Zweites Element
3. Drittes Element
      - Eingerücktes Element
      - Eingerücktes Element
4. Viertes Element

## Code

Um ein Wort oder einen Satz als Code zu kennzeichnen, setzen Sie ihn zwischen Backticks (`).

|Markup                              |HTML                                                  |Gerenderte Ausgabe                       |
| -------------------------------------- | ---------------------------------------------------- |--------------------------------------- |
|``No prompt de comando, digite `Nano`.``| No prompt de comando, digite <code>Nano</code>.      |No prompt de comando, digite `nano`.    |

### Backticks escapen
<!-- TODO: escaping-backticks -->

Wenn das Wort oder der Satz, das oder den Sie als Code kennzeichnen möchten, ein oder mehrere Backticks enthält, können Sie es escapen, indem Sie das Wort oder den Satz zwischen doppelte Backticks setzen `( `` )`.

|Markup                             |HTML                                              |Gerenderte Ausgabe           |
| ------------------------------------- | ------------------------------------------------ | -------------------------  |
|``Use `code` em seu arquivo Markdown.``| <code>Use `code` em seu arquivo Markdown.</code> |Use ´code´ in your Markdown file.|

### Codeblöcke
<!-- TODO: code-blocks -->

Um Codeblöcke zu erstellen, rücken Sie jede Zeile des Blocks mit mindestens vier Leerzeichen oder einem Tabulator ein.

    <html>
      <head>
      </head>
    </html>

Die gerenderte Ausgabe sieht so aus:

    <html>
      <head>
      </head>
    </html>

>  ℹ **Hinweis:** Um Codeblöcke ohne eingerückte Zeilen zu erstellen, verwenden Sie [eingefasste Codeblöcke](https://www.markdownguide.org/extended-syntax/#fenced-code-blocks).

## Horizontale Linien

Um eine horizontale Linie zu erstellen, verwenden Sie drei oder mehr Sternchen (`***`), Bindestriche (`---`) oder Unterstriche (`___`) allein in einer Zeile.

    ***
    ---
    ______________
Die gerenderte Ausgabe aller drei sieht identisch aus:

_____________________________________________________

### Bewährte Praktiken für horizontale Linien
<!-- TODO: horizontal-rule-best-practices -->

Aus Kompatibilitätsgründen setzen Sie Leerzeilen vor und nach die horizontalen Linien.

| ✅&nbsp; So machen Sie es                                                                      | ❌&nbsp; Nicht so |
|----------------------------------------------------------------------------------------- |------------------------|
|Tente colocar uma linha em branco antes...<br><br>---<br><br>...e depois de uma regra horizontal. |Sem linhas em branco, este seria um título.<br>---<br>Não faça isso!|

## Links

Um einen Link zu erstellen, setzen Sie den Linktext zwischen eckige Klammern (zum Beispiel `[Duck Duck Go]`) und folgen Sie ihm unmittelbar mit der URL zwischen Klammern (zum Beispiel `(https://duckduckgo.com)`).

    My favorite search engine is [Duck Duck Go](https://duckduckgo.com).


Die gerenderte Ausgabe sieht so aus:

Meine Lieblingssuchmaschine ist [Duck Duck Go](https://duckduckgo.com).

>  ℹ **Hinweis:** Um ein Element auf derselben Seite zu verlinken, siehe [Verknüpfung mit Überschrift-IDs](https://www.markdownguide.org/extended-syntax/#linking-to-heading-ids). Um einen Link zu erstellen, der in einem neuen Tab oder Fenster geöffnet wird, siehe den Abschnitt über [Linkziele](https://www.markdownguide.org/hacks/#link-targets).

### Titel hinzufügen
<!-- TODO: adding-titles -->

Optional können Sie einen Titel für einen Link hinzufügen. Dieser erscheint als Tooltip, wenn der Benutzer mit der Maus über den Link fährt. Fügen Sie den Titel hinzu, indem Sie ihn in Anführungszeichen nach der URL setzen.

    My favorite search engine is [Duck Duck Go](https://duckduckgo.com "The best search engine for privacy").

Die gerenderte Ausgabe sieht so aus:
Meine Lieblingssuchmaschine ist [Duck Duck Go](https://duckduckgo.com).

### URLs und E-Mail-Adressen
<!-- TODO: urls-and-email-addresses -->

Um eine URL oder E-Mail-Adresse schnell in einen Link umzuwandeln, setzen Sie sie zwischen spitze Klammern.

    <https://www.markdownguide.org>
    <fake@example.com>

Die gerenderte Ausgabe sieht so aus:

 <https://www.markdownguide.org>

 <fake@example.com>

### Links formatieren
<!-- TODO: formatting-links -->

Um Links zu [betonen](#enfase), fügen Sie Sternchen vor und nach die eckigen Klammern und Klammern ein. Um Links als [Code](#codigo) zu kennzeichnen, setzen Sie Backticks zwischen die eckigen Klammern.

    Adoro apoiar a **[EFF](https://eff.org)**.

    Este é o *[Markdown Guide](https://www.markdownguide.org)*.

    Consulte a seção sobre [`code`](#codigo).

Die gerenderte Ausgabe sieht so aus:

Ich unterstütze gerne die **[EFF](https://eff.org)**.

Dies ist der *[Markdown Guide](https://www.markdownguide.org)*.

Siehe den Abschnitt über [`code`](#codigo).

### Referenz-Links
<!-- TODO: reference-style-links -->

Referenz-Links sind eine besondere Art von Link, die URLs in Markdown leichter anzuzeigen und zu lesen macht. Referenz-Links bestehen aus zwei Teilen: dem Teil, der mit Ihrem Text fließt, und dem Teil, den Sie an anderer Stelle in der Datei speichern, um den Text gut lesbar zu halten.

#### Den ersten Teil des Links formatieren
<!-- TODO: formatting-the-first-part-of-the-link -->

Der erste Teil eines Referenz-Links wird mit zwei Paaren eckiger Klammern formatiert. Das erste Paar eckiger Klammern umschließt den Text, der als Link erscheinen soll. Das zweite Paar eckiger Klammern zeigt eine Bezeichnung, die auf den Link verweist, den Sie an anderer Stelle im Dokument speichern.

Obwohl es nicht erforderlich ist, können Sie ein Leerzeichen zwischen das erste und das zweite Paar eckiger Klammern setzen. Die Bezeichnung im zweiten Paar eckiger Klammern unterscheidet nicht zwischen Groß- und Kleinschreibung und kann Buchstaben, Zahlen, Leerzeichen oder Zeichensetzung enthalten.

Das bedeutet, dass die folgenden Beispielformate für den primeiro Teil des Links annähernd gleichwertig sind:

* [hobbit-hole][1]
* [hobbit-hole][1]

#### Den zweiten Teil des Links formatieren
<!-- TODO: formatting-the-second-part-of-the-link -->

Der zweite Teil eines Referenz-Links wird mit den folgenden Attributen formatiert:

    1. O rótulo, entre colchetes, seguido imediatamente por dois pontos e pelo menos um espaço (por exemplo, [label]: ).
    2. O URL do link, que você pode colocar opcionalmente entre colchetes angulares.
    3. O título opcional do link, que você pode colocar entre aspas duplas, aspas simples ou parênteses.

Das bedeutet, dass die folgenden Beispielformate für den zweiten Teil des Links annähernd gleichwertig sind:

    * [1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle
    * [1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle "Hobbit lifestyles"
    * [1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle 'Hobbit lifestyles'
    * [1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle (Hobbit lifestyles)
    * [1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle "Hobbit lifestyles"
    * [1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle 'Hobbit lifestyles'
    * [1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle (Hobbit lifestyles)

Sie können diesen zweiten Teil des Links überall in Ihrem Markdown-Dokument platzieren. Einige platzieren ihn unmittelbar nach dem Absatz, in dem er erscheint, während andere ihn am Ende des Dokuments platzieren (wie Endnoten oder Fußnoten).

#### Ein Beispiel, das die Teile zusammenführt
<!-- TODO: an-example-putting-the-parts-together -->

Nehmen wir an, Sie fügen eine URL als [Standard-URL-Link](#ligacoes) in einen Absatz ein, und sie sieht in Markdown so aus:

    Num buraco no chão vivia um hobbit. Não é um buraco nojento, sujo e molhado, cheio de pontas
    de vermes e com cheiro de lodo, nem um buraco seco, vazio e arenoso, sem nada onde sentar ou onde sentar.
    comer: era uma [toca de hobbit](https://en.wikipedia.org/wiki/Hobbit#Lifestyle "Hobbit lifestyles"), e isso significa conforto.

Obwohl sie auf zusätzliche interessante Informationen verweisen mag, bringt die angezeigte URL dem vorhandenen Rohtext nicht viel außer dass sie ihn schwieriger lesbar macht. Um dies zu korrigieren, können Sie die URL so formatieren:

    Em um buraco no chão vivia um hobbit. Não um buraco nojento, sujo e úmido, cheio de pontas de minhocas e com cheiro de lodo, nem ainda um buraco seco, vazio e arenoso, sem nada onde sentar ou comer: era um [buraco de hobbit](https://en.wikipedia.org/wiki/Hobbit#Lifestyle), e isso significa conforto.

In beiden obigen Fällen wäre die gerenderte Ausgabe identisch:

>
> In einem Loch im Boden lebte ein Hobbit. Nicht ein widerliches, schmutziges, feuchtes Loch, voller Wurmhacken und mit Schlammgeruch, noch ein trockenes, leeres, sandiges Loch, ohne nichts zum Sitzen oder Essen: es war ein [Hobbit-Loch](https://en.wikipedia.org/wiki/Hobbit#Lifestyle), und das bedeutet Komfort.
>

und das HTML des Links wäre:

    <a href="https://en.wikipedia.org/wiki/Hobbit#Lifestyle title="Hobbit lifestyles">hobbit-hole</a>

### Bewährte Praktiken für Links
<!-- TODO: link-best-practices -->

Die Markdown-Anwendungen sind sich nicht einig darüber, wie mit Leerzeichen inmitten einer URL umgegangen wird. Aus Kompatibilitätsgründen versuchen Sie, Leerzeichen als %20 zu kodieren. Alternativ können Sie, wenn Ihre Anwendung [Markdown HTML unterstützt](#html), das HTML-Tag verwenden.

| ✅&nbsp; So machen Sie es                                       | ❌&nbsp; Nicht so                               |
| -------------------------------------------------------- | ------------------------------------------------------|
|`[link](https://www.example.com/my%20great%20page)`<br><br>`<a href="https://www.example.com/my great page">link</a>`|`[link](https://www.example.com/my great page)`<br><br>|

Auch Klammern inmitten einer URL können problematisch sein. Aus Kompatibilitätsgründen versuchen Sie, die öffnende Klammer `(()` als %28 und die schließende Klammer `( ))` als %29 zu kodieren. Alternativ können Sie, wenn Ihre Anwendung [Markdown HTML unterstützt](#html), das HTML-Tag verwenden.

| ✅&nbsp; So machen Sie es                                       | ❌&nbsp; Nicht so                               |
| -------------------------------------------------------- | ------------------------------------------------------|
|`[a novel](https://en.wikipedia.org/wiki/The_Milagro_Beanfield_War_%28novel%29)`<br><br>`<a href="https://en.wikipedia.org/wiki/The_Milagro_Beanfield_War_(novel)">a novel</a>`|`[a novel](https://en.wikipedia.org/wiki/The_Milagro_Beanfield_War_(novel))`|

## Bilder

Um ein Bild hinzuzufügen, fügen Sie ein Ausrufezeichen (`!`) gefolgt von alternativem Text zwischen eckigen Klammern und dem Pfad oder der URL der Bildressource zwischen Klammern ein. Optional können Sie einen Titel in Anführungszeichen nach dem Pfad oder der URL hinzufügen.

    ![The San Juan Mountains are beautiful!](/assets/images/san-juan-mountains.jpg "San Juan Mountains")

Die gerenderte Ausgabe sieht so aus:

![The San Juan Mountains are beautiful!](https://mdg.imgix.net/assets/images/san-juan-mountains.jpg?auto=format&fit=clip&q=40&w=800 "San Juan Mountains")

>  ℹ **Hinweis:** Um die Größe eines Bildes zu ändern, siehe den Abschnitt über [Bildgröße](https://www.markdownguide.org/hacks/#image-size). Um eine Bildunterschrift hinzuzufügen, siehe den Abschnitt über [Bildunterschriften](https://www.markdownguide.org/hacks/#image-captions).

### Bilder verlinken
<!-- TODO: linking-images -->

Um ein Bild zu verlinken, setzen Sie das Markdown des Bildes zwischen eckige Klammern und fügen Sie den Link zwischen Klammern hinzu.

    [![An old rock in the desert](/assets/images/shiprock.jpg "Shiprock, New Mexico by Beau Rogers")](https://www.flickr.com/photos/beaurogers/31833779864/in/photolist-Qv3rFw-34mt9F-a9Cmfy-5Ha3Zi-9msKdv-o3hgjr-hWpUte-4WMsJ1-KUQ8N-deshUb-vssBD-6CQci6-8AFCiD-zsJWT-nNfsgB-dPDwZJ-bn9JGn-5HtSXY-6CUhAL-a4UTXB-ugPum-KUPSo-fBLNm-6CUmpy-4WMsc9-8a7D3T-83KJev-6CQ2bK-nNusHJ-a78rQH-nw3NvT-7aq2qf-8wwBso-3nNceh-ugSKP-4mh4kh-bbeeqH-a7biME-q3PtTf-brFpgb-cg38zw-bXMZc-nJPELD-f58Lmo-bXMYG-bz8AAi-bxNtNT-bXMYi-bXMY6-bXMYv)


Die gerenderte Ausgabe sieht so aus:

[![An old rock in the desert](https://mdg.imgix.net/assets/images/shiprock.jpg?auto=format&fit=clip&q=40&w=800 "Shiprock, New Mexico by Beau Rogers")](https://www.flickr.com/photos/beaurogers/31833779864/in/photolist-Qv3rFw-34mt9F-a9Cmfy-5Ha3Zi-9msKdv-o3hgjr-hWpUte-4WMsJ1-KUQ8N-deshUb-vssBD-6CQci6-8AFCiD-zsJWT-nNfsgB-dPDwZJ-bn9JGn-5HtSXY-6CUhAL-a4UTXB-ugPum-KUPSo-fBLNm-6CUmpy-4WMsc9-8a7D3T-83KJev-6CQ2bK-nNusHJ-a78rQH-nw3NvT-7aq2qf-8wwBso-3nNceh-ugSKP-4mh4kh-bbeeqH-a7biME-q3PtTf-brFpgb-cg38zw-bXMZc-nJPELD-f58Lmo-bXMYG-bz8AAi-bxNtNT-bXMYi-bXMY6-bXMYv)

## Zeichen escapen

Um ein literalisches Zeichen anzuzeigen, das andernfalls zur Formatierung von Text in einem Markdown-Dokument verwendet würde, fügen Sie davor einen Backslash (`\`) ein.

    \* Without the backslash, this would be a bullet in an unordered list.

Die gerenderte Ausgabe sieht so aus:

* Ohne den Backslash wäre das ein Aufzählungspunkt in einer ungeordneten Liste.

### Zeichen, die escapt werden können
<!-- TODO: characters-you-can-escape -->

Sie können einen Backslash verwenden, um die folgenden Zeichen zu escapen.

|Zeichen   |Name                                                                            |
| ----------- | ------------------------------------------------------------------------------ |
|\            |Backslash                                                                       |
|`            |Backtick (siehe auch [Backticks im Code escapen](#escapando-de-crases))         |
|*            |Sternchen                                                                       |
|_            |Unterstrich                                                                     |
|{}           |geschweifte Klammern                                                            |
|[]           |eckige Klammern                                                                 |
|<>           |spitze Klammern                                                                 |
|()           |runde Klammern                                                                  |
|#            |Rautenzeichen                                                                   |
|+            |Pluszeichen                                                                     |
|-            |Minuszeichen (Bindestrich)                                                      |
|.            |Punkt                                                                           |
|!            |Ausrufezeichen                                                                  |
|||            |Senkrechter Strich                                                              |

## HTML

Viele Markdown-Anwendungen erlauben die Verwendung von HTML-Tags in Markdown-formatiertem Text. Das ist nützlich, wenn Sie bestimmte HTML-Tags gegenüber der Markdown-Syntax bevorzugen. Zum Beispiel empfinden manche Menschen HTML-Tags für Bilder als einfacher. HTML ist auch nützlich, wenn Sie Attribute eines Elements ändern müssen, z. B. um die [Textfarbe](https://www.markdownguide.org/hacks/#color) anzugeben oder die Breite eines Bildes zu ändern.

Um HTML zu verwenden, setzen Sie die Tags in den Text Ihrer Markdown-formatierten Datei.

    This **word** is bold. This <em>word</em> is italic.

Die gerenderte Ausgabe sieht so aus:

Dieses **Wort** ist fett. Dieses *Wort* ist kursiv.

### Bewährte Praktiken für HTML
<!-- TODO: html-best-practices -->

Aus Sicherheitsgründen unterstützen nicht alle Markdown-Anwendungen HTML in Markdown-Dokumenten. Im Zweifelsfall prüfen Sie die Dokumentation Ihrer Markdown-Anwendung. Einige Anwendungen unterstützen nur eine Teilmenge der HTML-Tags.

Verwenden Sie Leerzeilen, um HTML-Elemente der Blockebene wie `<div>` und `<table><pre><p>` vom umgebenden Inhalt zu trennen. Versuchen Sie, die Tags nicht mit Tabulatoren oder Leerzeichen einzurücken – das kann die Formatierung beeinträchtigen.

Sie können keine Markdown-Syntax innerhalb von HTML-Tags der Blockebene verwenden. Zum Beispiel funktioniert `<p>italic and **bold**</p>` nicht.
## Emojis

[Emojis für Markdown](https://gist.github.com/rxaviers/7360908)

### Personen

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

### Natur

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

### Objekte

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

### Orte

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

### Symbole

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

## Referenzen

- https://www.markdownguide.org/basic-syntax/

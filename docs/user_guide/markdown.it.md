# Markdown - Sintassi di base

---

_basato su https://www.markdownguide.org/basic-syntax/_

---

## Panoramica
Quasi tutte le applicazioni Markdown supportano la sintassi di base descritta nel documento di progettazione originale di Markdown. Esistono piccole variazioni e discrepanze tra i processori Markdown – sono annotate in linea quando possibile.

## Titoli

Per creare un titolo, aggiungi segni di cancelletto (`#`) prima di una parola o frase.
Il numero di segni di cancelletto che usi deve corrispondere al livello del titolo.
Ad esempio, per creare un titolo di livello tre (`<h3>`), usa tre segni di cancelletto (ad esempio, `### My Header`).

| Markup              | HTML                       | Output renderizzato      |
|---------------------|----------------------------|--------------------------|
| `# Heading level 1` | `<h1>Heading level 1</h1>` | <h1>Heading level 1</h1> |
| `# Heading level 2` | `<h2>Heading level 2</h2>` | <h1>Heading level 1</h1> |
| `# Heading level 3` | `<h3>Heading level 3</h3>` | <h3>Heading level 3</h3> |
| `# Heading level 4` | `<h4>Heading level 4</h4>` | <h4>Heading level 4</h4> |
| `# Heading level 5` | `<h5>Heading level 5</h5>` | <h5>Heading level 5</h5> |
| `# Heading level 6` | `<h6>Heading level 6</h6>` | <h6>Heading level 6</h6> |

## Sintassi alternativa
Come alternativa, nella riga sotto il testo, aggiungi un numero qualsiasi di caratteri `==` per il livello di titolo 1 oppure caratteri `--` per il livello di titolo 2.

| Markup                                                                      | HTML                       | Output renderizzato      |
|-----------------------------------------------------------------------------|----------------------------|--------------------------|
| <code class="highlighter-rouge">Heading level 1<br>===============</code> | `<h1>Heading level 1</h1>` | <h1>Heading level 1</h1> |
| <code class="highlighter-rouge">Heading level 2<br>---------------</code> | `<h2>Heading level 2</h2>` | <h2>Heading level 2</h2> |

## Titoli: buone pratiche
Le applicazioni Markdown non concordano su come gestire la mancanza di spazio tra i segni di cancelletto (`#`) e il nome del titolo. Per compatibilità, inserisci sempre uno spazio tra i segni di cancelletto e il nome del titolo.

| ✅&nbsp; Fai così     | ❌&nbsp; Non fare così |
|:---------------------:|:----------------------:|
| `# Here's a Heading` | `#Here's a Heading`    |

Devi inoltre inserire righe vuote prima e dopo un titolo per compatibilità.

| ✅ Fai così                                                                                    | ❌ Non così                                                                                         |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| <code>Try to put a blank line before...<br><br># Heading<br><br>...and after a heading.</code> | <code>Without blank lines, this might not look right.<br># Heading<br>        Don't do this!</code> |

## Paragrafi

Per creare paragrafi, usa una riga vuota per separare una o più righe di testo.

| Markup                                    | HTML                                      | Output renderizzato                    |
|-------------------------------------------|-------------------------------------------|----------------------------------------|
| <code>Paragrafo1.<br><br>Paragrafo2.</code> | `<p>Paragrafo1.</p><p>Paragrafo2.</p>`    | <code>Paragrafo1.<br>Paragrafo2.</code> |

## Buone pratiche per i paragrafi

A meno che il [paragrafo non sia in un elenco](#aggiungere-elementi-agli-elenchi), non indentare i paragrafi con spazi o tabulazioni.

> ℹ **Nota:** Se hai bisogno di indentare i paragrafi nell'output, consulta la sezione su come indentare (tabulazione).

| ✅&nbsp; Fai così                             | ❌&nbsp; Non fare così                                   |
| -------------------------------------------- | -------------------------------------------------------- |
| Non inserire tabulazioni o spazi prima dei paragrafi. | Questo può causare problemi di formattazione imprevisti. |
| Mantieni le righe allineate a sinistra così.  | Non aggiungere tabulazioni o spazi prima dei paragrafi.  |

## Interruzioni di riga

Per creare un'interruzione di riga o una nuova riga (`<br>`), termina una riga con due o più spazi e premi invio.

| Markup                      | HTML                             | Output renderizzato         |
| --------------------------- | -------------------------------- | --------------------------- |
| Questa è la prima riga.     | <p>Questa è la prima riga.<br>   | Questa è la prima riga.     |
| E questa è la seconda riga. | E questa è la seconda riga.</p>  | E questa è la seconda riga. |

### Pratiche consigliate per l'interruzione di riga
<!-- TODO: line-break-best-practices -->

Puoi usare due o più spazi (comunemente chiamati "spazi finali") per le interruzioni di riga in quasi tutte le applicazioni Markdown, ma la questione è controversa. È difficile vedere gli spazi finali in un editor e molte persone inseriscono per errore o intenzionalmente due spazi dopo ogni frase. Per questo motivo, potresti preferire usare qualcosa di diverso dagli spazi finali per le interruzioni di riga. Se la tua applicazione [Markdown supporta HTML](#html), puoi usare il tag HTML `<br>`.

Per compatibilità, usa lo spazio finale o il tag HTML `<br>` alla fine della riga.

Esistono altre due opzioni che non consiglio. CommonMark e alcuni altri linguaggi di markup leggero consentono di digitare una barra rovesciata (`\`) alla fine della riga, ma non tutte le applicazioni Markdown la supportano, quindi non è la scelta migliore dal punto di vista della compatibilità. In almeno alcuni linguaggi di markup leggero non è richiesto nulla alla fine della riga – basta premere invio e verrà creata un'interruzione di riga.

| ✅&nbsp; Fai così                          | ❌&nbsp; Non fare così                             |
| ------------------------------------------ | -------------------------------------------------- |
| Prima riga con due spazi alla fine.        | Prima riga con una barra rovesciata alla fine.\    |
| E la riga successiva.                      | E la riga successiva.                              |
| Prima riga con il tag HTML alla fine.<br>  | Prima riga senza nulla alla fine.                  |
| E la riga successiva.                      | E la riga successiva.                              |

## Enfasi

Puoi aggiungere enfasi mettendo il testo in grassetto o corsivo.

### Grassetto

Per il testo in grassetto, aggiungi due asterischi o trattini bassi prima e dopo una parola o frase. Per mettere in grassetto la parte centrale di una parola per enfatizzarla, aggiungi due asterischi senza spazi intorno alle lettere.

| Markup                        | HTML                                       | Output renderizzato          |
| ----------------------------- | ------------------------------------------ | ---------------------------- |
| Amo `**testo in grassetto**`. | Adoro <strong>testo in grassetto</strong>. | Amo **testo in grassetto** . |
| Amo `__testo in grassetto__`. | Adoro <strong>testo in grassetto</strong>. | Amo __testo in grassetto__ . |
| L'amore `**è**` grassetto     | L'amore<strong>è</strong>grassetto         | L'amore **è** grassetto      |

#### Buone pratiche per il grassetto

Le applicazioni Markdown non concordano su come gestire i trattini bassi al centro di una parola. Per compatibilità, usa gli asterischi per il grassetto al centro di una parola per enfatizzarla.

| ✅&nbsp; Fai così         | ❌&nbsp; Non fare così  |
| ------------------------- | ----------------------- |
| L'amore `**è**` grassetto | L'amore`__è__`grassetto |

### Corsivo

Per mettere il testo in corsivo, aggiungi un asterisco o un trattino basso prima e dopo una parola o frase. Per mettere in corsivo la parte centrale di una parola per enfatizzarla, aggiungi un asterisco senza spazi intorno alle lettere.

| Markup                                           | HTML                                                 | Output renderizzato                             |
| ------------------------------------------------ | ---------------------------------------------------- | ----------------------------------------------- |
| Il testo in corsivo è il `*miagolio del gatto*`.  | Il testo in corsivo è il <em>miagolio del gatto</em>. | Il testo in corsivo è il *miagolio del gatto* . |
| Il testo in corsivo è il `_miagolio del gatto_`.  | Il testo in corsivo è il <em>miagolio del gatto</em>. | Il testo in corsivo è il _miagolio del gatto_ . |
| Un `*gatto*` miao                                | Un <em>gatto</em>> miao                              | Un *gatto* miao                                 |

#### Buone pratiche per il corsivo
<!-- TODO: italic-best-practices -->

Le applicazioni Markdown non concordano su come gestire i trattini bassi al centro di una parola. Per compatibilità, usa gli asterischi per mettere in corsivo la parte centrale di una parola per enfatizzarla.

| ✅&nbsp; Fai così       | ❌&nbsp; Non fare così |
| ----------------------- | ---------------------- |
| Un `*gatto*` miao       | Un`_gatto_`miao        |

### Grassetto e corsivo
<!-- TODO: bold-and-italic -->

Per enfatizzare il testo con grassetto e corsivo contemporaneamente, aggiungi tre asterischi o trattini bassi prima e dopo una parola o frase. Per mettere in grassetto e corsivo la parte centrale di una parola per enfatizzarla, aggiungi tre asterischi senza spazi intorno alle lettere.

| Markup                                           | HTML                                                                | Output renderizzato                         |
| ------------------------------------------------ | ------------------------------------------------------------------- | ------------------------------------------- |
| Questo testo è `***veramente importante***`.      | Questo testo è `<em><strong>veramente importante</strong></em>`.   | Questo testo è ***veramente importante***.  |
| Questo testo è `___veramente importante___`.      | Questo testo è `<em><strong>veramente importante</strong></em>`.   | Questo testo è ___veramente importante___.  |
| Questo testo è `__*veramente importante*__`.      | Questo testo è `<em><strong>veramente importante</strong></em>`.   | Questo testo è __*veramente importante*__.  |
| Questo testo è `**_veramente importante**_`.      | Questo testo è `<em><strong>veramente importante</strong></em>`.   | Questo testo è **_veramente importante**_.  |
| Questo testo è davvero `***molto***` importante.  | Questo testo è davvero `<em><strong>molto importante</strong></em>`. | Questo testo è davvero ***molto*** importante. |

> ℹ **Osservazione:** l'ordine dei tag `em` e `strong` può essere invertito a seconda del processore Markdown in uso.

#### Pratiche consigliate per grassetto e corsivo
<!-- TODO: bold-and-italic-best-practices -->

Le applicazioni Markdown non concordano su come gestire i trattini bassi al centro di una parola. Per compatibilità, usa gli asterischi per grassetto e corsivo al centro di una parola per enfatizzarla.

| ✅&nbsp; Fai così                                | ❌&nbsp; Non fare così                        |
| ------------------------------------------------ | --------------------------------------------- |
| Questo testo è davvero `***molto***` importante. | Questo testo è davvero`___molto___`importante. |

## Citazioni in blocco

Per creare una citazione in blocco, aggiungi un `>` prima di un paragrafo.

    > Dorothy followed her through many of the beautiful rooms in her castle.

L'output renderizzato è il seguente:

> Dorothy la seguì attraverso molte delle belle stanze del suo castello.

### Citazioni in blocco con più paragrafi
<!-- TODO: blockquotes-with-multiple-paragraphs -->

Le citazioni in blocco possono contenere più paragrafi. Aggiungi un `>` nelle righe vuote tra i paragrafi.

    > Dorothy la seguì attraverso molte delle belle stanze del suo castello.

    >

    > La Strega le ordinò di pulire le pentole e i bollitori, di spazzare il pavimento e di mantenere il fuoco alimentato con legna.

L'output renderizzato è il seguente:

> Dorothy la seguì attraverso molte delle belle stanze del suo castello.
>
> La Strega le ordinò di pulire le pentole e i bollitori, di spazzare il pavimento e di mantenere il fuoco alimentato con legna.

### Citazioni annidate
<!-- TODO: nested-blockquotes -->

Le citazioni in blocco possono essere annidate. Aggiungi un `>>` prima del paragrafo che vuoi annidare.

    > Dorothy la seguì attraverso molte delle belle stanze del suo castello.

    >

    >> La Strega le ordinò di pulire le pentole e i bollitori, di spazzare il pavimento e di mantenere il fuoco alimentato con legna.

L'output renderizzato è il seguente:

> Dorothy la seguì attraverso molte delle belle stanze del suo castello.
>
>> La Strega le ordinò di pulire le pentole e i bollitori, di spazzare il pavimento e di mantenere il fuoco alimentato con legna.

### Blockquote con altri elementi
<!-- TODO: blockquotes-with-other-elements -->

I blockquote possono contenere altri elementi formattati in Markdown. Non tutti gli elementi possono essere usati: dovrai sperimentare per vedere quali funzionano.

    > #### I risultati trimestrali sembrano ottimi!

    >

    > - I ricavi sono stati fuori scala.

    > - I profitti sono stati più alti che mai.

    >

    > *Tutto* sta procedendo secondo **piano** .

L'output renderizzato è il seguente:

> #### I risultati trimestrali sembrano ottimi!
>
> - I ricavi sono stati fuori scala.
> - I profitti sono stati più alti che mai.
>
> *Tutto* sta procedendo secondo **piano**.

### Pratiche consigliate per le citazioni in blocco
<!-- TODO: blockquotes-best-practices -->

Per compatibilità, inserisci righe vuote prima e dopo le citazioni.

| ✅&nbsp; Fai così                        | ❌&nbsp; Non fare così                          |
| ---------------------------------------- | ----------------------------------------------- |
| Prova a inserire una riga vuota prima... | Senza righe vuote, potrebbe non sembrare corretto.\ |
|                                          | > Questa è una citazione in blocco\             |
| > Questa è una citazione in blocco        | Non fare così!\                                 |
| ...e dopo una citazione in blocco.       |                                                 |

## Elenchi

Puoi organizzare gli elementi in elenchi ordinati e non ordinati.

### Elenchi ordinati
<!-- TODO: ordered-lists -->

Per creare un elenco ordinato, aggiungi voci di riga con numeri seguiti da punti. I numeri non devono essere in ordine numerico, ma l'elenco deve iniziare con il numero uno.

| Markup                                                                  | HTML                                                                                                 | Output renderizzato                     |
| ----------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | --------------------------------------- |
| 1. Primo elemento <br> 2. Secondo elemento <br> 3. Terzo elemento <br> 4. Quarto elemento | `<ol>`<br>ㅤ`<li>Primo elemento</li>`<br>ㅤ`<li>Secondo elemento</li>`<br>ㅤ`<li>Terzo elemento</li>`<br>ㅤ`<li>Quarto elemento</li>`<br>`</ol>` | 1. Primo elemento <br> 2. Secondo elemento <br> 3. Terzo elemento <br> 4. Quarto elemento |
| 1. Primo elemento <br> 1. Secondo elemento <br> 1. Terzo elemento <br> 1. Quarto elemento | `<ol>`<br>ㅤ`<li>Primo elemento</li>`<br>ㅤ`<li>Secondo elemento</li>`<br>ㅤ`<li>Terzo elemento</li>`<br>ㅤ`<li>Quarto elemento</li>`<br>`</ol>` | 1. Primo elemento <br> 2. Secondo elemento <br> 3. Terzo elemento <br> 4. Quarto elemento |
| 1. Primo elemento <br> 8. Secondo elemento <br> 3. Terzo elemento <br> 5. Quarto elemento | `<ol>`<br>ㅤ`<li>Primo elemento</li>`<br>ㅤ`<li>Secondo elemento</li>`<br>ㅤ`<li>Terzo elemento</li>`<br>ㅤ`<li>Quarto elemento</li>`<br>`</ol>` | 1. Primo elemento <br> 2. Secondo elemento <br> 3. Terzo elemento <br> 4. Quarto elemento |
| 1. Primo elemento <br> 2. Secondo elemento <br> 3. Terzo elemento <br>ㅤㅤ1. Elemento indentato <br>ㅤㅤ2. Elemento indentato <br> 4. Quarto elemento | `<ol>`<br>ㅤ`<li>Primo elemento</li>`<br>ㅤ`<li>Secondo elemento</li>`<br>ㅤ`<li>Terzo elemento</li>`<br>ㅤ`<li>Quarto elemento</li>`<br>`</ol>` | 1. Primo elemento <br> 2. Secondo elemento <br> 3. Terzo elemento <br>ㅤㅤ1. Elemento indentato <br>ㅤㅤ2. Elemento indentato <br> 4. Quarto elemento |

#### Buone pratiche per gli elenchi ordinati
<!-- TODO: ordered-list-best-practices -->

CommonMark e alcuni altri linguaggi di markup leggero consentono di usare le parentesi `( ))` come delimitatore (ad esempio, 1) _Primo elemento_), ma non tutte le applicazioni Markdown le supportano, quindi non è la scelta migliore dal punto di vista della compatibilità. Per compatibilità, usa solo i punti.

| ✅&nbsp; Fai così | ❌&nbsp; Non fare così |
| ----------------- | ---------------------- |
|1. First item<br>  |1) First item<br>       |
|2. Second item     |2) Second item          |

### Elenchi non ordinati
<!-- TODO: unordered-lists -->

Per creare un elenco non ordinato, aggiungi trattini ( `-` ), asterischi ( `*` ) o segni di più ( `+` ) davanti alle voci di riga. Indenta una o più voci per creare un elenco annidato.

| Markup                                                                  | HTML                                                                                                 | Output renderizzato                     |
| ----------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | --------------------------------------- |
| - Primo elemento <br> - Secondo elemento <br> - Terzo elemento <br> - Quarto elemento | `<ul>`<br>ㅤ`<li>Primo elemento</li>`<br>ㅤ`<li>Secondo elemento</li>`<br>ㅤ`<li>Terzo elemento</li>`<br>ㅤ`<li>Quarto elemento</li>`<br>`</ul>` | • Primo elemento <br> • Secondo elemento <br> • Terzo elemento <br> • Quarto elemento |
| * Primo elemento <br> * Secondo elemento <br> * Terzo elemento <br> * Quarto elemento | `<ul>`<br>ㅤ`<li>Primo elemento</li>`<br>ㅤ`<li>Secondo elemento</li>`<br>ㅤ`<li>Terzo elemento</li>`<br>ㅤ`<li>Quarto elemento</li>`<br>`</ul>` | • Primo elemento <br> • Secondo elemento <br> • Terzo elemento <br> • Quarto elemento |
| + Primo elemento <br> + Secondo elemento <br> + Terzo elemento <br> + Quarto elemento | `<ul>`<br>ㅤ`<li>Primo elemento</li>`<br>ㅤ`<li>Secondo elemento</li>`<br>ㅤ`<li>Terzo elemento</li>`<br>ㅤ`<li>Quarto elemento</li>`<br>`</ul>` | • Primo elemento <br> • Secondo elemento <br> • Terzo elemento <br> • Quarto elemento |
| - Primo elemento <br> - Secondo elemento <br> - Terzo elemento <br>ㅤㅤ- Elemento indentato <br>ㅤㅤ- Elemento indentato <br> - Quarto elemento | `<ul>`<br>ㅤ`<li>Primo elemento</li>`<br>ㅤ`<li>Secondo elemento</li>`<br>ㅤ`<li>Terzo elemento</li>`<br>ㅤ`<li>Quarto elemento</li>`<br>`</ul>` | • Primo elemento <br> • Secondo elemento <br> • Terzo elemento <br>ㅤㅤ◦ Elemento indentato <br>ㅤㅤ◦ Elemento indentato <br> • Quarto elemento |

#### Iniziare voci di elenco non ordinato con i numeri
<!-- TODO: starting-unordered-list-items-with-numbers -->

Se devi iniziare una voce di elenco non ordinato con un numero seguito da un punto, puoi usare una barra rovesciata ( `/` ) per [escapare](#caratteri-di-escape) del punto.

| Markup                                                      | HTML                                         | Output renderizzato                    |
| ----------------------------------------------------------- | -------------------------------------------- | -------------------------------------- |
| - 1968\. Un anno fantastico!<br>- Penso che 1969 sia stato il secondo migliore. |`<ul>`<br>ㅤ`<li>1968. Un anno fantastico!</li>`<br>`<li>Penso che 1969 sia stato il secondo migliore.</li>`<br>`</ul>` |• 1968. Un anno fantastico!<br>• Penso che 1969 sia stato il secondo migliore.|

#### Pratiche consigliate per gli elenchi non ordinati
<!-- TODO: unordered-list-best-practices -->

Le applicazioni Markdown non concordano su come gestire delimitatori diversi nello stesso elenco. Per compatibilità, non mischiare i delimitatori nello stesso elenco `–` scegline uno e mantienilo.

| ✅&nbsp; Fai così                                                       | ❌&nbsp; Non fare così |
| ---------------------------------------------------------------------- | ---------------------- |
| - Primo elemento<br>- Secondo elemento<br>- Terzo elemento<br>- Quarto elemento | + Primo elemento<br>* Secondo elemento<br>- Terzo elemento<br>+ Quarto elemento|

### Aggiungere elementi agli elenchi
<!-- TODO: adding-elements-in-lists -->

Per aggiungere un altro elemento a un elenco preservando la continuità dell'elenco, indenta l'elemento con quattro spazi o una tabulazione, come mostrato negli esempi seguenti.

> ℹ **Suggerimento:** Se gli elementi non appaiono nel modo previsto, verifica di nuovo di aver indentato gli elementi dell'elenco con quattro spazi o una tabulazione.

#### Paragrafi

    * Questo è il primo elemento dell'elenco.
    * Ecco il secondo elemento dell'elenco.

        Devo aggiungere un altro paragrafo sotto il secondo elemento dell'elenco.

    * Ecco il terzo elemento dell'elenco.

L'output renderizzato è il seguente:

* Questo è il primo elemento dell'elenco.
* Ecco il secondo elemento dell'elenco.

    Devo aggiungere un altro paragrafo sotto il secondo elemento dell'elenco.

* Ecco il terzo elemento dell'elenco.

#### Citazioni in blocco
<!-- TODO: blockquotes -->

    * Questo è il primo elemento dell'elenco.
    * Ecco il secondo elemento dell'elenco.

        > Una citazione in blocco starebbe bene sotto il secondo elemento dell'elenco.

    * Ecco il terzo elemento dell'elenco

L'output renderizzato è il seguente:

* Questo è il primo elemento dell'elenco.
* Ecco il secondo elemento dell'elenco.
    > Una citazione in blocco starebbe bene sotto il secondo elemento dell'elenco.
* Ecco il terzo elemento dell'elenco

#### Blocchi di codice
<!-- TODO: code-blocks-1 -->

[I blocchi di codice](#blocchi-di-codice) sono normalmente indentati con quattro spazi o una tabulazione. Quando si trovano in un elenco, indentali con otto spazi o due tabulazioni.

    1. Apri il file.
    2. Trova il seguente blocco di codice alla riga 21:

        <html>
          <head>
            <title>Test</title>
          </head>

    3. Aggiorna il titolo per corrispondere al nome del tuo sito.

L'output renderizzato è il seguente:

1. Apri il file.
2. Trova il seguente blocco di codice alla riga 21:

        <html>
          <head>
            <title>Test</title>
          </head>

3. Aggiorna il titolo per corrispondere al nome del tuo sito.

#### Immagini
<!-- TODO: images -->

    1. Apri il file che contiene la mascotte di Linux.
    2. Meravigliati della sua bellezza.

        ![Tux, the Linux mascot](https://mdg.imgix.net/assets/images/tux.png?auto=format&fit=clip&q=40&w=100)

    3. Chiudi il file.

L'output renderizzato è il seguente:

1. Apri il file che contiene la mascotte di Linux.
2. Meravigliati della sua bellezza.

    ![Tux, the Linux mascot](https://mdg.imgix.net/assets/images/tux.png?auto=format&fit=clip&q=40&w=100)

3. Chiudi il file.

#### Elenchi
<!-- TODO: lists -->

Puoi annidare un elenco non ordinato in un elenco ordinato o viceversa.

    1. Primo elemento
    2. Secondo elemento
    3. Terzo elemento
          - Elemento indentato
          - Elemento indentato
    4. Quarto elemento

L'output renderizzato è il seguente:

1. Primo elemento
2. Secondo elemento
3. Terzo elemento
      - Elemento indentato
      - Elemento indentato
4. Quarto elemento

## Codice

Per denotare una parola o una frase come codice, racchiudila tra backtick ( ` ).

|Markup                              |HTML                                                  |Output renderizzato                       |
| -------------------------------------- | ---------------------------------------------------- |--------------------------------------- |
|``Nel prompt dei comandi, digita `Nano`.``| Nel prompt dei comandi, digita <code>Nano</code>.      |Nel prompt dei comandi, digita `nano`.    |

### Escaping dei backtick
<!-- TODO: escaping-backticks -->

Se la parola o la frase che vuoi denotare come codice include uno o più backtick, puoi eseguirne l'escape racchiudendo la parola o la frase tra backtick doppi `( `` )`.

|Markup                             |HTML                                              |Output renderizzato           |
| ------------------------------------- | ------------------------------------------------ | -------------------------  |
|``Usa `code` nel tuo file Markdown.``| <code>Usa `code` nel tuo file Markdown.</code> |Use ´code´ in your Markdown file.|

### Blocchi di codice
<!-- TODO: code-blocks -->

Per creare blocchi di codice, indenta ogni riga del blocco con almeno quattro spazi o una tabulazione.

    <html>
      <head>
      </head>
    </html>

L'output renderizzato è il seguente:

    <html>
      <head>
      </head>
    </html>

> ℹ **Nota:** Per creare blocchi di codice senza indentare le righe, usa i [blocchi di codice delimitati](https://www.markdownguide.org/extended-syntax/#fenced-code-blocks).

## Linee orizzontali

Per creare una linea orizzontale, usa tre o più asterischi ( `***` ), trattini ( `---` ) o trattini bassi ( `___` ) su una riga da soli.

    ***
    ---
    ______________
L'output renderizzato dei tre sembra identico:

_____________________________________________________

### Pratiche consigliate per le linee orizzontali
<!-- TODO: horizontal-rule-best-practices -->

Per compatibilità, inserisci righe vuote prima e dopo le linee orizzontali.

| ✅&nbsp; Fai così                                                                      | ❌&nbsp; Non fare così |
|----------------------------------------------------------------------------------------- |------------------------|
|Prova a inserire una riga vuota prima...<br><br>---<br><br>...e dopo una linea orizzontale. |Senza righe vuote, questo sarebbe un titolo.<br>---<br>Non fare così!|

## Collegamenti

Per creare un collegamento, inserisci il testo del collegamento tra parentesi quadre (ad esempio, `[Duck Duck Go]`) e seguilo immediatamente con l'URL tra parentesi tonde (ad esempio, `(https://duckduckgo.com)`).

    My favorite search engine is [Duck Duck Go](https://duckduckgo.com).


L'output renderizzato è il seguente:

Il mio motore di ricerca preferito è [Duck Duck Go](https://duckduckgo.com).

> ℹ **Nota:** Per collegarti a un elemento nella stessa pagina, consulta [collegamento agli ID dei titoli](https://www.markdownguide.org/extended-syntax/#linking-to-heading-ids). Per creare un collegamento che si apre in una nuova scheda o finestra, consulta la sezione sui [destini dei collegamenti](https://www.markdownguide.org/hacks/#link-targets).

### Aggiungere titoli
<!-- TODO: adding-titles -->

Facoltativamente, puoi aggiungere un titolo a un collegamento. Questo apparirà come un suggerimento quando l'utente passa il mouse sul collegamento. Per aggiungere un titolo, inseriscilo tra virgolette dopo l'URL.

    My favorite search engine is [Duck Duck Go](https://duckduckgo.com "The best search engine for privacy").

L'output renderizzato è il seguente:

Il mio motore di ricerca preferito è [Duck Duck Go](https://duckduckgo.com).

### URL e indirizzi e-mail
<!-- TODO: urls-and-email-addresses -->

Per trasformare rapidamente un URL o un indirizzo e-mail in un collegamento, inseriscilo tra parentesi angolari.

    <https://www.markdownguide.org>
    <fake@example.com>

L'output renderizzato è il seguente:

 <https://www.markdownguide.org>

 <fake@example.com>

### Formattare i collegamenti
<!-- TODO: formatting-links -->

Per [enfatizzare](#enfasi) i collegamenti, aggiungi asterischi prima e dopo le parentesi quadre e tonde. Per denotare i collegamenti come [codice](#codice), aggiungi backtick tra le parentesi quadre.

    Adoro sostenere la **[EFF](https://eff.org)**.

    Questo è il *[Markdown Guide](https://www.markdownguide.org)*.

    Consulta la sezione su [`code`](#codice).

L'output renderizzato è il seguente:

Adoro sostenere la **[EFF](https://eff.org)**.

Questo è il *[Markdown Guide](https://www.markdownguide.org)*.

Consulta la sezione su [`code`](#codice).

### Collegamenti in stile di riferimento
<!-- TODO: reference-style-links -->

I collegamenti in stile di riferimento sono un tipo speciale di collegamento che rende gli URL più facili da visualizzare e leggere in Markdown. I collegamenti in stile di riferimento sono costruiti in due parti: la parte che mantieni allineata al tuo testo e la parte che archivia altrove nel file per mantenere il testo facile da leggere.

#### Formattare la prima parte del collegamento
<!-- TODO: formatting-the-first-part-of-the-link -->

La prima parte di un collegamento in stile di riferimento è formattata con due coppie di parentesi quadre. La prima coppia di parentesi quadre racchiude il testo che deve apparire collegato. La seconda coppia di parentesi quadre mostra un'etichetta usata per puntare al collegamento che archivia altrove nel documento.

Anche se non è obbligatorio, puoi includere uno spazio tra la prima e la seconda coppia di parentesi quadre. L'etichetta nella seconda coppia di parentesi quadre non distingue maiuscole da minuscole e può includere lettere, numeri, spazi o punteggiatura.

Ciò significa che i seguenti formati di esempio sono approssimativamente equivalenti per la prima parte del collegamento:

* [hobbit-hole][1]
* [hobbit-hole][1]

#### Formattare la seconda parte del collegamento
<!-- TODO: formatting-the-second-part-of-the-link -->

La seconda parte di un collegamento in stile di riferimento è formattata con i seguenti attributi:

    1. L'etichetta, tra parentesi quadre, seguita immediatamente da due punti e da almeno uno spazio (ad esempio, [label]: ).
    2. L'URL del collegamento, che puoi inserire facoltativamente tra parentesi angolari.
    3. Il titolo facoltativo del collegamento, che puoi inserire tra virgolette doppie, virgolette singole o parentesi tonde.

Ciò significa che i formati di esempio seguenti sono approssimativamente equivalenti per la seconda parte del collegamento:

    * [1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle
    * [1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle "Hobbit lifestyles"
    * [1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle 'Hobbit lifestyles'
    * [1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle (Hobbit lifestyles)
    * [1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle "Hobbit lifestyles"
    * [1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle 'Hobbit lifestyles'
    * [1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle (Hobbit lifestyles)

Puoi inserire questa seconda parte del collegamento in qualsiasi punto del tuo documento Markdown. Alcune persone la inseriscono subito dopo il paragrafo in cui appare, mentre altre la inseriscono alla fine del documento (come note finali o a piè di pagina).

#### Un esempio che unisce le parti
<!-- TODO: an-example-putting-the-parts-together -->

Diciamo che aggiungi un URL come [collegamento URL standard](#collegamenti) a un paragrafo e che nel Markdown risulta così:

    In una buca nel terreno viveva un hobbit. Non una buca sporca, sudicia e bagnata, piena di code di vermi e con odore di fango, né una buca secca, vuota e sabbiosa, senza nulla su cui sedersi o da mangiare: era una [tana di hobbit](https://en.wikipedia.org/wiki/Hobbit#Lifestyle "Hobbit lifestyles"), e ciò significa comfort.

Anche se può puntare a informazioni aggiuntive interessanti, l'URL visualizzato non aggiunge davvero molto al testo esistente, se non renderlo più difficile da leggere. Per correggere ciò, puoi formattare l'URL così:

    In una buca nel terreno viveva un hobbit. Non una buca sporca, sudicia e umida, piena di code di lombrichi e con odore di fango, né una buca secca, vuota e sabbiosa, senza nulla su cui sedersi o mangiare: era una [tana di hobbit](https://en.wikipedia.org/wiki/Hobbit#Lifestyle), e ciò significa comfort.

In entrambi i casi precedenti, l'output renderizzato sarebbe identico:

>
> In una buca nel terreno viveva un hobbit. Non una buca sporca, sudicia e umida, piena di code di lombrichi e con odore di fango, né una buca secca, vuota e sabbiosa, senza nulla su cui sedersi o mangiare: era una [tana di hobbit](https://en.wikipedia.org/wiki/Hobbit#Lifestyle), e ciò significa comfort.
>

e l'HTML del collegamento sarebbe:

    <a href="https://en.wikipedia.org/wiki/Hobbit#Lifestyle title="Hobbit lifestyles">hobbit-hole</a>

### Pratiche consigliate per i collegamenti
<!-- TODO: link-best-practices -->

Le applicazioni Markdown non concordano su come gestire gli spazi in mezzo a un URL. Per compatibilità, prova a codificare in URL eventuali spazi con %20. In alternativa, se la tua applicazione Markdown [supporta HTML](#html), puoi usare il tag HTML.

| ✅&nbsp; Fai così                                       | ❌&nbsp; Non fare così                               |
| -------------------------------------------------------- | ------------------------------------------------------|
|`[link](https://www.example.com/my%20great%20page)`<br><br>`<a href="https://www.example.com/my great page">link</a>`|`[link](https://www.example.com/my great page)`<br><br>|

Anche le parentesi in mezzo a un URL possono essere problematiche. Per compatibilità, prova a codificare in URL la parentesi aperta `(()` con %28 e la parentesi chiusa `( ))` con %29. In alternativa, se la tua applicazione Markdown [supporta HTML](#html) , puoi usare il tag HTML.

| ✅&nbsp; Fai così                                       | ❌&nbsp; Non fare così                               |
| -------------------------------------------------------- | ------------------------------------------------------|
|`[a novel](https://en.wikipedia.org/wiki/The_Milagro_Beanfield_War_%28novel%29)`<br><br>`<a href="https://en.wikipedia.org/wiki/The_Milagro_Beanfield_War_(novel)">a novel</a>`|`[a novel](https://en.wikipedia.org/wiki/The_Milagro_Beanfield_War_(novel))`|

## Immagini

Per aggiungere un'immagine, aggiungi un punto esclamativo ( `!` ), seguito da un testo alternativo tra parentesi quadre e dal percorso o URL della risorsa immagine tra parentesi tonde. Facoltativamente, puoi aggiungere un titolo tra virgolette dopo il percorso o l'URL.

    ![The San Juan Mountains are beautiful!](/assets/images/san-juan-mountains.jpg "San Juan Mountains")

L'output renderizzato è il seguente:

![The San Juan Mountains are beautiful!](https://mdg.imgix.net/assets/images/san-juan-mountains.jpg?auto=format&fit=clip&q=40&w=800 "San Juan Mountains")

> ℹ **Nota:** Per ridimensionare un'immagine, consulta la sezione su [dimensioni delle immagini](https://www.markdownguide.org/hacks/#image-size). Per aggiungere una didascalia, consulta la sezione sulle [didascalie delle immagini](https://www.markdownguide.org/hacks/#image-captions).

### Collegare le immagini
<!-- TODO: linking-images -->

Per aggiungere un collegamento a un'immagine, inserisci il Markdown dell'immagine tra parentesi quadre e aggiungi il collegamento tra parentesi tonde.

    [![An old rock in the desert](/assets/images/shiprock.jpg "Shiprock, New Mexico by Beau Rogers")](https://www.flickr.com/photos/beaurogers/31833779864/in/photolist-Qv3rFw-34mt9F-a9Cmfy-5Ha3Zi-9msKdv-o3hgjr-hWpUte-4WMsJ1-KUQ8N-deshUb-vssBD-6CQci6-8AFCiD-zsJWT-nNfsgB-dPDwZJ-bn9JGn-5HtSXY-6CUhAL-a4UTXB-ugPum-KUPSo-fBLNm-6CUmpy-4WMsc9-8a7D3T-83KJev-6CQ2bK-nNusHJ-a78rQH-nw3NvT-7aq2qf-8wwBso-3nNceh-ugSKP-4mh4kh-bbeeqH-a7biME-q3PtTf-brFpgb-cg38zw-bXMZc-nJPELD-f58Lmo-bXMYG-bz8AAi-bxNtNT-bXMYi-bXMY6-bXMYv)


L'output renderizzato è il seguente:

[![An old rock in the desert](https://mdg.imgix.net/assets/images/shiprock.jpg?auto=format&fit=clip&q=40&w=800 "Shiprock, New Mexico by Beau Rogers")](https://www.flickr.com/photos/beaurogers/31833779864/in/photolist-Qv3rFw-34mt9F-a9Cmfy-5Ha3Zi-9msKdv-o3hgjr-hWpUte-4WMsJ1-KUQ8N-deshUb-vssBD-6CQci6-8AFCiD-zsJWT-nNfsgB-dPDwZJ-bn9JGn-5HtSXY-6CUhAL-a4UTXB-ugPum-KUPSo-fBLNm-6CUmpy-4WMsc9-8a7D3T-83KJev-6CQ2bK-nNusHJ-a78rQH-nw3NvT-7aq2qf-8wwBso-3nNceh-ugSKP-4mh4kh-bbeeqH-a7biME-q3PtTf-brFpgb-cg38zw-bXMZc-nJPELD-f58Lmo-bXMYG-bz8AAi-bxNtNT-bXMYi-bXMY6-bXMYv)

## Caratteri di escape

Per visualizzare un carattere letterale che altrimenti verrebbe usato per formattare il testo in un documento Markdown, aggiungi una barra rovesciata ( `\` ) davanti al carattere.

    \* Without the backslash, this would be a bullet in an unordered list.

L'output renderizzato è il seguente:

* Senza la barra rovesciata, questo sarebbe un punto elenco in un elenco non ordinato.

### Caratteri che puoi eseguirne l'escape
<!-- TODO: characters-you-can-escape -->

Puoi usare una barra rovesciata per eseguire l'escape dei seguenti caratteri.

|Caratteri   |Nome                                                                            |
| ----------- | ------------------------------------------------------------------------------ |
|\            |barra rovesciata                                                                 |
|`            |backtick (vedi anche [escaping dei backtick nel codice](#escaping-dei-backtick)) |
|*            |asterisco                                                                       |
|_            |trattino basso                                                                  |
|{}           |parentesi graffe                                                                 |
|[]           |parentesi quadre                                                                 |
|<>           |parentesi angolari                                                             |
|()           |parentesi tonde                                                                      |
|#            |cancelletto.                                                                      |
|+            |segno più                                                                   |
|-            |segno meno (trattino)                                                          |
|.            |punto                                                                           |
|!            |punto esclamativo                                                             |
|\|            |barra verticale                                                                            |

## HTML

Molte applicazioni Markdown consentono di usare tag HTML nel testo formattato in Markdown. Questo è utile se preferisci alcuni tag HTML alla sintassi Markdown. Ad esempio, alcune persone ritengono più semplice usare i tag HTML per le immagini. Usare HTML è utile anche quando devi modificare gli attributi di un elemento, come specificare il [colore del testo](https://www.markdownguide.org/hacks/#color) o modificare la larghezza di un'immagine.

Per usare HTML, inserisci i tag nel testo del tuo file formattato in Markdown.

    This **word** is bold. This <em>word</em> is italic.

L'output renderizzato è il seguente:

Questa **parola** è in grassetto. Questa *parola* è in corsivo.

### Pratiche consigliate per HTML
<!-- TODO: html-best-practices -->

Per motivi di sicurezza, non tutte le applicazioni Markdown supportano HTML nei documenti Markdown. In caso di dubbio, verifica la documentazione della tua applicazione Markdown. Alcune applicazioni supportano solo un sottoinsieme di tag HTML.

Usa righe vuote per separare gli elementi HTML a livello di blocco, come `<table>`, `<pre>`, `<p>` e `<div>`, dal contenuto circostante. Cerca di non indentare i tag con tabulazioni o spazi — questo può interferire con la formattazione.

Non puoi usare la sintassi Markdown all'interno di tag HTML a livello di blocco. Ad esempio, `<p>italic and **bold**</p>` non funzionerà.

## Emoji

[Emoji per Markdown](https://gist.github.com/rxaviers/7360908)

### Persone
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

### Natura

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

### Oggetti

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

### Luoghi

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

### Simboli

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

## Riferimenti

- https://www.markdownguide.org/basic-syntax/

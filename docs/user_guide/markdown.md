# Markdown - Sintáxe básica

---

_baseado em https://www.markdownguide.org/basic-syntax/_

---

## Visão geral
Quase todos os aplicativos Markdown suportam a sintaxe básica descrita no documento de design original do Markdown. Existem pequenas variações e discrepâncias entre os processadores Markdown – elas são anotadas em linha sempre que possível.

## Títulos

Para criar um título, adicione sinais numéricos (`#`) antes de uma palavra ou frase.
O número de sinais numéricos que você usa deve corresponder ao nível do título.
Por exemplo, para criar um título de nível três (`<h3>`), use três sinais numéricos (por exemplo, `### My Header`).

| Remarcação          | 	HTML                       | Saída renderizada        |
|---------------------|------------------------------|--------------------------|
| `# Heading level 1` | 	`<h1>Heading level 1</h1>` | <h1>Heading level 1</h1> |
| `# Heading level 2` | 	`<h2>Heading level 2</h2>` | <h1>Heading level 1</h1> |
| `# Heading level 3` | 	`<h3>Heading level 3</h3>` | <h3>Heading level 3</h3> |
| `# Heading level 4` | 	`<h4>Heading level 4</h4>` | <h4>Heading level 4</h4> |
| `# Heading level 5` | 	`<h5>Heading level 5</h5>` | <h5>Heading level 5</h5> |
| `# Heading level 6` | 	`<h6>Heading level 6</h6>` | <h6>Heading level 6</h6> |

## Sintaxe Alternativa
Como alternativa, na linha abaixo do texto, adicione qualquer número de `==` caracteres para o nível de título 1 ou `--` caracteres para o nível de título 2.

| Remarcação                                                                | 	HTML                       | Saída renderizada        |
|---------------------------------------------------------------------------|------------------------------|--------------------------|
| <code class="highlighter-rouge">Heading level 1<br>===============</code> | 	`<h1>Heading level 1</h1>` | <h1>Heading level 1</h1> |
| <code class="highlighter-rouge">Heading level 2<br>---------------</code> | 	`<h2>Heading level 2</h2>` | <h2>Heading level 2</h2> |

## Cabeçalho Melhores Práticas
Os aplicativos de markdown não concordam sobre como lidar com a falta de espaço entre os sinais numéricos (`#`) e o nome do título. Para compatibilidade, sempre coloque um espaço entre os sinais numéricos e o nome do título.

|  ✅&nbsp; Faça isso   | ❌&nbsp; Não faça isso |
|:--------------------:|:---------------------:|
| `# Here's a Heading` |  `#Here's a Heading`  |


Você também deve colocar linhas em branco antes e depois de um título para compatibilidade.

| ✅  Faça assim                                                                                  | ❌ Não assim                                                                                         |
|------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| <code>Try to put a blank line before...<br><br># Heading<br><br>...and after a heading.</code> | <code>Without blank lines, this might not look right.<br># Heading<br>        Don't do this!</code> |


## Parágrafos

Para criar parágrafos, use uma linha em branco para separar uma ou mais linhas de texto.

| MarkDown                                    | 	HTML	                                      | Saída renderizada                       |
|---------------------------------------------|---------------------------------------------|-----------------------------------------|
| <code>Paragrafo1.<br><br>Paragrafo2.</code> | `<p>Paragrafo1.</p><p>Paragrafo2.</p>` | <code>Paragrafo1.<br>Paragrafo2.</code> |

## Melhores práticas de parágrafo

A menos que o [parágrafo esteja em uma lista](#adicionando-elementos-em-listas), não recue os parágrafos com espaços ou tabulações.

>  ℹ **Nota:** Se você precisar recuar parágrafos na saída, consulte a seção sobre como recuar (tabulação).

|          ✅&nbsp; Faça isso                                | ❌&nbsp; Não faça isso                                          |
| ---------------------------------------------------------- | ---------------------------------------------------------------- | 
| Não coloque tabulações ou espaços antes dos parágrafos.    | Isso pode resultar em problemas inesperados de formatação.       |
| Mantenha as linhas alinhadas à esquerda assim.             | Não adicione tabulações ou espaços antes dos parágrafos.         |

## Quebras de linha

Para criar uma quebra de linha ou uma nova linha (`<br>`), termine uma linha com dois ou mais espaços e digite return.

| Remarcação                  | HTML                             | Saída renderizada          |
| --------------------------- | ---------------------------------|----------------------------|
| Esta é a primeira linha.    | <p>Esta é a primeira linha.<br>  | Esta é a primeira linha.   |
| E esta é a segunda linha.   | E esta é a segunda linha.</p>    | E esta é a segunda linha.  |

### Práticas recomendadas para quebra de linha
#TODO #line-break-best-practices

Você pode usar dois ou mais espaços (comumente chamados de "espaços em branco finais") para quebras de linha em quase todos os aplicativos Markdown, mas isso é controverso. É difícil ver espaços em branco no final de um editor, e muitas pessoas acidentalmente ou intencionalmente colocam dois espaços após cada frase. Por esse motivo, você pode querer usar algo diferente de espaços em branco à direita para quebras de linha. Se o seu aplicativo [Markdown suportar HTML](#html), você poderá usar a `<br>` tag HTML.

Para compatibilidade, use o espaço em branco final ou a `<br>` tag HTML no final da linha.

Existem duas outras opções que não recomendo usar. CommonMark e algumas outras linguagens de marcação leves permitem digitar uma barra invertida ( `\` ) no final da linha, mas nem todos os aplicativos Markdown suportam isso, portanto, não é uma ótima opção do ponto de vista de compatibilidade. E pelo menos algumas linguagens de marcação leves não exigem nada no final da linha `-` basta digitar return e elas criarão uma quebra de linha.

| ✅&nbsp; Faça isso                       | ❌&nbsp; Não faça isso                         |
| ---------------------------------------- | ----------------------------------------------- |
| First line with two spaces after.        | Primeira linha com uma barra invertida depois.\ | 
| And the next line.                       |E a próxima linha.                               |                  |
| First line with the HTML tag after.<br>  | Primeira linha sem nada depois.                 |
|And the next line.                        |E a próxima linha.                               |                               

## Ênfase

Você pode adicionar ênfase colocando o texto em negrito ou itálico.

### Negrito

Para texto em negrito, adicione dois asteriscos ou sublinhados antes e depois de uma palavra ou frase. Para colocar o meio de uma palavra em negrito para dar ênfase, adicione dois asteriscos sem espaços ao redor das letras.

| Remarcação                     | HTML                                        | Saída renderizada               |
| ------------------------------ | ------------------------------------------- | --------------------------------| 
| Eu amo `**texto em negrito**`. | Eu adoro <strong>texto em negrito</strong>. | Eu adoro **texto em negrito** . |
| Eu amo `__texto em negrito__`. | Eu adoro <strong>texto em negrito</strong>. | Eu adoro __texto em negrito__ . |
| O amor `**é**` negrito         | O amor<strong>é</strong>negrito             | O amor **é** negrito            |

#### Melhores práticas em negrito

Os aplicativos Markdown não concordam sobre como lidar com sublinhados no meio de uma palavra. Para compatibilidade, use asteriscos em negrito no meio de uma palavra para dar ênfase.

|✅&nbsp; Faça isso     | ❌&nbsp; Não faça isso |
|------------------------|----------------------- |
| O amor `**é**` negrito | O amor`__é__`negrito    |

### Itálico

Para colocar o texto em itálico, adicione um asterisco ou sublinhado antes e depois de uma palavra ou frase. Para colocar o meio de uma palavra em itálico para dar ênfase, adicione um asterisco sem espaços ao redor das letras.

| Remarcação                                   | HTML                                            | Saída renderizada                        |
| -------------------------------------------- | ----------------------------------------------- | ---------------------------------------- |
| O texto em itálico é o `*miado do gato*`.    | O texto em itálico é o <em>miado do gato</em>.  | O texto em itálico é o *miado do gato* . |
| O texto em itálico é o `_miado do gato_`.    | O texto em itálico é o <em>miado do gato</em>.  | O texto em itálico é o _miado do gato_ . |
| Um `*gato*` miau                             | Um <em>gato</em>> miau                          | Um *gato* miau                           |

#### Melhores práticas em itálico
#TODO #italic-best-practices

Os aplicativos Markdown não concordam sobre como lidar com sublinhados no meio de uma palavra. Para compatibilidade, use asteriscos para colocar em itálico o meio de uma palavra para dar ênfase.

|✅&nbsp; Faça isso     |❌&nbsp; Não faça isso    |
|------------------------| ------------------------ |
| Um `*gato*` miau       | Um`_gato_`miau         |

### Negrito e Itálico
#TODO #bold-and-italic

Para enfatizar o texto com negrito e itálico ao mesmo tempo, adicione três asteriscos ou sublinhados antes e depois de uma palavra ou frase. Para colocar negrito e itálico no meio de uma palavra para dar ênfase, adicione três asteriscos sem espaços ao redor das letras.

| Remarcação                                       | HTML                                                                | Saída renderizada                              |
| ------------------------------------------------ | ------------------------------------------------------------------- | ---------------------------------------------- |
| Este texto é `***realmente importante***`.       | Este texto é `<em><strong>realmente importante</strong></em>`.      | Este texto é ***realmente importante***.       |
| Este texto é `___realmente importante___`.       | Este texto é `<em><strong>realmente importante</strong></em>`.      | Este texto é ___realmente importante___.       |
| Este texto é `__*realmente importante*__`.       | Este texto é `<em><strong>realmente importante</strong></em>`.      | Este texto é __*realmente importante*__.       |
| Este texto é `**_realmente importante**_`.       | Este texto é `<em><strong>realmente importante</strong></em>`.      | Este texto é **_realmente importante**_.       |
| Este texto é realmente `***muito***` importante. | Este texto é realmente `<em><strong>muito importante</strong></em>`.| Este texto é realmente ***muito*** importante. |

>  ℹ **Observação:** a ordem das tags `em` e `strong` pode ser invertida dependendo do processador Markdown que você está usando.

#### Práticas recomendadas para negrito e itálico
#TODO #bold-and-italic-best-practices

Os aplicativos Markdown não concordam sobre como lidar com sublinhados no meio de uma palavra. Para compatibilidade, use asteriscos para negrito e itálico no meio de uma palavra para dar ênfase.

|✅&nbsp; Faça isso                               |❌&nbsp; Não faça isso                          |
|-------------------------------------------------| ----------------------------------------------- |
| Este texto é realmente `***muito***` importante.| Este texto é realmente`___muito___`importante.|

## Citações em bloco

Para criar uma citação em bloco, adicione um `>` antes de um parágrafo.

    > Dorothy followed her through many of the beautiful rooms in her castle.

A saída renderizada fica assim:

> Dorothy a seguiu por muitos dos belos quartos de seu castelo.


### Citações em bloco com vários parágrafos
#TODO #blockquotes-with-multiple-paragraphs

Aspas em bloco podem conter vários parágrafos. Adicione um `>` nas linhas em branco entre os parágrafos.

    > Dorothy a seguiu por muitos dos belos quartos de seu castelo.

    >

    > A Bruxa ordenou-lhe que limpasse as panelas e as chaleiras, varresse o chão e mantivesse o fogo alimentado com lenha.

A saída renderizada fica assim:

> Dorothy a seguiu por muitos dos belos quartos de seu castelo.
>
> A Bruxa ordenou-lhe que limpasse as panelas e as chaleiras, varresse o chão e mantivesse o fogo alimentado com lenha.

### Citações aninhadas
#TODO #nested-blockquotes

Aspas em bloco podem ser aninhadas. Adicione um `>>` antes do parágrafo que você deseja aninhar.

    > Dorothy a seguiu por muitos dos belos quartos de seu castelo.

    >

    >> A Bruxa ordenou-lhe que limpasse as panelas e as chaleiras, varresse o chão e mantivesse o fogo alimentado com lenha.

A saída renderizada fica assim:

> Dorothy a seguiu por muitos dos belos quartos de seu castelo.
>
>> A Bruxa ordenou-lhe que limpasse as panelas e as chaleiras, varresse o chão e mantivesse o fogo alimentado com lenha.

### Blockquotes com outros elementos
#TODO #blockquotes-with-other-elements

Blockquotes podem conter outros elementos formatados em Markdown. Nem todos os elementos podem ser usados ​`​​​—` você precisará experimentar para ver quais funcionam.

    > #### Os resultados trimestrais parecem ótimos!

    >

    > - A receita estava fora do gráfico.

    > - Os lucros foram maiores do que nunca.

    >

    > *Tudo* está indo conforme o **planejado** .

A saída renderizada fica assim:

> #### Os resultados trimestrais parecem ótimos!
>
> - A receita estava fora do gráfico.
> - Os lucros foram maiores do que nunca.
>
> *Tudo* está indo conforme o **planejado**.

### Práticas recomendadas para citações em bloco
#TODO #blockquotes-best-practices

Para compatibilidade, coloque linhas em branco antes e depois das aspas.

| ✅&nbsp; Faça isso                        | ❌&nbsp; Não faça isso                             |
| ------------------------------------------ | -------------------------------------------------- |
| Tente colocar uma linha em branco antes... | Sem linhas em branco, isso pode não parecer certo.\ 
|                                            | > Esta é uma citação em bloco\                      
| > Esta é uma citação em bloco              | Não faça isso!\                                    
|                                            |                                                    |
| ...e depois de uma citação em bloco.       |                                                    |

## Listas

Você pode organizar itens em listas ordenadas e não ordenadas.

### Listas ordenadas
#TODO #ordered-lists

Para criar uma lista ordenada, adicione itens de linha com números seguidos de pontos. Os números não precisam estar em ordem numérica, mas a lista deve começar com o número um.

| Remarcação                                       | HTML                                                                | Saída renderizada                              |
| ------------------------------------------------ | ------------------------------------------------------------------- | ---------------------------------------------- |
| 1. Primeiro item <br> 2. Segundo item <br> 3. Terceiro item <br> 4. Quarto item| `<ol>`<br>ㅤ`<li>Primeiro item</li>`<br>ㅤ`<li>Segundo item</li>`<br>ㅤ`<li>Terceiro item</li>`<br>ㅤ`<li>Quarto item</li>`<br>`</ol>`| 1. Primeiro item <br> 2. Segundo item <br> 3. Terceiro item <br> 4. Quarto item|
| 1. Primeiro item <br> 1. Segundo item <br> 1. Terceiro item <br> 1. Quarto item| `<ol>`<br>ㅤ`<li>Primeiro item</li>`<br>ㅤ`<li>Segundo item</li>`<br>ㅤ`<li>Terceiro item</li>`<br>ㅤ`<li>Quarto item</li>`<br>`</ol>`| 1. Primeiro item <br> 2. Segundo item <br> 3. Terceiro item <br> 4. Quarto item|
| 1. Primeiro item <br> 8. Segundo item <br> 3. Terceiro item <br> 5. Quarto item| `<ol>`<br>ㅤ`<li>Primeiro item</li>`<br>ㅤ`<li>Segundo item</li>`<br>ㅤ`<li>Terceiro item</li>`<br>ㅤ`<li>Quarto item</li>`<br>`</ol>`| 1. Primeiro item <br> 2. Segundo item <br> 3. Terceiro item <br> 4. Quarto item|
| 1. Primeiro item <br> 2. Segundo item <br> 3. Terceiro item <br>ㅤㅤ1. Item recuado <br>ㅤㅤ2. Item recuado <br> 4. Quarto item | `<ol>`<br>ㅤ`<li>Primeiro item</li>`<br>ㅤ`<li>Segundo item</li>`<br>ㅤ`<li>Terceiro item</li>`<br>ㅤ`<li>Quarto item</li>`<br>`</ol>`| 1. Primeiro item <br> 2. Segundo item <br> 3. Terceiro item <br>ㅤㅤ1. Item recuado <br>ㅤㅤ2. Item recuado <br> 4. Quarto item |

#### Melhores práticas de lista ordenada
#TODO #ordered-list-best-practices

CommonMark e algumas outras linguagens de marcação leves permitem usar parênteses `( ))` como delimitador (por exemplo, 1) _First item_), mas nem todo Markdown os aplicativos suportam isso, portanto não é uma ótima opção do ponto de vista de compatibilidade. Para fins de compatibilidade, use apenas pontos.

|✅&nbsp; Faça isso |❌&nbsp; Não faça isso |
| ----------------- | ---------------------- |
|1. First item<br>  |1) First item<br>       |
|2. Second item     |2) Second item          |

### Listas não ordenadas
#TODO #unordered-lists

Para criar uma lista não ordenada, adicione travessões ( `-` ), asteriscos ( `*` ) ou sinais de adição ( `+` ) na frente dos itens de linha. Recue um ou mais itens para criar uma lista aninhada.

| Remarcação                                       | HTML                                                                | Saída renderizada                              |
| ------------------------------------------------ | ------------------------------------------------------------------- | ---------------------------------------------- |
| - Primeiro item <br> - Segundo item <br> - Terceiro item <br> - Quarto item| `<ul>`<br>ㅤ`<li>Primeiro item</li>`<br>ㅤ`<li>Segundo item</li>`<br>ㅤ`<li>Terceiro item</li>`<br>ㅤ`<li>Quarto item</li>`<br>`</ul>`| • Primeiro item <br> • Segundo item <br> • Terceiro item <br> • Quarto item|
| * Primeiro item <br> * Segundo item <br> * Terceiro item <br> * Quarto item| `<ul>`<br>ㅤ`<li>Primeiro item</li>`<br>ㅤ`<li>Segundo item</li>`<br>ㅤ`<li>Terceiro item</li>`<br>ㅤ`<li>Quarto item</li>`<br>`</ul>`| • Primeiro item <br> • Segundo item <br> • Terceiro item <br> • Quarto item|
| + Primeiro item <br> + Segundo item <br> + Terceiro item <br> + Quarto item| `<ul>`<br>ㅤ`<li>Primeiro item</li>`<br>ㅤ`<li>Segundo item</li>`<br>ㅤ`<li>Terceiro item</li>`<br>ㅤ`<li>Quarto item</li>`<br>`</ul>`| • Primeiro item <br> • Segundo item <br> • Terceiro item <br> • Quarto item|
| - Primeiro item <br> - Segundo item <br> - Terceiro item <br>ㅤㅤ- Item recuado <br>ㅤㅤ- Item recuado <br> - Quarto item | `<ul>`<br>ㅤ`<li>Primeiro item</li>`<br>ㅤ`<li>Segundo item</li>`<br>ㅤ`<li>Terceiro item</li>`<br>ㅤ`<li>Quarto item</li>`<br>`</ul>`| • Primeiro item <br> • Segundo item <br> • Terceiro item <br>ㅤㅤ◦ Item recuado <br>ㅤㅤ◦ Item recuado <br> • Quarto item |

#### Iniciando itens de lista não ordenados com números
#TODO #starting-unordered-list-items-with-numbers

Se precisar iniciar um item de lista não ordenado com um número seguido de um ponto final, você pode usar uma barra invertida ( `/` ) para [escapar](#caracteres-escapando) do ponto.

| Remarcação                                                      | HTML                                         | Saída renderizada                    |
| --------------------------------------------------------------- | -------------------------------------------- | ------------------------------------ |
| - 1968\. Um ótimo ano!<br>- Acho que 1969 foi o segundo melhor. |`<ul>`<br>ㅤ`<li>1968. Um ótimo ano!</li>`<br>`<li>Acho que 1969 foi o segundo melhor.</li>`<br>`</ul>` |• 1968. Um ótimo ano!<br>• Acho que 1969 foi o segundo melhor.|

#### Práticas recomendadas para lista não ordenada
#TODO #unordered-list-best-practices

Os aplicativos Markdown não concordam sobre como lidar com diferentes delimitadores na mesma lista. Para compatibilidade, não misture e combine delimitadores na mesma lista `–` escolha um e mantenha-o.

| ✅&nbsp; Faça isso                                                       | ❌&nbsp; Não faça isso |
| ------------------------------------------------------------------------ | ----------------------- |
| - Primeiro item<br>- Segundo item<br>- Terceiro item<br>- Quarto item    | + Primeiro item<br>* Segundo item<br>- Terceiro item<br>+ Quarto item|
      

### Adicionando Elementos em Listas
#TODO #adding-elements-in-lists

Para adicionar outro elemento a uma lista preservando a continuidade da lista, recue o elemento com quatro espaços ou uma tabulação, conforme mostrado nos exemplos a seguir.

>  ℹ **Dica:** Se as coisas não aparecerem da maneira esperada, verifique novamente se você recuou os elementos da lista com quatro espaços ou uma tabulação.

#### Parágrafos

    * Este é o primeiro item da lista.
    * Aqui está o segundo item da lista.

        Preciso adicionar outro parágrafo abaixo do segundo item da lista.

    * E aqui está o terceiro item da lista.

A saída renderizada fica assim:

* Este é o primeiro item da lista.
* Aqui está o segundo item da lista.

    Preciso adicionar outro parágrafo abaixo do segundo item da lista.

* E aqui está o terceiro item da lista.

#### Citações em bloco
#TODO #blockquotes

    * Este é o primeiro item da lista.
    * Aqui está o segundo item da lista.
    
        > Uma citação em bloco ficaria ótima abaixo do segundo item da lista.

    * E aqui está o terceiro item da lista

A saída renderizada fica assim:

* Este é o primeiro item da lista.
* Aqui está o segundo item da lista.
    > Uma citação em bloco ficaria ótima abaixo do segundo item da lista.
* E aqui está o terceiro item da lista

#### Blocos de códigos
#TODO #code-blocks-1

[Os blocos de código](#blocos-de-código) normalmente são recuados com quatro espaços ou uma tabulação. Quando estiverem em uma lista, recue-os com oito espaços ou duas tabulações.

    1. Abra o arquivo.
    2. Encontre o seguinte bloco de código na linha 21:

        <html>
          <head>
            <title>Test</title>
          </head>

    3. Atualize o título para corresponder ao nome do seu site.

A saída renderizada fica assim:

1. Abra o arquivo.
2. Encontre o seguinte bloco de código na linha 21:

        <html>
          <head>
            <title>Test</title>
          </head>  

3. Atualize o título para corresponder ao nome do seu site.

#### Imagens
#TODO #images

    1. Abra o arquivo que contém o mascote do Linux.
    2. Maravilhe-se com sua beleza.

        ![Tux, the Linux mascot](/assets/images/tux.png)

    3. Feche o arquivo.

A saída renderizada fica assim:

1. Abra o arquivo que contém o mascote do Linux.
2. Maravilhe-se com sua beleza.

    ![Tux, the Linux mascot](https://mdg.imgix.net/assets/images/tux.png?auto=format&fit=clip&q=40&w=100)

3. Feche o arquivo.

#### Listas
#TODO #lists

Você pode aninhar uma lista não ordenada em uma lista ordenada ou vice-versa.

    1. Primeiro item
    2. Segundo item
    3. Terceiro item
          - Item recuado
          - Item recuado
    4. Quarto item

A saída renderizada fica assim:

1. Primeiro item
2. Segundo item
3. Terceiro item
      - Item recuado
      - Item recuado
4. Quarto item

## Código

Para denotar uma palavra ou frase como código, coloque-a entre crases ( ` ).

|Remarcação                              |HTML                                                  |Saída renderizada                       |
| -------------------------------------- | ---------------------------------------------------- |--------------------------------------- |
|``No prompt de comando, digite `Nano`.``| No prompt de comando, digite <code>Nano</code>.      |No prompt de comando, digite `nano`.    |

### Escapando de crases
#TODO #escaping-backticks

Se a palavra ou frase que você deseja denotar como código incluir um ou mais crases, você poderá escapar dela colocando a palavra ou frase entre crases duplos `( `` )`.

|Remarcação                             |HTML                                              |Saída renderizada           |
| ------------------------------------- | ------------------------------------------------ | -------------------------  |
|``Use `code` em seu arquivo Markdown.``| <code>Use `code` em seu arquivo Markdown.</code> |Use ´code´ in your Markdown file.|

### Blocos de código
#TODO #code-blocks

Para criar blocos de código, recue cada linha do bloco com pelo menos quatro espaços ou uma tabulação.

    <html>
      <head>
      </head>
    </html>

A saída renderizada fica assim:

    <html>
      <head>
      </head>
    </html>

>  ℹ **Nota:** Para criar blocos de código sem recuar linhas, use [blocos de código protegidos](https://www.markdownguide.org/extended-syntax/#fenced-code-blocks).

## Regras horizontais

Para criar uma regra horizontal, use três ou mais asteriscos ( `***` ), travessões ( `---` ) ou sublinhados ( `___` ) em uma linha sozinhos.

    ***
    ---
    ______________
A saída renderizada de todos os três parece idêntica:

_____________________________________________________

### Práticas recomendadas para regras horizontais
#TODO #horizontal-rule-best-practices

Para compatibilidade, coloque linhas em branco antes e depois das réguas horizontais.

| ✅&nbsp; Faça isso                                                                      | ❌&nbsp; Não faça isso |
|----------------------------------------------------------------------------------------- |------------------------|
|Tente colocar uma linha em branco antes...<br><br>---<br><br>...e depois de uma regra horizontal. |Sem linhas em branco, este seria um título.<br>---<br>Não faça isso!

## Ligações

Para criar um link, coloque o texto do link entre colchetes (por exemplo, `[Duck Duck Go]`) e siga-o imediatamente com o URL entre parênteses (por exemplo, `(https://duckduckgo.com)`).

    My favorite search engine is [Duck Duck Go](https://duckduckgo.com).


A saída renderizada fica assim:

Meu mecanismo de pesquisa favorito é [Duck Duck Go](https://duckduckgo.com).

>  ℹ **Nota:** Para vincular a um elemento na mesma página, consulte [vinculação a IDs de cabeçalho](https://www.markdownguide.org/extended-syntax/#linking-to-heading-ids) . Para criar um link que abre em uma nova guia ou janela, consulte a seção sobre [destinos de link](https://www.markdownguide.org/hacks/#link-targets).

### Adicionando títulos
#TODO #adding-titles

Opcionalmente, você pode adicionar um título para um link. Isso aparecerá como uma dica quando o usuário passar o mouse sobre o link. Para adicionar um título, coloque-o entre aspas após o URL.

    My favorite search engine is [Duck Duck Go](https://duckduckgo.com "The best search engine for privacy").

A saída renderizada fica assim:
Meu mecanismo de pesquisa favorito é [Duck Duck Go](https://duckduckgo.com).

### URLs e endereços de e-mail
#TODO #urls-and-email-addresses

Para transformar rapidamente um URL ou endereço de e-mail em um link, coloque-o entre colchetes angulares.

    <https://www.markdownguide.org>
    <fake@example.com>

A saída renderizada fica assim:

 <https://www.markdownguide.org>

 <fake@example.com>

### Formatando links
#TODO #formatting-links

Para [enfatizar](#ênfase) os links, adicione asteriscos antes e depois dos colchetes e parênteses. Para denotar links como [code](#código), adicione crases entre colchetes.

    Adoro apoiar a **[EFF](https://eff.org)**.

    Este é o *[Markdown Guide](https://www.markdownguide.org)*.

    Consulte a seção sobre [`code`](#code).

A saída renderizada fica assim:

Adoro apoiar a **[EFF](https://eff.org)**.

Este é o *[Markdown Guide](https://www.markdownguide.org)*.

Consulte a seção sobre [`code`](#code).

### Links de estilo de referência
#TODO #reference-style-links

Links de estilo de referência são um tipo especial de link que torna os URLs mais fáceis de exibir e ler no Markdown. Os links de estilo de referência são construídos em duas partes: a parte que você mantém alinhada ao seu texto e a parte que você armazena em outro lugar do arquivo para manter o texto fácil de ler.

#### Formatando a primeira parte do link
#TODO #formatting-the-first-part-of-the-link

A primeira parte de um link de estilo de referência é formatada com dois conjuntos de colchetes. O primeiro conjunto de colchetes circunda o texto que deve aparecer vinculado. O segundo conjunto de colchetes exibe um rótulo usado para apontar para o link que você está armazenando em outro lugar do documento.

Embora não seja obrigatório, você pode incluir um espaço entre o primeiro e o segundo conjunto de colchetes. O rótulo no segundo conjunto de colchetes não diferencia maiúsculas de minúsculas e pode incluir letras, números, espaços ou pontuação.

Isso significa que os seguintes formatos de exemplo são aproximadamente equivalentes para a primeira parte do link:

* [hobbit-hole][1]
* [hobbit-hole][1]

#### Formatando a segunda parte do link
#TODO #formatting-the-second-part-of-the-link

A segunda parte de um link de estilo de referência é formatada com os seguintes atributos:

    1. O rótulo, entre colchetes, seguido imediatamente por dois pontos e pelo menos um espaço (por exemplo, [label]: ).
    2. O URL do link, que você pode colocar opcionalmente entre colchetes angulares.
    3. O título opcional do link, que você pode colocar entre aspas duplas, aspas simples ou parênteses.

Isso significa que os formatos de exemplo a seguir são aproximadamente equivalentes para a segunda parte do link:

    * [1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle
    * [1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle "Hobbit lifestyles"
    * [1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle 'Hobbit lifestyles'
    * [1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle (Hobbit lifestyles)
    * [1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle "Hobbit lifestyles"
    * [1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle 'Hobbit lifestyles'
    * [1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle (Hobbit lifestyles)

Você pode colocar esta segunda parte do link em qualquer lugar do seu documento Markdown. Algumas pessoas os colocam imediatamente após o parágrafo em que aparecem, enquanto outras os colocam no final do documento (como notas finais ou de rodapé).

#### Um exemplo juntando as peças
#TODO #an-example-putting-the-parts-together

Digamos que você adicione um URL como um [link de URL padrão](#ligações) a um parágrafo e ele ficará assim no Markdown:

    Num buraco no chão vivia um hobbit. Não é um buraco nojento, sujo e molhado, cheio de pontas
    de vermes e com cheiro de lodo, nem um buraco seco, vazio e arenoso, sem nada onde sentar ou onde sentar.
    comer: era uma [toca de hobbit](https://en.wikipedia.org/wiki/Hobbit#Lifestyle "Hobbit lifestyles"), e isso significa conforto.

Embora possa apontar para informações adicionais interessantes, o URL exibido realmente não acrescenta muito ao texto bruto existente, a não ser torná-lo mais difícil de ler. Para corrigir isso, você pode formatar o URL assim:

    Em um buraco no chão vivia um hobbit. Não um buraco nojento, sujo e úmido, cheio de pontas de minhocas e com cheiro de lodo, nem ainda um buraco seco, vazio e arenoso, sem nada onde sentar ou comer: era um [buraco de hobbit](https://en.wikipedia.org/wiki/Hobbit#Lifestyle), e isso significa conforto.

Em ambos os casos acima, a saída renderizada seria idêntica:

>
> Em um buraco no chão vivia um hobbit. Não um buraco nojento, sujo e úmido, cheio de pontas de minhocas e com cheiro de lodo, nem ainda um buraco seco, vazio e arenoso, sem nada onde sentar ou comer: era um [buraco de hobbit](https://en.wikipedia.org/wiki/Hobbit#Lifestyle), e isso significa conforto.
>

e o HTML do link seria:

    <a href="https://en.wikipedia.org/wiki/Hobbit#Lifestyle title="Hobbit lifestyles">hobbit-hole</a>

### Vincular práticas recomendadas
#TODO #link-best-practices

Os aplicativos Markdown não concordam sobre como lidar com espaços no meio de um URL. Para compatibilidade, tente codificar em URL quaisquer espaços com 20%. Como alternativa, se seu aplicativo Markdown [suportar HTML](#html), você poderá usar a tag HTML.

| ✅&nbsp; Faça isso                                       | ❌&nbsp; Não faça isso                               |
| -------------------------------------------------------- | ------------------------------------------------------|
|`[link](https://www.example.com/my%20great%20page)`<br><br>`<a href="https://www.example.com/my great page">link</a>`|`[link](https://www.example.com/my great page)`<br><br>|

Parênteses no meio de um URL também podem ser problemáticos. Para compatibilidade, tente codificar em URL o parêntese de abertura `(()` com %28e o parêntese de fechamento `( ))` com %29. Alternativamente, se o seu aplicativo Markdown [suportar HTML](#html) , você poderá usar a atag HTML.

| ✅&nbsp; Faça isso                                       | ❌&nbsp; Não faça isso                               |
| -------------------------------------------------------- | ------------------------------------------------------|
|`[a novel](https://en.wikipedia.org/wiki/The_Milagro_Beanfield_War_%28novel%29)`<br><br>`<a href="https://en.wikipedia.org/wiki/The_Milagro_Beanfield_War_(novel)">a novel</a>`|`[a novel](https://en.wikipedia.org/wiki/The_Milagro_Beanfield_War_(novel))`|

## Imagens

Para adicionar uma imagem, adicione um ponto de exclamação ( `!` ), seguido de texto alternativo entre colchetes e o caminho ou URL do recurso de imagem entre parênteses. Opcionalmente, você pode adicionar um título entre aspas após o caminho ou URL.

    ![The San Juan Mountains are beautiful!](/assets/images/san-juan-mountains.jpg "San Juan Mountains")

A saída renderizada fica assim:

![The San Juan Mountains are beautiful!](https://mdg.imgix.net/assets/images/san-juan-mountains.jpg?auto=format&fit=clip&q=40&w=800 "San Juan Mountains")

>  ℹ **Nota:** Para redimensionar uma imagem, consulte a seção sobre [tamanho da imagem](https://www.markdownguide.org/hacks/#image-size) . Para adicionar uma legenda, consulte a seção sobre [legendas de imagens](https://www.markdownguide.org/hacks/#image-captions).

### Vinculando imagens
#TODO #linking-images

Para adicionar um link a uma imagem, coloque o Markdown da imagem entre colchetes e adicione o link entre parênteses.

    [![An old rock in the desert](/assets/images/shiprock.jpg "Shiprock, New Mexico by Beau Rogers")](https://www.flickr.com/photos/beaurogers/31833779864/in/photolist-Qv3rFw-34mt9F-a9Cmfy-5Ha3Zi-9msKdv-o3hgjr-hWpUte-4WMsJ1-KUQ8N-deshUb-vssBD-6CQci6-8AFCiD-zsJWT-nNfsgB-dPDwZJ-bn9JGn-5HtSXY-6CUhAL-a4UTXB-ugPum-KUPSo-fBLNm-6CUmpy-4WMsc9-8a7D3T-83KJev-6CQ2bK-nNusHJ-a78rQH-nw3NvT-7aq2qf-8wwBso-3nNceh-ugSKP-4mh4kh-bbeeqH-a7biME-q3PtTf-brFpgb-cg38zw-bXMZc-nJPELD-f58Lmo-bXMYG-bz8AAi-bxNtNT-bXMYi-bXMY6-bXMYv)


A saída renderizada fica assim:

[![An old rock in the desert](https://mdg.imgix.net/assets/images/shiprock.jpg?auto=format&fit=clip&q=40&w=800 "Shiprock, New Mexico by Beau Rogers")](https://www.flickr.com/photos/beaurogers/31833779864/in/photolist-Qv3rFw-34mt9F-a9Cmfy-5Ha3Zi-9msKdv-o3hgjr-hWpUte-4WMsJ1-KUQ8N-deshUb-vssBD-6CQci6-8AFCiD-zsJWT-nNfsgB-dPDwZJ-bn9JGn-5HtSXY-6CUhAL-a4UTXB-ugPum-KUPSo-fBLNm-6CUmpy-4WMsc9-8a7D3T-83KJev-6CQ2bK-nNusHJ-a78rQH-nw3NvT-7aq2qf-8wwBso-3nNceh-ugSKP-4mh4kh-bbeeqH-a7biME-q3PtTf-brFpgb-cg38zw-bXMZc-nJPELD-f58Lmo-bXMYG-bz8AAi-bxNtNT-bXMYi-bXMY6-bXMYv)

## Caracteres escapando

Para exibir um caractere literal que de outra forma seria usado para formatar texto em um documento Markdown, adicione uma barra invertida ( `\` ) na frente do caractere.

    \* Without the backslash, this would be a bullet in an unordered list.

A saída renderizada fica assim:

* Sem a barra invertida, isso seria um marcador em uma lista não ordenada.

### Caracteres dos quais você pode escapar
#TODO #characters-you-can-escape

Você pode usar uma barra invertida para escapar dos seguintes caracteres.

|Caracteres   |Nome                                                                            |
| ----------- | ------------------------------------------------------------------------------ |
|\            |barra invertida                                                                 |
|`            |backtick (veja também [escapando de backticks no código](#escapando-de-crases)) |
|*            |asterisco                                                                       | 
|_            |sublinhado                                                                      |
|{}           |chaves                                                                          |
|[]           |colchetes                                                                       |
|<>           |colchetes angulares                                                             |
|()           |parênteses                                                                      |
|#            |cerquilha.                                                                      |
|+            |sinal de mais                                                                   |
|-            |sinal de menos (hífen)                                                          |
|.            |ponto                                                                           |
|!            |ponto de exclamação                                                             |
||            |pipe                                                                            |

## HTML

Muitos aplicativos Markdown permitem usar tags HTML em texto formatado em Markdown. Isso é útil se você preferir certas tags HTML à sintaxe Markdown. Por exemplo, algumas pessoas acham mais fácil usar tags HTML para imagens. Usar HTML também é útil quando você precisa alterar os atributos de um elemento, como especificar a [cor do texto](https://www.markdownguide.org/hacks/#color) ou alterar a largura de uma imagem.

Para usar HTML, coloque as tags no texto do seu arquivo formatado em Markdown.

    This **word** is bold. This <em>word</em> is italic.

A saída renderizada fica assim:

Esta **palavra** é ousada. Esta *palavra* está em itálico.

### Práticas recomendadas de HTML
#TODO #html-best-practices

Por motivos de segurança, nem todos os aplicativos Markdown suportam HTML em documentos Markdown. Em caso de dúvida, verifique a documentação do seu aplicativo Markdown. Alguns aplicativos suportam apenas um subconjunto de tags HTML.

Use linhas em branco para separar elementos HTML em nível de bloco, como , `<div>`, e do conteúdo circundante. Tente não recuar as tags com tabulações ou espaços — isso pode interferir na formatação.`<table><pre><p>`

Você não pode usar a sintaxe Markdown dentro de tags HTML em nível de bloco. Por exemplo, `<p>italic and **bold**</p>` não funcionará.
F
## Emojis

[Emoji para MarkDown](https://gist.github.com/rxaviers/7360908)

### People

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

### Nature

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

### Objects

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

### Places

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

### Symbols

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

## Referências

- https://www.markdownguide.org/basic-syntax/
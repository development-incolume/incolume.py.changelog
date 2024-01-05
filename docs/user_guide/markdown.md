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
|---------------------|-----------------------------|--------------------------|
| `# Heading level 1` | 	`<h1>Heading level 1</h1>` | <h1>Heading level 1</h1> |
| `# Heading level 2` | 	`<h2>Heading level 2</h2>` | <h1>Heading level 1</h1> |
| `# Heading level 3` | 	`<h3>Heading level 3</h3>` | <h3>Heading level 3</h3> |
| `# Heading level 4` | 	`<h4>Heading level 4</h4>` | <h4>Heading level 4</h4> |
| `# Heading level 5` | 	`<h5>Heading level 5</h5>` | <h5>Heading level 5</h5> |
| `# Heading level 6` | 	`<h6>Heading level 6</h6>` | <h6>Heading level 6</h6> |

## Sintaxe Alternativa
Como alternativa, na linha abaixo do texto, adicione qualquer número de `==` caracteres para o nível de título 1 ou `--` caracteres para o nível de título 2.

| Remarcação                                                                | 	HTML                       | Saída renderizada        |
|---------------------------------------------------------------------------|-----------------------------|--------------------------|
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

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">A menos que o </font></font><a href="/basic-syntax/#paragraphs"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">parágrafo esteja em uma lista</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">, não recue os parágrafos com espaços ou tabulações.</font></font></p>

<div class="alert alert-info">
  <svg class="svg-inline--fa fa-info-circle fa-w-16" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="info-circle" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" data-fa-i2svg=""><path fill="currentColor" d="M256 8C119.043 8 8 119.083 8 256c0 136.997 111.043 248 248 248s248-111.003 248-248C504 119.083 392.957 8 256 8zm0 110c23.196 0 42 18.804 42 42s-18.804 42-42 42-42-18.804-42-42 18.804-42 42-42zm56 254c0 6.627-5.373 12-12 12h-88c-6.627 0-12-5.373-12-12v-24c0-6.627 5.373-12 12-12h12v-64h-12c-6.627 0-12-5.373-12-12v-24c0-6.627 5.373-12 12-12h64c6.627 0 12 5.373 12 12v100h12c6.627 0 12 5.373 12 12v24z"></path></svg><!-- <i class="fas fa-info-circle"></i> --> <strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Observação:</font></font></strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> se você precisar recuar parágrafos na saída, consulte a seção sobre como </font></font><a href="/hacks/#indent-tab"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">recuar (tabulação)&lt; uma eu=3&gt;.
</font></font></a><font style="vertical-align: inherit;"></font></div>

<table class="table table-bordered">
  <thead class="thead-light">
    <tr>
      <th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">✅&nbsp; Faça isso</font></font></th>
      <th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">❌&nbsp; Não faça isso</font></font></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <code class="highlighter-rouge">
          Don't put tabs or spaces in front of your paragraphs.<br><br>

          Keep lines left-aligned like this.<br><br>
        </code>
      </td>
      <td>
        <code class="highlighter-rouge">
        &nbsp;&nbsp;&nbsp;&nbsp;This can result in unexpected
        formatting problems.<br><br>

        &nbsp;&nbsp;Don't add tabs or spaces in front of paragraphs.
        </code>
      </td>
    </tr>
  </tbody>
</table>

## Quebras de linha

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Para criar uma quebra de linha ou uma nova linha (</font></font><code class="language-plaintext highlighter-rouge">&lt;br&gt;</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">), termine uma linha com dois ou mais espaços e digite return.</font></font></p>

<table class="table table-bordered">
  <thead class="thead-light">
    <tr>
      <th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Remarcação</font></font></th>
      <th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">HTML</font></font></th>
      <th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Saída renderizada</font></font></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <code class="highlighter-rouge">
          This is the first line. &nbsp;<br>
          And this is the second line.
        </code>
      </td>
      <td>
        <code class="highlighter-rouge">&lt;p&gt;This is the first line.&lt;br&gt;<br>

        And this is the second line.&lt;/p&gt;</code>
      </td>
      <td>
        <p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Esta é a primeira linha.</font></font><br><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
        E esta é a segunda linha.</font></font></p>
      </td>
    </tr>
  </tbody>
</table>

<h3 id="line-break-best-practices"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Práticas recomendadas para quebra de linha</font></font><a class="anchorjs-link " aria-label="Âncora" data-anchorjs-icon="" href="#line-break-best-practices" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h3>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Você pode usar dois ou mais espaços (comumente chamados de “espaço em branco à direita”) para quebras de linha em quase todos os aplicativos Markdown, mas isso é controverso. É difícil ver espaços em branco no final de um editor, e muitas pessoas acidentalmente ou intencionalmente colocam dois espaços após cada frase. Por esse motivo, você pode querer usar algo diferente de espaços em branco à direita para quebras de linha. Se seu aplicativo Markdown </font></font><a href="/basic-syntax/#html"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">suportar HTML</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">, você poderá usar a tag HTML </font></font><code class="language-plaintext highlighter-rouge">&lt;br&gt;</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">.</font></font></p>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Para compatibilidade, use o espaço em branco final ou a tag HTML </font></font><code class="language-plaintext highlighter-rouge">&lt;br&gt;</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> no final da linha.</font></font></p>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Existem duas outras opções que não recomendo usar. CommonMark e algumas outras linguagens de marcação leves permitem digitar uma barra invertida (</font></font><code class="language-plaintext highlighter-rouge">\</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">) no final da linha, mas nem todos os aplicativos Markdown suportam isso, portanto não é uma ótima opção de compatibilidade perspectiva. E pelo menos algumas linguagens de marcação leves não exigem nada no final da linha — basta digitar return e elas criarão uma quebra de linha.</font></font></p>

<table class="table table-bordered">
  <thead class="thead-light">
    <tr>
      <th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">✅&nbsp; Faça isso</font></font></th>
      <th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">❌&nbsp; Não faça isso</font></font></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <code class="highlighter-rouge">
          First line with two spaces after. &nbsp;<br>
          And the next line.<br><br>

          First line with the HTML tag after.&lt;br&gt;<br>
          And the next line.<br><br>
        </code>
      </td>
      <td>
        <code class="highlighter-rouge">
        First line with a backslash after.\<br>
        And the next line.<br><br>

        First line with nothing after.<br>
        And the next line.<br><br>
        </code>
      </td>
    </tr>
  </tbody>
</table>


## Ênfase

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Você pode adicionar ênfase colocando o texto em negrito ou itálico.</font></font></p>

<h3 id="bold"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Audacioso</font></font><a class="anchorjs-link " aria-label="Âncora" data-anchorjs-icon="" href="#bold" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h3>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Para texto em negrito, adicione dois asteriscos ou sublinhados antes e depois de uma palavra ou frase. Para colocar o meio de uma palavra em negrito para dar ênfase, adicione dois asteriscos sem espaços ao redor das letras.</font></font></p>

<table class="table table-bordered">
  <thead class="thead-light">
    <tr>
      <th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Remarcação</font></font></th>
      <th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">HTML</font></font></th>
      <th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Saída renderizada</font></font></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code class="highlighter-rouge">I just love **bold text**.</code></td>
      <td><code class="highlighter-rouge">I just love &lt;strong&gt;bold text&lt;/strong&gt;.</code></td>
      <td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Adoro </font></font><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">texto em negrito</font></font></strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">.</font></font></td>
    </tr>
    <tr>
      <td><code class="highlighter-rouge">I just love __bold text__.</code></td>
      <td><code class="highlighter-rouge">I just love &lt;strong&gt;bold text&lt;/strong&gt;.</code></td>
      <td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Adoro </font></font><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">texto em negrito</font></font></strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">.</font></font></td>
    </tr>
    <tr>
      <td><code class="highlighter-rouge">Love**is**bold</code></td> <td><code class="highlighter-rouge">Love&lt;strong&gt;is&lt;/strong&gt;bold</code></td>
      <td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Amor</font></font><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">é</font></font></strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">ousado</font></font></td>
    </tr>
  </tbody>
</table>

<h4 id="bold-best-practices"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Melhores práticas ousadas</font></font><a class="anchorjs-link " aria-label="Âncora" data-anchorjs-icon="" href="#bold-best-practices" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h4>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Os aplicativos Markdown não concordam sobre como lidar com sublinhados no meio de uma palavra. Para compatibilidade, use asteriscos em negrito no meio de uma palavra para dar ênfase.</font></font></p>

<table class="table table-bordered">
  <thead class="thead-light">
    <tr>
      <th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">✅&nbsp; Faça isso</font></font></th>
      <th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">❌&nbsp; Não faça isso</font></font></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <code class="highlighter-rouge">
          Love**is**bold
        </code>
      </td>
      <td>
        <code class="highlighter-rouge">
          Love__is__bold
        </code>
      </td>
    </tr>
  </tbody>
</table>

<h3 id="italic"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">itálico</font></font><a class="anchorjs-link " aria-label="Âncora" data-anchorjs-icon="" href="#italic" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h3>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Para colocar o texto em itálico, adicione um asterisco ou sublinhado antes e depois de uma palavra ou frase. Para colocar o meio de uma palavra em itálico para dar ênfase, adicione um asterisco sem espaços ao redor das letras.</font></font></p>

<table class="table table-bordered">
  <thead class="thead-light">
    <tr>
      <th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Remarcação</font></font></th>
      <th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">HTML</font></font></th>
      <th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Saída renderizada</font></font></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code class="highlighter-rouge">Italicized text is the *cat's meow*.</code></td>
      <td><code class="highlighter-rouge">Italicized text is the &lt;em&gt;cat's meow&lt;/em&gt;.</code></td>
      <td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">O texto em itálico é o </font></font><em><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">miau do gato</font></font></em><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">.</font></font></td>
    </tr>
    <tr>
      <td><code class="highlighter-rouge">Italicized text is the _cat's meow_.</code></td>
      <td><code class="highlighter-rouge">Italicized text is the &lt;em&gt;cat's meow&lt;/em&gt;.</code></td>
      <td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">O texto em itálico é o </font></font><em><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">miau do gato</font></font></em><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">.</font></font></td>
    </tr>
    <tr>
      <td><code class="highlighter-rouge">A*cat*meow</code></td>
      <td><code class="highlighter-rouge">A&lt;em&gt;cat&lt;/em&gt;meow</code></td>
      <td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Um</font></font><em><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">gato</font></font></em><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">miau</font></font></td>
    </tr>
  </tbody>
</table>

<h4 id="italic-best-practices"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Melhores práticas em itálico</font></font><a class="anchorjs-link " aria-label="Âncora" data-anchorjs-icon="" href="#italic-best-practices" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h4>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Os aplicativos Markdown não concordam sobre como lidar com sublinhados no meio de uma palavra. Para compatibilidade, use asteriscos para colocar em itálico o meio de uma palavra para dar ênfase.</font></font></p>

<table class="table table-bordered">
  <thead class="thead-light">
    <tr>
      <th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">✅&nbsp; Faça isso</font></font></th>
      <th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">❌&nbsp; Não faça isso</font></font></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <code class="highlighter-rouge">
          A*cat*meow
        </code>
      </td>
      <td>
        <code class="highlighter-rouge">
          A_cat_meow
        </code>
      </td>
    </tr>
  </tbody>
</table>

<h3 id="bold-and-italic"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Negrito e Itálico</font></font><a class="anchorjs-link " aria-label="Âncora" data-anchorjs-icon="" href="#bold-and-italic" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h3>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Para enfatizar o texto com negrito e itálico ao mesmo tempo, adicione três asteriscos ou sublinhados antes e depois de uma palavra ou frase. Para colocar negrito e itálico no meio de uma palavra para dar ênfase, adicione três asteriscos sem espaços ao redor das letras.</font></font></p>

<table class="table table-bordered">
  <thead class="thead-light">
    <tr>
      <th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Remarcação</font></font></th>
      <th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">HTML</font></font></th>
      <th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Saída renderizada</font></font></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code class="highlighter-rouge">This text is ***really important***.</code></td>
      <td><code class="highlighter-rouge">This text is &lt;em&gt;&lt;strong&gt;really important&lt;/strong&gt;&lt;/em&gt;.</code></td>
      <td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Este texto é </font></font><em><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">muito importante</font></font></strong></em><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">.</font></font></td>
    </tr>
    <tr>
      <td><code class="highlighter-rouge">This text is ___really important___.</code></td>
      <td><code class="highlighter-rouge">This text is &lt;em&gt;&lt;strong&gt;really important&lt;/strong&gt;&lt;/em&gt;.</code></td>
      <td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Este texto é </font></font><em><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">muito importante</font></font></strong></em><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">.</font></font></td>
    </tr>
    <tr>
      <td><code class="highlighter-rouge">This text is __*really important*__.</code></td>
      <td><code class="highlighter-rouge">This text is &lt;em&gt;&lt;strong&gt;really important&lt;/strong&gt;&lt;/em&gt;.</code></td>
      <td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Este texto é </font></font><em><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">muito importante</font></font></strong></em><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">.</font></font></td>
    </tr>
    <tr>
      <td><code class="highlighter-rouge">This text is **_really important_**.</code></td>
      <td><code class="highlighter-rouge">This text is &lt;em&gt;&lt;strong&gt;really important&lt;/strong&gt;&lt;/em&gt;.</code></td>
      <td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Este texto é </font></font><em><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">muito importante</font></font></strong></em><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">.</font></font></td>
    </tr>
    <tr>
      <td><code class="highlighter-rouge">This is really***very***important text.</code></td>
      <td><code class="highlighter-rouge">This is really&lt;em&gt;&lt;strong&gt;very&lt;/strong&gt;&lt;/em&gt;important text.</code></td>
      <td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Este é realmente</font></font><em><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">um texto muito</font></font></strong></em><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">importante.</font></font></td>
    </tr>
  </tbody>
</table>

<div class="alert alert-info">
  <svg class="svg-inline--fa fa-info-circle fa-w-16" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="info-circle" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" data-fa-i2svg=""><path fill="currentColor" d="M256 8C119.043 8 8 119.083 8 256c0 136.997 111.043 248 248 248s248-111.003 248-248C504 119.083 392.957 8 256 8zm0 110c23.196 0 42 18.804 42 42s-18.804 42-42 42-42-18.804-42-42 18.804-42 42-42zm56 254c0 6.627-5.373 12-12 12h-88c-6.627 0-12-5.373-12-12v-24c0-6.627 5.373-12 12-12h12v-64h-12c-6.627 0-12-5.373-12-12v-24c0-6.627 5.373-12 12-12h64c6.627 0 12 5.373 12 12v100h12c6.627 0 12 5.373 12 12v24z"></path></svg><!-- <i class="fas fa-info-circle"></i> --> <strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Observação:</font></font></strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> a ordem das tags </font></font><code>em</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> e </font></font><code>strong</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> pode ser invertida dependendo do processador Markdown que você usa. 39;está usando.
</font></font></div>

<h4 id="bold-and-italic-best-practices"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Práticas recomendadas para negrito e itálico</font></font><a class="anchorjs-link " aria-label="Âncora" data-anchorjs-icon="" href="#bold-and-italic-best-practices" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h4>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Os aplicativos Markdown não concordam sobre como lidar com sublinhados no meio de uma palavra. Para compatibilidade, use asteriscos para negrito e itálico no meio de uma palavra para dar ênfase.</font></font></p>

<table class="table table-bordered">
  <thead class="thead-light">
    <tr>
      <th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">✅&nbsp; Faça isso</font></font></th>
      <th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">❌&nbsp; Não faça isso</font></font></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <code class="highlighter-rouge">
          This is really***very***important text.
        </code>
      </td>
      <td>
        <code class="highlighter-rouge">
          This is really___very___important text.
        </code>
      </td>
    </tr>
  </tbody>
</table>

## Citações em bloco

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Para criar uma citação em bloco, adicione um </font></font><code class="language-plaintext highlighter-rouge">&gt;</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> antes de um parágrafo.</font></font></p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>&gt; Dorothy followed her through many of the beautiful rooms in her castle.
</code></pre></div></div>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">A saída renderizada fica assim:</font></font></p>

<blockquote>
  <p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Dorothy a seguiu por muitos dos belos quartos de seu castelo.</font></font></p>
</blockquote>

<h3 id="blockquotes-with-multiple-paragraphs"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Citações em bloco com vários parágrafos</font></font><a class="anchorjs-link " aria-label="Âncora" data-anchorjs-icon="" href="#blockquotes-with-multiple-paragraphs" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h3>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Aspas em bloco podem conter vários parágrafos. Adicione um </font></font><code class="language-plaintext highlighter-rouge">&gt;</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> nas linhas em branco entre os parágrafos.</font></font></p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>&gt; Dorothy followed her through many of the beautiful rooms in her castle.<font></font>
&gt;<font></font>
&gt; The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood.<font></font>
</code></pre></div></div>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">A saída renderizada fica assim:</font></font></p>

<blockquote>
  <p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Dorothy a seguiu por muitos dos belos quartos de seu castelo.</font></font></p>

  <p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">A Bruxa ordenou-lhe que limpasse as panelas e as chaleiras, varresse o chão e mantivesse o fogo alimentado com lenha.</font></font></p>
</blockquote>

<h3 id="nested-blockquotes"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Citações aninhadas</font></font><a class="anchorjs-link " aria-label="Âncora" data-anchorjs-icon="" href="#nested-blockquotes" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h3>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Aspas em bloco podem ser aninhadas. Adicione um </font></font><code class="language-plaintext highlighter-rouge">&gt;&gt;</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> antes do parágrafo que você deseja aninhar.</font></font></p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>&gt; Dorothy followed her through many of the beautiful rooms in her castle.<font></font>
&gt;<font></font>
&gt;&gt; The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood.<font></font>
</code></pre></div></div>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">A saída renderizada fica assim:</font></font></p>

<blockquote>
  <p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Dorothy a seguiu por muitos dos belos quartos de seu castelo.</font></font></p>

  <blockquote>
    <p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">A Bruxa ordenou-lhe que limpasse as panelas e as chaleiras, varresse o chão e mantivesse o fogo alimentado com lenha.</font></font></p>
  </blockquote>
</blockquote>

<h3 id="blockquotes-with-other-elements"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Blockquotes com outros elementos</font></font><a class="anchorjs-link " aria-label="Âncora" data-anchorjs-icon="" href="#blockquotes-with-other-elements" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h3>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Blockquotes podem conter outros elementos formatados em Markdown. Nem todos os elementos podem ser usados ​​– você precisará experimentar para ver quais funcionam.</font></font></p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>&gt; #### The quarterly results look great!<font></font>
&gt;<font></font>
&gt; - Revenue was off the chart.<font></font>
&gt; - Profits were higher than ever.<font></font>
&gt;<font></font>
&gt;  *Everything* is going according to **plan**.<font></font>
</code></pre></div></div>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">A saída renderizada fica assim:</font></font></p>

<blockquote>
  <h4 class="no-anchor" id="the-quarterly-results-look-great"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Os resultados trimestrais parecem ótimos!</font></font></h4>

  <ul>
    <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">A receita estava fora do gráfico.</font></font></li>
    <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Os lucros foram maiores do que nunca.</font></font></li>
  </ul>

  <p><em><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Tudo</font></font></em><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> está indo de acordo com o </font></font><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">planejado</font></font></strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">.</font></font></p>
</blockquote>

<h3 id="blockquotes-best-practices"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Práticas recomendadas para citações em bloco</font></font><a class="anchorjs-link " aria-label="Âncora" data-anchorjs-icon="" href="#blockquotes-best-practices" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h3>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Para compatibilidade, coloque linhas em branco antes e depois das aspas.</font></font></p>

<table class="table table-bordered">
  <thead class="thead-light">
    <tr>
      <th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">✅&nbsp; Faça isso</font></font></th>
      <th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">❌&nbsp; Não faça isso</font></font></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <code class="highlighter-rouge">
        Try to put a blank line before...<br><br>

        &gt; This is a blockquote<br><br>

        ...and after a blockquote.
        </code>
      </td>
      <td>
        <code class="highlighter-rouge">
        Without blank lines, this might not look right.<br>
        &gt; This is a blockquote<br>
        Don't do this!
        </code>
      </td>
    </tr>
  </tbody>
</table>

## Listas

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Você pode organizar itens em listas ordenadas e não ordenadas.</font></font></p>

<h3 id="ordered-lists"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Listas ordenadas</font></font><a class="anchorjs-link " aria-label="Âncora" data-anchorjs-icon="" href="#ordered-lists" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h3>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Para criar uma lista ordenada, adicione itens de linha com números seguidos de pontos. Os números não precisam estar em ordem numérica, mas a lista deve começar com o número um.</font></font></p>

<table class="table table-bordered">
  <thead class="thead-light">
    <tr>
      <th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Remarcação</font></font></th>
      <th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">HTML</font></font></th>
      <th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Saída renderizada</font></font></th>
    </tr>
  </thead>
  <tbody>
  <tr>
    <td>
      <code class="highlighter-rouge">
        1. First item<br>
        2. Second item<br>
        3. Third item<br>
        4. Fourth item
      </code>
    </td>
    <td>
      <code class="highlighter-rouge">
        &lt;ol&gt;<br>
          &nbsp;&nbsp;&lt;li&gt;First item&lt;/li&gt;<br>
          &nbsp;&nbsp;&lt;li&gt;Second item&lt;/li&gt;<br>
          &nbsp;&nbsp;&lt;li&gt;Third item&lt;/li&gt;<br>
          &nbsp;&nbsp;&lt;li&gt;Fourth item&lt;/li&gt;<br>
        &lt;/ol&gt;
      </code>
    </td>
    <td>
      <ol>
        <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Primeiro item</font></font></li>
        <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Segundo item</font></font></li>
        <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Terceiro item</font></font></li>
        <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Quarto item</font></font></li>
      </ol>
    </td>
    </tr>
    <tr>
      <td>
        <code class="highlighter-rouge">
          1. First item<br>
          1. Second item<br>
          1. Third item<br>
          1. Fourth item
        </code>
      </td>
      <td>
        <code class="highlighter-rouge">
          &lt;ol&gt;<br>
            &nbsp;&nbsp;&lt;li&gt;First item&lt;/li&gt;<br>
            &nbsp;&nbsp;&lt;li&gt;Second item&lt;/li&gt;<br>
            &nbsp;&nbsp;&lt;li&gt;Third item&lt;/li&gt;<br>
            &nbsp;&nbsp;&lt;li&gt;Fourth item&lt;/li&gt;<br>
          &lt;/ol&gt;
        </code>
      </td>
      <td>
        <ol>
          <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Primeiro item</font></font></li>
          <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Segundo item</font></font></li>
          <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Terceiro item</font></font></li>
          <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Quarto item</font></font></li>
        </ol>
      </td>
    </tr>
    <tr>
      <td>
        <code class="highlighter-rouge">
          1. First item<br>
          8. Second item<br>
          3. Third item<br>
          5. Fourth item
        </code>
      </td>
      <td>
        <code class="highlighter-rouge">
          &lt;ol&gt;<br>
            &nbsp;&nbsp;&lt;li&gt;First item&lt;/li&gt;<br>
            &nbsp;&nbsp;&lt;li&gt;Second item&lt;/li&gt;<br>
            &nbsp;&nbsp;&lt;li&gt;Third item&lt;/li&gt;<br>
            &nbsp;&nbsp;&lt;li&gt;Fourth item&lt;/li&gt;<br>
          &lt;/ol&gt;
        </code>
      </td>
      <td>
        <ol>
          <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Primeiro item</font></font></li>
          <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Segundo item</font></font></li>
          <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Terceiro item</font></font></li>
          <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Quarto item</font></font></li>
        </ol>
      </td>
    </tr>
    <tr>
      <td>
        <code class="highlighter-rouge">
          1. First item<br>
          2. Second item<br>
          3. Third item<br>
          &nbsp;&nbsp;&nbsp;&nbsp;1. Indented item<br>
          &nbsp;&nbsp;&nbsp;&nbsp;2. Indented item<br>
          4. Fourth item
        </code>
      </td>
      <td>
        <code class="highlighter-rouge">
          &lt;ol&gt;<br>
            &nbsp;&nbsp;&lt;li&gt;First item&lt;/li&gt;<br>
            &nbsp;&nbsp;&lt;li&gt;Second item&lt;/li&gt;<br>
            &nbsp;&nbsp;&lt;li&gt;Third item<br>
              &nbsp;&nbsp;&nbsp;&nbsp;&lt;ol&gt;<br>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;li&gt;Indented item&lt;/li&gt;<br>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;li&gt;Indented item&lt;/li&gt;<br>
              &nbsp;&nbsp;&nbsp;&nbsp;&lt;/ol&gt;<br>
            &nbsp;&nbsp;&lt;/li&gt;<br>
            &nbsp;&nbsp;&lt;li&gt;Fourth item&lt;/li&gt;<br>
          &lt;/ol&gt;
        </code>
      </td>
      <td>
        <ol>
          <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Primeiro item</font></font></li>
          <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Segundo item</font></font></li>
          <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Terceiro item
            </font></font><ol>
              <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Item recuado</font></font></li>
              <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Item recuado</font></font></li>
            </ol>
          </li>
          <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Quarto item</font></font></li>
        </ol>
      </td>
    </tr>
  </tbody>
</table>

<h4 id="ordered-list-best-practices"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Melhores práticas de lista ordenada</font></font><a class="anchorjs-link " aria-label="Âncora" data-anchorjs-icon="" href="#ordered-list-best-practices" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h4>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">CommonMark e algumas outras linguagens de marcação leves permitem usar parênteses (</font></font><code class="language-plaintext highlighter-rouge">)</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">) como delimitador (por exemplo, </font></font><code class="language-plaintext highlighter-rouge">1) First item</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">), mas nem todo Markdown os aplicativos suportam isso, portanto não é uma ótima opção do ponto de vista de compatibilidade. Para fins de compatibilidade, use apenas pontos.</font></font></p>

<table class="table table-bordered">
  <thead class="thead-light">
    <tr>
      <th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">✅&nbsp; Faça isso</font></font></th>
      <th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">❌&nbsp; Não faça isso</font></font></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <code class="highlighter-rouge">
          1. First item<br>
          2. Second item
        </code>
      </td>
      <td>
        <code class="highlighter-rouge">
          1) First item<br>
          2) Second item
        </code>
      </td>
    </tr>
  </tbody>
</table>

<h3 id="unordered-lists"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Listas não ordenadas</font></font><a class="anchorjs-link " aria-label="Âncora" data-anchorjs-icon="" href="#unordered-lists" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h3>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Para criar uma lista não ordenada, adicione travessões (</font></font><code class="language-plaintext highlighter-rouge">-</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">), asteriscos (</font></font><code class="language-plaintext highlighter-rouge">*</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">) ou sinais de mais (</font></font><code class="language-plaintext highlighter-rouge">+</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">) na frente dos itens de linha. Recue um ou mais itens para criar uma lista aninhada.</font></font></p>

<table class="table table-bordered">
  <thead class="thead-light">
    <tr>
      <th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Remarcação</font></font></th>
      <th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">HTML</font></font></th>
      <th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Saída renderizada</font></font></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <code class="highlighter-rouge">
          - First item<br>
          - Second item<br>
          - Third item<br>
          - Fourth item
        </code>
      </td>
      <td>
        <code class="highlighter-rouge">
          &lt;ul&gt;<br>
            &nbsp;&nbsp;&lt;li&gt;First item&lt;/li&gt;<br>
            &nbsp;&nbsp;&lt;li&gt;Second item&lt;/li&gt;<br>
            &nbsp;&nbsp;&lt;li&gt;Third item&lt;/li&gt;<br>
            &nbsp;&nbsp;&lt;li&gt;Fourth item&lt;/li&gt;<br>
          &lt;/ul&gt;
        </code>
      </td>
      <td>
        <ul>
          <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Primeiro item</font></font></li>
          <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Segundo item</font></font></li>
          <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Terceiro item</font></font></li>
          <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Quarto item</font></font></li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>
        <code class="highlighter-rouge">
          * First item<br>
          * Second item<br>
          * Third item<br>
          * Fourth item
        </code>
      </td>
      <td>
        <code class="highlighter-rouge">
          &lt;ul&gt;<br>
            &nbsp;&nbsp;&lt;li&gt;First item&lt;/li&gt;<br>
            &nbsp;&nbsp;&lt;li&gt;Second item&lt;/li&gt;<br>
            &nbsp;&nbsp;&lt;li&gt;Third item&lt;/li&gt;<br>
            &nbsp;&nbsp;&lt;li&gt;Fourth item&lt;/li&gt;<br>
          &lt;/ul&gt;
        </code>
      </td>
      <td>
        <ul>
          <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Primeiro item</font></font></li>
          <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Segundo item</font></font></li>
          <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Terceiro item</font></font></li>
          <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Quarto item</font></font></li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>
        <code class="highlighter-rouge">
          + First item<br>
          + Second item<br>
          + Third item<br>
          + Fourth item
        </code>
      </td>
      <td>
        <code class="highlighter-rouge">
          &lt;ul&gt;<br>
            &nbsp;&nbsp;&lt;li&gt;First item&lt;/li&gt;<br>
            &nbsp;&nbsp;&lt;li&gt;Second item&lt;/li&gt;<br>
            &nbsp;&nbsp;&lt;li&gt;Third item&lt;/li&gt;<br>
            &nbsp;&nbsp;&lt;li&gt;Fourth item&lt;/li&gt;<br>
          &lt;/ul&gt;
        </code>
      </td>
      <td>
        <ul>
          <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Primeiro item</font></font></li>
          <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Segundo item</font></font></li>
          <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Terceiro item</font></font></li>
          <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Quarto item</font></font></li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>
        <code class="highlighter-rouge">
          - First item<br>
          - Second item<br>
          - Third item<br>
          &nbsp;&nbsp;&nbsp;&nbsp;- Indented item<br>
          &nbsp;&nbsp;&nbsp;&nbsp;- Indented item<br>
          - Fourth item
        </code>
      </td>
      <td>
        <code class="highlighter-rouge">
          &lt;ul&gt;<br>
            &nbsp;&nbsp;&lt;li&gt;First item&lt;/li&gt;<br>
            &nbsp;&nbsp;&lt;li&gt;Second item&lt;/li&gt;<br>
            &nbsp;&nbsp;&lt;li&gt;Third item<br>
              &nbsp;&nbsp;&nbsp;&nbsp;&lt;ul&gt;<br>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;li&gt;Indented item&lt;/li&gt;<br>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;li&gt;Indented item&lt;/li&gt;<br>
              &nbsp;&nbsp;&nbsp;&nbsp;&lt;/ul&gt;<br>
            &nbsp;&nbsp;&lt;/li&gt;<br>
            &nbsp;&nbsp;&lt;li&gt;Fourth item&lt;/li&gt;<br>
          &lt;/ul&gt;
        </code>
      </td>
      <td>
        <ul>
          <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Primeiro item</font></font></li>
          <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Segundo item</font></font></li>
          <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Terceiro item
            </font></font><ul>
              <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Item recuado</font></font></li>
              <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Item recuado</font></font></li>
            </ul>
          </li>
          <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Quarto item</font></font></li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

<h4 id="starting-unordered-list-items-with-numbers"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Iniciando itens de lista não ordenados com números</font></font><a class="anchorjs-link " aria-label="Âncora" data-anchorjs-icon="" href="#starting-unordered-list-items-with-numbers" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h4>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Se precisar iniciar um item de lista não ordenado com um número seguido de um ponto final, você pode usar uma barra invertida (</font></font><code class="language-plaintext highlighter-rouge">\</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">) para </font></font><a href="#escaping-characters"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">escapar&lt; /span&gt;</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> o ponto final.</font></font></p>

<table class="table table-bordered">
  <thead class="thead-light">
    <tr>
      <th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Remarcação</font></font></th>
      <th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">HTML</font></font></th>
      <th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Saída renderizada</font></font></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <code class="highlighter-rouge">
          - 1968\. A great year!<br>
          - I think 1969 was second best.
        </code>
      </td>
      <td>
        <code class="highlighter-rouge">
          &lt;ul&gt;<br>
            &nbsp;&nbsp;&lt;li&gt;1968. A great year!&lt;/li&gt;<br>
            &nbsp;&nbsp;&lt;li&gt;I think 1969 was second best.&lt;/li&gt;<br>
          &lt;/ul&gt;
        </code>
      </td>
      <td>
        <ul>
          <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">1968. Um ótimo ano!</font></font></li>
          <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Acho que 1969 foi o segundo melhor.</font></font></li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

<h4 id="unordered-list-best-practices"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Práticas recomendadas para lista não ordenada</font></font><a class="anchorjs-link " aria-label="Âncora" data-anchorjs-icon="" href="#unordered-list-best-practices" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h4>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Os aplicativos Markdown não concordam sobre como lidar com diferentes delimitadores na mesma lista. Para compatibilidade, não misture e combine delimitadores na mesma lista – escolha um e mantenha-o.</font></font></p>

<table class="table table-bordered">
  <thead class="thead-light">
    <tr>
      <th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">✅&nbsp; Faça isso</font></font></th>
      <th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">❌&nbsp; Não faça isso</font></font></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <code class="highlighter-rouge">
          - First item<br>
          - Second item<br>
          - Third item<br>
          - Fourth item
        </code>
      </td>
      <td>
        <code class="highlighter-rouge">
          + First item<br>
          * Second item<br>
          - Third item<br>
          + Fourth item
        </code>
      </td>
    </tr>
  </tbody>
</table>

<h3 id="adding-elements-in-lists"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Adicionando Elementos em Listas</font></font><a class="anchorjs-link " aria-label="Âncora" data-anchorjs-icon="" href="#adding-elements-in-lists" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h3>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Para adicionar outro elemento a uma lista preservando a continuidade da lista, recue o elemento com quatro espaços ou uma tabulação, conforme mostrado nos exemplos a seguir.</font></font></p>

<div class="alert alert-success">
  <svg class="svg-inline--fa fa-lightbulb fa-w-11" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="lightbulb" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 352 512" data-fa-i2svg=""><path fill="currentColor" d="M96.06 454.35c.01 6.29 1.87 12.45 5.36 17.69l17.09 25.69a31.99 31.99 0 0 0 26.64 14.28h61.71a31.99 31.99 0 0 0 26.64-14.28l17.09-25.69a31.989 31.989 0 0 0 5.36-17.69l.04-38.35H96.01l.05 38.35zM0 176c0 44.37 16.45 84.85 43.56 115.78 16.52 18.85 42.36 58.23 52.21 91.45.04.26.07.52.11.78h160.24c.04-.26.07-.51.11-.78 9.85-33.22 35.69-72.6 52.21-91.45C335.55 260.85 352 220.37 352 176 352 78.61 272.91-.3 175.45 0 73.44.31 0 82.97 0 176zm176-80c-44.11 0-80 35.89-80 80 0 8.84-7.16 16-16 16s-16-7.16-16-16c0-61.76 50.24-112 112-112 8.84 0 16 7.16 16 16s-7.16 16-16 16z"></path></svg><!-- <i class="fas fa-lightbulb"></i> --> <strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Dica:</font></font></strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> se as coisas não aparecerem como você espera, verifique se você recuou os elementos da lista com quatro espaços ou uma tabulação.
</font></font></div>

<h4 id="paragraphs"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Parágrafos</font></font><a class="anchorjs-link " aria-label="Âncora" data-anchorjs-icon="" href="#paragraphs" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h4>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>* This is the first list item.<font></font>
* Here's the second list item.<font></font>
<font></font>
    I need to add another paragraph below the second list item.<font></font>
<font></font>
* And here's the third list item.<font></font>
</code></pre></div></div>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">A saída renderizada fica assim:</font></font></p>

<ul>
  <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Este é o primeiro item da lista.</font></font></li>
  <li>
    <p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Aqui está o segundo item da lista.</font></font></p>

    <p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Preciso adicionar outro parágrafo abaixo do segundo item da lista.</font></font></p>
  </li>
  <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">E aqui está o terceiro item da lista.</font></font></li>
</ul>

<h4 id="blockquotes"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Citações em bloco</font></font><a class="anchorjs-link " aria-label="Âncora" data-anchorjs-icon="" href="#blockquotes" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h4>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>* This is the first list item.<font></font>
* Here's the second list item.<font></font>
<font></font>
    &gt; A blockquote would look great below the second list item.<font></font>
<font></font>
* And here's the third list item.<font></font>
</code></pre></div></div>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">A saída renderizada fica assim:</font></font></p>

<ul>
  <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Este é o primeiro item da lista.</font></font></li>
  <li>
    <p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Aqui está o segundo item da lista.</font></font></p>

    <blockquote>
      <p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Uma citação em bloco ficaria ótima abaixo do segundo item da lista.</font></font></p>
    </blockquote>
  </li>
  <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">E aqui está o terceiro item da lista.</font></font></li>
</ul>

<h4 id="code-blocks-1"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Blocos de código</font></font><a class="anchorjs-link " aria-label="Âncora" data-anchorjs-icon="" href="#code-blocks-1" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h4>

<p><a href="#code-blocks"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Blocos de código</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> normalmente são recuados com quatro espaços ou uma tabulação. Quando estiverem em uma lista, recue-os com oito espaços ou duas tabulações.</font></font></p>

<div class="language-text highlighter-rouge"><div class="highlight"><pre class="highlight"><code>1. Open the file.<font></font>
2. Find the following code block on line 21:<font></font>
<font></font>
        &lt;html&gt;<font></font>
          &lt;head&gt;<font></font>
            &lt;title&gt;Test&lt;/title&gt;<font></font>
          &lt;/head&gt;<font></font>
<font></font>
3. Update the title to match the name of your website.<font></font>
</code></pre></div></div>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">A saída renderizada fica assim:</font></font></p>

<ol>
  <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Abra o arquivo.</font></font></li>
  <li>
    <p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Encontre o seguinte bloco de código na linha 21:</font></font></p>

    <div class="language-text highlighter-rouge"><div class="highlight"><pre class="highlight"><code> &lt;html&gt;<font></font>
   &lt;head&gt;<font></font>
     &lt;title&gt;Test&lt;/title&gt;<font></font>
   &lt;/head&gt;<font></font>
</code></pre></div>    </div>
  </li>
  <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Atualize o título para corresponder ao nome do seu site.</font></font></li>
</ol>

<h4 id="images"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Imagens</font></font><a class="anchorjs-link " aria-label="Âncora" data-anchorjs-icon="" href="#images" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h4>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>1. Open the file containing the Linux mascot.<font></font>
2. Marvel at its beauty.<font></font>
<font></font>
    ![Tux, the Linux mascot](/assets/images/tux.png)<font></font>
<font></font>
3. Close the file.<font></font>
</code></pre></div></div>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">A saída renderizada fica assim:</font></font></p>

<ol>
  <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Abra o arquivo que contém o mascote do Linux.</font></font></li>
  <li>
    <p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Maravilhe-se com sua beleza.</font></font></p>

    <p><img srcset="https://mdg.imgix.net/assets/images/tux.png?auto=format&amp;fit=clip&amp;w=100 480w,           https://mdg.imgix.net/assets/images/tux.png?auto=format&amp;fit=clip&amp;q=40&amp;w=100 1080w" src="https://mdg.imgix.net/assets/images/tux.png" class="img-fluid" alt="Tux, o mascote do Linux" loading="lazy" sizes="100vw"></p>
  </li>
  <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Feche o arquivo.</font></font></li>
</ol>

<h4 id="lists"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Listas</font></font><a class="anchorjs-link " aria-label="Âncora" data-anchorjs-icon="" href="#lists" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h4>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Você pode aninhar uma lista não ordenada em uma lista ordenada ou vice-versa.</font></font></p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>1. First item<font></font>
2. Second item<font></font>
3. Third item<font></font>
    - Indented item<font></font>
    - Indented item<font></font>
4. Fourth item<font></font>
</code></pre></div></div>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">A saída renderizada fica assim:</font></font></p>

<ol>
  <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Primeiro item</font></font></li>
  <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Segundo item</font></font></li>
  <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Terceiro item
    </font></font><ul>
      <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Item recuado</font></font></li>
      <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Item recuado</font></font></li>
    </ul>
  </li>
  <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Quarto item</font></font></li>
</ol>

## Código

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Para denotar uma palavra ou frase como código, coloque-a entre crases (</font></font><code class="language-plaintext highlighter-rouge">`</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">).</font></font></p>

<table class="table table-bordered">
  <thead class="thead-light">
    <tr>
      <th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Remarcação</font></font></th>
      <th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">HTML</font></font></th>
      <th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Saída renderizada</font></font></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code class="highlighter-rouge">At the command prompt, type `nano`.</code></td>
      <td><code class="highlighter-rouge">At the command prompt, type &lt;code&gt;nano&lt;/code&gt;. </code></td>
      <td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">No prompt de comando, digite </font></font><code class="highlighter-rouge">nano</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">.</font></font></td>
    </tr>
  </tbody>
</table>

<h3 id="escaping-backticks"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Escapando de crases</font></font><a class="anchorjs-link " aria-label="Âncora" data-anchorjs-icon="" href="#escaping-backticks" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h3>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Se a palavra ou frase que você deseja denotar como código incluir um ou mais crases, você poderá escapar dela colocando a palavra ou frase entre crases duplos (</font></font><code>``</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">).</font></font></p>

<table class="table table-bordered">
  <thead class="thead-light">
    <tr>
      <th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Remarcação</font></font></th>
      <th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">HTML</font></font></th>
      <th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Saída renderizada</font></font></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>``Use `code` in your Markdown file.``</code></td>
      <td><code class="highlighter-rouge">&lt;code&gt;Use `code` in your Markdown file.&lt;/code&gt;</code></td>
      <td><code>Use `code` in your Markdown file.</code></td>
    </tr>
  </tbody>
</table>

<h3 id="code-blocks"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Blocos de código</font></font><a class="anchorjs-link " aria-label="Âncora" data-anchorjs-icon="" href="#code-blocks" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h3>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Para criar blocos de código, recue cada linha do bloco com pelo menos quatro espaços ou uma tabulação.</font></font></p>

<div class="language-text highlighter-rouge"><div class="highlight"><pre class="highlight"><code>    &lt;html&gt;<font></font>
      &lt;head&gt;<font></font>
      &lt;/head&gt;<font></font>
    &lt;/html&gt;<font></font>
</code></pre></div></div>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">A saída renderizada fica assim:</font></font></p>

<div class="language-text highlighter-rouge"><div class="highlight"><pre class="highlight"><code>&lt;html&gt;<font></font>
  &lt;head&gt;<font></font>
  &lt;/head&gt;<font></font>
&lt;/html&gt;<font></font>
</code></pre></div></div>

<div class="alert alert-info">
  <svg class="svg-inline--fa fa-info-circle fa-w-16" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="info-circle" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" data-fa-i2svg=""><path fill="currentColor" d="M256 8C119.043 8 8 119.083 8 256c0 136.997 111.043 248 248 248s248-111.003 248-248C504 119.083 392.957 8 256 8zm0 110c23.196 0 42 18.804 42 42s-18.804 42-42 42-42-18.804-42-42 18.804-42 42-42zm56 254c0 6.627-5.373 12-12 12h-88c-6.627 0-12-5.373-12-12v-24c0-6.627 5.373-12 12-12h12v-64h-12c-6.627 0-12-5.373-12-12v-24c0-6.627 5.373-12 12-12h64c6.627 0 12 5.373 12 12v100h12c6.627 0 12 5.373 12 12v24z"></path></svg><!-- <i class="fas fa-info-circle"></i> --> <strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Observação:</font></font></strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> para criar blocos de código sem recuo de linhas, use </font></font><a href="/extended-syntax/#fenced-code-blocks"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">blocos de código protegidos</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">.
</font></font></div>

## Regras horizontais

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Para criar uma regra horizontal, use três ou mais asteriscos (</font></font><code class="language-plaintext highlighter-rouge">***</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">), travessões (</font></font><code class="language-plaintext highlighter-rouge">---</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">) ou sublinhados (</font></font><code class="language-plaintext highlighter-rouge">___</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">) em uma linha sozinhos.</font></font></p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>***<font></font>
<font></font>
---<font></font>
<font></font>
_________________<font></font>
</code></pre></div></div>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">A saída renderizada de todos os três parece idêntica:</font></font></p>

<hr>

<h3 id="horizontal-rule-best-practices"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Práticas recomendadas para regras horizontais</font></font><a class="anchorjs-link " aria-label="Âncora" data-anchorjs-icon="" href="#horizontal-rule-best-practices" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h3>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Para compatibilidade, coloque linhas em branco antes e depois das réguas horizontais.</font></font></p>

<table class="table table-bordered">
  <thead class="thead-light">
    <tr>
      <th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">✅&nbsp; Faça isso</font></font></th>
      <th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">❌&nbsp; Não faça isso</font></font></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <code class="highlighter-rouge">
        Try to put a blank line before...<br><br>

        ---<br><br>

        ...and after a horizontal rule.
        </code>
      </td>
      <td>
        <code class="highlighter-rouge">
        Without blank lines, this would be a heading.<br>
        ---<br>
        Don't do this!
        </code>
      </td>
    </tr>
  </tbody>
</table>

## Ligações

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Para criar um link, coloque o texto do link entre colchetes (por exemplo, </font></font><code class="language-plaintext highlighter-rouge">[Duck Duck Go]</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">) e siga-o imediatamente com o URL entre parênteses (por exemplo, </font></font><code class="language-plaintext highlighter-rouge">(https://duckduckgo.com)</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">).</font></font></p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>My favorite search engine is [Duck Duck Go](https://duckduckgo.com).
</code></pre></div></div>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">A saída renderizada fica assim:</font></font></p>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Meu mecanismo de pesquisa favorito é </font></font><a href="https://duckduckgo.com"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Duck Duck Go</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">.</font></font></p>

<div class="alert alert-info">
  <svg class="svg-inline--fa fa-info-circle fa-w-16" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="info-circle" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" data-fa-i2svg=""><path fill="currentColor" d="M256 8C119.043 8 8 119.083 8 256c0 136.997 111.043 248 248 248s248-111.003 248-248C504 119.083 392.957 8 256 8zm0 110c23.196 0 42 18.804 42 42s-18.804 42-42 42-42-18.804-42-42 18.804-42 42-42zm56 254c0 6.627-5.373 12-12 12h-88c-6.627 0-12-5.373-12-12v-24c0-6.627 5.373-12 12-12h12v-64h-12c-6.627 0-12-5.373-12-12v-24c0-6.627 5.373-12 12-12h64c6.627 0 12 5.373 12 12v100h12c6.627 0 12 5.373 12 12v24z"></path></svg><!-- <i class="fas fa-info-circle"></i> --> <strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Observação:</font></font></strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> para vincular a um elemento na mesma página, consulte </font></font><a href="/extended-syntax/#linking-to-heading-ids"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">vincular a IDs de cabeçalho</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">. Para criar um link que abre em uma nova guia ou janela, consulte a seção sobre </font></font><a href="/hacks/#link-targets"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">destinos de link</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">.
</font></font></div>

<h3 id="adding-titles"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Adicionando títulos</font></font><a class="anchorjs-link " aria-label="Âncora" data-anchorjs-icon="" href="#adding-titles" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h3>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Opcionalmente, você pode adicionar um título para um link. Isso aparecerá como uma dica quando o usuário passar o mouse sobre o link. Para adicionar um título, coloque-o entre aspas após o URL.</font></font></p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>My favorite search engine is [Duck Duck Go](https://duckduckgo.com "The best search engine for privacy").
</code></pre></div></div>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">A saída renderizada fica assim:</font></font></p>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Meu mecanismo de pesquisa favorito é </font></font><a href="https://duckduckgo.com" title="O melhor mecanismo de busca para privacidade"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Duck Duck Go</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">.</font></font></p>

<h3 id="urls-and-email-addresses"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">URLs e endereços de e-mail</font></font><a class="anchorjs-link " aria-label="Âncora" data-anchorjs-icon="" href="#urls-and-email-addresses" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h3>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Para transformar rapidamente um URL ou endereço de e-mail em um link, coloque-o entre colchetes angulares.</font></font></p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>&lt;https://www.markdownguide.org&gt;<font></font>
&lt;fake@example.com&gt;<font></font>
</code></pre></div></div>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">A saída renderizada fica assim:</font></font></p>

<p><a href="https://www.markdownguide.org"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">https://www.markdownguide.org</font></font></a><br>
<a href="mailto:fake@example.com"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">fake@example.com</font></font></a></p>

<h3 id="formatting-links"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Formatando links</font></font><a class="anchorjs-link " aria-label="Âncora" data-anchorjs-icon="" href="#formatting-links" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h3>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Para </font></font><a href="#emphasis"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">enfatizar</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> links, adicione asteriscos antes e depois dos colchetes e parênteses. Para denotar links como </font></font><a href="#code"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">código</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">, adicione crases entre colchetes.</font></font></p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>I love supporting the **[EFF](https://eff.org)**.<font></font>
This is the *[Markdown Guide](https://www.markdownguide.org)*.<font></font>
See the section on [`code`](#code).<font></font>
</code></pre></div></div>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">A saída renderizada fica assim:</font></font></p>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Adoro apoiar a </font></font><strong><a href="https://eff.org"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">EFF</font></font></a></strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">.</font></font><br><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
Este é o </font></font><em><a href="https://www.markdownguide.org"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Guia de descontos</font></font></a></em><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">.</font></font><br><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
Consulte a seção sobre </font></font><a href="#code"><code class="language-plaintext highlighter-rouge">code</code></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">.</font></font></p>

<h3 id="reference-style-links"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Links de estilo de referência</font></font><a class="anchorjs-link " aria-label="Âncora" data-anchorjs-icon="" href="#reference-style-links" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h3>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Links de estilo de referência são um tipo especial de link que torna os URLs mais fáceis de exibir e ler no Markdown. Os links de estilo de referência são construídos em duas partes: a parte que você mantém alinhada ao seu texto e a parte que você armazena em outro lugar do arquivo para manter o texto fácil de ler.</font></font></p>

<h4 id="formatting-the-first-part-of-the-link"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Formatando a primeira parte do link</font></font><a class="anchorjs-link " aria-label="Âncora" data-anchorjs-icon="" href="#formatting-the-first-part-of-the-link" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h4>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">A primeira parte de um link de estilo de referência é formatada com dois conjuntos de colchetes. O primeiro conjunto de colchetes circunda o texto que deve aparecer vinculado. O segundo conjunto de colchetes exibe um rótulo usado para apontar para o link que você está armazenando em outro lugar do documento.</font></font></p>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Embora não seja obrigatório, você pode incluir um espaço entre o primeiro e o segundo conjunto de colchetes. O rótulo no segundo conjunto de colchetes não diferencia maiúsculas de minúsculas e pode incluir letras, números, espaços ou pontuação.</font></font></p>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Isso significa que os seguintes formatos de exemplo são aproximadamente equivalentes para a primeira parte do link:</font></font></p>

<ul>
  <li><code class="language-plaintext highlighter-rouge">[hobbit-hole][1]</code></li>
  <li><code class="language-plaintext highlighter-rouge">[hobbit-hole] [1]</code></li>
</ul>

<h4 id="formatting-the-second-part-of-the-link"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Formatando a segunda parte do link</font></font><a class="anchorjs-link " aria-label="Âncora" data-anchorjs-icon="" href="#formatting-the-second-part-of-the-link" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h4>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">A segunda parte de um link de estilo de referência é formatada com os seguintes atributos:</font></font></p>

<ol>
  <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">O rótulo, entre colchetes, seguido imediatamente por dois pontos e pelo menos um espaço (por exemplo, </font></font><code class="language-plaintext highlighter-rouge">[label]: </code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">).</font></font></li>
  <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">O URL do link, que você pode colocar opcionalmente entre colchetes angulares.</font></font></li>
  <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">O título opcional do link, que você pode colocar entre aspas duplas, aspas simples ou parênteses.</font></font></li>
</ol>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Isso significa que os formatos de exemplo a seguir são aproximadamente equivalentes para a segunda parte do link:</font></font></p>

<ul>
  <li><code class="language-plaintext highlighter-rouge">[1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle</code></li>
  <li><code class="language-plaintext highlighter-rouge">[1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle "Hobbit lifestyles"</code></li>
  <li><code class="language-plaintext highlighter-rouge">[1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle 'Hobbit lifestyles'</code></li>
  <li><code class="language-plaintext highlighter-rouge">[1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle (Hobbit lifestyles)</code></li>
  <li><code class="language-plaintext highlighter-rouge">[1]: &lt;https://en.wikipedia.org/wiki/Hobbit#Lifestyle&gt; "Hobbit lifestyles"</code></li>
  <li><code class="language-plaintext highlighter-rouge">[1]: &lt;https://en.wikipedia.org/wiki/Hobbit#Lifestyle&gt; 'Hobbit lifestyles'</code></li>
  <li><code class="language-plaintext highlighter-rouge">[1]: &lt;https://en.wikipedia.org/wiki/Hobbit#Lifestyle&gt; (Hobbit lifestyles)</code></li>
</ul>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Você pode colocar esta segunda parte do link em qualquer lugar do seu documento Markdown. Algumas pessoas os colocam imediatamente após o parágrafo em que aparecem, enquanto outras os colocam no final do documento (como notas finais ou de rodapé).</font></font></p>

<h4 id="an-example-putting-the-parts-together"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Um exemplo juntando as peças</font></font><a class="anchorjs-link " aria-label="Âncora" data-anchorjs-icon="" href="#an-example-putting-the-parts-together" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h4>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Digamos que você adicione um URL como um </font></font><a href="#links"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">link de URL padrão</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> a um parágrafo e ele ficará assim no Markdown:</font></font></p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>In a hole in the ground there lived a hobbit. Not a nasty, dirty, wet hole, filled with the ends<font></font>
of worms and an oozy smell, nor yet a dry, bare, sandy hole with nothing in it to sit down on or to<font></font>
eat: it was a [hobbit-hole](https://en.wikipedia.org/wiki/Hobbit#Lifestyle "Hobbit lifestyles"), and that means comfort.<font></font>
</code></pre></div></div>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Embora possa apontar para informações adicionais interessantes, o URL exibido realmente não acrescenta muito ao texto bruto existente, a não ser torná-lo mais difícil de ler. Para corrigir isso, você pode formatar o URL assim:</font></font></p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>In a hole in the ground there lived a hobbit. Not a nasty, dirty, wet hole, filled with the ends<font></font>
of worms and an oozy smell, nor yet a dry, bare, sandy hole with nothing in it to sit down on or to<font></font>
eat: it was a [hobbit-hole][1], and that means comfort.<font></font>
<font></font>
[1]: &lt;https://en.wikipedia.org/wiki/Hobbit#Lifestyle&gt; "Hobbit lifestyles"<font></font>
</code></pre></div></div>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Em ambos os casos acima, a saída renderizada seria idêntica:</font></font></p>

<blockquote>
  <p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Em um buraco no chão vivia um hobbit. Não um buraco nojento, sujo e úmido, cheio de pontas de minhocas e com cheiro de lodo, nem ainda um buraco seco, vazio e arenoso, sem nada onde sentar ou comer: era um </font></font><a href="https://en.wikipedia.org/wiki/Hobbit#Lifestyle" title="Estilo de vida dos Hobbits"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">toca do hobbit</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">, e isso significa conforto.</font></font></p>
</blockquote>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">e o HTML do link seria:</font></font></p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>&lt;a href="https://en.wikipedia.org/wiki/Hobbit#Lifestyle" title="Hobbit lifestyles"&gt;hobbit-hole&lt;/a&gt;
</code></pre></div></div>

<h3 id="link-best-practices"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Vincular práticas recomendadas</font></font><a class="anchorjs-link " aria-label="Âncora" data-anchorjs-icon="" href="#link-best-practices" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h3>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Os aplicativos Markdown não concordam sobre como lidar com espaços no meio de um URL. Para compatibilidade, tente codificar em URL quaisquer espaços com </font></font><code class="language-plaintext highlighter-rouge">%20</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">. Como alternativa, se seu aplicativo Markdown </font></font><a href="#html"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">suportar HTML</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">, você poderá usar a tag HTML </font></font><code class="language-plaintext highlighter-rouge">a</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">.</font></font></p>

<table class="table table-bordered">
  <thead class="thead-light">
    <tr>
      <th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">✅&nbsp; Faça isso</font></font></th>
      <th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">❌&nbsp; Não faça isso</font></font></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <code class="highlighter-rouge">
        [link](https://www.example.com/my%20great%20page)<br><br>

        &lt;a href="https://www.example.com/my great page"&gt;link&lt;/a&gt;<br><br>
        </code>
      </td>
      <td>
        <code class="highlighter-rouge">
        [link](https://www.example.com/my great page)<br><br>
        </code>
      </td>
    </tr>
  </tbody>
</table>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Parênteses no meio de uma URL também podem ser problemáticos. Para compatibilidade, tente codificar em URL o parêntese de abertura (</font></font><code class="language-plaintext highlighter-rouge">(</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">) com </font></font><code class="language-plaintext highlighter-rouge">%28</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> e o parêntese de fechamento (</font></font><code class="language-plaintext highlighter-rouge">)</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">) com </font><font style="vertical-align: inherit;">.</font><font style="vertical-align: inherit;">, você poderá usar a tag HTML </font><a href="#html"><font style="vertical-align: inherit;">suportar HTML</font></a></font><code class="language-plaintext highlighter-rouge">%29</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">. Como alternativa, se seu aplicativo Markdown </font></font><a href="#html"><font style="vertical-align: inherit;"></font></a><font style="vertical-align: inherit;"></font><code class="language-plaintext highlighter-rouge">a</code><font style="vertical-align: inherit;"></font></p>

<table class="table table-bordered">
  <thead class="thead-light">
    <tr>
      <th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">✅&nbsp; Faça isso</font></font></th>
      <th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">❌&nbsp; Não faça isso</font></font></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <code class="highlighter-rouge">
        [a novel](https://en.wikipedia.org/wiki/<wbr>The_Milagro_Beanfield_War_%28novel%29)<br><br>

        &lt;a href="https://en.wikipedia.org/wiki/<wbr>The_Milagro_Beanfield_War_(novel)"&gt;a novel&lt;/a&gt;<br><br>
        </code>
      </td>
      <td>
        <code class="highlighter-rouge">
        [a novel](https://en.wikipedia.org/wiki/<wbr>The_Milagro_Beanfield_War_(novel))
        </code>
      </td>
    </tr>
  </tbody>
</table>

## Imagens

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Para adicionar uma imagem, adicione um ponto de exclamação (</font></font><code class="language-plaintext highlighter-rouge">!</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">), seguido de texto alternativo entre colchetes e o caminho ou URL do recurso de imagem entre parênteses. Opcionalmente, você pode adicionar um título entre aspas após o caminho ou URL.</font></font></p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>![The San Juan Mountains are beautiful!](/assets/images/san-juan-mountains.jpg "San Juan Mountains")
</code></pre></div></div>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">A saída renderizada fica assim:</font></font></p>

<p><img srcset="https://mdg.imgix.net/assets/images/san-juan-mountains.jpg?auto=format&amp;fit=clip&amp;w=480 480w,              https://mdg.imgix.net/assets/images/san-juan-mountains.jpg?auto=format&amp;fit=clip&amp;q=40&amp;w=1080 1080w" src="https://mdg.imgix.net/assets/images/san-juan-mountains.jpg" class="img-fluid" title="Montanhas de San Juan" alt="As montanhas de San Juan são lindas!" loading="lazy" sizes="100vw"></p>

<div class="alert alert-info">
  <svg class="svg-inline--fa fa-info-circle fa-w-16" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="info-circle" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" data-fa-i2svg=""><path fill="currentColor" d="M256 8C119.043 8 8 119.083 8 256c0 136.997 111.043 248 248 248s248-111.003 248-248C504 119.083 392.957 8 256 8zm0 110c23.196 0 42 18.804 42 42s-18.804 42-42 42-42-18.804-42-42 18.804-42 42-42zm56 254c0 6.627-5.373 12-12 12h-88c-6.627 0-12-5.373-12-12v-24c0-6.627 5.373-12 12-12h12v-64h-12c-6.627 0-12-5.373-12-12v-24c0-6.627 5.373-12 12-12h64c6.627 0 12 5.373 12 12v100h12c6.627 0 12 5.373 12 12v24z"></path></svg><!-- <i class="fas fa-info-circle"></i> --> <strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Observação:</font></font></strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> para redimensionar uma imagem, consulte a seção sobre </font></font><a href="/hacks/#image-size"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">tamanho da imagem</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">. Para adicionar uma legenda, consulte a seção </font></font><a href="/hacks/#image-captions"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">legendas de imagens</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">.
</font></font></div>

<h3 id="linking-images"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Vinculando imagens</font></font><a class="anchorjs-link " aria-label="Âncora" data-anchorjs-icon="" href="#linking-images" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h3>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Para adicionar um link a uma imagem, coloque o Markdown da imagem entre colchetes e adicione o link entre parênteses.</font></font></p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>[![An old rock in the desert](/assets/images/shiprock.jpg "Shiprock, New Mexico by Beau Rogers")](https://www.flickr.com/photos/beaurogers/31833779864/in/photolist-Qv3rFw-34mt9F-a9Cmfy-5Ha3Zi-9msKdv-o3hgjr-hWpUte-4WMsJ1-KUQ8N-deshUb-vssBD-6CQci6-8AFCiD-zsJWT-nNfsgB-dPDwZJ-bn9JGn-5HtSXY-6CUhAL-a4UTXB-ugPum-KUPSo-fBLNm-6CUmpy-4WMsc9-8a7D3T-83KJev-6CQ2bK-nNusHJ-a78rQH-nw3NvT-7aq2qf-8wwBso-3nNceh-ugSKP-4mh4kh-bbeeqH-a7biME-q3PtTf-brFpgb-cg38zw-bXMZc-nJPELD-f58Lmo-bXMYG-bz8AAi-bxNtNT-bXMYi-bXMY6-bXMYv)
</code></pre></div></div>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">A saída renderizada fica assim:</font></font></p>

<div>
  <a href="https://www.flickr.com/photos/beaurogers/31833779864/in/photolist-Qv3rFw-34mt9F-a9Cmfy-5Ha3Zi-9msKdv-o3hgjr-hWpUte-4WMsJ1-KUQ8N-deshUb-vssBD-6CQci6-8AFCiD-zsJWT-nNfsgB-dPDwZJ-bn9JGn-5HtSXY-6CUhAL-a4UTXB-ugPum-KUPSo-fBLNm-6CUmpy-4WMsc9-8a7D3T-83KJev-6CQ2bK-nNusHJ-a78rQH-nw3NvT-7aq2qf-8wwBso-3nNceh-ugSKP-4mh4kh-bbeeqH-a7biME-q3PtTf-brFpgb-cg38zw-bXMZc-nJPELD-f58Lmo-bXMYG-bz8AAi-bxNtNT-bXMYi-bXMY6-bXMYv" class="no-underline">

<img srcset="https://mdg.imgix.net/assets/images/shiprock.jpg?auto=format&amp;fit=clip&amp;w=480 480w,
             https://mdg.imgix.net/assets/images/shiprock.jpg?auto=format&amp;fit=clip&amp;q=40&amp;w=1080 1080w" src="https://mdg.imgix.net/assets/images/shiprock.jpg" class="img-fluid" title="Shiprock, Novo México por Beau Rogers" alt="Uma velha rocha no deserto" loading="lazy" sizes="100vw">

  </a>
</div>

## Personagens escapando

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Para exibir um caractere literal que de outra forma seria usado para formatar texto em um documento Markdown, adicione uma barra invertida (</font></font><code class="language-plaintext highlighter-rouge">\</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">) na frente do caractere.</font></font></p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>\* Without the backslash, this would be a bullet in an unordered list.
</code></pre></div></div>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">A saída renderizada fica assim:</font></font></p>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">* Sem a barra invertida, isso seria um marcador em uma lista não ordenada.</font></font></p>

<h3 id="characters-you-can-escape"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Personagens dos quais você pode escapar</font></font><a class="anchorjs-link " aria-label="Âncora" data-anchorjs-icon="" href="#characters-you-can-escape" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h3>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Você pode usar uma barra invertida para escapar dos seguintes caracteres.</font></font></p>

<table class="table table-bordered">
  <thead class="thead-light">
    <tr>
      <th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Personagem</font></font></th>
      <th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Nome</font></font></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">\</font></font></td>
      <td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">barra invertida</font></font></td>
    </tr>
    <tr>
      <td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">`</font></font></td>
      <td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">crases (veja também </font></font><a href="#escaping-backticks"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">escapando de crases no código</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">)</font></font></td>
    </tr>
    <tr>
      <td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">*</font></font></td>
      <td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">asterisco</font></font></td>
    </tr>
    <tr>
      <td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">_</font></font></td>
      <td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">sublinhado</font></font></td>
    </tr>
    <tr>
      <td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">{ }</font></font></td>
      <td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">aparelho encaracolado</font></font></td>
    </tr>
    <tr>
      <td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">[ ]</font></font></td>
      <td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">colchetes</font></font></td>
    </tr>
    <tr>
      <td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">&lt; &gt;</font></font></td>
      <td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">colchetes angulares</font></font></td>
    </tr>
    <tr>
      <td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">( )</font></font></td>
      <td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">parênteses</font></font></td>
    </tr>
    <tr>
      <td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">#</font></font></td>
      <td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">sinal de libra</font></font></td>
    </tr>
    <tr>
      <td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">+</font></font></td>
      <td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">sinal de mais</font></font></td>
    </tr>
    <tr>
      <td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">-</font></font></td>
      <td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">sinal de menos (hífen)</font></font></td>
    </tr>
    <tr>
      <td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">.</font></font></td>
      <td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">ponto</font></font></td>
    </tr>
    <tr>
      <td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">!</font></font></td>
      <td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">ponto de exclamação</font></font></td>
    </tr>
    <tr>
      <td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">|</font></font></td>
      <td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">pipe (veja também </font></font><a href="/extended-syntax/#escaping-pipe-characters-in-tables"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">escapamento de pipe em tabelas</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">)</font></font></td>
    </tr>
  </tbody>
</table>

## HTML

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Muitos aplicativos Markdown permitem usar tags HTML em texto formatado em Markdown. Isso é útil se você preferir certas tags HTML à sintaxe Markdown. Por exemplo, algumas pessoas acham mais fácil usar tags HTML para imagens. Usar HTML também é útil quando você precisa alterar os atributos de um elemento, como especificar a </font></font><a href="/hacks/#color"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">cor do texto</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> ou alterar a largura de uma imagem.</font></font></p>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Para usar HTML, coloque as tags no texto do seu arquivo formatado em Markdown.</font></font></p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>This **word** is bold. This &lt;em&gt;word&lt;/em&gt; is italic.
</code></pre></div></div>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">A saída renderizada fica assim:</font></font></p>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Esta </font></font><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">palavra</font></font></strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> está em negrito. Esta </font></font><em><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">palavra</font></font></em><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> está em itálico.</font></font></p>

<h3 id="html-best-practices"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Práticas recomendadas de HTML</font></font><a class="anchorjs-link " aria-label="Âncora" data-anchorjs-icon="" href="#html-best-practices" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h3>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Por motivos de segurança, nem todos os aplicativos Markdown suportam HTML em documentos Markdown. Em caso de dúvida, verifique a documentação do seu aplicativo Markdown. Alguns aplicativos suportam apenas um subconjunto de tags HTML.</font></font></p>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Use linhas em branco para separar elementos HTML em nível de bloco, como </font></font><code class="language-plaintext highlighter-rouge">&lt;div&gt;</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">, </font></font><code class="language-plaintext highlighter-rouge">&lt;table&gt;</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">, </font></font><code class="language-plaintext highlighter-rouge">&lt;pre&gt;</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> e </font></font><code class="language-plaintext highlighter-rouge">&lt;p&gt;</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> do conteúdo circundante. Tente não recuar as tags com tabulações ou espaços, pois isso pode interferir na formatação.</font></font></p>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Você não pode usar a sintaxe Markdown dentro de tags HTML em nível de bloco. Por exemplo, </font></font><code class="language-plaintext highlighter-rouge">&lt;p&gt;italic and **bold**&lt;/p&gt;</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> não funcionará.</font></font></p>


          <div class="card bg-light mb-3" style="max-width: 100%; margin-top: 50px;">
  <div class="row no-gutters">
    <div class="col-md-3">
      <a href="/book/">

<img srcset="https://mdg.imgix.net/assets/images/book-cover.jpg?auto=format&amp;fit=clip&amp;w=480 480w,
             https://mdg.imgix.net/assets/images/book-cover.jpg?auto=format&amp;fit=clip&amp;q=40&amp;w=1080 1080w" src="https://mdg.imgix.net/assets/images/book-cover.jpg" class="img-fluid" alt="Capa do livro Guia Markdown" loading="lazy" sizes="100vw">

      </a>
    </div>
    <div class="col-md-9">
      <div class="card-body" style="padding-left: 6%;">
        <h5 class="card-title no-anchor" data-toc-skip="" id="take-your-markdown-skills-to-the-next-level"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Leve suas habilidades de Markdown para o próximo nível.</font></font></h5>
        <p class="card-text"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Aprenda Markdown em 60 páginas. Projetado tanto para iniciantes quanto para especialistas, o livro </font></font><em><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">The Markdown Guide</font></font></em><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> é uma referência abrangente que tem tudo que você precisa para começar e dominar a sintaxe do Markdown.</font></font></p>
        <a class="btn btn-success" style="margin-top: 5px; margin-right: 15px" href="/book/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Obtenha o livro</font></font></a>
      </div>
    </div>
  </div>
</div>

<div class="card border-info" style="margin-top: 50px">
  <h6 class="card-header no-anchor bg-info text-white" data-toc-skip=""><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Quer saber mais sobre Markdown?</font></font></h6>
  <div class="card-body">
    <p class="card-text"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
      Não pare agora! 🚀 Marque o </font></font><a href="https://github.com/mattcone/markdown-guide"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">repositório GitHub</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> e digite seu endereço de e-mail abaixo para receber novos tutoriais do Markdown por e-mail. Sem spam!</font></font></p>

      <form method="post" action="https://pika.forklabs.com/subscription/form" class="listmonk-form">
      <div class="form-group" style="margin-top: 20px">
        <input type="hidden" name="nonce">
        <input id="b7668" type="hidden" name="l" value="b766881d-27fd-43a8-9b76-1b74f2a76763">
        <input type="email" class="form-control form-control-lg" name="email" placeholder="Seu endereço de email">
      </div>
      <button type="submit" class="btn btn-success"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Ficar atualizado</font></font></button>
    </form>

  </div>
</div>
        </div>

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

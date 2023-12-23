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


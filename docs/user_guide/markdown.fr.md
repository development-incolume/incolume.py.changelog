# Markdown - Syntaxe de base

---

_basé sur https://www.markdownguide.org/basic-syntax/_

---

## Vue d'ensemble
La quasi-totalité des applications Markdown prennent en charge la syntaxe de base décrite dans le document de conception original de Markdown. Il existe de légères variations et divergences entre les moteurs de rendu Markdown — elles sont signalées en ligne chaque fois que c'est possible.

## Titres

Pour créer un titre, ajoutez des signes dièse (`#`) devant un mot ou une phrase.
Le nombre de signes dièse utilisés doit correspondre au niveau du titre.
Par exemple, pour créer un titre de niveau trois (`<h3>`), utilisez trois signes dièse (par exemple, `### My Header`).

| Balisage          | \tHTML                       | Rendu        |
|---------------------|------------------------------|--------------------------|
| `# Heading level 1` | \t`<h1>Heading level 1</h1>` | <h1>Heading level 1</h1> |
| `# Heading level 2` | \t`<h2>Heading level 2</h2>` | <h1>Heading level 1</h1> |
| `# Heading level 3` | \t`<h3>Heading level 3</h3>` | <h3>Heading level 3</h3> |
| `# Heading level 4` | \t`<h4>Heading level 4</h4>` | <h4>Heading level 4</h4> |
| `# Heading level 5` | \t`<h5>Heading level 5</h5>` | <h5>Heading level 5</h5> |
| `# Heading level 6` | \t`<h6>Heading level 6</h6>` | <h6>Heading level 6</h6> |

## Syntaxe alternative
En alternative, sous la ligne de texte, ajoutez un nombre quelconque de caractères `==` pour un titre de niveau 1, ou des caractères `--` pour un titre de niveau 2.

| Balisage                                                                | \tHTML                       | Rendu        |
|---------------------------------------------------------------------------|------------------------------|--------------------------|
| <code class="highlighter-rouge">Heading level 1<br>===============</code> | \t`<h1>Heading level 1</h1>` | <h1>Heading level 1</h1> |
| <code class="highlighter-rouge">Heading level 2<br>---------------</code> | \t`<h2>Heading level 2</h2>` | <h2>Heading level 2</h2> |

## Bonnes pratiques pour les titres
Les applications Markdown ne s'accordent pas sur la façon de traiter l'absence d'espace entre les signes dièse (`#`) et le nom du titre. Pour des raisons de compatibilité, placez toujours un espace entre les signes dièse et le nom du titre.

|  ✅&nbsp; Faites ainsi   | ❌&nbsp; Ne faites pas cela |
|:--------------------:|:---------------------:|
| `# Here's a Heading` |  `#Here's a Heading`  |


Placez également des lignes vides avant et après un titre, pour la compatibilité.

| ✅  Faites ainsi                                                                                  | ❌ Ne faites pas ainsi                                                                                         |
|------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| <code>Essayez de placer une ligne vide avant...<br><br># Heading<br><br>...et après un titre.</code> | <code>Sans lignes vides, le rendu peut être incorrect.<br># Heading<br>        Ne faites pas cela !</code> |


## Paragraphes

Pour créer des paragraphes, utilisez une ligne vide afin de séparer une ou plusieurs lignes de texte.

| Markdown                                    | \tHTML\t                                      | Rendu                       |
|---------------------------------------------|---------------------------------------------|-----------------------------------------|
| <code>Paragraphe 1.<br><br>Paragraphe 2.</code> | `<p>Paragraphe 1.</p><p>Paragraphe 2.</p>` | <code>Paragraphe 1.<br>Paragraphe 2.</code> |

## Bonnes pratiques pour les paragraphes

À moins que le [paragraphe ne figure dans une liste](#ajout-delements-dans-les-listes), n'indentez pas les paragraphes avec des espaces ou des tabulations.

>  ℹ **Note :** Si vous devez indenter des paragraphes dans le rendu, consultez la section consacrée à l'indentation (tabulation).

|          ✅&nbsp; Faites ainsi                                | ❌&nbsp; Ne faites pas cela                                          |
| ---------------------------------------------------------- | ---------------------------------------------------------------- |
| Ne placez pas de tabulations ni d'espaces avant les paragraphes.    | Cela peut entraîner des problèmes de mise en forme inattendus.       |
| Gardez les lignes alignées à gauche, comme ceci.             | N'ajoutez pas de tabulations ni d'espaces avant les paragraphes.         |

## Sauts de ligne

Pour créer un saut de ligne ou une nouvelle ligne (`<br>`), terminez la ligne par deux espaces ou plus et appuyez sur Entrée.

| Balisage                  | HTML                             | Rendu          |
| --------------------------- | ---------------------------------|----------------------------|
| Ceci est la première ligne.    | <p>Ceci est la première ligne.<br>  | Ceci est la première ligne.   |
| Et ceci est la seconde ligne.   | Et ceci est la seconde ligne.</p>    | Et ceci est la seconde ligne.  |

### Bonnes pratiques pour les sauts de ligne
<!-- TODO: line-break-best-practices -->

Vous pouvez utiliser deux espaces ou plus (souvent appelés « espaces finaux ») pour créer des sauts de ligne dans presque toutes les applications Markdown, mais cette pratique est controversée. Il est difficile de voir les espaces en fin de ligne dans un éditeur, et beaucoup de personnes placent deux espaces après chaque phrase, accidentellement ou intentionnellement. Pour cette raison, vous pouvez préférer utiliser autre chose que des espaces finaux pour les sauts de ligne. Si votre application [Markdown prend en charge le HTML](#html), vous pouvez utiliser la balise HTML `<br>`.

Pour la compatibilité, utilisez les espaces finaux ou la balise HTML `<br>` en fin de ligne.

Il existe deux autres options que je déconseille. CommonMark et certains autres langages de balisage légers permettent de taper une barre oblique inverse (`\`) en fin de ligne, mais toutes les applications Markdown ne le prennent pas en charge : ce n'est donc pas une bonne option du point de vue de la compatibilité. Et au moins certains langages de balisage légers n'exigent rien en fin de ligne — il suffit d'appuyer sur Entrée pour créer un saut de ligne.

| ✅&nbsp; Faites ainsi                       | ❌&nbsp; Ne faites pas cela                         |
| ---------------------------------------- | ----------------------------------------------- |
| Première ligne avec deux espaces à la fin.        | Première ligne avec une barre oblique inverse à la fin.\ |
| Et la ligne suivante.                       |Et la ligne suivante.                               |                  |
| Première ligne avec la balise HTML à la fin.<br>  | Première ligne sans rien à la fin.                 |
|Et la ligne suivante.                        |Et la ligne suivante.                               |

## Emphase

Vous pouvez mettre un texte en emphase en le plaçant en gras ou en italique.

### Gras

Pour mettre un texte en gras, ajoutez deux astérisques ou deux tirets bas avant et après un mot ou une phrase. Pour mettre en gras le milieu d'un mot afin d'y insister, ajoutez deux astérisques sans espaces autour des lettres.

| Balisage                     | HTML                                        | Rendu               |
| ------------------------------ | ------------------------------------------- | --------------------------------|
| J'aime `**texte en gras**`. | J'aime <strong>texte en gras</strong>. | J'aime **texte en gras** . |
| J'aime `__texte en gras__`. | J'aime <strong>texte en gras</strong>. | J'aime __texte en gras__ . |
| L'amour `**est**` gras         | L'amour<strong>est</strong>gras             | L'amour **est** gras            |

#### Bonnes pratiques pour le gras

Les applications Markdown ne s'accordent pas sur la façon de traiter les tirets bas au milieu d'un mot. Pour la compatibilité, utilisez les astérisques pour mettre en gras le milieu d'un mot afin d'y insister.

|✅&nbsp; Faites ainsi     | ❌&nbsp; Ne faites pas cela |
|------------------------|----------------------- |
| L'amour `**est**` gras | L'amour`__est__`gras    |

### Italique

Pour mettre un texte en italique, ajoutez un astérisque ou un tiret bas avant et après un mot ou une phrase. Pour mettre en italique le milieu d'un mot afin d'y insister, ajoutez un astérisque sans espaces autour des lettres.

| Balisage                                   | HTML                                            | Rendu                        |
| -------------------------------------------- | ----------------------------------------------- | ---------------------------------------- |
| Le texte en italique est le `*miaulement du chat*`.    | Le texte en italique est le <em>miaulement du chat</em>.  | Le texte en italique est le *miaulement du chat* . |
| Le texte en italique est le `_miaulement du chat_`.    | Le texte en italique est le <em>miaulement du chat</em>.  | Le texte en italique est le _miaulement du chat_ . |
| Un `*chat*` miaule                             | Un <em>chat</em> miaule                          | Un *chat* miaule                           |

#### Bonnes pratiques pour l'italique
<!-- TODO: italic-best-practices -->

Les applications Markdown ne s'accordent pas sur la façon de traiter les tirets bas au milieu d'un mot. Pour la compatibilité, utilisez les astérisques pour mettre en italique le milieu d'un mot afin d'y insister.

|✅&nbsp; Faites ainsi     |❌&nbsp; Ne faites pas cela    |
|------------------------| ------------------------ |
| Un `*chat*` miaule       | Un`_chat_`miaule         |

### Gras et italique
<!-- TODO: bold-and-italic -->

Pour mettre un texte en gras et en italique à la fois, ajoutez trois astérisques ou trois tirets bas avant et après un mot ou une phrase. Pour mettre en gras et en italique le milieu d'un mot afin d'y insister, ajoutez trois astérisques sans espaces autour des lettres.

| Balisage                                       | HTML                                                                | Rendu                              |
| ------------------------------------------------ | ------------------------------------------------------------------- | ---------------------------------------------- |
| Ce texte est `***vraiment important***`.       | Ce texte est `<em><strong>vraiment important</strong></em>`.      | Ce texte est ***vraiment important***.       |
| Ce texte est `___vraiment important___`.       | Ce texte est `<em><strong>vraiment important</strong></em>`.      | Ce texte est ___vraiment important___.       |
| Ce texte est `__*vraiment important*__`.       | Ce texte est `<em><strong>vraiment important</strong></em>`.      | Ce texte est __*vraiment important*__.       |
| Ce texte est `**_vraiment important**_`.       | Ce texte est `<em><strong>vraiment important</strong></em>`.      | Ce texte est **_vraiment important**_.       |
| Ce texte est vraiment `***très***` important. | Ce texte est vraiment `<em><strong>très important</strong></em>`.| Ce texte est vraiment ***très*** important. |

>  ℹ **Remarque :** l'ordre des balises `em` et `strong` peut être inversé selon le moteur Markdown que vous utilisez.

#### Bonnes pratiques pour le gras et l'italique
<!-- TODO: bold-and-italic-best-practices -->

Les applications Markdown ne s'accordent pas sur la façon de traiter les tirets bas au milieu d'un mot. Pour la compatibilité, utilisez les astérisques pour le gras et l'italique au milieu d'un mot afin d'y insister.

|✅&nbsp; Faites ainsi                               |❌&nbsp; Ne faites pas cela                          |
|-------------------------------------------------| ----------------------------------------------- |
| Ce texte est vraiment `***très***` important.| Ce texte est vraiment`___très___`important.|

## Citations

Pour créer une citation, ajoutez un `>` devant un paragraphe.

    > Dorothy l'a suivie à travers nombre des belles pièces de son château.

Le rendu est le suivant :

> Dorothy l'a suivie à travers nombre des belles pièces de son château.


### Citations à plusieurs paragraphes
<!-- TODO: blockquotes-with-multiple-paragraphs -->

Les citations peuvent contenir plusieurs paragraphes. Ajoutez un `>` sur les lignes vides entre les paragraphes.

    > Dorothy l'a suivie à travers nombre des belles pièces de son château.

    >

    > La Sorcière lui ordonna de nettoyer les casseroles et les bouilloires, de balayer le sol et d'entretenir le feu avec du bois.

Le rendu est le suivant :

> Dorothy l'a suivie à travers nombre des belles pièces de son château.
>
> La Sorcière lui ordonna de nettoyer les casseroles et les bouilloires, de balayer le sol et d'entretenir le feu avec du bois.

### Citations imbriquées
<!-- TODO: nested-blockquotes -->

Les citations peuvent être imbriquées. Ajoutez `>>` devant le paragraphe que vous souhaitez imbriquer.

    > Dorothy l'a suivie à travers nombre des belles pièces de son château.

    >

    >> La Sorcière lui ordonna de nettoyer les casseroles et les bouilloires, de balayer le sol et d'entretenir le feu avec du bois.

Le rendu est le suivant :

> Dorothy l'a suivie à travers nombre des belles pièces de son château.
>
>> La Sorcière lui ordonna de nettoyer les casseroles et les bouilloires, de balayer le sol et d'entretenir le feu avec du bois.

### Citations avec d'autres éléments
<!-- TODO: blockquotes-with-other-elements -->

Les citations peuvent contenir d'autres éléments formatés en Markdown. Tous les éléments ne sont pas forcément pris en charge — il faudra essayer pour voir lesquels fonctionnent.

    > #### Les résultats trimestriels sont excellents !

    >

    > - Les revenus étaient au sommet.

    > - Les bénéfices n'ont jamais été aussi élevés.

    >

    > *Tout* se déroule comme **prévu**.

Le rendu est le suivant :

> #### Les résultats trimestriels sont excellents !
>
> - Les revenus étaient au sommet.
> - Les bénéfices n'ont jamais été aussi élevés.
>
> *Tout* se déroule comme **prévu**.

### Bonnes pratiques pour les citations
<!-- TODO: blockquotes-best-practices -->

Pour la compatibilité, placez des lignes vides avant et après les citations.

| ✅&nbsp; Faites ainsi                        | ❌&nbsp; Ne faites pas cela                             |
| ------------------------------------------ | -------------------------------------------------- |
| Essayez de placer une ligne vide avant... | Sans lignes vides, le rendu peut être incorrect.\
|                                            | > Ceci est une citation.\
| > Ceci est une citation              | Ne faites pas cela !\
|                                            |                                                    |
| ...et après une citation.       |                                                    |

## Listes

Vous pouvez organiser des éléments en listes ordonnées et non ordonnées.

### Listes ordonnées
<!-- TODO: ordered-lists -->

Pour créer une liste ordonnée, ajoutez des éléments de ligne avec des nombres suivis de points. Les nombres n'ont pas besoin d'être dans l'ordre numérique, mais la liste doit commencer par le numéro un.

| Balisage                                       | HTML                                                                | Rendu                              |
| ------------------------------------------------ | ------------------------------------------------------------------- | ---------------------------------------------- |
| 1. Premier élément <br> 2. Deuxième élément <br> 3. Troisième élément <br> 4. Quatrième élément| `<ol>`<br>ㅤ`<li>Premier élément</li>`<br>ㅤ`<li>Deuxième élément</li>`<br>ㅤ`<li>Troisième élément</li>`<br>ㅤ`<li>Quatrième élément</li>`<br>`</ol>`| 1. Premier élément <br> 2. Deuxième élément <br> 3. Troisième élément <br> 4. Quatrième élément|
| 1. Premier élément <br> 1. Deuxième élément <br> 1. Troisième élément <br> 1. Quatrième élément| `<ol>`<br>ㅤ`<li>Premier élément</li>`<br>ㅤ`<li>Deuxième élément</li>`<br>ㅤ`<li>Troisième élément</li>`<br>ㅤ`<li>Quatrième élément</li>`<br>`</ol>`| 1. Premier élément <br> 2. Deuxième élément <br> 3. Troisième élément <br> 4. Quatrième élément|
| 1. Premier élément <br> 8. Deuxième élément <br> 3. Troisième élément <br> 5. Quatrième élément| `<ol>`<br>ㅤ`<li>Premier élément</li>`<br>ㅤ`<li>Deuxième élément</li>`<br>ㅤ`<li>Troisième élément</li>`<br>ㅤ`<li>Quatrième élément</li>`<br>`</ol>`| 1. Premier élément <br> 2. Deuxième élément <br> 3. Troisième élément <br> 4. Quatrième élément|
| 1. Premier élément <br> 2. Deuxième élément <br> 3. Troisième élément <br>ㅤㅤ1. Élément indenté <br>ㅤㅤ2. Élément indenté <br> 4. Quatrième élément | `<ol>`<br>ㅤ`<li>Premier élément</li>`<br>ㅤ`<li>Deuxième élément</li>`<br>ㅤ`<li>Troisième élément</li>`<br>ㅤ`<li>Quatrième élément</li>`<br>`</ol>`| 1. Premier élément <br> 2. Deuxième élément <br> 3. Troisième élément <br>ㅤㅤ1. Élément indenté <br>ㅤㅤ2. Élément indenté <br> 4. Quatrième élément |

#### Bonnes pratiques pour les listes ordonnées
<!-- TODO: ordered-list-best-practices -->

CommonMark et certains autres langages de balisage légers permettent d'utiliser des parenthèses (`( )`) comme délimiteur (par exemple, 1) _Premier élément_), mais toutes les applications Markdown ne les prennent pas en charge : ce n'est donc pas une bonne option du point de vue de la compatibilité. Pour la compatibilité, utilisez uniquement des points.

|✅&nbsp; Faites ainsi |❌&nbsp; Ne faites pas cela |
| ----------------- | ---------------------- |
|1. Premier élément<br>  |1) Premier élément<br>       |
|2. Deuxième élément     |2) Deuxième élément          |

### Listes non ordonnées
<!-- TODO: unordered-lists -->

Pour créer une liste non ordonnée, ajoutez des tirets ( `-` ), des astérisques ( `*` ) ou des signes plus ( `+` ) devant les éléments de ligne. Indentez un ou plusieurs éléments pour créer une liste imbriquée.

| Balisage                                       | HTML                                                                | Rendu                              |
| ------------------------------------------------ | ------------------------------------------------------------------- | ---------------------------------------------- |
| - Premier élément <br> - Deuxième élément <br> - Troisième élément <br> - Quatrième élément| `<ul>`<br>ㅤ`<li>Premier élément</li>`<br>ㅤ`<li>Deuxième élément</li>`<br>ㅤ`<li>Troisième élément</li>`<br>ㅤ`<li>Quatrième élément</li>`<br>`</ul>`| • Premier élément <br> • Deuxième élément <br> • Troisième élément <br> • Quatrième élément|
| * Premier élément <br> * Deuxième élément <br> * Troisième élément <br> * Quatrième élément| `<ul>`<br>ㅤ`<li>Premier élément</li>`<br>ㅤ`<li>Deuxième élément</li>`<br>ㅤ`<li>Troisième élément</li>`<br>ㅤ`<li>Quatrième élément</li>`<br>`</ul>`| • Premier élément <br> • Deuxième élément <br> • Troisième élément <br> • Quatrième élément|
| + Premier élément <br> + Deuxième élément <br> + Troisième élément <br> + Quatrième élément| `<ul>`<br>ㅤ`<li>Premier élément</li>`<br>ㅤ`<li>Deuxième élément</li>`<br>ㅤ`<li>Troisième élément</li>`<br>ㅤ`<li>Quatrième élément</li>`<br>`</ul>`| • Premier élément <br> • Deuxième élément <br> • Troisième élément <br> • Quatrième élément|
| - Premier élément <br> - Deuxième élément <br> - Troisième élément <br>ㅤㅤ- Élément indenté <br>ㅤㅤ- Élément indenté <br> - Quatrième élément | `<ul>`<br>ㅤ`<li>Premier élément</li>`<br>ㅤ`<li>Deuxième élément</li>`<br>ㅤ`<li>Troisième élément</li>`<br>ㅤ`<li>Quatrième élément</li>`<br>`</ul>`| • Premier élément <br> • Deuxième élément <br> • Troisième élément <br>ㅤㅤ◦ Élément indenté <br>ㅤㅤ◦ Élément indenté <br> • Quatrième élément |

#### Commencer les éléments d'une liste non ordonnée par des nombres
<!-- TODO: starting-unordered-list-items-with-numbers -->

Si vous devez commencer un élément de liste non ordonnée par un nombre suivi d'un point, vous pouvez utiliser une barre oblique inverse (`\`) pour [échapper](#caractres-déchappement) au point.

| Balisage                                                      | HTML                                         | Rendu                    |
| --------------------------------------------------------------- | -------------------------------------------- | ------------------------------------ |
| - 1968\. Une grande année !<br>- Je pense que 1969 était la deuxième meilleure. |`<ul>`<br>ㅤ`<li>1968. Une grande année !</li>`<br>`<li>Je pense que 1969 était la deuxième meilleure.</li>`<br>`</ul>` |• 1968. Une grande année !<br>• Je pense que 1969 était la deuxième meilleure.|

#### Bonnes pratiques pour les listes non ordonnées
<!-- TODO: unordered-list-best-practices -->

Les applications Markdown ne s'accordent pas sur la façon de traiter différents délimiteurs dans une même liste. Pour la compatibilité, ne mélangez pas les délimiteurs au sein d'une même liste — choisissez-en un et conservez-le.

| ✅&nbsp; Faites ainsi                                                       | ❌&nbsp; Ne faites pas cela |
| ------------------------------------------------------------------------ | ----------------------- |
| - Premier élément<br>- Deuxième élément<br>- Troisième élément<br>- Quatrième élément    | + Premier élément<br>* Deuxième élément<br>- Troisième élément<br>+ Quatrième élément|


### Ajout d'éléments dans les listes
<!-- TODO: adding-elements-in-lists -->

Pour ajouter un autre élément à une liste tout en préservant sa continuité, indentez l'élément avec quatre espaces ou une tabulation, comme indiqué dans les exemples ci-dessous.

>  ℹ **Astuce :** Si les éléments ne s'affichent pas comme prévu, vérifiez que vous avez bien indenté les éléments de la liste avec quatre espaces ou une tabulation.

#### Paragraphes

    * Ceci est le premier élément de la liste.
    * Voici le deuxième élément de la liste.

        Je dois ajouter un autre paragraphe sous le deuxième élément de la liste.

    * Et voici le troisième élément de la liste.

Le rendu est le suivant :

* Ceci est le premier élément de la liste.
* Voici le deuxième élément de la liste.

    Je dois ajouter un autre paragraphe sous le deuxième élément de la liste.

* Et voici le troisième élément de la liste.

#### Citations
<!-- TODO: blockquotes -->

    * Ceci est le premier élément de la liste.
    * Voici le deuxième élément de la liste.

        > Une citation serait parfaite sous le deuxième élément de la liste.

    * Et voici le troisième élément de la liste

Le rendu est le suivant :

* Ceci est le premier élément de la liste.
* Voici le deuxième élément de la liste.
    > Une citation serait parfaite sous le deuxième élément de la liste.
* Et voici le troisième élément de la liste

#### Blocs de code
<!-- TODO: code-blocks-1 -->

Les [blocs de code](#blocs-de-code) sont généralement indentés de quatre espaces ou d'une tabulation. Lorsqu'ils figurent dans une liste, indentez-les de huit espaces ou de deux tabulations.

    1. Ouvrez le fichier.
    2. Trouvez le bloc de code suivant à la ligne 21 :

        <html>
          <head>
            <title>Test</title>
          </head>

    3. Mettez à jour le titre pour qu'il corresponde au nom de votre site.

Le rendu est le suivant :

1. Ouvrez le fichier.
2. Trouvez le bloc de code suivant à la ligne 21 :

        <html>
          <head>
            <title>Test</title>
          </head>

3. Mettez à jour le titre pour qu'il corresponde au nom de votre site.

#### Images
<!-- TODO: images -->

    1. Ouvrez le fichier contenant la mascotte de Linux.
    2. Admirez sa beauté.

        ![Tux, la mascotte de Linux](https://mdg.imgix.net/assets/images/tux.png?auto=format&fit=clip&q=40&w=100)

    3. Fermez le fichier.

Le rendu est le suivant :

1. Ouvrez le fichier contenant la mascotte de Linux.
2. Admirez sa beauté.

    ![Tux, la mascotte de Linux](https://mdg.imgix.net/assets/images/tux.png?auto=format&fit=clip&q=40&w=100)

3. Fermez le fichier.

#### Listes
<!-- TODO: lists -->

Vous pouvez imbriquer une liste non ordonnée dans une liste ordonnée, ou l'inverse.

    1. Premier élément
    2. Deuxième élément
    3. Troisième élément
          - Élément indenté
          - Élément indenté
    4. Quatrième élément

Le rendu est le suivant :

1. Premier élément
2. Deuxième élément
3. Troisième élément
      - Élément indenté
      - Élément indenté
4. Quatrième élément

## Code

Pour désigner un mot ou une phrase comme du code, placez-le entre des accents graves (`` ` ``).

|Balisage                              |HTML                                                  |Rendu                       |
| -------------------------------------- | ---------------------------------------------------- |--------------------------------------- |
|``À l'invite de commande, tapez `Nano`.``| À l'invite de commande, tapez <code>Nano</code>.      |À l'invite de commande, tapez `nano`.    |

### Échapper aux accents graves
<!-- TODO: escaping-backticks -->

Si le mot ou la phrase que vous désirez désigner comme code contient un ou plusieurs accents graves, vous pouvez l'échapper en plaçant le mot ou la phrase entre deux accents graves (`` ``).

|Balisage                             |HTML                                              |Rendu           |
| ------------------------------------- | ------------------------------------------------ | -------------------------  |
|``Utilisez `code` dans votre fichier Markdown.``| <code>Utilisez `code` dans votre fichier Markdown.</code> |Utilisez ´code´ dans votre fichier Markdown.|

### Blocs de code
<!-- TODO: code-blocks -->

Pour créer des blocs de code, indentez chaque ligne du bloc d'au moins quatre espaces ou d'une tabulation.

    <html>
      <head>
      </head>
    </html>

Le rendu est le suivant :

    <html>
      <head>
      </head>
    </html>

>  ℹ **Note :** Pour créer des blocs de code sans indenter les lignes, utilisez les [blocs de code délimités](https://www.markdownguide.org/extended-syntax/#fenced-code-blocks).

## Lignes horizontales

Pour créer une ligne horizontale, utilisez trois astérisques ( `***` ), trois tirets ( `---` ) ou trois tirets bas ( `___` ) ou plus sur une ligne seule.

    ***
    ---
    ______________
Le rendu des trois semble identique :

_____________________________________________________

### Bonnes pratiques pour les lignes horizontales
<!-- TODO: horizontal-rule-best-practices -->

Pour la compatibilité, placez des lignes vides avant et après les lignes horizontales.

| ✅&nbsp; Faites ainsi                                                                      | ❌&nbsp; Ne faites pas cela |
|----------------------------------------------------------------------------------------- |------------------------|
|Essayez de placer une ligne vide avant...<br><br>---<br><br>...et après une ligne horizontale. |Sans lignes vides, ceci deviendrait un titre.<br>---<br>Ne faites pas cela !

## Liens

Pour créer un lien, placez le texte du lien entre crochets (par exemple, `[Duck Duck Go]`) et faites-le suivre immédiatement de l'URL entre parenthèses (par exemple, `(https://duckduckgo.com)`).

    Mon moteur de recherche préféré est [Duck Duck Go](https://duckduckgo.com).


Le rendu est le suivant :

Mon moteur de recherche préféré est [Duck Duck Go](https://duckduckgo.com).

>  ℹ **Note :** Pour créer un lien vers un élément de la même page, consultez la section sur les [liens vers les identifiants de titre](https://www.markdownguide.org/extended-syntax/#linking-to-heading-ids). Pour créer un lien qui s'ouvre dans un nouvel onglet ou une nouvelle fenêtre, consultez la section sur les [cibles de lien](https://www.markdownguide.org/hacks/#link-targets).

### Ajouter des titres
<!-- TODO: adding-titles -->

Vous pouvez éventuellement ajouter un titre à un lien. Celui-ci apparaîtra sous forme d'infobulle lorsque l'utilisateur survolera le lien. Pour ajouter un titre, placez-le entre guillemets après l'URL.

    Mon moteur de recherche préféré est [Duck Duck Go](https://duckduckgo.com "The best search engine for privacy").

Le rendu est le suivant :
Mon moteur de recherche préféré est [Duck Duck Go](https://duckduckgo.com).

### URL et adresses e-mail
<!-- TODO: urls-and-email-addresses -->

Pour transformer rapidement une URL ou une adresse e-mail en lien, placez-la entre crochets angulaires.

    <https://www.markdownguide.org>
    <fake@example.com>

Le rendu est le suivant :

 <https://www.markdownguide.org>

 <fake@example.com>

### Mise en forme des liens
<!-- TODO: formatting-links -->

Pour [mettre les liens en emphase](#emphase), ajoutez des astérisques avant et après les crochets et les parenthèses. Pour désigner des liens comme du [code](#code), ajoutez des accents graves entre les crochets.

    J'adore soutenir l'**[EFF](https://eff.org)**.

    Ceci est le *[Markdown Guide](https://www.markdownguide.org)*.

    Consultez la section sur le [`code`](#code).

Le rendu est le suivant :

J'adore soutenir l'**[EFF](https://eff.org)**.

Ceci est le *[Markdown Guide](https://www.markdownguide.org)*.

Consultez la section sur le [`code`](#code).

### Liens de type référence
<!-- TODO: reference-style-links -->

Les liens de type référence sont un type particulier de lien qui rend les URL plus faciles à afficher et à lire en Markdown. Ils se construisent en deux parties : celle que vous conservez alignée avec votre texte et celle que vous stockez ailleurs dans le fichier pour que le texte reste facile à lire.

#### Mise en forme de la première partie du lien
<!-- TODO: formatting-the-first-part-of-the-link -->

La première partie d'un lien de type référence est mise en forme avec deux paires de crochets. La première paire entoure le texte qui doit apparaître lié. La seconde paire affiche un libellé utilisé pour pointer vers le lien stocké ailleurs dans le document.

Bien que ce ne soit pas obligatoire, vous pouvez insérer un espace entre la première et la seconde paire de crochets. Le libellé de la seconde paire de crochets est insensible à la casse et peut contenir des lettres, des chiffres, des espaces ou de la ponctuation.

Cela signifie que les formats d'exemple suivants sont approximativement équivalents pour la première partie du lien :

* [hobbit-hole][1]
* [hobbit-hole][1]

#### Mise en forme de la seconde partie du lien
<!-- TODO: formatting-the-second-part-of-the-link -->

La seconde partie d'un lien de type référence est mise en forme avec les attributs suivants :

    1. Le libellé, entre crochets, suivi immédiatement de deux points et d'au moins un espace (par exemple, [label]: ).
    2. L'URL du lien, que vous pouvez placer entre crochets angulaires.
    3. Le titre facultatif du lien, que vous pouvez placer entre guillemets doubles, guillemets simples ou parenthèses.

Cela signifie que les formats d'exemple suivants sont approximativement équivalents pour la seconde partie du lien :

    * [1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle
    * [1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle "Hobbit lifestyles"
    * [1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle 'Hobbit lifestyles'
    * [1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle (Hobbit lifestyles)
    * [1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle "Hobbit lifestyles"
    * [1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle 'Hobbit lifestyles'
    * [1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle (Hobbit lifestyles)

Vous pouvez placer cette seconde partie du lien n'importe où dans votre document Markdown. Certains la placent immédiatement après le paragraphe où elle apparaît, d'autres à la fin du document (comme des notes de fin ou de bas de page).

#### Un exemple qui assemble les éléments
<!-- TODO: an-example-putting-the-parts-together -->

Supposons que vous ajoutiez une URL sous forme de [lien d'URL standard](#liens) à un paragraphe et qu'il ressemble à ceci en Markdown :

    Dans un trou du sol vivait un hobbit. Ce n'était ni un trou dégoûtant, sale et humide, rempli de bouts
    de vers et suintant une odeur de vase, ni un trou sec, vide et sableux, où il n'y avait rien pour s'asseoir ou pour
    manger : c'était un [terrier de hobbit](https://en.wikipedia.org/wiki/Hobbit#Lifestyle "Hobbit lifestyles"), et cela signifie le confort.

Bien qu'elle puisse pointer vers des informations complémentaires intéressantes, l'URL affichée n'ajoute pas grand-chose au texte brut existant, sinon de le rendre plus difficile à lire. Pour corriger cela, vous pouvez mettre en forme l'URL ainsi :

    Dans un trou du sol vivait un hobbit. Ce n'était ni un trou dégoûtant, sale et humide, rempli de bouts de vers et suintant une odeur de vase, ni un trou sec, vide et sableux, où il n'y avait rien pour s'asseoir ou pour manger : c'était un [terrier de hobbit](https://en.wikipedia.org/wiki/Hobbit#Lifestyle), et cela signifie le confort.

Dans les deux cas ci-dessus, le rendu serait identique :

>
> Dans un trou du sol vivait un hobbit. Ce n'était ni un trou dégoûtant, sale et humide, rempli de bouts de vers et suintant une odeur de vase, ni un trou sec, vide et sableux, où il n'y avait rien pour s'asseoir ou pour manger : c'était un [terrier de hobbit](https://en.wikipedia.org/wiki/Hobbit#Lifestyle), et cela signifie le confort.
>

et le HTML du lien serait :

    <a href="https://en.wikipedia.org/wiki/Hobbit#Lifestyle title="Hobbit lifestyles">hobbit-hole</a>

### Bonnes pratiques pour les liens
<!-- TODO: link-best-practices -->

Les applications Markdown ne s'accordent pas sur la façon de traiter les espaces au milieu d'une URL. Pour la compatibilité, encodez les espaces dans les URL avec %20. En alternative, si votre application Markdown [prend en charge le HTML](#html), vous pouvez utiliser la balise HTML.

| ✅&nbsp; Faites ainsi                                       | ❌&nbsp; Ne faites pas cela                               |
| -------------------------------------------------------- | ------------------------------------------------------|
|`[link](https://www.example.com/my%20great%20page)`<br><br>`<a href="https://www.example.com/my great page">link</a>`|`[link](https://www.example.com/my great page)`<br><br>|

Les parenthèses au milieu d'une URL peuvent également poser problème. Pour la compatibilité, encodez la parenthèse ouvrante `(` en %28 et la parenthèse fermante `)` en %29. En alternative, si votre application Markdown [prend en charge le HTML](#html), vous pouvez utiliser la balise HTML.

| ✅&nbsp; Faites ainsi                                       | ❌&nbsp; Ne faites pas cela                               |
| -------------------------------------------------------- | ------------------------------------------------------|
|`[a novel](https://en.wikipedia.org/wiki/The_Milagro_Beanfield_War_%28novel%29)`<br><br>`<a href="https://en.wikipedia.org/wiki/The_Milagro_Beanfield_War_(novel)">a novel</a>`|`[a novel](https://en.wikipedia.org/wiki/The_Milagro_Beanfield_War_(novel))`|

## Images

Pour ajouter une image, ajoutez un point d'exclamation ( `!` ), suivi d'un texte alternatif entre crochets et du chemin ou de l'URL de la ressource image entre parenthèses. Vous pouvez éventuellement ajouter un titre entre guillemets après le chemin ou l'URL.

    ![Les montagnes San Juan sont belles !](/assets/images/san-juan-mountains.jpg "San Juan Mountains")

Le rendu est le suivant :

![Les montagnes San Juan sont belles !](https://mdg.imgix.net/assets/images/san-juan-mountains.jpg?auto=format&fit=clip&q=40&w=800 "San Juan Mountains")

>  ℹ **Note :** Pour redimensionner une image, consultez la section sur la [taille des images](https://www.markdownguide.org/hacks/#image-size). Pour ajouter une légende, consultez la section sur les [légendes d'images](https://www.markdownguide.org/hacks/#image-captions).

### Liens sur les images
<!-- TODO: linking-images -->

Pour ajouter un lien à une image, placez le Markdown de l'image entre crochets et ajoutez le lien entre parenthèses.

    [![An old rock in the desert](/assets/images/shiprock.jpg "Shiprock, New Mexico by Beau Rogers")](https://www.flickr.com/photos/beaurogers/31833779864/in/photolist-Qv3rFw-34mt9F-a9Cmfy-5Ha3Zi-9msKdv-o3hgjr-hWpUte-4WMsJ1-KUQ8N-deshUb-vssBD-6CQci6-8AFCiD-zsJWT-nNfsgB-dPDwZJ-bn9JGn-5HtSXY-6CUhAL-a4UTXB-ugPum-KUPSo-fBLNm-6CUmpy-4WMsc9-8a7D3T-83KJev-6CQ2bK-nNusHJ-a78rQH-nw3NvT-7aq2qf-8wwBso-3nNceh-ugSKP-4mh4kh-bbeeqH-a7biME-q3PtTf-brFpgb-cg38zw-bXMZc-nJPELD-f58Lmo-bXMYG-bz8AAi-bxNtNT-bXMYi-bXMY6-bXMYv)


Le rendu est le suivant :

[![An old rock in the desert](https://mdg.imgix.net/assets/images/shiprock.jpg?auto=format&fit=clip&q=40&w=800 "Shiprock, New Mexico by Beau Rogers")](https://www.flickr.com/photos/beaurogers/31833779864/in/photolist-Qv3rFw-34mt9F-a9Cmfy-5Ha3Zi-9msKdv-o3hgjr-hWpUte-4WMsJ1-KUQ8N-deshUb-vssBD-6CQci6-8AFCiD-zsJWT-nNfsgB-dPDwZJ-bn9JGn-5HtSXY-6CUhAL-a4UTXB-ugPum-KUPSo-fBLNm-6CUmpy-4WMsc9-8a7D3T-83KJev-6CQ2bK-nNusHJ-a78rQH-nw3NvT-7aq2qf-8wwBso-3nNceh-ugSKP-4mh4kh-bbeeqH-a7biME-q3PtTf-brFpgb-cg38zw-bXMZc-nJPELD-f58Lmo-bXMYG-bz8AAi-bxNtNT-bXMYi-bXMY6-bXMYv)

## Caractères d'échappement

Pour afficher un caractère littéral qui serait autrement utilisé pour formater du texte dans un document Markdown, ajoutez une barre oblique inverse ( `\` ) devant le caractère.

    \* Sans la barre oblique inverse, ce serait un tiret dans une liste non ordonnée.

Le rendu est le suivant :

* Sans la barre oblique inverse, ce serait un tiret dans une liste non ordonnée.

### Caractères que vous pouvez échapper
<!-- TODO: characters-you-can-escape -->

Vous pouvez utiliser une barre oblique inverse pour échapper les caractères suivants.

|Caractères   |Nom                                                                            |
| ----------- | ------------------------------------------------------------------------------ |
|\            |barre oblique inverse                                                           |
|`            |accent grave (voir aussi [échapper les accents graves dans le code](#échapper-aux-accents-graves)) |
|*            |astérisque                                                                      |
|_            |tiret bas                                                                       |
|{}           |accolades                                                                       |
|[]           |crochets                                                                        |
|<>           |crochets angulaires                                                             |
|()           |parenthèses                                                                     |
|#            |dièse                                                                           |
|+            |signe plus                                                                      |
|-            |signe moins (tiret)                                                             |
|.            |point                                                                           |
|!            |point d'exclamation                                                             |
||            |barre verticale                                                                 |

## HTML

De nombreuses applications Markdown permettent d'utiliser des balises HTML dans du texte formaté en Markdown. C'est utile si vous préférez certaines balises HTML à la syntaxe Markdown. Par exemple, certaines personnes trouvent plus facile d'utiliser des balises HTML pour les images. Le HTML est également utile lorsque vous devez modifier les attributs d'un élément, comme définir la [couleur du texte](https://www.markdownguide.org/hacks/#color) ou modifier la largeur d'une image.

Pour utiliser le HTML, placez les balises dans le texte de votre fichier formaté en Markdown.

    This **word** is bold. This <em>word</em> is italic.

Le rendu est le suivant :

Ce **mot** est en gras. Ce *mot* est en italique.

### Bonnes pratiques pour le HTML
<!-- TODO: html-best-practices -->

Pour des raisons de sécurité, toutes les applications Markdown ne prennent pas en charge le HTML dans les documents Markdown. En cas de doute, consultez la documentation de votre application Markdown. Certaines applications ne prennent en charge qu'un sous-ensemble des balises HTML.

Utilisez des lignes vides pour séparer les éléments HTML de niveau bloc, tels que `<table><pre><p>`, du contenu qui les entoure. Essayez de ne pas indenter les balises avec des tabulations ou des espaces — cela peut interférer avec la mise en forme.

Vous ne pouvez pas utiliser la syntaxe Markdown à l'intérieur des balises HTML de niveau bloc. Par exemple, `<p>italic and **bold**</p>` ne fonctionnera pas.
F
## Emojis

[Emoji pour MarkDown](https://gist.github.com/rxaviers/7360908)

### Personnes

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

### Objets

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

### Lieux

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

### Symboles

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

## Références

- https://www.markdownguide.org/basic-syntax/

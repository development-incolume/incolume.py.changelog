# Mensagens de commits do Git

---

Este projeto segue Conventional Commits, uma especificação para adicionar significado humano e
legível por máquina às mensagens de commit.

```bash
<tipo>[escopo opcional]: <descrição>

[corpo opcional]

[rodapé(s) opcional(is)]
```

O commit contém os seguintes elementos estruturais, para comunicar a intenção aos consumidores da sua biblioteca:

+ **type**: o tipo de commit (feat|feature, fix|bugfix, chore, refactor, docs, style, test, perf, ci, build, revert)
    + **feat**: Um commit do tipo feat introduz um novo recurso à base de código (isso se correlaciona com MINOR no Versionamento Semântico).
    + **fix** ou **bugfix**: Um commit do tipo fix corrige um bug na sua base de código (isso se correlaciona com PATCH no Versionamento Semântico).
    + **chore**: Alterações que não estão relacionadas com uma correção ou funcionalidade e não modificam os ficheiros src ou de teste (por exemplo, atualizar dependências);
    + **refactor**: código refactorizado que não corrige um bug nem adiciona uma funcionalidade;
    + **docs**: actualizações à documentação, como o README ou outros ficheiros markdown ou rst;
    + **style**: Alterações que não afectam o significado do código, provavelmente relacionadas com a formatação do código, como espaços em branco, pontos e vírgulas em falta, estilo preto aplicado, etc;
    + **teste**: Inclusão de novos testes ou correção de testes anteriores;
    + **perf**: melhorias de desempenho;
    + **ci**: Relacionadas com a integração contínua;
    + **build**: alterações que afectam o sistema de compilação ou dependências externas;
    + **revert**: reverte um teste anterior

Traduzido com a versão gratuita do tradutor - DeepL.com

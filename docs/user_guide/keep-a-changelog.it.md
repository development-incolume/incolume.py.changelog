# keep a changelog

## Che cos'è un changelog?
Un changelog è un file che contiene un elenco selezionato, ordinato cronologicamente, delle modifiche significative apportate a ciascuna versione di un progetto.

## Perché tenere un changelog?
Per consentire agli utenti e ai collaboratori di vedere con precisione quali modifiche significative sono state apportate tra ciascuna versione pubblicata di un progetto.

## Chi ha bisogno di un changelog?
Le persone ne hanno bisogno. Che siano consumatori o sviluppatori, gli utenti finali dei software sono esseri umani che si preoccupano di ciò che è contenuto nel software. Quando il software cambia, le persone vogliono sapere perché e come.

## Come creare un buon changelog?
### Principi fondamentali
- I changelog sono per gli esseri umani, non per le macchine.
- Ci deve essere una voce per ogni versione.
- Le modifiche dello stesso tipo devono essere raggruppate.
- Le versioni e le sezioni devono essere collegabili (con link).
- La versione più recente viene prima.
- Viene visualizzata la data di rilascio di ogni versione.
- Indica se segui il [versionamento semantico](https://semver.org/).


### Tipi di modifiche
- **Added**: (Aggiunto) per le nuove funzionalità.
- **Changed**: (Modificato) per le modifiche alle funzionalità esistenti.
- **Deprecated**: (Obsoleto) per le funzionalità che saranno rimosse nelle prossime versioni.
- **Removed**: (Rimosso) per le funzionalità rimosse in questa versione.
- **Fixed**: (Corretto) per qualsiasi correzione di bug.
- **Security**: (Sicurezza) in caso di vulnerabilità.

## Come applicare il changelog a questo progetto?
   Questo progetto utilizza il pacchetto python incolumepy.utils, che ha la
   prerogativa di creare automaticamente un `CHANGELOG.md` dalle
voci di `git tag -n`.

Esempi:
```shell
git tag -f Unreleased -m 'added: Aggiunte linee guida su Keep a CHANGELOG.md in docs/user_guide/keep-a-chagelog.md'
git tag -f `poetry version -s` -m ‘added: Aggiunte linee guida su Keep a CHANGELOG.md in docs/user_guide/keep-a-chagelog.md’
git tag -f 1.0.0 -m 'Added: (Aggiunto) per nuove funzionalità;
Changed: (Modificato) per modifiche a funzionalità esistenti;
Deprecated: (Obsoleto) per le funzionalità che saranno rimosse nelle prossime versioni;
Removed: (Rimosso) per le funzionalità rimosse in questa versione;
Fixed: (Corretto) per qualsiasi correzione di bug;
Security: (Sicurezza) in caso di vulnerabilità;'
```

### Aggiornare CHANGELOG.md
```shell
task gcl
```

## Riferimento
- https://keepachangelog.com/pt-BR/1.0.0/

Tradotto con DeepL.com (versione gratuita)

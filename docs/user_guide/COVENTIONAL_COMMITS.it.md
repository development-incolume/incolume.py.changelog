# Messaggi di commit Git

---

Questo progetto segue i commit convenzionali, una specifica per aggiungere ai messaggi di commit un significato leggibile dall'uomo e dalla macchina
.

```bash
<tipo>[scope opzionale]: <descrizione>

[corpo opzionale]

[piè di pagina opzionali]
````

Il commit contiene i seguenti elementi strutturali, per comunicare l'intento ai consumatori della libreria:

+ **type**: il tipo di commit (feat|feature, fix|bugfix, chore, refactor, docs, style, test, perf, ci, build, revert)
    + **feat**: Un commit del tipo feat introduce una nuova caratteristica nella base di codice (questo corrisponde a MINOR nel Semantic Versioning).
    + **fix** o **bugfix**: Un commit del tipo fix corregge un bug nella base di codice (questo è correlato con PATCH nel versionamento semantico).
    + **chore**: Modifiche che non riguardano una correzione o una caratteristica e non modificano i file src o di test (per esempio l'aggiornamento delle dipendenze);
    + **refactor**: codice rifattorizzato che non corregge un bug né aggiunge una funzionalità;
    + **docs**: aggiornamenti della documentazione come il README o altri file markdown o rst;
    + **style**: Modifiche che non influiscono sul significato del codice, probabilmente relative alla formattazione del codice come spazi bianchi, punti e virgole mancanti, stile nero applicato e così via;
    + **test**: Inclusione di nuovi test o correzione di quelli precedenti;
    + **perf**: miglioramenti delle prestazioni;
    + **ci**: Integrazione continua;
    + **build**: modifiche che riguardano il sistema di compilazione o le dipendenze esterne;
    + **revert**: ripristina una precedente modifica 

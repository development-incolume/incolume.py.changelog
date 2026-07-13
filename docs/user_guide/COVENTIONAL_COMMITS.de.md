# Git Commits Nachrichten

---

Dieses Projekt folgt Conventional Commits, einer Spezifikation für das Hinzufügen von menschlich und
maschinenlesbarer Bedeutung zu Commit-Nachrichten.

```bash
<type>[optionaler Bereich]: <Beschreibung>

[optional body]

[optionale Fußzeile(n)]
````

Der Commit enthält die folgenden Strukturelemente, um den Nutzern Ihrer Bibliothek Ihre Absicht mitzuteilen:

+ **type**: der Typ des Commits (feat|feature, fix|bugfix, chore, refactor, docs, style, test, perf, ci, build, revert)
    + **feat**: Ein Commit vom Typ feat führt ein neues Feature in die Codebasis ein (dies entspricht MINOR in Semantic Versioning).
    + **fix** oder **bugfix**: Ein Commit vom Typ fix behebt einen Fehler in der Codebasis (dies entspricht PATCH in Semantic Versioning).
    **chore**: Änderungen, die sich nicht auf einen Fix oder ein Feature beziehen und keine src- oder Testdateien verändern (z.B. Aktualisieren von Abhängigkeiten);
    **refactor**: Refactored Code, der weder einen Fehler behebt noch eine Funktion hinzufügt;
    **docs**: Aktualisierungen der Dokumentation wie z.B. die README oder andere Markdown- oder rst-Dateien;
    **style**: Änderungen, die sich nicht auf die Bedeutung des Codes auswirken und wahrscheinlich mit der Formatierung des Codes zu tun haben, wie z.B. Leerzeichen, fehlende Semikolons, schwarzer Stil und so weiter;
    **test**: Einfügen neuer oder Korrigieren früherer Tests;
    + **perf**: Leistungsverbesserungen;
    + **ci**: Fortlaufende Integration;
    + **build**: Änderungen, die das Build-System oder externe Abhängigkeiten betreffen;
    **revert**: macht einen vorherigen Test rückgängig

Übersetzt mit DeepL.com (kostenlose Version)

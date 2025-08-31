# Führen Sie ein Änderungsprotokoll

## Was ist ein Änderungsprotokoll?
Ein Änderungsprotokoll ist eine Datei, die eine ausgewählte, chronologisch geordnete Liste der wesentlichen Änderungen für jede Version eines Projekts enthält.

## Warum sollte man ein Änderungsprotokoll führen?
Damit Benutzer und Mitwirkende genau sehen können, welche wesentlichen Änderungen zwischen den einzelnen veröffentlichten Versionen eines Projekts vorgenommen wurden.

## Wer braucht ein Änderungsprotokoll?
Menschen brauchen es. Ob Verbraucher oder Entwickler, die Endnutzer von Software sind Menschen, die sich dafür interessieren, was in der Software steckt. Wenn sich die Software ändert, wollen die Menschen wissen, warum und wie.

## Wie erstellt man ein gutes Änderungsprotokoll?
### Grundlegende Prinzipien
- Änderungsprotokolle sind für Menschen gedacht, nicht für Maschinen.
- Es sollte für jede Version ein Eintrag vorhanden sein.
- Änderungen derselben Art sollten gruppiert werden.
- Versionen und Abschnitte sollten verlinkbar sein.
- Die neueste Version steht an erster Stelle.
- Das Veröffentlichungsdatum jeder Version wird angezeigt.
- Geben Sie an, ob Sie die [semantische Versionierung](https://semver.org/) verwenden.


### Arten von Änderungen
- **Added**: (Hinzugefügt) für neue Funktionen.
- **Changed**: (Geändert) für Änderungen an bestehenden Funktionen.
- **Deprecated**: (Veraltet) für Funktionen, die in zukünftigen Versionen entfernt werden.
- **Removed**: (Entfernt) für Funktionen, die in dieser Version entfernt wurden.
- **Fixed**: (Behoben) für alle Fehlerbehebungen.
- **Security**: (Sicherheit) bei Sicherheitslücken.

## Wie wendet man das Changelog in diesem Projekt an?
   Dieses Projekt verwendet das Python-Paket incolumepy.utils, das die
   die Möglichkeit bietet, automatisch eine `CHANGELOG.md` aus den
Einträgen von `git tag -n` zu erstellen.

Beispiele:
```shell
git tag -f Unreleased -m 'added: Hinzugefügt: Hinweise zu Keep a CHANGELOG.md in docs/user_guide/keep-a-chagelog.md'
git tag -f `poetry version -s` -m ‚added: Hinzugefügt: Anweisungen zu Keep a CHANGELOG.md in docs/user_guide/keep-a-chagelog.md‘
git tag -f 1.0.0 -m 'Added: (Hinzugefügt) für neue Funktionen;
Changed: (Geändert) für Änderungen an bestehenden Funktionen;
Deprecated: (Veraltet) für Funktionen, die in zukünftigen Versionen entfernt werden;
Removed: (Entfernt) für Funktionen, die in dieser Version entfernt wurden;
Fixed: (Behoben) für alle Fehlerbehebungen;
Security: (Sicherheit) im Falle von Sicherheitslücken;'
```

### CHANGELOG.md aktualisieren
```shell
task gcl
```

## Referenz
- https://keepachangelog.com/pt-BR/1.0.0/

Übersetzt mit DeepL.com (kostenlose Version)

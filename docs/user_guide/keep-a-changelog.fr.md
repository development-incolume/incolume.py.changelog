# keep a changelog

## Qu'est-ce qu'un changelog ?
Un changelog est un fichier qui contient une liste sélectionnée, classée par ordre chronologique, des changements significatifs apportés à chaque version d'un projet.

## Pourquoi tenir un changelog ?
Pour permettre aux utilisateurs et aux contributeurs de voir précisément quels changements significatifs ont été apportés entre chaque version publiée d'un projet.

## Qui a besoin d'un journal des modifications ?
Les gens en ont besoin. Qu'ils soient consommateurs ou développeurs, les utilisateurs finaux de logiciels sont des êtres humains qui se soucient du contenu du logiciel. Lorsque le logiciel change, les gens veulent savoir pourquoi et comment.

## Comment créer un bon journal des modifications ?
### Principes fondamentaux
- Les journaux des modifications sont destinés aux humains, pas aux machines.
- Il doit y avoir une entrée pour chaque version.
- Les modifications du même type doivent être regroupées.
- Les versions et les sections doivent être liées (avec des liens).
- La version la plus récente vient en premier.
- La date de sortie de chaque version est affichée.
- Mentionnez si vous suivez le [versionnement sémantique](https://semver.org/).


### Types de modifications
- **Added** : (Ajouté) pour les nouvelles fonctionnalités.
- **Changed** : (Modifié) pour les modifications apportées aux fonctionnalités existantes.
- **Deprecated** : (Obsolète) pour les fonctionnalités qui seront supprimées dans les prochaines versions.
- **Removed** : (Supprimé) pour les fonctionnalités supprimées dans cette version.
- **Fixed** : (Corrigé) pour toute correction de bug.
- **Security** : (Sécurité) en cas de vulnérabilités.

## Comment appliquer le changelog à ce projet ?
 Ce projet utilise le paquet python incolumepy.utils, qui a la
   prerogative de créer automatiquement un `CHANGELOG.md` à partir des
entrées de `git tag -n`.

Exemples :
```shell
git tag -f Unreleased -m 'added: Ajout d'instructions sur Keep a CHANGELOG.md dans docs/user_guide/keep-a-chagelog.md'
git tag -f `poetry version -s` -m “added: Ajout d'instructions sur Keep a CHANGELOG.md dans docs/user_guide/keep-a-chagelog.md”
git tag -f 1.0.0 -m 'Added: (Ajouté) pour les nouvelles fonctionnalités ;
Changed: (Modifié) pour les modifications apportées aux fonctionnalités existantes ;
Obsolète : pour les fonctionnalités qui seront supprimées dans les prochaines versions ;
Supprimé : pour les fonctionnalités supprimées dans cette version ;
Corrigé : pour toute correction de bug ;
Sécurité : en cas de vulnérabilités ;'
```

### Mettre à jour le fichier CHANGELOG.md
```shell
task gcl
```

## Référence
- https://keepachangelog.com/pt-BR/1.0.0/

# Git commits messages

---

Ce projet suit Conventional Commits, une spécification pour ajouter une signification lisible par l'homme et
par la machine aux messages de commit.

```bash
<type>[champ d'application optionnel] : <description>

[corps optionnel]

[optional footer(s)]
````

Le commit contient les éléments structurels suivants, pour communiquer l'intention aux consommateurs de votre bibliothèque :

**type** : le type de commit (feat|feature, fix|bugfix, chore, refactor, docs, style, test, perf, ci, build, revert)
    + **feat** : Un commit de type feat introduit une nouvelle fonctionnalité dans la base de code (ce qui correspond à MINOR dans le Semantic Versioning).
    **fix** ou **bugfix** : Un commit de type fix corrige un bogue dans votre base de code (ce qui correspond à PATCH dans le versionnement sémantique).
    **chore** : Changements qui ne sont pas liés à un correctif ou à une fonctionnalité et qui ne modifient pas les fichiers src ou test (par exemple, mise à jour des dépendances) ;
    **refactor** : code refactoré qui ne corrige pas de bogue et n'ajoute pas de fonctionnalité ;
    **docs** : mises à jour de la documentation comme le README ou d'autres fichiers markdown ou rst ;
    **style** : Changements qui n'affectent pas la signification du code, probablement liés au formatage du code comme les espaces blancs, les points-virgules manquants, le style noir appliqué, et ainsi de suite ;
    **test** : Inclure de nouveaux tests ou corriger les tests précédents ;
    **perf** : amélioration des performances ;
    **ci** : Intégration continue ;
    **build** : changements qui affectent le système de construction ou les dépendances externes ;
    **revert** : rétablissement d'un test précédent 

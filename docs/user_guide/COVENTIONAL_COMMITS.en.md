# Git Commit Messages

---

This project follows Conventional Commits, a specification for adding human and
machine-readable meaning to commit messages.

```bash
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

The commit contains the following structural elements, to communicate intent to the consumers of your library:

+ **type**: the type of commit (feat|feature, fix|bugfix, chore, refactor, docs, style, test, perf, ci, build, revert)
    + **feat**: A commit of the type feat introduces a new feature to the codebase (this correlates with MINOR in Semantic Versioning).
    + **fix** or **bugfix**: A commit of the type fix patches a bug in your codebase (this correlates with PATCH in Semantic Versioning).
    + **chore**: Changes that do not relate to a fix or feature and do not modify src or test files (for example, updating dependencies);
    + **refactor**: refactored code that neither fixes a bug nor adds a feature;
    + **docs**: updates to documentation, such as the README or other markdown or rst files;
    + **style**: Changes that do not affect the meaning of the code, likely related to code formatting, such as white-space, missing semi-colons, black style applied, and so on;
    + **test**: A commit of the type test includes new tests or corrections to previous ones;
    + **perf**: Performance improvements;
    + **ci**: Continuous integration related;
    + **build**: Changes that affect the build system or external dependencies;
    + **revert**: Reverts a previous commit

Translated with the free version of the translator - DeepL.com

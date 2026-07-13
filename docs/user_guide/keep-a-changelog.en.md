# keep a changelog

## What is a changelog?
A changelog is a file that contains a selected, chronologically ordered list of significant changes for each version of a project.

## Why keep a changelog?
To make it easier for users and contributors to see precisely what significant changes have been made between each published version of a project.

## Who needs a changelog?
People do. Whether they are consumers or developers, end users of software are human beings who care about what is in the software. When software changes, people want to know why and how.

## How to make a good changelog?
### Fundamental principles
- Changelogs are for humans, not machines.
- There should be one entry for each version.
- Changes of the same type should be grouped together.
- Versions and sections should be linkable.
- The most recent version comes first.
- The release date of each version is displayed.
- Mention if you follow [semantic versioning](https://semver.org/).


### Types of changes
- **Added**: for new features.
- **Changed**: for changes to existing features.
- **Deprecated**: for features that will be removed in future versions.
- **Removed**: for features removed in this version.
- **Fixed**: for any bug fixes.
- **Security**: in case of vulnerabilities.

## How to apply changelog in this project?
   This project uses the python package incolumepy.utils, which has the
   prerogative to automatically create a `CHANGELOG.md` from the
entries in `git tag -n`.

Examples:
```shell
git tag -f Unreleased -m 'added: Added guidelines on Keep a CHANGELOG.md in docs/user_guide/keep-a-chagelog.md'
git tag -f `poetry version -s` -m ‘added: Added guidelines on Keep a CHANGELOG.md in docs/user_guide/keep-a-chagelog.md’
git tag -f 1.0.0 -m 'Added: for new features;
Changed: for changes to existing features;
Deprecated: for features that will be removed in future versions;
Removed: for features removed in this version;
Fixed: for any bug fixes;
Security: in case of vulnerabilities;'
```

### Update CHANGELOG.md
```shell
task gcl
```

## Reference
- https://keepachangelog.com/pt-BR/1.0.0/

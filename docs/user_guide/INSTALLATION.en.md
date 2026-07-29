# Guia de Uso
## Instalação

To install it using poetry:

More detail can be see in [Python Poetry: Gerenciando dependências de projeto](https://brito.blog.incolume.com.br/2022/01/python-poetry-gerenciando-dependencias.html)

Last package version from pypi.org:
```shell
  poetry add -G dev incolume.py.changelog
```
Download package wheel:
```shell
  poetry add -G dev incolume.py.changelog-1.0.0-py3-none-any.whl
```
Download package tar.gz:
```shell
  poetry add -G dev incolume.py.changelog-1.0.0.tar.gz
```
Last package version from git repo:
```shell
  poetry add -G dev git+https://github.com/development-incolume/incolume.py.changelog.git@main
```
Specific version from git repo:
```shell
  poetry add -G dev git+https://github.com/development-incolume/incolume.py.changelog.git@"1.0.0"
```
Specific branch from git repo:
```shell
  poetry add -G dev git+https://github.com/development-incolume/incolume.py.changelog.git@"enhacement-123456789"
```

To install package using uv:

Last package version from pypi.org:
```shell
  uv add --dev incolume.py.changelog
```

Download package wheel:
```shell
  uv add --dev incolume.py.changelog-1.0.0-py3-none-any.whl
```

Download package tar.gz:

```shell
  uv add --dev incolume.py.changelog-1.0.0.tar.gz
```

Specific release or tag from git repo:
```shell
uv add --dev git+https://github.com/development-incolume/incolume.py.changelog.git --tag 1.0.0
uv add --dev git+https://github.com/development-incolume/incolume.py.changelog.git --tag Unreleased
uv add --dev git+https://github.com/development-incolume/incolume.py.changelog.git --tag 0.19.0rc4
```

Specific branch from git repo:

```shell
uv add --dev git+https://github.com/development-incolume/incolume.py.changelog.git --branch main
uv add --dev git+https://github.com/development-incolume/incolume.py.changelog.git --branch tags
uv add --dev git+https://github.com/development-incolume/incolume.py.changelog.git --branch dev
```

Specific revision from git repo:
```shell
uv add --dev git+https://github.com/development-incolume/incolume.py.changelog.git --rev f8bb0dc6792391f30cdabcac1fa5731160a3c27c   
```


To install package using pip:

```shell
  pip install incolume.py.changelog
```

## Detalhes da API ##

Disponível em [docs/api](../api/index.md)


## Detalhes para desenvolvimento ##
Disponível em [docs/user_guide/development.md](development.md)

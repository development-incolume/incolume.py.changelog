from pathlib import Path
from tempfile import gettempdir

import pytest


from incolume.py.changelog.changelog import (
    Changelog,
    __version__,
    changelog_messages,
    msg_classify,
    update_changelog,
)

__author__ = "@britodfbr"  # pragma: no cover


class TestCase:
    """Class test case."""
    @pytest.mark.parametrize(
        "entrance",
        (
            "1.0.0 Added: Fake record; other fake record; Fixed: Fake fixed",
            "1.3.0 Fixed: Fake record; other fake record; Changed: Fake fixed",
            "2.2.1 Security: Fake record; other fake record; Fake fixed",
            "1.0.5 Added: Fake record; other fake record; Fixed: Fake fixed",
        ),
    )
    def test_msg_classify_type(self, entrance):
        assert isinstance(msg_classify(entrance), dict)

    @pytest.mark.parametrize(
        "entrance",
        (
            "1.0.0 Added: Fake record; other fake record; Fixed: Fake fixed",
            "1.0.5 Added: Fake record; other fake record; Fixed: Fake fixed",
            "1.3.0 Fixed: Fake record; other fake record; Changed: Fake fixed",
            "2.0.0 Security: "
            "Aderência a https://keepachangelog.com/pt-BR/1.0.0/",
            "2.2.1 Security: Fake record; other fake record; Fake fixed",
        ),
    )
    def test_msg_classify_value(self, entrance):
        result = msg_classify(entrance)
        assert "key" in result
        assert "date" in result
        assert "messages" in result

    @pytest.mark.parametrize(
        "entrance expected".split(),
        (
            pytest.param(
                {
                    "msg": "1.0.0 Added: Fake record; other "
                    "fakrecord; Fixed: Fake fixed"
                },
                {
                    "key": "1.0.0",
                    "date": "2018-10-19",
                    "messages": {
                        "Added": ["Fake record", " other fakrecord"],
                        "Fixed": ["Fake fixed"],
                    },
                },
                # marks=pytest.mark.skip(reason='skiped')
            ),
            pytest.param(
                {
                    "msg": "1.5.0 Added: Fake record; "
                    "other fake record; Fixed: Fake fixed",
                    "lang": "en-US",
                },
                {
                    "key": "1.5.0",
                    "date": "2022-01-22",
                    "messages": {
                        "Added": ["Fake record", " other fake record"],
                        "Fixed": ["Fake fixed"],
                    },
                },
                # marks=pytest.mark.skip(reason='skiped')
            ),
            pytest.param(
                {
                    "msg": "2.0.0 Segurança: Aderência a "
                    "https://keepachangelog.com/pt-BR/1.0.0/",
                    "lang": "pt-BR",
                },
                {
                    "key": "2.0.0",
                    "date": "2022-02-16",
                    "messages": {
                        "Security": [
                            "Aderência a "
                            "https://keepachangelog.com/pt-BR/1.0.0/"
                        ]
                    },
                },
                # marks=pytest.mark.skip(reason='skiped')
            ),
            pytest.param(
                {
                    "msg": "2.4.1 Obsoleto: Fakerecord; "
                    "other fkrecord; Fak fixd",
                    "lang": "pt-BR",
                },
                {
                    "key": "2.4.1",
                    "date": "2022-03-08",
                    "messages": {
                        "Deprecated": [
                            "Fakerecord",
                            " other fkrecord",
                            " Fak fixd",
                        ]
                    },
                },
                # marks=pytest.mark.skip(reason='skiped')
            ),
            pytest.param(
                {
                    "msg": "1.0.1 deprecated: Fake record; "
                    "Removed: other fake; ab; cd; ef;gh; ij; kl; "
                    "mn; op; Fixed: Fake fixed",
                    # "lang": "pt-BR",
                },
                {
                    "key": "1.0.1",
                    "date": "2018-10-19",
                    "messages": {
                        "Fixed": ["Fake fixed"],
                        "Removed": [
                            "other fake",
                            " ab",
                            " cd",
                            " ef",
                            "gh",
                            " ij",
                            " kl",
                            " mn",
                            " op",
                        ],
                        "Deprecated": ["Fake record"],
                    },
                },
                # marks=pytest.mark.skip(reason='skiped')
            ),
            pytest.param(
                {
                    "msg": "2.8.0      Adicionado: Unreleased/"
                    "Não publicado para o número de versão e adicionar "
                    "uma nova seção Unreleased/Não publicado no topo; "
                    "Tradução para labels ptBR -> enUS; "
                    "Implementado nova função iter_logs(); Fixed: "
                    "Formatação visual para CHANGELOG.md retirado link"
                    " quebrado para 1ª release; Changed: Fatorado "
                    "código para changelog_body(); Security: em caso de"
                    " vulnerabilidades.;Adicionado: para novos "
                    "recursos.; Modificado: para alterações em "
                    "recursos existentes.; "
                    "Obsoleto: para recursos que serão "
                    "removidos nas próximas versões.;Removido :para "
                    "recursos removidos nesta versão.; Corrigido :para "
                    "qualquer correção de bug.; Segurança :em caso de "
                    "vulnerabilidades.;",
                },
                {
                    "key": "2.8.0",
                    "date": "2023-07-22",
                    "messages": {
                        "Added": [
                            "Unreleased/Não publicado para o número de versão "
                            "e adicionar uma nova seção Unreleased/Não "
                            "publicado no topo",
                            " Tradução para labels ptBR -> enUS",
                            " Implementado nova função iter_logs()",
                            "para novos recursos.",
                        ],
                        "Changed": [
                            "Fatorado código para changelog_body()",
                            "para alterações em recursos existentes.",
                        ],
                        "Fixed": [
                            "para qualquer correção de bug.",
                            "Formatação visual para CHANGELOG.md retirado "
                            "link quebrado para 1ª release",
                        ],
                        "Deprecated": [
                            "para recursos que serão removidos "
                            "nas próximas versões."
                        ],
                        "Removed": ["para recursos removidos nesta versão."],
                        "Security": [
                            "em caso de vulnerabilidades.",
                            "em caso de vulnerabilidades.",
                        ],
                    },
                }
                # marks=pytest.mark.skip(reason='skiped')
            ),
        ),
    )
    def test_msg_classify_result(self, entrance, expected):
        result = msg_classify(**entrance)
        assert expected == result

    @pytest.mark.parametrize(
        "entrance expected".split(),
        (
            pytest.param(
                {
                    "text": "1.0.1 Obsoleto: Fake record; Removed: other fake;"
                    " ab; cd; ef;gh; ij; kl; mn;op; Fixed: Fake fixed,"
                    "Unreleased    Added: Unreleased/Não publicado "
                    "para o número de versão e adicionar uma nova "
                    "seção Unreleased/Não publicado no topo; Tradução "
                    "para labels ptBR -> enUS; Implementado nova "
                    "função iter_logs(); Fixed: Formatação visual "
                    "para CHANGELOG.md retirado link quebrado para 1ª "
                    "release; Changed: Fatorado código para "
                    "changelog_body(); Security: em caso de "
                    "vulnerabilidades.;Adicionado: para novos "
                    "recursos.; Modificado: para alterações em "
                    "recursos existentes.; Obsoleto: para recursos que"
                    " serão removidos nas próximas versões.;Removido"
                    " :para recursos removidos nesta versão.; "
                    "Corrigido :para qualquer correção de bug.; "
                    "Segurança :em caso de vulnerabilidades.;",
                    "lang": None,
                },
                [
                    (
                        "1.0.1",
                        {
                            "key": "1.0.1",
                            "date": "2018-10-19",
                            "messages": {
                                "Added": [
                                    "Unreleased/Não publicado para o número "
                                    "de versão e adicionar uma nova seção "
                                    "Unreleased/Não publicado no topo",
                                    " Tradução para labels ptBR -> enUS",
                                    " Implementado nova função iter_logs()",
                                    "para novos recursos.",
                                ],
                                "Changed": [
                                    "Fatorado código para changelog_body()",
                                    "para alterações em recursos existentes.",
                                ],
                                "Fixed": [
                                    "para qualquer correção de bug.",
                                    "Fake fixed,Unreleased",
                                    "Formatação visual para CHANGELOG.md "
                                    "retirado link quebrado para 1ª release",
                                ],
                                "Deprecated": [
                                    "Fake record",
                                    "para recursos que serão removidos "
                                    "nas próximas versões.",
                                ],
                                "Removed": [
                                    "other fake",
                                    " ab",
                                    " cd",
                                    " ef",
                                    "gh",
                                    " ij",
                                    " kl",
                                    " mn",
                                    "op",
                                    "para recursos removidos nesta versão.",
                                ],
                                "Security": [
                                    "em caso de vulnerabilidades.",
                                    "em caso de vulnerabilidades.",
                                ],
                            },
                        },
                    ),
                ],
                # marks=pytest.mark.skip(reason='skiped')
            ),
            (
                {
                    "text": """
                    1.0.0 Added: Fake record; other fake; Fixed: Fake fixed",
                    1.3.0 Fixed: Fake record; other fake; Changed: Fake fixed",
                    1.5.0 Added: Fake record; other fake; Fixed: Fake fixed",
                    2.2.0 Security: Fake record; other record; Fake fixed",
                    """
                },
                [
                    (
                        "1.0.0",
                        {
                            "date": "2018-10-19",
                            "key": "1.0.0",
                            "messages": {
                                "Added": ["Fake record", " other fake"],
                                "Fixed": ['Fake fixed",'],
                            },
                        },
                    ),
                    (
                        "1.3.0",
                        {
                            "date": "2022-01-21",
                            "key": "1.3.0",
                            "messages": {
                                "Changed": ['Fake fixed",'],
                                "Fixed": ["Fake record", " other fake"],
                            },
                        },
                    ),
                    (
                        "1.5.0",
                        {
                            "date": "2022-01-22",
                            "key": "1.5.0",
                            "messages": {
                                "Added": ["Fake record", " other fake"],
                                "Fixed": ['Fake fixed",'],
                            },
                        },
                    ),
                    (
                        "2.2.0",
                        {
                            "date": "2022-02-16",
                            "key": "2.2.0",
                            "messages": {
                                "Security": [
                                    "Fake record",
                                    " other record",
                                    ' Fake fixed",',
                                ]
                            },
                        },
                    ),
                ],
            ),
            (
                {
                    "text": "1.0.0 Security: a;b;c; "
                    "Removed: 1;2;3; Changed: a;b;c;d;e; "
                    "Fixed: http://example.com; http://httpbin.com;"
                    "Deprecated: 1;2;3;a;s;b; Added: a1;a2;a3."
                },
                [
                    (
                        "1.0.0",
                        {
                            "key": "1.0.0",
                            "date": "2018-10-19",
                            "messages": {
                                "Added": "a1 a2 a3.".split(),
                                "Changed": "a;b;c;d;e".split(";"),
                                "Deprecated": "1;2;3;a;s;b".split(";"),
                                "Fixed": [
                                    "http://example.com",
                                    " http://httpbin.com",
                                ],
                                "Removed": ["1", "2", "3"],
                                "Security": ["a", "b", "c"],
                            },
                        },
                    )
                ],
            ),
        ),
    )
    def test_changelog_messages(self, entrance, expected):
        assert changelog_messages(**entrance) == expected

    @pytest.mark.parametrize(
        "entrance",
        (
            {"changelog_file": Path(gettempdir()) / "CHANGELOG.md"},
            pytest.param(
                {"changelog_file": None},
                # marks=pytest.mark.skip(
                #     reason='need mock to write CHANGELOG.md')
            ),
            pytest.param(
                {},
            ),
        ),
    )
    def test_changelog_write(self, entrance, ftemp, return_git_tag, mocker):
        result = changelog_messages(text=return_git_tag)
        entrance.update({"content": result})
        if "changelog_file" not in entrance:
            entrance.update({"changelog_file": ftemp})

        mocked = mocker.Mock(spec=incolumepy.utils.changelog.changelog_write)
        result = mocked(**entrance)
        esperado = mocker.call(**entrance)
        assert esperado == mocked.call_args  # cobertura QA
        assert result  # Resultado

    @pytest.mark.parametrize(
        "entrance",
        (
            {},
            {
                "changelog_file": Path(gettempdir())
                .joinpath("xpto.md")
                .as_posix()
            },
        ),
    )
    def test_update_changelog(self, entrance, ftemp, return_git_tag):
        entrance.update({"content": return_git_tag})
        if "changelog_file" not in entrance:
            entrance.update({"changelog_file": ftemp})
        assert update_changelog(**entrance)


class TestClassChangelog:
    @pytest.mark.parametrize(
        "entrance",
        (
            {},
            {"reverse": False},
        ),
    )
    def test_init(self, entrance):
        """Test for init class."""
        o = Changelog(**entrance)
        assert isinstance(o, Changelog)

    @pytest.mark.parametrize(
        "entrance expected".split(),
        (
            (
                {},
                [
                    "# CHANGELOG\n\n\n",
                    "All notable changes to this project",
                    " will be documented in this file.\n\n",
                    "The format is based on ",
                    "[Keep a Changelog]"
                    "(https://keepachangelog.com/en/1.0.0/), ",
                    "this project adheres to [Semantic Versioning]"
                    "(https://semver.org/spec/v2.0.0.html) and "
                    "[Conventional Commit]"
                    "(https://www.conventionalcommits.org/"
                    "pt-br/v1.0.0/).\n\n",
                    "This file was automatically generated for",
                    " [incolumepy.utils]"
                    "(https://gitlab.com/development-incolume/"
                    f"incolumepy.utils/-/tree/{__version__})",
                    "\n\n---\n",
                ],
            ),
            (
                {"reverse": False},
                [
                    "# CHANGELOG\n\n\n",
                    "All notable changes to this project",
                    " will be documented in this file.\n\n",
                    "The format is based on ",
                    "[Keep a Changelog]"
                    "(https://keepachangelog.com/en/1.0.0/), ",
                    "this project adheres to [Semantic Versioning]"
                    "(https://semver.org/spec/v2.0.0.html) and "
                    "[Conventional Commit]"
                    "(https://www.conventionalcommits.org/"
                    "pt-br/v1.0.0/).\n\n",
                    "This file was automatically generated for",
                    " [incolumepy.utils]"
                    "(https://gitlab.com/development-incolume/"
                    f"incolumepy.utils/-/tree/{__version__})",
                    "\n\n---\n",
                ],
            ),
        ),
    )
    def test_header(self, entrance, expected):
        """Test for header file."""
        o = Changelog(**entrance)
        assert o.header() == expected

    @pytest.mark.parametrize(
        "entrance expected".split(),
        (
            (
                {
                    "content": [
                        (
                            "1.0.0a1",
                            {
                                "date": "2023-7-19",
                                "key": "1.0.0a1",
                                "messages": {
                                    "Added": ["Fake record", " other fake"],
                                    "Fixed": ['Fake fixed",'],
                                },
                            },
                        ),
                    ],
                    "linked": False,
                },
                [
                    "\n\n## 1.0.0a1\t &#8212; \t2023-7-19:",
                    "\n### Added",
                    "\n  - Fake record;",
                    "\n  - Other fake;",
                    "\n### Fixed",
                    '\n  - Fake fixed",;',
                ],
            ),
            (
                {
                    "content": [
                        (
                            "1.0.0a0",
                            {
                                "date": "2023-7-19",
                                "key": "1.0.0a0",
                                "messages": {
                                    "Added": ["Fake record", " other fake"],
                                    "Fixed": ['Fake fixed",'],
                                },
                            },
                        ),
                    ],
                },
                [
                    "\n\n## [1.0.0a0]\t &#8212; \t2023-7-19:",
                    "\n### Added",
                    "\n  - Fake record;",
                    "\n  - Other fake;",
                    "\n### Fixed",
                    '\n  - Fake fixed",;',
                ],
            ),
        ),
    )
    def test_iter_logs(self, entrance, expected):
        """Test for iter_logs"""
        assert Changelog.iter_logs(**entrance) == expected

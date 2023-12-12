import datetime as dt

import pytest

import incolumepy.utils.changelog
from incolumepy.utils import decorators


class TestCase0:
    @pytest.fixture
    def input_dict(self):
        return {"a": 1}

    def test_fixture(self, input_dict):
        assert input_dict["a"] == 1, f"Check fixture {input_dict}"

    def test_mock_write_files(self, mocker, temp_file_name):
        mock_save_file = mocker.Mock(
            spec=incolumepy.utils.changelog.changelog_write
        )
        content = [
            (
                "1.0.0",
                {
                    "key": "1.0.0",
                    "date": dt.datetime.now().strftime("%FT%T%z"),
                    "messages": {
                        "Added": [1, 3, 4],
                        "Changed": [1, 3, 4],
                        "Fixed": [1, 3, 4],
                        "Security": [1, 3, 4],
                    },
                },
            )
        ]
        mock_save_file(conteudo=content, changelog_file=temp_file_name)
        esperado = mocker.call(conteudo=content, changelog_file=temp_file_name)
        assert esperado == mock_save_file.call_args


def my_sum(x, y):
    return x + y


class TestCaseExamples:
    """Test Case Examples."""

    def test_mock_builtins(self, mocker):
        mocker.patch("__main__.ord", return_value=67)
        print(ord("c"))

    def test_sum1(self, mocker):
        mocker.patch(__name__ + ".my_sum", return_value=9)
        assert my_sum(2, 3) == 9

    def test_sum2(self, mocker):
        def crazy_sum(a, b):
            return b + b

        mocker.patch(__name__ + ".my_sum", side_effect=crazy_sum)
        assert my_sum(2, 3) == 6

    @pytest.mark.xfail(reason="Decorator not available!")
    def test_only_unix_exception(self, mocker):
        with mocker.patch("platform.system", return_value="windows"):

            @decorators.only_unix
            def winexec():
                return ""

            with pytest.raises(
                expected_exception=AssertionError,
                match='Sistema operacional "windows" '
                "incompativél com este método",
            ):
                winexec()

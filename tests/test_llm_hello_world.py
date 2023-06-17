from click.testing import CliRunner
from llm import cli


def test_hello_world():
    runner = CliRunner()
    result = runner.invoke(cli.cli, ["hello-world"])
    assert result.exit_code == 0
    assert result.output == "Hello world!\n"

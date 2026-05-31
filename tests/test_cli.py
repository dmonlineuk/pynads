from typer.testing import CliRunner

from ui.cli import app

runner = CliRunner()

def test_init_db():
    result = runner.invoke(app, ["init-db"])
    assert result.exit_code == 0
    assert "initialised" in result.stdout.lower()

def test_add_node_minimal():
    result = runner.invoke(
        app,
        [
            "add-node",
            "testnode",
            "--cpu-model", "i5",
            "--ram-gb", "16",
            "--storage-gb", "256",
            "--os-type", "Linux",
            "--access-categories", "SSH",
            "--network-types", "Wired",
            "--ip-type", "DHCP",
            "--purpose", "test machine"
        ]
    )
    assert result.exit_code == 0
    assert "testnode" in result.stdout

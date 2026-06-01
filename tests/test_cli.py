from typer.testing import CliRunner

from ui.cli import app

runner = CliRunner()

def test_init_db():
    result = runner.invoke(app, ["init"])
    assert result.exit_code == 0
    assert "initialised" in result.stdout.lower()

def test_add_node_minimal():
    result = runner.invoke(
        app,
        [
            "add",
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

def test_list_nodes():
    result = runner.invoke(app, ["list"])
    assert result.exit_code == 0

def test_search_nodes():
    result = runner.invoke(app, ["search", "test"])
    assert result.exit_code == 0

def test_view_node_not_found():
    result = runner.invoke(app, ["view", "99999"])
    assert "not found" in result.stdout.lower()

def test_edit_node():
    result = runner.invoke(app, ["edit", "1", "purpose", "updated"])
    assert result.exit_code == 0

def test_delete_node():
    result = runner.invoke(app, ["delete", "1"])
    assert result.exit_code == 0

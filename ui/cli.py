import typer

from db.nodes import insert_node
from db.schema import create_tables
from models.node import Node
from utils.validators import validate_ip, validate_os

app = typer.Typer(help="Network Asset Documentation CLI")

@app.command("init-db")
def init_db():
    """Initialise the SQLite database."""
    create_tables()
    typer.echo("Database initialised.")

@app.command("add-node")
def add_node(
    hostname: str = typer.Argument(...),
    cpu_model: str = typer.Option(..., prompt=True),
    ram_gb: int = typer.Option(..., prompt=True),
    storage_gb: int = typer.Option(..., prompt=True),
    os_type: str = typer.Option(..., prompt=True),
    access_categories: list[str] = typer.Option(  # noqa: B008
        None,
        help="Multiple allowed: Physical Terminal, Web UI, SSH, RDP Remote"
    ),
    network_types: list[str] = typer.Option(  # noqa: B008
        None,
        help="Multiple allowed: Wired, Wireless"
    ),
    ip_type: str = typer.Option(..., prompt=True),
    static_ip: str | None = typer.Option(None),
    purpose: str = typer.Option(..., prompt=True)
):
    """Add a new node to the database."""
    validate_os(os_type)
    validate_ip(ip_type, static_ip)

    node = Node(
        hostname=hostname,
        cpu_model=cpu_model,
        ram_gb=ram_gb,
        storage_gb=storage_gb,
        os_type=os_type,
        access_categories=access_categories or [],
        network_types=network_types or [],
        ip_type=ip_type,
        static_ip=static_ip,
        purpose=purpose
    )

    insert_node(node)
    typer.echo(f"Node '{hostname}' added.")

@app.command("list")
def list_nodes_cmd():
    """List all nodes."""
    from db.nodes import list_nodes
    rows = list_nodes()
    for r in rows:
        typer.echo(f"{r[0]}: {r[1]} ({r[2]}) - {r[3]}")

@app.command("search")
def search_nodes_cmd(term: str):
    """Search nodes by hostname."""
    from db.nodes import search_nodes
    rows = search_nodes(term)
    for r in rows:
        typer.echo(f"{r[0]}: {r[1]} ({r[2]}) - {r[3]}")

@app.command("view")
def view_node_cmd(node_id: int):
    """View full details of a node."""
    from db.nodes import get_node
    row = get_node(node_id)
    if not row:
        typer.echo("Node not found.")
        raise typer.Exit()

    fields = [
        "id", "hostname", "cpu_model", "ram_gb", "storage_gb",
        "os_type", "network_types", "access_categories",
        "ip_type", "static_ip", "purpose"
    ]

    for f, v in zip(fields, row, strict=True):
        typer.echo(f"{f}: {v}")

@app.command("edit")
def edit_node_cmd(
    node_id: int,
    field: str = typer.Argument(...),
    value: str = typer.Argument(...)
):
    """Edit a single field of a node."""
    from db.nodes import update_node
    update_node(node_id, field, value)
    typer.echo(f"Updated {field} for node {node_id}.")

@app.command("delete")
def delete_node_cmd(node_id: int):
    """Delete a node."""
    from db.nodes import delete_node
    delete_node(node_id)
    typer.echo(f"Node {node_id} deleted.")


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

from db.connection import get_connection
from db.nodes import insert_node
from db.schema import create_tables
from models.node import Node


def test_insert_node(temp_db):
    # Create schema
    create_tables()

    node = Node(
        hostname="nas1",
        cpu_model="Xeon",
        ram_gb=32,
        storage_gb=8000,
        os_type="Linux",
        access_categories=["SSH", "Web UI"],
        network_types=["Wired"],
        ip_type="Static",
        static_ip="192.168.1.50",
        purpose="NAS"
    )

    insert_node(node)

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT hostname, os_type, static_ip FROM nodes")
    row = cur.fetchone()

    assert row == ("nas1", "Linux", "192.168.1.50")

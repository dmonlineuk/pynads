from .connection import get_connection


def insert_node(node):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO nodes (
            hostname, cpu_model, ram_gb, storage_gb, os_type,
            network_types, access_categories, ip_type, static_ip, purpose
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        node.hostname,
        node.cpu_model,
        node.ram_gb,
        node.storage_gb,
        node.os_type,
        ",".join(node.network_types),
        ",".join(node.access_categories),
        node.ip_type,
        node.static_ip,
        node.purpose
    ))

    conn.commit()
    conn.close()

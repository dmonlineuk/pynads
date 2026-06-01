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

def list_nodes():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, hostname, os_type, purpose FROM nodes")
    rows = cur.fetchall()
    conn.close()
    return rows

def search_nodes(term):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT id, hostname, os_type, purpose
        FROM nodes
        WHERE hostname LIKE ?
    """, (f"%{term}%",))
    rows = cur.fetchall()
    conn.close()
    return rows

def get_node(node_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM nodes WHERE id = ?", (node_id,))
    row = cur.fetchone()
    conn.close()
    return row

def update_node(node_id, field, value):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f"UPDATE nodes SET {field} = ? WHERE id = ?", (value, node_id))
    conn.commit()
    conn.close()

def delete_node(node_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM nodes WHERE id = ?", (node_id,))
    conn.commit()
    conn.close()


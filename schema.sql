-- ============================
--  Network Asset Database
--  Flexible, future‑proof schema
-- ============================

PRAGMA foreign_keys = ON;

-- ----------------------------
--  Nodes (top‑level assets)
-- ----------------------------
CREATE TABLE IF NOT EXISTS nodes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    hostname TEXT NOT NULL,
    cpu_model TEXT,
    ram_gb INTEGER,
    storage_gb INTEGER,
    os_type TEXT,              -- validated in application layer
    network_types TEXT,        -- comma-separated list
    access_categories TEXT,    -- comma-separated list
    ip_type TEXT,              -- DHCP or Static (validated in app)
    static_ip TEXT,            -- only used if ip_type = Static
    purpose TEXT               -- free text
);

-- ----------------------------
--  Components (future expansion)
-- ----------------------------
CREATE TABLE IF NOT EXISTS components (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    node_id INTEGER NOT NULL,
    component_type TEXT,       -- CPU, RAM, PSU, etc.
    description TEXT,
    FOREIGN KEY (node_id) REFERENCES nodes(id)
);

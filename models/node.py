from dataclasses import dataclass


@dataclass
class Node:
    hostname: str
    cpu_model: str
    ram_gb: int
    storage_gb: int
    os_type: str
    access_categories: list[str]
    network_types: list[str]
    ip_type: str
    static_ip: str | None
    purpose: str

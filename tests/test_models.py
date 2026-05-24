from models.node import Node


def test_node_creation():
    node = Node(
        hostname="router1",
        cpu_model="ARMv8",
        ram_gb=2,
        storage_gb=16,
        os_type="Linux",
        access_categories=["Web UI"],
        network_types=["Wired"],
        ip_type="DHCP",
        static_ip=None,
        purpose="router"
    )

    assert node.hostname == "router1"
    assert node.os_type == "Linux"
    assert "Web UI" in node.access_categories

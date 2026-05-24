from db.nodes import insert_node
from models.node import Node
from utils.validators import validate_ip, validate_os


def prompt_list(prompt, options):
    print(prompt)
    for i, opt in enumerate(options, 1):
        print(f"{i}) {opt}")
    choices = input("Select (comma-separated): ")
    idx = [int(x.strip()) - 1 for x in choices.split(",")]
    return [options[i] for i in idx]

def create_node_interactively():
    hostname = input("Hostname: ")
    cpu = input("CPU model: ")
    ram = int(input("RAM (GB): "))
    storage = int(input("Storage (GB): "))

    os_type = input("OS (Linux/Windows): ")
    validate_os(os_type)

    access = prompt_list(
        "Access categories:",
        ["Physical Terminal", "Web UI", "SSH", "RDP Remote"]
    )
    network = prompt_list("Network types:", ["Wired", "Wireless"])

    ip_type = input("IP type (DHCP/Static): ")
    static_ip = None
    if ip_type == "Static":
        static_ip = input("Static IP: ")
    validate_ip(ip_type, static_ip)

    purpose = input("Purpose: ")

    node = Node(
        hostname, cpu, ram, storage, os_type,
        access, network, ip_type, static_ip, purpose
    )

    insert_node(node)
    print("Node saved.")

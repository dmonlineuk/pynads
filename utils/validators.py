def validate_os(os_type):
    allowed = ["Linux", "Windows"]
    if os_type not in allowed:
        raise ValueError(f"OS must be one of {allowed}")

def validate_ip(ip_type, static_ip):
    if ip_type == "Static" and not static_ip:
        raise ValueError("Static IP must be provided for ip_type='Static'")

import pytest

from utils.validators import validate_ip, validate_os


def test_validate_os_valid():
    validate_os("Linux")
    validate_os("Windows")

def test_validate_os_invalid():
    with pytest.raises(ValueError):
        validate_os("MacOS")

def test_validate_ip_static_requires_address():
    with pytest.raises(ValueError):
        validate_ip("Static", None)

def test_validate_ip_dhcp_allows_no_address():
    validate_ip("DHCP", None)

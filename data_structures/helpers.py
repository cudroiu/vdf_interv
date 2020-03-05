"""
This module contains helper functions.
"""
from sys import version_info
import re
import ipaddress


def str_to_ipaddress(address):
    """
    This function converts an IP address expressed as a string to an ipaddress.IPv4Address object.
    """
    if version_info.major == 2:
        addr = ipaddress.IPv4Address(address.decode())
    elif version_info.major == 3:
        addr = ipaddress.IPv4Address(address)

    return addr


def validate_address(address, ipv4_network):
    """
    This function validates a particular Entry object.
    It returns True if the address is valid and False otherwise.
    """
    result = True
    try:
        addr = str_to_ipaddress(address)
        if addr not in ipv4_network:
            result = False
    except Exception:
        result = False

    return result


def validate_cluster_name(cluster_name, datacenter_name):
    """
    This function validates a cluster.
    It returns True if the cluster is valid and False otherwise.
    """
    result = True
    if not re.search(r'^' + re.escape(datacenter_name[0:3].upper()) + r'-\d{1,3}$', cluster_name):
        result = False

    return result

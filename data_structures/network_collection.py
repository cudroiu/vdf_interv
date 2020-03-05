"""
Module data_structures/network_collections.py
"""

from sys import version_info
import ipaddress
from .entry import Entry


class NetworkCollection:
    """
    Class NetworkCollection
    """
    def __init__(self, ipv4_network, raw_entry_list):
        """
        Constructor for NetworkCollection data structure.

        self.ipv4_network -> ipaddress.IPv4Network
        self.entries -> list(Entry)
        """
        self.ipv4_network = ipaddress.IPv4Network(ipv4_network)
        self.entries = [Entry(e["address"], e["available"], e["last_used"]) for e in raw_entry_list]

    def remove_invalid_records(self):
        """
        Removes invalid objects from the entries list.
        """
        self.entries[:] = [e for e in self.entries if self.validate_address(e)]

    def validate_address(self, entry):
        """
        This function validates a particular Entry object.
        It returns True if the address is valid and False otherwise.
        """
        result = True
        try:
            if version_info.major == 2:
                addr = ipaddress.IPv4Address(entry.address.decode())
            elif version_info.major == 3:
                addr = ipaddress.IPv4Address(entry.address)
            if addr not in self.ipv4_network:
                result = False
        except Exception:
            result = False

        return result

    def sort_records(self):
        """
        Sorts the list of associated entries in ascending order.
        DO NOT change this method, make the changes in entry.py :)
        """

        self.entries = sorted(self.entries, key=lambda entry: entry.address)

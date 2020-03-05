"""
Module data_structures/network_collections.py
"""

import ipaddress
from .entry import Entry
from .helpers import validate_address


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
        self.entries[:] = [e for e in self.entries if validate_address(e.address, self.ipv4_network)]

    def sort_records(self):
        """
        Sorts the list of associated entries in ascending order.
        DO NOT change this method, make the changes in entry.py :)
        """
        self.entries = sorted(self.entries)

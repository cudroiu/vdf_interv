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
        self.entries = EntryIterator(raw_entry_list)

    def remove_invalid_records(self):
        """
        Removes invalid objects from the entries list.
        """
        self.entries = ValidEntryIterator(self.entries, self.ipv4_network)

    def sort_records(self):
        """
        Sorts the list of associated entries in ascending order.
        DO NOT change this method, make the changes in entry.py :)
        """
        self.entries = sorted(self.entries)


class EntryIterator(object):
    def __init__(self, input_list):
        self.input_list = input_list

    def __iter__(self):
        for entry in self.input_list:
            yield Entry(entry["address"], entry["available"], entry["last_used"])


class ValidEntryIterator(object):
    def __init__(self, it, ipv4_network):
        self.it = it
        self.ipv4_network = ipv4_network

    def __iter__(self):
        for entry in self.it:
            if validate_address(entry.address, self.ipv4_network):
                yield entry


"""
Module data_structures.cluster.py
"""

from .network_collection import NetworkCollection


class Cluster:
    """
    Class Cluster
    """
    def __init__(self, name, network_dict, security_level):
        """
        Constructor for Cluster data structure.

        self.name -> str
        self.security_level -> int
        self.networks -> list(NetworkCollection)
        """
        self.name = str(name)
        self.security_level = int(security_level)
        self.networks = (NetworkCollection(network, raw_entry_list)
                         for network, raw_entry_list in network_dict.items())

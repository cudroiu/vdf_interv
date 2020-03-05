"""
Module data_structures/datacenter.py
"""
from .cluster import Cluster
from .helpers import validate_cluster_name


class Datacenter:
    """
    Class Datancenter
    """
    def __init__(self, name, cluster_dict):
        """
        Constructor for Datacenter data structure.

        self.name -> str
        self.clusters -> list(Cluster)
        """
        self.name = str(name)
        self.clusters = [Cluster(k, v["networks"], v["security_level"])
                         for k, v in cluster_dict.items()]

    def remove_invalid_clusters(self):
        """
        Removes invalid objects from the clusters list.
        """
        self.clusters[:] = [c for c in self.clusters if validate_cluster_name(c.name, self.name)]

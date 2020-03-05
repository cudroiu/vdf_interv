"""
Module data_structures/datacenter.py
"""
import re
from .cluster import Cluster


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
        self.clusters[:] = [c for c in self.clusters if self.validate_cluster(c)]

    def validate_cluster(self, cluster):
        """
        This function validates a cluster.
        It returns True if the cluster is valid and False otherwise.
        """
        result = True
        if not re.search(r'^' + re.escape(self.name[0:3].upper()) + r'-\d{1,3}$', cluster.name):
            result = False

        return result

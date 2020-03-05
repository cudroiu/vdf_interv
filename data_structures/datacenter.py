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
        self.clusters = ClusterIterator(cluster_dict)

    def remove_invalid_clusters(self):
        """
        Removes invalid objects from the clusters list.
        """
        self.clusters = ValidClusterIterator(self.clusters, self.name)


class ClusterIterator(object):
    def __init__(self, input_dict):
        self.input_dict = input_dict

    def __iter__(self):
        for cluster, data in self.input_dict.items():
            yield Cluster(cluster, data["networks"], data["security_level"])


class ValidClusterIterator(object):
    def __init__(self, it, dc_name):
        self.it = it
        self.dc_name = dc_name

    def __iter__(self):
        for cluster in self.it:
            if validate_cluster_name(cluster.name, self.dc_name):
                yield cluster

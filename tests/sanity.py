import unittest
import json
import re
from data_structures.network_collection import NetworkCollection
from data_structures.cluster import Cluster
from data_structures.datacenter import Datacenter


class TestMockIo(unittest.TestCase):
    def setUp(self):
        with open('response.json') as f:
            self.data = json.load(f)

        self.datacenters = [
                Datacenter(key, value)
                for key, value in self.data.items()
                ]

    def test_valid_cluster_name(self):
        result = True
        for datacenter in self.datacenters:
            datacenter.remove_invalid_clusters()
            for cluster in datacenter.clusters:
                if not re.match(r'^' + re.escape(datacenter.name[0:3].upper()) + r'-\d{1,3}$', cluster.name):
                    result = False
        self.assertTrue(result)

    def test_valid_ipv4_addr(self):
        total_valid_ip = 0
        for datacenter in self.datacenters:
            for cluster in datacenter.clusters:
                for network in cluster.networks:
                    network.remove_invalid_records()
                    valid_ip = len(network.entries)
                    total_valid_ip += valid_ip
        self.assertEqual(total_valid_ip, 16)

    def test_entry_order(self):
        result = True
        for datacenter in self.datacenters:
            for cluster in datacenter.clusters:
                for network in cluster.networks:
                    network.remove_invalid_records()
                    network.sort_records()
                    for i, entry in enumerate(network.entries[1:]):
                        if entry < network.entries[i]:
                            result = False

        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()

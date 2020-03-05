from time import sleep
import requests
from data_structures.datacenter import Datacenter

URL = "http://www.mocky.io/v2/5e539b332e00007c002dacbe"


def get_data(url, max_retries=5, delay_between_retries=1):
    """
    Fetch the data from http://www.mocky.io/v2/5e539b332e00007c002dacbe
    and return it as a JSON object.
    Args:
        url (str): The url to be fetched.
        max_retries (int): Number of retries.
        delay_between_retries (int): Delay between retries in seconds.
    Returns:
        data (dict)
    """
    result = {}
    retry_cnt = 0
    while retry_cnt < max_retries:
        retry_cnt += 1
        try:
            response = requests.get(url=url, timeout=10)
            if response and response.status_code == 200:
                result = response.json()
                break
            elif response.status_code != 200:
                raise Exception("Expected status code 200, but received %d" % response.status_code)
        except Exception:
            sleep(delay_between_retries)
            continue

    return result


def main():
    """
    Main entry to our program.
    """
    
    print("Retrieving data from API")
    data = get_data(URL)

    if not data:
        raise ValueError('No data to process')

    print("Successfully retrieved data from API")
    print("Instantiating elements")
    datacenters = [
        Datacenter(key, value)
        for key, value in data.items()
    ]
    print("Successfully instantiated elements")

    for d in datacenters:
        print("Removing invalid clusters from datacenter {}".format(d.name))
        d.remove_invalid_clusters()
        print("Found {} valid clusters: {}".format(str(len(list(d.clusters))), ', '.join((cluster.name for cluster in d.clusters))))
        for c in d.clusters:
            for n in c.networks:
                print("Removing invalid records for network {}, cluster {}".format(str(n.ipv4_network), c.name))
                n.remove_invalid_records()
                print("Found {} valid records: {}".format(str(len(list(n.entries))), ', '.join([e.address for e in n.entries])))
                print("Sorting records by IPv4 address")
                n.sort_records()
                print("Successfully sorted records by IPv4 address: {}".format(', '.join([e.address for e in n.entries])))


if __name__ == '__main__':
    main()

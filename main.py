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

    data = get_data(URL)

    if not data:
        raise ValueError('No data to process')

    datacenters = [
        Datacenter(key, value)
        for key, value in data.items()
    ]

    for d in datacenters:
        d.remove_invalid_clusters()
        for c in d.clusters:
            for n in c.networks:
                n.remove_invalid_records()
                n.sort_records()


if __name__ == '__main__':
    main()

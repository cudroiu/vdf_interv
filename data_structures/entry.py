"""
data_structures.entry.py
"""

import datetime
from .helpers import str_to_ipaddress


class Entry:
    """
    Class Entry
    """
    def __init__(self, address, available, last_used):
        """
        Constructor for Entry data structure.

        self.address -> str
        self.available -> bool
        self.last_used -> datetime
        """
        self.address = str(address)
        self.available = True if available else False
        self.last_used = datetime.datetime.strptime(last_used, '%d/%m/%y %H:%M:%S')

    def __lt__(self, other):
        """
        This function compares 2 ip addresses by their decimal values.
        """
        return int(str_to_ipaddress(self.address)) < int(str_to_ipaddress(other.address))

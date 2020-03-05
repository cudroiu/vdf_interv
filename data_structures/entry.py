"""
data_structures.entry.py
"""

import datetime


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

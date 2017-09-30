"""
python
 "Ping two times, (one is for the ARP to sync) if there is a replay return true, else return false.\n")
"""

import os


def ping(address):
    if os.system("ping " + address + " -c 2") == 0:
        return True
    else:
        return False

import os
def ping(address):

    response = os.system("ping " + address + " -c 2")
    if response == 0:
        return True
    else:
        return False

"""
Created by: Matthew O'Malley-Nichols
Code based off of: https://zeromq.org/languages/python/
Modified by: Brendan Cook Date: 05/17/23
"""

import zmq

class REQSocket():
    def __init__(self, connection = "tcp://localhost:5555"):
        self.context = zmq.Context()
        # Using REQ and REP socket pair
        self.socket = self.context.socket(zmq.REQ)
        self.socket.connect(connection)

SOCKET = REQSocket().socket


def send_sql_request(request):
    """
    Sends queries to server and returns the return message
    """
    
    # Unicode not allowed
    SOCKET.send_string(request)
    if request == "q": return False

    return_message = SOCKET.recv_string()


    return return_message

#!/usr/bin/python3
import subprocess as sub
import socket

class server():
    def __init__(self, new_logger):
        self.debugging = False
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.logger = new_logger

    # Assigns a local protocal address to a certain socket, in this case 1234
    #       What is the difference between a socket and a port?
    #           Sockets are parts of ports, port numbers are parts of sockets
    #           A port is a physical endpoint on a piece of hardware
    #           A socket is defined by the combination of a network address and port identifier, 0.0.0.0:321
    def bind(self):
        # For local testing
        self.s.bind(("127.0.0.1", 22))
        # For testing across the network (*.249 is Nathan's IP on the HPU network)
        # self.s.bind(("10.240.224.249", 22))

    # Specifies the maximum number of queued connections to our "server"
    def listen(self):
        self.s.listen(5)

    # Continuously runs and accepts connections to the 4444 socket on the XPS-15 host
    def start(self):
        while True:
            clientsocket, address = self.s.accept()
            self.logger.handle_request(address)
            print("Attempting to spin up docker container")
            cont_name = "ssh_service"
            cont_action = "start"
            sub.run(["docker", cont_action, cont_name])
            

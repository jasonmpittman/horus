#!/usr/bin/python3
import subprocess as sub
import socket


class horus_server():
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Assigns a local protocal address to a certain socket, in this case 1234
    #       What is the difference between a socket and a port?
    #           Sockets are parts of ports, port numbers are parts of sockets
    #           A port is a physical endpoint on a piece of hardware
    #           A socket is defined by the combination of a network address and port identifier, 0.0.0.0:321
    def bind(self):
        self.s.bind(("10.240.224.249", 22))

    # Specifies the maximum number of queued connections to our "server"
    def listen(self):
        self.s.listen(5)

    # Continuously runs and accepts connections to the 4444 socket on the XPS-15 host
    def start(self):
        while True:
            clientsocket, address = self.s.accept()
            print(f"Connection from {address} has been established!")
            clientsocket.send(bytes("Welcome to the honeypot, bitch!", "utf-8"))
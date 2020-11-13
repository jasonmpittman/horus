#!/usr/bin/python3

import socket

# Creates the socket and defines traffic to be a stream of data
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connects to the socket located at the network address 127.0.0.1 behind the hostname XPS-15 through
s.connect((socket.gethostname(), 22))

msg = s.recv(1024)
print("The message received was:")
print("\t", msg.decode("utf-8"))
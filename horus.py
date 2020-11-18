#!/usr/bin/python3

import horus_server
import horus_logger

class Horus():
  def __init__(self):
    self.debugging = True
    self.logger = horus_logger.logger()
    self.server = horus_server.server(self.logger)

Ra = Horus()
if(Ra.debugging):
  print("Initialized the Horus object")
Ra.server.bind()
if(Ra.debugging):
  print("Successfully bound Horus object to socket")
Ra.server.listen()
if(Ra.debugging):
  print("Successfully initialized the queue limit")
  print("Starting entertainment of requests...")
  print("")
Ra.server.start()
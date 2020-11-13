#!/usr/bin/python3

import horus_server

class Horus():
  def __init__(self):
    self.server = horus_server.horus_server()

Ra = Horus()
Ra.server.bind()
Ra.server.listen()
Ra.server.start()
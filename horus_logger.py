#!/usr/bin/python3
from datetime import date, datetime

class logger():
  def __init__(self):
    self.debugging = True
    self.path = "./logging/"

  def new_connection(self, connection_information):
    current_time = datetime.utcnow()
    if(self.debugging):
      print("New connection at %s from: %s:%s" %(current_time, connection_information[0], connection_information[1]))
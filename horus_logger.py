#!/usr/bin/python3
from datetime import date, datetime
import sqlite3
from sqlite3 import Error
import uuid

class logger():
  def __init__(self):
    self.debugging = True
    self.database = "horus.db"
    self.create_table_value = """ CREATE TABLE IF NOT EXISTS adversaries (
                                    id text PRIMARY KEY,
                                    ip_address text NOT NULL,
                                    port text NOT NULL,
                                    date_arrived text NOT NULL,
                                    times_visited integer NOT NULL
                                  );
                              """
    self.conn = None
    self.sql = ''' INSERT INTO adversaries(id,ip_address,port,date_arrived,times_visited)
                   VALUES(?,?,?,?,?) '''
    self.cur = None

  """
    Precondition: n/A
    Postcondition: Creates the table within the sql database
  """
  def create_table(self):
    try:
      c = self.conn.cursor()
      c.execute(self.create_table_value)
    except Error as e:
      print(e)

  """
    Precondition: n/A
    Postcondition: Creates connection to the sql database
      specified by default in the init.
  """
  def create_connection(self):
    try:
      self.conn = sqlite3.connect(self.database)
    except Error as e:
      print(e)

  """
    Precondition: The information of a new connection
    Postcondition: Creates the database cursor, executes the sql 
      command with the inputted information, commits the sql command
      to the database and returns the last row id.
  """
  def insert_information(self, information):
    self.cur = self.conn.cursor()
    self.cur.execute(self.sql, information)
    self.conn.commit()
    return self.cur.lastrowid
    
  """
    Precondition: The connection information
    Postcondition: Gets the current time, formats the info for SQL insertion,
      initializes a connection interface to the database, creates the database
      if it does not already exist, and inserts the information. Lastly, we increment
      the number of values within the database because this serves as the primary key
      for each record in the database.
  """
  def handle_request(self, connection_information):
    current_time = datetime.utcnow()
    unique_id = str(uuid.uuid4())
    if(self.debugging):
      print("Unique identifier is: ", unique_id)
    info = (unique_id, connection_information[0], connection_information[1], current_time, 1)
    self.create_connection()
    if(self.debugging):
      print("Successfully created connection with conn connection of: ", self.conn)
    self.create_table()
    if(self.debugging):
      print("Successfully created table with the following query:")
      print(self.create_table_value)
    self.insert_information(info)
    if(self.debugging):
      print("Inserted the information with the query:", self.sql)
    if(self.debugging):
      print("New connection at %s from: %s:%s" %(current_time, connection_information[0], connection_information[1]))
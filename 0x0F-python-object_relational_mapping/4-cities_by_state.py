#!/usr/bin/python3

import MySQLdb
import sys

'''script that list cities from the database'''

if __name__ == "__main__":
    try:
      db = MySQLdb.connect(host = "localhost", user = sys.argv[1],\
passwd = sys.argv[2], port = 3306, db = sys.argv[3])
    except MySQLdb.Error:
      print("error connecting to database")
    cur = db.cursor()
    try:
      cur.execute("SELECT cities.id, cities.name, states.name\
 FROM cities INNER JOIN states ON cities.state_id = states.id\
 ORDER BY cities.id ASC")
      results = cur.fetchall()
      for result in results:
          print(result)
    except MySQLdb.Error:
      print("error in query the database")
    cur.close()
    db.close()    
    

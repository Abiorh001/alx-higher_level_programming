#!/usr/bin/python3

import MySQLdb
import sys

'''script that list states from the database
   where name start from N
'''

if __name__ == "__main__":
    try:
      db = MySQLdb.connect(host = "localhost", user = sys.argv[1],\
passwd = sys.argv[2], port = 3306, db = sys.argv[3])
    except MySQL.ERROR:
      print("error connecting to database")
    cur = db.cursor()
    try:
      cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC")
      results = cur.fetchall()
      for result in results:
          print(result)
    except MySQL.ERROR:
      print("error in query the database")
    cur.close()
    db.close()    
    

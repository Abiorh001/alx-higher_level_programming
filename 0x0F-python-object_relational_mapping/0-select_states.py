#!/usr/bin/python3
""" script that list states from the database """
import MySQldb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
         user=sys.argv[1],
         passwd=sys.argv[2],
         port=3306,
         db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    results = cur.fetchall()
    for result in results:
        print(result)
    cur.close()
    db.close()

#!/usr/bin/python3
'''script that list states from the database'''
import MySQldb
import sys

if __name__ == "__main__":
    try:
        db = MySQLdb.connect(host="localhost",
                             user=sys.argv[1],
                             passwd=sys.argv[2],
                             port=3306, db=sys.argv[3])
    except MySQL.ERROR:
        print("error connecting to database")
    cur = db.cursor()
    try:
        cur.execute("SELECT * FROM states ORDER BY states.id ASC")
        results = cur.fetchall()
        for result in results:
            print(result)
    except MySQL.ERROR:
        print("error in query the database")
    cur.close()
    db.close()

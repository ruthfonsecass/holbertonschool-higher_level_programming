#!/usr/bin/python3
"""lists all states with a name starting with N"""

import MySQLdb
import sys

if __name__ == "__main__":
    user_db = sys.argv[1]
    passwd_db = sys.argv[2]
    dbname= sys.argv[3]

    db = MySQLdb.connect(
        host="localhost", user=user_db, passwd=passwd_db, db=dbname, port=3306
    )

    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE '%N' ORDER BY id ASC")

    results = cur.fetchall()
    for state in results:
        print(state)

    db.close()
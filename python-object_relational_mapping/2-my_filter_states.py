#!/usr/bin/python3
"""lists all states with a name starting with N"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        username=sys.argv[1]
        passwd=sys.argv[2]
        db=sys.argv[3]
    )

    cur = db.cursor()

    query = "SELECT * FROM states WHERE name LIKE '%N' ORDER BY id ASC"

    cur.execute(query, )

    results = cur.fetchall()

    for state in results:
        print(state)

    db.close()

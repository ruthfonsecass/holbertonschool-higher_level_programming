#!/usr/bin/python3
"""lists all states with a name starting with N"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    passwd_db = sys.argv[2]
    dbname= sys.argv[3]
    state_name = sys.argv[4]


    db = MySQLdb.connect(
        host="localhost", user=username, passwd=passwd_db, db=dbname, port=3306
    )

    cur = db.cursor()

    query = "SELECT * FROM states WHERE name LIKE '%N' ORDER BY id ASC"

    cur.execute(query, (staty_name,))

    results = cur.fetchall()

    
    for state in results:
        print(state)

    db.close()
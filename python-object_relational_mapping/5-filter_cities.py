import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()
    cursor.execute(
         """
        SELECT cities.name
        FROM cities
        JOIN states
        ON states.id = cities.state_id
        WHERE states.name LIKE BINARY %s
        ORDER BY cities.id
        """, (sys.argv[4],)
    )

    rows = cursor.fetchall()

    city_names = []
    for row in rows:
        city_names.append(row[0])
    string = ", ".join(city_names)
    print(string)

    cursor.close()
    db.close()
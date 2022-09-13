#!/usr/bin/python3
"""
lists all cities from the database
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    user, password, database, arg = argv[1], argv[2], argv[3], argv[4]
    db = MySQLdb.connect(
        host='localhost', port=3306,
        user=user, password=password,
        database=database
    )
    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name(SELECT states.name FROM states WHERE name = 'Texas')
                FROM cities
                JOIN states ON cities.state_id = states.id
                ORDER BY cities.id ASC""")
    for item in cur.fetchall():
        print(item)

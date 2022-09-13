#!/usr/bin/python3
"""
lists from the database hbtn_0e_0_usa
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
    cur.execute(
            """SELECT * FROM states WHERE name LIKE '{:s}'
                ORDER BY id ASC""".format(arg))
    for item in cur.fetchall():
        print(item)

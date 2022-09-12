#!/usr/bin/python3

import MySQLdb
from sys import argv

""" script that lists all states from
the database """


if __name__ == '__main__':
    user, password, database = argv[1], argv[2], argv[3]
    db = MySQLdb.connect(
                                            host='localhost', port=3306,
                                            user=user, password=password,
                                            database=database
                                            )

    cur = db.cursor()

    cur.execute("SELECT * FROM states")

    db = cur.fetchall()

    for item in db:
        print(item)

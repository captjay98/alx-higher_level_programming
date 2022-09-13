#!/usr/bin/python3


import MySQLdb
from sys import argv

"""
lists all states with starting name with N
from the database hbtn_0e_0_usa
"""
if __name__ == "__main__":
    user, password, database = argv[1], argv[2], argv[3]
    db = MySQLdb.connect(
                                            host='localhost', port=3306,
                                            user=user, password=password,
                                            database=database
                                            )
    cur = db.cursor()
    cur.execute(
            "SELECT * FROM states WHERE name LIKE\
                BINARY 'N%' ORDER BY id ASC")
    for item in cur.fetchall():
        print(item)
